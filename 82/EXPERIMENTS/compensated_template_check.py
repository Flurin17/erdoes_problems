#!/usr/bin/env python3
"""Check and inspect the compensated double spread-one template."""

from __future__ import annotations

import argparse
from itertools import combinations

import regular_induced as ri


def edge_index(pc: ri.Precomp) -> dict[tuple[int, int], int]:
    return {edge: index for index, edge in enumerate(pc.edges)}


def has_edge(mask: int, u: int, v: int, index: dict[tuple[int, int], int]) -> bool:
    if u > v:
        u, v = v, u
    return bool(mask & (1 << index[(u, v)]))


def vertices_from_csv(text: str | None) -> list[int]:
    if not text:
        return []
    return [int(part) for part in text.split(",") if part]


def base_degrees(mask: int, m: int, index: dict[tuple[int, int], int]) -> list[int]:
    return [
        sum(has_edge(mask, i, j, index) for j in range(m) if j != i)
        for i in range(m)
    ]


def cross_row_degrees(mask: int, m: int, index: dict[tuple[int, int], int]) -> list[int]:
    return [sum(has_edge(mask, i, m + j, index) for j in range(m)) for i in range(m)]


def cross_col_degrees(mask: int, m: int, index: dict[tuple[int, int], int]) -> list[int]:
    return [sum(has_edge(mask, i, m + j, index) for i in range(m)) for j in range(m)]


def check_template(mask: int, m: int, index: dict[tuple[int, int], int]) -> tuple[bool, list[int]]:
    ok = True
    for i, j in combinations(range(m), 2):
        if has_edge(mask, i, j, index) == has_edge(mask, m + i, m + j, index):
            ok = False
    d = base_degrees(mask, m, index)
    rows = cross_row_degrees(mask, m, index)
    cols = cross_col_degrees(mask, m, index)
    eps: list[int] = []
    for i in range(m):
        if rows[i] != m - 1 - d[i]:
            ok = False
        epsilon = cols[i] - d[i]
        eps.append(epsilon)
        if epsilon not in (0, 1):
            ok = False
    return ok, eps


def induced_base_degree(
    mask: int,
    vertex: int,
    subset: list[int],
    index: dict[tuple[int, int], int],
) -> int:
    return sum(has_edge(mask, vertex, other, index) for other in subset if other != vertex)


def cross_degree_to_indices(
    mask: int,
    a_index: int,
    b_indices: list[int],
    m: int,
    index: dict[tuple[int, int], int],
) -> int:
    return sum(has_edge(mask, a_index, m + j, index) for j in b_indices)


def cross_degree_from_indices(
    mask: int,
    b_index: int,
    a_indices: list[int],
    m: int,
    index: dict[tuple[int, int], int],
) -> int:
    return sum(has_edge(mask, i, m + b_index, index) for i in a_indices)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--witness", help="comma-separated vertices from the 2m graph")
    args = parser.parse_args()

    pc = ri.precompute(2 * args.m)
    index = edge_index(pc)
    ok, eps = check_template(args.mask, args.m, index)
    d = base_degrees(args.mask, args.m, index)
    rows = cross_row_degrees(args.mask, args.m, index)
    cols = cross_col_degrees(args.mask, args.m, index)
    full = (1 << (2 * args.m)) - 1
    full_degrees = [(args.mask & pc.incident[full][v]).bit_count() for v in range(2 * args.m)]

    print(f"m={args.m}")
    print(f"n={2 * args.m}")
    print(f"mask={args.mask}")
    print(f"template_ok={ok}")
    print("base_degrees=" + ",".join(map(str, d)))
    print("cross_row_degrees=" + ",".join(map(str, rows)))
    print("cross_col_degrees=" + ",".join(map(str, cols)))
    print("epsilon=" + ",".join(map(str, eps)))
    print("full_degrees=" + ",".join(map(str, full_degrees)))

    witness = vertices_from_csv(args.witness)
    if witness:
        a_indices = sorted(v for v in witness if v < args.m)
        b_indices = sorted(v - args.m for v in witness if v >= args.m)
        subset_mask = sum(1 << v for v in witness)
        degree = (args.mask & pc.incident[subset_mask][witness[0]]).bit_count()
        print("witness=" + ",".join(map(str, witness)))
        print(f"witness_regular={ri.is_regular_on(args.mask, subset_mask, pc)}")
        print(f"witness_degree={degree}")
        print("U=" + ",".join(map(str, a_indices)))
        print("V=" + ",".join(map(str, b_indices)))

        a_profiles = []
        for i in a_indices:
            internal = induced_base_degree(args.mask, i, a_indices, index)
            cross = cross_degree_to_indices(args.mask, i, b_indices, args.m, index)
            a_profiles.append(f"{i}:{internal}+{cross}={internal + cross}")

        b_profiles = []
        for j in b_indices:
            base_internal = induced_base_degree(args.mask, j, b_indices, index)
            internal = len(b_indices) - 1 - base_internal
            cross = cross_degree_from_indices(args.mask, j, a_indices, args.m, index)
            b_profiles.append(f"{j}:{internal}+{cross}={internal + cross}")

        print("A_profiles=" + ",".join(a_profiles))
        print("B_profiles=" + ",".join(b_profiles))


if __name__ == "__main__":
    main()
