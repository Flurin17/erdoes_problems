#!/usr/bin/env python3
"""Chromatic pruning checks for the first dyadic lift.

The flexible first-lift question asks whether every even graph can be
partitioned into at most four induced subgraphs whose degrees are constant
modulo 4.  The chromatic certificate in PROOF.md removes graphs with
chi(G) <= 4 or chi(complement(G)) <= 4.  This script searches the remaining
high-chromatic region and tests the exact modular partition predicate.
"""

from __future__ import annotations

import argparse
import random

import modular_lift
import modular_partition
import regular_induced as ri


def complement_mask(graph_mask: int, pc: ri.Precomp) -> int:
    full_edges = (1 << len(pc.edges)) - 1
    return full_edges ^ graph_mask


def is_proper_colorable(
    n: int, graph_mask: int, colors: int, pc: ri.Precomp
) -> bool:
    color = [-1] * n
    order = sorted(
        range(n),
        key=lambda vertex: (graph_mask & pc.incident[(1 << n) - 1][vertex]).bit_count(),
        reverse=True,
    )

    def can_use(vertex: int, value: int) -> bool:
        for other in range(n):
            if color[other] != value:
                continue
            edge = (min(vertex, other), max(vertex, other))
            if edge in edge_index and (graph_mask >> edge_index[edge]) & 1:
                return False
        return True

    edge_index = {edge: idx for idx, edge in enumerate(pc.edges)}

    def rec(position: int, used: int) -> bool:
        if position == n:
            return True
        vertex = order[position]
        for value in range(min(used + 1, colors)):
            if can_use(vertex, value):
                color[vertex] = value
                if rec(position + 1, max(used, value + 1)):
                    return True
                color[vertex] = -1
        return False

    return rec(0, 0)


def chromatic_number(n: int, graph_mask: int, pc: ri.Precomp) -> int:
    for colors in range(1, n + 1):
        if is_proper_colorable(n, graph_mask, colors, pc):
            return colors
    return n


def graph_stats(n: int, graph_mask: int, pc: ri.Precomp) -> tuple[int, int, bool]:
    chi = chromatic_number(n, graph_mask, pc)
    chi_bar = chromatic_number(n, complement_mask(graph_mask, pc), pc)
    p4 = (
        modular_partition.find_partition(
            n,
            graph_mask,
            modulus=4,
            colors=4,
            node_limit=200_000,
        )
        is not None
    )
    return chi, chi_bar, p4


def sample_even(n: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: idx for idx, edge in enumerate(pc.edges)}
    high = 0
    high_examples: list[tuple[int, int, int]] = []
    failures: list[tuple[int, int, int]] = []
    histogram: dict[tuple[int, int], int] = {}
    for _ in range(trials):
        graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        assert graph_mask is not None
        chi, chi_bar, p4 = graph_stats(n, graph_mask, pc)
        histogram[(chi, chi_bar)] = histogram.get((chi, chi_bar), 0) + 1
        if chi >= 5 and chi_bar >= 5:
            high += 1
            if len(high_examples) < 5:
                high_examples.append((graph_mask, chi, chi_bar))
            if not p4 and len(failures) < 5:
                failures.append((graph_mask, chi, chi_bar))

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"seed={seed}")
    print(f"high_chromatic_candidates={high}")
    print(f"p4_failures={len(failures)}")
    print("histogram=chi,chi_complement:count")
    for key in sorted(histogram):
        print(f"  {key[0]},{key[1]}: {histogram[key]}")
    for graph_mask, chi, chi_bar in high_examples:
        print(f"high_mask={graph_mask} chi={chi} chi_complement={chi_bar}")
    for graph_mask, chi, chi_bar in failures:
        print(f"failure_mask={graph_mask} chi={chi} chi_complement={chi_bar}")


def fixed_mask(n: int, graph_mask: int) -> None:
    pc = ri.precompute(n)
    chi, chi_bar, p4 = graph_stats(n, graph_mask, pc)
    print(f"n={n}")
    print(f"mask={graph_mask}")
    print(f"chi={chi}")
    print(f"chi_complement={chi_bar}")
    print(f"has_4_part_4_modular_partition={p4}")


def exhaustive_even(n: int, limit: int | None) -> None:
    pc = ri.precompute(n)
    checked = 0
    high = 0
    high_examples: list[tuple[int, int, int]] = []
    failures: list[tuple[int, int, int]] = []
    for graph_mask in modular_lift.parity_graphs(n, odd=False):
        checked += 1
        chi, chi_bar, p4 = graph_stats(n, graph_mask, pc)
        if chi >= 5 and chi_bar >= 5:
            high += 1
            if len(high_examples) < 5:
                high_examples.append((graph_mask, chi, chi_bar))
            if not p4 and len(failures) < 5:
                failures.append((graph_mask, chi, chi_bar))
        if limit is not None and checked >= limit:
            break

    print(f"n={n}")
    print(f"exhaustive_even_checked={checked}")
    if limit is not None:
        print(f"limit={limit}")
    print(f"high_chromatic_candidates={high}")
    print(f"p4_failures={len(failures)}")
    for graph_mask, chi, chi_bar in high_examples:
        print(f"high_mask={graph_mask} chi={chi} chi_complement={chi_bar}")
    for graph_mask, chi, chi_bar in failures:
        print(f"failure_mask={graph_mask} chi={chi} chi_complement={chi_bar}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--sample-even", type=int, default=0)
    parser.add_argument("--exhaustive-even", action="store_true")
    parser.add_argument("--mask", type=int)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if args.mask is not None:
        fixed_mask(args.n, args.mask)
    elif args.sample_even:
        sample_even(args.n, args.sample_even, args.seed)
    elif args.exhaustive_even:
        exhaustive_even(args.n, args.limit)
    else:
        parser.error("choose --sample-even or --exhaustive-even")


if __name__ == "__main__":
    main()
