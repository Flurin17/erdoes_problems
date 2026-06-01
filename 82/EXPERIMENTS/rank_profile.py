#!/usr/bin/env python3
"""Adjacency-rank diagnostics for fixed graph masks."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations

import regular_bitset


def adjacency_rows(n: int, mask: int) -> list[list[int]]:
    rows = [[0] * n for _ in range(n)]
    edge_index = 0
    for u, v in combinations(range(n), 2):
        if mask & (1 << edge_index):
            rows[u][v] = 1
            rows[v][u] = 1
        edge_index += 1
    return rows


def row_bitmasks(rows: list[list[int]]) -> list[int]:
    masks: list[int] = []
    for row in rows:
        value = 0
        for index, entry in enumerate(row):
            if entry:
                value |= 1 << index
        masks.append(value)
    return masks


def rank_mod_p(rows: list[list[int]], p: int) -> int:
    matrix = [[entry % p for entry in row] for row in rows]
    if not matrix:
        return 0
    height = len(matrix)
    width = len(matrix[0])
    rank = 0
    for col in range(width):
        pivot = None
        for row in range(rank, height):
            if matrix[row][col] % p:
                pivot = row
                break
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inv = pow(matrix[rank][col], -1, p)
        matrix[rank] = [(value * inv) % p for value in matrix[rank]]
        for row in range(height):
            if row == rank:
                continue
            factor = matrix[row][col] % p
            if factor:
                matrix[row] = [
                    (value - factor * pivot_value) % p
                    for value, pivot_value in zip(matrix[row], matrix[rank])
                ]
        rank += 1
        if rank == height:
            break
    return rank


def shifted_rows(rows: list[list[int]], shift: int, p: int) -> list[list[int]]:
    matrix = [[entry % p for entry in row] for row in rows]
    for index in range(min(len(matrix), len(matrix[0]) if matrix else 0)):
        matrix[index][index] = (matrix[index][index] + shift) % p
    return matrix


def max_regular_order(adj: list[int], n: int) -> tuple[int, int | None]:
    for order in range(n, 0, -1):
        witness, degree, _checks = regular_bitset.find_regular_order(
            adj, n, order, max_checks=None
        )
        if witness is not None:
            return order, degree
    return 0, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument(
        "--primes",
        default="2,3,5",
        help="comma-separated primes for modular rank diagnostics",
    )
    parser.add_argument("--regular", action="store_true")
    args = parser.parse_args()

    rows = adjacency_rows(args.n, args.mask)
    bit_rows = row_bitmasks(rows)
    row_counts = Counter(bit_rows)
    primes = [int(item) for item in args.primes.split(",") if item]

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"distinct_adjacency_rows={len(row_counts)}")
    print(f"max_identical_row_class={max(row_counts.values(), default=0)}")
    for p in primes:
        rank = rank_mod_p(rows, p)
        shifted_rank = rank_mod_p(shifted_rows(rows, 1, p), p)
        print(f"rank_mod_{p}={rank}")
        print(f"nullity_mod_{p}={args.n - rank}")
        print(f"rank_mod_{p}_A_plus_I={shifted_rank}")
        print(f"nullity_mod_{p}_A_plus_I={args.n - shifted_rank}")
        print(f"low_shifted_rank_clique_bound_mod_{p}={args.n / (2 ** shifted_rank):.6g}")
        if p == 2:
            print(f"low_rank_independent_bound={args.n / (2 ** rank):.6g}")
            print(f"kernel_even_witness_bound={args.n - rank}")
            print(f"kernel_odd_witness_bound={args.n - shifted_rank}")

    if args.regular:
        adj = regular_bitset.build_adjacency(args.n, args.mask)
        order, degree = max_regular_order(adj, args.n)
        print(f"max_regular_order={order}")
        print(f"witness_degree={degree}")


if __name__ == "__main__":
    main()
