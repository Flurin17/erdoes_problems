#!/usr/bin/env python3
"""Fast enumerator for recorded sufficient 3alpha+2beta=pi constructions.

The broader `beeson_3alpha2beta_filter.py` solves necessary equations for a
fixed N.  This script goes the other direction for the source-recorded
sufficient subfamilies:

- Beeson Table 7's five explicit small constructions.
- The triquadratic sufficient condition

      N = 2K^2 - M^2,  0 < M < K,  K | M^2.

- The `(2alpha, alpha, 2beta)` sufficient condition recorded in the filter:
  for a rational `s=a/c`, if the primitive reconstructed sides satisfy
  `c | a^2`, then any integer `M` making the area formula integral gives a
  construction.

The output is a positive-certificate enumerator only.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


@dataclass(frozen=True)
class Construction:
    n: int
    source: str
    details: str


def primitive_sides_from_s(s: Fraction) -> tuple[int, int, int]:
    p, q = s.numerator, s.denominator
    a = p * q
    b = q * q - p * p
    c = q * q
    g = gcd(a, gcd(b, c))
    return a // g, b // g, c // g


def table_7() -> list[Construction]:
    return [
        Construction(28, "Beeson Table 7", "triquadratic, M=2, tile=(2,3,4)"),
        Construction(44, "Beeson Table 7", "isosceles-beta, M=6, tile=(2,3,4)"),
        Construction(48, "Beeson Table 7", "isosceles-alpha+beta, M=4, tile=(2,3,4)"),
        Construction(77, "Beeson Table 7", "(2alpha,alpha,2beta), M=5, tile=(2,3,4)"),
        Construction(84, "Beeson Table 7", "isosceles-alpha, M=10, tile=(2,3,4)"),
    ]


def triquadratic(limit_n: int) -> list[Construction]:
    out: list[Construction] = []
    max_k = isqrt((limit_n + 1) // 2) + 2
    for k in range(2, max_k + 1):
        for m in range(1, k):
            if (m * m) % k != 0:
                continue
            n = 2 * k * k - m * m
            if n <= limit_n:
                sides = primitive_sides_from_s(Fraction(m, k))
                out.append(
                    Construction(
                        n,
                        "TriangleTiling3 triquadratic sufficient condition",
                        f"M={m}, K={k}, tile={sides}",
                    )
                )
    return out


def two_alpha_alpha_two_beta(limit_n: int, max_denominator: int) -> list[Construction]:
    out: list[Construction] = []
    for q in range(2, max_denominator + 1):
        for p in range(1, q):
            s = Fraction(p, q)
            sides = primitive_sides_from_s(s)
            a, _b, c = sides
            if (a * a) % c != 0:
                continue
            ratio = Fraction(
                (2 * q * q - p * p) * (3 * q * q - p * p),
                (q - p) * (q - p) * (2 * q + p) * (2 * q + p),
            )
            for m in range(1, isqrt(limit_n) + 1):
                n = ratio * m * m
                if n.denominator == 1 and n.numerator <= limit_n:
                    out.append(
                        Construction(
                            n.numerator,
                            "TriangleTiling3 (2alpha,alpha,2beta) sufficient condition",
                            f"M={m}, s={s}, tile={sides}",
                        )
                    )
    return out


def constructions(limit_n: int, max_denominator: int = 120) -> dict[int, list[Construction]]:
    out: dict[int, list[Construction]] = {}
    for construction in [
        *table_7(),
        *triquadratic(limit_n),
        *two_alpha_alpha_two_beta(limit_n, max_denominator),
    ]:
        if construction.n <= limit_n:
            out.setdefault(construction.n, []).append(construction)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit-n", type=int, default=250)
    parser.add_argument("--max-denominator", type=int, default=120)
    args = parser.parse_args()

    rows = constructions(args.limit_n, args.max_denominator)
    print(
        "recorded sufficient 3alpha+2beta constructions "
        f"<= {args.limit_n}: {len(rows)} counts"
    )
    for n in sorted(rows):
        first = rows[n][0]
        print(f"{n}: {first.source}; {first.details}")


if __name__ == "__main__":
    main()
