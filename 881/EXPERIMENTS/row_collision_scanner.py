#!/usr/bin/env python3
"""Scan row-bank collisions for singleton-high-excess witnesses.

For a singleton witness w=b+d and C=A\\{b}, Lemma 16.9 forces rows
d-p in 2A for retained padders p.  If both

    d-p in 2C
    b+p in 2C

hold for the same p, then w=(d-p)+(b+p) lies in 4C and the witness is
repaired.  Viable row banks must avoid these collisions, or ensure the
row d-p is b-dependent.
"""

from __future__ import annotations


def two_sum_witnesses(elements: set[int]) -> dict[int, list[tuple[int, int]]]:
    ordered = sorted(elements)
    out: dict[int, list[tuple[int, int]]] = {}
    for i, x in enumerate(ordered):
        for y in ordered[i:]:
            out.setdefault(x + y, []).append((x, y))
    return out


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def cover_end(values: set[int], start: int, cap: int) -> int:
    x = start
    while x <= cap and x in values:
        x += 1
    return x - 1


def scan(A: set[int], b: int, d: int) -> None:
    C = A - {b}
    w = b + d
    two_a = two_sum_witnesses(A)
    two_c = two_sum_witnesses(C)
    four_c = hsum(C, 4, max(4 * max(A), w) + 20)
    rows = {}
    collisions = {}
    b_dependent = {}
    reflected = {}
    unique_gate = {}
    for p in sorted(C):
        row_target = d - p
        if row_target in two_a:
            rows[p] = two_a[row_target]
            if row_target in two_c and b + p in two_c:
                collisions[p] = {
                    "row": two_c[row_target],
                    "shift": two_c[b + p],
                }
            if row_target not in two_c:
                b_dependent[p] = two_a[row_target]
                reflected[p] = d - b - p
        if b + p not in two_c:
            unique_gate[p] = b + p
    print("A=", sorted(A))
    print("b=", b, "d=", d, "w=", w)
    print("3A coverage from 3=", cover_end(hsum(A, 3, 6 * max(A) + 100), 3, 6 * max(A) + 100))
    print("w in 4(A\\{b})=", w in four_c)
    print("row count=", len(rows), "expected=", len(C))
    print("b-dependent rows=", b_dependent)
    print("one-term reflected rows d-b-p=", reflected)
    print("unique gate translates b+p notin 2C=", unique_gate)
    print("collisions=", collisions)


def main() -> None:
    prepared = {1, 2, 3, 4, 8, 19, 20, 28, 33}
    scan(prepared, b=33, d=40)


if __name__ == "__main__":
    main()
