#!/usr/bin/env python3
"""Generate and verify the linear P=2 full-drop construction."""

from __future__ import annotations

import argparse

import column_drop_census as cdc
import full_drop_census as fdc


def columns_for_h(h: int) -> list[int]:
    if h < 4:
        raise ValueError("h must be at least 4")
    t = h - 3
    n = 4 * h - 7
    columns = [0] * n

    # Matching component: a_1,...,a_t,b_1,...,b_t.
    for i in range(t):
        columns[t + i] = 1 << i

    c0 = 2 * t
    cycle_edges = [
        (c0 + 0, c0 + 1),
        (c0 + 0, c0 + 2),
        (c0 + 1, c0 + 3),
        (c0 + 2, c0 + 4),
        (c0 + 3, c0 + 4),
    ]
    for u, v in cycle_edges:
        columns[v] |= 1 << u

    top0 = c0 + 5
    cycle_mask = sum(1 << (c0 + i) for i in range(5))
    for part in range(t):
        p = top0 + 2 * part
        q = p + 1
        previous_top = ((1 << p) - 1) & ~((1 << top0) - 1)
        mate_mask = 1 << p
        columns[p] |= cycle_mask | previous_top
        columns[q] |= cycle_mask | (previous_top & ~mate_mask)

    return columns


def verify(h: int) -> None:
    columns = columns_for_h(h)
    n = len(columns)
    pc = cdc.precompute(n)
    adj = cdc.columns_to_adjacency(columns)
    mask = cdc.columns_to_mask(columns, pc)
    homogeneous, kind, vertices = cdc.max_homogeneous(adj, pc)
    regular, degree, regular_vertices = cdc.max_regular(adj, pc)
    print(f"h={h}")
    print(f"n={n}")
    print("columns=" + ",".join(map(str, columns)))
    print(f"mask={mask}")
    print(f"max_full_drop={fdc.max_full_drop(adj, n)}")
    print(f"max_column_drop={cdc.max_column_drop(adj, n)}")
    print(f"max_homogeneous={homogeneous}")
    print(f"homogeneous_kind={kind}")
    print("homogeneous_vertices=" + ",".join(map(str, vertices)))
    print(f"max_regular={regular}")
    print(f"regular_degree={degree}")
    print("regular_vertices=" + ",".join(map(str, regular_vertices)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("h", type=int)
    args = parser.parse_args()
    verify(args.h)


if __name__ == "__main__":
    main()
