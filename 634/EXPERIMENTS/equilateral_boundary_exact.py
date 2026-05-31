#!/usr/bin/env python3
"""Exact boundary-length arithmetic for equilateral outer triangles.

For an equilateral outer triangle tiled by `N` congruent triangles, each outer
side is a sum of full tile side lengths.  If the tile has a distinguished
`pi/3` or `2pi/3` angle between sides `a,b`, primitive integer sides satisfy

    c^2 = a^2 - a*b + b^2      for pi/3,
    c^2 = a^2 + a*b + b^2      for 2pi/3,
    L^2 = N*a*b                for the equilateral outer side L.

On one side, write

    L = x*a + y*b + z*c,       x+y+z <= N.

For fixed `(N,x,y,z)`, eliminating `L` and `c` gives a polynomial in
`r = a/b`.  This script solves those rational equations exactly and then checks
the original integer equations.  It replaces side-bounded brute force for these
equilateral arithmetic candidates.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt


Poly = list[int]


@dataclass(frozen=True)
class Candidate:
    n: int
    angle: str
    sides: tuple[int, int, int]
    outer_side: int
    decompositions: tuple[tuple[int, int, int], ...]


def trim(poly: Poly) -> Poly:
    out = poly[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return trim(
        [
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(size)
        ]
    )


def scale(factor: int, poly: Poly) -> Poly:
    return trim([factor * value for value in poly])


def sub(left: Poly, right: Poly) -> Poly:
    return add(left, scale(-1, right))


def mul(left: Poly, right: Poly) -> Poly:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out)


def eval_poly(poly: Poly, value: Fraction) -> Fraction:
    total = Fraction(0)
    power = Fraction(1)
    for coefficient in poly:
        total += coefficient * power
        power *= value
    return total


@lru_cache(maxsize=None)
def divisors(n: int) -> tuple[int, ...]:
    n = abs(n)
    if n == 0:
        return (0,)
    out: list[int] = []
    for divisor in range(1, isqrt(n) + 1):
        if n % divisor == 0:
            out.append(divisor)
            if divisor * divisor != n:
                out.append(n // divisor)
    return tuple(sorted(out))


@lru_cache(maxsize=None)
def rational_roots_cached(poly_tuple: tuple[int, ...]) -> tuple[Fraction, ...]:
    poly = trim(list(poly_tuple))
    while len(poly) > 1 and poly[0] == 0:
        poly = poly[1:]
    if len(poly) == 1:
        return ()
    if len(poly) == 2:
        c0, c1 = poly
        if c1 == 0:
            return ()
        return (Fraction(-c0, c1),)
    c0 = poly[0]
    lead = poly[-1]
    roots: set[Fraction] = set()
    for numerator in divisors(c0):
        for denominator in divisors(lead):
            if denominator == 0:
                continue
            for sign in (-1, 1):
                root = Fraction(sign * numerator, denominator)
                if eval_poly(poly, root) == 0:
                    roots.add(root)
    return tuple(sorted(roots))


def rational_roots(poly: Poly) -> tuple[Fraction, ...]:
    return rational_roots_cached(tuple(trim(poly)))


def boundary_poly(n: int, sign: int, x: int, y: int, z: int) -> Poly:
    """Return polynomial in r=a/b for L=x*a+y*b+z*c.

    `sign` is +1 for `2pi/3` and -1 for `pi/3`.
    """
    if z == 0:
        # (x*r+y)^2 = n*r
        return [y * y, 2 * x * y - n, x * x]

    a_poly = [y, x]  # x*r+y
    c2_poly = [1, sign, 1]  # r^2 + sign*r + 1, increasing order
    # B = n*r - (x*r+y)^2 - z^2*(r^2+sign*r+1)
    b_poly = sub(
        [0, n],
        add(mul(a_poly, a_poly), scale(z * z, c2_poly)),
    )
    return sub(mul(b_poly, b_poly), scale(4 * z * z, mul(mul(a_poly, a_poly), c2_poly)))


def valid_candidate(n: int, sign: int, ratio: Fraction, decomposition: tuple[int, int, int]) -> tuple[int, int, int, int] | None:
    if ratio <= 0:
        return None
    a = ratio.numerator
    b = ratio.denominator
    c2 = a * a + sign * a * b + b * b
    c = isqrt(c2)
    if c * c != c2:
        return None
    if gcd(a, gcd(b, c)) != 1:
        return None
    outer2 = n * a * b
    outer = isqrt(outer2)
    if outer * outer != outer2:
        return None
    x, y, z = decomposition
    if x * a + y * b + z * c != outer:
        return None
    return a, b, c, outer


def candidates_for_n(n: int, max_side_edges: int | None = None) -> list[Candidate]:
    max_edges = n if max_side_edges is None else max_side_edges
    by_key: dict[tuple[str, tuple[int, int, int], int], set[tuple[int, int, int]]] = {}

    for angle, sign in (("2pi/3", 1), ("pi/3", -1)):
        for x in range(max_edges + 1):
            for y in range(max_edges + 1 - x):
                for z in range(max_edges + 1 - x - y):
                    if x + y + z == 0:
                        continue
                    poly = boundary_poly(n, sign, x, y, z)
                    for ratio in rational_roots(poly):
                        row = valid_candidate(n, sign, ratio, (x, y, z))
                        if row is None:
                            continue
                        a, b, c, outer = row
                        key = (angle, (a, b, c), outer)
                        by_key.setdefault(key, set()).add((x, y, z))

    out = [
        Candidate(n, angle, sides, outer, tuple(sorted(decompositions)))
        for (angle, sides, outer), decompositions in by_key.items()
    ]
    return sorted(out, key=lambda row: (row.angle, row.outer_side, row.sides))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument(
        "--max-side-edges",
        type=int,
        default=None,
        help="maximum number of tile sides used on one outer side; default N",
    )
    args = parser.parse_args()

    for n in args.n:
        rows = candidates_for_n(n, args.max_side_edges)
        max_edges = n if args.max_side_edges is None else args.max_side_edges
        print(f"N={n}: {len(rows)} exact equilateral boundary-length candidate(s), side-edge cap {max_edges}")
        for row in rows:
            decomps = ", ".join(
                f"{x}a+{y}b+{z}c" for x, y, z in row.decompositions[:6]
            )
            suffix = " ..." if len(row.decompositions) > 6 else ""
            print(
                f"  angle={row.angle:5s} sides={row.sides} "
                f"L={row.outer_side} boundary={decomps}{suffix}"
            )


if __name__ == "__main__":
    main()
