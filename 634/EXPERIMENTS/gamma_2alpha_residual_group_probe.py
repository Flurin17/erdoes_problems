#!/usr/bin/env python3
"""Stratified residual probe for `gamma=2alpha` outside-cover shell groups."""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import (  # noqa: E402
    refined_survivors_for_n,
    viable_free_x_representations,
    viable_x_representations,
)
from gamma_2alpha_boundary_transition_demand import BoundaryDemand  # noqa: E402
from gamma_2alpha_endpoint_automaton import PlacedEdge, alpha_corner, apex_corner  # noqa: E402
from gamma_2alpha_low_mixed_shell_census import paths_by_endpoint_and_mixed  # noqa: E402
from gamma_2alpha_residual_capped_census import (  # noqa: E402
    LocalCoverChecker,
    classify_shell,
)


def edge_text(edge: PlacedEdge) -> str:
    return f"{edge.side}:{edge.start}->{edge.end}"


def group_key(demand) -> str:
    return (
        f"m=({mixed(demand.left_path)},{mixed(demand.right_path)},{mixed(demand.base_path)}) "
        f"L={edge_text(demand.left_path[0])}..{edge_text(demand.left_path[-1])} "
        f"R={edge_text(demand.right_path[0])}..{edge_text(demand.right_path[-1])} "
        f"B={edge_text(demand.base_path[0])}..{edge_text(demand.base_path[-1])}"
    )


def mixed(path: tuple[PlacedEdge, ...]) -> int:
    return sum((left.side == "c") != (right.side == "c") for left, right in zip(path, path[1:]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--min-total-mixed", type=int, default=6)
    parser.add_argument("--max-total-mixed", type=int, default=6)
    parser.add_argument("--per-group", type=int, default=3)
    parser.add_argument("--limit", type=int, default=250000)
    parser.add_argument("--top", type=int, default=30)
    args = parser.parse_args()

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
        for survivor in survivors:
            radicand = exact.field_radicand(survivor)
            if radicand is None:
                print("  exact quadratic classifier unavailable", flush=True)
                continue
            local_checker = LocalCoverChecker(survivor, radicand)
            candidate = survivor.candidate
            bounded_reps = viable_x_representations(candidate)
            free_reps = viable_free_x_representations(candidate)
            base_reps = survivor.y_representations
            indexes = {
                rep: paths_by_endpoint_and_mixed(rep)
                for rep in set(bounded_reps + free_reps + base_reps)
            }
            generated = 0
            covered = 0
            diagnosed = 0
            group_counts: dict[str, Counter[str]] = defaultdict(Counter)
            endpoint_groups = 0

            for left_reps, right_reps, short_side in ((bounded_reps, free_reps, "left"),):
                for left_rep in left_reps:
                    for right_rep in right_reps:
                        for base_rep in base_reps:
                            for (left_first, left_last, left_mixed), left_paths in indexes[left_rep].items():
                                for (right_first, right_last, right_mixed), right_paths in indexes[right_rep].items():
                                    if not apex_corner(left_last, right_first):
                                        continue
                                    for (base_first, base_last, base_mixed), base_paths in indexes[base_rep].items():
                                        total_mixed = left_mixed + right_mixed + base_mixed
                                        if not args.min_total_mixed <= total_mixed <= args.max_total_mixed:
                                            continue
                                        if not alpha_corner(right_last, base_first):
                                            continue
                                        if not alpha_corner(base_last, left_first):
                                            continue
                                        endpoint_groups += 1
                                        group_done = False
                                        for left_path in left_paths:
                                            if group_done:
                                                break
                                            for right_path in right_paths:
                                                if group_done:
                                                    break
                                                for base_path in base_paths:
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
                                                    generated += 1
                                                    if generated > args.limit:
                                                        group_done = True
                                                        break
                                                    if local_checker.first_overlap(demand) is not None:
                                                        covered += 1
                                                        continue
                                                    key = group_key(demand)
                                                    if sum(group_counts[key].values()) >= args.per_group:
                                                        group_done = True
                                                        break
                                                    detail = classify_shell(survivor, demand, radicand)
                                                    diagnosed += 1
                                                    group_counts[key][detail.status] += 1
                                                    if sum(group_counts[key].values()) >= args.per_group:
                                                        group_done = True
                                                        break
            print(
                f"  generated={min(generated, args.limit)} covered={covered} "
                f"diagnosed={diagnosed} endpoint_groups={endpoint_groups} groups={len(group_counts)}",
                flush=True,
            )
            for key, counts in sorted(group_counts.items())[: args.top]:
                print(f"    {dict(sorted(counts.items()))}: {key}", flush=True)


if __name__ == "__main__":
    main()
