#!/usr/bin/env python3
"""Exact small census for the column-drop ordered parameter C_drop(P,h)."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations
from time import monotonic


@dataclass(frozen=True)
class Precomp:
    n: int
    edges: list[tuple[int, int]]
    edge_index: dict[tuple[int, int], int]
    subsets_by_size: list[tuple[int, list[tuple[int, tuple[int, ...]]]]]


def precompute(n: int) -> Precomp:
    edges = list(combinations(range(n), 2))
    edge_index = {edge: index for index, edge in enumerate(edges)}
    subsets_by_size = []
    for size in range(n, 0, -1):
        entries = []
        for subset in range(1, 1 << n):
            if subset.bit_count() == size:
                vertices = tuple(v for v in range(n) if (subset >> v) & 1)
                entries.append((subset, vertices))
        subsets_by_size.append((size, entries))
    return Precomp(n, edges, edge_index, subsets_by_size)


def adjacency(n: int, mask: int, pc: Precomp) -> list[int]:
    adj = [0] * n
    for index, (u, v) in enumerate(pc.edges):
        if (mask >> index) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def max_column_drop(adj: list[int], n: int) -> int:
    maximum = 0
    for j in range(n):
        for k in range(j + 1, n):
            drop = 0
            for i in range(j):
                if ((adj[i] >> j) & 1) and not ((adj[i] >> k) & 1):
                    drop += 1
            maximum = max(maximum, drop)
    return maximum


def max_homogeneous(adj: list[int], pc: Precomp) -> tuple[int, str, tuple[int, ...]]:
    for size, entries in pc.subsets_by_size:
        clique_degree = size - 1
        for subset, vertices in entries:
            degree = (adj[vertices[0]] & subset).bit_count()
            if degree not in (0, clique_degree):
                continue
            if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                kind = "independent" if degree == 0 else "clique"
                return size, kind, vertices
    return 1, "single", (0,)


def exact(n: int, p: int, progress: int) -> None:
    pc = precompute(n)
    total = 1 << len(pc.edges)
    checked = 0
    best_homogeneous = n
    examples: list[tuple[int, str, tuple[int, ...], int]] = []
    start = monotonic()

    for mask in range(total):
        adj = adjacency(n, mask, pc)
        if max_column_drop(adj, n) >= p:
            continue
        checked += 1
        homogeneous, kind, vertices = max_homogeneous(adj, pc)
        if homogeneous < best_homogeneous:
            best_homogeneous = homogeneous
            examples = [(mask, kind, vertices, max_column_drop(adj, n))]
            print(
                "new_best "
                f"mask={mask} max_homogeneous={homogeneous} kind={kind} "
                f"vertices={vertices}",
                flush=True,
            )
        elif homogeneous == best_homogeneous and len(examples) < 5:
            examples.append((mask, kind, vertices, max_column_drop(adj, n)))

        if progress and mask and mask % progress == 0:
            print(
                f"progress mask={mask}/{total} checked={checked} "
                f"best={best_homogeneous} elapsed={monotonic() - start:.1f}s",
                flush=True,
            )

    print(f"n={n}")
    print(f"P={p}")
    print(f"labelled_graphs={total}")
    print(f"checked_column_drop={checked}")
    print(f"min_max_homogeneous={best_homogeneous}")
    for mask, kind, vertices, drop in examples:
        print(
            f"example mask={mask} max_drop={drop} "
            f"homogeneous_kind={kind} homogeneous_vertices="
            + ",".join(map(str, vertices))
        )


def fixed(n: int, mask: int) -> None:
    pc = precompute(n)
    adj = adjacency(n, mask, pc)
    homogeneous, kind, vertices = max_homogeneous(adj, pc)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"max_column_drop={max_column_drop(adj, n)}")
    print(f"max_homogeneous={homogeneous}")
    print(f"homogeneous_kind={kind}")
    print("homogeneous_vertices=" + ",".join(map(str, vertices)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--p", type=int, default=1)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--progress", type=int, default=0)
    args = parser.parse_args()
    if args.p < 1:
        raise SystemExit("--p must be positive")

    if args.mask is None:
        exact(args.n, args.p, args.progress)
    else:
        fixed(args.n, args.mask)


if __name__ == "__main__":
    main()
