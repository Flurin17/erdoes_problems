#!/usr/bin/env python3
"""Exhaustively verify Lemma 16.54 on small intervals.

If an interval I=[a,b] loses at most r points, then

    [2a + 2r, 2b - 2r] subset 2(I \\ F).

The script checks all deletion sets up to rank r for small translated
intervals.
"""

from __future__ import annotations

from itertools import combinations


def two_sum(values: set[int]) -> set[int]:
    vals = sorted(values)
    sums: set[int] = set()
    for i, x in enumerate(vals):
        for y in vals[i:]:
            sums.add(x + y)
    return sums


def check_interval(a: int, b: int, r: int) -> tuple[int, int]:
    interval = set(range(a, b + 1))
    n = b - a + 1
    if n <= 2 * r:
        return 0, 0

    checked = 0
    band = set(range(2 * a + 2 * r, 2 * b - 2 * r + 1))
    for size in range(r + 1):
        for deleted_tuple in combinations(sorted(interval), size):
            deleted = set(deleted_tuple)
            retained = interval - deleted
            sums = two_sum(retained)
            checked += 1
            if not band <= sums:
                missing = sorted(band - sums)
                raise AssertionError(
                    f"failed: I=[{a},{b}], r={r}, F={sorted(deleted)}, "
                    f"missing={missing[:10]}"
                )
    return checked, len(band)


def main() -> None:
    total_checked = 0
    total_band_points = 0
    cases = [
        (1, 8, 1),
        (1, 12, 2),
        (10, 25, 3),
        (100, 125, 4),
    ]
    for a, b, r in cases:
        checked, band_points = check_interval(a, b, r)
        total_checked += checked
        total_band_points += band_points
        print(
            "case",
            f"I=[{a},{b}]",
            f"r={r}",
            f"checked={checked}",
            f"band_points={band_points}",
        )
    print("interval central two-sum band check passed")
    print("total_checked=", total_checked)
    print("total_band_points=", total_band_points)


if __name__ == "__main__":
    main()
