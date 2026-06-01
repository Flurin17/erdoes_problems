#!/usr/bin/env python3
"""Count and sample-classify outside-cover shells by side-label word triples.

This is an experimental quotient for the remaining `gamma=2alpha` boundary
shells.  It uses the same count-only local-cover factorization as
`gamma_2alpha_overlap_remainder_inventory.py`, but aggregates uncovered shells
by `(left label word, right label word, base label word)` and then classifies a
bounded number of representative demands from those word groups.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import refined_survivors_for_n, viable_free_x_representations, viable_x_representations  # noqa: E402
from gamma_2alpha_boundary_transition_demand import BoundaryDemand  # noqa: E402
from gamma_2alpha_endpoint_automaton import alpha_corner, apex_corner  # noqa: E402
from gamma_2alpha_low_mixed_shell_census import paths_by_endpoint_and_mixed  # noqa: E402
from gamma_2alpha_overlap_cover import (  # noqa: E402
    DEFAULT_PAIR_TEXT,
    KPolygon,
    kscale_polygon,
    parse_pair,
    qdenominator_scale,
    side_tile_polygon,
    valid_pairs_for_lengths,
)
from gamma_2alpha_overlap_remainder_inventory import (  # noqa: E402
    label_word,
    path_profile,
    profile_text,
    word_signature,
)
from gamma_2alpha_residual_capped_census import classify_shell, demand_key  # noqa: E402


BoundaryPath = tuple
Triple = tuple[int, int, int]
WordData = tuple[int, BoundaryPath]


def overlap(left: KPolygon, right: KPolygon) -> bool:
    if exact.kbbox_disjoint(exact.kbbox(left), exact.kbbox(right)):
        return False
    if exact.ksame_triangle(left, right):
        return False
    return exact.kpositive_overlap(left, right)


def mixed(path) -> int:
    return sum((left.side == "c") != (right.side == "c") for left, right in zip(path, path[1:]))


def add_rep(reps: list[BoundaryDemand], demand: BoundaryDemand, limit: int) -> None:
    if len(reps) < limit:
        reps.append(demand)


def parse_word_signature(signature: str) -> tuple[str, str, str]:
    parts = signature.split()
    if len(parts) != 3 or not all(part[1] == "=" for part in parts):
        raise ValueError(signature)
    return parts[0][2:], parts[1][2:], parts[2][2:]


def census_survivor(
    survivor,
    *,
    min_total_mixed: int,
    max_total_mixed: int,
    reps_per_word: int,
    skip_classified_words: int,
    max_classified_words: int,
    classification_mode: str,
    quotient: str,
    progress_every: int,
    example_words_per_status: int,
) -> dict:
    radicand = exact.field_radicand(survivor)
    if radicand is None:
        raise ValueError("quadratic field unavailable")
    exact.RADICAND = radicand
    pairs = tuple(parse_pair(text) for text in DEFAULT_PAIR_TEXT)

    candidate = survivor.candidate
    bounded_reps = viable_x_representations(candidate)
    free_reps = viable_free_x_representations(candidate)
    base_reps = survivor.y_representations
    x_reps = set(bounded_reps + free_reps)
    active_pairs = valid_pairs_for_lengths(
        pairs,
        max(sum(rep) for rep in x_reps),
        max(sum(rep) for rep in base_reps),
    )
    indexes = {
        rep: paths_by_endpoint_and_mixed(rep)
        for rep in set(bounded_reps + free_reps + base_reps)
    }
    paths_by_rep_and_word = {}
    for rep, index in indexes.items():
        by_word: dict[str, list[BoundaryPath]] = defaultdict(list)
        for group in index.values():
            for path in group:
                by_word[label_word(path)].append(path)
        paths_by_rep_and_word[rep] = {word: tuple(paths) for word, paths in by_word.items()}
    x_paths = tuple(path for rep in x_reps for group in indexes[rep].values() for path in group)
    base_paths_all = tuple(path for rep in base_reps for group in indexes[rep].values() for path in group)
    needed_positions = {
        "L": sorted({pair.side_position for pair in active_pairs if pair.side == "L"}),
        "R": sorted({pair.side_position for pair in active_pairs if pair.side == "R"}),
        "B": sorted({pair.base_position for pair in active_pairs}),
    }

    q_polygons = {}
    all_polygons = []
    for side_name, paths in (("L", x_paths), ("R", x_paths), ("B", base_paths_all)):
        for position in needed_positions[side_name]:
            for path in paths:
                if position > len(path):
                    continue
                polygon = side_tile_polygon(
                    survivor,
                    side_name=side_name,
                    path=path,
                    position=position,
                    radicand=radicand,
                )
                q_polygons[(side_name, position, path)] = polygon
                all_polygons.append(polygon)
    scale = qdenominator_scale(all_polygons)
    polygons = {key: kscale_polygon(polygon, scale) for key, polygon in q_polygons.items()}
    overlap_cache: dict[tuple[KPolygon, KPolygon], bool] = {}
    side_group_cache: dict[tuple[str, tuple[BoundaryPath, ...], tuple[KPolygon, ...]], dict[str, WordData]] = {}

    base_positions = needed_positions["B"]

    def base_feature(path) -> tuple[KPolygon, ...]:
        return tuple(polygons[("B", position, path)] for position in base_positions)

    def base_polygon(feature: tuple[KPolygon, ...], position: int) -> KPolygon:
        return feature[base_positions.index(position)]

    def overlaps_cached(left: KPolygon, right: KPolygon) -> bool:
        key = (left, right)
        value = overlap_cache.get(key)
        if value is None:
            value = overlap(left, right)
            overlap_cache[key] = value
        return value

    def demand_covered(demand: BoundaryDemand) -> bool:
        for pair in active_pairs:
            side_path = demand.left_path if pair.side == "L" else demand.right_path
            side_polygon = polygons[(pair.side, pair.side_position, side_path)]
            base_polygon_value = polygons[("B", pair.base_position, demand.base_path)]
            if overlaps_cached(side_polygon, base_polygon_value):
                return True
        return False

    def path_quotient_key(side_name: str, path: BoundaryPath) -> str:
        if quotient == "word":
            return label_word(path)
        if quotient == "profile":
            return profile_text(path_profile(path, tuple(needed_positions[side_name])))
        raise ValueError(quotient)

    def group_signature(left_key: str, right_key: str, base_key: str) -> str:
        if quotient == "word":
            return word_signature(left_key, right_key, base_key)
        if quotient == "profile":
            return f"L[{left_key}] R[{right_key}] B[{base_key}]"
        raise ValueError(quotient)

    def side_good_groups(
        side_name: str,
        paths: tuple[BoundaryPath, ...],
        feature: tuple[KPolygon, ...],
    ) -> dict[str, WordData]:
        key = (side_name, paths, feature)
        cached = side_group_cache.get(key)
        if cached is not None:
            return cached
        relevant = tuple(pair for pair in active_pairs if pair.side == side_name)
        counts: Counter[str] = Counter()
        reps: dict[str, BoundaryPath] = {}
        for path in paths:
            bad = any(
                overlaps_cached(
                    polygons[(side_name, pair.side_position, path)],
                    base_polygon(feature, pair.base_position),
                )
                for pair in relevant
            )
            if bad:
                continue
            quotient_key = path_quotient_key(side_name, path)
            counts[quotient_key] += 1
            reps.setdefault(quotient_key, path)
        cached = {quotient_key: (count, reps[quotient_key]) for quotient_key, count in counts.items()}
        side_group_cache[key] = cached
        return cached

    quotient_counts: Counter[str] = Counter()
    quotient_reps: dict[str, list[BoundaryDemand]] = defaultdict(list)
    total_uncovered = 0
    endpoint_groups = 0

    orientations = [("left", bounded_reps, free_reps)]
    if bounded_reps != free_reps:
        orientations.append(("right", free_reps, bounded_reps))

    def classify_word_exhaustively(signature: str) -> Counter[str]:
        left_word, right_word, base_word = parse_word_signature(signature)
        statuses: Counter[str] = Counter()
        seen_demands = set()
        for short_side, left_reps, right_reps in orientations:
            for left_rep in left_reps:
                left_paths = paths_by_rep_and_word[left_rep].get(left_word, ())
                if not left_paths:
                    continue
                for right_rep in right_reps:
                    right_paths = paths_by_rep_and_word[right_rep].get(right_word, ())
                    if not right_paths:
                        continue
                    for base_rep in base_reps:
                        base_paths = paths_by_rep_and_word[base_rep].get(base_word, ())
                        if not base_paths:
                            continue
                        for left_path in left_paths:
                            left_mixed = mixed(left_path)
                            for right_path in right_paths:
                                if not apex_corner(left_path[-1], right_path[0]):
                                    continue
                                right_mixed = mixed(right_path)
                                for base_path in base_paths:
                                    total_mixed = left_mixed + right_mixed + mixed(base_path)
                                    if not min_total_mixed <= total_mixed <= max_total_mixed:
                                        continue
                                    if not alpha_corner(right_path[-1], base_path[0]):
                                        continue
                                    if not alpha_corner(base_path[-1], left_path[0]):
                                        continue
                                    demand = BoundaryDemand(
                                        short_side=short_side,
                                        left_rep=left_rep,
                                        right_rep=right_rep,
                                        base_rep=base_rep,
                                        mixed_transitions=total_mixed,
                                        left_path=left_path,
                                        right_path=right_path,
                                        base_path=base_path,
                                    )
                                    key = demand_key(demand)
                                    if key in seen_demands:
                                        continue
                                    seen_demands.add(key)
                                    if demand_covered(demand):
                                        continue
                                    statuses[classify_shell(survivor, demand, radicand).status] += 1
        return statuses

    started = time.monotonic()
    for short_side, left_reps, right_reps in orientations:
        for left_rep in left_reps:
            for right_rep in right_reps:
                for base_rep in base_reps:
                    for left_key, left_paths in indexes[left_rep].items():
                        left_first, left_last, left_mixed = left_key
                        for right_key, right_paths in indexes[right_rep].items():
                            right_first, right_last, right_mixed = right_key
                            if left_mixed + right_mixed > max_total_mixed:
                                continue
                            if not apex_corner(left_last, right_first):
                                continue
                            for base_key, base_paths in indexes[base_rep].items():
                                base_first, base_last, base_mixed = base_key
                                total_mixed = left_mixed + right_mixed + base_mixed
                                if not min_total_mixed <= total_mixed <= max_total_mixed:
                                    continue
                                if not alpha_corner(right_last, base_first):
                                    continue
                                if not alpha_corner(base_last, left_first):
                                    continue
                                endpoint_groups += 1

                                base_counts: Counter[tuple[tuple[KPolygon, ...], str]] = Counter()
                                base_rep_by_key: dict[tuple[tuple[KPolygon, ...], str], BoundaryPath] = {}
                                for base_path in base_paths:
                                    key = (base_feature(base_path), path_quotient_key("B", base_path))
                                    base_counts[key] += 1
                                    base_rep_by_key.setdefault(key, base_path)

                                for (feature, base_key), base_count in base_counts.items():
                                    left_groups = side_good_groups("L", left_paths, feature)
                                    right_groups = side_good_groups("R", right_paths, feature)
                                    if not left_groups or not right_groups:
                                        continue
                                    base_path = base_rep_by_key[(feature, base_key)]
                                    for left_key, (left_count, left_path) in left_groups.items():
                                        for right_key, (right_count, right_path) in right_groups.items():
                                            signature = group_signature(left_key, right_key, base_key)
                                            multiplicity = base_count * left_count * right_count
                                            quotient_counts[signature] += multiplicity
                                            total_uncovered += multiplicity
                                            add_rep(
                                                quotient_reps[signature],
                                                BoundaryDemand(
                                                    short_side=short_side,
                                                    left_rep=left_rep,
                                                    right_rep=right_rep,
                                                    base_rep=base_rep,
                                                    mixed_transitions=total_mixed,
                                                    left_path=left_path,
                                                    right_path=right_path,
                                                    base_path=base_path,
                                                ),
                                                reps_per_word,
                                            )
        if progress_every and len(quotient_counts) and len(quotient_counts) % progress_every == 0:
            elapsed = time.monotonic() - started
            print(
                f"    counted {quotient}_groups={len(quotient_counts)} uncovered={total_uncovered} "
                f"elapsed={elapsed:.1f}s",
                flush=True,
            )

    status_group_counts: Counter[str] = Counter()
    status_weight_counts: Counter[str] = Counter()
    status_signatures: Counter[tuple[tuple[str, int], ...]] = Counter()
    example_words: dict[str, list[dict[str, object]]] = defaultdict(list)
    mixed_example_words: list[dict[str, object]] = []
    mixed_status_words = 0
    word_count_mismatches: list[dict[str, object]] = []
    classified_words = 0
    classified_weight = 0
    for word_index, (signature, multiplicity) in enumerate(quotient_counts.items(), start=1):
        if word_index <= skip_classified_words:
            continue
        if classified_words >= max_classified_words:
            break
        if classification_mode == "representative":
            statuses = Counter(
                classify_shell(survivor, demand, radicand).status
                for demand in quotient_reps[signature]
            )
            status_weights = Counter({next(iter(statuses)): multiplicity})
            word_weight = multiplicity
        elif classification_mode == "exhaustive":
            if quotient != "word":
                raise ValueError("exhaustive classification is only implemented for word quotient")
            statuses = classify_word_exhaustively(signature)
            status_weights = statuses
            word_weight = sum(statuses.values())
            if word_weight != multiplicity:
                word_count_mismatches.append(
                    {
                        "word": signature,
                        "expected": multiplicity,
                        "actual": word_weight,
                        "statuses": dict(sorted(statuses.items())),
                    }
                )
        else:
            raise ValueError(classification_mode)
        if len(statuses) > 1:
            mixed_status_words += 1
            if example_words_per_status and len(mixed_example_words) < example_words_per_status:
                mixed_example_words.append(
                    {
                        "word": signature,
                        "multiplicity": multiplicity,
                        "statuses": dict(sorted(statuses.items())),
                    }
                )
        representative_status = next(iter(statuses)) if len(statuses) == 1 else "mixed-status"
        status_group_counts[representative_status] += 1
        status_weight_counts.update(status_weights)
        status_signatures[tuple(sorted(statuses.items()))] += 1
        if example_words_per_status and len(example_words[representative_status]) < example_words_per_status:
            example_words[representative_status].append(
                {
                    "word": signature,
                    "multiplicity": multiplicity,
                    "statuses": dict(sorted(statuses.items())),
                }
            )
        classified_words += 1
        classified_weight += word_weight
        if progress_every and classified_words % progress_every == 0:
            elapsed = time.monotonic() - started
            print(
                f"    classified {quotient}_groups={classified_words} weight={classified_weight} "
                f"elapsed={elapsed:.1f}s",
                flush=True,
            )

    return {
        "tile": survivor.candidate.tile,
        "radicand": radicand,
        "min_total_mixed": min_total_mixed,
        "max_total_mixed": max_total_mixed,
        "endpoint_groups": endpoint_groups,
        "outside_cover_shells": total_uncovered,
        "quotient": quotient,
        "word_groups": len(quotient_counts) if quotient == "word" else None,
        "profile_groups": len(quotient_counts) if quotient == "profile" else None,
        "quotient_groups": len(quotient_counts),
        "reps_per_word": reps_per_word,
        "reps_per_group": reps_per_word,
        "skip_classified_words": skip_classified_words,
        "skip_classified_groups": skip_classified_words,
        "classification_mode": classification_mode,
        "classified_words": classified_words,
        "classified_groups": classified_words,
        "first_classified_word_index": skip_classified_words + 1 if classified_words else None,
        "first_classified_group_index": skip_classified_words + 1 if classified_words else None,
        "last_classified_word_index": skip_classified_words + classified_words if classified_words else None,
        "last_classified_group_index": skip_classified_words + classified_words if classified_words else None,
        "classified_weight": classified_weight,
        "mixed_status_words": mixed_status_words,
        "status_group_counts": dict(sorted(status_group_counts.items())),
        "status_weight_counts": dict(sorted(status_weight_counts.items())),
        "status_signatures": {
            json.dumps(dict(signature), sort_keys=True): count
            for signature, count in sorted(status_signatures.items())
        },
        "example_words": dict(sorted(example_words.items())),
        "mixed_example_words": mixed_example_words,
        "word_count_mismatches": word_count_mismatches,
        "elapsed_seconds": round(time.monotonic() - started, 6),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--min-total-mixed", type=int, default=6)
    parser.add_argument("--max-total-mixed", type=int, default=6)
    parser.add_argument("--reps-per-word", type=int, default=1)
    parser.add_argument("--skip-classified-words", type=int, default=0)
    parser.add_argument("--max-classified-words", type=int, default=10000)
    parser.add_argument("--classification-mode", choices=("representative", "exhaustive"), default="representative")
    parser.add_argument("--quotient", choices=("word", "profile"), default="word")
    parser.add_argument("--progress-every", type=int, default=0)
    parser.add_argument("--example-words-per-status", type=int, default=0)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    if args.min_total_mixed < 0:
        raise SystemExit("--min-total-mixed must be nonnegative")
    if args.max_total_mixed < args.min_total_mixed:
        raise SystemExit("--max-total-mixed must be at least --min-total-mixed")
    if args.reps_per_word <= 0:
        raise SystemExit("--reps-per-word must be positive")
    if args.skip_classified_words < 0:
        raise SystemExit("--skip-classified-words must be nonnegative")
    if args.max_classified_words <= 0:
        raise SystemExit("--max-classified-words must be positive")
    if args.example_words_per_status < 0:
        raise SystemExit("--example-words-per-status must be nonnegative")
    if args.classification_mode == "exhaustive" and args.quotient != "word":
        raise SystemExit("--classification-mode exhaustive is only implemented with --quotient word")

    results = []
    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
        for survivor in survivors:
            result = census_survivor(
                survivor,
                min_total_mixed=args.min_total_mixed,
                max_total_mixed=args.max_total_mixed,
                reps_per_word=args.reps_per_word,
                skip_classified_words=args.skip_classified_words,
                max_classified_words=args.max_classified_words,
                classification_mode=args.classification_mode,
                quotient=args.quotient,
                progress_every=args.progress_every,
                example_words_per_status=args.example_words_per_status,
            )
            result["n"] = n
            results.append(result)
            print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    if args.json_out is not None:
        payload = results[0] if len(results) == 1 else results
        args.json_out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
