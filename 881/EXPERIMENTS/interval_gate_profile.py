#!/usr/bin/env python3
"""Finite checks for the interval gate-distance profile.

For an interval I=[a,b], a deletion set F inside I with |F|<=r, and an
integer gate f, the retained interval core C=I\\F has a central two-sum band.
Thus the rows

    U_f = {u in I\\F : f+u not in 2C}

must be controlled by the distance from f to the central gate range
[a+2r, b-2r].  This is the interval-only version of Corollary 16.59 before
adding the bounded row-dependent allowance.
"""

from __future__ import annotations

from itertools import combinations


def interval(a: int, b: int) -> set[int]:
    return set(range(a, b + 1))


def two_sums(values: set[int]) -> set[int]:
    return {x + y for x in values for y in values}


def central_gate_distance(a: int, b: int, r: int, gate: int) -> int:
    return max(0, a + 2 * r - gate, gate - b + 2 * r)


def check_case(a: int, b: int, r: int, margin: int) -> dict[str, int]:
    I = interval(a, b)
    n = b - a + 1
    if n <= 2 * r:
        raise ValueError("interval must have length > 2r")

    checked = 0
    max_gap = 0
    worst: tuple[int, tuple[int, ...], int, int, int] | None = None

    for size in range(r + 1):
        for deletion in combinations(sorted(I), size):
            F = set(deletion)
            C = I - F
            sums = two_sums(C)
            for gate in range(a - margin, b + margin + 1):
                rows = {u for u in C if gate + u not in sums}
                D = central_gate_distance(a, b, r, gate)
                bound = 2 * D
                checked += 1
                if len(rows) > bound:
                    raise AssertionError(
                        {
                            "interval": [a, b],
                            "r": r,
                            "gate": gate,
                            "deletion": deletion,
                            "rows": sorted(rows),
                            "bound": bound,
                        }
                    )
                gap = bound - len(rows)
                if gap > max_gap:
                    max_gap = gap
                    worst = (gate, deletion, len(rows), bound, gap)

    print(
        f"case I=[{a},{b}] r={r} margin={margin} "
        f"checked={checked} max_slack={max_gap} worst={worst}"
    )
    return {"checked": checked, "max_slack": max_gap}


def main() -> None:
    cases = [
        (1, 8, 1, 12),
        (1, 12, 2, 18),
        (10, 25, 3, 24),
        (100, 124, 4, 32),
    ]
    total = 0
    for case in cases:
        total += check_case(*case)["checked"]
    print("interval gate-distance profile check passed")
    print("total_checked=", total)


if __name__ == "__main__":
    main()
