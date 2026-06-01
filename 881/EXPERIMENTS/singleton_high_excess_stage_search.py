#!/usr/bin/env python3
"""Search the Lemma 16.9 singleton-high-excess target for k=3.

A stage adds a block P to A_old, extends 3-sum coverage with the two-point
buffer, and every new b in P has a singleton order-4 private witness

    w notin 4(A\\{b}),      w - b - 2 * min(A) >= max(A).

The second condition makes the Lemma 16.9 terminal gap vacuous on the
current finite stage.  The script is a finite diagnostic only.
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


def find_extension(
    old: set[int],
    base: int,
    previous_endpoint: int,
    slack: int = 200,
    max_new_size: int = 3,
    max_candidate: int = 150,
) -> tuple[tuple[int, ...], int, int, int, dict[int, list[int]]] | None:
    cap0 = max(6 * max(old) + 200, previous_endpoint + 200)
    oldcov = cover_end(hsum(old, 3, cap0), base, cap0)
    candidates = [
        x
        for x in range(previous_endpoint + 1, min(max_candidate, oldcov + slack) + 1)
        if x not in old
    ]
    for size in range(1, max_new_size + 1):
        checked = 0
        for new_tuple in combinations(candidates, size):
            checked += 1
            new = set(new_tuple)
            elements = old | new
            cap = max(6 * max(elements) + 300, oldcov + slack + 300)
            newcov = cover_end(hsum(elements, 3, cap), base, cap)
            last_declared = newcov - 2 * min(elements)
            if last_declared < max(previous_endpoint + 1, max(new)):
                continue
            four_all = hsum(elements, 4, cap)
            for declared in range(max(previous_endpoint + 1, max(new)), last_declared + 1):
                witnesses: dict[int, list[int]] = {}
                ok = True
                for b in sorted(new):
                    without = hsum(elements - {b}, 4, cap)
                    found = [
                        w
                        for w in range(previous_endpoint + 1, declared + 1)
                        if w in four_all
                        and w not in without
                        and w - b - 2 * min(elements) >= max(elements)
                    ]
                    if not found:
                        ok = False
                        break
                    witnesses[b] = found[:3]
                if ok:
                    print("checked size", size, "count", checked)
                    return new_tuple, declared, newcov, oldcov, witnesses
        print("checked size", size, "count", checked)
    return None


def greedy_chain() -> None:
    old = {1, 2, 3, 4}
    base = 3
    endpoint = 4
    for step in range(1, 6):
        found = find_extension(old, base, endpoint)
        print("step", step, "old=", sorted(old), "endpoint=", endpoint, "found=", found)
        if found is None:
            return
        new, declared, _, _, _ = found
        old |= set(new)
        endpoint = declared


if __name__ == "__main__":
    greedy_chain()
