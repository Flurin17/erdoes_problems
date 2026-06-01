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


def complement_adjacency(adj: list[int], n: int) -> list[int]:
    full = (1 << n) - 1
    return [((~adj[v]) & (full ^ (1 << v))) for v in range(n)]


def complement_rows(rows: list[list[int]]) -> list[list[int]]:
    n = len(rows)
    return [[0 if i == j else 1 - rows[i][j] for j in range(n)] for i in range(n)]


def bucket_diameters(adj: list[int], vertices: list[int], n: int) -> tuple[int, int, int]:
    bucket_mask = 0
    for vertex in vertices:
        bucket_mask |= 1 << vertex
    full = (1 << n) - 1
    outside_mask = full ^ bucket_mask

    max_global = 0
    max_internal = 0
    max_external = 0
    for i, u in enumerate(vertices):
        for v in vertices[i + 1 :]:
            pair_mask = full ^ (1 << u) ^ (1 << v)
            diff = adj[u] ^ adj[v]
            max_global = max(max_global, (diff & pair_mask).bit_count())
            max_internal = max(max_internal, (diff & bucket_mask & pair_mask).bit_count())
            max_external = max(max_external, (diff & outside_mask).bit_count())
    return max_global, max_internal, max_external


def print_profile(name: str, adj: list[int], rows: list[list[int]], n: int, primes: list[int]) -> None:
    full = (1 << n) - 1
    buckets: dict[int, list[int]] = defaultdict(list)
    for vertex in range(n):
        buckets[(adj[vertex] & full).bit_count()].append(vertex)

    print(f"{name}_bucket_count={len(buckets)}")
    for degree in sorted(buckets):
        vertices = buckets[degree]
        matrix = induced_matrix(rows, vertices)
        regular_order, regular_degree = max_regular_in_vertices(adj, vertices)
        max_global, max_internal, max_external = bucket_diameters(adj, vertices, n)
        fields = [
            f"{name}_degree={degree}",
            f"size={len(vertices)}",
            "vertices=" + ",".join(map(str, vertices)),
            f"max_regular={regular_order}",
            f"regular_degree={regular_degree}",
            f"max_global_sigma={max_global}",
            f"max_internal_sigma={max_internal}",
            f"max_external_sigma={max_external}",
        ]
        for p in primes:
            rank = rank_profile.rank_mod_p(matrix, p)
            shifted_rank = rank_profile.rank_mod_p(
                rank_profile.shifted_rows(matrix, 1, p), p
            )
            fields.append(f"rank_mod_{p}={rank}")
            fields.append(f"shifted_rank_mod_{p}={shifted_rank}")
        print(" ".join(fields))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--primes", default="2")
    args = parser.parse_args()

    primes = [int(item) for item in args.primes.split(",") if item]
    adj = regular_bitset.build_adjacency(args.n, args.mask)
    rows = rank_profile.adjacency_rows(args.n, args.mask)
    comp_adj = complement_adjacency(adj, args.n)
    comp_rows = complement_rows(rows)

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print_profile("graph", adj, rows, args.n, primes)
    print_profile("complement", comp_adj, comp_rows, args.n, primes)


if __name__ == "__main__":
    main()
