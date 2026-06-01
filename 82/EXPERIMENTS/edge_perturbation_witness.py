#!/usr/bin/env python3
"""Inspect regular witnesses created by adding or deleting one edge."""

from __future__ import annotations

import argparse
from itertools import combinations

import regular_bitset


def edge_index(n: int) -> dict[tuple[int, int], int]:
    return {edge: index for index, edge in enumerate(combinations(range(n), 2))}


def has_edge(mask: int, u: int, v: int, index: dict[tuple[int, int], int]) -> bool:
    if u > v:
        u, v = v, u
    return bool(mask & (1 << index[(u, v)]))


def perturb(mask: int, u: int, v: int, index: dict[tuple[int, int], int]) -> int:
    if u > v:
        u, v = v, u
    return mask ^ (1 << index[(u, v)])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--threshold", type=int, required=True)
    parser.add_argument("--mode", choices=("add", "delete", "both"), default="both")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    index = edge_index(args.n)
    checked = 0
    successes = 0
    containing_pair = 0
    examples: list[str] = []

    for u, v in combinations(range(args.n), 2):
        present = has_edge(args.mask, u, v, index)
        if args.mode == "add" and present:
            continue
        if args.mode == "delete" and not present:
            continue
        checked += 1
        changed = perturb(args.mask, u, v, index)
        adj = regular_bitset.build_adjacency(args.n, changed)
        witness: tuple[int, ...] | None = None
        degree: int | None = None
        for order in range(args.n, args.threshold - 1, -1):
            found, found_degree, _checks = regular_bitset.find_regular_order(
                adj, args.n, order, max_checks=None
            )
            if found is not None:
                witness = found
                degree = found_degree
                break
        if witness is None:
            continue
        successes += 1
        if u in witness and v in witness:
            containing_pair += 1
        if len(examples) < args.limit:
            action = "delete" if present else "add"
            examples.append(
                "{} {}-{} order={} degree={} contains_pair={} witness={}".format(
                    action,
                    u,
                    v,
                    len(witness),
                    degree,
                    u in witness and v in witness,
                    ",".join(map(str, witness)),
                )
            )

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"threshold={args.threshold}")
    print(f"mode={args.mode}")
    print(f"pairs_checked={checked}")
    print(f"successful_perturbations={successes}")
    print(f"successes_containing_pair={containing_pair}")
    for example in examples:
        print("example=" + example)


if __name__ == "__main__":
    main()
