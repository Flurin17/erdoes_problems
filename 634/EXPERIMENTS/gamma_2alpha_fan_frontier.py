#!/usr/bin/env python3
"""Aggregate boundary-fan frontier for `gamma=2alpha` survivors.

This strengthens `gamma_2alpha_boundary_fan_inventory.py` from one displayed
boundary word to all endpoint/mixed boundary-word classes.  It groups complete
boundary paths by first edge, last edge, mixed-transition count, and
Pareto-minimal local fan side-incidence vectors, then combines the three outer
sides at the triangle corners.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import refined_survivors_for_n, viable_x_representations  # noqa: E402
from gamma_2alpha_boundary_fan_inventory import add, format_triple, leq, pareto_minimal, transition_options  # noqa: E402
from gamma_2alpha_endpoint_automaton import PlacedEdge, alpha_corner, apex_corner  # noqa: E402
from gamma_2alpha_random_shell_search import all_path_options, mixed_transitions  # noqa: E402


Triple = tuple[int, int, int]
EndpointMixed = tuple[PlacedEdge, PlacedEdge, int]
FrontierIndex = dict[EndpointMixed, tuple[Triple, ...]]


@lru_cache(maxsize=None)
def cached_transition_options(left: PlacedEdge, right: PlacedEdge, tile: Triple, max_pieces: int, mode: str) -> tuple[Triple, ...]:
    class TransitionStub:
        def __init__(self, left: PlacedEdge, right: PlacedEdge) -> None:
            self.left = left
            self.right = right

    return transition_options(
        TransitionStub(left, right),
        tile,
        max_pieces=max_pieces,
        mode=mode,
    )


def combine_frontiers(left: tuple[Triple, ...], right: tuple[Triple, ...], limit: Triple | None = None) -> tuple[Triple, ...]:
    vectors = {add(left_vector, right_vector) for left_vector in left for right_vector in right}
    if limit is not None:
        vectors = {vector for vector in vectors if leq(vector, limit)}
    return pareto_minimal(vectors)


def path_frontier(path: tuple[PlacedEdge, ...], tile: Triple, *, max_pieces: int, mode: str) -> tuple[Triple, ...]:
    frontier: tuple[Triple, ...] = ((0, 0, 0),)
    for left, right in zip(path, path[1:]):
        options = cached_transition_options(left, right, tile, max_pieces, mode)
        if not options:
            return ()
        frontier = combine_frontiers(frontier, options)
    return frontier


def grouped_frontiers(rep: Triple, tile: Triple, *, max_pieces: int, mode: str) -> tuple[FrontierIndex, int]:
    grouped: defaultdict[EndpointMixed, set[Triple]] = defaultdict(set)
    path_count = 0
    for path in all_path_options(rep):
        path_count += 1
        frontier = path_frontier(path, tile, max_pieces=max_pieces, mode=mode)
        if not frontier:
            continue
        grouped[(path[0], path[-1], mixed_transitions(path))].update(frontier)
    return {key: pareto_minimal(value) for key, value in grouped.items()}, path_count


def frontier_summary(n: int, *, max_pieces: int, mode: str) -> None:
    survivors = refined_survivors_for_n(n)
    print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
    for survivor in survivors:
        tile = survivor.candidate.tile
        x_rep = viable_x_representations(survivor.candidate)[0]
        base_rep = survivor.y_representations[0]
        x_frontiers, x_paths = grouped_frontiers(x_rep, tile, max_pieces=max_pieces, mode=mode)
        base_frontiers, base_paths = grouped_frontiers(base_rep, tile, max_pieces=max_pieces, mode=mode)
        boundary = (
            2 * x_rep[0] + base_rep[0],
            2 * x_rep[1] + base_rep[1],
            2 * x_rep[2] + base_rep[2],
        )
        interior = tuple(n - boundary[index] for index in range(3))  # type: ignore[return-value]
        feasible = 0
        considered = 0
        by_mixed: Counter[int] = Counter()
        best: Triple | None = None
        for (left_first, left_last, left_mixed), left_frontier in x_frontiers.items():
            for (right_first, right_last, right_mixed), right_frontier in x_frontiers.items():
                if not apex_corner(left_last, right_first):
                    continue
                left_right = combine_frontiers(left_frontier, right_frontier, interior)
                if not left_right:
                    continue
                for (base_first, base_last, base_mixed), base_frontier in base_frontiers.items():
                    if not alpha_corner(right_last, base_first):
                        continue
                    if not alpha_corner(base_last, left_first):
                        continue
                    considered += 1
                    combined = combine_frontiers(left_right, base_frontier, interior)
                    if not combined:
                        continue
                    feasible += 1
                    by_mixed[left_mixed + right_mixed + base_mixed] += 1
                    candidate = min(combined, key=lambda vector: (sum(vector), vector))
                    if best is None or (sum(candidate), candidate) < (sum(best), best):
                        best = candidate
        print(f"  tile={tile} X={survivor.candidate.x} Y={survivor.candidate.y}")
        print(f"  x_rep={x_rep}: paths={x_paths}, endpoint/mixed groups={len(x_frontiers)}")
        print(f"  base_rep={base_rep}: paths={base_paths}, endpoint/mixed groups={len(base_frontiers)}")
        print(f"  boundary={format_triple(boundary)} interior={format_triple(interior)}")
        if best is None:
            print(f"  feasible endpoint/mixed groups=0 of {considered}")
            continue
        slack = tuple(interior[index] - best[index] for index in range(3))  # type: ignore[return-value]
        print(
            f"  feasible endpoint/mixed groups={feasible} of {considered}; "
            f"best={format_triple(best)} slack={format_triple(slack)}"
        )
        print(f"  feasible groups by mixed count={dict(sorted(by_mixed.items()))}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--max-pieces", type=int, default=6)
    parser.add_argument("--mode", choices=("angle", "fan"), default="angle")
    args = parser.parse_args()

    for n in args.n:
        frontier_summary(n, max_pieces=args.max_pieces, mode=args.mode)


if __name__ == "__main__":
    main()
