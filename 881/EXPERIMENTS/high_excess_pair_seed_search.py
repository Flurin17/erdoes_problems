#!/usr/bin/env python3
"""Search for high-excess k=3 singleton pair stages.

This tests a construction-side escape from Corollary 16.4.  A singleton
new point b is required to have, for every old a, a pair witness w with

    w - b - 2 * min(A) >= max(old).

Then old retained padders do not enter the old-gate shadow interval.  The
diagnostic is finite only: positive output shows local compatibility, while
the greedy chain records how quickly the local pattern stalls.
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


def high_excess_witnesses(
    old: set[int],
    b: int,
    previous_endpoint: int,
    declared_endpoint: int,
    cap: int,
) -> dict[int, list[int]] | None:
    elements = old | {b}
    four_all = hsum(elements, 4, cap)
    result: dict[int, list[int]] = {}
    for a in sorted(old):
        without = hsum(elements - {a, b}, 4, cap)
        found = [
            w
            for w in range(previous_endpoint + 1, declared_endpoint + 1)
            if w in four_all
            and w not in without
            and w - b - 2 * min(elements) >= max(old)
        ]
        if not found:
            return None
        result[a] = found[:5]
    return result


def find_singleton_extension(
    old: set[int],
    base: int,
    previous_endpoint: int,
    slack: int,
) -> tuple[int, int, int, int, dict[int, list[int]]] | None:
    cap0 = max(5 * max(old) + 200, previous_endpoint + 200)
    oldcov = cover_end(hsum(old, 3, cap0), base, cap0)
    for b in range(previous_endpoint + 1, oldcov + slack + 1):
        if b in old:
            continue
        elements = old | {b}
        cap = max(5 * max(elements) + 300, oldcov + slack + 300)
        newcov = cover_end(hsum(elements, 3, cap), base, cap)
        last_declared = newcov - 2 * min(elements)
        if last_declared < max(previous_endpoint + 1, b):
            continue
        for declared in range(max(previous_endpoint + 1, b), last_declared + 1):
            witnesses = high_excess_witnesses(
                old,
                b,
                previous_endpoint,
                declared,
                cap,
            )
            if witnesses is not None:
                return b, declared, newcov, oldcov, witnesses
    return None


def find_first_seed() -> None:
    for max_old in range(6, 19):
        universe = range(1, max_old + 1)
        for size in range(3, min(8, max_old) + 1):
            for old_tuple in combinations(universe, size):
                old = set(old_tuple)
                if 1 not in old:
                    continue
                cap0 = 5 * max_old + 80
                old_sums = hsum(old, 3, cap0)
                starts = [
                    x
                    for x in range(3, cap0 + 1)
                    if x in old_sums and (x == 3 or x - 1 not in old_sums)
                ]
                for base in starts:
                    oldcov = cover_end(old_sums, base, cap0)
                    if oldcov - base < 8:
                        continue
                    for previous_endpoint in range(max(base, oldcov - 8), oldcov + 1):
                        found = find_singleton_extension(
                            old,
                            base,
                            previous_endpoint,
                            slack=80,
                        )
                        if found is None:
                            continue
                        b, declared, newcov, oldcov2, witnesses = found
                        print("first high-excess singleton seed")
                        print(
                            "old=",
                            sorted(old),
                            "base=",
                            base,
                            "oldcov=",
                            oldcov2,
                            "endpoint=",
                            previous_endpoint,
                        )
                        print("new=", b, "declared=", declared, "coverage=", newcov)
                        print("witnesses=", witnesses)
                        return
    print("no high-excess singleton seed within searched bounds")


def greedy_chain() -> None:
    old = {1, 2, 3, 4}
    base = 3
    endpoint = 4
    for step in range(1, 8):
        found = find_singleton_extension(old, base, endpoint, slack=200)
        if found is None:
            print("stalled", "step=", step, "old=", sorted(old), "endpoint=", endpoint)
            return
        b, declared, newcov, oldcov, witnesses = found
        print(
            "stage=",
            step,
            "old=",
            sorted(old),
            "oldcov=",
            oldcov,
            "new=",
            b,
            "endpoint=",
            declared,
            "coverage=",
            newcov,
            "sample=",
            {a: witnesses[a][:3] for a in sorted(witnesses)[:6]},
        )
        old.add(b)
        endpoint = declared


if __name__ == "__main__":
    find_first_seed()
    print()
    greedy_chain()
