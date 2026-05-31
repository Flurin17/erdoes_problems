#!/usr/bin/env python3
"""Search finite windows for terminal gaps that are genuine A-gaps.

This is a toy diagnostic for Corollary 10.3d in PROOF.md.  It searches
finite order-2 windows for inclusion-minimal collective order-3 holes
whose terminal forbidden interval contains no elements of the finite set at
all, not merely no retained elements after the deletion.
"""

from __future__ import annotations

import argparse
from itertools import combinations


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def cover_end(elements: set[int], start: int, cap: int) -> int:
    sums = hsum(elements, 2, cap)
    x = start
    while x <= cap and x in sums:
        x += 1
    return x - 1


def minimal_hole(elements: set[int], deletion: tuple[int, ...], witness: int) -> bool:
    removed = set(deletion)
    if witness in hsum(elements - removed, 3, witness):
        return False
    return all(
        witness in hsum(elements - (removed - {f}), 3, witness)
        for f in removed
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-value", type=int, default=45)
    parser.add_argument("--max-size", type=int, default=13)
    parser.add_argument("--max-rank", type=int, default=5)
    parser.add_argument("--min-gap", type=int, default=3)
    args = parser.parse_args()

    threshold = 2
    for max_value in range(8, args.max_value + 1):
        universe = range(1, max_value + 1)
        for size in range(5, min(max_value, args.max_size) + 1):
            for tuple_a in combinations(universe, size):
                elements = set(tuple_a)
                coverage = cover_end(elements, threshold, 3 * max_value)
                if coverage < max_value:
                    continue

                m0 = min(elements)
                for rank in range(2, min(args.max_rank, size) + 1):
                    for deletion in combinations(sorted(elements), rank):
                        for witness in range(max(deletion) + 1, coverage + 1):
                            if not minimal_hole(elements, deletion, witness):
                                continue
                            gap_left = witness - min(deletion) - m0
                            gap_right = witness - threshold
                            if gap_right - gap_left < args.min_gap:
                                continue
                            if gap_left <= max(deletion):
                                continue
                            actual_gap = [
                                x
                                for x in sorted(elements)
                                if gap_left < x <= gap_right
                            ]
                            if actual_gap:
                                continue
                            print("actual terminal-gap barrier")
                            print("A=", sorted(elements), "coverage=", (threshold, coverage))
                            print(
                                "F=", deletion,
                                "w=", witness,
                                "gap=", (gap_left, gap_right),
                                "gap_length=", gap_right - gap_left,
                            )
                            return
    print("no actual terminal-gap barrier found within searched bounds")


if __name__ == "__main__":
    main()
