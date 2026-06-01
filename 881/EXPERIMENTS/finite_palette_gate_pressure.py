#!/usr/bin/env python3
"""Finite checker for Lemmas 16.41, 16.46, and 16.48.

The lemma says that if a gate packet U satisfies

    (U + f - U) intersect A is contained in F,

then every anchored shadow f + U - u0 contains at most |F| points of A.
If, in addition, f and U lie in one interval I contained in A, then
|U| <= 2|F|.
If f lies just outside such an interval, at distance delta, then
|U| <= delta + |F|.

This script exhaustively checks small finite universes after generating all
sets A that contain a fixed palette F and a retained packet U.
"""

from __future__ import annotations

from itertools import combinations


def powerset(values: list[int]):
    for size in range(len(values) + 1):
        yield from combinations(values, size)


def check_instance(
    universe: range,
    f: int,
    F: set[int],
    U: set[int],
    interval: range | None = None,
) -> tuple[int, int]:
    assert f in F
    assert F.isdisjoint(U)
    interval_set = set(interval or [])
    if interval is not None:
        assert U <= interval_set

    forced = set(F) | set(U) | interval_set
    optional = [x for x in universe if x not in forced]
    checked = 0
    admissible = 0

    for extra_tuple in powerset(optional):
        A = set(forced) | set(extra_tuple)
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
        if interval is not None:
            lo = min(interval_set)
            hi = max(interval_set)
            if f in interval_set:
                bound = 2 * len(F)
                label = "same-interval"
            elif f < lo:
                bound = lo - f + len(F)
                label = "below-interval"
            elif f > hi:
                bound = f - hi + len(F)
                label = "above-interval"
            else:
                raise AssertionError("unexpected interval relation")
            if len(U) > bound:
                raise AssertionError(
                    f"{label} counterexample: A={sorted(A)}, F={sorted(F)}, "
                    f"U={sorted(U)}, interval={list(interval)}, bound={bound}"
                )

    return checked, admissible


def main() -> None:
    cases: list[tuple[range, int, set[int], set[int], range | None]] = [
        (range(1, 13), 2, {2}, {7, 8, 10}, None),
        (range(1, 16), 3, {3, 5}, {9, 11, 14}, None),
        (range(1, 18), 4, {1, 4, 6}, {10, 12, 15, 16}, None),
        (range(1, 7), 1, {1, 2}, {3, 4}, range(1, 5)),
        (range(1, 9), 1, {1}, {4, 5, 6}, range(4, 7)),
        (range(1, 10), 8, {8}, {3, 4, 5}, range(3, 6)),
        (range(1, 13), 2, {2}, {4, 6, 9}, range(2, 10)),
        (range(1, 16), 3, {3, 5}, {6, 9, 12, 14}, range(3, 15)),
    ]

    total_checked = 0
    total_admissible = 0
    for universe, f, F, U, interval in cases:
        checked, admissible = check_instance(universe, f, F, U, interval)
        total_checked += checked
        total_admissible += admissible
        print(
            "case",
            f"f={f}",
            f"F={sorted(F)}",
            f"U={sorted(U)}",
            f"interval={list(interval) if interval is not None else None}",
            f"checked={checked}",
            f"admissible={admissible}",
        )

    print("finite-palette gate pressure check passed")
    print("total_checked=", total_checked)
    print("total_admissible=", total_admissible)


if __name__ == "__main__":
    main()
