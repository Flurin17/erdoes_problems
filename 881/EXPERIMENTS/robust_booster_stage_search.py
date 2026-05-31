#!/usr/bin/env python3
"""Finite-stage search for lifting the robust k=3 residue booster.

The residue seed is S={0,1,3} and booster f=5 modulo 10.  This script keeps
f fixed and searches for finite stages C_s whose elements lie in those
residue classes.  The target stage property is:

  * [N+1, Ns] is contained in 3(C_s union {f});
  * every new c has a witness w<=Ns with
        w notin 4((C_s union {f})\\{c});
  * future stages can be placed above Ns, so witnesses below Ns freeze.

This is a finite analogue only.  It tests the single-integer privacy issue
that a thick residue lift does not solve.
"""

from __future__ import annotations

import random
import sys
from itertools import combinations


BOOSTER = 5
RESIDUES = {0, 1, 3}
MODULUS = 10


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


def find_one_stage(
    C: set[int],
    previous_endpoint: int,
    base: int,
    slack: int = 80,
    max_new_size: int = 4,
) -> tuple[set[int], int, int, dict[int, list[int]]] | None:
    A_old = C | {BOOSTER}
    cap0 = max(6 * max(A_old) + 200, previous_endpoint + 200)
    oldcov = cover_end(hsum(A_old, 3, cap0), base, cap0)
    candidates = [
        x
        for x in range(previous_endpoint + 1, oldcov + slack + 1)
        if x % MODULUS in RESIDUES and x not in C and x != BOOSTER
    ]
    for new_size in range(1, max_new_size + 1):
        for new_tuple in combinations(candidates, new_size):
            new = set(new_tuple)
            A = C | new | {BOOSTER}
            cap = max(6 * max(A) + 200, oldcov + slack + 200)
            newcov = cover_end(hsum(A, 3, cap), base, cap)
            if newcov <= previous_endpoint:
                continue
            first_declared = max(previous_endpoint + 1, max(new))
            # Lemma 13.1d with min element 1 asks for a two-point buffer.
            for declared in range(first_declared, max(first_declared, newcov - 1)):
                witnesses: dict[int, list[int]] = {}
                ok = True
                four_all = hsum(A, 4, cap)
                for c in sorted(new):
                    without = hsum(A - {c}, 4, cap)
                    found = [
                        w
                        for w in range(previous_endpoint + 1, declared + 1)
                        if w in four_all
                        if w not in without
                    ]
                    if not found:
                        ok = False
                        break
                    witnesses[c] = found[:5]
                if ok:
                    return new, declared, newcov, witnesses
    return None


def main() -> None:
    # A small seed found by bounded search.  With the booster, 3A covers
    # [22,31].  The first extension below has genuine four-sum private
    # witnesses for both new elements and leaves a two-point buffer.
    C = {1, 3, 20, 21}
    base = 22
    endpoint = 22
    print(
        "start",
        "C=", sorted(C),
        "booster=", BOOSTER,
        "base=", base,
        "endpoint=", endpoint,
    )

    for step in range(1, 8):
        found = find_one_stage(C, endpoint, base)
        if found is None:
            print("stalled", "step=", step, "C=", sorted(C), "endpoint=", endpoint)
            return
        new, declared, newcov, witnesses = found
        print(
            "stage=", step,
            "new=", sorted(new),
            "endpoint=", declared,
            "coverage=", newcov,
            "witnesses=", witnesses,
        )
        C |= new
        endpoint = declared


def extended_second_stage_check() -> None:
    """Reproduce the bounded search after the first printed stage."""

    random.seed(881)
    C = {1, 3, 20, 21, 30, 31}
    previous_endpoint = 38
    base = 22
    candidates = [
        x
        for x in range(previous_endpoint + 1, 181)
        if x % MODULUS in RESIDUES and x not in C and x != BOOSTER
    ]

    def check(new_tuple: tuple[int, ...]) -> tuple[int, int, dict[int, list[int]]] | None:
        new = set(new_tuple)
        A = C | new | {BOOSTER}
        cap = max(400, 6 * max(A) + 100)
        newcov = cover_end(hsum(A, 3, cap), base, cap)
        if newcov <= previous_endpoint or max(new) > newcov - 2:
            return None
        four_all = hsum(A, 4, cap)
        withouts = {c: hsum(A - {c}, 4, cap) for c in new}
        for declared in range(max(previous_endpoint + 1, max(new)), newcov - 1):
            witnesses: dict[int, list[int]] = {}
            for c in sorted(new):
                found = [
                    w
                    for w in range(previous_endpoint + 1, declared + 1)
                    if w in four_all and w not in withouts[c]
                ]
                if not found:
                    break
                witnesses[c] = found[:3]
            else:
                return declared, newcov, witnesses
        return None

    for limit in (80, 120):
        bounded = [x for x in candidates if x <= limit]
        for size in range(1, 6):
            count = 0
            for new_tuple in combinations(bounded, size):
                count += 1
                result = check(new_tuple)
                if result is not None:
                    print("found exhaustive", "limit=", limit, "new=", new_tuple, "result=", result)
                    return
            print("checked", "limit=", limit, "size=", size, "count=", count)

    for size in range(6, 13):
        for _ in range(5000):
            new_tuple = tuple(sorted(random.sample(candidates, size)))
            result = check(new_tuple)
            if result is not None:
                print("found random", "size=", size, "new=", new_tuple, "result=", result)
                return
        print("checked random", "size=", size, "trials=", 5000)

    print("no second-stage extension found in extended bounded/random search")


if __name__ == "__main__":
    if "--extend" in sys.argv:
        extended_second_stage_check()
    else:
        main()
