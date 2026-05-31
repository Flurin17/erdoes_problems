#!/usr/bin/env python3
"""Enumerate Zhang's constructive families for 2pi/3 triangular tiles.

This script records positive constructions only.  It deliberately does not use
Zhang's conjectural exactness statements as obstructions.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


def ceil_div(num: int, den: int) -> int:
    return -(-num // den)


@dataclass(frozen=True)
class Tile:
    a: int
    b: int
    c: int
    gamma: str


@dataclass(frozen=True)
class Family:
    label: str
    coefficient: int
    parameter: str
    min_parameter: int | None
    source: str

    def count(self, value: int) -> int:
        return self.coefficient * value * value


def primitive_2pi3_tiles(limit_side: int) -> list[Tile]:
    """Primitive integer tiles with c^2 = a^2 + ab + b^2."""
    out: list[Tile] = []
    for a in range(1, limit_side + 1):
        for b in range(1, limit_side + 1):
            if gcd(a, b) != 1:
                continue
            c2 = a * a + a * b + b * b
            c = isqrt(c2)
            if c * c == c2 and c <= limit_side:
                out.append(Tile(a, b, c, "2pi/3"))
    return out


def primitive_pi3_tiles(limit_side: int) -> list[Tile]:
    """Primitive integer tiles with c^2 = a^2 - ab + b^2."""
    out: list[Tile] = []
    for a in range(1, limit_side + 1):
        for b in range(1, limit_side + 1):
            if gcd(a, b) != 1:
                continue
            c2 = a * a - a * b + b * b
            c = isqrt(c2)
            if c * c == c2 and c <= limit_side and not (a == b == c):
                out.append(Tile(a, b, c, "pi/3"))
    return out


def zhang_threshold_2pi3(tile: Tile) -> int:
    return max(1, 3 * ceil_div(tile.c * tile.c - tile.a - tile.b, tile.a * tile.b))


def zhang_threshold_pi3(tile: Tile) -> int:
    return max(1, 3 * ceil_div(tile.a * tile.a + tile.b * tile.b - tile.a - tile.b, tile.a * tile.b))


def semigroup_values(x: int, y: int, limit: int) -> list[int]:
    values: set[int] = set()
    for i in range(limit // x + 1):
        for j in range(limit // y + 1):
            value = i * x + j * y
            if 0 < value <= limit:
                values.add(value)
    return sorted(values)


def gamma_2pi3_families(tile: Tile) -> list[Family]:
    """Zhang Section 3/5 families using the 2pi/3 equilateral auxiliary tiling."""
    a, b = tile.a, tile.b
    m0 = zhang_threshold_2pi3(tile)
    return [
        Family("equilateral", a * b, "m", m0, "Theorem 4"),
        Family("isosceles alpha-alpha", b * (a + 2 * b), "m", m0, "Proposition 8"),
        Family("isosceles beta-beta", a * (b + 2 * a), "m", m0, "Proposition 8, swapped"),
        Family("alpha, alpha+beta, alpha+2beta", b * (a + b), "m", m0, "Proposition 9"),
        Family("beta, alpha+beta, beta+2alpha", a * (a + b), "m", m0, "Proposition 9, swapped"),
        Family("alpha, 2beta, 2alpha+beta", (b + 2 * a) * (a + b), "m", m0, "Proposition 10"),
        Family("beta, 2alpha, alpha+2beta", (a + 2 * b) * (a + b), "m", m0, "Proposition 10, swapped"),
    ]


def gamma_2pi3_semigroup_families(tile: Tile) -> list[Family]:
    """Zhang families whose parameter lies in b*N0 + c*N0, eventually all large values."""
    a, b = tile.a, tile.b
    frobenius = b * tile.c - b - tile.c
    return [
        Family("2alpha, 2beta, alpha+beta", (a + 2 * b) * (b + 2 * a), "q in bN0+cN0", frobenius + 1, "Theorem 7"),
        Family("alpha, 2alpha, 3beta", 3 * (a + 2 * b) * (a + b), "q in bN0+cN0", frobenius + 1, "Proposition 11"),
        Family("beta, 2beta, 3alpha", 3 * (b + 2 * a) * (a + b), "q in bN0+cN0", frobenius + 1, "Proposition 11, swapped"),
    ]


def gamma_pi3_equilateral_family(tile: Tile) -> Family:
    """Zhang Theorem 5, the pi/3 analogue of the equilateral construction."""
    return Family("equilateral pi/3 analogue", tile.a * tile.b, "m", zhang_threshold_pi3(tile), "Theorem 5")


def constructed_counts(limit_n: int, limit_side: int) -> dict[int, list[str]]:
    out: dict[int, list[str]] = {}

    for tile in primitive_2pi3_tiles(limit_side):
        for family in gamma_2pi3_families(tile):
            assert family.min_parameter is not None
            m = family.min_parameter
            while family.count(m) <= limit_n:
                out.setdefault(family.count(m), []).append(
                    f"{family.source}: ({tile.a},{tile.b},{tile.c}), {family.label}, m={m}"
                )
                m += 1
        q_limit = isqrt(limit_n // min(f.coefficient for f in gamma_2pi3_semigroup_families(tile)))
        for q in semigroup_values(tile.b, tile.c, q_limit):
            for family in gamma_2pi3_semigroup_families(tile):
                n = family.count(q)
                if n <= limit_n:
                    out.setdefault(n, []).append(
                        f"{family.source}: ({tile.a},{tile.b},{tile.c}), {family.label}, q={q}"
                    )

    for tile in primitive_pi3_tiles(limit_side):
        family = gamma_pi3_equilateral_family(tile)
        assert family.min_parameter is not None
        m = family.min_parameter
        while family.count(m) <= limit_n:
            out.setdefault(family.count(m), []).append(
                f"{family.source}: pi/3 ({tile.a},{tile.b},{tile.c}), {family.label}, m={m}"
            )
            m += 1

    return out


def can_zhang_construct_prime(p: int, limit_side: int) -> list[str]:
    """Check whether any Zhang family with searched side bound can hit prime p."""
    hits: list[str] = []
    for tile in primitive_2pi3_tiles(limit_side):
        for family in [*gamma_2pi3_families(tile), *gamma_2pi3_semigroup_families(tile)]:
            if p % family.coefficient == 0:
                q2 = p // family.coefficient
                q = isqrt(q2)
                if q * q == q2:
                    hits.append(f"({tile.a},{tile.b},{tile.c}) {family.label} with parameter {q}")
    for tile in primitive_pi3_tiles(limit_side):
        family = gamma_pi3_equilateral_family(tile)
        if p % family.coefficient == 0:
            q2 = p // family.coefficient
            q = isqrt(q2)
            if q * q == q2:
                hits.append(f"pi/3 ({tile.a},{tile.b},{tile.c}) {family.label} with parameter {q}")
    return hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit-n", type=int, default=5000)
    parser.add_argument("--limit-side", type=int, default=80)
    parser.add_argument("--prime", type=int, default=19)
    args = parser.parse_args()

    counts = constructed_counts(args.limit_n, args.limit_side)
    print(f"Zhang constructed counts <= {args.limit_n} with side bound {args.limit_side}: {len(counts)}")
    for n in sorted(counts)[:30]:
        print(f"{n}: {counts[n][0]}")
    hits = can_zhang_construct_prime(args.prime, args.limit_side)
    if hits:
        print(f"prime {args.prime}: constructed by searched Zhang families")
        for hit in hits:
            print(f"  {hit}")
    else:
        print(f"prime {args.prime}: no hit in Zhang quadratic families with side bound {args.limit_side}")


if __name__ == "__main__":
    main()
