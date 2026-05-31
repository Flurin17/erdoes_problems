#!/usr/bin/env python3
"""Sample q-modular hosts and measure regular/modular induced subgraphs."""

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
    parser.add_argument(
        "--target-modulus",
        type=int,
        help="modulus to measure in induced witnesses; defaults to 2q",
    )
    args = parser.parse_args()
    if args.target_modulus is None:
        args.target_modulus = 2 * args.q

    rng = random.Random(args.seed)
    pc = ri.precompute(args.n)
    edge_index = {edge: index for index, edge in enumerate(pc.edges)}
    full = (1 << args.n) - 1
    edge_count = len(pc.edges)

    checked = 0
    attempts = 0
    best_regular = args.n
    best_regular_mask = 0
    regular_histogram: dict[int, int] = {}
    best_target = args.n
    best_target_mask = 0
    target_histogram: dict[int, int] = {}
    tradeoff_histogram: dict[tuple[int, int], int] = {}

    while checked < args.trials and attempts < args.max_attempts:
        attempts += 1
        graph_mask = mp.random_full_modular_candidate(
            args.n, args.q, edge_count, rng, pc, edge_index
        )
        if graph_mask is None or not ri.is_modular_on(graph_mask, full, args.q, pc):
            continue
        checked += 1
        regular_value = ri.max_regular_order(graph_mask, pc)
        target_value = ri.max_modular_order(graph_mask, args.target_modulus, pc)
        regular_histogram[regular_value] = regular_histogram.get(regular_value, 0) + 1
        target_histogram[target_value] = target_histogram.get(target_value, 0) + 1
        tradeoff = (regular_value, target_value)
        tradeoff_histogram[tradeoff] = tradeoff_histogram.get(tradeoff, 0) + 1
        if regular_value < best_regular:
            best_regular = regular_value
            best_regular_mask = graph_mask
        if target_value < best_target:
            best_target = target_value
            best_target_mask = graph_mask

    print(f"q={args.q}")
    print(f"target_modulus={args.target_modulus}")
    print(f"n={args.n}")
    print(f"trials={args.trials}")
    print(f"max_attempts={args.max_attempts}")
    print(f"attempts={attempts}")
    print(f"checked={checked}")
    print(f"best_max_regular_order={best_regular if checked else 'NA'}")
    print(f"best_regular_mask={best_regular_mask if checked else 'NA'}")
    print("histogram=max_regular_order:count")
    for value in sorted(regular_histogram):
        print(f"  {value}: {regular_histogram[value]}")
    print(f"best_max_{args.target_modulus}_modular_order={best_target if checked else 'NA'}")
    print(f"best_target_mask={best_target_mask if checked else 'NA'}")
    print(f"histogram=max_{args.target_modulus}_modular_order:count")
    for value in sorted(target_histogram):
        print(f"  {value}: {target_histogram[value]}")
    print("histogram=(max_regular_order,max_target_modular_order):count")
    for value in sorted(tradeoff_histogram):
        print(f"  {value}: {tradeoff_histogram[value]}")


if __name__ == "__main__":
    main()
