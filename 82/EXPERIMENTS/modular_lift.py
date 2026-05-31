#!/usr/bin/env python3
"""Exact and sampled checks for dyadic modular lifting."""

from __future__ import annotations

import argparse
import random

import regular_induced as ri


def parity_graphs(n: int, odd: bool = False):
    """Generate labelled graphs on n vertices with all degrees even or odd.

    Choose arbitrary edges among the first n-1 vertices, then force the edges
    to the last vertex to give the desired parity at those vertices.  The last
    vertex automatically has the desired parity when the requested parity is
    globally feasible.
    """
    if odd and n % 2:
        return
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    free_edges = [(i, j) for i in range(n - 1) for j in range(i + 1, n - 1)]
    target = 1 if odd else 0
    for choice in range(1 << len(free_edges)):
        mask = 0
        parities = [0] * n
        for bit, (i, j) in enumerate(free_edges):
            if (choice >> bit) & 1:
                idx = edge_index[(i, j)]
                mask |= 1 << idx
                parities[i] ^= 1
                parities[j] ^= 1
        for i in range(n - 1):
            if parities[i] != target:
                idx = edge_index[(i, n - 1)]
                mask |= 1 << idx
                parities[i] ^= 1
                parities[n - 1] ^= 1
        if parities[n - 1] == target:
            yield mask


def exact_parity_to_mod4(n: int, odd: bool) -> None:
    pc = ri.precompute(n)
    checked = 0
    best = n
    histogram: dict[int, int] = {}
    witnesses: list[int] = []
    for mask in parity_graphs(n, odd):
        checked += 1
        value = ri.max_modular_order(mask, 4, pc)
        histogram[value] = histogram.get(value, 0) + 1
        if value < best:
            best = value
            witnesses = [mask]
        elif value == best and len(witnesses) < 5:
            witnesses.append(mask)
    print(f"n={n}")
    print(f"parity={'odd' if odd else 'even'}")
    print(f"checked={checked}")
    print(f"minimum_max_4_modular_order={best if checked else 'NA'}")
    print("histogram=max_4_modular_order:count")
    for key in sorted(histogram):
        print(f"  {key}: {histogram[key]}")
    print("sample_extremal_graph_masks=" + ",".join(map(str, witnesses)))


def sample_parity_to_mod4(n: int, odd: bool, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    free_edges = [(i, j) for i in range(n - 1) for j in range(i + 1, n - 1)]
    target = 1 if odd else 0
    best = n
    histogram: dict[int, int] = {}
    best_mask = 0
    for _ in range(trials):
        mask = 0
        parities = [0] * n
        for i, j in free_edges:
            if rng.randrange(2):
                idx = edge_index[(i, j)]
                mask |= 1 << idx
                parities[i] ^= 1
                parities[j] ^= 1
        for i in range(n - 1):
            if parities[i] != target:
                idx = edge_index[(i, n - 1)]
                mask |= 1 << idx
                parities[i] ^= 1
                parities[n - 1] ^= 1
        if parities[n - 1] != target:
            continue
        value = ri.max_modular_order(mask, 4, pc)
        histogram[value] = histogram.get(value, 0) + 1
        if value < best:
            best = value
            best_mask = mask
    print(f"n={n}")
    print(f"parity={'odd' if odd else 'even'}")
    print(f"trials={trials}")
    print(f"accepted={sum(histogram.values())}")
    print(f"minimum_seen={best}")
    print(f"sample_witness_mask={best_mask}")
    print("histogram=max_4_modular_order:count")
    for key in sorted(histogram):
        print(f"  {key}: {histogram[key]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--odd", action="store_true")
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    if args.sample:
        sample_parity_to_mod4(args.n, args.odd, args.sample, args.seed)
    else:
        exact_parity_to_mod4(args.n, args.odd)


if __name__ == "__main__":
    main()
