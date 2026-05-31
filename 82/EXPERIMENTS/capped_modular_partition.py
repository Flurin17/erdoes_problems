#!/usr/bin/env python3
"""Exact modular partition checker for capped part sizes.

Unlike `modular_partition.py`, this script never builds all `2^n` subsets.
It enumerates only candidate parts up to `--max-part-size`, then runs an exact
cover search indexed by the first uncovered vertex.  This is intended for
terminal and small-excess experiments such as `n=25,q=5,max_part_size=7`.
"""

from __future__ import annotations

import argparse
import random
from functools import lru_cache
from itertools import combinations


class SearchLimitExceeded(RuntimeError):
    pass


def adjacency_masks(n: int, graph_mask: int) -> list[int]:
    adj = [0] * n
    edge = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (graph_mask >> edge) & 1:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            edge += 1
    return adj


def subset_from_vertices(vertices: tuple[int, ...]) -> int:
    subset = 0
    for vertex in vertices:
        subset |= 1 << vertex
    return subset


def is_modular_subset(subset: int, vertices: tuple[int, ...], modulus: int, adj: list[int]) -> bool:
    first = (adj[vertices[0]] & subset).bit_count() % modulus
    return all((adj[vertex] & subset).bit_count() % modulus == first for vertex in vertices[1:])


def generate_candidates(
    n: int,
    graph_mask: int,
    modulus: int,
    min_part_size: int,
    max_part_size: int,
) -> list[list[int]]:
    adj = adjacency_masks(n, graph_mask)
    by_pivot: list[list[int]] = [[] for _ in range(n)]
    for size in range(max(1, min_part_size), max_part_size + 1):
        for vertices in combinations(range(n), size):
            subset = subset_from_vertices(vertices)
            if is_modular_subset(subset, vertices, modulus, adj):
                for vertex in vertices:
                    by_pivot[vertex].append(subset)
    for choices in by_pivot:
        choices.sort(key=lambda subset: (subset.bit_count(), subset), reverse=True)
    return by_pivot


def find_partition(
    n: int,
    graph_mask: int,
    modulus: int,
    colors: int,
    min_part_size: int,
    max_part_size: int,
    node_limit: int | None,
) -> tuple[list[int] | None, int, int]:
    by_pivot = generate_candidates(n, graph_mask, modulus, min_part_size, max_part_size)
    full = (1 << n) - 1
    choices: dict[tuple[int, int], int] = {}
    nodes = 0
    branches = 0

    @lru_cache(maxsize=None)
    def rec(remaining: int, colors_left: int) -> bool:
        nonlocal nodes, branches
        nodes += 1
        if node_limit is not None and nodes + branches > node_limit:
            raise SearchLimitExceeded
        if remaining == 0:
            return True
        if colors_left == 0:
            return False
        remaining_size = remaining.bit_count()
        if remaining_size > colors_left * max_part_size:
            return False
        if min_part_size and remaining_size < min_part_size:
            return False

        pivot = (remaining & -remaining).bit_length() - 1
        for subset in by_pivot[pivot]:
            branches += 1
            if node_limit is not None and nodes + branches > node_limit:
                raise SearchLimitExceeded
            if subset & ~remaining:
                continue
            if rec(remaining ^ subset, colors_left - 1):
                choices[(remaining, colors_left)] = subset
                return True
        return False

    if not rec(full, colors):
        return None, nodes, branches

    assignment = [-1] * n
    remaining = full
    colors_left = colors
    color = 0
    while remaining:
        subset = choices[(remaining, colors_left)]
        for vertex in range(n):
            if (subset >> vertex) & 1:
                assignment[vertex] = color
        remaining ^= subset
        colors_left -= 1
        color += 1
    return assignment, nodes, branches


def assignment_stats(
    n: int,
    graph_mask: int,
    assignment: list[int],
    modulus: int,
) -> list[tuple[int, int, int]]:
    adj = adjacency_masks(n, graph_mask)
    out = []
    for color in sorted(set(assignment)):
        subset = 0
        for vertex, assigned in enumerate(assignment):
            if assigned == color:
                subset |= 1 << vertex
        if subset == 0:
            continue
        vertices = [vertex for vertex, assigned in enumerate(assignment) if assigned == color]
        residues = {(adj[vertex] & subset).bit_count() % modulus for vertex in vertices}
        residue = next(iter(residues)) if len(residues) == 1 else -1
        out.append((color, len(vertices), residue))
    return out


def sample_random(
    n: int,
    modulus: int,
    colors: int,
    min_part_size: int,
    max_part_size: int,
    node_limit: int | None,
    trials: int,
    seed: int,
) -> None:
    rng = random.Random(seed)
    edges = n * (n - 1) // 2
    limited = 0
    for trial in range(1, trials + 1):
        graph_mask = rng.getrandbits(edges)
        try:
            assignment, nodes, branches = find_partition(
                n,
                graph_mask,
                modulus,
                colors,
                min_part_size,
                max_part_size,
                node_limit,
            )
        except SearchLimitExceeded:
            limited += 1
            continue
        if assignment is None:
            print(f"n={n}")
            print(f"modulus={modulus}")
            print(f"colors={colors}")
            if min_part_size:
                print(f"min_part_size={min_part_size}")
            print(f"max_part_size={max_part_size}")
            print(f"trials={trials}")
            print(f"counterexample_trial={trial}")
            print(f"counterexample_mask={graph_mask}")
            print(f"nodes={nodes}")
            print(f"branches={branches}")
            return

    print(f"n={n}")
    print(f"modulus={modulus}")
    print(f"colors={colors}")
    if min_part_size:
        print(f"min_part_size={min_part_size}")
    print(f"max_part_size={max_part_size}")
    print(f"trials={trials}")
    print(f"limited={limited}")
    print("no_counterexample_seen")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("mask", type=int, nargs="?")
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--colors", type=int, required=True)
    parser.add_argument("--min-part-size", type=int, default=0)
    parser.add_argument("--max-part-size", type=int, required=True)
    parser.add_argument("--node-limit", type=int)
    parser.add_argument("--sample-random", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()

    if args.sample_random:
        sample_random(
            args.n,
            args.modulus,
            args.colors,
            args.min_part_size,
            args.max_part_size,
            args.node_limit,
            args.sample_random,
            args.seed,
        )
        return

    if args.mask is None:
        parser.error("mask is required unless --sample-random is used")

    try:
        assignment, nodes, branches = find_partition(
            args.n,
            args.mask,
            args.modulus,
            args.colors,
            args.min_part_size,
            args.max_part_size,
            args.node_limit,
        )
    except SearchLimitExceeded:
        print(f"n={args.n}")
        print(f"mask={args.mask}")
        print(f"modulus={args.modulus}")
        print(f"colors={args.colors}")
        print(f"max_part_size={args.max_part_size}")
        print("partition_exists=unknown_node_limit")
        return

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"modulus={args.modulus}")
    print(f"colors={args.colors}")
    if args.min_part_size:
        print(f"min_part_size={args.min_part_size}")
    print(f"max_part_size={args.max_part_size}")
    print(f"nodes={nodes}")
    print(f"branches={branches}")
    print(f"partition_exists={assignment is not None}")
    if assignment is not None:
        print("assignment=" + ",".join(map(str, assignment)))
        print(
            "parts="
            + " ".join(
                f"color{color}:size{size}:residue{residue}"
                for color, size, residue in assignment_stats(
                    args.n, args.mask, assignment, args.modulus
                )
            )
        )


if __name__ == "__main__":
    main()
