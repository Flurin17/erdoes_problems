#!/usr/bin/env python3
"""Sample compensated spread-one templates with memory-light verification."""

from __future__ import annotations

import argparse
import random
import compensated_spread
import regular_bitset


def max_regular_order_bounded(n: int, mask: int, lower_bound: int) -> tuple[int, tuple[int, ...]]:
    adj = regular_bitset.build_adjacency(n, mask)
    for order in range(n, lower_bound - 1, -1):
        witness, _degree, _checks = regular_bitset.find_regular_order(
            adj, n, order, max_checks=None
        )
        if witness is not None:
            return order, witness
    return lower_bound - 1, ()


def find_graph(args: argparse.Namespace) -> None:
    rng = random.Random(args.seed)
    n = 2 * args.m
    best = n
    best_mask = 0
    best_witness: tuple[int, ...] = ()
    accepted = 0
    histogram: dict[int, int] = {}

    for trial in range(args.trials):
        base = compensated_spread.base_edges(args.m, rng, args.p_num, args.p_den)
        degrees = compensated_spread.degrees_from_edges(args.m, base)
        rows = [args.m - 1 - degree for degree in degrees]
        eps_count = sum(rows) - sum(degrees)
        if eps_count < 0 or eps_count > args.m:
            continue
        eps = [0] * args.m
        for index in rng.sample(range(args.m), eps_count):
            eps[index] = 1
        cols = [degree + eps_i for degree, eps_i in zip(degrees, eps)]
        cross = compensated_spread.bipartite_havel_hakimi(rows, cols, rng)
        if cross is None:
            continue

        accepted += 1
        graph_mask = compensated_spread.mask_from_parts(args.m, base, cross)
        value, witness = max_regular_order_bounded(n, graph_mask, args.lower_bound)
        histogram[value] = histogram.get(value, 0) + 1
        if value < best:
            best = value
            best_mask = graph_mask
            best_witness = witness
            print(
                f"trial={trial} accepted={accepted} best_regular={best} "
                f"mask={best_mask}",
                flush=True,
            )
            if args.target and best < args.target:
                break

    print(f"m={args.m}")
    print(f"n={n}")
    print(f"trials={args.trials}")
    print(f"accepted={accepted}")
    print(f"p={args.p_num}/{args.p_den}")
    print(f"lower_bound={args.lower_bound}")
    print(f"target={args.target if args.target else 'NA'}")
    print(f"best_regular={best if accepted else 'NA'}")
    print(f"best_mask={best_mask if accepted else 'NA'}")
    if best_witness:
        print("best_witness=" + ",".join(map(str, best_witness)))
    print("histogram=max_regular_order_or_lower_bucket:count")
    for value in sorted(histogram):
        print(f"  {value}: {histogram[value]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, required=True)
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--p-num", type=int, default=1)
    parser.add_argument("--p-den", type=int, default=2)
    parser.add_argument(
        "--lower-bound",
        type=int,
        default=1,
        help="stop exact descending search once this order is passed",
    )
    parser.add_argument(
        "--target",
        type=int,
        default=0,
        help="stop sampling once a graph below this regular order is found",
    )
    args = parser.parse_args()
    if args.p_den <= 0 or not (0 <= args.p_num <= args.p_den):
        parser.error("need 0 <= --p-num <= --p-den")
    if args.lower_bound < 1 or args.lower_bound > 2 * args.m:
        parser.error("--lower-bound out of range")
    find_graph(args)


if __name__ == "__main__":
    main()
