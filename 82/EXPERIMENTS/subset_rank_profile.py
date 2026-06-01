#!/usr/bin/env python3
"""Minimum induced-subset adjacency ranks by order for a fixed graph mask."""

from __future__ import annotations

import argparse
from itertools import combinations

import rank_profile


def induced_matrix(rows: list[list[int]], vertices: tuple[int, ...]) -> list[list[int]]:
    return [[rows[u][v] for v in vertices] for u in vertices]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--min-order", type=int, default=1)
    parser.add_argument("--max-order", type=int)
    parser.add_argument("--primes", default="2")
    parser.add_argument("--examples", action="store_true")
    args = parser.parse_args()

    rows = rank_profile.adjacency_rows(args.n, args.mask)
    primes = [int(item) for item in args.primes.split(",") if item]
    max_order = args.max_order or args.n

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"min_order={args.min_order}")
    print(f"max_order={max_order}")
    print("primes=" + ",".join(map(str, primes)))

    for order in range(args.min_order, max_order + 1):
        best: dict[int, tuple[int, tuple[int, ...]]] = {}
        best_shifted: dict[int, tuple[int, tuple[int, ...]]] = {}
        count = 0
        for vertices in combinations(range(args.n), order):
            count += 1
            matrix = induced_matrix(rows, vertices)
            for p in primes:
                rank = rank_profile.rank_mod_p(matrix, p)
                shifted_rank = rank_profile.rank_mod_p(
                    rank_profile.shifted_rows(matrix, 1, p), p
                )
                if p not in best or rank < best[p][0]:
                    best[p] = (rank, vertices)
                if p not in best_shifted or shifted_rank < best_shifted[p][0]:
                    best_shifted[p] = (shifted_rank, vertices)

        fields: list[str] = [f"order={order}", f"subsets={count}"]
        for p in primes:
            fields.append(f"min_rank_mod_{p}={best[p][0]}")
            fields.append(f"min_shifted_rank_mod_{p}={best_shifted[p][0]}")
            if args.examples:
                fields.append(
                    "rank_witness_mod_{}={}".format(
                        p, ",".join(map(str, best[p][1]))
                    )
                )
                fields.append(
                    "shifted_rank_witness_mod_{}={}".format(
                        p, ",".join(map(str, best_shifted[p][1]))
                    )
                )
        print(" ".join(fields))


if __name__ == "__main__":
    main()
