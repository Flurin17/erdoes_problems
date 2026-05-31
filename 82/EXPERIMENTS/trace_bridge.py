#!/usr/bin/env python3
"""Evaluate a repeated-degree bridge.

For an induced subgraph H and an equal-degree class A in H, if every vertex in
A has the same number of neighbors in H\\A, then H[A] is regular.  This script
compares that degree-class certificate with the true maximum regular induced
subgraph for small graphs.
"""

from __future__ import annotations

import argparse
import random
import sys

import regular_induced as ri


def degree_class_bridge_order(graph_mask: int, pc: ri.Precomp, min_h_size: int = 1) -> int:
    best = 1
    for hset in range(1, 1 << pc.n):
        vs = pc.vertices[hset]
        if len(vs) < min_h_size:
            continue
        by_degree: dict[int, list[int]] = {}
        for v in vs:
            deg = (graph_mask & pc.incident[hset][v]).bit_count()
            by_degree.setdefault(deg, []).append(v)

        for group in by_degree.values():
            aset = sum(1 << v for v in group)
            outside = hset ^ aset
            outside_degrees = {
                (graph_mask & pc.incident[outside | (1 << v)][v]).bit_count()
                for v in group
            }
            if len(outside_degrees) == 1:
                best = max(best, len(group))
    return best


def whole_graph_degree_class_bridge_order(graph_mask: int, pc: ri.Precomp) -> int:
    full = (1 << pc.n) - 1
    by_degree: dict[int, list[int]] = {}
    for v in range(pc.n):
        deg = (graph_mask & pc.incident[full][v]).bit_count()
        by_degree.setdefault(deg, []).append(v)

    best = 1
    for group in by_degree.values():
        aset = sum(1 << v for v in group)
        outside = full ^ aset
        outside_degrees = {
            (graph_mask & pc.incident[outside | (1 << v)][v]).bit_count()
            for v in group
        }
        if len(outside_degrees) == 1:
            best = max(best, len(group))
    return best


def exhaustive(n: int, min_h_size: int) -> None:
    pc = ri.precompute(n)
    total = 1 << len(pc.edges)
    gaps: dict[tuple[int, int], int] = {}
    min_bridge_for_reg: dict[int, int] = {}
    min_whole_bridge_for_reg: dict[int, int] = {}

    for graph_mask in range(total):
        reg = ri.max_regular_order(graph_mask, pc)
        bridge = degree_class_bridge_order(graph_mask, pc, min_h_size)
        whole_bridge = whole_graph_degree_class_bridge_order(graph_mask, pc)
        gaps[(reg, bridge)] = gaps.get((reg, bridge), 0) + 1
        min_bridge_for_reg[reg] = min(min_bridge_for_reg.get(reg, bridge), bridge)
        min_whole_bridge_for_reg[reg] = min(
            min_whole_bridge_for_reg.get(reg, whole_bridge), whole_bridge
        )

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"min_h_size={min_h_size}")
    print("min_bridge_for_true_reg")
    for reg in sorted(min_bridge_for_reg):
        print(f"  reg={reg}: bridge>={min_bridge_for_reg[reg]}")
    print("min_whole_graph_bridge_for_true_reg")
    for reg in sorted(min_whole_bridge_for_reg):
        print(f"  reg={reg}: whole_bridge>={min_whole_bridge_for_reg[reg]}")
    print("distribution=true_reg,bridge:count")
    for (reg, bridge), count in sorted(gaps.items()):
        print(f"  {reg},{bridge}: {count}")


def sample(n: int, trials: int, seed: int, min_h_size: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    m = len(pc.edges)
    records: list[tuple[int, int, int]] = []

    for _ in range(trials):
        graph_mask = rng.getrandbits(m)
        records.append(
            (
                ri.max_regular_order(graph_mask, pc),
                degree_class_bridge_order(graph_mask, pc, min_h_size),
                whole_graph_degree_class_bridge_order(graph_mask, pc),
            )
        )

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"min_h_size={min_h_size}")
    print(f"min_true_reg={min(r for r, _, _ in records)}")
    print(f"min_bridge={min(b for _, b, _ in records)}")
    print(f"min_whole_graph_bridge={min(w for _, _, w in records)}")
    print(f"max_whole_graph_gap={max(r - w for r, _, w in records)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--min-h-size", type=int, default=1)
    args = parser.parse_args()

    if args.sample:
        sample(args.n, args.sample, args.seed, args.min_h_size)
    else:
        if args.n > 6:
            print("exhaustive trace checks are intentionally capped at n=6", file=sys.stderr)
            sys.exit(2)
        exhaustive(args.n, args.min_h_size)


if __name__ == "__main__":
    main()
