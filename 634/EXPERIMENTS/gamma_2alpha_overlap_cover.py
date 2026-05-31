#!/usr/bin/env python3
"""Exact count cover by local overlap positions for `gamma=2alpha` shells.

The sampler `gamma_2alpha_overlap_causes.py` shows that high-mixed proper
overlaps concentrate at a few base/equal-side tile positions.  This script
turns those candidate local lemmas into exact counts: it counts how many valid
boundary-shell triples are killed by a selected set of position-pair overlap
tests, without materializing every triple.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import lcm
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import RefinedGamma2AlphaSurvivor, refined_survivors_for_n, viable_x_representations  # noqa: E402
from gamma_2alpha_endpoint_automaton import PlacedEdge, alpha_corner, apex_corner, other_side  # noqa: E402
from gamma_2alpha_random_shell_search import Path as BoundaryPath  # noqa: E402
from gamma_2alpha_random_shell_search import all_path_options, by_endpoint_and_mixed  # noqa: E402


Triple = tuple[int, int, int]
KPolygon = exact.KPolygon


@dataclass(frozen=True)
class PositionPair:
    side: str
    side_position: int
    base_position: int


DEFAULT_PAIR_TEXT = (
    "L2-B8",
    "R6-B2",
    "R5-B3",
    "R8-B2",
    "R7-B2",
    "L2-B7",
    "R7-B3",
    "L3-B7",
    "R6-B4",
)


def parse_pair(text: str) -> PositionPair:
    try:
        side_text, base_text = text.split("-", 1)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid pair {text!r}; expected e.g. L2-B8") from exc
    if not side_text or not base_text or side_text[0] not in ("L", "R") or base_text[0] != "B":
        raise argparse.ArgumentTypeError(f"invalid pair {text!r}; expected e.g. L2-B8")
    return PositionPair(side_text[0], int(side_text[1:]), int(base_text[1:]))


def qdenominator_scale(polygons: list[exact.QPolygon]) -> int:
    scale = 1
    for polygon in polygons:
        for point in polygon:
            for value in point:
                if exact.RADICAND == 1:
                    scale = lcm(scale, (value.rational + value.radical).denominator)
                else:
                    scale = lcm(scale, value.rational.denominator, value.radical.denominator)
    return scale


def kscale_polygon(polygon: exact.QPolygon, scale: int) -> KPolygon:
    return tuple(exact.kscale_point(point, scale) for point in polygon)


def side_vertices(
    survivor: RefinedGamma2AlphaSurvivor,
    side_name: str,
    radicand: int,
) -> tuple[exact.QPoint, exact.QPoint, Fraction]:
    vertices = exact.outer_vertices(survivor, radicand)
    if vertices is None:
        raise ValueError("outer triangle not in selected quadratic field")
    left_base, apex, right_base = vertices
    if side_name == "L":
        return left_base, apex, Fraction(survivor.candidate.x)
    if side_name == "R":
        return apex, right_base, Fraction(survivor.candidate.x)
    if side_name == "B":
        return right_base, left_base, Fraction(survivor.candidate.y)
    raise ValueError(side_name)


def side_tile_polygon(
    survivor: RefinedGamma2AlphaSurvivor,
    *,
    side_name: str,
    path: BoundaryPath,
    position: int,
    radicand: int,
) -> exact.QPolygon:
    start, end, length = side_vertices(survivor, side_name, radicand)
    vector = exact.qpsub(end, start)
    direction = exact.qpdiv_fraction(vector, length)
    offset = Fraction(0)
    for index, edge in enumerate(path, start=1):
        side_length = Fraction(survivor.candidate.tile[{"a": 0, "b": 1, "c": 2}[edge.side]])
        if index == position:
            tile = exact.place_edge_tile(
                label=f"{side_name}{index}:{edge.side}:{edge.start}->{edge.end}",
                edge=edge,
                start=start,
                direction=direction,
                offset=offset,
                sides=survivor.candidate.tile,
                radicand=radicand,
            )
            if tile is None:
                raise ValueError("tile not in selected quadratic field")
            return tile.polygon
        offset += side_length
    raise IndexError((side_name, position, len(path)))


def overlap(left: KPolygon, right: KPolygon) -> bool:
    if exact.kbbox_disjoint(exact.kbbox(left), exact.kbbox(right)):
        return False
    if exact.ksame_triangle(left, right):
        return False
    return exact.kpositive_overlap(left, right)


def valid_pairs_for_lengths(pairs: tuple[PositionPair, ...], x_len: int, base_len: int) -> tuple[PositionPair, ...]:
    return tuple(
        pair
        for pair in pairs
        if pair.side_position <= x_len and pair.base_position <= base_len
    )


def total_shell_count_by_mixed(
    x_index: dict[tuple[PlacedEdge, PlacedEdge, int], tuple[BoundaryPath, ...]],
    base_index: dict[tuple[PlacedEdge, PlacedEdge, int], tuple[BoundaryPath, ...]],
    *,
    max_total_mixed: int | None,
) -> Counter[int]:
    totals: Counter[int] = Counter()
    for (left_first, left_last, left_mixed), left_paths in x_index.items():
        for (right_first, right_last, right_mixed), right_paths in x_index.items():
            if not apex_corner(left_last, right_first):
                continue
            for (base_first, base_last, base_mixed), base_paths in base_index.items():
                total_mixed = left_mixed + right_mixed + base_mixed
                if max_total_mixed is not None and total_mixed > max_total_mixed:
                    continue
                if not alpha_corner(right_last, base_first):
                    continue
                if not alpha_corner(base_last, left_first):
                    continue
                totals[total_mixed] += len(left_paths) * len(right_paths) * len(base_paths)
    return totals


def count_cover(
    survivor: RefinedGamma2AlphaSurvivor,
    pairs: tuple[PositionPair, ...],
    *,
    max_total_mixed: int | None,
) -> tuple[Counter[int], Counter[int], tuple[PositionPair, ...]]:
    radicand = exact.field_radicand(survivor)
    if radicand is None:
        raise ValueError("quadratic field unavailable")
    exact.RADICAND = radicand
    x_rep = viable_x_representations(survivor.candidate)[0]
    base_rep = survivor.y_representations[0]
    x_len = sum(x_rep)
    base_len = sum(base_rep)
    active_pairs = valid_pairs_for_lengths(pairs, x_len, base_len)
    x_paths = all_path_options(x_rep)
    base_paths = all_path_options(base_rep)
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
    bad_count_cache: dict[tuple[str, tuple[BoundaryPath, ...], tuple[KPolygon, ...]], int] = {}

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

    def side_bad_count(side_name: str, paths: tuple[BoundaryPath, ...], feature: tuple[KPolygon, ...]) -> int:
        key = (side_name, paths, feature)
        cached = bad_count_cache.get(key)
        if cached is not None:
            return cached
        relevant = tuple(pair for pair in active_pairs if pair.side == side_name)
        count = 0
        for path in paths:
            if any(
                overlaps_cached(
                    polygons[(side_name, pair.side_position, path)],
                    base_polygon(feature, pair.base_position),
                )
                for pair in relevant
            ):
                count += 1
        bad_count_cache[key] = count
        return count

    covered: Counter[int] = Counter()
    totals = total_shell_count_by_mixed(x_index, base_index, max_total_mixed=max_total_mixed)
    for (left_first, left_last, left_mixed), left_paths in x_index.items():
        for (right_first, right_last, right_mixed), right_paths in x_index.items():
            if not apex_corner(left_last, right_first):
                continue
            for (base_first, base_last, base_mixed), base_paths in base_index.items():
                total_mixed = left_mixed + right_mixed + base_mixed
                if max_total_mixed is not None and total_mixed > max_total_mixed:
                    continue
                if not alpha_corner(right_last, base_first):
                    continue
                if not alpha_corner(base_last, left_first):
                    continue
                feature_counts = Counter(base_feature(path) for path in base_paths)
                left_total = len(left_paths)
                right_total = len(right_paths)
                for feature, multiplicity in feature_counts.items():
                    left_bad = side_bad_count("L", left_paths, feature)
                    right_bad = side_bad_count("R", right_paths, feature)
                    covered[total_mixed] += multiplicity * (
                        left_total * right_total
                        - (left_total - left_bad) * (right_total - right_bad)
                    )
    return totals, covered, active_pairs


def format_count(value: int) -> str:
    return f"{value:,}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--pair", action="append", type=parse_pair, help="local overlap pair such as L2-B8")
    parser.add_argument("--max-total-mixed", type=int)
    args = parser.parse_args()

    pairs = tuple(args.pair) if args.pair else tuple(parse_pair(text) for text in DEFAULT_PAIR_TEXT)
    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
        for survivor in survivors:
            totals, covered, active_pairs = count_cover(
                survivor,
                pairs,
                max_total_mixed=args.max_total_mixed,
            )
            pair_text = ", ".join(f"{pair.side}{pair.side_position}-B{pair.base_position}" for pair in active_pairs)
            print(f"  active local overlap pairs: {pair_text}")
            print("  mixed count coverage:")
            for mixed in sorted(totals):
                total = totals[mixed]
                hit = covered[mixed]
                percent = 100 * hit / total if total else 0.0
                print(
                    f"    mixed={mixed}: covered={format_count(hit)} "
                    f"of {format_count(total)} ({percent:.2f}%)"
                )
            total_all = sum(totals.values())
            covered_all = sum(covered.values())
            percent_all = 100 * covered_all / total_all if total_all else 0.0
            print(
                f"  total covered={format_count(covered_all)} "
                f"of {format_count(total_all)} ({percent_all:.2f}%)"
            )


if __name__ == "__main__":
    main()
