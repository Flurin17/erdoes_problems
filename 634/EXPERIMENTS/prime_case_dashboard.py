#!/usr/bin/env python3
"""High-level source-case dashboard for prime tile counts.

This script does not prove new theorems. It applies the source-level reductions
recorded in PROOF.md/LITERATURE.md to a prime p and reports which broad cases are
settled by known arithmetic and which remain open to exact template analysis.
"""

from __future__ import annotations

import argparse
from math import isqrt

from beeson_3alpha2beta_filter import candidates_for_n
from blz_gamma_2pi3_nonisosceles_filter import (
    boundary_minimum_counts,
    known_witnesses_for_19,
)
from gamma_2pi3_isosceles_filter import (
    candidates_for_n as gamma_isosceles_candidates,
    prime_candidates as gamma_isosceles_prime_candidates,
)
from beeson_isosceles_alpha_plus_beta_filter import candidates_for_n as alpha_plus_beta_candidates


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


def is_sum_two_positive_squares(n: int) -> bool:
    for a in range(1, isqrt(n) + 1):
        b2 = n - a * a
        b = isqrt(b2)
        if b >= 1 and b * b == b2:
            return True
    return False


def status_for_prime(p: int) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []

    if p in {7, 11}:
        rows.append(("all cases", "ruled out", "Beeson theorem: no 7-tiling or 11-tiling"))
        return rows
    if p == 3:
        rows.append(("existence", "positive", "the 3m^2 family gives a 3-tiling"))
        return rows

    reptile_positive = p == 3 or is_sum_two_positive_squares(p)
    rows.append(
        (
            "similar/reptile",
            "possible by arithmetic" if reptile_positive else "ruled out",
            "Snover-Waiveris-Williams: prime reptile counts are 3 or sums of two squares",
        )
    )

    commensurable_positive = p in {2, 3} or is_sum_two_positive_squares(p)
    rows.append(
        (
            "commensurable-angle source table",
            "possible by arithmetic" if commensurable_positive else "ruled out",
            "Beeson/Laczkovich table forms reduce prime counts to 2, 3, or sums of two squares",
        )
    )

    rows.append(
        (
            "equilateral outer triangle",
            "ruled out" if p > 3 else "possible",
            "Beeson: equilateral N-tiling with N>3 is not prime",
        )
    )

    if p <= 500:
        candidates_3a2b = candidates_for_n(p)
        alpha_plus_beta_raw = [c for c in candidates_3a2b if c.case == "(a+b,a+b,a)"]
        alpha_plus_beta_strong = alpha_plus_beta_candidates(p)
        sanity_note = (
            f"sanity filters: {len(candidates_3a2b)} raw rational candidate(s), "
            f"{len(alpha_plus_beta_raw)} isosceles-alpha+beta, "
            f"{len(alpha_plus_beta_strong)} survive the stronger filter"
        )
    else:
        sanity_note = "sanity filters skipped for p > 500"
    rows.append(
        (
            "3alpha+2beta=pi template",
            "ruled out",
            (
                "Beeson Theorem 21 proves prime N impossible in this template; "
                f"{sanity_note}"
            ),
        )
    )

    gamma_iso = (
        [c for c in gamma_isosceles_prime_candidates(p, p % 4) if c.n == p]
        if is_prime(p)
        else gamma_isosceles_candidates(p)
    )
    if gamma_iso:
        gamma_status = "ruled out by boundary transition"
        gamma_reason = (
            "Beeson Section 12 filter leaves arithmetic candidate(s), but the "
            "local boundary-transition table forbids an outer base side whose "
            "two corner endpoints are both alpha"
        )
    else:
        gamma_status = "ruled out by necessary arithmetic"
        gamma_reason = "Beeson Section 12 filter leaves 0 candidate(s)"
    rows.append(
        (
            "gamma=2pi/3 isosceles outer triangle",
            gamma_status,
            gamma_reason,
        )
    )

    known_blz_witnesses = known_witnesses_for_19() if p == 19 else []
    boundary_mins = boundary_minimum_counts()
    rows.append(
        (
            "gamma=2pi/3 non-isosceles templates",
            "ruled out for prime counts",
            "BLZ Propositions 24 and 31 rule out primes in two templates; "
            "boundary integrality upgrades the Proposition 26 and 28 square-class templates to "
            "integer product formulas, hence no prime counts; "
            f"minimum coefficients for those two templates are "
            f"{', '.join(str(minimum) for _, minimum, _ in boundary_mins)}"
            + (
                f"; {len(known_blz_witnesses)} exact N=19 square-class witness(es) illustrate why the extra boundary step is needed"
                if known_blz_witnesses
                else ""
            ),
        )
    )

    other_isosceles_ruled = p % 4 == 3 and p != 3
    rows.append(
        (
            "other isosceles outer-triangle templates",
            "ruled out for this prime" if other_isosceles_ruled else "partly source-ruled",
            (
                "Beeson: right-tile isosceles counts are squares, even sums of squares, or 6m^2; "
                "gamma=2alpha counts are not squarefree; "
                "3alpha+2beta is prime-ruled by TriangleTiling3"
            ),
        )
    )

    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    args = parser.parse_args()
    p = args.p
    if not is_prime(p):
        raise SystemExit(f"{p} is not prime")
    print(f"Prime case dashboard for p={p}")
    for case, status, reason in status_for_prime(p):
        print(f"- {case}: {status}. {reason}.")


if __name__ == "__main__":
    main()
