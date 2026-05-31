#!/usr/bin/env python3
"""Finite search for fixed-center star pair obstructions.

This is a diagnostic for Warning 8.2b in PROOF.md. It looks for a finite
order-2 window where a fixed retained center e and an old deleted element d
make several later candidates b fail the pair repair

    e + d + b in 3(A \\ {d,b}).

The output is not an infinite construction; it only shows that the
fixed-prefix star obstruction occurs in genuine finite sum windows.
"""

from __future__ import annotations

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


def search(max_value: int = 22, max_size: int = 10, min_spokes: int = 3) -> None:
    for candidate_max in range(8, max_value + 1):
        for size in range(5, min(candidate_max, max_size) + 1):
            for tuple_a in combinations(range(1, candidate_max + 1), size):
                elements = set(tuple_a)
                coverage = cover_end(elements, 2, 3 * candidate_max)
                if coverage < candidate_max:
                    continue
                for e, d in combinations(sorted(elements), 2):
                    spokes: list[tuple[int, int]] = []
                    for b in sorted(x for x in elements if x > d and x != e):
                        witness = e + d + b
                        if witness > coverage:
                            continue
                        if witness in hsum(elements - {d, b}, 3, witness):
                            continue
                        if witness not in hsum(elements - {b}, 3, witness):
                            continue
                        if witness not in hsum(elements - {d}, 3, witness):
                            continue
                        spokes.append((b, witness))
                    if len(spokes) >= min_spokes:
                        print("finite fixed-center star obstruction")
                        print("A=", sorted(elements), "coverage_end=", coverage)
                        print("center e=", e, "old d=", d)
                        print("bad spokes=", spokes)
                        return
    print("no fixed-center star obstruction found within searched bounds")


def prefix_star_example() -> None:
    elements = {1, 2, 3, 4, 5, 6, 7}
    e = 1
    deleted_prefix = {4, 6}
    d = 6
    b = 7
    witness = e + d + b
    retained = elements - deleted_prefix - {b}
    print("finite prefix star not descending to a pair hole")
    print("A=", sorted(elements), "e=", e, "D=", sorted(deleted_prefix))
    print("d=", d, "b=", b, "w=", witness)
    print("e+b in 2C:", e + b in hsum(retained, 2, witness))
    print("e+2b in 3C:", e + 2 * b in hsum(retained, 3, e + 2 * b))
    print("w in 3C:", witness in hsum(retained, 3, witness))
    print("w in 3(A\\{d,b}):", witness in hsum(elements - {d, b}, 3, witness))
    print("w in 3(A\\{4,b}):", witness in hsum(elements - {4, b}, 3, witness))
    print("w in 3(A\\{4,d}):", witness in hsum(elements - {4, d}, 3, witness))


if __name__ == "__main__":
    search()
    prefix_star_example()
