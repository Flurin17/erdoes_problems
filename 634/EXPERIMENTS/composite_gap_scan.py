#!/usr/bin/env python3
"""Scan small counts against the currently encoded #634 certificates.

This script is deliberately conservative.  It separates three states:

* classified by a recorded positive or negative theorem/construction;
* not classified, but with an explicit survivor in one of the encoded filters;
* not classified and with no survivor in the encoded filters.

The last state is not a proof of impossibility.  It usually means the value is
blocked on source-reduction coverage that has not been reconstructed locally.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt

from beeson_3alpha2beta_boundary import feasible_n14_triquadratic_boundaries
from beeson_3alpha2beta_boundary import feasible_n21_isosceles_alpha_boundaries
from beeson_3alpha2beta_boundary import feasible_n46_triquadratic_boundaries
from beeson_3alpha2beta_boundary import feasible_n56_triquadratic_boundaries
from beeson_3alpha2beta_boundary import boundary_integrality_obstructed
from beeson_3alpha2beta_filter import Candidate as ThreeAlphaCandidate
from beeson_3alpha2beta_filter import candidates_for_n as three_alpha_candidates
from beeson_3alpha2beta_sufficient import constructions as three_alpha_constructions
from beeson_isosceles_alpha_plus_beta_filter import (
    candidates_for_n as alpha_plus_beta_candidates,
)
from equilateral_area_candidates import candidates_for_n as equilateral_candidates
from equilateral_boundary_exact import candidates_for_n as equilateral_exact_candidates
from equilateral_gamma_boundary import feasible_boundary as feasible_equilateral_gamma_boundary
from equilateral_pi_boundary import feasible_boundary as feasible_equilateral_pi_boundary
from gamma_2pi3_isosceles_filter import candidates_for_n as gamma_isosceles_candidates
from gamma_2pi3_nonisosceles_boundary import boundary_star_obstructed as gamma_boundary_obstructed
from gamma_2pi3_nonisosceles_exact import Candidate as GammaCandidate
from gamma_2pi3_nonisosceles_exact import candidates_for_n as gamma_nonisosceles_candidates
from zhang_constructive_families import constructed_counts as zhang_counts


@dataclass(frozen=True)
class ScanRow:
    n: int
    status: str
    reasons: tuple[str, ...]
    three_alpha_raw: int = 0
    three_alpha_survivors: int = 0
    gamma_iso_raw: int = 0
    gamma_noniso_raw: int = 0
    gamma_noniso_survivors: int = 0
    equilateral_raw: int = 0
    equilateral_survivors: int = 0


def is_square(n: int) -> bool:
    root = isqrt(n)
    return root * root == n


def is_sum_two_positive_squares(n: int) -> bool:
    for a in range(1, isqrt(n) + 1):
        b2 = n - a * a
        b = isqrt(b2)
        if b >= 1 and b * b == b2:
            return True
    return False


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


def elementary_positive_reasons(n: int) -> list[str]:
    reasons: list[str] = []
    if is_square(n):
        reasons.append("square")
    if n % 2 == 0 and is_square(n // 2):
        reasons.append("2m^2")
    if n % 3 == 0 and is_square(n // 3):
        reasons.append("3m^2")
    if n % 6 == 0 and is_square(n // 6):
        reasons.append("6m^2")
    if is_sum_two_positive_squares(n):
        reasons.append("a^2+b^2")
    return reasons


def gamma_prime_filter_survives(p: int) -> bool:
    for t in range(1, isqrt((p - 1) // 2) + 1):
        b = t * t
        a = p - 2 * b
        if a <= 0 or gcd(a, b) != 1:
            continue
        c2 = a * a + a * b + b * b
        c = isqrt(c2)
        if c * c == c2:
            return True
    return False


def classified_reasons(n: int, zhang_side_bound: int) -> tuple[str, list[str]]:
    positives = elementary_positive_reasons(n)
    beeson = three_alpha_constructions(n)
    if n in beeson:
        first = beeson[n][0]
        positives.append(f"Beeson 3alpha+2beta sufficient: {first.details}")
    zhang = zhang_counts(n, zhang_side_bound)
    if n in zhang:
        positives.append(f"Zhang family: {zhang[n][0]}")
    if positives:
        return "positive", positives

    if n in {7, 11}:
        return "negative", ["Beeson no-7/no-11 theorem"]
    if n in {14, 15, 21, 30, 33, 35, 38, 39, 42, 46, 51, 55, 57, 62}:
        return "negative", ["workspace composite benchmark; exact source-row eliminations"]
    if n == 22:
        return "negative", ["workspace N=22 composite benchmark; exact source-row eliminations"]
    if is_prime(n) and n % 4 == 3 and n != 3:
        if gamma_prime_filter_survives(n):
            return "negative", ["prime 3 mod 4 obstruction; isosceles gamma removed by boundary transition"]
        return "negative", ["prime 3 mod 4 obstruction; no isosceles gamma arithmetic candidate"]
    return "open", []


def three_alpha_survivors(n: int) -> tuple[list[ThreeAlphaCandidate], list[ThreeAlphaCandidate]]:
    raw = three_alpha_candidates(n)
    strong_alpha_beta = alpha_plus_beta_candidates(n)
    strong_keys = {(row.M, row.sides) for row in strong_alpha_beta}
    n14_boundary_obstructed = n == 14 and not feasible_n14_triquadratic_boundaries()
    n21_boundary_obstructed = n == 21 and not feasible_n21_isosceles_alpha_boundaries()
    n46_boundary_obstructed = n == 46 and not feasible_n46_triquadratic_boundaries()
    n56_boundary_obstructed = n == 56 and not feasible_n56_triquadratic_boundaries()

    survivors: list[ThreeAlphaCandidate] = []
    for candidate in raw:
        if candidate.case == "(a+b,a+b,a)" and (candidate.m, candidate.sides) not in strong_keys:
            continue
        if (
            n14_boundary_obstructed
            and candidate.case == "(2a,b,a+b)"
            and candidate.m == 2
            and candidate.sides == (6, 5, 9)
        ):
            continue
        if (
            n21_boundary_obstructed
            and candidate.case == "(a,a,a+2b)"
            and candidate.m == 5
            and candidate.sides == (2, 3, 4)
        ):
            continue
        if (
            n46_boundary_obstructed
            and candidate.case == "(2a,b,a+b)"
            and candidate.m == 2
            and candidate.sides == (10, 21, 25)
        ):
            continue
        if (
            n56_boundary_obstructed
            and candidate.case == "(2a,b,a+b)"
            and candidate.m == 4
            and candidate.sides == (6, 5, 9)
        ):
            continue
        if boundary_integrality_obstructed(n, candidate.case, candidate.sides):
            continue
        survivors.append(candidate)
    return raw, survivors


def gamma_survivors(n: int) -> tuple[list[GammaCandidate], list[GammaCandidate]]:
    raw = gamma_nonisosceles_candidates(n)
    survivors: list[GammaCandidate] = []
    for candidate in raw:
        if gamma_boundary_obstructed(candidate.template, candidate.sides, candidate.square_parameter):
            continue
        survivors.append(candidate)
    return raw, survivors


def equilateral_survivors(n: int, side_bound: int, exact: bool):
    raw = equilateral_exact_candidates(n) if exact else equilateral_candidates(n, side_bound)
    survivors = []
    for candidate in raw:
        a, b, _c = candidate.sides
        if candidate.angle == "2pi/3" and not feasible_equilateral_gamma_boundary(n, a, b):
            continue
        if candidate.angle == "pi/3" and not feasible_equilateral_pi_boundary(n, a, b):
            continue
        survivors.append(candidate)
    return raw, survivors


def scan(n: int, zhang_side_bound: int, equilateral_side_bound: int, equilateral_exact: bool) -> ScanRow:
    status, reasons = classified_reasons(n, zhang_side_bound)
    if status != "open":
        return ScanRow(n, status, tuple(reasons))

    three_raw, three_survivors = three_alpha_survivors(n)
    equilateral_raw, equilateral_unresolved = equilateral_survivors(
        n, equilateral_side_bound, equilateral_exact
    )
    gamma_iso = gamma_isosceles_candidates(n)
    gamma_raw, gamma_unresolved = gamma_survivors(n)

    reasons = []
    if three_survivors:
        reasons.append("3alpha+2beta survivor")
    if gamma_unresolved:
        reasons.append("non-isosceles gamma=2pi/3 survivor")
    if gamma_iso:
        reasons.append("isosceles gamma arithmetic candidate; boundary-transition lemma rules this template out")
    if equilateral_unresolved:
        preview = ", ".join(
            f"{row.angle} sides={row.sides} L={row.outer_side}" for row in equilateral_unresolved[:2]
        )
        suffix = " ..." if len(equilateral_unresolved) > 2 else ""
        reasons.append(f"equilateral area/boundary candidate(s): {preview}{suffix}")
    elif equilateral_raw:
        reasons.append("equilateral area candidates locally eliminated by boundary-star check")

    if three_survivors or gamma_unresolved or equilateral_unresolved:
        status = "open-with-encoded-survivor"
    else:
        status = "open-no-encoded-survivor"
        reasons.append("all currently encoded filters empty or locally eliminated")

    return ScanRow(
        n,
        status,
        tuple(reasons),
        three_alpha_raw=len(three_raw),
        three_alpha_survivors=len(three_survivors),
        gamma_iso_raw=len(gamma_iso),
        gamma_noniso_raw=len(gamma_raw),
        gamma_noniso_survivors=len(gamma_unresolved),
        equilateral_raw=len(equilateral_raw),
        equilateral_survivors=len(equilateral_unresolved),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="*", type=int, help="specific counts to scan")
    parser.add_argument("--limit", type=int, default=250)
    parser.add_argument("--lo", type=int, default=1)
    parser.add_argument("--zhang-side-bound", type=int, default=80)
    parser.add_argument("--equilateral-side-bound", type=int, default=250)
    parser.add_argument(
        "--equilateral-exact",
        action="store_true",
        help="use exact finite equilateral boundary-length solver instead of side-bounded scan",
    )
    parser.add_argument(
        "--only-open",
        action="store_true",
        help="print only rows not classified by recorded certificates",
    )
    args = parser.parse_args()

    ns = args.n if args.n else range(args.lo, args.limit + 1)
    for n in ns:
        row = scan(n, args.zhang_side_bound, args.equilateral_side_bound, args.equilateral_exact)
        if args.only_open and not row.status.startswith("open"):
            continue
        counts = (
            f"3a2b={row.three_alpha_survivors}/{row.three_alpha_raw}, "
            f"eq={row.equilateral_survivors}/{row.equilateral_raw}, "
            f"gIso={row.gamma_iso_raw}, "
            f"gNonIso={row.gamma_noniso_survivors}/{row.gamma_noniso_raw}"
        )
        print(f"{row.n:4d}  {row.status:26s}  {counts:24s}  {'; '.join(row.reasons)}", flush=True)


if __name__ == "__main__":
    main()
