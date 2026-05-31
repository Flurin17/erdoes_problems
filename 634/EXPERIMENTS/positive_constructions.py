#!/usr/bin/env python3
"""Exact sanity checks for elementary positive families in Problem 634.

This is not a tiling renderer. It verifies the algebraic coordinate certificates
used in PROOF.md for the primitive families.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import ceil, gcd, isqrt


@dataclass(frozen=True)
class Point:
    x: Fraction
    y: Fraction

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)


def dot(u: Point, v: Point) -> Fraction:
    return u.x * v.x + u.y * v.y


def norm2(u: Point) -> Fraction:
    return dot(u, u)


def assert_sum_two_squares(a: int, b: int) -> None:
    """Verify the coordinate construction for N=a^2+b^2."""
    assert a > 0 and b > 0
    n = a * a + b * b
    A = Point(Fraction(0), Fraction(0))
    B = Point(Fraction(a * a), Fraction(a * b))
    C = Point(Fraction(-b * b), Fraction(a * b))
    D = Point(Fraction(0), Fraction(a * b))

    AB = B - A
    AC = C - A
    BC = C - B
    AD = D - A
    DB = B - D
    DC = C - D

    assert dot(AB, AC) == 0
    assert norm2(AB) == a * a * n
    assert norm2(AC) == b * b * n
    assert norm2(BC) == n * n
    assert norm2(AD) == a * a * b * b
    assert norm2(DB) == a**4
    assert norm2(DC) == b**4


def subdivision_triangle_count(m: int) -> int:
    """Count small triangles in the barycentric subdivision lemma."""
    assert m >= 1
    upward = sum(1 for i in range(m) for j in range(m - i))
    downward = sum(1 for i in range(m - 1) for j in range(m - 1 - i))
    return upward + downward


def eisenstein_triples(limit: int) -> list[tuple[int, int, int, int]]:
    """List primitive c^2=a^2+ab+b^2 triples and Zhang thresholds.

    Returns (a,b,c,M), where M=3*ceil((c^2-a-b)/(ab)).
    """
    out: list[tuple[int, int, int, int]] = []
    for a in range(1, limit + 1):
        for b in range(1, a + 1):
            if gcd(a, b) != 1:
                continue
            c2 = a * a + a * b + b * b
            c = isqrt(c2)
            if c * c == c2:
                M = 3 * ceil((c2 - a - b) / (a * b))
                out.append((a, b, c, M))
    return out


def main() -> None:
    for m in range(1, 12):
        assert subdivision_triangle_count(m) == m * m

    for a in range(1, 12):
        for b in range(1, 12):
            assert_sum_two_squares(a, b)

    triples = eisenstein_triples(80)
    assert (5, 3, 7, 9) in triples or (3, 5, 7, 9) in triples
    print("subdivision counts OK for m <= 11")
    print("sum-of-two-squares certificates OK for a,b <= 11")
    print("first primitive Zhang triples (a,b,c,M):")
    for row in triples[:12]:
        a, b, c, M = row
        print(f"  {row}; first N = {M*M*a*b}")


if __name__ == "__main__":
    main()
