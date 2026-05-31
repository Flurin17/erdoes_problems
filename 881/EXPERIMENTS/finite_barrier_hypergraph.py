#!/usr/bin/env python3
"""Finite residue hypergraph barriers for the broad deletion theorem.

For a residue set S in Z/mZ, build the hypergraph of finite deletions
F subset S for which (k+1)(S\\F) is not the whole group.  This is a finite
analogue of the late-bad finite barriers in PROOF.md.

The script reports examples where singleton deletions are harmless, but the
bad finite deletions of size up to q form a barrier on S in the finite sense
that every r-subset of S contains one of them. This is not an infinite
counterexample; it is a way to locate genuinely collective finite patterns.
"""

from __future__ import annotations

import sys
from itertools import combinations


def hsum(values: set[int], h: int, mod: int) -> set[int]:
    out = {0}
    for _ in range(h):
        out = {(x + y) % mod for x in out for y in values}
    return out


def first_hole(values: set[int], h: int, mod: int) -> int | None:
    sums = hsum(values, h, mod)
    for x in range(mod):
        if x not in sums:
            return x
    return None


def bad_edges(
    S: set[int],
    h: int,
    mod: int,
    max_size: int,
) -> dict[tuple[int, ...], int]:
    edges: dict[tuple[int, ...], int] = {}
    for size in range(2, min(max_size, len(S)) + 1):
        for edge in combinations(sorted(S), size):
            hole = first_hole(S - set(edge), h, mod)
            if hole is not None:
                edges[edge] = hole
    return edges


def minimal_edges(edges: dict[tuple[int, ...], int]) -> dict[tuple[int, ...], int]:
    edge_sets = [(edge, set(edge)) for edge in edges]
    out: dict[tuple[int, ...], int] = {}
    for edge, edge_set in edge_sets:
        if not any(other_set < edge_set for other, other_set in edge_sets if other != edge):
            out[edge] = edges[edge]
    return out


def covers_all_r_subsets(
    S: set[int],
    edges: dict[tuple[int, ...], int],
    r: int,
) -> bool:
    edge_sets = [set(edge) for edge in edges]
    return all(
        any(edge <= set(chunk) for edge in edge_sets)
        for chunk in combinations(sorted(S), r)
    )


def main(
    limit_mod: int = 18,
    k: int = 2,
    max_edge_size: int = 4,
    min_edge_size: int = 2,
    minimal_only: bool = True,
) -> None:
    h = k + 1
    for mod in range(2, limit_mod + 1):
        group = set(range(mod))
        for mask in range(1, 1 << mod):
            S = {i for i in range(mod) if (mask >> i) & 1}
            if len(S) < 4 or hsum(S, k, mod) != group:
                continue
            if any(hsum(S - {s}, h, mod) != group for s in S):
                continue
            edges = bad_edges(S, h, mod, max_edge_size)
            if minimal_only:
                edges = minimal_edges(edges)
            edges = {
                edge: hole
                for edge, hole in edges.items()
                if len(edge) >= min_edge_size
            }
            if not edges:
                continue
            for r in range(2, len(S) + 1):
                if covers_all_r_subsets(S, edges, r):
                    print(
                        "finite barrier",
                        "mod=", mod,
                        "k=", k,
                        "S=", sorted(S),
                        "edge_max=", max_edge_size,
                        "edge_min=", min_edge_size,
                        "minimal=", minimal_only,
                        "r=", r,
                        "edge_count=", len(edges),
                    )
                    print("sample_edges=", list(edges.items())[:12])
                    return
    print("no finite barrier found within searched bounds")


if __name__ == "__main__":
    main(
        min_edge_size=3 if "--rank3" in sys.argv else 2,
        minimal_only="--all" not in sys.argv,
    )
