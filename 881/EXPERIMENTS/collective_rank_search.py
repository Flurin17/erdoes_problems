#!/usr/bin/env python3
"""Search finite windows for genuinely high-rank collective holes.

For k=2, this looks for finite sets A such that:

* 2A covers a tail of the finite box;
* 3(A\\F) covers a test window for every |F| < rank;
* some rank-element deletion F creates a hole in that same window.

This is a finite analogue only. Endpoint artefacts are common, but the
search helps distinguish pair obstructions from higher-rank collective
barriers.
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


def cover_end(values: set[int], start: int, cap: int) -> int:
    x = start
    while x <= cap and x in values:
        x += 1
    return x - 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, default=3)
    parser.add_argument("--max-value", type=int, default=22)
    parser.add_argument("--max-size", type=int, default=11)
    parser.add_argument("--window", type=int, default=12)
    parser.add_argument(
        "--allow-uncovered",
        action="store_true",
        help="allow the test window to extend beyond the two-sum coverage interval",
    )
    args = parser.parse_args()

    rank = args.rank
    for max_value in range(max(2 * rank + 1, 7), args.max_value + 1):
        universe = range(1, max_value + 1)
        for size in range(rank + 2, min(max_value, args.max_size) + 1):
            for tuple_a in combinations(universe, size):
                elements = set(tuple_a)
                two_sums = hsum(elements, 2, 3 * max_value)
                two_tail = first_tail(
                    two_sums,
                    2,
                    2 * max_value,
                )
                if two_tail is None:
                    continue
                two_end = cover_end(two_sums, two_tail, 3 * max_value)

                cap = 3 * max_value
                three_sums = hsum(elements, 3, cap)
                max_window_end = cap if args.allow_uncovered else two_end
                for start in range(two_tail, max_window_end - rank - 4):
                    end = min(max_window_end, start + args.window)
                    if not covers(three_sums, start, end):
                        continue

                    lower_ok = True
                    for lower_rank in range(1, rank):
                        for deletion in combinations(elements, lower_rank):
                            if not covers(
                                hsum(elements - set(deletion), 3, cap),
                                start,
                                end,
                            ):
                                lower_ok = False
                                break
                        if not lower_ok:
                            break
                    if not lower_ok:
                        continue

                    bad: list[tuple[tuple[int, ...], list[int]]] = []
                    for deletion in combinations(sorted(elements), rank):
                        sums = hsum(elements - set(deletion), 3, cap)
                        holes = [
                            n
                            for n in range(start, end + 1)
                            if n not in sums
                        ]
                        if holes:
                            bad.append((deletion, holes[:4]))

                    if bad:
                        print("finite collective rank window")
                        print(
                            "rank=", rank,
                            "A=", sorted(elements),
                            "2-coverage=", (two_tail, two_end),
                            "window=", (start, end),
                        )
                        print("bad_deletions=", bad[:12])
                        return

    print("no finite rank window found within searched bounds")


if __name__ == "__main__":
    main()
