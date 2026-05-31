#!/usr/bin/env python3
"""Optimize fixed-slot modular partitions by a simple defect cost."""

from __future__ import annotations

import argparse
import random
from functools import lru_cache

import modular_partition
import regular_induced as ri


def optimize(
    n: int,
    graph_mask: int,
    modulus: int,
    slots: tuple[int, ...],
    zero_residue: int,
) -> tuple[int, tuple[tuple[int, int], ...]] | None:
    pc = ri.precompute(n)
    allowed_by_residue: dict[int, list[int]] = {residue: [] for residue in set(slots)}
    for subset in range(1, 1 << n):
        residue = modular_partition.residue_on(graph_mask, subset, modulus, pc)
        if residue in allowed_by_residue:
            allowed_by_residue[residue].append(subset)
    for residue in allowed_by_residue:
        allowed_by_residue[residue].sort(key=lambda subset: (subset.bit_count(), subset))

    full = (1 << n) - 1
    sorted_slots = tuple(sorted(slots))

    @lru_cache(maxsize=None)
    def rec(remaining: int, state: tuple[int, ...]) -> tuple[int, tuple[tuple[int, int], ...]] | None:
        if remaining == 0:
            return 0, ()
        if not state:
            return None
        pivot = remaining & -remaining
        best: tuple[int, tuple[tuple[int, int], ...]] | None = None
        for index, residue in enumerate(state):
            next_state = tuple(state[:index] + state[index + 1 :])
            for subset in allowed_by_residue[residue]:
                if not (subset & pivot) or subset & ~remaining:
                    continue
                suffix = rec(remaining ^ subset, next_state)
                if suffix is None:
                    continue
                cost = suffix[0] + (0 if residue == zero_residue else subset.bit_count())
                candidate = cost, ((residue, subset),) + suffix[1]
                if best is None or candidate[0] < best[0]:
                    best = candidate
        return best

    return rec(full, sorted_slots)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument("--slots", type=str, default="0,0,1,2")
    parser.add_argument("--zero-residue", type=int, default=0)
    parser.add_argument("--sample-even", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    slots = tuple(int(item) % args.modulus for item in args.slots.split(",") if item)
    if args.sample_even:
        rng = random.Random(args.seed)
        pc = ri.precompute(args.n)
        edge_index = {edge: index for index, edge in enumerate(pc.edges)}
        histogram: dict[int | str, int] = {}
        examples: list[tuple[int, int | str]] = []
        for _ in range(args.sample_even):
            graph_mask = modular_partition.random_parity_mask(
                args.n, False, rng, pc, edge_index
            )
            if graph_mask is None:
                continue
            answer = optimize(args.n, graph_mask, args.modulus, slots, args.zero_residue)
            cost: int | str = "NA" if answer is None else answer[0]
            histogram[cost] = histogram.get(cost, 0) + 1
            if len(examples) < 5:
                examples.append((graph_mask, cost))
        print(f"n={args.n}")
        print(f"modulus={args.modulus}")
        print("slots=" + ",".join(map(str, slots)))
        print(f"zero_residue={args.zero_residue}")
        print(f"sample_even={args.sample_even}")
        print(f"seed={args.seed}")
        print("histogram=nonzero_cost:count")
        for cost in sorted(histogram, key=lambda item: args.n + 1 if item == "NA" else item):
            print(f"  {cost}: {histogram[cost]}")
        print("examples=mask,cost")
        for graph_mask, cost in examples:
            print(f"  {graph_mask},{cost}")
        return
    if args.mask is None:
        raise SystemExit("--mask is required unless --sample-even is used")
    answer = optimize(args.n, args.mask, args.modulus, slots, args.zero_residue)
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"modulus={args.modulus}")
    print("slots=" + ",".join(map(str, slots)))
    print(f"zero_residue={args.zero_residue}")
    if answer is None:
        print("slot_partition=no")
        return
    cost, parts = answer
    print("slot_partition=yes")
    print(f"nonzero_cost={cost}")
    for residue, subset in parts:
        vertices = [vertex for vertex in range(args.n) if (subset >> vertex) & 1]
        print(
            f"part residue={residue} size={len(vertices)} vertices="
            + ",".join(map(str, vertices))
        )


if __name__ == "__main__":
    main()
