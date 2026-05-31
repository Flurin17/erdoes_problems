#!/usr/bin/env python3
"""Generate compensated-double graphs with degree spread at most one.

Given a base graph F on m vertices with degrees d_i, the construction puts F
on side A, complement(F) on side B, and a bipartite graph X with row degrees
m-1-d_i and column degrees d_i+epsilon_i.  If X exists, the resulting graph on
2m vertices has degrees m-1 on A and m-1+epsilon_i on B.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations

import regular_induced as ri


def base_edges(m: int, rng: random.Random, p_num: int, p_den: int) -> set[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for i, j in combinations(range(m), 2):
        if rng.randrange(p_den) < p_num:
            edges.add((i, j))
    return edges


def degrees_from_edges(m: int, edges: set[tuple[int, int]]) -> list[int]:
    degrees = [0] * m
    for i, j in edges:
        degrees[i] += 1
        degrees[j] += 1
    return degrees


def bipartite_havel_hakimi(
    rows: list[int], cols: list[int], rng: random.Random
) -> set[tuple[int, int]] | None:
    if sum(rows) != sum(cols):
        return None
    col_remaining = list(cols)
    row_order = list(range(len(rows)))
    row_order.sort(key=lambda i: (rows[i], rng.random()), reverse=True)
    edges: set[tuple[int, int]] = set()
    for i in row_order:
        need = rows[i]
        if need < 0:
            return None
        choices = [j for j, value in enumerate(col_remaining) if value > 0]
        if need > len(choices):
            return None
        choices.sort(key=lambda j: (col_remaining[j], rng.random()), reverse=True)
        for j in choices[:need]:
            edges.add((i, j))
            col_remaining[j] -= 1
            if col_remaining[j] < 0:
                return None
    if any(col_remaining):
        return None
    return edges


def mask_from_parts(
    m: int, base: set[tuple[int, int]], cross: set[tuple[int, int]]
) -> int:
    n = 2 * m
    edge_index = {edge: idx for idx, edge in enumerate(combinations(range(n), 2))}
    mask = 0
    for i, j in base:
        mask |= 1 << edge_index[(i, j)]
    base_set = set(base)
    for i, j in combinations(range(m), 2):
        if (i, j) not in base_set:
            mask |= 1 << edge_index[(m + i, m + j)]
    for i, j in cross:
        a, b = i, m + j
        if a > b:
            a, b = b, a
        mask |= 1 << edge_index[(a, b)]
    return mask


def find_graph(args: argparse.Namespace) -> None:
    rng = random.Random(args.seed)
    n = 2 * args.m
    pc = ri.precompute(n)
    best = n
    best_mask = 0
    checked = 0
    accepted = 0
    histogram: dict[int, int] = {}

    for _ in range(args.trials):
        checked += 1
        base = base_edges(args.m, rng, args.p_num, args.p_den)
        degrees = degrees_from_edges(args.m, base)
        rows = [args.m - 1 - degree for degree in degrees]
        eps_count = sum(rows) - sum(degrees)
        if eps_count < 0 or eps_count > args.m:
            continue
        eps = [0] * args.m
        for index in rng.sample(range(args.m), eps_count):
            eps[index] = 1
        cols = [degree + eps_i for degree, eps_i in zip(degrees, eps)]
        cross = bipartite_havel_hakimi(rows, cols, rng)
        if cross is None:
            continue
        accepted += 1
        graph_mask = mask_from_parts(args.m, base, cross)
        value = ri.max_regular_order(graph_mask, pc)
        histogram[value] = histogram.get(value, 0) + 1
        if value < best:
            best = value
            best_mask = graph_mask
            print(f"accepted={accepted} best_regular={best} mask={best_mask}", flush=True)

    print(f"m={args.m}")
    print(f"n={n}")
    print(f"trials={args.trials}")
    print(f"accepted={accepted}")
    print(f"p={args.p_num}/{args.p_den}")
    print(f"best_regular={best if accepted else 'NA'}")
    print(f"best_mask={best_mask if accepted else 'NA'}")
    print("histogram=max_regular_order:count")
    for value in sorted(histogram):
        print(f"  {value}: {histogram[value]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, required=True, help="base graph order")
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--p-num", type=int, default=1)
    parser.add_argument("--p-den", type=int, default=4)
    args = parser.parse_args()
    if args.p_den <= 0 or not (0 <= args.p_num <= args.p_den):
        parser.error("need 0 <= --p-num <= --p-den")
    find_graph(args)


if __name__ == "__main__":
    main()
