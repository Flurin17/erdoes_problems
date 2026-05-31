#!/usr/bin/env python3
"""Stratified residual probe for `gamma=2alpha` outside-cover shell groups."""

from __future__ import annotations

import argparse
import json
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
from gamma_2alpha_overlap_remainder_inventory import path_profile, profile_signature  # noqa: E402
from gamma_2alpha_residual_capped_census import (  # noqa: E402
    LocalCoverChecker,
    classify_shell,
)
from gamma_2alpha_residual_chunked_census import LazyLocalCoverChecker  # noqa: E402


def edge_text(edge: PlacedEdge) -> str:
    return f"{edge.side}:{edge.start}->{edge.end}"


def group_key(demand) -> str:
    return (
        f"m=({mixed(demand.left_path)},{mixed(demand.right_path)},{mixed(demand.base_path)}) "
        f"L={edge_text(demand.left_path[0])}..{edge_text(demand.left_path[-1])} "
        f"R={edge_text(demand.right_path[0])}..{edge_text(demand.right_path[-1])} "
        f"B={edge_text(demand.base_path[0])}..{edge_text(demand.base_path[-1])}"
    )


def profile_key(demand, needed_positions: dict[str, tuple[int, ...]]) -> str:
    return profile_signature(
        path_profile(demand.left_path, needed_positions["L"]),
        path_profile(demand.right_path, needed_positions["R"]),
        path_profile(demand.base_path, needed_positions["B"]),
    )


def label_word(path: tuple[PlacedEdge, ...]) -> str:
    return "".join(edge.side for edge in path)


def word_key(demand) -> str:
    return (
        f"L={label_word(demand.left_path)} "
        f"R={label_word(demand.right_path)} "
        f"B={label_word(demand.base_path)}"
    )


def mixed(path: tuple[PlacedEdge, ...]) -> int:
    return sum((left.side == "c") != (right.side == "c") for left, right in zip(path, path[1:]))


def make_local_checker(survivor, radicand: int, mode: str):
    if mode == "eager":
        return LocalCoverChecker(survivor, radicand)
    if mode == "lazy":
        return LazyLocalCoverChecker(survivor, radicand)
    raise ValueError(mode)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--min-total-mixed", type=int, default=6)
    parser.add_argument("--max-total-mixed", type=int, default=6)
    parser.add_argument("--per-group", type=int, default=3)
    parser.add_argument("--limit", type=int, default=250000)
    parser.add_argument("--top", type=int, default=30)
    parser.add_argument("--group-by", choices=("endpoint", "profile", "word"), default="endpoint")
    parser.add_argument("--local-cover-mode", choices=("eager", "lazy"), default="eager")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    results = []
    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
        for survivor in survivors:
            radicand = exact.field_radicand(survivor)
            if radicand is None:
                print("  exact quadratic classifier unavailable", flush=True)
                continue
            local_checker = make_local_checker(survivor, radicand, args.local_cover_mode)
            needed_positions = {
                "L": tuple(sorted({pair.side_position for pair in local_checker.active_pairs if pair.side == "L"})),
                "R": tuple(sorted({pair.side_position for pair in local_checker.active_pairs if pair.side == "R"})),
                "B": tuple(sorted({pair.base_position for pair in local_checker.active_pairs})),
            }
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
                                                    if args.group_by == "endpoint":
                                                        key = group_key(demand)
                                                    elif args.group_by == "profile":
                                                        key = profile_key(demand, needed_positions)
                                                    else:
                                                        key = word_key(demand)
                                                    if sum(group_counts[key].values()) >= args.per_group:
                                                        if args.group_by == "endpoint":
                                                            group_done = True
                                                            break
                                                        continue
                                                    detail = classify_shell(survivor, demand, radicand)
                                                    diagnosed += 1
                                                    group_counts[key][detail.status] += 1
                                                    if sum(group_counts[key].values()) >= args.per_group:
                                                        if args.group_by == "endpoint":
                                                            group_done = True
                                                            break
            print(
                f"  generated={min(generated, args.limit)} covered={covered} "
                f"diagnosed={diagnosed} endpoint_groups={endpoint_groups} "
                f"{args.group_by}_groups={len(group_counts)}",
                flush=True,
            )
            status_signatures = Counter(tuple(sorted(counts.items())) for counts in group_counts.values())
            mixed_status_groups = sum(1 for counts in group_counts.values() if len(counts) > 1)
            print(
                f"  mixed_status_groups={mixed_status_groups} "
                f"status_signatures={len(status_signatures)}",
                flush=True,
            )
            for signature, count in status_signatures.most_common(args.top):
                print(f"    {count} groups with {dict(signature)}", flush=True)
            for key, counts in sorted(group_counts.items())[: args.top]:
                print(f"    {dict(sorted(counts.items()))}: {key}", flush=True)
            results.append(
                {
                    "n": n,
                    "tile": survivor.candidate.tile,
                    "min_total_mixed": args.min_total_mixed,
                    "max_total_mixed": args.max_total_mixed,
                    "per_group": args.per_group,
                    "limit": args.limit,
                    "group_by": args.group_by,
                    "local_cover_mode": args.local_cover_mode,
                    "generated": min(generated, args.limit),
                    "covered": covered,
                    "diagnosed": diagnosed,
                    "endpoint_groups": endpoint_groups,
                    "groups": len(group_counts),
                    "mixed_status_groups": mixed_status_groups,
                    "status_signatures": {
                        json.dumps(dict(signature), sort_keys=True): count
                        for signature, count in sorted(status_signatures.items())
                    },
                }
            )
    if args.json_out is not None:
        payload = results[0] if len(results) == 1 else results
        args.json_out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
