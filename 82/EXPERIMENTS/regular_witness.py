#!/usr/bin/env python3
"""Print a largest regular induced witness and basic diagnostics."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations

import regular_induced as ri


def edge_index(pc: ri.Precomp) -> dict[tuple[int, int], int]:
    return {edge: index for index, edge in enumerate(pc.edges)}


def has_edge(mask: int, u: int, v: int, index: dict[tuple[int, int], int]) -> bool:
    if u > v:
        u, v = v, u
    return bool(mask & (1 << index[(u, v)]))


def largest_regular_subset(mask: int, pc: ri.Precomp) -> int:
    for subset in pc.subsets_by_size_desc:
        if ri.is_regular_on(mask, subset, pc):
            return subset
    return 0


def degrees_on(mask: int, subset: int, pc: ri.Precomp) -> list[tuple[int, int]]:
    return [
        (v, (mask & pc.incident[subset][v]).bit_count())
        for v in pc.vertices[subset]
    ]


def degree_to_set(
    mask: int,
    vertex: int,
    targets: list[int],
    index: dict[tuple[int, int], int],
) -> int:
    return sum(has_edge(mask, vertex, w, index) for w in targets if w != vertex)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--split", type=int, help="report counts below/above this index")
    args = parser.parse_args()

    pc = ri.precompute(args.n)
    index = edge_index(pc)
    subset = largest_regular_subset(args.mask, pc)
    vertices = pc.vertices[subset]
    full = (1 << args.n) - 1
    full_degrees = degrees_on(args.mask, full, pc)
    witness_degrees = degrees_on(args.mask, subset, pc)
    witness_edges = [
        (u, v)
        for u, v in combinations(vertices, 2)
        if has_edge(args.mask, u, v, index)
    ]

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print("full_degrees=" + ",".join(f"{v}:{d}" for v, d in full_degrees))
    print(f"max_regular_order={len(vertices)}")
    print("witness_vertices=" + ",".join(map(str, vertices)))
    print("witness_degrees=" + ",".join(f"{v}:{d}" for v, d in witness_degrees))
    print("witness_edges=" + " ".join(f"{u}-{v}" for u, v in witness_edges))
    if args.split is not None:
        left = [v for v in vertices if v < args.split]
        right = [v for v in vertices if v >= args.split]
        print(f"split={args.split}")
        print("left_vertices=" + ",".join(map(str, left)))
        print("right_vertices=" + ",".join(map(str, right)))
        print(f"left_count={len(left)}")
        print(f"right_count={len(right)}")
        print(
            "left_profile="
            + ",".join(
                f"{v}:{degree_to_set(args.mask, v, left, index)}"
                f"+{degree_to_set(args.mask, v, right, index)}"
                f"={degree_to_set(args.mask, v, vertices, index)}"
                for v in left
            )
        )
        left_hist = Counter(
            (
                degree_to_set(args.mask, v, left, index),
                degree_to_set(args.mask, v, right, index),
            )
            for v in left
        )
        print(
            "left_profile_hist="
            + ",".join(
                f"{internal}+{cross}:{count}"
                for (internal, cross), count in sorted(left_hist.items())
            )
        )
        print(
            "right_profile="
            + ",".join(
                f"{v}:{degree_to_set(args.mask, v, right, index)}"
                f"+{degree_to_set(args.mask, v, left, index)}"
                f"={degree_to_set(args.mask, v, vertices, index)}"
                for v in right
            )
        )
        right_hist = Counter(
            (
                degree_to_set(args.mask, v, right, index),
                degree_to_set(args.mask, v, left, index),
            )
            for v in right
        )
        print(
            "right_profile_hist="
            + ",".join(
                f"{internal}+{cross}:{count}"
                for (internal, cross), count in sorted(right_hist.items())
            )
        )


if __name__ == "__main__":
    main()
