#!/usr/bin/env python3
"""Search graphs with bounded degree spread.

If many vertices have the same degree in a slightly larger induced subgraph,
the induced graph on those vertices has small degree spread.  This script
tests whether small degree spread alone forces large regular induced subgraphs.
"""

from __future__ import annotations

import argparse
import random

import regular_induced as ri


def degree_spread(graph_mask: int, subset: int, pc: ri.Precomp) -> int:
    vs = pc.vertices[subset]
    if not vs:
        return 0
    degrees = [(graph_mask & pc.incident[subset][v]).bit_count() for v in vs]
    return max(degrees) - min(degrees)


def num_distinct_degrees(graph_mask: int, subset: int, pc: ri.Precomp) -> int:
    return len({(graph_mask & pc.incident[subset][v]).bit_count() for v in pc.vertices[subset]})


def exhaustive(n: int, max_spread: int | None, max_degree_values: int | None) -> None:
    pc = ri.precompute(n)
    full = (1 << n) - 1
    total = 1 << len(pc.edges)
    checked = 0
    best = n
    histogram: dict[int, int] = {}
    witnesses: list[int] = []

    for graph_mask in range(total):
        if max_spread is not None and degree_spread(graph_mask, full, pc) > max_spread:
            continue
        if (
            max_degree_values is not None
            and num_distinct_degrees(graph_mask, full, pc) > max_degree_values
        ):
            continue
        checked += 1
        value = ri.max_regular_order(graph_mask, pc)
        histogram[value] = histogram.get(value, 0) + 1
        if value < best:
            best = value
            witnesses = [graph_mask]
        elif value == best and len(witnesses) < 5:
            witnesses.append(graph_mask)

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"checked={checked}")
    if max_spread is not None:
        print(f"max_spread={max_spread}")
    if max_degree_values is not None:
        print(f"max_degree_values={max_degree_values}")
    print(f"minimum_regular_order={best if checked else 'NA'}")
    print("histogram=max_regular_order:count")
    for key in sorted(histogram):
        print(f"  {key}: {histogram[key]}")
    print("sample_extremal_graph_masks=" + ",".join(map(str, witnesses)))


def sample_near_regular(n: int, trials: int, seed: int, max_spread: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    full = (1 << n) - 1
    m = len(pc.edges)
    seen = 0
    attempts = 0
    best = n
    histogram: dict[int, int] = {}

    while seen < trials:
        attempts += 1
        graph_mask = rng.getrandbits(m)
        if degree_spread(graph_mask, full, pc) > max_spread:
            continue
        seen += 1
        value = ri.max_regular_order(graph_mask, pc)
        best = min(best, value)
        histogram[value] = histogram.get(value, 0) + 1

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"max_spread={max_spread}")
    print(f"minimum_seen={best}")
    print("histogram=max_regular_order:count")
    for key in sorted(histogram):
        print(f"  {key}: {histogram[key]}")


def analyze_mask(n: int, graph_mask: int) -> None:
    pc = ri.precompute(n)
    full = (1 << n) - 1
    degrees = [(graph_mask & pc.incident[full][v]).bit_count() for v in range(n)]
    print(f"n={n}")
    print(f"mask={graph_mask}")
    print("degrees=" + ",".join(map(str, degrees)))
    print(f"spread={max(degrees) - min(degrees)}")
    print(f"max_regular_order={ri.max_regular_order(graph_mask, pc)}")
    print(f"max_2_modular_order={ri.max_modular_order(graph_mask, 2, pc)}")
    print(f"max_4_modular_order={ri.max_modular_order(graph_mask, 4, pc)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--max-spread", type=int)
    parser.add_argument("--max-degree-values", type=int)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--mask", type=int)
    args = parser.parse_args()

    if args.mask is not None:
        analyze_mask(args.n, args.mask)
        return
    if args.sample:
        if args.max_spread is None:
            parser.error("--sample requires --max-spread")
        sample_near_regular(args.n, args.sample, args.seed, args.max_spread)
    else:
        exhaustive(args.n, args.max_spread, args.max_degree_values)


if __name__ == "__main__":
    main()
