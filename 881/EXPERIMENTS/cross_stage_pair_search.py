#!/usr/bin/env python3
"""Search finite stages for the cross-stage pair-barrier criterion.

Proposition 13.1c in PROOF.md would give a k=2 counterexample if one could
build stages where every old-new pair has a local order-3-private witness
below the new endpoint. This script searches small finite stages for that
local condition.

The search finds short initial chains, but the greedy chain currently stalls
quickly. This is only finite evidence; it is not a proof of impossibility.

By default this script requires the declared endpoint to be at least the
largest new element. Proposition 13.1c does not formally require that:
elements above the declared endpoint are dormant for that stage. The default
is aimed at genuinely local old-new pair witnesses rather than witnesses
that ignore a too-large new element and collapse to old singleton privacy.
"""

from __future__ import annotations

from itertools import combinations


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def cover_end(elements: set[int], start: int, cap: int) -> int:
    two_sums = hsum(elements, 2, cap)
    x = start
    while x <= cap and x in two_sums:
        x += 1
    return x - 1


def cross_pair_witnesses(
    old: set[int],
    new: set[int],
    previous_endpoint: int,
    declared_endpoint: int,
    cap: int,
) -> dict[tuple[int, int], list[int]] | None:
    elements = old | new
    two_sums = hsum(elements, 2, cap)
    result: dict[tuple[int, int], list[int]] = {}
    for a in sorted(old):
        for b in sorted(new):
            three_without_pair = hsum(elements - {a, b}, 3, cap)
            witnesses = [
                w
                for w in range(previous_endpoint + 1, declared_endpoint + 1)
                if w in two_sums and w not in three_without_pair
            ]
            if not witnesses:
                return None
            result[(a, b)] = witnesses[:3]
    return result


def find_next_stage(
    old: set[int],
    previous_endpoint: int,
    base: int,
    slack: int,
    max_new_size: int,
) -> tuple[set[int], int, int, dict[tuple[int, int], list[int]]] | None:
    oldcov = cover_end(old, base, 10_000)
    candidates = [
        x
        for x in range(previous_endpoint + 1, oldcov + slack + 1)
        if x not in old
    ]
    for new_size in range(1, max_new_size + 1):
        for new_tuple in combinations(candidates, new_size):
            new = set(new_tuple)
            elements = old | new
            cap = max(4 * max(elements) + 100, oldcov + 200)
            newcov = cover_end(elements, base, cap)
            if newcov <= previous_endpoint:
                continue
            first_declared = max(previous_endpoint + 1, max(new))
            for declared in range(first_declared, newcov + 1):
                witnesses = cross_pair_witnesses(
                    old,
                    new,
                    previous_endpoint,
                    declared,
                    cap,
                )
                if witnesses is not None:
                    return new, declared, newcov, witnesses
    return None


def main() -> None:
    elements = {1, 2}
    endpoint = 2
    base = 2

    for step in range(1, 8):
        found = find_next_stage(
            elements,
            endpoint,
            base=base,
            slack=40,
            max_new_size=5,
        )
        if found is None:
            print(
                "stalled",
                "step=", step,
                "A=", sorted(elements),
                "endpoint=", endpoint,
                "coverage=", cover_end(elements, base, 10_000),
            )
            return
        new, declared, newcov, witnesses = found
        print(
            "stage=", step,
            "new=", sorted(new),
            "endpoint=", declared,
            "coverage=", newcov,
            "pairs=", len(witnesses),
            "sample=", list(witnesses.items())[:5],
        )
        elements |= new
        endpoint = declared


if __name__ == "__main__":
    main()
