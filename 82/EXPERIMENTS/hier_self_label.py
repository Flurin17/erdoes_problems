#!/usr/bin/env python3
"""Test hierarchical routes from a self-labelled mod-2 split to mod-4 slots.

The default route is:
1. split V into a self-labelled mod-2 partition, so the 0-side has even
   internal degrees and the 1-side has odd internal degrees;
2. split the 0-side into residues {0,2} modulo 4 and the 1-side into
   residues {1,3} modulo 4.

This is stronger than an arbitrary self-labelled mod-4 coloring.  The script
checks the condition by precomputing all subset residues once.
"""

from __future__ import annotations

import argparse
from functools import lru_cache

import modular_partition
import regular_induced as ri


def subset_residues(n: int, graph_mask: int, modulus: int) -> list[int | None]:
    pc = ri.precompute(n)
    residues: list[int | None] = [0] * (1 << n)
    for subset in range(1, 1 << n):
        residues[subset] = modular_partition.residue_on(graph_mask, subset, modulus, pc)
    return residues


def has_slot_split(
    subset: int,
    slots: tuple[int, int],
    residues4: list[int | None],
) -> bool:
    if subset == 0:
        return True
    slot_a, slot_b = slots
    if residues4[subset] in slots:
        return True

    pivot = subset & -subset
    part = subset
    while part:
        if part & pivot:
            rest = subset ^ part
            if residues4[part] == slot_a and (rest == 0 or residues4[rest] == slot_b):
                return True
            if residues4[part] == slot_b and (rest == 0 or residues4[rest] == slot_a):
                return True
        part = (part - 1) & subset
    return False


def find_hierarchical(
    n: int,
    graph_mask: int,
    even_slots: tuple[int, int],
    odd_slots: tuple[int, int],
) -> tuple[int, tuple[int, int, int, int]] | None:
    full = (1 << n) - 1
    residues2 = subset_residues(n, graph_mask, 2)
    residues4 = subset_residues(n, graph_mask, 4)

    @lru_cache(maxsize=None)
    def side_ok(subset: int, slots: tuple[int, int]) -> bool:
        return has_slot_split(subset, slots, residues4)

    for odd_side in range(1 << n):
        even_side = full ^ odd_side
        if even_side and residues2[even_side] != 0:
            continue
        if odd_side and residues2[odd_side] != 1:
            continue
        if side_ok(even_side, even_slots) and side_ok(odd_side, odd_slots):
            return odd_side, (
                residues4[even_side] if even_side else -1,
                residues4[odd_side] if odd_side else -1,
                even_side.bit_count(),
                odd_side.bit_count(),
            )
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--even-slots", default="0,2")
    parser.add_argument("--odd-slots", default="1,3")
    args = parser.parse_args()
    even_slots = tuple(int(item) % 4 for item in args.even_slots.split(","))
    odd_slots = tuple(int(item) % 4 for item in args.odd_slots.split(","))
    if len(even_slots) != 2 or len(odd_slots) != 2:
        raise SystemExit("--even-slots and --odd-slots must each contain two residues")
    result = find_hierarchical(args.n, args.mask, even_slots, odd_slots)
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print("even_slots=" + ",".join(map(str, even_slots)))
    print("odd_slots=" + ",".join(map(str, odd_slots)))
    if result is None:
        print("hier_self_label=no")
        return
    odd_side, stats = result
    print("hier_self_label=yes")
    print(f"odd_side_mask={odd_side}")
    print("stats=even_residue,odd_residue,even_size,odd_size")
    print(",".join(map(str, stats)))


if __name__ == "__main__":
    main()
