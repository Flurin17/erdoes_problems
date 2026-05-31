#!/usr/bin/env python3
"""Search finite-window collective barriers for the remaining k=2 case.

The remaining k=2 obstruction in the notes is collective: all one-point
deletions may preserve order-3 coverage eventually, while some pairs or
larger finite sets still create order-3 holes. This script searches small
finite windows for that pattern.

Output is only heuristic. A finite window where all singleton deletions
cover the window but some pair deletion has holes does not imply an infinite
counterexample, because the holes may disappear after a larger threshold.
"""

from __future__ import annotations

from itertools import combinations


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def covers_interval(values: set[int], start: int, end: int) -> bool:
    return all(n in values for n in range(start, end + 1))


def main() -> None:
    for max_value in range(8, 26):
        universe = range(1, max_value + 1)
        for size in range(4, min(max_value, 10) + 1):
            for tuple_a in combinations(universe, size):
                elements = set(tuple_a)
                two_sums = hsum(elements, 2, 2 * max_value)

                two_tail = None
                for base in range(2, max_value + 1):
                    if covers_interval(two_sums, base, 2 * max_value):
                        two_tail = base
                        break
                if two_tail is None:
                    continue

                cap = 3 * max_value
                three_sums = hsum(elements, 3, cap)
                for start in range(two_tail, cap - 5):
                    end = min(cap, start + 10)
                    if not covers_interval(three_sums, start, end):
                        continue

                    if any(
                        not covers_interval(hsum(elements - {a}, 3, cap), start, end)
                        for a in elements
                    ):
                        continue

                    bad_pairs: list[tuple[tuple[int, int], list[int]]] = []
                    for x, y in combinations(sorted(elements), 2):
                        pair_sums = hsum(elements - {x, y}, 3, cap)
                        holes = [
                            n
                            for n in range(start, end + 1)
                            if n not in pair_sums
                        ]
                        if holes:
                            bad_pairs.append(((x, y), holes[:4]))

                    if bad_pairs:
                        print("finite collective barrier window")
                        print(
                            "A=", sorted(elements),
                            "2-tail=", two_tail,
                            "window=", (start, end),
                        )
                        print("bad_pairs=", bad_pairs[:8])
                        return

    print("no finite collective barrier found within searched bounds")


if __name__ == "__main__":
    main()
