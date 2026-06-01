#!/usr/bin/env python3
"""Sample two-degree q-modular graphs and measure flexible 2q partitions."""

from __future__ import annotations

import argparse
import random

import large_modular_partition as lmp
import two_level_modular_sample as tl


def sample(args: argparse.Namespace) -> None:
    rng = random.Random(args.seed)
    high = args.low_degree + args.q
    degree_sequence = [args.low_degree] * args.low_count + [high] * (
        args.n - args.low_count
    )
    if len(degree_sequence) != args.n:
        raise SystemExit("--low-count must be between 0 and n")
    if sum(degree_sequence) % 2:
        raise SystemExit("degree sum is odd")

    attempts = 0
    accepted = 0
    limited = 0
    histogram: dict[int | str, int] = {}
    witness_histogram: dict[int, int] = {}
    best_colors = 0
    best_mask = 0
    best_witness = args.n + 1
    best_witness_mask = 0

    while accepted < args.trials and attempts < args.max_attempts:
        attempts += 1
        degrees = degree_sequence[:]
        rng.shuffle(degrees)
        edges = tl.havel_hakimi_random(degrees, rng)
        if edges is None:
            continue
        edges = tl.randomize_by_swaps(edges, args.n, args.swaps, rng)
        adjacency = tl.adjacency_from_edges(edges, args.n)
        if args.connected_only and not tl.is_connected_adjacency(adjacency, args.n):
            continue

        accepted += 1
        graph_mask = tl.mask_from_edges_by_order(edges, args.n)
        if args.measure_witness:
            witness = lmp.max_modular_order(adjacency, 2 * args.q)
            witness_histogram[witness] = witness_histogram.get(witness, 0) + 1
            if witness < best_witness:
                best_witness = witness
                best_witness_mask = graph_mask

        allowed = lmp.build_allowed(adjacency, 2 * args.q, None, 0, None)
        try:
            result = lmp.find_min_colors(
                args.n, allowed, args.max_colors, args.node_limit
            )
        except lmp.SearchLimitExceeded:
            limited += 1
            continue

        value: int | str = "NA" if result is None else result[0]
        histogram[value] = histogram.get(value, 0) + 1
        numeric = args.max_colors + 1 if result is None else result[0]
        if numeric > best_colors:
            best_colors = numeric
            best_mask = graph_mask

    print(f"n={args.n}")
    print(f"q={args.q}")
    print(f"target_modulus={2 * args.q}")
    print(f"low_degree={args.low_degree}")
    print(f"high_degree={high}")
    print(f"low_count={args.low_count}")
    print(f"trials={args.trials}")
    print(f"max_attempts={args.max_attempts}")
    print(f"attempts={attempts}")
    print(f"accepted={accepted}")
    print(f"swaps={args.swaps}")
    print(f"max_colors={args.max_colors}")
    if args.connected_only:
        print("connected_only=True")
    if args.node_limit is not None:
        print(f"node_limited={limited}")
    print(f"worst_min_colors={best_colors if accepted - limited else 'NA'}")
    print(f"worst_color_mask={best_mask if best_mask else 'NA'}")
    print("histogram=min_colors:count")
    for key in sorted(histogram, key=lambda item: args.max_colors + 1 if item == "NA" else item):
        print(f"  {key}: {histogram[key]}")
    if args.measure_witness:
        print(f"best_max_{2 * args.q}_modular_order={best_witness if accepted else 'NA'}")
        print(f"best_witness_mask={best_witness_mask if accepted else 'NA'}")
        print(f"histogram=max_{2 * args.q}_modular_order:count")
        for key in sorted(witness_histogram):
            print(f"  {key}: {witness_histogram[key]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--low-degree", type=int, required=True)
    parser.add_argument("--low-count", type=int)
    parser.add_argument("--trials", type=int, default=5)
    parser.add_argument("--max-attempts", type=int, default=1000)
    parser.add_argument("--swaps", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--connected-only", action="store_true")
    parser.add_argument("--max-colors", type=int, default=6)
    parser.add_argument("--node-limit", type=int)
    parser.add_argument("--measure-witness", action="store_true")
    args = parser.parse_args()
    if args.low_count is None:
        args.low_count = args.n // 2
    sample(args)


if __name__ == "__main__":
    main()
