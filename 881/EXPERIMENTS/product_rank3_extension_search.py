#!/usr/bin/env python3
"""Search for a fourth packet extending Example 8.5a.7z.

The seed from `product_rank3_terminal_cover.py` has three two-point packets
whose selector triples all have terminal-gap witnesses.  This script asks
for a bounded one-step extension: add a fourth two-point packet, optionally
with a few filler elements, and require every 3-of-4 packet selector triple
to have the same kind of witness while all singleton and pair deletions are
harmless on the witness window.

This is a finite diagnostic only.  A failed bounded search is not a proof.
It records the immediate staging pressure for the local rank-3 product
window.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import combinations, product


SEED_A = frozenset({1, 3, 4, 5, 8, 10, 11, 12})
SEED_BLOCKS = ((4, 10), (5, 11), (8, 12))
ORDER2_THRESHOLD = 4
WITNESS_START = 14


@cache
def hsum_cached(elements: frozenset[int], order: int, cap: int) -> frozenset[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(order):
        sums = {
            value + element
            for value in sums
            for element in ordered
            if value + element <= cap
        }
    return frozenset(sums)


def covers(values: frozenset[int], start: int, end: int) -> bool:
    return start <= end and all(target in values for target in range(start, end + 1))


def cover_end(values: frozenset[int], start: int, cap: int) -> int:
    target = start
    while target <= cap and target in values:
        target += 1
    return target - 1


def minimal_hole(elements: frozenset[int], deletion: tuple[int, ...], witness: int) -> bool:
    removed = frozenset(deletion)
    if witness in hsum_cached(elements - removed, 3, witness):
        return False
    return all(
        witness in hsum_cached(elements - (removed - {point}), 3, witness)
        for point in removed
    )


def terminal_gap(
    elements: frozenset[int],
    deletion: tuple[int, ...],
    witness: int,
) -> bool:
    removed = frozenset(deletion)
    left = witness - min(deletion) - min(elements)
    right = witness - ORDER2_THRESHOLD
    return not any(left < point <= right for point in elements - removed)


def selector_witnesses(
    elements: frozenset[int],
    blocks: tuple[tuple[int, int], ...],
    witness_end: int,
) -> dict[tuple[tuple[int, ...], tuple[int, ...]], list[int]] | None:
    out: dict[tuple[tuple[int, ...], tuple[int, ...]], list[int]] = {}
    for block_indices in combinations(range(len(blocks)), 3):
        for selector in product(*(blocks[index] for index in block_indices)):
            witnesses = [
                witness
                for witness in range(max(WITNESS_START, max(selector) - 1), witness_end + 1)
                if terminal_gap(elements, selector, witness)
                and minimal_hole(elements, selector, witness)
            ]
            if not witnesses:
                return None
            out[(block_indices, selector)] = witnesses
    return out


def check_candidate(
    elements: frozenset[int],
    blocks: tuple[tuple[int, int], ...],
) -> tuple[int, int, dict[tuple[tuple[int, ...], tuple[int, ...]], list[int]]] | None:
    cap = 3 * max(elements)
    two_sums = hsum_cached(elements, 2, cap)
    two_end = cover_end(two_sums, ORDER2_THRESHOLD, cap)
    witness_end = two_end - min(elements)
    if witness_end < WITNESS_START:
        return None

    for rank in (1, 2):
        for deletion in combinations(sorted(elements), rank):
            retained = elements - frozenset(deletion)
            if not covers(hsum_cached(retained, 3, cap), WITNESS_START, witness_end):
                return None

    witnesses = selector_witnesses(elements, blocks, witness_end)
    if witnesses is None:
        return None
    return two_end, witness_end, witnesses


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-value", type=int, default=30)
    parser.add_argument("--max-fillers", type=int, default=1)
    parser.add_argument("--limit", type=int, default=1)
    args = parser.parse_args()

    found = 0
    checked = 0
    candidate_values = [
        value
        for value in range(13, args.max_value + 1)
        if value not in SEED_A
    ]

    for filler_count in range(args.max_fillers + 1):
        for new_block in combinations(candidate_values, 2):
            filler_pool = [value for value in candidate_values if value not in new_block]
            for fillers in combinations(filler_pool, filler_count):
                checked += 1
                elements = frozenset(SEED_A | set(new_block) | set(fillers))
                blocks = SEED_BLOCKS + (tuple(new_block),)
                result = check_candidate(elements, blocks)
                if result is None:
                    continue

                two_end, witness_end, witnesses = result
                found += 1
                print("rank-3 product extension found")
                print(f"A={sorted(elements)}")
                print(f"new_block={new_block}")
                print(f"fillers={fillers}")
                print(f"blocks={blocks}")
                print(f"two_coverage=({ORDER2_THRESHOLD}, {two_end})")
                print(f"witness_window=({WITNESS_START}, {witness_end})")
                for key, values in witnesses.items():
                    print(f"{key}: {values[:4]}")
                if found >= args.limit:
                    print(f"checked={checked}")
                    return

    print("no rank-3 product extension found")
    print(f"max_value={args.max_value}")
    print(f"max_fillers={args.max_fillers}")
    print(f"checked={checked}")


if __name__ == "__main__":
    main()
