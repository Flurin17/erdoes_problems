#!/usr/bin/env python3
"""Finite checker for Lemma 16.41.

The lemma says that if a gate packet U satisfies

    (U + f - U) intersect A is contained in F,

then every anchored shadow f + U - u0 contains at most |F| points of A.

This script exhaustively checks small finite universes after generating all
sets A that contain a fixed palette F and a retained packet U.
"""

from __future__ import annotations

from itertools import combinations


def powerset(values: list[int]):
    for size in range(len(values) + 1):
        yield from combinations(values, size)


def check_instance(universe: range, f: int, F: set[int], U: set[int]) -> tuple[int, int]:
    assert f in F
    assert F.isdisjoint(U)

    optional = [x for x in universe if x not in F and x not in U]
    checked = 0
    admissible = 0

    for extra_tuple in powerset(optional):
        A = set(F) | set(U) | set(extra_tuple)
        checked += 1

        gate_shadow = {u + f - v for u in U for v in U}
        if not (gate_shadow & A) <= F:
            continue

        admissible += 1
        for u0 in U:
            anchored = {f + u - u0 for u in U}
            if len(anchored & A) > len(F):
                raise AssertionError(
                    f"counterexample: A={sorted(A)}, F={sorted(F)}, "
                    f"U={sorted(U)}, anchor={u0}, shadow={sorted(anchored & A)}"
                )

    return checked, admissible


def main() -> None:
    cases = [
        (range(1, 13), 2, {2}, {7, 8, 10}),
        (range(1, 16), 3, {3, 5}, {9, 11, 14}),
        (range(1, 18), 4, {1, 4, 6}, {10, 12, 15, 16}),
    ]

    total_checked = 0
    total_admissible = 0
    for universe, f, F, U in cases:
        checked, admissible = check_instance(universe, f, F, U)
        total_checked += checked
        total_admissible += admissible
        print(
            "case",
            f"f={f}",
            f"F={sorted(F)}",
            f"U={sorted(U)}",
            f"checked={checked}",
            f"admissible={admissible}",
        )

    print("finite-palette gate pressure check passed")
    print("total_checked=", total_checked)
    print("total_admissible=", total_admissible)


if __name__ == "__main__":
    main()
