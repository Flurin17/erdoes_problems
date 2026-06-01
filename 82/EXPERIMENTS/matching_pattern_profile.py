#!/usr/bin/env python3
"""Uniform cross-pattern blowups of a matching.

The graph has q matched pairs (a_i,b_i).  For each i<j the four bits of
`pattern` decide the cross edges a_i-a_j, a_i-b_j, b_i-a_j, b_i-b_j.
Each pair a_i-b_i is always an edge.
"""

from __future__ import annotations

import argparse

import regular_bitset


def build_pattern_graph(q: int, pattern: int) -> list[int]:
    n = 2 * q
    adj = [0] * n

    def add(u: int, v: int) -> None:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for i in range(q):
        add(2 * i, 2 * i + 1)
    for i in range(q):
        ai = 2 * i
        bi = 2 * i + 1
        for j in range(i + 1, q):
            aj = 2 * j
            bj = 2 * j + 1
            if pattern & 1:
                add(ai, aj)
            if pattern & 2:
                add(ai, bj)
            if pattern & 4:
                add(bi, aj)
            if pattern & 8:
                add(bi, bj)
    return adj


def adjacency_to_mask(adj: list[int]) -> int:
    n = len(adj)
    mask = 0
    edge_index = 0
    for u in range(n):
        for v in range(u + 1, n):
            if (adj[u] >> v) & 1:
                mask |= 1 << edge_index
            edge_index += 1
    return mask


def max_regular(adj: list[int]) -> tuple[int, int | None, tuple[int, ...] | None]:
    n = len(adj)
    for order in range(n, 0, -1):
        witness, degree, _checks = regular_bitset.find_regular_order(
            adj, n, order, max_checks=None
        )
        if witness is not None:
            return order, degree, witness
    return 0, None, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--pattern", type=int)
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    patterns = range(16) if args.all else [args.pattern]
    if not args.all and args.pattern is None:
        parser.error("--pattern is required unless --all is used")

    print(f"q={args.q}")
    best_min: tuple[int, list[int]] | None = None
    for pattern in patterns:
        adj = build_pattern_graph(args.q, pattern)
        order, degree, witness = max_regular(adj)
        if best_min is None or order < best_min[0]:
            best_min = (order, [pattern])
        elif order == best_min[0]:
            best_min[1].append(pattern)
        bits = format(pattern, "04b")
        print(
            f"pattern={pattern} bits={bits} max_regular={order} "
            f"degree={degree} witness="
            + (",".join(map(str, witness)) if witness is not None else "")
        )
    if args.all and best_min is not None:
        print(
            "minimum_max_regular={} patterns={}".format(
                best_min[0], ",".join(map(str, best_min[1]))
            )
        )


if __name__ == "__main__":
    main()
