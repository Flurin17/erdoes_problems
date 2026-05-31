#!/usr/bin/env python3
"""Diagnostics for prime candidates in Beeson's isosceles gamma=2pi/3 filter.

For prime N=p == 3 mod 4, the filter forces b=t^2 and a+2b=p.  Combining this
with the primitive Eisenstein triple parametrization gives

    t = 2rs,
    a = 3s^4 - 2r^2s^2 - r^4,
    b = 4r^2s^2,
    c = 3s^4 + r^4,
    p = 3s^4 + 6r^2s^2 - r^4,

where gcd(r,s)=1, r<s, and r,s have opposite parity.

The output here is diagnostic.  It records boundary decompositions and the
strict edge-to-edge boundary parity test for the surviving prime candidates.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from gamma_2pi3_isosceles_filter import Candidate, prime_candidates


@dataclass(frozen=True)
class Parameters:
    r: int
    s: int
    u: int
    v: int


def recover_parameters(candidate: Candidate) -> Parameters:
    a, b, c = candidate.sides
    t = candidate.m
    for r in range(1, t + 1):
        if t % (2 * r) != 0:
            continue
        s = t // (2 * r)
        if not (0 < r < s):
            continue
        if 3 * s**4 - 2 * r * r * s * s - r**4 != a:
            continue
        if 4 * r * r * s * s != b:
            continue
        if 3 * s**4 + r**4 != c:
            continue
        return Parameters(r, s, s * s + r * r, s * s - r * r)
    raise ValueError(candidate)


def decompositions(length: int, sides: tuple[int, int, int]) -> list[tuple[int, int, int, int]]:
    """Return decompositions as (nb, na, nc, edge_count)."""
    a, b, c = sides
    out: list[tuple[int, int, int, int]] = []
    for nb in range(length // b + 1):
        for na in range(length // a + 1):
            rem = length - nb * b - na * a
            if rem >= 0 and rem % c == 0:
                nc = rem // c
                out.append((nb, na, nc, nb + na + nc))
    return out


def diagnostic(candidate: Candidate) -> list[str]:
    params = recover_parameters(candidate)
    a, b, c = candidate.sides
    t = candidate.m
    equal = decompositions(candidate.outer_equal_side, candidate.sides)
    base = decompositions(candidate.outer_base, candidate.sides)
    equal_unique_c = equal == [(0, 0, t, t)]
    viable_base = [row for row in base if not equal_unique_c or row[0] >= 2]
    strict_possible = any((2 * t + row[3]) % 2 == candidate.n % 2 for row in viable_base)
    lines = [
        f"N={candidate.n}, (r,s)=({params.r},{params.s}), sides=(a,b,c)={candidate.sides}, t={t}",
        f"  p=3s^4+6r^2s^2-r^4, a=3s^4-2r^2s^2-r^4, c=3s^4+r^4",
        f"  equal-side decompositions: {equal}",
        f"  base decompositions: {base}",
        f"  viable base decompositions under unique-c equal sides: {viable_base}",
        (
            "  strict edge-to-edge boundary parity: possible"
            if strict_possible
            else "  strict edge-to-edge boundary parity: impossible"
        ),
    ]
    for nb, na, nc, edge_count in viable_base:
        interior = (candidate.n - na, candidate.n - nb, candidate.n - 2 * t - nc)
        lines.append(f"    base ({nb},{na},{nc}) leaves interior (a,b,c)={interior}")
        if interior[2] % 2 == 1:
            lines.append(
                f"      odd c-incidence forces an odd-c matched segment; "
                f"small parametrized relation {params.u}a={params.v}b+{params.v}c"
            )
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=20_000)
    args = parser.parse_args()
    candidates = prime_candidates(args.limit)
    print(f"prime isosceles gamma=2pi/3 candidates up to {args.limit}: {len(candidates)}")
    for candidate in candidates:
        for line in diagnostic(candidate):
            print(line)


if __name__ == "__main__":
    main()
