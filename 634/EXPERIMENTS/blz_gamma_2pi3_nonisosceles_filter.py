#!/usr/bin/env python3
"""BLZ square-class filters for non-isosceles gamma=2pi/3 templates.

Source: Beeson-Laczkovich-Zhang, "Solution of Erdos Problem 633",
Propositions 24, 26, 28, and 31.

The formulas here are necessary conditions for the relevant template.  They do
not constitute a complete search for arbitrary tilings unless the source theorem
states a prime obstruction.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt


@dataclass(frozen=True)
class Tile:
    a: int
    b: int
    c: int


@dataclass(frozen=True)
class Candidate:
    n: int
    template: str
    tile: Tile
    coefficient: Fraction


@dataclass(frozen=True)
class Witness:
    template: str
    squareclass: str
    tile: Tile
    A: int
    S: int
    c_quartic: int
    q: Fraction
    coefficient: Fraction


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_rational_square(x: Fraction) -> bool:
    return x > 0 and is_square(x.numerator) and is_square(x.denominator)


def gcd_many(values: tuple[int, ...]) -> int:
    out = 0
    for value in values:
        out = gcd(out, value)
    return out


@lru_cache(maxsize=None)
def primitive_eisenstein_triples(limit_side: int) -> tuple[Tile, ...]:
    """Primitive integer side triples with c^2 = a^2 + ab + b^2.

    The order of a and b matters because they face alpha and beta respectively.
    """
    out: set[Tile] = set()
    # Euclid parametrization for primitive 120-degree integer triangles.
    # For m > n > 0,
    #   a=m^2-n^2, b=2mn+n^2, c=m^2+mn+n^2.
    for m in range(2, isqrt(limit_side) + 2):
        for n in range(1, m):
            c = m * m + m * n + n * n
            if c > limit_side:
                continue
            a = m * m - n * n
            b = 2 * m * n + n * n
            if gcd(a, b) != 1:
                continue
            out.add(Tile(a, b, c))
            out.add(Tile(b, a, c))
    return tuple(sorted(out, key=lambda tile: (tile.c, tile.a, tile.b)))


def coefficient_alpha_2alpha_3beta(tile: Tile) -> Fraction:
    """BLZ Proposition 26 square class for T=(alpha,2alpha,3beta)."""
    return Fraction(tile.a + 2 * tile.b, 3 * (tile.a + tile.b))


def coefficient_alpha_2beta_2alpha_beta(tile: Tile) -> Fraction:
    """BLZ Proposition 28 square class for T=(alpha,2beta,2alpha+beta)."""
    return Fraction(tile.b + 2 * tile.a, tile.a + tile.b)


def candidates_for_n(n: int, limit_side: int = 5000) -> list[Candidate]:
    """Search primitive side triples whose BLZ square class can equal n."""
    out: list[Candidate] = []
    for tile in primitive_eisenstein_triples(limit_side):
        checks = [
            ("alpha,2alpha,3beta", coefficient_alpha_2alpha_3beta(tile)),
            ("alpha,2beta,2alpha+beta", coefficient_alpha_2beta_2alpha_beta(tile)),
        ]
        for template, coeff in checks:
            if is_rational_square(coeff / n):
                out.append(Candidate(n, template, tile, coeff))
    return out


def prime_impossible_templates() -> list[tuple[str, str]]:
    return [
        (
            "alpha,alpha+beta,alpha+2beta",
            "BLZ Proposition 24: N=((a+b)/b)m^2; for prime N this forces a+b=N and b square, contradicting c^2=a^2+ab+b^2 with 0<c<a+b",
        ),
        (
            "2alpha,2beta,alpha+beta",
            "BLZ Proposition 31: N=(a+2b)(b+2a)m^2; the coefficient is a product of two integers >1",
        ),
    ]


def squareclass_cases_for_19() -> dict[str, list[tuple[int, int]]]:
    """Return (d,e) cases where A=d*u^2 and S=e*v^2 for N=19.

    Here S=a+b and A is a+2b or b+2a, depending on the template.  In all cases
    c^2 = A^2 - 3AS + 3S^2.
    """
    return {
        "alpha,2alpha,3beta": [(1, 57), (3, 19), (19, 3), (57, 1)],
        "alpha,2beta,2alpha+beta": [(1, 19), (19, 1)],
    }


def known_witnesses_for_19() -> list[Witness]:
    """Exact BLZ square-class witnesses for N=19.

    These satisfy the necessary BLZ arithmetic conditions only.  They are not
    tiling certificates.
    """
    return [
        Witness(
            template="alpha,2beta,2alpha+beta",
            squareclass="(A,S)=(u^2,19v^2), u=1619, v=280",
            tile=Tile(1_131_561, 358_039, 1_346_761),
            A=2_621_161,
            S=1_489_600,
            c_quartic=1_346_761,
            q=Fraction(5320, 1619),
            coefficient=Fraction(2_621_161, 1_489_600),
        ),
        Witness(
            template="alpha,2alpha,3beta",
            squareclass="(A,S)=(u^2,57v^2), u=8407184675313313, v=1088102355826499",
            tile=Tile(
                64_291_453_825_267_166_692_191_813_022_145,
                3_194_650_169_777_924_718_531_451_006_912,
                65_946_838_654_721_589_964_381_492_334_497,
            ),
            A=70_680_754_164_823_016_129_254_715_035_969,
            S=67_486_103_995_045_091_410_723_264_029_057,
            c_quartic=65_946_838_654_721_589_964_381_492_334_497,
            q=Fraction(62_021_834_282_110_443, 8_407_184_675_313_313),
            coefficient=Fraction(
                70_680_754_164_823_016_129_254_715_035_969,
                3 * 67_486_103_995_045_091_410_723_264_029_057,
            ),
        ),
    ]


def boundary_ratio(template: str, tile: Tile) -> tuple[int, int, int]:
    a, b, c = tile.a, tile.b, tile.c
    if template == "alpha,2beta,2alpha+beta":
        return (a * c, b * (b + 2 * a), c * (a + b))
    if template == "alpha,2alpha,3beta":
        return (c * c, c * (a + 2 * b), 3 * b * (a + b))
    raise ValueError(template)


def boundary_count_coefficient(template: str, tile: Tile) -> int:
    a, b = tile.a, tile.b
    if template == "alpha,2beta,2alpha+beta":
        return (b + 2 * a) * (a + b)
    if template == "alpha,2alpha,3beta":
        return 3 * (a + 2 * b) * (a + b)
    raise ValueError(template)


def boundary_minimum_counts(limit_side: int = 100) -> list[tuple[str, int, str]]:
    """Primitive boundary-integrality product formulas for the two hard templates."""
    templates = [
        (
            "alpha,2beta,2alpha+beta",
            "outer side ratio (ac, b(b+2a), c(a+b)); primitive, so N=(b+2a)(a+b)m^2, composite for prime testing",
        ),
        (
            "alpha,2alpha,3beta",
            "outer side ratio (c^2, c(a+2b), 3b(a+b)); primitive, so N=3(a+2b)(a+b)m^2, composite for prime testing",
        ),
    ]
    triples = primitive_eisenstein_triples(limit_side)
    out: list[tuple[str, int, str]] = []
    for template, formula in templates:
        best_tile = min(triples, key=lambda tile: boundary_count_coefficient(template, tile))
        minimum = boundary_count_coefficient(template, best_tile)
        ratio = boundary_ratio(template, best_tile)
        assert gcd_many(ratio) == 1
        out.append(
            (
                template,
                minimum,
                f"{formula}; minimum attained at sides=({best_tile.a},{best_tile.b},{best_tile.c}) "
                f"with primitive ratio={ratio}",
            )
        )
    return out


def verify_witness(witness: Witness) -> None:
    a, b, c = witness.tile.a, witness.tile.b, witness.tile.c
    assert gcd(a, b) == 1
    assert c * c == a * a + a * b + b * b
    assert witness.c_quartic == c
    assert witness.S < witness.A < 2 * witness.S
    assert c * c == witness.A * witness.A - 3 * witness.A * witness.S + 3 * witness.S * witness.S
    assert witness.coefficient * witness.q * witness.q == 19
    if witness.template == "alpha,2beta,2alpha+beta":
        assert witness.S == a + b
        assert witness.A == b + 2 * a
    elif witness.template == "alpha,2alpha,3beta":
        assert witness.S == a + b
        assert witness.A == a + 2 * b
    else:
        raise AssertionError(witness.template)


def candidate_dict(candidate: Candidate) -> dict[str, object]:
    return {
        "n": candidate.n,
        "template": candidate.template,
        "tile_sides": [candidate.tile.a, candidate.tile.b, candidate.tile.c],
        "coefficient": f"{candidate.coefficient.numerator}/{candidate.coefficient.denominator}",
        "source_status": "square-class candidate only; not a tiling certificate",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--limit-side", type=int, default=5000)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    candidates = candidates_for_n(args.n, args.limit_side)
    if args.json:
        print(json.dumps([candidate_dict(c) for c in candidates], indent=2))
        return

    print(f"N={args.n}: {len(candidates)} BLZ square-class candidate(s) with side bound {args.limit_side}")
    for template, reason in prime_impossible_templates():
        print(f"prime-impossible template: {template}; {reason}")
    if args.n == 19:
        print("N=19 square-class cases for the two unresolved templates:")
        for template, cases in squareclass_cases_for_19().items():
            rendered = ", ".join(f"(A,S)=({d}u^2,{e}v^2)" for d, e in cases)
            print(f"  {template}: {rendered}")
        witnesses = known_witnesses_for_19()
        for witness in witnesses:
            verify_witness(witness)
        print("N=19 exact square-class witnesses satisfying the BLZ necessary arithmetic:")
        for witness in witnesses:
            tile = witness.tile
            print(
                f"  {witness.template}: sides=({tile.a},{tile.b},{tile.c}), "
                f"{witness.squareclass}, q={witness.q}"
            )
        print("N=19 boundary-integrality obstruction for those witnesses/templates:")
        for template, minimum, reason in boundary_minimum_counts():
            print(f"  {template}: ruled out for prime N; minimum coefficient {minimum}; {reason}")
    for candidate in candidates[:50]:
        tile = candidate.tile
        print(
            f"  {candidate.template}: sides=({tile.a},{tile.b},{tile.c}) "
            f"coefficient={candidate.coefficient}"
        )
    if len(candidates) > 50:
        print(f"  ... {len(candidates) - 50} more")


if __name__ == "__main__":
    main()
