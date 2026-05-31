#!/usr/bin/env python3
"""Finite representation-hypergraph statistics.

For a finite set A, an order h, and a target n, build the hypergraph whose
edges are h-term representation supports of n from A, optionally ignoring a
finite protected core E. Report edge count, maximum degree, and a greedy
matching size. This mirrors Proposition 3.4 in PROOF.md.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations_with_replacement


def rep_edges(A: list[int], h: int, n: int, protected: set[int]) -> set[frozenset[int]]:
    edges: set[frozenset[int]] = set()
    for rep in combinations_with_replacement(A, h):
        if sum(rep) != n:
            continue
        edge = frozenset(x for x in rep if x not in protected)
        if edge:
            edges.add(edge)
    return edges


def stats(edges: set[frozenset[int]]) -> tuple[int, int, int]:
    degree: dict[int, int] = defaultdict(int)
    for edge in edges:
        for v in edge:
            degree[v] += 1
    max_degree = max(degree.values(), default=0)
    matching = 0
    used: set[int] = set()
    for edge in sorted(edges, key=len):
        if edge.isdisjoint(used):
            matching += 1
            used.update(edge)
    return len(edges), max_degree, matching


def demo_residue_padding(k: int = 3, limit: int = 120) -> None:
    A = [1] + [k * i for i in range(1, limit // k + 1)]
    protected = {1}
    h = k + 1
    print(f"residue-padding model k={k}, h={h}, protected={protected}")
    for n in range(limit - 10, limit + 1):
        edges = rep_edges(A, h, n, protected)
        edge_count, max_degree, greedy = stats(edges)
        ratio = edge_count / max_degree if max_degree else 0
        print(
            f"n={n:3d} edges={edge_count:4d} "
            f"maxdeg={max_degree:4d} ratio={ratio:6.2f} greedy={greedy}"
        )


if __name__ == "__main__":
    demo_residue_padding()
