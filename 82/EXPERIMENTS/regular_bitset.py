#!/usr/bin/env python3
"""Memory-light fixed-mask regular induced subgraph checks.

This avoids the all-subset incident precomputation in regular_induced.py.
It is slower per subset but can inspect fixed graphs on moderately larger
orders when only a threshold or one witness is needed.
"""

from __future__ import annotations

import argparse
from itertools import combinations


def build_adjacency(n: int, mask: int) -> list[int]:
    adj = [0] * n
    edge_index = 0
    for u, v in combinations(range(n), 2):
        if mask & (1 << edge_index):
            adj[u] |= 1 << v
            adj[v] |= 1 << u
        edge_index += 1
    return adj


def subset_mask(vertices: tuple[int, ...]) -> int:
    mask = 0
    for vertex in vertices:
        mask |= 1 << vertex
    return mask


def regular_degree(adj: list[int], mask: int, vertices: tuple[int, ...]) -> int | None:
    first = (adj[vertices[0]] & mask).bit_count()
    for vertex in vertices[1:]:
        if (adj[vertex] & mask).bit_count() != first:
            return None
    return first


def find_regular_order(
    adj: list[int],
    n: int,
    order: int,
    max_checks: int | None,
) -> tuple[tuple[int, ...] | None, int | None, int]:
    checks = 0
    for vertices in combinations(range(n), order):
        checks += 1
        mask = subset_mask(vertices)
        degree = regular_degree(adj, mask, vertices)
        if degree is not None:
            return vertices, degree, checks
        if max_checks is not None and checks >= max_checks:
            return None, None, checks
    return None, None, checks


def degree_sequence(adj: list[int], n: int) -> list[int]:
    full = (1 << n) - 1
    return sorted((adj[vertex] & full).bit_count() for vertex in range(n))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--threshold", type=int)
    parser.add_argument("--max-checks-per-order", type=int)
    args = parser.parse_args()

    adj = build_adjacency(args.n, args.mask)
    start = args.n
    stop = args.threshold if args.threshold is not None else 1
    total_checks = 0

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print("degree_sequence=" + ",".join(map(str, degree_sequence(adj, args.n))))

    for order in range(start, stop - 1, -1):
        witness, degree, checks = find_regular_order(
            adj, args.n, order, args.max_checks_per_order
        )
        total_checks += checks
        if witness is not None:
            if args.threshold is None:
                print(f"max_regular_order={order}")
            else:
                print(f"has_regular_order_at_least_{args.threshold}=True")
                print(f"found_order={order}")
            print(f"witness_degree={degree}")
            print("witness=" + ",".join(map(str, witness)))
            print(f"subset_checks={total_checks}")
            return
        if args.max_checks_per_order is not None and checks >= args.max_checks_per_order:
            print(f"order_{order}_search_truncated_after={checks}")
            if args.threshold is not None:
                break

    if args.threshold is None:
        print("max_regular_order=0")
    else:
        print(f"has_regular_order_at_least_{args.threshold}=False")
    print(f"subset_checks={total_checks}")


if __name__ == "__main__":
    main()
