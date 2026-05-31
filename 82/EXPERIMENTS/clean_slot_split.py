#!/usr/bin/env python3
"""Test first-split rules for the clean slots (0,0,2,2).

For a chosen high-bit set Y, the slots (0,0,2,2) reduce to:

* split X=V\\Y into two 0-mod-4 parts;
* split Y into two 2-mod-4 parts.

This script tests such fixed choices of Y.  It is not a complete checker for
the slots unless all possible high-bit sets are searched elsewhere.
"""

from __future__ import annotations

import argparse
import random

import modular_lift
import modular_partition
import regular_induced as ri


def empty_or_residue(
    graph_mask: int,
    subset: int,
    target: int,
    pc: ri.Precomp,
) -> bool:
    if subset == 0:
        return True
    return modular_partition.residue_on(graph_mask, subset, 4, pc) == target


def can_two_cut(
    n: int,
    graph_mask: int,
    subset: int,
    target: int,
    pc: ri.Precomp,
) -> bool:
    """Return whether subset splits into two target-residue induced parts."""
    first = subset & -subset
    part = subset
    while True:
        # Break the symmetry between the two sides when subset is nonempty.
        if subset == 0 or part & first:
            if empty_or_residue(graph_mask, part, target, pc) and empty_or_residue(
                graph_mask,
                subset ^ part,
                target,
                pc,
            ):
                return True
        if part == 0:
            break
        part = (part - 1) & subset
    return False


def degree_high_mask(
    n: int,
    graph_mask: int,
    source_parity: int,
    pc: ri.Precomp,
) -> int:
    full = (1 << n) - 1
    mask = 0
    for vertex in range(n):
        degree = (graph_mask & pc.incident[full][vertex]).bit_count()
        if ((degree - source_parity) // 2) & 1:
            mask |= 1 << vertex
    return mask


def check_high_mask(
    n: int,
    graph_mask: int,
    high_mask: int,
    pc: ri.Precomp,
) -> bool:
    full = (1 << n) - 1
    low_mask = full ^ high_mask
    return can_two_cut(n, graph_mask, low_mask, 0, pc) and can_two_cut(
        n,
        graph_mask,
        high_mask,
        2,
        pc,
    )


def parse_mask(text: str | None) -> int | None:
    if text is None:
        return None
    if "," in text:
        mask = 0
        for item in text.split(","):
            if item:
                mask |= 1 << int(item)
        return mask
    return int(text)


def describe_set(n: int, mask: int) -> str:
    return ",".join(str(vertex) for vertex in range(n) if (mask >> vertex) & 1)


def check_one(n: int, graph_mask: int, high_mask: int, pc: ri.Precomp) -> None:
    print(f"n={n}")
    print(f"mask={graph_mask}")
    print(f"high_mask={high_mask}")
    print("high_vertices=" + describe_set(n, high_mask))
    print(f"clean_split={'yes' if check_high_mask(n, graph_mask, high_mask, pc) else 'no'}")


def exhaustive_degree_rule(n: int, source_parity: int) -> None:
    pc = ri.precompute(n)
    checked = 0
    for graph_mask in modular_lift.parity_graphs(n, odd=bool(source_parity)):
        checked += 1
        high_mask = degree_high_mask(n, graph_mask, source_parity, pc)
        if not check_high_mask(n, graph_mask, high_mask, pc):
            print(f"n={n}")
            print(f"source_parity={source_parity}")
            print(f"checked_before_failure={checked}")
            print(f"failure_mask={graph_mask}")
            print(f"high_mask={high_mask}")
            print("high_vertices=" + describe_set(n, high_mask))
            return
    print(f"n={n}")
    print(f"source_parity={source_parity}")
    print(f"checked={checked}")
    print("no_counterexample_seen")


def sample_degree_rule(n: int, source_parity: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    checked = 0
    for _ in range(trials):
        graph_mask = modular_partition.random_parity_mask(
            n,
            bool(source_parity),
            rng,
            pc,
            edge_index,
        )
        if graph_mask is None:
            continue
        checked += 1
        high_mask = degree_high_mask(n, graph_mask, source_parity, pc)
        if not check_high_mask(n, graph_mask, high_mask, pc):
            print(f"n={n}")
            print(f"source_parity={source_parity}")
            print(f"seed={seed}")
            print(f"checked_before_failure={checked}")
            print(f"failure_mask={graph_mask}")
            print(f"high_mask={high_mask}")
            print("high_vertices=" + describe_set(n, high_mask))
            return
    print(f"n={n}")
    print(f"source_parity={source_parity}")
    print(f"seed={seed}")
    print(f"checked={checked}")
    print("no_counterexample_seen")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--high-mask")
    parser.add_argument("--source-parity", type=int, choices=(0, 1), default=0)
    parser.add_argument("--degree-rule", action="store_true")
    parser.add_argument("--exhaustive", action="store_true")
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if args.exhaustive:
        exhaustive_degree_rule(args.n, args.source_parity)
        return
    if args.sample:
        sample_degree_rule(args.n, args.source_parity, args.sample, args.seed)
        return
    if args.mask is None:
        raise SystemExit("--mask is required unless --exhaustive or --sample is used")

    pc = ri.precompute(args.n)
    if args.degree_rule:
        high_mask = degree_high_mask(args.n, args.mask, args.source_parity, pc)
    else:
        high_mask = parse_mask(args.high_mask)
        if high_mask is None:
            raise SystemExit("--high-mask or --degree-rule is required")
    check_one(args.n, args.mask, high_mask, pc)


if __name__ == "__main__":
    main()
