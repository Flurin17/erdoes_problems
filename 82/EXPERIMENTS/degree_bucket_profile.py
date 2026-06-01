#!/usr/bin/env python3
"""Exact-degree bucket diagnostics for fixed graph masks."""

from __future__ import annotations

import argparse
from collections import defaultdict

import rank_profile
import regular_bitset


def induced_matrix(rows: list[list[int]], vertices: list[int]) -> list[list[int]]:
    return [[rows[u][v] for v in vertices] for u in vertices]


def max_regular_in_vertices(adj: list[int], vertices: list[int]) -> tuple[int, int | None]:
    if not vertices:
        return 0, None
    local_count = len(vertices)
    local_adj = [0] * local_count
    index = {vertex: i for i, vertex in enumerate(vertices)}
    for u in vertices:
        i = index[u]
        for v in vertices:
            j = index[v]
            if i < j and ((adj[u] >> v) & 1):
                local_adj[i] |= 1 << j
                local_adj[j] |= 1 << i
    for order in range(local_count, 0, -1):
        witness, degree, _checks = regular_bitset.find_regular_order(
            local_adj, local_count, order, max_checks=None
        )
        if witness is not None:
            return order, degree
    return 0, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--primes", default="2")
    args = parser.parse_args()

    adj = regular_bitset.build_adjacency(args.n, args.mask)
    rows = rank_profile.adjacency_rows(args.n, args.mask)
    full = (1 << args.n) - 1
    buckets: dict[int, list[int]] = defaultdict(list)
    for vertex in range(args.n):
        buckets[(adj[vertex] & full).bit_count()].append(vertex)

    primes = [int(item) for item in args.primes.split(",") if item]
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"bucket_count={len(buckets)}")
    for degree in sorted(buckets):
        vertices = buckets[degree]
        matrix = induced_matrix(rows, vertices)
        regular_order, regular_degree = max_regular_in_vertices(adj, vertices)
        fields = [
            f"degree={degree}",
            f"size={len(vertices)}",
            "vertices=" + ",".join(map(str, vertices)),
            f"max_regular={regular_order}",
            f"regular_degree={regular_degree}",
        ]
        for p in primes:
            rank = rank_profile.rank_mod_p(matrix, p)
            shifted_rank = rank_profile.rank_mod_p(
                rank_profile.shifted_rows(matrix, 1, p), p
            )
            fields.append(f"rank_mod_{p}={rank}")
            fields.append(f"shifted_rank_mod_{p}={shifted_rank}")
        print(" ".join(fields))


if __name__ == "__main__":
    main()
