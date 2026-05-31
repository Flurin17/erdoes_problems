#!/usr/bin/env python3
"""Count-only inventory of `gamma=2alpha` shells outside the local cover.

This is a grouped companion to `gamma_2alpha_overlap_cover.py`.  It uses the
same cached local-position overlap tests, but instead of reporting only total
coverage it records which endpoint/mixed boundary-word groups remain after the
default local-overlap cover.  The output is meant to guide the next symbolic
residual obstruction for the `N=63` and `N=99` survivors.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import refined_survivors_for_n, viable_x_representations  # noqa: E402
from gamma_2alpha_endpoint_automaton import (  # noqa: E402
    STRAIGHT_TYPES,
    PlacedEdge,
    alpha_corner,
    apex_corner,
    other_side,
)
from gamma_2alpha_overlap_cover import (  # noqa: E402
    DEFAULT_PAIR_TEXT,
    KPolygon,
    format_count,
    kscale_polygon,
    parse_pair,
    qdenominator_scale,
    side_tile_polygon,
    valid_pairs_for_lengths,
)
from gamma_2alpha_random_shell_search import Path as BoundaryPath  # noqa: E402
from gamma_2alpha_random_shell_search import all_path_options, by_endpoint_and_mixed  # noqa: E402


EndpointMixed = tuple[PlacedEdge, PlacedEdge, int]
PathProfile = tuple[tuple[int, ...], tuple[int, ...], str, tuple[str, ...]]


def edge_text(edge: PlacedEdge) -> str:
    return f"{edge.side}:{edge.start}->{edge.end}"


def group_signature(
    left_key: EndpointMixed,
    right_key: EndpointMixed,
    base_key: EndpointMixed,
) -> str:
    left_first, left_last, left_mixed = left_key
    right_first, right_last, right_mixed = right_key
    base_first, base_last, base_mixed = base_key
    return (
        f"m=({left_mixed},{right_mixed},{base_mixed}) "
        f"L={edge_text(left_first)}..{edge_text(left_last)} "
        f"R={edge_text(right_first)}..{edge_text(right_last)} "
        f"B={edge_text(base_first)}..{edge_text(base_last)}"
    )


def tuple_text(values: tuple[int, ...]) -> str:
    return ",".join(str(value) for value in values) if values else "-"


def angle_counter_text(counter: Counter[str]) -> str:
    parts: list[str] = []
    for name in ("alpha", "beta", "gamma"):
        count = counter[name]
        if count == 1:
            parts.append(name)
        elif count > 1:
            parts.append(f"{count}{name}")
    return "+".join(parts) if parts else "0"


def mixed_transition_signature(index: int, left: PlacedEdge, right: PlacedEdge) -> str:
    visible = Counter((left.end, right.start))
    deficits = tuple(
        angle_counter_text(target - visible)
        for target in STRAIGHT_TYPES
        if all(visible[key] <= target[key] for key in visible)
    )
    deficit_text = "/".join(deficits) if deficits else "none"
    inward = f"{other_side(left, left.end)}>{other_side(right, right.start)}"
    return f"{index}:{left.side}{right.side}:{left.end}+{right.start}:{inward}:{deficit_text}"


def path_profile(path: BoundaryPath, positions: tuple[int, ...]) -> PathProfile:
    c_positions = tuple(index for index, edge in enumerate(path, start=1) if edge.side == "c")
    mixed_positions = tuple(
        index
        for index, (left, right) in enumerate(zip(path, path[1:]), start=1)
        if (left.side == "c") != (right.side == "c")
    )
    tested_labels = "".join(path[position - 1].side for position in positions if position <= len(path))
    fan_signatures = tuple(
        mixed_transition_signature(index, left, right)
        for index, (left, right) in enumerate(zip(path, path[1:]), start=1)
        if (left.side == "c") != (right.side == "c")
    )
    return c_positions, mixed_positions, tested_labels, fan_signatures


def profile_text(profile: PathProfile) -> str:
    c_positions, mixed_positions, tested_labels, fan_signatures = profile
    fan_text = "|".join(fan_signatures) if fan_signatures else "-"
    return f"c={tuple_text(c_positions)} mix={tuple_text(mixed_positions)} test={tested_labels or '-'} fan={fan_text}"


def profile_signature(left: PathProfile, right: PathProfile, base: PathProfile) -> str:
    return f"L[{profile_text(left)}] R[{profile_text(right)}] B[{profile_text(base)}]"


def label_word(path: BoundaryPath) -> str:
    return "".join(edge.side for edge in path)


def word_signature(left: str, right: str, base: str) -> str:
    return f"L={left} R={right} B={base}"


def overlap(left: KPolygon, right: KPolygon) -> bool:
    if exact.kbbox_disjoint(exact.kbbox(left), exact.kbbox(right)):
        return False
    if exact.ksame_triangle(left, right):
        return False
    return exact.kpositive_overlap(left, right)


def inventory_n(
    n: int,
    *,
    min_total_mixed: int,
    max_total_mixed: int | None,
    top: int,
) -> None:
    survivors = refined_survivors_for_n(n)
    print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
    pairs = tuple(parse_pair(text) for text in DEFAULT_PAIR_TEXT)
    for survivor in survivors:
        radicand = exact.field_radicand(survivor)
        if radicand is None:
            print("  exact quadratic classifier unavailable")
            continue
        exact.RADICAND = radicand
        x_rep = viable_x_representations(survivor.candidate)[0]
        base_rep = survivor.y_representations[0]
        x_paths = all_path_options(x_rep)
        base_paths = all_path_options(base_rep)
        active_pairs = valid_pairs_for_lengths(pairs, sum(x_rep), sum(base_rep))
        x_index = by_endpoint_and_mixed(x_paths)
        base_index = by_endpoint_and_mixed(base_paths)

        needed_positions = {
            "L": sorted({pair.side_position for pair in active_pairs if pair.side == "L"}),
            "R": sorted({pair.side_position for pair in active_pairs if pair.side == "R"}),
            "B": sorted({pair.base_position for pair in active_pairs}),
        }
        q_polygons: dict[tuple[str, int, BoundaryPath], exact.QPolygon] = {}
        all_polygons: list[exact.QPolygon] = []
        for side_name, paths in (("L", x_paths), ("R", x_paths), ("B", base_paths)):
            for position in needed_positions[side_name]:
                for path in paths:
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
        good_profile_cache: dict[tuple[str, tuple[BoundaryPath, ...], tuple[KPolygon, ...]], Counter[PathProfile]] = {}
        good_word_cache: dict[tuple[str, tuple[BoundaryPath, ...], tuple[KPolygon, ...]], Counter[str]] = {}

        base_positions = needed_positions["B"]

        def base_feature(path: BoundaryPath) -> tuple[KPolygon, ...]:
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

        def side_good_profiles(
            side_name: str,
            paths: tuple[BoundaryPath, ...],
            feature: tuple[KPolygon, ...],
        ) -> Counter[PathProfile]:
            key = (side_name, paths, feature)
            cached = good_profile_cache.get(key)
            if cached is not None:
                return cached
            relevant = tuple(pair for pair in active_pairs if pair.side == side_name)
            out: Counter[PathProfile] = Counter()
            for path in paths:
                bad = any(
                    overlaps_cached(
                        polygons[(side_name, pair.side_position, path)],
                        base_polygon(feature, pair.base_position),
                    )
                    for pair in relevant
                )
                if not bad:
                    out[path_profile(path, tuple(needed_positions[side_name]))] += 1
            good_profile_cache[key] = out
            return out

        def side_good_words(
            side_name: str,
            paths: tuple[BoundaryPath, ...],
            feature: tuple[KPolygon, ...],
        ) -> Counter[str]:
            key = (side_name, paths, feature)
            cached = good_word_cache.get(key)
            if cached is not None:
                return cached
            relevant = tuple(pair for pair in active_pairs if pair.side == side_name)
            out: Counter[str] = Counter()
            for path in paths:
                bad = any(
                    overlaps_cached(
                        polygons[(side_name, pair.side_position, path)],
                        base_polygon(feature, pair.base_position),
                    )
                    for pair in relevant
                )
                if not bad:
                    out[label_word(path)] += 1
            good_word_cache[key] = out
            return out

        total_by_mixed: Counter[int] = Counter()
        uncovered_by_mixed: Counter[int] = Counter()
        covered_by_mixed: Counter[int] = Counter()
        uncovered_by_split: Counter[tuple[int, int, int]] = Counter()
        uncovered_by_endpoint_group: Counter[str] = Counter()
        uncovered_by_word_profile: Counter[str] = Counter()
        uncovered_by_c_profile: Counter[str] = Counter()
        total_groups = 0
        uncovered_groups = 0

        for left_key, left_paths in x_index.items():
            left_first, left_last, left_mixed = left_key
            for right_key, right_paths in x_index.items():
                right_first, right_last, right_mixed = right_key
                if not apex_corner(left_last, right_first):
                    continue
                for base_key, base_paths_for_key in base_index.items():
                    base_first, base_last, base_mixed = base_key
                    total_mixed = left_mixed + right_mixed + base_mixed
                    if total_mixed < min_total_mixed:
                        continue
                    if max_total_mixed is not None and total_mixed > max_total_mixed:
                        continue
                    if not alpha_corner(right_last, base_first):
                        continue
                    if not alpha_corner(base_last, left_first):
                        continue

                    total_groups += 1
                    left_total = len(left_paths)
                    right_total = len(right_paths)
                    total = left_total * right_total * len(base_paths_for_key)
                    total_by_mixed[total_mixed] += total
                    uncovered = 0
                    for (feature, base_profile), multiplicity in Counter(
                        (base_feature(path), path_profile(path, tuple(needed_positions["B"])))
                        for path in base_paths_for_key
                    ).items():
                        left_profiles = side_good_profiles("L", left_paths, feature)
                        right_profiles = side_good_profiles("R", right_paths, feature)
                        left_good = sum(left_profiles.values())
                        right_good = sum(right_profiles.values())
                        feature_uncovered = multiplicity * left_good * right_good
                        uncovered += feature_uncovered
                        if feature_uncovered:
                            for left_profile, left_count in left_profiles.items():
                                for right_profile, right_count in right_profiles.items():
                                    uncovered_by_c_profile[
                                        profile_signature(left_profile, right_profile, base_profile)
                                    ] += multiplicity * left_count * right_count
                    for (feature, base_word), multiplicity in Counter(
                        (base_feature(path), label_word(path))
                        for path in base_paths_for_key
                    ).items():
                        left_words = side_good_words("L", left_paths, feature)
                        right_words = side_good_words("R", right_paths, feature)
                        for left_word, left_count in left_words.items():
                            for right_word, right_count in right_words.items():
                                uncovered_by_word_profile[
                                    word_signature(left_word, right_word, base_word)
                                ] += multiplicity * left_count * right_count
                    if uncovered:
                        uncovered_groups += 1
                        uncovered_by_mixed[total_mixed] += uncovered
                        covered_by_mixed[total_mixed] += total - uncovered
                        uncovered_by_split[(left_mixed, right_mixed, base_mixed)] += uncovered
                        uncovered_by_endpoint_group[group_signature(left_key, right_key, base_key)] += uncovered
                    else:
                        covered_by_mixed[total_mixed] += total

        pair_text = ", ".join(f"{pair.side}{pair.side_position}-B{pair.base_position}" for pair in active_pairs)
        print(f"  active local overlap pairs: {pair_text}")
        print(f"  endpoint/mixed groups: total={total_groups}, outside_cover={uncovered_groups}")
        print("  coverage by mixed:")
        for mixed in sorted(total_by_mixed):
            total = total_by_mixed[mixed]
            covered = covered_by_mixed[mixed]
            uncovered = uncovered_by_mixed[mixed]
            percent = 100 * covered / total if total else 0.0
            print(
                f"    mixed={mixed}: covered={format_count(covered)} "
                f"outside={format_count(uncovered)} total={format_count(total)} ({percent:.2f}% covered)"
            )
        print("  outside-cover mixed split counts:")
        for split, count in uncovered_by_split.most_common(top):
            print(f"    {split}: {format_count(count)}")
        print("  top outside-cover endpoint/mixed groups:")
        for signature, count in uncovered_by_endpoint_group.most_common(top):
            print(f"    {format_count(count)}: {signature}")
        print("  top outside-cover label-word profiles:")
        word_total = sum(uncovered_by_word_profile.values())
        word_top_total = sum(count for _signature, count in uncovered_by_word_profile.most_common(top))
        word_top_percent = 100 * word_top_total / word_total if word_total else 0.0
        print(
            f"    word_groups={len(uncovered_by_word_profile)} "
            f"top_{top}_mass={format_count(word_top_total)} "
            f"of {format_count(word_total)} ({word_top_percent:.2f}%)"
        )
        for signature, count in uncovered_by_word_profile.most_common(top):
            print(f"    {format_count(count)}: {signature}")
        print("  top outside-cover c/mixed/test/fan profiles:")
        profile_total = sum(uncovered_by_c_profile.values())
        profile_top_total = sum(count for _signature, count in uncovered_by_c_profile.most_common(top))
        profile_top_percent = 100 * profile_top_total / profile_total if profile_total else 0.0
        print(
            f"    profile_groups={len(uncovered_by_c_profile)} "
            f"top_{top}_mass={format_count(profile_top_total)} "
            f"of {format_count(profile_total)} ({profile_top_percent:.2f}%)"
        )
        for signature, count in uncovered_by_c_profile.most_common(top):
            print(f"    {format_count(count)}: {signature}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--min-total-mixed", type=int, default=0)
    parser.add_argument("--max-total-mixed", type=int)
    parser.add_argument("--top", type=int, default=20)
    args = parser.parse_args()
    if args.min_total_mixed < 0:
        raise SystemExit("--min-total-mixed must be nonnegative")
    if args.max_total_mixed is not None and args.max_total_mixed < args.min_total_mixed:
        raise SystemExit("--max-total-mixed must be at least --min-total-mixed")

    for n in args.n:
        inventory_n(
            n,
            min_total_mixed=args.min_total_mixed,
            max_total_mixed=args.max_total_mixed,
            top=args.top,
        )


if __name__ == "__main__":
    main()
