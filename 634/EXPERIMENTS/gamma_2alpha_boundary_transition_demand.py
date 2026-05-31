#!/usr/bin/env python3
"""Boundary transition demand for `gamma=2alpha` survivor rows.

For a candidate boundary pattern, this script minimizes the number of
outer-boundary transitions where a `c` edge is adjacent to an `a` or `b` edge.
Such transitions are exactly where the strict side-label fan diagnostic needs
an overhang component.

The calculation is boundary-only.  It proves neither existence nor
non-existence of a full tiling, but it converts the remaining fan gap into a
small, reproducible boundary demand.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import (  # noqa: E402
    RefinedGamma2AlphaSurvivor,
    refined_survivors_for_n,
    viable_free_x_representations,
    viable_x_representations,
)
from gamma_2alpha_endpoint_automaton import (  # noqa: E402
    PlacedEdge,
    alpha_corner,
    apex_corner,
    edge_text,
    orientations,
    straight_transition,
)


Triple = tuple[int, int, int]
INF = 10**9


@dataclass(frozen=True)
class PathOption:
    first: PlacedEdge
    last: PlacedEdge
    mixed_transitions: int
    path: tuple[PlacedEdge, ...]


@dataclass(frozen=True)
class BoundaryDemand:
    short_side: str
    left_rep: Triple
    right_rep: Triple
    base_rep: Triple
    mixed_transitions: int
    left_path: tuple[PlacedEdge, ...]
    right_path: tuple[PlacedEdge, ...]
    base_path: tuple[PlacedEdge, ...]


def rep_text(rep: Triple) -> str:
    return f"{rep[0]}a+{rep[1]}b+{rep[2]}c"


def path_labels(path: tuple[PlacedEdge, ...]) -> str:
    return "".join(edge.side for edge in path)


def path_text(path: tuple[PlacedEdge, ...]) -> str:
    return " ".join(edge_text(edge) for edge in path)


def mixed_edge(left: PlacedEdge, right: PlacedEdge) -> int:
    return int((left.side == "c") != (right.side == "c"))


@lru_cache(maxsize=None)
def path_options(rep: Triple) -> tuple[PathOption, ...]:
    """Minimum-mixed paths for each endpoint pair of a side representation."""
    placed_edges = tuple(edge for side in ("a", "b", "c") for edge in orientations(side))

    @lru_cache(maxsize=None)
    def completions(remaining: Triple, previous_index: int) -> dict[int, tuple[int, tuple[int, ...]]]:
        if remaining == (0, 0, 0):
            return {previous_index: (0, ())}

        out: dict[int, tuple[int, tuple[int, ...]]] = {}
        counts = {"a": remaining[0], "b": remaining[1], "c": remaining[2]}
        for side_index, side in enumerate(("a", "b", "c")):
            if counts[side] == 0:
                continue
            next_remaining_list = list(remaining)
            next_remaining_list[side_index] -= 1
            next_remaining = tuple(next_remaining_list)
            for edge_index, edge in enumerate(placed_edges):
                if edge.side != side:
                    continue
                previous = placed_edges[previous_index]
                if not straight_transition(previous, edge, "angle"):
                    continue
                added = mixed_edge(previous, edge)
                for last_index, (cost, suffix) in completions(next_remaining, edge_index).items():
                    value = added + cost
                    if last_index not in out or value < out[last_index][0]:
                        out[last_index] = (value, (edge_index, *suffix))
        return out

    best_by_endpoints: dict[tuple[PlacedEdge, PlacedEdge], PathOption] = {}
    for first_index, first in enumerate(placed_edges):
        side_position = {"a": 0, "b": 1, "c": 2}[first.side]
        if rep[side_position] == 0:
            continue
        remaining_list = list(rep)
        remaining_list[side_position] -= 1
        remaining = tuple(remaining_list)
        for last_index, (cost, suffix) in completions(remaining, first_index).items():
            path = tuple(placed_edges[index] for index in (first_index, *suffix))
            option = PathOption(first, placed_edges[last_index], cost, path)
            key = (option.first, option.last)
            if key not in best_by_endpoints or option.mixed_transitions < best_by_endpoints[key].mixed_transitions:
                best_by_endpoints[key] = option
    return tuple(best_by_endpoints.values())


def options_by_rep(reps: tuple[Triple, ...]) -> dict[Triple, tuple[PathOption, ...]]:
    return {rep: path_options(rep) for rep in reps}


def best_demand_for_survivor(survivor: RefinedGamma2AlphaSurvivor) -> BoundaryDemand | None:
    candidate = survivor.candidate
    bounded_x = viable_x_representations(candidate)
    free_x = viable_free_x_representations(candidate)

    bounded_options = options_by_rep(bounded_x)
    free_options = options_by_rep(free_x)
    base_options = options_by_rep(survivor.y_representations)
    best: BoundaryDemand | None = None

    def consider(
        *,
        short_side: str,
        left_options_by_rep: dict[Triple, tuple[PathOption, ...]],
        right_options_by_rep: dict[Triple, tuple[PathOption, ...]],
    ) -> None:
        nonlocal best
        for left_rep, left_options in left_options_by_rep.items():
            for right_rep, right_options in right_options_by_rep.items():
                for base_rep, base_paths in base_options.items():
                    for left in left_options:
                        for right in right_options:
                            if not apex_corner(left.last, right.first):
                                continue
                            for base in base_paths:
                                if not alpha_corner(base.last, left.first):
                                    continue
                                if not alpha_corner(right.last, base.first):
                                    continue
                                mixed = (
                                    left.mixed_transitions
                                    + right.mixed_transitions
                                    + base.mixed_transitions
                                )
                                demand = BoundaryDemand(
                                    short_side=short_side,
                                    left_rep=left_rep,
                                    right_rep=right_rep,
                                    base_rep=base_rep,
                                    mixed_transitions=mixed,
                                    left_path=left.path,
                                    right_path=right.path,
                                    base_path=base.path,
                                )
                                if best is None or demand.mixed_transitions < best.mixed_transitions:
                                    best = demand

    consider(short_side="left", left_options_by_rep=bounded_options, right_options_by_rep=free_options)
    consider(short_side="right", left_options_by_rep=free_options, right_options_by_rep=bounded_options)
    return best


def print_demand(n: int, demand: BoundaryDemand, *, show_paths: bool) -> None:
    print(
        f"  mixed={demand.mixed_transitions}; short={demand.short_side}; "
        f"L={rep_text(demand.left_rep)} labels={path_labels(demand.left_path)}; "
        f"R={rep_text(demand.right_rep)} labels={path_labels(demand.right_path)}; "
        f"B={rep_text(demand.base_rep)} labels={path_labels(demand.base_path)}"
    )
    if show_paths:
        print(f"    L: {path_text(demand.left_path)}")
        print(f"    R: {path_text(demand.right_path)}")
        print(f"    B: {path_text(demand.base_path)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--show-paths", action="store_true")
    args = parser.parse_args()

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
        for survivor in survivors:
            candidate = survivor.candidate
            print(f"  tile={candidate.tile}, X={candidate.x}, Y={candidate.y}")
            demand = best_demand_for_survivor(survivor)
            if demand is None:
                print("  no angle-compatible boundary witness")
            else:
                print_demand(n, demand, show_paths=args.show_paths)


if __name__ == "__main__":
    main()
