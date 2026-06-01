#!/usr/bin/env python3
"""Greedily make a fixed graph edge-maximal or edge-minimal below a threshold."""

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


def flip(mask: int, u: int, v: int, index: dict[tuple[int, int], int]) -> int:
    if u > v:
        u, v = v, u
    return mask ^ (1 << index[(u, v)])


def has_regular_at_least(n: int, mask: int, threshold: int) -> bool:
    adj = regular_bitset.build_adjacency(n, mask)
    for order in range(n, threshold - 1, -1):
        witness, _degree, _checks = regular_bitset.find_regular_order(
            adj, n, order, max_checks=None
        )
        if witness is not None:
            return True
    return False


def edge_count(mask: int) -> int:
    return mask.bit_count()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--threshold", type=int, required=True)
    parser.add_argument("--mode", choices=("add", "delete"), required=True)
    args = parser.parse_args()

    if has_regular_at_least(args.n, args.mask, args.threshold):
        raise SystemExit("initial mask already has a regular witness at threshold")

    index = edge_index(args.n)
    mask = args.mask
    changes: list[tuple[int, int]] = []
    changed = True
    while changed:
        changed = False
        for u, v in combinations(range(args.n), 2):
            present = has_edge(mask, u, v, index)
            if args.mode == "add" and present:
                continue
            if args.mode == "delete" and not present:
                continue
            candidate = flip(mask, u, v, index)
            if not has_regular_at_least(args.n, candidate, args.threshold):
                mask = candidate
                changes.append((u, v))
                changed = True

    blocked = 0
    available = 0
    for u, v in combinations(range(args.n), 2):
        present = has_edge(mask, u, v, index)
        if args.mode == "add" and present:
            continue
        if args.mode == "delete" and not present:
            continue
        available += 1
        if has_regular_at_least(args.n, flip(mask, u, v, index), args.threshold):
            blocked += 1

    print(f"n={args.n}")
    print(f"initial_mask={args.mask}")
    print(f"threshold={args.threshold}")
    print(f"mode={args.mode}")
    print(f"changes={len(changes)}")
    print("changed_edges=" + ",".join(f"{u}-{v}" for u, v in changes))
    print(f"final_mask={mask}")
    print(f"final_edge_count={edge_count(mask)}")
    print(f"remaining_pairs={available}")
    print(f"blocking_perturbations={blocked}")
    print(f"saturated={blocked == available}")


if __name__ == "__main__":
    main()
