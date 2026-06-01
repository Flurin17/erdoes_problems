#!/usr/bin/env python3
"""Search the one-trace regular merge criterion from Lemma 14A.5."""

from __future__ import annotations

import argparse
from itertools import combinations


def build_adjacency(n: int, mask: int) -> list[int]:
    adj = [0] * n
    edge_index = 0
    for u, v in combinations(range(n), 2):
        if mask & (1 << edge_index):
            adj[u] |= 1 << v
            adj[v] |= 1 << u
        edge_index += 1
    return adj


def vertices_from_csv(text: str) -> list[int]:
    if not text:
        return []
    return [int(part) for part in text.split(",") if part]


def mask_from_vertices(vertices: list[int] | tuple[int, ...]) -> int:
    mask = 0
    for vertex in vertices:
        mask |= 1 << vertex
    return mask


def regular_degree(adj: list[int], vertices: list[int] | tuple[int, ...]) -> int | None:
    if not vertices:
        return None
    mask = mask_from_vertices(vertices)
    first = (adj[vertices[0]] & mask).bit_count()
    for vertex in vertices[1:]:
        if (adj[vertex] & mask).bit_count() != first:
            return None
    return first


def has_trace(adj: list[int], vertex: int, base: list[int], trace: set[int]) -> bool:
    return {a for a in base if adj[vertex] & (1 << a)} == trace


def find_regular_subsets(
    adj: list[int],
    vertices: list[int],
    *,
    target_deficit: int | None = None,
    target_degree: int | None = None,
    limit: int,
) -> list[tuple[tuple[int, ...], int]]:
    found: list[tuple[tuple[int, ...], int]] = []
    for size in range(len(vertices), 0, -1):
        for subset in combinations(vertices, size):
            degree = regular_degree(adj, subset)
            if degree is None:
                continue
            if target_deficit is not None and size - degree != target_deficit:
                continue
            if target_degree is not None and degree != target_degree:
                continue
            found.append((subset, degree))
            if len(found) >= limit:
                return found
    return found


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--A", required=True, help="comma-separated base vertices")
    parser.add_argument("--T", required=True, help="comma-separated trace vertices inside A")
    parser.add_argument("--B", required=True, help="comma-separated vertices in one trace class")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    adj = build_adjacency(args.n, args.mask)
    base = vertices_from_csv(args.A)
    trace = set(vertices_from_csv(args.T))
    trace_side = [v for v in base if v in trace]
    nontrace_side = [v for v in base if v not in trace]
    b_vertices = vertices_from_csv(args.B)

    b_degree = regular_degree(adj, b_vertices)
    if b_degree is None:
        raise SystemExit("B is not regular")
    bad_trace = [v for v in b_vertices if not has_trace(adj, v, base, trace)]
    if bad_trace:
        raise SystemExit("B is not contained in the supplied trace class: " + ",".join(map(str, bad_trace)))

    b_size = len(b_vertices)
    deficit = b_size - b_degree
    trace_matches = find_regular_subsets(
        adj,
        trace_side,
        target_deficit=deficit,
        limit=args.limit,
    )
    nontrace_matches = find_regular_subsets(
        adj,
        nontrace_side,
        target_degree=b_degree,
        limit=args.limit,
    )

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print("A=" + ",".join(map(str, base)))
    print("T=" + ",".join(map(str, sorted(trace))))
    print("B=" + ",".join(map(str, b_vertices)))
    print(f"B_size={b_size}")
    print(f"B_degree={b_degree}")
    print(f"B_deficit={deficit}")
    print(f"trace_side_size={len(trace_side)}")
    print(f"nontrace_side_size={len(nontrace_side)}")
    print(f"trace_deficit_matches={len(trace_matches)}")
    for subset, degree in trace_matches:
        union_degree = regular_degree(adj, list(subset) + b_vertices)
        print(
            "  X={} degree={} deficit={} union_order={} union_degree={}".format(
                ",".join(map(str, subset)),
                degree,
                len(subset) - degree,
                len(subset) + b_size,
                union_degree,
            )
        )
    print(f"nontrace_degree_matches={len(nontrace_matches)}")
    for subset, degree in nontrace_matches:
        union_degree = regular_degree(adj, list(subset) + b_vertices)
        print(
            "  X={} degree={} union_order={} union_degree={}".format(
                ",".join(map(str, subset)),
                degree,
                len(subset) + b_size,
                union_degree,
            )
        )


if __name__ == "__main__":
    main()
