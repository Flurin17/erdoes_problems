#!/usr/bin/env python3
"""Modular partition checks for fixed larger graph masks.

This is a memory-light companion to ``modular_partition.py``.  It avoids the
large incident-subset precompute and instead works directly with adjacency
bitmasks.  It is intended for one-off checks around 20--26 vertices, where a
full ``2^n`` allowed-subset table is still feasible but the older precompute is
not.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations


class SearchLimitExceeded(RuntimeError):
    pass


def adjacency_from_mask(n: int, graph_mask: int) -> list[int]:
    adjacency = [0] * n
    for index, (u, v) in enumerate(combinations(range(n), 2)):
        if (graph_mask >> index) & 1:
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
    return adjacency


def vertices_of(subset: int) -> list[int]:
    out = []
    rest = subset
    while rest:
        bit = rest & -rest
        out.append(bit.bit_length() - 1)
        rest ^= bit
    return out


def residue_on(adjacency: list[int], subset: int, modulus: int) -> int | None:
    residue: int | None = None
    rest = subset
    while rest:
        bit = rest & -rest
        vertex = bit.bit_length() - 1
        value = (adjacency[vertex] & subset).bit_count() % modulus
        if residue is None:
            residue = value
        elif value != residue:
            return None
        rest ^= bit
    return 0 if residue is None else residue


def is_connected(adjacency: list[int]) -> bool:
    n = len(adjacency)
    if n <= 1:
        return True
    seen = 1
    stack = [0]
    while stack:
        vertex = stack.pop()
        unseen = adjacency[vertex] & ~seen
        while unseen:
            bit = unseen & -unseen
            seen |= bit
            stack.append(bit.bit_length() - 1)
            unseen ^= bit
    return seen == (1 << n) - 1


def build_allowed(
    adjacency: list[int],
    modulus: int,
    required_residue: int | None,
    min_part_size: int,
    max_part_size: int | None,
) -> list[bool]:
    n = len(adjacency)
    allowed = [False] * (1 << n)
    allowed[0] = True
    for subset in range(1, 1 << n):
        size = subset.bit_count()
        if size < min_part_size:
            continue
        if max_part_size is not None and size > max_part_size:
            continue
        residue = residue_on(adjacency, subset, modulus)
        allowed[subset] = residue is not None and (
            required_residue is None or residue == required_residue
        )
    return allowed


def max_modular_order(adjacency: list[int], modulus: int) -> int:
    n = len(adjacency)
    for size in range(n, 0, -1):
        for vertices in combinations(range(n), size):
            subset = 0
            for vertex in vertices:
                subset |= 1 << vertex
            if residue_on(adjacency, subset, modulus) is not None:
                return size
    return 0


def find_partition_from_allowed(
    n: int,
    allowed: list[bool],
    colors: int,
    node_limit: int | None,
) -> list[int] | None:
    full = (1 << n) - 1
    by_pivot: list[list[int]] = [[] for _ in range(n)]
    max_allowed_size = 0
    for subset, ok in enumerate(allowed):
        if not ok or subset == 0:
            continue
        size = subset.bit_count()
        max_allowed_size = max(max_allowed_size, size)
        rest = subset
        while rest:
            bit = rest & -rest
            by_pivot[bit.bit_length() - 1].append(subset)
            rest ^= bit
    for choices_for_pivot in by_pivot:
        choices_for_pivot.sort(key=lambda item: (item.bit_count(), item), reverse=True)

    choices: dict[tuple[int, int], int] = {}
    nodes = 0
    branches = 0

    @lru_cache(maxsize=None)
    def rec(remaining: int, colors_left: int) -> bool:
        nonlocal branches, nodes
        nodes += 1
        if node_limit is not None and nodes + branches > node_limit:
            raise SearchLimitExceeded
        if remaining == 0:
            return True
        if colors_left == 0:
            return False
        if remaining.bit_count() > colors_left * max_allowed_size:
            return False

        pivot = remaining & -remaining
        pivot_index = pivot.bit_length() - 1
        for sub in by_pivot[pivot_index]:
            branches += 1
            if node_limit is not None and nodes + branches > node_limit:
                raise SearchLimitExceeded
            if (sub & ~remaining) == 0 and rec(remaining ^ sub, colors_left - 1):
                choices[(remaining, colors_left)] = sub
                return True
        return False

    if not rec(full, colors):
        return None

    assignment = [-1] * n
    remaining = full
    colors_left = colors
    color = 0
    while remaining:
        subset = choices[(remaining, colors_left)]
        for vertex in vertices_of(subset):
            assignment[vertex] = color
        remaining ^= subset
        colors_left -= 1
        color += 1
    return assignment


def find_min_colors(
    n: int,
    allowed: list[bool],
    max_colors: int,
    node_limit: int | None,
) -> tuple[int, list[int]] | None:
    for colors in range(1, max_colors + 1):
        assignment = find_partition_from_allowed(n, allowed, colors, node_limit)
        if assignment is not None:
            return colors, assignment
    return None


def assignment_stats(
    adjacency: list[int], assignment: list[int], modulus: int
) -> list[tuple[int, int, int]]:
    out = []
    for color in sorted(set(assignment)):
        subset = 0
        for vertex, assigned in enumerate(assignment):
            if assigned == color:
                subset |= 1 << vertex
        residue = residue_on(adjacency, subset, modulus)
        out.append((color, subset.bit_count(), -1 if residue is None else residue))
    return out


def degree_sequence(adjacency: list[int]) -> list[int]:
    return sorted(row.bit_count() for row in adjacency)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("mask", type=int)
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--required-residue", type=int)
    parser.add_argument("--min-part-size", type=int, default=0)
    parser.add_argument("--max-part-size", type=int)
    parser.add_argument("--find-min-colors", type=int)
    parser.add_argument("--colors", type=int)
    parser.add_argument("--max-modular-order", action="store_true")
    parser.add_argument("--node-limit", type=int)
    args = parser.parse_args()

    adjacency = adjacency_from_mask(args.n, args.mask)
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"modulus={args.modulus}")
    print("degree_sequence=" + ",".join(map(str, degree_sequence(adjacency))))
    print(f"connected={is_connected(adjacency)}")

    if args.max_modular_order:
        print(f"max_{args.modulus}_modular_order={max_modular_order(adjacency, args.modulus)}")

    if args.find_min_colors is None and args.colors is None:
        return

    allowed = build_allowed(
        adjacency,
        args.modulus,
        args.required_residue,
        args.min_part_size,
        args.max_part_size,
    )
    try:
        if args.find_min_colors is not None:
            result = find_min_colors(args.n, allowed, args.find_min_colors, args.node_limit)
            print(f"max_colors={args.find_min_colors}")
            print(f"min_colors={result[0] if result is not None else 'NA'}")
            if result is not None:
                print("assignment=" + ",".join(map(str, result[1])))
                print(
                    "parts="
                    + " ".join(
                        f"color{color}:size{size}:residue{residue}"
                        for color, size, residue in assignment_stats(
                            adjacency, result[1], args.modulus
                        )
                    )
                )
        else:
            assert args.colors is not None
            assignment = find_partition_from_allowed(
                args.n, allowed, args.colors, args.node_limit
            )
            print(f"colors={args.colors}")
            print(f"partition_exists={assignment is not None}")
            if assignment is not None:
                print("assignment=" + ",".join(map(str, assignment)))
                print(
                    "parts="
                    + " ".join(
                        f"color{color}:size{size}:residue{residue}"
                        for color, size, residue in assignment_stats(
                            adjacency, assignment, args.modulus
                        )
                    )
                )
    except SearchLimitExceeded:
        print("search_limited=True")


if __name__ == "__main__":
    main()
