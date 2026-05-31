#!/usr/bin/env python3
"""Boundary-fan side-incidence inventories for `gamma=2alpha` survivors.

For each straight boundary vertex in a transition-demand witness, enumerate
local overhang-aware fans and sum the side incidences consumed by their interior
rays.  This is a necessary-condition diagnostic only: passing it does not extend
the boundary to a full tiling.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import refined_survivors_for_n  # noqa: E402
from gamma_2alpha_boundary_transition_demand import (  # noqa: E402
    BoundaryDemand,
    best_demand_for_survivor,
    path_labels,
)
from gamma_2alpha_endpoint_automaton import PlacedEdge, edge_text  # noqa: E402
from gamma_2alpha_overhang_fan import SideLengths, overhang_fans  # noqa: E402


Triple = tuple[int, int, int]
SIDE_INDEX = {"a": 0, "b": 1, "c": 2}


@dataclass(frozen=True)
class Transition:
    side_name: str
    index: int
    left: PlacedEdge
    right: PlacedEdge


def add(left: Triple, right: Triple) -> Triple:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def leq(left: Triple, right: Triple) -> bool:
    return all(left[i] <= right[i] for i in range(3))


def side_string_counts(seq: tuple[str, ...]) -> Triple:
    counts = [0, 0, 0]
    for side in seq:
        counts[SIDE_INDEX[side]] += 1
    return tuple(counts)  # type: ignore[return-value]


def component_counts(components: tuple[tuple[str, str, str, str, tuple[str, ...], tuple[str, ...]], ...]) -> Triple:
    total = (0, 0, 0)
    for component in components:
        total = add(total, side_string_counts(component[4]))
        total = add(total, side_string_counts(component[5]))
    return total


def pareto_minimal(vectors: set[Triple]) -> tuple[Triple, ...]:
    out: list[Triple] = []
    for vector in sorted(vectors, key=lambda item: (sum(item), item)):
        if any(leq(other, vector) for other in out):
            continue
        out = [other for other in out if not leq(vector, other)]
        out.append(vector)
    return tuple(out)


def mixed_c_transition(left: PlacedEdge, right: PlacedEdge) -> bool:
    return (left.side == "c") != (right.side == "c")


def boundary_counts(demand: BoundaryDemand) -> Triple:
    counts = [0, 0, 0]
    for path in (demand.left_path, demand.right_path, demand.base_path):
        for edge in path:
            counts[SIDE_INDEX[edge.side]] += 1
    return tuple(counts)  # type: ignore[return-value]


def straight_boundary_transitions(demand: BoundaryDemand, *, mixed_only: bool) -> tuple[Transition, ...]:
    out: list[Transition] = []
    for side_name, path in (
        ("L", demand.left_path),
        ("R", demand.right_path),
        ("B", demand.base_path),
    ):
        for index, (left, right) in enumerate(zip(path, path[1:]), start=1):
            if mixed_only and not mixed_c_transition(left, right):
                continue
            out.append(Transition(side_name, index, left, right))
    return tuple(out)


def transition_options(
    transition: Transition,
    tile: SideLengths,
    *,
    max_pieces: int,
    mode: str,
) -> tuple[Triple, ...]:
    fans = overhang_fans(
        transition.left,
        transition.right,
        tile,
        max_pieces=max_pieces,
        mode=mode,
    )
    return pareto_minimal({component_counts(components) for _angles, components in fans})


def inventory_frontier(
    transitions: tuple[Transition, ...],
    tile: SideLengths,
    *,
    max_pieces: int,
    mode: str,
) -> tuple[Triple, ...] | None:
    frontier: tuple[Triple, ...] = ((0, 0, 0),)
    for transition in transitions:
        options = transition_options(transition, tile, max_pieces=max_pieces, mode=mode)
        if not options:
            return None
        frontier = pareto_minimal({add(base, option) for base in frontier for option in options})
    return frontier


def min_sum_vector(frontier: tuple[Triple, ...]) -> Triple:
    return min(frontier, key=lambda item: (sum(item), item))


def format_triple(triple: Triple) -> str:
    return f"({triple[0]},{triple[1]},{triple[2]})"


def print_transition_options(
    transitions: tuple[Transition, ...],
    tile: SideLengths,
    *,
    max_pieces: int,
    mode: str,
) -> None:
    for transition in transitions:
        options = transition_options(transition, tile, max_pieces=max_pieces, mode=mode)
        if options:
            option_text = ", ".join(format_triple(option) for option in options[:6])
            if len(options) > 6:
                option_text += f", ... {len(options) - 6} more"
        else:
            option_text = "none"
        print(
            f"    {transition.side_name}{transition.index}: "
            f"{edge_text(transition.left)} -> {edge_text(transition.right)} "
            f"options={len(options)} [{option_text}]"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--max-pieces", type=int, default=6)
    parser.add_argument("--mode", choices=("angle", "fan"), default="angle")
    parser.add_argument("--mixed-only", action="store_true")
    parser.add_argument("--show-transitions", action="store_true")
    args = parser.parse_args()

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
        for survivor in survivors:
            demand = best_demand_for_survivor(survivor)
            if demand is None:
                print("  no transition-demand witness")
                continue
            transitions = straight_boundary_transitions(demand, mixed_only=args.mixed_only)
            boundary = boundary_counts(demand)
            interior = tuple(n - boundary[i] for i in range(3))  # type: ignore[assignment]
            frontier = inventory_frontier(
                transitions,
                survivor.candidate.tile,
                max_pieces=args.max_pieces,
                mode=args.mode,
            )
            print(
                f"  tile={survivor.candidate.tile}; "
                f"L={path_labels(demand.left_path)} R={path_labels(demand.right_path)} "
                f"B={path_labels(demand.base_path)}"
            )
            print(f"  boundary={format_triple(boundary)} interior={format_triple(interior)}")
            print(
                f"  transitions={len(transitions)} "
                f"({'mixed only' if args.mixed_only else 'all straight boundary vertices'})"
            )
            if args.show_transitions:
                print_transition_options(
                    transitions,
                    survivor.candidate.tile,
                    max_pieces=args.max_pieces,
                    mode=args.mode,
                )
            if frontier is None:
                print("  no local fan option for at least one transition")
                continue
            feasible = tuple(vector for vector in frontier if leq(vector, interior))
            best = min_sum_vector(frontier)
            slack = tuple(interior[i] - best[i] for i in range(3))  # type: ignore[assignment]
            print(
                f"  fan-inventory frontier={len(frontier)}; "
                f"feasible-under-interior={len(feasible)}; "
                f"min-sum={format_triple(best)} slack={format_triple(slack)}"
            )


if __name__ == "__main__":
    main()
