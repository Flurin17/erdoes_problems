#!/usr/bin/env python3
"""Inspect the upper-bit obstruction for self-labelled mod-4 colorings.

For a fixed high-bit labeling b, Lemma 4H says the low bit a can always be
chosen so that deg_same(v) == a_v (mod 2).  This script solves that affine
F_2 system and searches its solution space for one that also satisfies the
upper-bit condition floor(deg_same(v)/2) == b_v (mod 2).
"""

from __future__ import annotations

import argparse
import random

import regular_induced as ri


def adjacency_masks(n: int, graph_mask: int) -> list[int]:
    pc = ri.precompute(n)
    out = [0] * n
    for index, (i, j) in enumerate(pc.edges):
        if (graph_mask >> index) & 1:
            out[i] |= 1 << j
            out[j] |= 1 << i
    return out


def rref(rows: list[int], rhs: list[int], n: int) -> tuple[list[int], list[int], list[int]] | None:
    rows = rows[:]
    rhs = rhs[:]
    pivots: list[int] = []
    rank = 0
    for col in range(n):
        pivot = None
        for i in range(rank, len(rows)):
            if (rows[i] >> col) & 1:
                pivot = i
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        rhs[rank], rhs[pivot] = rhs[pivot], rhs[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
                rhs[i] ^= rhs[rank]
        pivots.append(col)
        rank += 1

    for i in range(rank, len(rows)):
        if rows[i] == 0 and rhs[i]:
            return None
    return rows[:rank], rhs[:rank], pivots


def lower_bit_system(
    n: int,
    graph_mask: int,
    high_bits: int,
) -> tuple[list[int], list[int]]:
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    rows: list[int] = []
    rhs: list[int] = []
    for v in range(n):
        row = 0
        degree_same_high = 0
        for u in range(n):
            if u == v:
                continue
            if ((high_bits >> u) & 1) != ((high_bits >> v) & 1):
                continue
            a, b = sorted((u, v))
            if (graph_mask >> edge_index[(a, b)]) & 1:
                degree_same_high += 1
                row ^= 1 << u
        if degree_same_high % 2 == 0:
            row ^= 1 << v
        rows.append(row)
        rhs.append(degree_same_high % 2)
    return rows, rhs


def enumerate_solutions(
    rows: list[int],
    rhs: list[int],
    pivots: list[int],
    n: int,
    max_solutions: int | None,
) -> list[int]:
    pivot_set = set(pivots)
    free = [i for i in range(n) if i not in pivot_set]
    count = 1 << len(free)
    if max_solutions is not None:
        count = min(count, max_solutions)
    solutions: list[int] = []
    for mask in range(count):
        x = 0
        for j, col in enumerate(free):
            if (mask >> j) & 1:
                x ^= 1 << col
        for row, value, pivot in reversed(list(zip(rows, rhs, pivots))):
            parity = (row & x).bit_count() & 1
            if parity != value:
                x ^= 1 << pivot
        solutions.append(x)
    return solutions


def upper_bit_ok(adj: list[int], high_bits: int, low_bits: int) -> bool:
    n = len(adj)
    label_masks = [0, 0, 0, 0]
    for v in range(n):
        label = ((low_bits >> v) & 1) + 2 * ((high_bits >> v) & 1)
        label_masks[label] |= 1 << v
    for v in range(n):
        label_v = ((low_bits >> v) & 1) + 2 * ((high_bits >> v) & 1)
        degree_same = (adj[v] & label_masks[label_v]).bit_count()
        if ((degree_same // 2) & 1) != ((high_bits >> v) & 1):
            return False
    return True


def inspect(
    n: int,
    graph_mask: int,
    samples: int,
    seed: int,
    max_solutions: int | None,
    fixed_high_bits: int | None,
    all_high_bits: bool,
) -> None:
    rng = random.Random(seed)
    adj = adjacency_masks(n, graph_mask)
    if all_high_bits:
        high_bit_masks = list(range(1 << n))
    elif fixed_high_bits is None:
        high_bit_masks = [rng.randrange(1 << n) for _ in range(samples)]
        high_bit_masks.extend([0, (1 << n) - 1])
    else:
        high_bit_masks = [fixed_high_bits]
    checked = 0
    total_solution_space = 0
    best_nullity = -1
    working_high_bits = 0
    first_solution: tuple[int, int] | None = None
    for high_bits in high_bit_masks:
        rows, rhs = lower_bit_system(n, graph_mask, high_bits)
        result = rref(rows, rhs, n)
        if result is None:
            print("lower_bit_inconsistent")
            print(f"high_bits={high_bits}")
            return
        rr, rr_rhs, pivots = result
        nullity = n - len(pivots)
        best_nullity = max(best_nullity, nullity)
        total_solution_space += 1 << nullity
        for low_bits in enumerate_solutions(rr, rr_rhs, pivots, n, max_solutions):
            if upper_bit_ok(adj, high_bits, low_bits):
                working_high_bits += 1
                if first_solution is None:
                    first_solution = (high_bits, low_bits)
                if all_high_bits:
                    break
                print(f"n={n}")
                print(f"mask={graph_mask}")
                print(f"samples={samples}")
                print(f"seed={seed}")
                if fixed_high_bits is not None:
                    print(f"fixed_high_bits={fixed_high_bits}")
                print(f"checked_high_bits={checked + 1}")
                print(f"best_nullity={best_nullity}")
                print("upper_bit_solution=yes")
                print(f"high_bits={high_bits}")
                print(f"low_bits={low_bits}")
                return
        checked += 1

    if all_high_bits:
        print(f"n={n}")
        print(f"mask={graph_mask}")
        print("mode=all_high_bits")
        print(f"checked_high_bits={checked}")
        print(f"best_nullity={best_nullity}")
        print(f"total_lower_solution_space={total_solution_space}")
        print(f"working_high_bits={working_high_bits}")
        if first_solution is not None:
            print(f"first_high_bits={first_solution[0]}")
            print(f"first_low_bits={first_solution[1]}")
        return

    print(f"n={n}")
    print(f"mask={graph_mask}")
    print(f"samples={samples}")
    print(f"seed={seed}")
    if fixed_high_bits is not None:
        print(f"fixed_high_bits={fixed_high_bits}")
    print(f"checked_high_bits={checked}")
    print(f"best_nullity={best_nullity}")
    print(f"total_lower_solution_space={total_solution_space}")
    print("upper_bit_solution=no_in_sample")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--samples", type=int, default=20)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--max-solutions", type=int)
    parser.add_argument("--high-bits", type=int)
    parser.add_argument("--all-high-bits", action="store_true")
    args = parser.parse_args()
    inspect(
        args.n,
        args.mask,
        args.samples,
        args.seed,
        args.max_solutions,
        args.high_bits,
        args.all_high_bits,
    )


if __name__ == "__main__":
    main()
