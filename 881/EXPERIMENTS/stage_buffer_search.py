#!/usr/bin/env python3
"""Search for buffered finite stages in the k=2 counterexample criterion.

The stage criterion in PROOF.md asks for a finite extension A_old -> A
with a declared endpoint Ns such that:

  * [N+1, Ns] is contained in 2A;
  * every new element a has a witness w in [N+1, Ns] not in 3(A\\{a});
  * the witness is above the first padding range, so w-min(old) is in the
    old two-sum coverage window rather than below it;
  * for iteration, it is useful if 2A actually covers beyond Ns.

This script searches small finite examples with an explicit buffer
`newcov > Ns`. It is a toy model only: positive output is not an infinite
construction, and negative output is only within the searched bounds.
"""

from __future__ import annotations

from itertools import combinations


def sumset(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def cover_end(two_sums: set[int], start: int, cap: int) -> int:
    x = start
    while x <= cap and x in two_sums:
        x += 1
    return x - 1


def witnesses(
    elements: set[int],
    new_elements: set[int],
    base: int,
    previous_endpoint: int,
    declared_endpoint: int,
    cap: int,
) -> dict[int, list[int]] | None:
    two_sums = sumset(elements, 2, cap)
    result: dict[int, list[int]] = {}
    retained_old = elements - new_elements
    min_retained = min(retained_old) if retained_old else min(elements)
    for a in sorted(new_elements):
        three_without_a = sumset(elements - {a}, 3, cap)
        found = [
            w
            for w in range(previous_endpoint + 1, declared_endpoint + 1)
            if w - min_retained >= base
            if w in two_sums and w not in three_without_a
        ]
        if not found:
            return None
        result[a] = found
    return result


def old_intervals(elements: set[int], cap: int) -> list[tuple[int, int]]:
    two_sums = sumset(elements, 2, cap)
    intervals: list[tuple[int, int]] = []
    start = None
    previous = None
    for x in range(1, cap + 1):
        if x in two_sums:
            if start is None:
                start = previous = x
            elif previous is not None and x == previous + 1:
                previous = x
            else:
                intervals.append((start, previous))
                start = previous = x
        elif start is not None:
            intervals.append((start, previous))
            start = previous = None
    if start is not None:
        intervals.append((start, previous))
    return intervals


def main() -> None:
    max_old = 10
    max_old_size = 5
    max_new_size = 3
    slack = 12

    for old_max in range(5, max_old + 1):
        universe = range(1, old_max + 1)
        for old_size in range(3, min(old_max, max_old_size) + 1):
            for old_tuple in combinations(universe, old_size):
                old = set(old_tuple)
                cap0 = 4 * old_max + 30
                for base, oldcov in old_intervals(old, cap0):
                    if oldcov - base + 1 < 4:
                        continue
                    for previous_endpoint in range(base, oldcov):
                        candidates = [
                            x
                            for x in range(previous_endpoint + 1, oldcov + slack + 1)
                            if x not in old
                        ]
                        for new_size in range(1, max_new_size + 1):
                            for new_tuple in combinations(candidates, new_size):
                                new = set(new_tuple)
                                elements = old | new
                                cap = max(4 * max(elements) + 50, oldcov + 80)
                                two_sums = sumset(elements, 2, cap)
                                newcov = cover_end(two_sums, base, cap)
                                if newcov <= oldcov:
                                    continue

                                first_declared = max(
                                    previous_endpoint + 1, max(new)
                                )
                                for declared in range(first_declared, newcov):
                                    found = witnesses(
                                        elements,
                                        new,
                                        base,
                                        previous_endpoint,
                                        declared,
                                        cap,
                                    )
                                    if found is None:
                                        continue
                                    print("found buffered stage")
                                    print(
                                        "old=", sorted(old),
                                        "base=", base,
                                        "oldcov=", oldcov,
                                        "N=", previous_endpoint,
                                    )
                                    print(
                                        "new=", sorted(new),
                                        "Ns=", declared,
                                        "newcov=", newcov,
                                    )
                                    print(
                                        "witnesses=",
                                        {a: found[a][:5] for a in sorted(found)},
                                    )
                                    return
    print("no buffered stage within searched bounds")


if __name__ == "__main__":
    main()
