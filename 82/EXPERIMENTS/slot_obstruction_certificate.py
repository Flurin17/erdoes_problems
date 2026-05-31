#!/usr/bin/env python3
"""Verify finite certificates that kill all fixed slot multisets."""

from __future__ import annotations

import argparse
from itertools import combinations_with_replacement

import modular_partition
import regular_induced as ri
import universal_slots


def verify(
    n: int,
    source_modulus: int,
    source_residue: int,
    target_modulus: int,
    slot_count: int,
    masks: list[int],
) -> None:
    pc = ri.precompute(n)
    full = (1 << n) - 1
    candidates = list(combinations_with_replacement(range(target_modulus), slot_count))
    remaining = set(candidates)

    print(f"n={n}")
    print(f"source_modulus={source_modulus}")
    print(f"source_residue={source_residue % source_modulus}")
    print(f"target_modulus={target_modulus}")
    print(f"slot_count={slot_count}")
    print(f"candidate_count={len(candidates)}")

    for index, graph_mask in enumerate(masks, 1):
        residue = modular_partition.residue_on(graph_mask, full, source_modulus, pc)
        if residue != source_residue % source_modulus:
            print(f"mask{index}={graph_mask}")
            print(f"bad_source_residue={residue}")
            return

        killed = []
        for slots in list(remaining):
            if not universal_slots.has_slot_partition(
                n, graph_mask, target_modulus, slots, pc
            ):
                killed.append(slots)
        for slots in killed:
            remaining.remove(slots)

        print(
            f"mask{index}={graph_mask} "
            f"killed_now={len(killed)} remaining={len(remaining)}"
        )

    if remaining:
        print("certificate_ok=False")
        print("remaining_slots=" + ";".join(",".join(map(str, slots)) for slots in sorted(remaining)))
    else:
        print("certificate_ok=True")


def parse_masks(raw: str) -> list[int]:
    return [int(item) for item in raw.replace(",", " ").split()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--source-modulus", type=int, required=True)
    parser.add_argument("--source-residue", type=int, required=True)
    parser.add_argument("--target-modulus", type=int, required=True)
    parser.add_argument("--slot-count", type=int, required=True)
    parser.add_argument("--masks", required=True, help="comma- or space-separated graph masks")
    args = parser.parse_args()
    verify(
        args.n,
        args.source_modulus,
        args.source_residue,
        args.target_modulus,
        args.slot_count,
        parse_masks(args.masks),
    )


if __name__ == "__main__":
    main()
