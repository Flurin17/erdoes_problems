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
import bisect
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


def by_mixed(paths: tuple[Path, ...]) -> dict[int, tuple[Path, ...]]:
    out: dict[int, list[Path]] = defaultdict(list)
    for path in paths:
        out[mixed_transitions(path)].append(path)
    return {key: tuple(value) for key, value in out.items()}


def by_endpoint_and_mixed(paths: tuple[Path, ...]) -> dict[tuple[PlacedEdge, PlacedEdge, int], tuple[Path, ...]]:
    out: dict[tuple[PlacedEdge, PlacedEdge, int], list[Path]] = defaultdict(list)
    for path in paths:
        out[(path[0], path[-1], mixed_transitions(path))].append(path)
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
    max_total_mixed: int | None,
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
    mixed_index = {rep: by_mixed(paths) for rep, paths in paths_by_rep.items()}
    first_mixed_index = {
        rep: {mixed: by_first(paths) for mixed, paths in by_mixed(paths_by_rep[rep]).items()}
        for rep in paths_by_rep
    }
    endpoint_mixed_index = {
        rep: {mixed: by_first_last(paths) for mixed, paths in by_mixed(paths_by_rep[rep]).items()}
        for rep in paths_by_rep
    }

    def choose_uncapped(left_rep: Triple, right_rep: Triple, base_rep: Triple) -> tuple[Path, Path, Path] | None:
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
            return None
        base_groups = tuple(
            group
            for (first, last), group in base_by_endpoints.items()
            if alpha_corner(right[-1], first) and alpha_corner(last, left[0])
        )
        base = choose_from_weighted_groups(rng, base_groups)
        if base is None:
            return None
        return left, right, base

    def choose_capped(left_rep: Triple, right_rep: Triple, base_rep: Triple, cap: int) -> tuple[Path, Path, Path] | None:
        mixed_choices = [
            (left_mixed, right_mixed, base_mixed)
            for left_mixed in mixed_index[left_rep]
            for right_mixed in mixed_index[right_rep]
            for base_mixed in mixed_index[base_rep]
            if left_mixed + right_mixed + base_mixed <= cap
        ]
        if not mixed_choices:
            return None
        left_mixed, right_mixed, base_mixed = rng.choice(mixed_choices)
        left = rng.choice(mixed_index[left_rep][left_mixed])
        right_by_first = first_mixed_index[right_rep][right_mixed]
        right_groups = tuple(
            group
            for first, group in right_by_first.items()
            if apex_corner(left[-1], first)
        )
        right = choose_from_weighted_groups(rng, right_groups)
        if right is None:
            return None
        base_by_endpoints = endpoint_mixed_index[base_rep][base_mixed]
        base_groups = tuple(
            group
            for (first, last), group in base_by_endpoints.items()
            if alpha_corner(right[-1], first) and alpha_corner(last, left[0])
        )
        base = choose_from_weighted_groups(rng, base_groups)
        if base is None:
            return None
        return left, right, base

    for _ in range(samples):
        left_rep = rng.choice(bounded_reps)
        right_rep = rng.choice(free_reps)
        base_rep = rng.choice(base_reps)
        chosen = (
            choose_uncapped(left_rep, right_rep, base_rep)
            if max_total_mixed is None
            else choose_capped(left_rep, right_rep, base_rep, max_total_mixed)
        )
        if chosen is None:
            continue
        left, right, base = chosen
        key = (oriented_path_key(left), oriented_path_key(right), oriented_path_key(base))
        if key in seen:
            continue
        total_mixed = (
            mixed_transitions(left)
            + mixed_transitions(right)
            + mixed_transitions(base)
        )
        if max_total_mixed is not None and total_mixed > max_total_mixed:
            continue
        seen.add(key)
        demands.append(
            BoundaryDemand(
                short_side="sampled",
                left_rep=left_rep,
                right_rep=right_rep,
                base_rep=base_rep,
                mixed_transitions=total_mixed,
                left_path=left,
                right_path=right,
                base_path=base,
            )
        )
    return tuple(demands)


def weighted_valid_demands(
    survivor: RefinedGamma2AlphaSurvivor,
    *,
    rng: random.Random,
    samples: int,
    max_total_mixed: int | None,
) -> tuple[BoundaryDemand, ...]:
    candidate = survivor.candidate
    bounded_reps = viable_x_representations(candidate)
    free_reps = viable_free_x_representations(candidate)
    base_reps = survivor.y_representations
    reps = set(bounded_reps + free_reps + base_reps)
    indexes = {rep: by_endpoint_and_mixed(all_path_options(rep)) for rep in reps}
    groups: list[
        tuple[
            int,
            str,
            Triple,
            Triple,
            Triple,
            tuple[Path, ...],
            tuple[Path, ...],
            tuple[Path, ...],
            int,
        ]
    ] = []

    def add_groups(short_side: str, left_reps: tuple[Triple, ...], right_reps: tuple[Triple, ...]) -> None:
        for left_rep in left_reps:
            for right_rep in right_reps:
                for base_rep in base_reps:
                    left_index = indexes[left_rep]
                    right_index = indexes[right_rep]
                    base_index = indexes[base_rep]
                    for (left_first, left_last, left_mixed), left_paths in left_index.items():
                        for (right_first, right_last, right_mixed), right_paths in right_index.items():
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
                                weight = len(left_paths) * len(right_paths) * len(base_paths)
                                groups.append(
                                    (
                                        weight,
                                        short_side,
                                        left_rep,
                                        right_rep,
                                        base_rep,
                                        left_paths,
                                        right_paths,
                                        base_paths,
                                        total_mixed,
                                    )
                                )

    add_groups("left", bounded_reps, free_reps)
    if bounded_reps != free_reps:
        add_groups("right", free_reps, bounded_reps)
    if not groups:
        return ()

    cumulative: list[int] = []
    total = 0
    for weight, *_rest in groups:
        total += weight
        cumulative.append(total)

    demands: list[BoundaryDemand] = []
    seen: set[tuple[tuple[tuple[str, str, str], ...], ...]] = set()
    for _ in range(samples):
        group = groups[bisect.bisect_right(cumulative, rng.randrange(total))]
        (
            _weight,
            short_side,
            left_rep,
            right_rep,
            base_rep,
            left_paths,
            right_paths,
            base_paths,
            total_mixed,
        ) = group
        left = rng.choice(left_paths)
        right = rng.choice(right_paths)
        base = rng.choice(base_paths)
        key = (oriented_path_key(left), oriented_path_key(right), oriented_path_key(base))
        if key in seen:
            continue
        seen.add(key)
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
    parser.add_argument(
        "--max-total-mixed",
        type=int,
        help="only keep sampled boundary cycles with at most this many c/non-c transitions",
    )
    parser.add_argument("--stop-on-pass", action="store_true")
    parser.add_argument("--show-examples", action="store_true")
    parser.add_argument("--by-mixed", action="store_true", help="also print status counts grouped by total mixed transitions")
    parser.add_argument(
        "--valid-weighted",
        action="store_true",
        help="sample directly from valid endpoint/mixed groups, weighted by boundary-shell count",
    )
    parser.add_argument(
        "--exact-quadratic",
        action="store_true",
        help="classify sampled shells with the exact Q(sqrt(d)) classifier",
    )
    args = parser.parse_args()

    exact_classifier = None
    field_radicand = None
    if args.exact_quadratic:
        from gamma_2alpha_quadratic_shell_census import classify_quadratic_shell, field_radicand as exact_radicand

        exact_classifier = classify_quadratic_shell
        field_radicand = exact_radicand

    rng = random.Random(args.seed)
    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
        for survivor in survivors:
            sampler = weighted_valid_demands if args.valid_weighted else sampled_demands
            demands = sampler(survivor, rng=rng, samples=args.samples, max_total_mixed=args.max_total_mixed)
            counts: Counter[str] = Counter()
            mixed_counts: dict[int, Counter[str]] = defaultdict(Counter)
            examples: dict[str, tuple[BoundaryDemand, ShellResult]] = {}
            suffix = ""
            if args.max_total_mixed is not None:
                suffix = f" with total mixed <= {args.max_total_mixed}"
            mode_text = "valid-weighted " if args.valid_weighted else ""
            print(f"  {mode_text}sampled unique boundary cycles={len(demands)} from {args.samples} attempts{suffix}")
            radicand = field_radicand(survivor) if field_radicand is not None else None
            for demand in demands:
                if exact_classifier is None:
                    result = classify_shell(survivor, demand)
                elif radicand is None:
                    result = ShellResult("not-quadratic", 0, 0)
                else:
                    result = exact_classifier(survivor, demand, radicand)
                counts[result.status] += 1
                mixed_counts[demand.mixed_transitions][result.status] += 1
                examples.setdefault(result.status, (demand, result))
                if args.stop_on_pass and result.status == "passes-corner-label-check":
                    print("  found shell passing current checks")
                    print_example(result.status, demand, result)
                    break
            print(f"  status counts={dict(sorted(counts.items()))}")
            if args.by_mixed:
                for mixed, statuses in sorted(mixed_counts.items()):
                    print(f"    mixed={mixed}: {dict(sorted(statuses.items()))}")
            if args.show_examples:
                for status, (demand, result) in sorted(examples.items()):
                    print_example(status, demand, result)


if __name__ == "__main__":
    main()
