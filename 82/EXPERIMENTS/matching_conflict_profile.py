#!/usr/bin/env python3
"""Conflict graph diagnostics for maximum matchings in fixed masks."""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations

import regular_bitset


def complement_adjacency(adj: list[int], n: int) -> list[int]:
    full = (1 << n) - 1
    return [((~adj[v]) & (full ^ (1 << v))) for v in range(n)]


def maximum_matching(adj: list[int], n: int) -> list[tuple[int, int]]:
    @lru_cache(maxsize=None)
    def solve(remaining: int) -> tuple[tuple[int, int], ...]:
        if remaining == 0:
            return ()
        v = (remaining & -remaining).bit_length() - 1
        best = solve(remaining & ~(1 << v))
        candidates = adj[v] & remaining & ~(1 << v)
        while candidates:
            bit = candidates & -candidates
            u = bit.bit_length() - 1
            rest = solve(remaining & ~(1 << v) & ~(1 << u))
            option = ((v, u),) + rest
            if len(option) > len(best):
                best = option
            candidates ^= bit
        return best

    return list(solve((1 << n) - 1))


def has_cross_edge(adj: list[int], edge_a: tuple[int, int], edge_b: tuple[int, int]) -> bool:
    a0, a1 = edge_a
    b0, b1 = edge_b
    bmask = (1 << b0) | (1 << b1)
    return bool((adj[a0] | adj[a1]) & bmask)


def conflict_adjacency(adj: list[int], matching: list[tuple[int, int]]) -> list[int]:
    m = len(matching)
    conflict = [0] * m
    for i, j in combinations(range(m), 2):
        if has_cross_edge(adj, matching[i], matching[j]):
            conflict[i] |= 1 << j
            conflict[j] |= 1 << i
    return conflict


def max_independent_set_order(adj: list[int]) -> int:
    m = len(adj)
    best = 0
    for subset in range(1 << m):
        size = subset.bit_count()
        if size <= best:
            continue
        if all((adj[v] & subset).bit_count() == 0 for v in range(m) if (subset >> v) & 1):
            best = size
    return best


def profile(name: str, adj: list[int], n: int) -> None:
    matching = maximum_matching(adj, n)
    conflict = conflict_adjacency(adj, matching)
    m = len(matching)
    conflict_edges = sum(row.bit_count() for row in conflict) // 2
    alpha = max_independent_set_order(conflict)
    avg = (2 * conflict_edges / m) if m else 0.0
    print(f"{name}_matching_size={m}")
    print(f"{name}_matching=" + ",".join(f"{u}-{v}" for u, v in matching))
    print(f"{name}_conflict_edges={conflict_edges}")
    print(f"{name}_conflict_average_degree={avg:.6g}")
    print(f"{name}_conflict_independence={alpha}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    args = parser.parse_args()

    adj = regular_bitset.build_adjacency(args.n, args.mask)
    comp = complement_adjacency(adj, args.n)
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    profile("graph", adj, args.n)
    profile("complement", comp, args.n)


if __name__ == "__main__":
    main()
