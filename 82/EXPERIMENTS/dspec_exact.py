#!/usr/bin/env python3
"""Exact labelled checks for the spectrum-matching parameter D_spec(h)."""

from __future__ import annotations

import argparse
from itertools import combinations


def edge_data(n: int) -> tuple[list[tuple[int, int]], list[tuple[int, tuple[int, ...], list[int]]]]:
    edges = list(combinations(range(n), 2))
    incident = [[0] * n for _ in range(1 << n)]
    for edge_index, (u, v) in enumerate(edges):
        bit = 1 << edge_index
        for subset in range(1 << n):
            if (subset & (1 << u)) and (subset & (1 << v)):
                incident[subset][u] |= bit
                incident[subset][v] |= bit

    subsets: list[tuple[int, tuple[int, ...], list[int]]] = []
    for subset in range(1, 1 << n):
        vertices = tuple(v for v in range(n) if subset & (1 << v))
        masks = [incident[subset][v] for v in vertices]
        subsets.append((len(vertices), vertices, masks))
    return edges, subsets


def regular_summary(mask: int, subsets: list[tuple[int, tuple[int, ...], list[int]]], h: int) -> tuple[bool, tuple[tuple[int, int], ...]]:
    best_by_degree: dict[int, int] = {}
    has_large = False
    for size, _vertices, incident_masks in subsets:
        first = (mask & incident_masks[0]).bit_count()
        if all((mask & incident_mask).bit_count() == first for incident_mask in incident_masks[1:]):
            if size > best_by_degree.get(first, 0):
                best_by_degree[first] = size
            if size >= h:
                has_large = True
    return has_large, tuple(sorted(best_by_degree.items()))


def compatible(summary_a: tuple[tuple[int, int], ...], summary_b: tuple[tuple[int, int], ...], h: int) -> bool:
    a = dict(summary_a)
    b = dict(summary_b)
    for degree in a.keys() & b.keys():
        if a[degree] + b[degree] >= h:
            return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="component order M")
    parser.add_argument("--h", type=int, required=True)
    parser.add_argument("--limit", type=int, default=0, help="optional graph mask limit")
    args = parser.parse_args()

    edges, subsets = edge_data(args.n)
    total_graphs = 1 << len(edges)
    graph_limit = min(args.limit or total_graphs, total_graphs)

    examples: dict[tuple[tuple[int, int], ...], int] = {}
    large_count = 0
    for mask in range(graph_limit):
        has_large, summary = regular_summary(mask, subsets, args.h)
        if has_large:
            large_count += 1
            continue
        examples.setdefault(summary, mask)

    summaries = list(examples)
    print(f"n={args.n}")
    print(f"h={args.h}")
    print(f"graphs_checked={graph_limit}")
    print(f"graphs_with_regular_at_least_h={large_count}")
    print(f"unique_counterexample_summaries={len(summaries)}")

    for i, summary_a in enumerate(summaries):
        for summary_b in summaries[i:]:
            if not compatible(summary_a, summary_b, args.h):
                print("D_spec_obstruction_found=True")
                print(f"mask_a={examples[summary_a]}")
                print(f"mask_b={examples[summary_b]}")
                print("summary_a=" + " ".join(f"{d}:{s}" for d, s in summary_a))
                print("summary_b=" + " ".join(f"{d}:{s}" for d, s in summary_b))
                return
    print("D_spec_obstruction_found=False")
    if graph_limit == total_graphs:
        print(f"D_spec_at_most_{args.n}=True")


if __name__ == "__main__":
    main()
