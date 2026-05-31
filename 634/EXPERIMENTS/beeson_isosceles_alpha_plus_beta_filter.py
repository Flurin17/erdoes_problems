#!/usr/bin/env python3
"""Beeson filter for 3alpha+2beta=pi, isosceles base angles alpha+beta.

Source: Beeson, "Triangle tiling: the case 3 alpha + 2 beta = pi",
Section 11.4, Figures 25 and 26.

This implements the SageMath filter printed in the paper. It is stronger than
the bare tiling equation

    N/M^2 = (1+s)/(1-s)

and checks:

- primitive integral tile sides (a,b,c);
- c = gcd(a,c)^2;
- g*mu integral, where g=gcd(a,c) and mu=M(1+s);
- N*b*c square;
- Lemma 46's squarefree-b implication;
- boundary decompositions after reserving two c edges on each side.

Passing this filter is still only necessary. Failing it is a source-backed
obstruction for this specific template.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


@dataclass(frozen=True)
class Candidate:
    n: int
    M: int
    mu: Fraction
    sides: tuple[int, int, int]
    equal_side: int
    base: int


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_squarefree(n: int) -> bool:
    n = abs(n)
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return False
        d += 1
    return True


def fraction_text(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def primitive_tile(n: int, M: int) -> tuple[int, int, int]:
    """Return primitive integer sides from s=(N-M^2)/(N+M^2)."""
    a = n - M * M
    c = n + M * M
    # b/c = 1-s^2, so b = c - a^2/c. If needed, scale by c.
    if (a * a) % c != 0:
        old_c = c
        a = a * old_c
        c = old_c * old_c
    b = c - (a * a) // c
    g = gcd(a, gcd(b, c))
    return (a // g, b // g, c // g)


def integer_value(x: Fraction) -> int | None:
    if x.denominator != 1:
        return None
    return x.numerator


def check_edges(x: int, a: int, b: int, c: int) -> bool:
    """Can x=pa+qb+rc with q>0 and q divisible by g=gcd(a,c)?"""
    if x < 0:
        return False
    g = gcd(a, c)
    for p in range(0, x // a + 1):
        rem1 = x - p * a
        for q in range(g, rem1 // b + 1, g):
            rem2 = rem1 - q * b
            if rem2 >= 0 and rem2 % c == 0:
                return True
    return False


def edge_count_triples(x: int, a: int, b: int, c: int) -> list[tuple[int, int, int]]:
    """Return full side-count triples after the two reserved `c` edges.

    A triple `(p,q,r)` represents `x = p*a + q*b + r*c`, with the congruence
    and positivity conditions from Beeson's equal-side check.
    """
    if x < 0:
        return []
    out: list[tuple[int, int, int]] = []
    g = gcd(a, c)
    for p in range(0, x // a + 1):
        rem1 = x - p * a
        for q in range(g, rem1 // b + 1, g):
            rem2 = rem1 - q * b
            if rem2 >= 2 * c and rem2 % c == 0:
                out.append((p, q, rem2 // c))
    return out


def check_base(y: int, a: int, b: int, c: int, M: int) -> bool:
    """Can y=pa+qb+rc with q congruent to -M mod g?"""
    if y < 0:
        return False
    g = gcd(a, c)
    start = (int(M / g) * g) - M
    if start < 0:
        start += g
    for p in range(0, y // a + 1):
        rem1 = y - p * a
        for q in range(start, rem1 // b + 1, g):
            rem2 = rem1 - q * b
            if rem2 >= 0 and rem2 % c == 0:
                return True
    return False


def base_count_triples(x: int, a: int, b: int, c: int, M: int) -> list[tuple[int, int, int]]:
    """Return full base-count triples after the two reserved `c` edges."""
    if x < 0:
        return []
    out: list[tuple[int, int, int]] = []
    g = gcd(a, c)
    start = (-M) % g
    for p in range(0, x // a + 1):
        rem1 = x - p * a
        for q in range(start, rem1 // b + 1, g):
            rem2 = rem1 - q * b
            if rem2 >= 2 * c and rem2 % c == 0:
                out.append((p, q, rem2 // c))
    return out


def candidates_for_n(n: int) -> list[Candidate]:
    out: list[Candidate] = []
    # Beeson loops over M with M^2 < N.
    for M in range(1, isqrt(n) + 1):
        if M * M >= n:
            continue
        a, b, c = primitive_tile(n, M)
        s = Fraction(a, c)
        g = gcd(a, c)
        if c != g * g:
            continue
        mu = Fraction(M) * (1 + s)
        if integer_value(mu * g) is None:
            continue
        if not is_square(n * b * c):
            continue
        if is_squarefree(b) and gcd(c - a, b) == 1 and integer_value(mu) is None:
            continue
        X = integer_value(mu * c)
        Y = integer_value(mu * a)
        if X is None or Y is None:
            continue
        if check_edges(X - 2 * c, a, b, c) and check_base(Y - 2 * c, a, b, c, M):
            out.append(Candidate(n, M, mu, (a, b, c), X, Y))
    return out


def candidate_dict(c: Candidate) -> dict[str, object]:
    return {
        "n": c.n,
        "M": c.M,
        "mu": fraction_text(c.mu),
        "template": "3alpha+2beta=pi, isosceles base angles alpha+beta",
        "primitive_tile_sides": c.sides,
        "outer_equal_side_X": c.equal_side,
        "outer_base_Y": c.base,
        "source_status": "necessary filter survivor, not necessarily a tiling",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="*", type=int)
    parser.add_argument("--range", dest="range_", nargs=2, type=int, metavar=("LO", "HI"))
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "--counts",
        action="store_true",
        help="print Beeson side-count triples for surviving candidates",
    )
    args = parser.parse_args()

    ns = args.n
    if args.range_:
        lo, hi = args.range_
        ns.extend(range(lo, hi + 1))
    if not ns:
        ns = list(range(1, 109))

    rows = [(n, candidates_for_n(n)) for n in ns]
    if args.json:
        print(json.dumps({str(n): [candidate_dict(c) for c in cs] for n, cs in rows}, indent=2))
        return

    for n, cs in rows:
        print(f"N={n}: {len(cs)} candidate(s)")
        for c in cs:
            print(
                f"  M={c.M} mu={fraction_text(c.mu)}"
                f" sides={c.sides} X={c.equal_side} Y={c.base}"
            )
            if args.counts:
                a, b, side_c = c.sides
                edges = edge_count_triples(c.equal_side, a, b, side_c)
                base = base_count_triples(c.base, a, b, side_c, c.M)
                print(f"    equal-side count triples (p,q,r): {edges}")
                print(f"    base count triples (p,q,r): {base}")


if __name__ == "__main__":
    main()
