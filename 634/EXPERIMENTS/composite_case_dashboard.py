#!/usr/bin/env python3
"""Case dashboard for unresolved composite tile counts.

This is the composite analogue of `prime_case_dashboard.py`: it does not prove
new theorems by itself, but it collects the current positive certificates and
template filters for a requested `N`.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from beeson_3alpha2beta_filter import candidates_for_n as beeson_3alpha2beta_candidates
from beeson_3alpha2beta_boundary import feasible_n14_triquadratic_boundaries
from beeson_3alpha2beta_boundary import feasible_n21_isosceles_alpha_boundaries
from beeson_3alpha2beta_boundary import feasible_n46_triquadratic_boundaries
from beeson_3alpha2beta_boundary import feasible_n56_triquadratic_boundaries
from beeson_3alpha2beta_boundary import boundary_integrality_obstructed
from beeson_3alpha2beta_sufficient import constructions as beeson_3alpha2beta_constructions
from beeson_isosceles_alpha_plus_beta_filter import (
    candidates_for_n as beeson_alpha_plus_beta_candidates,
)
from equilateral_area_candidates import candidates_for_n as equilateral_candidates
from equilateral_boundary_exact import candidates_for_n as equilateral_exact_candidates
from equilateral_gamma_boundary import feasible_boundary as feasible_equilateral_gamma_boundary
from equilateral_pi_boundary import feasible_boundary as feasible_equilateral_pi_boundary
from gamma_2pi3_isosceles_filter import candidates_for_n as gamma_isosceles_candidates
from gamma_2pi3_nonisosceles_boundary import boundary_star_obstructed as gamma_boundary_obstructed
from gamma_2pi3_nonisosceles_exact import candidates_for_n as gamma_nonisosceles_candidates
from zhang_constructive_families import constructed_counts as zhang_counts


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


def is_squarefree(n: int) -> bool:
    n = abs(n)
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return False
        d += 1
    return True


def elementary_positive_reasons(n: int) -> list[str]:
    reasons: list[str] = []
    if is_square(n):
        reasons.append("square family")
    if n % 2 == 0 and is_square(n // 2):
        reasons.append("2m^2 family")
    if n % 3 == 0 and is_square(n // 3):
        reasons.append("3m^2 family")
    if n % 6 == 0 and is_square(n // 6):
        reasons.append("6m^2 family")
    if is_sum_two_positive_squares(n):
        reasons.append("sum of two positive squares")
    return reasons


def commensurable_source_table_status(n: int) -> str:
    """Arithmetic forms listed from Laczkovich/Beeson commensurable reductions."""
    if (
        is_square(n)
        or is_sum_two_positive_squares(n)
        or (n % 2 == 0 and is_square(n // 2))
        or (n % 3 == 0 and is_square(n // 3))
        or (n % 6 == 0 and is_square(n // 6))
    ):
        return "possible by recorded arithmetic forms"
    return "ruled out by recorded arithmetic forms"


def reptile_status(n: int) -> str:
    if is_square(n) or is_sum_two_positive_squares(n) or (n % 3 == 0 and is_square(n // 3)):
        return "possible by Snover-Waiveris-Williams arithmetic"
    return "ruled out in the similar/reptile subcase"


def right_tile_isosceles_status(n: int) -> str:
    if is_square(n) or (n % 6 == 0 and is_square(n // 6)):
        return "possible by recorded arithmetic forms"
    if n % 2 == 0 and is_sum_two_positive_squares(n // 2):
        return "possible by recorded arithmetic forms"
    return "ruled out by recorded arithmetic forms"


def gamma_2alpha_status(n: int) -> str:
    if is_squarefree(n):
        return "ruled out because recorded counts are not squarefree"
    return "not ruled out by squarefree test"


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


def workspace_negative_reason(n: int) -> str | None:
    if n in {14, 15}:
        return "negative by the 14/15 composite benchmark in PROOF.md"
    if n in {21, 30}:
        return "negative by the 21/30 composite benchmark in PROOF.md"
    if n in {33, 35}:
        return "negative by the 33/35 composite benchmark in PROOF.md"
    if n == 22:
        return "negative by the N=22 composite benchmark in PROOF.md"
    return None


def dashboard(n: int, zhang_side_bound: int, equilateral_side_bound: int, equilateral_exact: bool) -> list[str]:
    lines = [f"Composite/general case dashboard for N={n}"]

    if n in {7, 11}:
        lines.append("- all cases: ruled out by Beeson")
        return lines
    if is_prime(n) and n % 4 == 3 and n != 3:
        reason = (
            "source reductions + isosceles gamma boundary transition"
            if gamma_prime_filter_survives(n)
            else "source reductions + isosceles gamma arithmetic filter"
        )
        lines.append(f"- prime obstruction: ruled out by {reason}")
        return lines
    workspace_negative = workspace_negative_reason(n)
    if workspace_negative:
        lines.append(f"- workspace classification: {workspace_negative}")

    elementary = elementary_positive_reasons(n)
    lines.append(
        "- elementary positive families: "
        + (", ".join(elementary) if elementary else "no current elementary hit")
    )
    lines.append(f"- commensurable-angle source table: {commensurable_source_table_status(n)}")
    lines.append(f"- similar/reptile subcase: {reptile_status(n)}")
    lines.append(f"- right-tile isosceles subcase: {right_tile_isosceles_status(n)}")
    lines.append(f"- gamma=2alpha isosceles subcase: {gamma_2alpha_status(n)}")

    beeson_sufficient = beeson_3alpha2beta_constructions(n)
    if n in beeson_sufficient:
        first = beeson_sufficient[n][0]
        lines.append(f"- recorded 3alpha+2beta sufficient construction: positive. {first.source}: {first.details}")
    else:
        lines.append("- recorded 3alpha+2beta sufficient construction: no hit")

    zhang = zhang_counts(n, zhang_side_bound)
    if n in zhang:
        lines.append(f"- Zhang proved constructive families: positive. {zhang[n][0]}")
    else:
        lines.append(f"- Zhang proved constructive families: no hit with side bound {zhang_side_bound}")

    equilateral = (
        equilateral_exact_candidates(n)
        if equilateral_exact
        else equilateral_candidates(n, equilateral_side_bound)
    )
    equilateral_survivors = []
    equilateral_eliminated = []
    for candidate in equilateral:
        a, b, _c = candidate.sides
        if candidate.angle == "2pi/3" and not feasible_equilateral_gamma_boundary(n, a, b):
            equilateral_eliminated.append(candidate)
        elif candidate.angle == "pi/3" and not feasible_equilateral_pi_boundary(n, a, b):
            equilateral_eliminated.append(candidate)
        else:
            equilateral_survivors.append(candidate)
    if equilateral:
        preview = "; ".join(
            f"angle={row.angle}, sides={row.sides}, L={row.outer_side}"
            for row in equilateral_survivors[:4]
        )
        suffix = " ..." if len(equilateral_survivors) > 4 else ""
        survivor_text = (
            f"{len(equilateral_survivors)} remain after encoded boundary checks"
            if equilateral_survivors
            else "0 remain after encoded boundary checks"
        )
        equilateral_source = (
            "from exact boundary-length equations; "
            if equilateral_exact
            else f"with primitive side entries <= {equilateral_side_bound}; "
        )
        lines.append(
            "- equilateral outer arithmetic filter: "
            + f"{len(equilateral)} area/boundary-length candidate(s) "
            + equilateral_source
            + f"{survivor_text}"
        )
        if equilateral_survivors:
            lines.append(f"  surviving equilateral candidates: {preview}{suffix}")
        if equilateral_eliminated:
            lines.append(
                f"  eliminated equilateral candidates: {len(equilateral_eliminated)} "
                "by boundary-star obstruction"
            )
    else:
        lines.append(
            "- equilateral outer arithmetic filter: "
            + (
                "no exact boundary-length candidates"
                if equilateral_exact
                else f"no area/boundary-length candidates with primitive side entries <= {equilateral_side_bound}"
            )
        )

    raw_3a2b = beeson_3alpha2beta_candidates(n)
    strong_alpha_beta = beeson_alpha_plus_beta_candidates(n)
    unresolved_3a2b = []
    eliminated_3a2b = []
    strong_keys = {(row.M, row.sides) for row in strong_alpha_beta}
    n14_boundary_obstructed = n == 14 and not feasible_n14_triquadratic_boundaries()
    n21_boundary_obstructed = n == 21 and not feasible_n21_isosceles_alpha_boundaries()
    n46_boundary_obstructed = n == 46 and not feasible_n46_triquadratic_boundaries()
    n56_boundary_obstructed = n == 56 and not feasible_n56_triquadratic_boundaries()
    for candidate in raw_3a2b:
        if candidate.case == "(a+b,a+b,a)" and (candidate.m, candidate.sides) not in strong_keys:
            eliminated_3a2b.append((candidate, "strong isosceles-alpha+beta filter"))
        elif (
            n14_boundary_obstructed
            and candidate.case == "(2a,b,a+b)"
            and candidate.m == 2
            and candidate.sides == (6, 5, 9)
        ):
            eliminated_3a2b.append((candidate, "boundary-star obstruction"))
        elif (
            n21_boundary_obstructed
            and candidate.case == "(a,a,a+2b)"
            and candidate.m == 5
            and candidate.sides == (2, 3, 4)
        ):
            eliminated_3a2b.append((candidate, "boundary-star obstruction"))
        elif (
            n46_boundary_obstructed
            and candidate.case == "(2a,b,a+b)"
            and candidate.m == 2
            and candidate.sides == (10, 21, 25)
        ):
            eliminated_3a2b.append((candidate, "boundary-star obstruction"))
        elif (
            n56_boundary_obstructed
            and candidate.case == "(2a,b,a+b)"
            and candidate.m == 4
            and candidate.sides == (6, 5, 9)
        ):
            eliminated_3a2b.append((candidate, "boundary-star obstruction"))
        elif boundary_integrality_obstructed(n, candidate.case, candidate.sides):
            eliminated_3a2b.append((candidate, "boundary-integrality obstruction"))
        else:
            unresolved_3a2b.append(candidate)
    lines.append(
        "- 3alpha+2beta necessary filter: "
        f"{len(raw_3a2b)} raw rational candidate(s); "
        f"{len(strong_alpha_beta)} survive the strong isosceles-alpha+beta filter; "
        f"{len(unresolved_3a2b)} remain after encoded local eliminations"
    )
    if raw_3a2b:
        preview = "; ".join(
            f"M={candidate.m}, case={candidate.case}, sides={candidate.sides}"
            for candidate in raw_3a2b[:4]
        )
        suffix = " ..." if len(raw_3a2b) > 4 else ""
        lines.append(f"  first raw candidates: {preview}{suffix}")
    if eliminated_3a2b:
        summary: dict[str, int] = {}
        for _candidate, reason in eliminated_3a2b:
            summary[reason] = summary.get(reason, 0) + 1
        rendered = ", ".join(f"{count} by {reason}" for reason, count in sorted(summary.items()))
        lines.append(f"  eliminated among raw candidates: {rendered}")
    if unresolved_3a2b:
        preview = "; ".join(
            f"M={candidate.m}, case={candidate.case}, sides={candidate.sides}"
            for candidate in unresolved_3a2b[:3]
        )
        suffix = " ..." if len(unresolved_3a2b) > 3 else ""
        lines.append(f"  unresolved 3alpha+2beta candidates: {preview}{suffix}")

    gamma_iso = gamma_isosceles_candidates(n)
    if gamma_iso:
        preview = ", ".join(f"sides={candidate.sides}, m={candidate.m}" for candidate in gamma_iso[:3])
        lines.append(
            "- isosceles gamma=2pi/3 filter: "
            f"{len(gamma_iso)} arithmetic candidate(s), all ruled out by the boundary-transition lemma; "
            f"{preview}"
        )
    else:
        lines.append("- isosceles gamma=2pi/3 filter: no arithmetic candidates")

    blz = gamma_nonisosceles_candidates(n)
    unresolved_blz = []
    eliminated_blz = []
    for candidate in blz:
        if gamma_boundary_obstructed(candidate.template, candidate.sides, candidate.square_parameter):
            eliminated_blz.append((candidate, "boundary-star obstruction"))
        else:
            unresolved_blz.append(candidate)
    lines.append(
        "- non-isosceles gamma=2pi/3 exact arithmetic filter: "
        f"{len(blz)} candidate(s); {len(unresolved_blz)} remain after encoded local eliminations"
    )
    if blz:
        preview = "; ".join(
            f"{candidate.template}, sides={candidate.sides}, coefficient={candidate.coefficient}"
            for candidate in blz[:3]
        )
        suffix = " ..." if len(blz) > 3 else ""
        lines.append(f"  first BLZ candidates: {preview}{suffix}")
    if eliminated_blz:
        summary: dict[str, int] = {}
        for _candidate, reason in eliminated_blz:
            summary[reason] = summary.get(reason, 0) + 1
        rendered = ", ".join(f"{count} by {reason}" for reason, count in sorted(summary.items()))
        lines.append(f"  eliminated among gamma candidates: {rendered}")
    if unresolved_blz:
        preview = "; ".join(
            f"{candidate.template}, sides={candidate.sides}, coefficient={candidate.coefficient}"
            for candidate in unresolved_blz[:3]
        )
        suffix = " ..." if len(unresolved_blz) > 3 else ""
        lines.append(f"  unresolved gamma candidates: {preview}{suffix}")

    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--zhang-side-bound", type=int, default=80)
    parser.add_argument("--equilateral-side-bound", type=int, default=250)
    parser.add_argument(
        "--equilateral-exact",
        action="store_true",
        help="use the exact finite equilateral boundary-length solver instead of side-bounded scan",
    )
    args = parser.parse_args()

    for index, n in enumerate(args.n):
        if index:
            print()
        for line in dashboard(n, args.zhang_side_bound, args.equilateral_side_bound, args.equilateral_exact):
            print(line)


if __name__ == "__main__":
    main()
