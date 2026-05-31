#!/usr/bin/env python3
"""Search finite analogues of collective delayed barriers.

This is a diagnostic for Corollary 3.1e' in PROOF.md.  It looks for a
finite order-2 window S and a finite deletion F such that:

* 2S covers a tail of the finite box;
* every proper nonempty G subset F has an early finite 3S-tail after
  deleting G;
* deleting F still has a finite 3S-tail, but the first such tail starts at
  or beyond max(F);
* some witness w >= max(F)-1 below that tail is an inclusion-minimal
  three-fold hole for F.

This is only a finite model.  A finite tail endpoint is not an asymptotic
threshold, but the search is useful for finding local shapes that satisfy
the delayed-barrier checklist.
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


def covers(values: set[int], start: int, end: int) -> bool:
    return all(n in values for n in range(start, end + 1))


def first_tail(values: set[int], start: int, end: int) -> int | None:
    for base in range(start, end + 1):
        if covers(values, base, end):
            return base
    return None


def minimal_hole(elements: set[int], deletion: tuple[int, ...], witness: int) -> bool:
    removed = set(deletion)
    if witness in hsum(elements - removed, 3, witness):
        return False
    return all(
        witness in hsum(elements - (removed - {f}), 3, witness)
        for f in removed
    )


def proper_subsets(items: tuple[int, ...]) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for size in range(1, len(items)):
        out.extend(combinations(items, size))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, default=2)
    parser.add_argument("--max-value", type=int, default=28)
    parser.add_argument("--max-size", type=int, default=11)
    parser.add_argument("--tail-start", type=int, default=2)
    parser.add_argument("--cap-mult", type=int, default=3)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    found = 0
    for max_value in range(max(7, args.rank + 4), args.max_value + 1):
        cap = args.cap_mult * max_value
        for size in range(args.rank + 2, min(max_value, args.max_size) + 1):
            for tuple_s in combinations(range(1, max_value + 1), size):
                if tuple_s[-1] != max_value:
                    continue
                elements = set(tuple_s)
                two_end = 2 * max(elements)
                two_tail = first_tail(hsum(elements, 2, cap), args.tail_start, two_end)
                if two_tail is None or two_tail > max_value:
                    continue

                for deletion in combinations(tuple_s, args.rank):
                    kept = elements - set(deletion)
                    if not kept:
                        continue
                    tail_end = 3 * max(kept)
                    if tail_end < max(deletion):
                        continue
                    tail = first_tail(hsum(kept, 3, cap), args.tail_start, tail_end)
                    if tail is None or tail < max(deletion):
                        continue

                    holes = [
                        w
                        for w in range(max(deletion) - 1, tail)
                        if minimal_hole(elements, deletion, w)
                    ]
                    if not holes:
                        continue

                    proper_ok = True
                    proper_tails: list[tuple[tuple[int, ...], int]] = []
                    for sub in proper_subsets(deletion):
                        sub_kept = elements - set(sub)
                        sub_end = 3 * max(sub_kept)
                        sub_tail = first_tail(
                            hsum(sub_kept, 3, cap),
                            args.tail_start,
                            sub_end,
                        )
                        if sub_tail is None or sub_tail >= max(sub):
                            proper_ok = False
                            break
                        proper_tails.append((sub, sub_tail))
                    if not proper_ok:
                        continue

                    print("finite collective delayed barrier")
                    print("rank=", args.rank, "S=", sorted(elements))
                    print("2-tail=", (two_tail, two_end), "cap=", cap)
                    print("F=", deletion, "3-tail-after-F=", (tail, tail_end))
                    print("minimal holes=", holes[:8])
                    print("proper tails=", proper_tails[:12])
                    found += 1
                    if found >= args.limit:
                        return

    print("no finite collective delayed barrier found within searched bounds")


if __name__ == "__main__":
    main()
