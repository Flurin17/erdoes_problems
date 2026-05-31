#!/usr/bin/env python3
"""Random noncanonical boundary-shell search for `gamma=2alpha` survivors.

The endpoint-minimal census checks one canonical path for each oriented endpoint
pair.  This script samples from all angle-compatible boundary paths with the
same side-count representations, then applies the same shell overlap and
residual corner-label diagnostics.

This is deliberately a randomized diagnostic, not an impossibility proof.
"""

from __future__ import annotations

import argparse
import random
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path as FsPath


sys.path.insert(0, str(FsPath(__file__).resolve().parent))
from gamma_2alpha_boundary import (  # noqa: E402
    RefinedGamma2AlphaSurvivor,
    refined_survivors_for_n,
    viable_free_x_representations,
    viable_x_representations,
)
from gamma_2alpha_boundary_transition_demand import BoundaryDemand, path_labels  # noqa: E402
from gamma_2alpha_endpoint_automaton import (  # noqa: E402
    PlacedEdge,
    alpha_corner,
    apex_corner,
    orientations,
    straight_transition,
)
from gamma_2alpha_min_shell_census import ShellResult, classify_shell  # noqa: E402


Triple = tuple[int, int, int]
Path = tuple[PlacedEdge, ...]


def oriented_path_key(path: Path) -> tuple[tuple[str, str, str], ...]:
    return tuple((edge.side, edge.start, edge.end) for edge in path)


def mixed_transitions(path: Path) -> int:
    return sum((left.side == "c") != (right.side == "c") for left, right in zip(path, path[1:]))


@lru_cache(maxsize=None)
def all_path_options(rep: Triple) -> tuple[Path, ...]:
    placed_edges = tuple(edge for side in ("a", "b", "c") for edge in orientations(side))

    @lru_cache(maxsize=None)
    def completions(remaining: Triple, previous_index: int) -> tuple[tuple[int, ...], ...]:
        if remaining == (0, 0, 0):
            return ((),)
        out: list[tuple[int, ...]] = []
        previous = placed_edges[previous_index]
        for side_index, side in enumerate(("a", "b", "c")):
            if remaining[side_index] == 0:
                continue
            next_remaining = list(remaining)
            next_remaining[side_index] -= 1
            for edge_index, edge in enumerate(placed_edges):
                if edge.side != side:
                    continue
                if not straight_transition(previous, edge, "angle"):
                    continue
                for suffix in completions(tuple(next_remaining), edge_index):
                    out.append((edge_index, *suffix))
        return tuple(out)

    out: list[Path] = []
    for side_index, side in enumerate(("a", "b", "c")):
        if rep[side_index] == 0:
            continue
        remaining = list(rep)
        remaining[side_index] -= 1
        for edge_index, edge in enumerate(placed_edges):
            if edge.side != side:
                continue
            for suffix in completions(tuple(remaining), edge_index):
                out.append(tuple(placed_edges[index] for index in (edge_index, *suffix)))
    return tuple(out)


def by_first(paths: tuple[Path, ...]) -> dict[PlacedEdge, tuple[Path, ...]]:
    out: dict[PlacedEdge, list[Path]] = defaultdict(list)
    for path in paths:
        out[path[0]].append(path)
    return {key: tuple(value) for key, value in out.items()}


def by_first_last(paths: tuple[Path, ...]) -> dict[tuple[PlacedEdge, PlacedEdge], tuple[Path, ...]]:
    out: dict[tuple[PlacedEdge, PlacedEdge], list[Path]] = defaultdict(list)
    for path in paths:
        out[(path[0], path[-1])].append(path)
    return {key: tuple(value) for key, value in out.items()}


def choose_from_weighted_groups(
    rng: random.Random,
    groups: tuple[tuple[Path, ...], ...],
) -> Path | None:
    total = sum(len(group) for group in groups)
    if total == 0:
        return None
    choice = rng.randrange(total)
    for group in groups:
        if choice < len(group):
            return group[choice]
        choice -= len(group)
    raise AssertionError("unreachable")


def sampled_demands(
    survivor: RefinedGamma2AlphaSurvivor,
    *,
    rng: random.Random,
    samples: int,
) -> tuple[BoundaryDemand, ...]:
    candidate = survivor.candidate
    bounded_reps = viable_x_representations(candidate)
    free_reps = viable_free_x_representations(candidate)
    base_reps = survivor.y_representations
    demands: list[BoundaryDemand] = []
    seen: set[tuple[tuple[tuple[str, str, str], ...], ...]] = set()
    paths_by_rep = {
        rep: all_path_options(rep)
        for rep in set(bounded_reps + free_reps + base_reps)
    }
    first_index = {rep: by_first(paths) for rep, paths in paths_by_rep.items()}
    endpoint_index = {rep: by_first_last(paths) for rep, paths in paths_by_rep.items()}

    for _ in range(samples):
        left_rep = rng.choice(bounded_reps)
        right_rep = rng.choice(free_reps)
        base_rep = rng.choice(base_reps)
        left_paths = paths_by_rep[left_rep]
        right_by_first = first_index[right_rep]
        base_by_endpoints = endpoint_index[base_rep]

        left = rng.choice(left_paths)
        right_groups = tuple(
            group
            for first, group in right_by_first.items()
            if apex_corner(left[-1], first)
        )
        right = choose_from_weighted_groups(rng, right_groups)
        if right is None:
            continue
        base_groups = tuple(
            group
            for (first, last), group in base_by_endpoints.items()
            if alpha_corner(right[-1], first) and alpha_corner(last, left[0])
        )
        base = choose_from_weighted_groups(rng, base_groups)
        if base is None:
            continue
        key = (oriented_path_key(left), oriented_path_key(right), oriented_path_key(base))
        if key in seen:
            continue
        seen.add(key)
        demands.append(
            BoundaryDemand(
                short_side="sampled",
                left_rep=left_rep,
                right_rep=right_rep,
                base_rep=base_rep,
                mixed_transitions=(
                    mixed_transitions(left)
                    + mixed_transitions(right)
                    + mixed_transitions(base)
                ),
                left_path=left,
                right_path=right,
                base_path=base,
            )
        )
    return tuple(demands)


def print_example(status: str, demand: BoundaryDemand, result: ShellResult) -> None:
    print(
        f"    {status}: forced={result.forced_corners}, "
        f"violations={result.label_violations}, "
        f"L={path_labels(demand.left_path)} "
        f"R={path_labels(demand.right_path)} "
        f"B={path_labels(demand.base_path)} "
        f"mixed={demand.mixed_transitions}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--samples", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=634)
    parser.add_argument("--stop-on-pass", action="store_true")
    parser.add_argument("--show-examples", action="store_true")
    args = parser.parse_args()

    rng = random.Random(args.seed)
    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
        for survivor in survivors:
            demands = sampled_demands(survivor, rng=rng, samples=args.samples)
            counts: Counter[str] = Counter()
            examples: dict[str, tuple[BoundaryDemand, ShellResult]] = {}
            print(f"  sampled unique boundary cycles={len(demands)} from {args.samples} attempts")
            for demand in demands:
                result = classify_shell(survivor, demand)
                counts[result.status] += 1
                examples.setdefault(result.status, (demand, result))
                if args.stop_on_pass and result.status == "passes-corner-label-check":
                    print("  found shell passing current checks")
                    print_example(result.status, demand, result)
                    break
            print(f"  status counts={dict(sorted(counts.items()))}")
            if args.show_examples:
                for status, (demand, result) in sorted(examples.items()):
                    print_example(status, demand, result)


if __name__ == "__main__":
    main()
