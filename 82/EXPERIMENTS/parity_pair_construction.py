#!/usr/bin/env python3
"""Generate and test a parity-cross marked-pair obstruction candidate."""

from __future__ import annotations

import argparse
from itertools import combinations

import balanced_pair_parameter_search
import regular_bitset


def edge_index(n: int) -> dict[tuple[int, int], int]:
    return {edge: index for index, edge in enumerate(combinations(range(n), 2))}


def add_edge(mask: int, index: dict[tuple[int, int], int], u: int, v: int) -> int:
    if u > v:
        u, v = v, u
    return mask | (1 << index[(u, v)])


def construction_mask(h: int) -> int:
    """Return a marked graph with |A|=|B|=h.

    A has one edge a0-a1.  B has a clique on b0,...,b_{h-2} and one isolated
    vertex b_{h-1}.  Cross edges are parity edges a_i b_j with i+j even.
    """
    n = 2 * h
    index = edge_index(n)
    mask = 0
    mask = add_edge(mask, index, 0, 1)
    for u, v in combinations(range(h, 2 * h - 1), 2):
        mask = add_edge(mask, index, u, v)
    for i in range(h):
        for j in range(h):
            if (i + j) % 2 == 0:
                mask = add_edge(mask, index, i, h + j)
    return mask


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("h", type=int)
    args = parser.parse_args()
    if args.h < 3:
        parser.error("h must be at least 3")

    n = 2 * args.h
    mask = construction_mask(args.h)
    adj = regular_bitset.build_adjacency(n, mask)
    has_regular, regular_order = balanced_pair_parameter_search.has_regular_at_least(
        adj, n, args.h
    )
    r = (args.h - 1) // 2
    balanced = balanced_pair_parameter_search.balanced_witness(adj, args.h, r, r)

    print(f"h={args.h}")
    print(f"n={n}")
    print(f"side_size={args.h}")
    print(f"balanced_side_size={r}")
    print(f"mask={mask}")
    print(f"has_regular_at_least_h={has_regular}")
    if has_regular:
        print(f"found_regular_order={regular_order}")
    print(f"has_balanced_plus_middle={balanced is not None}")
    if balanced is not None:
        x_vertices, y_vertices = balanced
        print("X=" + ",".join(map(str, x_vertices)))
        print("Y=" + ",".join(map(str, y_vertices)))
    print(f"plus_obstruction={not has_regular and balanced is None}")


if __name__ == "__main__":
    main()
