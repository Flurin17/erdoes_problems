#!/usr/bin/env python3
"""Search follow-up protection for the prepared row-bank marker stage.

Diagnostic 16.12 gives a prepared singleton-high-excess witness for b=33
using fillers 19, 20, and 28.  This script asks whether those fillers, or
the marker itself, can be protected in the next bounded stage by adjoining a
small block.
"""

from __future__ import annotations

from itertools import combinations


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def cover_end(values: set[int], start: int, cap: int) -> int:
    x = start
    while x <= cap and x in values:
        x += 1
    return x - 1


def find_protection(
    A: set[int],
    base: int,
    previous_endpoint: int,
    target: int,
    max_new_size: int = 3,
    max_candidate: int = 180,
    slack: int = 120,
    strict_high_excess: bool = False,
) -> tuple[tuple[int, ...], int, int, int, list[int]] | None:
    cap0 = max(6 * max(A) + 200, previous_endpoint + 200)
    oldcov = cover_end(hsum(A, 3, cap0), base, cap0)
    candidates = [
        x
        for x in range(previous_endpoint + 1, min(max_candidate, oldcov + slack) + 1)
        if x not in A
    ]
    for size in range(0, max_new_size + 1):
        checked = 0
        iterator = [()] if size == 0 else combinations(candidates, size)
        for new_tuple in iterator:
            checked += 1
            elements = A | set(new_tuple)
            cap = max(7 * max(elements) + 500, oldcov + slack + 500)
            newcov = cover_end(hsum(elements, 3, cap), base, cap)
            last_declared = newcov - 2 * min(elements)
            if last_declared <= previous_endpoint:
                continue
            if new_tuple and last_declared < max(new_tuple):
                continue
            four_all = hsum(elements, 4, cap)
            without = hsum(elements - {target}, 4, cap)
            for declared in range(
                max(previous_endpoint + 1, max(new_tuple) if new_tuple else previous_endpoint + 1),
                last_declared + 1,
            ):
                witnesses = [
                    w
                    for w in range(previous_endpoint + 1, declared + 1)
                    if w in four_all
                    and w not in without
                    and (
                        not strict_high_excess
                        or w - target - 2 * min(elements) >= max(elements)
                    )
                ]
                if witnesses:
                    print("checked size", size, "count", checked)
                    return new_tuple, declared, newcov, oldcov, witnesses[:5]
        print("checked size", size, "count", checked)
    return None


def main() -> None:
    A = {1, 2, 3, 4, 8, 19, 20, 28, 33}
    base = 3
    previous_endpoint = 74
    for target in (19, 20, 28, 33, 8):
        print("target", target, "ordinary")
        print(find_protection(A, base, previous_endpoint, target))
        print("target", target, "strict_high_excess")
        print(
            find_protection(
                A,
                base,
                previous_endpoint,
                target,
                max_new_size=2,
                max_candidate=150,
                slack=80,
                strict_high_excess=True,
            )
        )


if __name__ == "__main__":
    main()
