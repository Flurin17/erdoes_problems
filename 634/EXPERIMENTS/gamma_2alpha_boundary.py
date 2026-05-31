#!/usr/bin/env python3
"""Boundary arithmetic for Beeson's isosceles `gamma=2alpha` branch.

This implements the finite arithmetic enumeration described in Lemma 11.14 of
Beeson's isosceles-triangle paper.  It is intentionally only a certificate
generator for the boundary-arithmetic stage, not a full tiling search.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


Triple = tuple[int, int, int]


@dataclass(frozen=True)
class BoundaryCandidate:
    n: int
    tile: Triple
    x: int
    y: int
    x_representations: tuple[Triple, ...]
    y_representations: tuple[Triple, ...]
    min_boundary_tiles: int
    boundary_count_obstructed: bool


@dataclass(frozen=True)
class RefinedGamma2AlphaSurvivor:
    candidate: BoundaryCandidate
    y_representations: tuple[Triple, ...]


def squarefree_part(n: int) -> int:
    n = abs(n)
    out = 1
    d = 2
    while d * d <= n:
        parity = 0
        while n % d == 0:
            n //= d
            parity ^= 1
        if parity:
            out *= d
        d += 1 if d == 2 else 2
    if n > 1:
        out *= n
    return out


def integer_square_root(n: int) -> int | None:
    root = isqrt(n)
    return root if root * root == n else None


def strict_m_bound(n: int) -> int:
    """Largest integer `m` satisfying Lemma 11.12's strict bound."""
    numerator = 16 * n + (n + 1) * (n + 1)
    candidate = numerator // 16
    while 16 * candidate >= numerator:
        candidate -= 1
    return candidate


def is_triangle(sides: Triple) -> bool:
    largest = max(sides)
    return largest < sum(sides) - largest


def side_representations(
    total: int,
    sides: Triple,
    *,
    max_tiles_exclusive_times4: int | None = None,
    require_qr: bool = False,
) -> tuple[Triple, ...]:
    """Return all `total = pa+qb+rc` representations in nonnegative integers."""
    a, b, c = sides
    out: list[Triple] = []
    for p in range(total // a + 1):
        rem_p = total - p * a
        for q in range(rem_p // b + 1):
            rem_q = rem_p - q * b
            if rem_q % c != 0:
                continue
            r = rem_q // c
            if require_qr and (q == 0 or r == 0):
                continue
            if (
                max_tiles_exclusive_times4 is not None
                and 4 * (p + q + r) >= max_tiles_exclusive_times4
            ):
                continue
            out.append((p, q, r))
    return tuple(out)


def min_representation_terms(total: int, sides: Triple) -> int | None:
    reps = side_representations(total, sides)
    if not reps:
        return None
    return min(sum(rep) for rep in reps)


def boundary_count_obstructed(n: int, x: int, y: int, sides: Triple) -> tuple[int, bool]:
    """Apply the boundary-count lower bound used in Beeson Lemma 11.16.

    If a side of length `x` needs at least `sx` tile edges and the base of
    length `y` needs at least `sy`, then the boundary supports at least
    `2*sx + sy - 2` tiles after the two base-corner tiles are counted once.
    Beeson then counts boundary gaps.  This check is kept as a diagnostic; the
    current promoted `N=56` certificate uses the stronger fact that the
    Lemma 11.14 enumeration has no candidate at all.
    """
    x_terms = min_representation_terms(x, sides)
    y_terms = min_representation_terms(y, sides)
    if x_terms is None or y_terms is None:
        return 0, False
    boundary_tiles = 2 * x_terms + y_terms - 2
    return boundary_tiles, boundary_tiles + (boundary_tiles - 2) > n


def candidates_for_n(n: int) -> tuple[BoundaryCandidate, ...]:
    """Return Lemma 11.14 boundary-arithmetic candidates for `N=n`."""
    out: list[BoundaryCandidate] = []
    n_squarefree = squarefree_part(n)
    for m in range(2, strict_m_bound(n) + 1):
        for k in range(1, m):
            if 2 * k <= m or gcd(k, m) != 1:
                continue
            sides = (k * k, m * m - k * k, m * k)
            a, b, c = sides
            if not is_triangle(sides):
                continue
            if squarefree_part(b) != n_squarefree:
                continue
            x = integer_square_root(n * a * b)
            if x is None:
                continue
            if (c * x) % a != 0:
                continue
            y = c * x // a
            if x * y != n * b * c:
                continue
            x_reps = side_representations(
                x,
                sides,
                max_tiles_exclusive_times4=n + 1,
                require_qr=True,
            )
            if not x_reps:
                continue
            y_reps = side_representations(y, sides)
            if not y_reps:
                continue
            boundary_tiles, count_obstructed = boundary_count_obstructed(n, x, y, sides)
            out.append(
                BoundaryCandidate(
                    n=n,
                    tile=sides,
                    x=x,
                    y=y,
                    x_representations=x_reps,
                    y_representations=y_reps,
                    min_boundary_tiles=boundary_tiles,
                    boundary_count_obstructed=count_obstructed,
                )
            )
    return tuple(out)


def survivors_for_n(n: int) -> tuple[BoundaryCandidate, ...]:
    return tuple(row for row in candidates_for_n(n) if not row.boundary_count_obstructed)


def base_representation_obstructed(rep: Triple) -> bool:
    """Beeson-style base endpoint obstruction for `gamma=2alpha`.

    On the base `AC`, both outer corners are alpha angles.  If the base has no
    `c` edges, then the first and last edges must be `b` edges using their alpha
    endpoints.  Starting from the left corner, avoiding a forbidden gamma-gamma
    straight boundary point forces every `a`/`b` edge to end at gamma, so the
    right corner cannot be alpha.  The case with no `b` edges is the analogous
    beta-beta argument for `a`/`c` edges.
    """
    _u, v, w = rep
    return v == 0 or w == 0


def c_edge_lower_bound_applies(sides: Triple) -> bool:
    """Whether Beeson's two-`c` boundary-edge lemma applies.

    The lemma applies when `gamma > pi/2`, `alpha/pi` is irrational, and every
    outer angle is less than `gamma`.  In the `gamma=2alpha` isosceles branch,
    `gamma > pi/2` also makes the apex angle `pi-2alpha` less than `gamma`;
    the base angles are `alpha < gamma`.
    """
    a, b, c = sides
    if c * c <= a * a + b * b:
        return False

    # cos(alpha) is rational for integer sides.  Niven's theorem rules out a
    # rational multiple of pi unless this rational cosine is 0, +/-1/2, or +/-1.
    numerator = b * b + c * c - a * a
    denominator = 2 * b * c
    return 2 * numerator not in {
        -2 * denominator,
        -denominator,
        0,
        denominator,
        2 * denominator,
    }


def lemma_1117_obstructed(candidate: BoundaryCandidate, y_rep: Triple) -> bool:
    """Return whether Beeson Lemma 11.17 eliminates this base representation.

    The lemma applies when both equal sides have exactly one `c` edge and the
    base has one or two `c` edges.  We only use it when every allowed short
    `X` representation has one `c`; otherwise the other equal side might use a
    two-`c` representation not covered by the lemma.
    """
    return all(rep[2] == 1 for rep in candidate.x_representations) and y_rep[2] in {1, 2}


def viable_x_representations(candidate: BoundaryCandidate) -> tuple[Triple, ...]:
    reps = candidate.x_representations
    if c_edge_lower_bound_applies(candidate.tile):
        reps = tuple(rep for rep in reps if rep[2] >= 2)
    return reps


def viable_free_x_representations(candidate: BoundaryCandidate) -> tuple[Triple, ...]:
    reps = side_representations(candidate.x, candidate.tile, require_qr=True)
    if c_edge_lower_bound_applies(candidate.tile):
        reps = tuple(rep for rep in reps if rep[2] >= 2)
    return reps


def boundary_c_parity_obstructed(candidate: BoundaryCandidate, y_rep: Triple) -> bool:
    """Every interior `c` edge is counted twice, so `N - boundary_c` is even."""
    bounded = viable_x_representations(candidate)
    free = viable_free_x_representations(candidate)
    if not bounded or not free:
        return True
    return not any(
        (candidate.n - short[2] - other[2] - y_rep[2]) % 2 == 0
        for short in bounded
        for other in free
    )


def refined_surviving_y_representations(candidate: BoundaryCandidate) -> tuple[Triple, ...]:
    """Surviving base reps after the local base lemma and Lemma 11.17.

    This intentionally does not use the stricter side-label fan automaton:
    in non-edge-to-edge tilings, overhangs can emanate from an outer-boundary
    transition along interior rays.  The fan automaton remains diagnostic until
    that overhang case is ruled out.
    """
    out: list[Triple] = []
    if not viable_x_representations(candidate) or not viable_free_x_representations(candidate):
        return tuple(out)
    for rep in candidate.y_representations:
        if base_representation_obstructed(rep):
            continue
        if c_edge_lower_bound_applies(candidate.tile) and rep[2] < 2:
            continue
        if lemma_1117_obstructed(candidate, rep):
            continue
        if boundary_c_parity_obstructed(candidate, rep):
            continue
        out.append(rep)
    return tuple(out)


def refined_survivors_for_n(n: int) -> tuple[RefinedGamma2AlphaSurvivor, ...]:
    out: list[RefinedGamma2AlphaSurvivor] = []
    for candidate in survivors_for_n(n):
        y_reps = refined_surviving_y_representations(candidate)
        if y_reps:
            out.append(RefinedGamma2AlphaSurvivor(candidate, y_reps))
    return tuple(out)


def format_reps(reps: tuple[Triple, ...], limit: int = 4) -> str:
    text = ", ".join(f"{p}a+{q}b+{r}c" for p, q, r in reps[:limit])
    if len(reps) > limit:
        text += ", ..."
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    args = parser.parse_args()

    for n in args.n:
        rows = candidates_for_n(n)
        survivors = survivors_for_n(n)
        refined = refined_survivors_for_n(n)
        print(
            f"N={n}: {len(rows)} gamma=2alpha boundary candidate(s), "
            f"{len(survivors)} after boundary-count obstruction, "
            f"{len(refined)} after refined local obstructions"
        )
        for row in rows:
            status = "obstructed" if row.boundary_count_obstructed else "survives"
            print(
                f"  tile={row.tile}, X={row.x}, Y={row.y}, "
                f"min_boundary_tiles={row.min_boundary_tiles}, {status}"
            )
            print(f"    X reps: {format_reps(row.x_representations)}")
            viable_x = viable_x_representations(row)
            if viable_x != row.x_representations:
                print(f"    viable X reps after c-edge lower bound: {format_reps(viable_x)}")
            print(f"    Y reps: {format_reps(row.y_representations)}")
            refined_y = refined_surviving_y_representations(row)
            if refined_y:
                print(f"    refined Y survivors: {format_reps(refined_y)}")
            elif not row.boundary_count_obstructed:
                print(
                    "    refined obstruction: c-edge lower bound, base endpoint lemma, "
                    "boundary c-parity, and Beeson Lemma 11.17"
                )


if __name__ == "__main__":
    main()
