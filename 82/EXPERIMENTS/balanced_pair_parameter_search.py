#!/usr/bin/env python3
"""Sample marked two-part obstructions for the balanced pair parameter.

The vertex set is A union B with |A|=|B|=M.  For a target order h, put
r=ceil((h-2)/2).  The script searches for graphs with no regular induced
subgraph of order at least h and no balanced choice X subset A, Y subset B,
|X|=|Y|=r, whose induced middle graph has the requested degree.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations

import regular_bitset


def edge_index(n: int) -> dict[tuple[int, int], int]:
    return {edge: index for index, edge in enumerate(combinations(range(n), 2))}


def toggle(mask: int, u: int, v: int, index: dict[tuple[int, int], int]) -> int:
    if u > v:
        u, v = v, u
    return mask ^ (1 << index[(u, v)])


def subset_mask(vertices: tuple[int, ...]) -> int:
    out = 0
    for vertex in vertices:
        out |= 1 << vertex
    return out


def has_regular_at_least(adj: list[int], n: int, threshold: int) -> tuple[bool, int]:
    for order in range(n, threshold - 1, -1):
        witness, _degree, _checks = regular_bitset.find_regular_order(
            adj, n, order, max_checks=None
        )
        if witness is not None:
            return True, order
    return False, 0


def is_regular_with_degree(adj: list[int], mask: int, degree: int) -> bool:
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        vertex = bit.bit_length() - 1
        if (adj[vertex] & mask).bit_count() != degree:
            return False
        remaining ^= bit
    return True


def balanced_witness(
    adj: list[int],
    m: int,
    side_size: int,
    degree: int,
) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    left = tuple(range(m))
    right = tuple(range(m, 2 * m))
    left_masks = [(choice, subset_mask(choice)) for choice in combinations(left, side_size)]
    right_masks = [(choice, subset_mask(choice)) for choice in combinations(right, side_size)]
    for x_vertices, x_mask in left_masks:
        for y_vertices, y_mask in right_masks:
            if is_regular_with_degree(adj, x_mask | y_mask, degree):
                return x_vertices, y_vertices
    return None


def evaluate(mask: int, n: int, m: int, h: int, middle_degree: int) -> tuple[bool, int, object]:
    adj = regular_bitset.build_adjacency(n, mask)
    has_regular, regular_order = has_regular_at_least(adj, n, h)
    if has_regular:
        return False, regular_order, None
    r = (h - 1) // 2
    witness = balanced_witness(adj, m, r, middle_degree)
    return witness is None, 0, witness


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--h", type=int, required=True)
    parser.add_argument("--m", type=int, required=True, help="size of each marked side")
    parser.add_argument("--mode", choices=("plus", "minus"), default="plus")
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--hill-steps", type=int, default=0)
    parser.add_argument("--mask", type=int, help="inspect one fixed graph mask")
    args = parser.parse_args()

    n = 2 * args.m
    r = (args.h - 1) // 2
    middle_degree = r if args.mode == "plus" else r - 1
    if middle_degree < 0:
        parser.error("middle degree is negative")

    rng = random.Random(args.seed)
    edges = list(combinations(range(n), 2))
    index = edge_index(n)

    print(f"h={args.h}")
    print(f"side_size={args.m}")
    print(f"mode={args.mode}")
    print(f"balanced_side_size={r}")
    print(f"middle_degree={middle_degree}")

    if args.mask is not None:
        ok, regular_order, witness = evaluate(args.mask, n, args.m, args.h, middle_degree)
        print(f"mask={args.mask}")
        print(f"has_regular_at_least_h={regular_order != 0}")
        if regular_order:
            print(f"found_regular_order={regular_order}")
        print(f"has_balanced_middle={witness is not None}")
        if witness is not None:
            x_vertices, y_vertices = witness
            print("X=" + ",".join(map(str, x_vertices)))
            print("Y=" + ",".join(map(str, y_vertices)))
        print(f"obstruction={ok}")
        return

    best_regular_order = n + 1
    best_mask = 0
    found_obstruction: int | None = None

    for sample in range(args.samples):
        mask = rng.getrandbits(len(edges))
        ok, regular_order, witness = evaluate(mask, n, args.m, args.h, middle_degree)
        if ok:
            found_obstruction = mask
            break
        if regular_order and regular_order < best_regular_order:
            best_regular_order = regular_order
            best_mask = mask

        for _step in range(args.hill_steps):
            u, v = rng.choice(edges)
            candidate = toggle(mask, u, v, index)
            candidate_ok, candidate_order, _candidate_witness = evaluate(
                candidate, n, args.m, args.h, middle_degree
            )
            if candidate_ok:
                found_obstruction = candidate
                break
            if candidate_order and candidate_order < regular_order:
                mask = candidate
                regular_order = candidate_order
                if regular_order < best_regular_order:
                    best_regular_order = regular_order
                    best_mask = mask
            elif rng.random() < 0.01:
                mask = candidate
                regular_order = candidate_order
        if found_obstruction is not None:
            break

    print(f"samples={args.samples}")
    print(f"hill_steps={args.hill_steps}")
    if found_obstruction is None:
        print("obstruction_found=False")
        if best_regular_order <= n:
            print(f"best_regular_order_seen={best_regular_order}")
            print(f"best_mask={best_mask}")
    else:
        print("obstruction_found=True")
        print(f"mask={found_obstruction}")


if __name__ == "__main__":
    main()
