#!/usr/bin/env python3
"""Census of endpoint-minimal `gamma=2alpha` boundary shells.

`gamma_2alpha_boundary_transition_demand.path_options` keeps one minimum-mixed
path for each pair of oriented side endpoints.  This script enumerates the
boundary cycles obtained from those representatives and applies the residual
corner-label diagnostic to each shell.

This is a finite diagnostic over canonical endpoint-minimal representatives,
not an exhaustive search over all side-label orderings.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass


sys.path.insert(0, "634/EXPERIMENTS")
from gamma_2alpha_boundary import (  # noqa: E402
    RefinedGamma2AlphaSurvivor,
    refined_survivors_for_n,
    viable_free_x_representations,
    viable_x_representations,
)
from gamma_2alpha_boundary_shell import (  # noqa: E402
    DisjointSet,
    intersection_area,
    outer_vertices,
    place_boundary_shell,
    signed_area,
    tile_area_from_sides,
)
from gamma_2alpha_boundary_transition_demand import (  # noqa: E402
    BoundaryDemand,
    path_labels,
    path_options,
)
from gamma_2alpha_endpoint_automaton import alpha_corner, apex_corner  # noqa: E402
from gamma_2alpha_residual_boundary import simple_cycle  # noqa: E402
from gamma_2alpha_residual_corner_labels import (  # noqa: E402
    ANGLE_SIDES,
    angle_combos,
    cycle_edge_key,
    forced_angle_name,
    interior_angle,
    length,
    residual_segments_with_labels,
    side_decomposable,
    tile_angles,
)


Triple = tuple[int, int, int]


@dataclass(frozen=True)
class ShellResult:
    status: str
    forced_corners: int
    label_violations: int


def classify_shell(survivor: RefinedGamma2AlphaSurvivor, demand: BoundaryDemand) -> ShellResult:
    shell = place_boundary_shell(survivor, demand)
    tile_area = tile_area_from_sides(survivor.candidate.tile)
    disjoint = DisjointSet(len(shell))
    duplicate_threshold = tile_area * (1 - 1e-7)
    overlap_threshold = tile_area * 1e-9
    for left in range(len(shell)):
        for right in range(left + 1, len(shell)):
            shared = intersection_area(shell[left].polygon, shell[right].polygon)
            if shared >= duplicate_threshold:
                disjoint.union(left, right)
            elif shared > overlap_threshold:
                return ShellResult("proper-overlap", 0, 0)

    unique = tuple(tile for index, tile in enumerate(shell) if disjoint.find(index) == index)
    outer = outer_vertices(survivor)
    residual_labels = residual_segments_with_labels(unique, outer, digits=7, eps=1e-7)
    cycle = simple_cycle(list(residual_labels))
    if cycle is None:
        return ShellResult("not-simple-cycle", 0, 0)
    if signed_area(tuple(cycle)) < 0:
        cycle.reverse()

    sides = survivor.candidate.tile
    if any(side_decomposable(length(segment), sides, eps=1e-7) for segment in residual_labels):
        return ShellResult("decomposable-residual-atom", 0, 0)

    angles = tile_angles(sides)
    forced_corners = 0
    violations = 0
    for index in range(len(cycle)):
        previous_edge = cycle_edge_key(cycle, index - 1, digits=7)
        next_edge = cycle_edge_key(cycle, index, digits=7)
        angle_name = forced_angle_name(angle_combos(interior_angle(cycle, index), angles))
        if angle_name is None:
            continue
        forced_corners += 1
        side_pair = frozenset((residual_labels[previous_edge], residual_labels[next_edge]))
        if side_pair != ANGLE_SIDES[angle_name]:
            violations += 1

    if violations:
        return ShellResult("corner-label-violation", forced_corners, violations)
    return ShellResult("passes-corner-label-check", forced_corners, violations)


def endpoint_min_demands(survivor: RefinedGamma2AlphaSurvivor) -> tuple[BoundaryDemand, ...]:
    candidate = survivor.candidate
    bounded_x = viable_x_representations(candidate)
    free_x = viable_free_x_representations(candidate)
    base_reps = survivor.y_representations
    demands: list[BoundaryDemand] = []

    def add_demands(short_side: str, left_reps: tuple[Triple, ...], right_reps: tuple[Triple, ...]) -> None:
        for left_rep in left_reps:
            for right_rep in right_reps:
                for base_rep in base_reps:
                    for left in path_options(left_rep):
                        for right in path_options(right_rep):
                            if not apex_corner(left.last, right.first):
                                continue
                            for base in path_options(base_rep):
                                if not alpha_corner(base.last, left.first):
                                    continue
                                if not alpha_corner(right.last, base.first):
                                    continue
                                demands.append(
                                    BoundaryDemand(
                                        short_side=short_side,
                                        left_rep=left_rep,
                                        right_rep=right_rep,
                                        base_rep=base_rep,
                                        mixed_transitions=(
                                            left.mixed_transitions
                                            + right.mixed_transitions
                                            + base.mixed_transitions
                                        ),
                                        left_path=left.path,
                                        right_path=right.path,
                                        base_path=base.path,
                                    )
                                )

    add_demands("left", bounded_x, free_x)
    add_demands("right", free_x, bounded_x)

    # When the bounded and free representation sets are equal, the two short-side
    # orientations duplicate the same geometric boundary cycles.
    seen: set[tuple[str, str, str]] = set()
    unique: list[BoundaryDemand] = []
    for demand in demands:
        key = (
            path_labels(demand.left_path),
            path_labels(demand.right_path),
            path_labels(demand.base_path),
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(demand)
    return tuple(unique)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--show-examples", action="store_true")
    args = parser.parse_args()

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
        for survivor in survivors:
            demands = endpoint_min_demands(survivor)
            counts: Counter[str] = Counter()
            forced: Counter[str] = Counter()
            examples: dict[str, tuple[BoundaryDemand, ShellResult]] = {}
            for demand in demands:
                result = classify_shell(survivor, demand)
                counts[result.status] += 1
                forced[result.status] += result.forced_corners
                examples.setdefault(result.status, (demand, result))
            print(f"  endpoint-minimal shell representatives={len(demands)}")
            print(f"  status counts={dict(sorted(counts.items()))}")
            if args.show_examples:
                for status, (demand, result) in sorted(examples.items()):
                    print(
                        f"    {status}: forced={result.forced_corners}, "
                        f"violations={result.label_violations}, "
                        f"L={path_labels(demand.left_path)} "
                        f"R={path_labels(demand.right_path)} "
                        f"B={path_labels(demand.base_path)} "
                        f"mixed={demand.mixed_transitions}"
                    )


if __name__ == "__main__":
    main()
