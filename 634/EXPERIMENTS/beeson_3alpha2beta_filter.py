#!/usr/bin/env python3
"""Necessary-equation filter for Beeson/Laczkovich 3a+2b=pi cases.

Beeson's paper "Triangle tiling: the case 3 alpha + 2 beta = pi" ends with a
table of necessary equations for the five possible outer-triangle shapes. This
script solves those equations over rational s=a/c for a requested tile count N.

It is only a filter:

- no rational solution means that shape is impossible in this angle template;
- a rational solution is only a candidate unless the source gives a matching
  sufficient condition.

The side ratios are reconstructed from

    a/c = s,          b/c = 1 - s^2.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


Poly = list[int]  # coefficients in increasing degree order


@dataclass(frozen=True)
class Candidate:
    n: int
    m: int
    case: str
    s: Fraction
    sides: tuple[int, int, int]
    sufficient: bool
    note: str


def trim(poly: Poly) -> Poly:
    out = poly[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(a: Poly, b: Poly) -> Poly:
    size = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(size)])


def scale(c: int, p: Poly) -> Poly:
    return trim([c * x for x in p])


def sub(a: Poly, b: Poly) -> Poly:
    return add(a, scale(-1, b))


def mul(a: Poly, b: Poly) -> Poly:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return trim(out)


def eval_poly(poly: Poly, x: Fraction) -> Fraction:
    total = Fraction(0)
    power = Fraction(1)
    for coeff in poly:
        total += coeff * power
        power *= x
    return total


def divisors(n: int) -> list[int]:
    n = abs(n)
    if n == 0:
        return [0]
    out: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def rational_roots(poly: Poly) -> list[Fraction]:
    poly = trim(poly)
    if len(poly) == 1:
        return []
    if len(poly) == 2:
        c0, c1 = poly
        if c1 == 0:
            return []
        return [Fraction(-c0, c1)]
    c0 = poly[0]
    lead = poly[-1]
    roots: set[Fraction] = set()
    if c0 == 0:
        roots.add(Fraction(0))
        reduced = poly[1:]
        roots.update(rational_roots(reduced))
        return sorted(roots)
    for p in divisors(c0):
        for q in divisors(lead):
            if q == 0:
                continue
            for sign in (-1, 1):
                x = Fraction(sign * p, q)
                if eval_poly(poly, x) == 0:
                    roots.add(x)
    return sorted(roots)


def primitive_sides(s: Fraction) -> tuple[int, int, int]:
    """Return primitive integer sides for a/c=s and b/c=1-s^2."""
    p, q = s.numerator, s.denominator
    a = p * q
    b = q * q - p * p
    c = q * q
    g = gcd(a, gcd(b, c))
    return (a // g, b // g, c // g)


def is_valid_s(s: Fraction) -> bool:
    return Fraction(0) < s < Fraction(1)


def equation_poly(case: str, n: int, m: int) -> Poly:
    """Return integer polynomial whose rational roots are candidate s values."""
    one_minus_s = [1, -1]
    one_plus_s = [1, 1]
    two_plus_s = [2, 1]
    two_minus_s2 = [2, 0, -1]
    three_minus_s2 = [3, 0, -1]

    if case == "triquadratic":
        # N/M^2 = 2/s^2 - 1, with s=a/c=M/K.
        # The table text extracted from the PDF is ambiguous here, but the
        # surrounding theorem N+M^2=2K^2 and s=M/K fixes this reciprocal form.
        return [-2 * m * m, 0, n + m * m]
    if case == "2a_a_2b":
        # N/M^2 = (2-s^2)(3-s^2)/((1-s)^2(2+s)^2)
        return sub(
            scale(n, mul(mul(one_minus_s, one_minus_s), mul(two_plus_s, two_plus_s))),
            scale(m * m, mul(two_minus_s2, three_minus_s2)),
        )
    if case == "isosceles_beta":
        # N/M^2 = (3-s^2)/(1+s)^2
        return sub(scale(n, mul(one_plus_s, one_plus_s)), scale(m * m, three_minus_s2))
    if case == "isosceles_alpha_plus_beta":
        # N/M^2 = (1+s)/(1-s)
        return sub(scale(n, one_minus_s), scale(m * m, one_plus_s))
    if case == "isosceles_alpha":
        # N/M^2 = (1+s)(2-s^2)/((1-s)(2+s)^2)
        return sub(
            scale(n, mul(one_minus_s, mul(two_plus_s, two_plus_s))),
            scale(m * m, mul(one_plus_s, two_minus_s2)),
        )
    raise ValueError(case)


def sufficient(case: str, n: int, m: int, s: Fraction, sides: tuple[int, int, int]) -> tuple[bool, str]:
    known_table_7 = {
        ("triquadratic", 28, 2, (2, 3, 4)),
        ("isosceles_beta", 44, 6, (2, 3, 4)),
        ("isosceles_alpha_plus_beta", 48, 4, (2, 3, 4)),
        ("2a_a_2b", 77, 5, (2, 3, 4)),
        ("isosceles_alpha", 84, 10, (2, 3, 4)),
    }
    if (case, n, m, sides) in known_table_7:
        return True, "source Table 7 lists an explicit tiling for this candidate"
    if case == "triquadratic":
        k = Fraction(m, 1) / s
        if k.denominator == 1 and k.numerator > 0 and (m * m) % k.numerator == 0:
            return True, f"source sufficient condition: s=M/K with K={k.numerator} and K|M^2"
        return False, "necessary equation only; triquadratic K|M^2 failed"
    if case == "2a_a_2b":
        a, _b, c = sides
        if (a * a) % c == 0:
            return True, "source sufficient condition: c|a^2"
        return False, "necessary equation only; c|a^2 failed"
    if case == "isosceles_beta":
        a, _b, c = sides
        g = gcd(a, c)
        if m % g == 0:
            return False, "necessary condition g|M holds; source table has no full sufficiency here"
        return False, "necessary equation root but g|M failed"
    if case in {"isosceles_alpha_plus_beta", "isosceles_alpha"}:
        return False, "necessary equation only; source table records no full sufficiency"
    return False, ""


CASES = [
    ("triquadratic", "(2a,b,a+b)"),
    ("2a_a_2b", "(2a,a,2b)"),
    ("isosceles_beta", "(b,b,3a)"),
    ("isosceles_alpha_plus_beta", "(a+b,a+b,a)"),
    ("isosceles_alpha", "(a,a,a+2b)"),
]


def fraction_text(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def candidate_dict(c: Candidate) -> dict[str, object]:
    internal_case = next(k for k, label in CASES if label == c.case)
    poly = equation_poly(internal_case, c.n, c.m)
    return {
        "n": c.n,
        "M": c.m,
        "template": "3alpha+2beta=pi",
        "outer_triangle_case": c.case,
        "s=a_over_c": fraction_text(c.s),
        "primitive_tile_sides": c.sides,
        "necessary_polynomial_coefficients_in_increasing_degree": poly,
        "sufficient_by_recorded_source_condition": c.sufficient,
        "note": c.note,
    }


def candidates_for_n(n: int) -> list[Candidate]:
    out: list[Candidate] = []
    # Coloring number M is strictly smaller than N in the source computations.
    for m in range(1, n):
        for case, label in CASES:
            for s in rational_roots(equation_poly(case, n, m)):
                if not is_valid_s(s):
                    continue
                sides = primitive_sides(s)
                ok, note = sufficient(case, n, m, s, sides)
                out.append(Candidate(n, m, label, s, sides, ok, note))
    return sorted(out, key=lambda c: (c.n, c.case, c.m, c.s))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="*", type=int, help="tile counts to filter")
    parser.add_argument("--range", dest="range_", nargs=2, type=int, metavar=("LO", "HI"))
    parser.add_argument("--json", action="store_true", help="emit machine-readable candidate records")
    args = parser.parse_args()

    ns = args.n
    if args.range_:
        lo, hi = args.range_
        ns.extend(range(lo, hi + 1))
    if not ns:
        ns = [7, 11, 19, 28, 44, 48, 77, 84]

    all_candidates = [(n, candidates_for_n(n)) for n in ns]
    if args.json:
        print(json.dumps({str(n): [candidate_dict(c) for c in cs] for n, cs in all_candidates}, indent=2))
        return

    for n, cs in all_candidates:
        print(f"N={n}: {len(cs)} rational candidates")
        for c in cs:
            marker = "sufficient" if c.sufficient else "necessary"
            print(
                f"  M={c.m:3d} case={c.case:18s} s={c.s}"
                f" sides={c.sides} [{marker}] {c.note}"
            )


if __name__ == "__main__":
    main()
