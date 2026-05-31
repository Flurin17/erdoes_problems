#!/usr/bin/env python3
"""Beeson filter for isosceles ABC tiled by a gamma=2pi/3 tile.

Source: Beeson, "Tilings of an isosceles triangle", Section 12.

For an isosceles outer triangle ABC with base angles alpha, tiled by a rational
tile with angles (alpha,beta,2pi/3) and integer sides (a,b,c), Beeson proves:

    c^2 = a^2 + ab + b^2
    2b + a divides N
    N b / (2b + a) is a square, say m^2
    outer equal side X = m c
    outer base Y = m(2b+a)

Theorem 12.10 uses this to compute all candidates for N <= 200 and finds none
for N < 33. This script reproduces that exact arithmetic filter.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class Candidate:
    n: int
    sides: tuple[int, int, int]
    m: int
    outer_equal_side: int
    outer_base: int


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def candidates_for_n(n: int) -> list[Candidate]:
    out: list[Candidate] = []
    # From 2b+a | N, both a and b are at most N.
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if gcd(a, b) != 1:
                continue
            d = 2 * b + a
            if n % d != 0:
                continue
            c2 = a * a + a * b + b * b
            c = isqrt(c2)
            if c * c != c2:
                continue
            if gcd(a, gcd(b, c)) != 1:
                continue
            m2 = n * b // d
            if not is_square(m2):
                continue
            m = isqrt(m2)
            out.append(Candidate(n, (a, b, c), m, m * c, m * d))
    return sorted(out, key=lambda c: (c.n, c.sides, c.m))


def prime_candidates(limit: int, residue_mod_4: int = 3) -> list[Candidate]:
    """Fast exact scan of prime N in the isosceles gamma=2pi/3 filter.

    For prime N=p, the divisor condition forces 2b+a=p and then b=m^2.
    """
    out: list[Candidate] = []
    for p in range(2, limit + 1):
        if not is_prime(p) or p % 4 != residue_mod_4:
            continue
        for m in range(1, isqrt((p - 1) // 2) + 1):
            b = m * m
            a = p - 2 * b
            if a <= 0 or gcd(a, b) != 1:
                continue
            c2 = a * a + a * b + b * b
            c = isqrt(c2)
            if c * c != c2:
                continue
            out.append(Candidate(p, (a, b, c), m, m * c, m * p))
    return out


def candidate_dict(c: Candidate) -> dict[str, object]:
    return {
        "n": c.n,
        "template": "isosceles ABC, tile angles (alpha,beta,2pi/3)",
        "primitive_tile_sides": c.sides,
        "m": c.m,
        "outer_equal_side_X": c.outer_equal_side,
        "outer_base_Y": c.outer_base,
        "source_status": "necessary arithmetic candidate, not necessarily a tiling",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="*", type=int)
    parser.add_argument("--range", dest="range_", nargs=2, type=int, metavar=("LO", "HI"))
    parser.add_argument("--prime-scan", type=int, metavar="LIMIT")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.prime_scan is not None:
        rows = prime_candidates(args.prime_scan)
        if args.json:
            print(json.dumps([candidate_dict(c) for c in rows], indent=2))
            return
        print(f"prime N == 3 mod 4 candidates up to {args.prime_scan}: {len(rows)}")
        for c in rows:
            print(f"  N={c.n}: sides={c.sides} m={c.m} X={c.outer_equal_side} Y={c.outer_base}")
        return

    ns = args.n
    if args.range_:
        lo, hi = args.range_
        ns.extend(range(lo, hi + 1))
    if not ns:
        ns = list(range(1, 201))

    rows = [(n, candidates_for_n(n)) for n in ns]
    if args.json:
        print(json.dumps({str(n): [candidate_dict(c) for c in cs] for n, cs in rows}, indent=2))
        return

    for n, cs in rows:
        print(f"N={n}: {len(cs)} candidate(s)")
        for c in cs:
            print(f"  sides={c.sides} m={c.m} X={c.outer_equal_side} Y={c.outer_base}")


if __name__ == "__main__":
    main()
