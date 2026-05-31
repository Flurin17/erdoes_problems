#!/usr/bin/env python3
"""Sample q-modular hosts and measure regular/modular induced subgraphs."""

from __future__ import annotations

import argparse
import random

import modular_partition as mp
import regular_induced as ri


def measure_tradeoff(graph_mask: int, pc: ri.Precomp, target_modulus: int) -> tuple[int, int]:
    return (
        ri.max_regular_order(graph_mask, pc),
        ri.max_modular_order(graph_mask, target_modulus, pc),
    )


def print_summary(
    *,
    q: int,
    target_modulus: int,
    n: int,
    checked: int,
    attempts: int,
    trials: int | str,
    max_attempts: int | str,
    regular_histogram: dict[int, int],
    target_histogram: dict[int, int],
    tradeoff_histogram: dict[tuple[int, int], int],
    best_regular: int,
    best_regular_mask: int,
    best_target: int,
    best_target_mask: int,
    gap_examples: list[tuple[int, int, int]],
) -> None:
    print(f"q={q}")
    print(f"target_modulus={target_modulus}")
    print(f"n={n}")
    print(f"trials={trials}")
    print(f"max_attempts={max_attempts}")
    print(f"attempts={attempts}")
    print(f"checked={checked}")
    print(f"best_max_regular_order={best_regular if checked else 'NA'}")
    print(f"best_regular_mask={best_regular_mask if checked else 'NA'}")
    print("histogram=max_regular_order:count")
    for value in sorted(regular_histogram):
        print(f"  {value}: {regular_histogram[value]}")
    print(f"best_max_{target_modulus}_modular_order={best_target if checked else 'NA'}")
    print(f"best_target_mask={best_target_mask if checked else 'NA'}")
    print(f"histogram=max_{target_modulus}_modular_order:count")
    for value in sorted(target_histogram):
        print(f"  {value}: {target_histogram[value]}")
    print("histogram=(max_regular_order,max_target_modular_order):count")
    for value in sorted(tradeoff_histogram):
        print(f"  {value}: {tradeoff_histogram[value]}")
    print("gap_examples=mask,regular,target")
    for mask, regular_value, target_value in gap_examples:
        print(f"  {mask},{regular_value},{target_value}")


def exhaustive(args: argparse.Namespace) -> None:
    pc = ri.precompute(args.n)
    full = (1 << args.n) - 1
    total = 1 << len(pc.edges)
    checked = 0
    regular_histogram: dict[int, int] = {}
    target_histogram: dict[int, int] = {}
    tradeoff_histogram: dict[tuple[int, int], int] = {}
    best_regular = args.n
    best_regular_mask = 0
    best_target = args.n
    best_target_mask = 0
    gap_examples: list[tuple[int, int, int]] = []

    for graph_mask in range(total):
        if not ri.is_modular_on(graph_mask, full, args.q, pc):
            continue
        checked += 1
        regular_value, target_value = measure_tradeoff(graph_mask, pc, args.target_modulus)
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
        if target_value > regular_value and len(gap_examples) < 5:
            gap_examples.append((graph_mask, regular_value, target_value))

    print_summary(
        q=args.q,
        target_modulus=args.target_modulus,
        n=args.n,
        checked=checked,
        attempts=total,
        trials="exhaustive",
        max_attempts="exhaustive",
        regular_histogram=regular_histogram,
        target_histogram=target_histogram,
        tradeoff_histogram=tradeoff_histogram,
        best_regular=best_regular,
        best_regular_mask=best_regular_mask,
        best_target=best_target,
        best_target_mask=best_target_mask,
        gap_examples=gap_examples,
    )


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
    parser.add_argument("--exhaustive", action="store_true")
    args = parser.parse_args()
    if args.target_modulus is None:
        args.target_modulus = 2 * args.q
    if args.exhaustive:
        exhaustive(args)
        return

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
    gap_examples: list[tuple[int, int, int]] = []

    while checked < args.trials and attempts < args.max_attempts:
        attempts += 1
        graph_mask = mp.random_full_modular_candidate(
            args.n, args.q, edge_count, rng, pc, edge_index
        )
        if graph_mask is None or not ri.is_modular_on(graph_mask, full, args.q, pc):
            continue
        checked += 1
        regular_value, target_value = measure_tradeoff(graph_mask, pc, args.target_modulus)
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
        if target_value > regular_value and len(gap_examples) < 5:
            gap_examples.append((graph_mask, regular_value, target_value))

    print_summary(
        q=args.q,
        target_modulus=args.target_modulus,
        n=args.n,
        checked=checked,
        attempts=attempts,
        trials=args.trials,
        max_attempts=args.max_attempts,
        regular_histogram=regular_histogram,
        target_histogram=target_histogram,
        tradeoff_histogram=tradeoff_histogram,
        best_regular=best_regular,
        best_regular_mask=best_regular_mask,
        best_target=best_target,
        best_target_mask=best_target_mask,
        gap_examples=gap_examples,
    )


if __name__ == "__main__":
    main()
