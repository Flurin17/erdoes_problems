#!/usr/bin/env python3
"""Residual corner-label check for the `gamma=2alpha` boundary shell.

This diagnostic inspects the residual simple cycle produced by
`gamma_2alpha_residual_boundary.py`.  When a residual boundary vertex has a
unique one-tile angle and the two adjacent residual segments are full,
indecomposable tile sides, the next tile would have to occupy that corner.
The adjacent side labels must then be exactly the two labels incident to that
tile angle.

The check is run on the current transition-demand witness.  It is therefore a
shell-extension diagnostic, not a proof that every possible boundary ordering
for the same arithmetic survivor fails.
"""

from __future__ import annotations

import argparse
import math
import sys
from collections import Counter, defaultdict


sys.path.insert(0, "634/EXPERIMENTS")
from gamma_2alpha_boundary import refined_survivors_for_n  # noqa: E402
from gamma_2alpha_boundary_shell import (  # noqa: E402
    Point,
    ShellTile,
    outer_vertices,
    place_boundary_shell,
    signed_area,
    tile_area_from_sides,
)
from gamma_2alpha_boundary_transition_demand import best_demand_for_survivor, path_labels  # noqa: E402
from gamma_2alpha_endpoint_automaton import other_side  # noqa: E402
from gamma_2alpha_residual_boundary import (  # noqa: E402
    SegmentKey,
    point_on_segment,
    segment_key,
    segment_on_outer,
    simple_cycle,
    split_segment,
    unique_shell_tiles,
)


ANGLE_SIDES: dict[str, frozenset[str]] = {
    "alpha": frozenset(("b", "c")),
    "beta": frozenset(("a", "c")),
    "gamma": frozenset(("a", "b")),
}
SIDE_INDEX = {"a": 0, "b": 1, "c": 2}
EPS = 1e-7


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1])


def dot(left: Point, right: Point) -> float:
    return left[0] * right[0] + left[1] * right[1]


def cross(left: Point, right: Point) -> float:
    return left[0] * right[1] - left[1] * right[0]


def length(segment: SegmentKey) -> float:
    start, end = segment
    return math.hypot(end[0] - start[0], end[1] - start[1])


def edge_labels_for_tile(tile: ShellTile) -> tuple[str, str, str]:
    return (
        tile.edge.side,
        other_side(tile.edge, tile.edge.end),
        other_side(tile.edge, tile.edge.start),
    )


def residual_segments_with_labels(
    tiles: tuple[ShellTile, ...],
    outer: tuple[Point, Point, Point],
    *,
    digits: int,
    eps: float,
) -> dict[SegmentKey, str]:
    all_points = tuple(point for tile in tiles for point in tile.polygon)
    counts: Counter[SegmentKey] = Counter()
    labels: dict[SegmentKey, str] = {}

    for tile in tiles:
        for index, side_label in enumerate(edge_labels_for_tile(tile)):
            start = tile.polygon[index]
            end = tile.polygon[(index + 1) % 3]
            for atom_start, atom_end in split_segment(start, end, all_points, eps=eps):
                key = segment_key(atom_start, atom_end, digits)
                counts[key] += 1
                labels[key] = side_label

    return {
        key: labels[key]
        for key, count in counts.items()
        if count == 1 and not segment_on_outer(key, outer, eps=eps)
    }


def side_decomposable(target: float, sides: tuple[int, int, int], *, eps: float) -> bool:
    """Return whether target can be a sum of at least two tile side lengths."""
    limit = int(target // min(sides)) + 1
    for a_count in range(limit + 1):
        for b_count in range(limit + 1):
            for c_count in range(limit + 1):
                pieces = a_count + b_count + c_count
                if pieces < 2:
                    continue
                value = a_count * sides[0] + b_count * sides[1] + c_count * sides[2]
                if abs(value - target) <= eps:
                    return True
    return False


def tile_angles(sides: tuple[int, int, int]) -> dict[str, float]:
    a, b, c = sides
    return {
        "alpha": math.acos((b * b + c * c - a * a) / (2 * b * c)),
        "beta": math.acos((a * a + c * c - b * b) / (2 * a * c)),
        "gamma": math.acos((a * a + b * b - c * c) / (2 * a * b)),
    }


def interior_angle(cycle: list[Point], index: int) -> float:
    incoming = sub(cycle[index], cycle[index - 1])
    outgoing = sub(cycle[(index + 1) % len(cycle)], cycle[index])
    turn = math.atan2(cross(incoming, outgoing), dot(incoming, outgoing))
    value = math.pi - turn
    return value + 2 * math.pi if value < 0 else value


def angle_combos(target: float, angles: dict[str, float]) -> tuple[tuple[int, int, int], ...]:
    out: list[tuple[int, int, int]] = []
    for alpha_count in range(8):
        for beta_count in range(8):
            for gamma_count in range(8):
                value = (
                    alpha_count * angles["alpha"]
                    + beta_count * angles["beta"]
                    + gamma_count * angles["gamma"]
                )
                if abs(value - target) < 1e-6:
                    out.append((alpha_count, beta_count, gamma_count))
    return tuple(out)


def forced_angle_name(combos: tuple[tuple[int, int, int], ...]) -> str | None:
    single = [combo for combo in combos if sum(combo) == 1]
    if len(combos) != 1 or len(single) != 1:
        return None
    combo = single[0]
    return ("alpha", "beta", "gamma")[combo.index(1)]


def cycle_edge_key(cycle: list[Point], index: int, *, digits: int) -> SegmentKey:
    return segment_key(cycle[index], cycle[(index + 1) % len(cycle)], digits)


def check_n(n: int, *, digits: int, eps: float) -> None:
    survivors = refined_survivors_for_n(n)
    print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
    for survivor in survivors:
        demand = best_demand_for_survivor(survivor)
        if demand is None:
            print("  no transition-demand witness")
            continue
        shell = place_boundary_shell(survivor, demand)
        unique = unique_shell_tiles(shell, tile_area_from_sides(survivor.candidate.tile))
        outer = outer_vertices(survivor)
        residual_labels = residual_segments_with_labels(unique, outer, digits=digits, eps=eps)
        cycle = simple_cycle(list(residual_labels))
        print(
            f"  witness L={path_labels(demand.left_path)} R={path_labels(demand.right_path)} "
            f"B={path_labels(demand.base_path)}"
        )
        if cycle is None:
            print("  residual is not a simple cycle; corner-label check skipped")
            continue
        if signed_area(tuple(cycle)) < 0:
            cycle.reverse()

        sides = survivor.candidate.tile
        side_lengths = {side: sides[SIDE_INDEX[side]] for side in "abc"}
        segment_lengths = Counter(round(length(segment), 6) for segment in residual_labels)
        decomposable = [
            segment
            for segment in residual_labels
            if side_decomposable(length(segment), sides, eps=eps)
        ]

        violations: list[tuple[int, Point, str, str, str]] = []
        forced = 0
        angle_histogram: Counter[str] = Counter()
        angles = tile_angles(sides)
        for index, point in enumerate(cycle):
            previous_edge = cycle_edge_key(cycle, index - 1, digits=digits)
            next_edge = cycle_edge_key(cycle, index, digits=digits)
            previous_label = residual_labels[previous_edge]
            next_label = residual_labels[next_edge]
            combos = angle_combos(interior_angle(cycle, index), angles)
            angle_name = forced_angle_name(combos)
            if angle_name is None:
                continue
            forced += 1
            angle_histogram[angle_name] += 1
            side_pair = frozenset((previous_label, next_label))
            if side_pair != ANGLE_SIDES[angle_name]:
                violations.append((index, point, angle_name, previous_label, next_label))

        print(f"  residual segments={len(residual_labels)}; length histogram={dict(sorted(segment_lengths.items()))}")
        print(f"  decomposable residual full-side atoms={len(decomposable)}")
        print(f"  forced single-angle corners={forced}; angle histogram={dict(sorted(angle_histogram.items()))}")
        print(f"  label violations={len(violations)}")
        for index, point, angle_name, previous_label, next_label in violations[:12]:
            print(
                f"    v{index} ({point[0]:.9g},{point[1]:.9g}): "
                f"{angle_name} corner with labels {previous_label},{next_label}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--digits", type=int, default=7)
    parser.add_argument("--eps", type=float, default=1e-7)
    args = parser.parse_args()

    for n in args.n:
        check_n(n, digits=args.digits, eps=args.eps)


if __name__ == "__main__":
    main()
