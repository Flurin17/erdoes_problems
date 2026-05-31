#!/usr/bin/env python3
"""Search source-residue slot families in complete multipartite models."""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations_with_replacement

import multipartite_modular as mm


def slot_weight(residue: int, modulus: int) -> int:
    value = (residue + 1) % modulus
    return modulus if value == 0 else value


def subset_sum(slots: tuple[int, ...], modulus: int, target: int) -> bool:
    weights = [slot_weight(residue, modulus) for residue in slots]
    possible = {0}
    for weight in weights:
        possible |= {value + weight for value in list(possible)}
    return target in possible


def passes_clique_test(
    slots: tuple[int, ...],
    source_modulus: int,
    source_residue: int,
    target_modulus: int,
) -> bool:
    first = (source_residue + 1) % target_modulus
    if first == 0:
        first = target_modulus
    second = first + source_modulus
    if second > target_modulus:
        second -= target_modulus
    if second == 0:
        second = target_modulus
    return subset_sum(slots, target_modulus, first) and subset_sum(
        slots, target_modulus, second
    )


def source_degree_residue(sizes: tuple[int, ...], source_modulus: int) -> int:
    return (sum(sizes) - sizes[0]) % source_modulus


def source_vectors(
    source_modulus: int,
    source_residue: int,
    max_classes: int,
    max_size: int,
) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for classes in range(1, max_classes + 1):
        for sizes in combinations_with_replacement(range(1, max_size + 1), classes):
            if not mm.full_is_modular(sizes, source_modulus):
                continue
            if source_degree_residue(sizes, source_modulus) != source_residue % source_modulus:
                continue
            out.append(sizes)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-modulus", type=int, required=True)
    parser.add_argument("--target-modulus", type=int, required=True)
    parser.add_argument("--source-residue", type=int, required=True)
    parser.add_argument("--slot-count", type=int, required=True)
    parser.add_argument("--max-classes", type=int, default=5)
    parser.add_argument("--max-size", type=int, default=16)
    parser.add_argument("--max-vectors", type=int)
    parser.add_argument("--max-survivors", type=int, default=20)
    parser.add_argument("--no-clique-filter", action="store_true")
    args = parser.parse_args()

    candidates = list(
        combinations_with_replacement(range(args.target_modulus), args.slot_count)
    )
    if not args.no_clique_filter:
        candidates = [
            slots
            for slots in candidates
            if passes_clique_test(
                slots,
                args.source_modulus,
                args.source_residue,
                args.target_modulus,
            )
        ]

    vectors = source_vectors(
        args.source_modulus,
        args.source_residue,
        args.max_classes,
        args.max_size,
    )

    @lru_cache(maxsize=None)
    def can_partition(sizes: tuple[int, ...], slots: tuple[int, ...]) -> bool:
        return mm.can_slot_partition(sizes, args.target_modulus, slots)

    survivors = list(candidates)
    killed_by: dict[tuple[int, ...], tuple[int, ...]] = {}
    checked_vectors = 0
    truncated = False
    for sizes in vectors:
        if args.max_vectors is not None and checked_vectors >= args.max_vectors:
            truncated = True
            break
        checked_vectors += 1
        next_survivors: list[tuple[int, ...]] = []
        for slots in survivors:
            if can_partition(sizes, slots):
                next_survivors.append(slots)
            else:
                killed_by.setdefault(slots, sizes)
        survivors = next_survivors
        if not survivors:
            break

    print(f"source_modulus={args.source_modulus}")
    print(f"source_residue={args.source_residue % args.source_modulus}")
    print(f"target_modulus={args.target_modulus}")
    print(f"slot_count={args.slot_count}")
    print(f"max_classes={args.max_classes}")
    print(f"max_size={args.max_size}")
    print(f"clique_filter={not args.no_clique_filter}")
    print(f"candidate_count={len(candidates)}")
    print(f"source_vectors={len(vectors)}")
    print(f"checked_vectors={checked_vectors}")
    print(f"truncated={truncated}")
    print(f"survivor_count={len(survivors)}")
    for slots in survivors[: args.max_survivors]:
        print("survivor=" + ",".join(map(str, slots)))
    if len(survivors) > args.max_survivors:
        print(f"survivor_omitted={len(survivors) - args.max_survivors}")
    if not survivors and killed_by:
        # The last vector considered killed the final survivors; report it as
        # a compact obstruction seed for reproducing the failure.
        print("last_killer=" + ",".join(map(str, sizes)))


if __name__ == "__main__":
    main()
