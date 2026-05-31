#!/usr/bin/env python3
"""Exact arithmetic filters for non-isosceles gamma=2pi/3 templates.

Combines BLZ formulas with the boundary-integrality product formulas recorded
in PROOF.md.  These are necessary arithmetic filters, not construction
certificates.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class Candidate:
    n: int
    template: str
    sides: tuple[int, int, int]
    coefficient: int
    square_parameter: int


def is_square(n: int) -> bool:
    if n < 0:
        return False
    root = isqrt(n)
    return root * root == n


def eisenstein_c(a: int, b: int) -> int | None:
    if gcd(a, b) != 1:
        return None
    c2 = a * a + a * b + b * b
    c = isqrt(c2)
    return c if c * c == c2 else None


def primitive_pairs_for_sum(total: int) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    for a in range(1, total):
        b = total - a
        c = eisenstein_c(a, b)
        if c is not None:
            out.append((a, b, c))
    return out


def primitive_pairs_with_coefficient_bound(bound: int) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    # All product coefficients used below dominate (a+b)^2, so a+b <= sqrt(bound)
    # is enough, except the factor 3 only shrinks the search.
    for total in range(2, isqrt(bound) + 2):
        out.extend(primitive_pairs_for_sum(total))
    return out


def candidates_for_n(n: int) -> list[Candidate]:
    out: list[Candidate] = []

    # BLZ Proposition 24: N=((a+b)/b)m^2.  Since gcd(a+b,b)=1, a+b | N.
    for divisor in range(2, n + 1):
        if n % divisor != 0:
            continue
        for a, b, c in primitive_pairs_for_sum(divisor):
            m2 = n * b // divisor
            if n * b % divisor == 0 and is_square(m2):
                out.append(
                    Candidate(
                        n,
                        "alpha,alpha+beta,alpha+2beta",
                        (a, b, c),
                        divisor,
                        isqrt(m2),
                    )
                )

    for a, b, c in primitive_pairs_with_coefficient_bound(n):
        checks = [
            ("2alpha,2beta,alpha+beta", (a + 2 * b) * (b + 2 * a)),
            ("alpha,2beta,2alpha+beta", (b + 2 * a) * (a + b)),
            ("alpha,2alpha,3beta", 3 * (a + 2 * b) * (a + b)),
        ]
        for template, coefficient in checks:
            if coefficient <= n and n % coefficient == 0 and is_square(n // coefficient):
                out.append(Candidate(n, template, (a, b, c), coefficient, isqrt(n // coefficient)))

    return sorted(out, key=lambda row: (row.template, row.sides, row.coefficient))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    args = parser.parse_args()
    for n in args.n:
        rows = candidates_for_n(n)
        print(f"N={n}: {len(rows)} exact non-isosceles gamma=2pi/3 arithmetic candidate(s)")
        for row in rows:
            print(
                f"  {row.template}: sides={row.sides}, "
                f"coefficient={row.coefficient}, square_parameter={row.square_parameter}"
            )


if __name__ == "__main__":
    main()
