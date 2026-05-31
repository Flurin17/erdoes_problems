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
from gamma_2alpha_overlap_remainder_inventory import label_word, word_signature  # noqa: E402
from gamma_2alpha_residual_capped_census import classify_shell  # noqa: E402


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


def census_survivor(
    survivor,
    *,
    min_total_mixed: int,
    max_total_mixed: int,
    reps_per_word: int,
    skip_classified_words: int,
    max_classified_words: int,
    progress_every: int,
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
    side_word_cache: dict[tuple[str, tuple[BoundaryPath, ...], tuple[KPolygon, ...]], dict[str, WordData]] = {}

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

    def side_good_words(
        side_name: str,
        paths: tuple[BoundaryPath, ...],
        feature: tuple[KPolygon, ...],
    ) -> dict[str, WordData]:
        key = (side_name, paths, feature)
        cached = side_word_cache.get(key)
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
            word = label_word(path)
            counts[word] += 1
            reps.setdefault(word, path)
        cached = {word: (count, reps[word]) for word, count in counts.items()}
        side_word_cache[key] = cached
        return cached

    word_counts: Counter[str] = Counter()
    word_reps: dict[str, list[BoundaryDemand]] = defaultdict(list)
    total_uncovered = 0
    endpoint_groups = 0

    orientations = [("left", bounded_reps, free_reps)]
    if bounded_reps != free_reps:
        orientations.append(("right", free_reps, bounded_reps))

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
                                    key = (base_feature(base_path), label_word(base_path))
                                    base_counts[key] += 1
                                    base_rep_by_key.setdefault(key, base_path)

                                for (feature, base_word), base_count in base_counts.items():
                                    left_words = side_good_words("L", left_paths, feature)
                                    right_words = side_good_words("R", right_paths, feature)
                                    if not left_words or not right_words:
                                        continue
                                    base_path = base_rep_by_key[(feature, base_word)]
                                    for left_word, (left_count, left_path) in left_words.items():
                                        for right_word, (right_count, right_path) in right_words.items():
                                            signature = word_signature(left_word, right_word, base_word)
                                            multiplicity = base_count * left_count * right_count
                                            word_counts[signature] += multiplicity
                                            total_uncovered += multiplicity
                                            add_rep(
                                                word_reps[signature],
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
        if progress_every and len(word_counts) and len(word_counts) % progress_every == 0:
            elapsed = time.monotonic() - started
            print(
                f"    counted word_groups={len(word_counts)} uncovered={total_uncovered} "
                f"elapsed={elapsed:.1f}s",
                flush=True,
            )

    status_group_counts: Counter[str] = Counter()
    status_weight_counts: Counter[str] = Counter()
    status_signatures: Counter[tuple[tuple[str, int], ...]] = Counter()
    mixed_status_words = 0
    classified_words = 0
    classified_weight = 0
    for word_index, (signature, multiplicity) in enumerate(word_counts.items(), start=1):
        if word_index <= skip_classified_words:
            continue
        if classified_words >= max_classified_words:
            break
        statuses = Counter(
            classify_shell(survivor, demand, radicand).status
            for demand in word_reps[signature]
        )
        if len(statuses) > 1:
            mixed_status_words += 1
        representative_status = next(iter(statuses))
        status_group_counts[representative_status] += 1
        status_weight_counts[representative_status] += multiplicity
        status_signatures[tuple(sorted(statuses.items()))] += 1
        classified_words += 1
        classified_weight += multiplicity
        if progress_every and classified_words % progress_every == 0:
            elapsed = time.monotonic() - started
            print(
                f"    classified word_groups={classified_words} weight={classified_weight} "
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
        "word_groups": len(word_counts),
        "reps_per_word": reps_per_word,
        "skip_classified_words": skip_classified_words,
        "classified_words": classified_words,
        "first_classified_word_index": skip_classified_words + 1 if classified_words else None,
        "last_classified_word_index": skip_classified_words + classified_words if classified_words else None,
        "classified_weight": classified_weight,
        "mixed_status_words": mixed_status_words,
        "status_group_counts": dict(sorted(status_group_counts.items())),
        "status_weight_counts": dict(sorted(status_weight_counts.items())),
        "status_signatures": {
            json.dumps(dict(signature), sort_keys=True): count
            for signature, count in sorted(status_signatures.items())
        },
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
    parser.add_argument("--progress-every", type=int, default=0)
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
                progress_every=args.progress_every,
            )
            result["n"] = n
            results.append(result)
            print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    if args.json_out is not None:
        payload = results[0] if len(results) == 1 else results
        args.json_out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
