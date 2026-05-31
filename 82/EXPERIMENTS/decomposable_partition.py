#!/usr/bin/env python3
"""Exact checks for merge-decomposable modular partitions.

A target-modular set is merge-decomposable if it can be built from singleton
sets by repeatedly merging two already merge-decomposable sets whose union is
target-modular.  This script compares exact modular partitions with the
stronger merge-decomposable partitions.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
import random

import modular_partition
import regular_induced as ri


def modular_and_decomposable(
    n: int, graph_mask: int, modulus: int, pc: ri.Precomp | None = None
) -> tuple[list[bool], list[bool]]:
    if pc is None:
        pc = ri.precompute(n)
    modular = [False] * (1 << n)
    decomposable = [False] * (1 << n)
    modular[0] = True
    decomposable[0] = True

    by_size = sorted(range(1, 1 << n), key=int.bit_count)
    for subset in by_size:
        modular[subset] = modular_partition.residue_on(graph_mask, subset, modulus, pc) is not None
        if not modular[subset]:
            continue
        if subset.bit_count() == 1:
            decomposable[subset] = True
            continue
        pivot = subset & -subset
        sub = (subset - 1) & subset
        while sub:
            other = subset ^ sub
            if (sub & pivot) and other and decomposable[sub] and decomposable[other]:
                decomposable[subset] = True
                break
            sub = (sub - 1) & subset

    return modular, decomposable


def min_allowed_partition(n: int, allowed: list[bool]) -> tuple[int, list[int]]:
    full = (1 << n) - 1
    choice: dict[int, int] = {}

    @lru_cache(maxsize=None)
    def rec(remaining: int) -> int:
        if remaining == 0:
            return 0
        pivot = remaining & -remaining
        best = n + 1
        best_sub = 0
        sub = remaining
        while sub:
            if (sub & pivot) and allowed[sub]:
                value = 1 + rec(remaining ^ sub)
                if value < best:
                    best = value
                    best_sub = sub
            sub = (sub - 1) & remaining
        choice[remaining] = best_sub
        return best

    count = rec(full)
    assignment = [-1] * n
    remaining = full
    color = 0
    while remaining:
        sub = choice[remaining]
        for vertex in range(n):
            if (sub >> vertex) & 1:
                assignment[vertex] = color
        remaining ^= sub
        color += 1
    return count, assignment


def summarize(n: int, graph_mask: int, modulus: int, pc: ri.Precomp | None = None) -> dict[str, object]:
    modular, decomposable = modular_and_decomposable(n, graph_mask, modulus, pc)
    modular_count = sum(modular)
    decomposable_count = sum(decomposable)
    nondecomp = [
        subset
        for subset in range(1, 1 << n)
        if modular[subset] and not decomposable[subset]
    ]
    largest_nondecomp = max((subset.bit_count() for subset in nondecomp), default=0)
    modular_min, modular_assignment = min_allowed_partition(n, modular)
    decomp_min, decomp_assignment = min_allowed_partition(n, decomposable)
    return {
        "modular_count": modular_count,
        "decomposable_count": decomposable_count,
        "nondecomposable_count": len(nondecomp),
        "largest_nondecomposable": largest_nondecomp,
        "sample_nondecomposable": nondecomp[0] if nondecomp else 0,
        "modular_min": modular_min,
        "modular_assignment": modular_assignment,
        "decomp_min": decomp_min,
        "decomp_assignment": decomp_assignment,
    }


def analyze(n: int, graph_mask: int, modulus: int) -> None:
    summary = summarize(n, graph_mask, modulus)

    print(f"n={n}")
    print(f"mask={graph_mask}")
    print(f"modulus={modulus}")
    print(f"modular_subsets={summary['modular_count']}")
    print(f"decomposable_subsets={summary['decomposable_count']}")
    print(f"nondecomposable_modular_subsets={summary['nondecomposable_count']}")
    print(f"largest_nondecomposable_modular_size={summary['largest_nondecomposable']}")
    if summary["sample_nondecomposable"]:
        print(f"sample_nondecomposable_subset={summary['sample_nondecomposable']}")
    print(f"min_modular_parts={summary['modular_min']}")
    print("modular_assignment=" + ",".join(map(str, summary["modular_assignment"])))
    print(f"min_decomposable_parts={summary['decomp_min']}")
    print("decomposable_assignment=" + ",".join(map(str, summary["decomp_assignment"])))


def sample_parity(n: int, modulus: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    pair_histogram: dict[tuple[int, int], int] = {}
    gap_histogram: dict[int, int] = {}
    worst_gap = -1
    worst_mask = 0
    worst_pair = (0, 0)
    worst_nondecomp = 0
    for _ in range(trials):
        graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        assert graph_mask is not None
        summary = summarize(n, graph_mask, modulus, pc)
        pair = (int(summary["modular_min"]), int(summary["decomp_min"]))
        gap = pair[1] - pair[0]
        pair_histogram[pair] = pair_histogram.get(pair, 0) + 1
        gap_histogram[gap] = gap_histogram.get(gap, 0) + 1
        if gap > worst_gap or (gap == worst_gap and pair[1] > worst_pair[1]):
            worst_gap = gap
            worst_mask = graph_mask
            worst_pair = pair
            worst_nondecomp = int(summary["nondecomposable_count"])

    print(f"n={n}")
    print("parity=even")
    print(f"modulus={modulus}")
    print(f"trials={trials}")
    print(f"worst_gap={worst_gap}")
    print(f"worst_pair=min_modular,min_decomposable:{worst_pair[0]},{worst_pair[1]}")
    print(f"worst_nondecomposable_subsets={worst_nondecomp}")
    print(f"worst_mask={worst_mask}")
    print("histogram=gap:count")
    for key in sorted(gap_histogram):
        print(f"  {key}: {gap_histogram[key]}")
    print("histogram=min_modular,min_decomposable:count")
    for key in sorted(pair_histogram):
        print(f"  {key[0]},{key[1]}: {pair_histogram[key]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("mask", type=int, nargs="?")
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument("--sample-parity", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    if args.sample_parity:
        sample_parity(args.n, args.modulus, args.sample_parity, args.seed)
        return
    if args.mask is None:
        parser.error("mask is required unless --sample-parity is used")
    analyze(args.n, args.mask, args.modulus)


if __name__ == "__main__":
    main()
