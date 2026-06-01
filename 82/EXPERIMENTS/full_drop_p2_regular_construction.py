#!/usr/bin/env python3
"""Generate the block family behind small P=2 regular full-drop obstructions."""

from __future__ import annotations

import argparse

import column_drop_census as cdc
import full_drop_census as fdc


def build_columns(h: int) -> list[int]:
    if h < 5:
        raise ValueError("h must be at least 5")
    t = h - 3
    n = 2 * h
    columns = [0] * n

    p0, p1, q0, q1 = 0, 1, 2, 3
    middle = list(range(4, 4 + t))
    clique = list(range(4 + t, 4 + 2 * t))
    top = [n - 2, n - 1]

    def add_edge(u: int, v: int) -> None:
        if u > v:
            u, v = v, u
        columns[v] |= 1 << u

    add_edge(p0, q0)
    add_edge(p1, q1)
    for c in clique:
        add_edge(q1, c)
    for m in middle:
        for c in clique:
            add_edge(m, c)
    for i, c in enumerate(clique):
        for c2 in clique[:i]:
            add_edge(c2, c)
    for u in top:
        for v in range(n):
            if v != u and v not in top:
                add_edge(u, v)
    return columns


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("h", type=int)
    args = parser.parse_args()

    columns = build_columns(args.h)
    n = len(columns)
    pc = cdc.precompute(n)
    adj = cdc.columns_to_adjacency(columns)
    homogeneous, kind, homogeneous_vertices = cdc.max_homogeneous(adj, pc)
    clique, clique_vertices, independent, independent_vertices = (
        fdc.max_clique_independent(adj, pc)
    )
    regular, regular_degree, regular_vertices = cdc.max_regular(adj, pc)
    print(f"h={args.h}")
    print(f"n={n}")
    print("columns=" + ",".join(map(str, columns)))
    print(f"mask={cdc.columns_to_mask(columns, pc)}")
    print(f"max_full_drop={fdc.max_full_drop(adj, n)}")
    print(f"max_homogeneous={homogeneous}")
    print(f"homogeneous_kind={kind}")
    print("homogeneous_vertices=" + ",".join(map(str, homogeneous_vertices)))
    print(f"clique_number={clique}")
    print("clique_vertices=" + ",".join(map(str, clique_vertices)))
    print(f"independence_number={independent}")
    print("independent_vertices=" + ",".join(map(str, independent_vertices)))
    print(f"max_regular={regular}")
    print(f"regular_degree={regular_degree}")
    print("regular_vertices=" + ",".join(map(str, regular_vertices)))


if __name__ == "__main__":
    main()
