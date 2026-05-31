#!/usr/bin/env python3
"""Sample q-modular hosts and measure largest regular induced subgraphs."""

from __future__ import annotations

import argparse
import random

import modular_partition as mp
import regular_induced as ri


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--max-attempts", type=int, default=500000)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    pc = ri.precompute(args.n)
    edge_index = {edge: index for index, edge in enumerate(pc.edges)}
    full = (1 << args.n) - 1
    edge_count = len(pc.edges)

    checked = 0
    attempts = 0
    best = args.n
    best_mask = 0
    histogram: dict[int, int] = {}

    while checked < args.trials and attempts < args.max_attempts:
        attempts += 1
        graph_mask = mp.random_full_modular_candidate(
            args.n, args.q, edge_count, rng, pc, edge_index
        )
        if graph_mask is None or not ri.is_modular_on(graph_mask, full, args.q, pc):
            continue
        checked += 1
        value = ri.max_regular_order(graph_mask, pc)
        histogram[value] = histogram.get(value, 0) + 1
        if value < best:
            best = value
            best_mask = graph_mask

    print(f"q={args.q}")
    print(f"n={args.n}")
    print(f"trials={args.trials}")
    print(f"max_attempts={args.max_attempts}")
    print(f"attempts={attempts}")
    print(f"checked={checked}")
    print(f"best={best if checked else 'NA'}")
    print(f"best_mask={best_mask if checked else 'NA'}")
    print("histogram=max_regular_order:count")
    for value in sorted(histogram):
        print(f"  {value}: {histogram[value]}")


if __name__ == "__main__":
    main()
