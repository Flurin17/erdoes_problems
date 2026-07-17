#!/usr/bin/env python3
"""Exhaustively verify the four-defect construction for a finite range."""

from __future__ import annotations

import argparse
import math
from functools import cmp_to_key


def construction(n: int) -> list[tuple[int, int]]:
    m = (n + 4) // 5
    points: list[tuple[int, int]] = []
    for d in range(1, 5):
        for b in range(m * d, min((3 * m - 1) * d, n) + 1):
            if math.gcd(d, b) == 1:
                points.append((b - d, b))
    points.sort(
        key=cmp_to_key(
            lambda p, q: (p[0] * q[1] > q[0] * p[1])
            - (p[0] * q[1] < q[0] * p[1])
        )
    )
    return points


def claimed_count(n: int) -> int:
    return n + 2 * ((n + 1) // 2) - n // 3 - 3 * ((n + 4) // 5)


def verify(n: int) -> None:
    points = construction(n)
    assert len(points) == claimed_count(n), (n, len(points), claimed_count(n))
    for i, (a, b) in enumerate(points):
        assert math.gcd(a, b) == 1 and b <= n
        for c, d in points[i + 1 :]:
            assert a * d < c * b
            assert (a - c) * (b - d) >= 0, (n, (a, b), (c, d))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=500)
    args = parser.parse_args()
    for n in range(16, args.max_n + 1):
        verify(n)
    print(f"verified construction and exact count for 16 <= n <= {args.max_n}")


if __name__ == "__main__":
    main()
