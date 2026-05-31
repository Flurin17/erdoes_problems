#!/usr/bin/env python3
"""Exact low-mixed boundary-shell census for `gamma=2alpha` survivors.

This enumerates all angle-compatible boundary paths with the refined survivor
side-count representations whose total number of `c`/non-`c` boundary
transitions is at most a requested cap.  It then applies the same shell
overlap, residual-cycle, and residual corner-label filters used by the
randomized sampler.

The default cap `4` is the minimum currently observed for the `N=63` and
`N=99` benchmark survivors.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import (  # noqa: E402
    RefinedGamma2AlphaSurvivor,
    refined_survivors_for_n,
    viable_free_x_representations,
    viable_x_representations,
)
from gamma_2alpha_boundary_transition_demand import BoundaryDemand, path_labels  # noqa: E402
from gamma_2alpha_endpoint_automaton import PlacedEdge, alpha_corner, apex_corner  # noqa: E402
from gamma_2alpha_min_shell_census import ShellResult, classify_shell  # noqa: E402
from gamma_2alpha_random_shell_search import Path as BoundaryPath  # noqa: E402
from gamma_2alpha_random_shell_search import all_path_options, mixed_transitions  # noqa: E402


Triple = tuple[int, int, int]
EndpointMixed = tuple[PlacedEdge, PlacedEdge, int]


def paths_by_endpoint_and_mixed(rep: Triple) -> dict[EndpointMixed, tuple[BoundaryPath, ...]]:
    out: dict[EndpointMixed, list[BoundaryPath]] = defaultdict(list)
    for path in all_path_options(rep):
        out[(path[0], path[-1], mixed_transitions(path))].append(path)
    return {key: tuple(value) for key, value in out.items()}


def low_mixed_demands(
    survivor: RefinedGamma2AlphaSurvivor,
    *,
    max_total_mixed: int,
) -> tuple[BoundaryDemand, ...]:
    candidate = survivor.candidate
    bounded_reps = viable_x_representations(candidate)
    free_reps = viable_free_x_representations(candidate)
    base_reps = survivor.y_representations

    indexes = {
        rep: paths_by_endpoint_and_mixed(rep)
        for rep in set(bounded_reps + free_reps + base_reps)
    }
    demands: list[BoundaryDemand] = []

    def add(short_side: str, left_reps: tuple[Triple, ...], right_reps: tuple[Triple, ...]) -> None:
        for left_rep in left_reps:
            for right_rep in right_reps:
                for base_rep in base_reps:
                    left_index = indexes[left_rep]
                    right_index = indexes[right_rep]
                    base_index = indexes[base_rep]
                    for (left_first, left_last, left_mixed), left_paths in left_index.items():
                        for (right_first, right_last, right_mixed), right_paths in right_index.items():
                            if left_mixed + right_mixed > max_total_mixed - 1:
                                continue
                            if not apex_corner(left_last, right_first):
                                continue
                            for (base_first, base_last, base_mixed), base_paths in base_index.items():
                                total_mixed = left_mixed + right_mixed + base_mixed
                                if total_mixed > max_total_mixed:
                                    continue
                                if not alpha_corner(right_last, base_first):
                                    continue
                                if not alpha_corner(base_last, left_first):
                                    continue
                                for left in left_paths:
                                    for right in right_paths:
                                        for base in base_paths:
                                            demands.append(
                                                BoundaryDemand(
                                                    short_side=short_side,
                                                    left_rep=left_rep,
                                                    right_rep=right_rep,
                                                    base_rep=base_rep,
                                                    mixed_transitions=total_mixed,
                                                    left_path=left,
                                                    right_path=right,
                                                    base_path=base,
                                                )
                                            )

    add("left", bounded_reps, free_reps)
    add("right", free_reps, bounded_reps)

    # If the bounded and free X representation sets are equal, the two
    # short-side orientations enumerate the same oriented shell triples.
    seen: set[tuple[tuple[tuple[str, str, str], ...], ...]] = set()
    unique: list[BoundaryDemand] = []
    for demand in demands:
        key = (
            tuple((edge.side, edge.start, edge.end) for edge in demand.left_path),
            tuple((edge.side, edge.start, edge.end) for edge in demand.right_path),
            tuple((edge.side, edge.start, edge.end) for edge in demand.base_path),
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(demand)
    return tuple(unique)


def print_example(status: str, demand: BoundaryDemand, result: ShellResult) -> None:
    print(
        f"    {status}: forced={result.forced_corners}, "
        f"violations={result.label_violations}, "
        f"L={path_labels(demand.left_path)} "
        f"R={path_labels(demand.right_path)} "
        f"B={path_labels(demand.base_path)} "
        f"mixed={demand.mixed_transitions}"
    )


def census_n(n: int, *, max_total_mixed: int, show_examples: bool, stop_on_pass: bool) -> None:
    survivors = refined_survivors_for_n(n)
    print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
    for survivor in survivors:
        demands = low_mixed_demands(survivor, max_total_mixed=max_total_mixed)
        counts: Counter[str] = Counter()
        examples: dict[str, tuple[BoundaryDemand, ShellResult]] = {}
        print(f"  exact boundary shells with total mixed <= {max_total_mixed}: {len(demands)}", flush=True)
        for demand in demands:
            result = classify_shell(survivor, demand)
            counts[result.status] += 1
            examples.setdefault(result.status, (demand, result))
            if stop_on_pass and result.status == "passes-corner-label-check":
                print("  found shell passing current checks")
                print_example(result.status, demand, result)
                break
        print(f"  status counts={dict(sorted(counts.items()))}", flush=True)
        if show_examples:
            for status, (demand, result) in sorted(examples.items()):
                print_example(status, demand, result)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--max-total-mixed", type=int, default=4)
    parser.add_argument("--show-examples", action="store_true")
    parser.add_argument("--stop-on-pass", action="store_true")
    args = parser.parse_args()

    for n in args.n:
        census_n(
            n,
            max_total_mixed=args.max_total_mixed,
            show_examples=args.show_examples,
            stop_on_pass=args.stop_on_pass,
        )


if __name__ == "__main__":
    main()
