#!/usr/bin/env python3
"""Summarize pair-role signatures inside largest regular witnesses."""

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


def paley_mask(p: int, pc: ri.Precomp) -> int:
    residues = {(x * x) % p for x in range(1, p)}
    mask = 0
    for index, (u, v) in enumerate(pc.edges):
        if (u - v) % p in residues:
            mask |= 1 << index
    return mask


def role_counts(
    mask: int,
    subset_vertices: list[int],
    u: int,
    v: int,
    index: dict[tuple[int, int], int],
) -> tuple[int, int, int, int]:
    counts = {"A": 0, "B": 0, "C": 0, "E": 0}
    for w in subset_vertices:
        if w == u or w == v:
            continue
        uw = has_edge(mask, u, w, index)
        vw = has_edge(mask, v, w, index)
        if uw and not vw:
            counts["A"] += 1
        elif vw and not uw:
            counts["B"] += 1
        elif uw and vw:
            counts["C"] += 1
        else:
            counts["E"] += 1
    return counts["A"], counts["B"], counts["C"], counts["E"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--paley-prime", type=int)
    parser.add_argument("--max-witnesses", type=int, default=1000)
    args = parser.parse_args()

    if (args.mask is None) == (args.paley_prime is None):
        parser.error("provide exactly one of --mask or --paley-prime")
    if args.paley_prime is not None and args.paley_prime != args.n:
        parser.error("--paley-prime must equal n")

    pc = ri.precompute(args.n)
    index = edge_index(pc)
    mask = args.mask if args.mask is not None else paley_mask(args.paley_prime, pc)
    assert mask is not None

    max_order = ri.max_regular_order(mask, pc)
    role_count_hist: Counter[int] = Counter()
    signature_hist: Counter[tuple[int, int, int, int]] = Counter()
    min_role_count: int | None = None
    min_example: tuple[list[int], int, int, tuple[int, int, int, int]] | None = None
    witnesses_seen = 0

    for subset in pc.subsets_by_size_desc:
        size = len(pc.vertices[subset])
        if size < max_order or witnesses_seen >= args.max_witnesses:
            break
        if size > max_order or not ri.is_regular_on(mask, subset, pc):
            continue
        witnesses_seen += 1
        subset_vertices = pc.vertices[subset]
        for u, v in combinations(subset_vertices, 2):
            counts = role_counts(mask, subset_vertices, u, v, index)
            nonempty = sum(1 for count in counts if count)
            role_count_hist[nonempty] += 1
            signature_hist[counts] += 1
            if min_role_count is None or nonempty < min_role_count:
                min_role_count = nonempty
                min_example = (subset_vertices, u, v, counts)

    print(f"n={args.n}")
    print(f"mask={mask}")
    if args.paley_prime is not None:
        print(f"paley_prime={args.paley_prime}")
    print(f"max_regular_order={max_order}")
    print(f"max_regular_witnesses_inspected={witnesses_seen}")
    print(f"min_pair_nonempty_roles={min_role_count}")
    if min_example is not None:
        subset_vertices, u, v, counts = min_example
        print("example_witness=" + ",".join(map(str, subset_vertices)))
        print(f"example_pair={u},{v}")
        print("example_role_counts=A:{},B:{},C:{},E:{}".format(*counts))
    print("role_count_histogram=" + ",".join(
        f"{key}:{role_count_hist[key]}" for key in sorted(role_count_hist)
    ))
    print("top_signatures=" + ";".join(
        "A:{},B:{},C:{},E:{}:{}".format(*signature, count)
        for signature, count in signature_hist.most_common(10)
    ))


if __name__ == "__main__":
    main()
