#!/usr/bin/env python3
"""Arithmetic candidates for equilateral outer-triangle tilings.

The Laczkovich/Beeson reductions include equilateral outer triangles with a
tile angle pi/3 or 2pi/3.  If the primitive tile sides are integers and the
distinguished angle lies between sides a and b, then the tile area is

    sqrt(3) * a*b / 4.

For an equilateral outer triangle of side L and tile count N, the area equation
is therefore

    L^2 = N*a*b.

This is only a necessary arithmetic/boundary-length filter.  It is not a tiling
certificate: the boundary decompositions and interior geometry still have to be
realized.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class Candidate:
    n: int
    angle: str
    sides: tuple[int, int, int]
    outer_side: int
    boundary_decompositions: tuple[tuple[int, int, int], ...]


def side_representations(length: int, sides: tuple[int, int, int], limit: int = 12) -> tuple[tuple[int, int, int], ...]:
    a, b, c = sides
    out: list[tuple[int, int, int]] = []
    for ca in range(length // a + 1):
        rest_a = length - ca * a
        for cb in range(rest_a // b + 1):
            rest = rest_a - cb * b
            if rest % c == 0:
                out.append((ca, cb, rest // c))
                if len(out) >= limit:
                    return tuple(out)
    return tuple(out)


def candidates_for_n(n: int, side_bound: int = 250) -> list[Candidate]:
    out: list[Candidate] = []
    seen: set[tuple[str, tuple[int, int, int], int]] = set()
    for angle, sign in (("2pi/3", 1), ("pi/3", -1)):
        for a in range(1, side_bound + 1):
            for b in range(1, side_bound + 1):
                if gcd(a, b) != 1:
                    continue
                c2 = a * a + sign * a * b + b * b
                c = isqrt(c2)
                if c * c != c2:
                    continue
                if gcd(c, gcd(a, b)) != 1:
                    continue
                outer2 = n * a * b
                outer = isqrt(outer2)
                if outer * outer != outer2:
                    continue
                sides = (a, b, c)
                key = (angle, sides, outer)
                if key in seen:
                    continue
                reps = side_representations(outer, sides)
                if not reps:
                    continue
                seen.add(key)
                out.append(Candidate(n, angle, sides, outer, reps))
    return sorted(out, key=lambda row: (row.angle, row.outer_side, row.sides))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--side-bound", type=int, default=250)
    args = parser.parse_args()

    for n in args.n:
        rows = candidates_for_n(n, args.side_bound)
        print(
            f"N={n}: {len(rows)} equilateral area candidate(s) "
            f"with primitive side entries <= {args.side_bound}"
        )
        for row in rows:
            decomps = ", ".join(
                f"{ca}a+{cb}b+{cc}c" for ca, cb, cc in row.boundary_decompositions[:4]
            )
            suffix = " ..." if len(row.boundary_decompositions) > 4 else ""
            print(
                f"  angle={row.angle:5s} sides={row.sides} "
                f"outer_side={row.outer_side} boundary={decomps}{suffix}"
            )


if __name__ == "__main__":
    main()
