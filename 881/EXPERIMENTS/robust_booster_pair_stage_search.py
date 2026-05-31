#!/usr/bin/env python3
"""Cross-stage pair-barrier search for the k=3 robust booster seed.

This tests the stage criterion:

  * A_s = C_s union {5} is a 3-basis on the declared interval;
  * every old-new pair {a,b}, a in C_{s-1}, b in P_s, has a witness
    w <= N_s with w notin 4(A_s\\{a,b});
  * a two-point post-endpoint buffer is left for iteration.

If such stages could be iterated with N_s -> infinity, the final set would
be an order-3 basis and no infinite deletion would remain an order-4 basis.
The search is finite evidence only.
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


def pair_witnesses(
    old: set[int],
    new: set[int],
    previous_endpoint: int,
    declared_endpoint: int,
    cap: int,
) -> dict[tuple[int, int], list[int]] | None:
    A = old | new | {BOOSTER}
    four_all = hsum(A, 4, cap)
    result: dict[tuple[int, int], list[int]] = {}
    for a in sorted(old):
        for b in sorted(new):
            without = hsum(A - {a, b}, 4, cap)
            found = [
                w
                for w in range(previous_endpoint + 1, declared_endpoint + 1)
                if w in four_all and w not in without
            ]
            if not found:
                return None
            result[(a, b)] = found[:5]
    return result


def find_one_stage(
    old: set[int],
    previous_endpoint: int,
    base: int,
    slack: int = 100,
    max_new_size: int = 4,
) -> tuple[set[int], int, int, dict[tuple[int, int], list[int]]] | None:
    A_old = old | {BOOSTER}
    cap0 = max(6 * max(A_old) + 200, previous_endpoint + 200)
    oldcov = cover_end(hsum(A_old, 3, cap0), base, cap0)
    candidates = [
        x
        for x in range(previous_endpoint + 1, oldcov + slack + 1)
        if x % MODULUS in RESIDUES and x not in old and x != BOOSTER
    ]
    for new_size in range(1, max_new_size + 1):
        for new_tuple in combinations(candidates, new_size):
            new = set(new_tuple)
            A = old | new | {BOOSTER}
            cap = max(6 * max(A) + 200, oldcov + slack + 200)
            newcov = cover_end(hsum(A, 3, cap), base, cap)
            if newcov <= previous_endpoint:
                continue
            first_declared = max(previous_endpoint + 1, max(new))
            # Leave the two-point buffer required for order-3 coverage.
            for declared in range(first_declared, max(first_declared, newcov - 1)):
                witnesses = pair_witnesses(
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
    C = {1, 3, 20, 21}
    base = 22
    endpoint = 22
    print("start", "C=", sorted(C), "booster=", BOOSTER, "base=", base, "endpoint=", endpoint)
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
            "pairs=", len(witnesses),
            "sample=", list(witnesses.items())[:6],
        )
        C |= new
        endpoint = declared


def extended_third_stage_check() -> None:
    """Reproduce a bounded check after the two printed greedy stages."""

    random.seed(881)
    old = {1, 3, 20, 21, 23, 30, 31}
    previous_endpoint = 40
    base = 22
    candidates = [
        x
        for x in range(previous_endpoint + 1, 201)
        if x % MODULUS in RESIDUES and x not in old and x != BOOSTER
    ]

    def check(new_tuple: tuple[int, ...]) -> tuple[int, int, int] | None:
        new = set(new_tuple)
        A = old | new | {BOOSTER}
        cap = max(500, 6 * max(A) + 200)
        newcov = cover_end(hsum(A, 3, cap), base, cap)
        if newcov <= previous_endpoint or max(new) > newcov - 2:
            return None
        for declared in range(max(previous_endpoint + 1, max(new)), newcov - 1):
            witnesses = pair_witnesses(old, new, previous_endpoint, declared, cap)
            if witnesses is not None:
                return declared, newcov, len(witnesses)
        return None

    for limit in (80, 120, 160):
        bounded = [x for x in candidates if x <= limit]
        for size in range(1, 5):
            count = 0
            for new_tuple in combinations(bounded, size):
                count += 1
                result = check(new_tuple)
                if result is not None:
                    print("found exhaustive", "limit=", limit, "new=", new_tuple, "result=", result)
                    return
            print("checked", "limit=", limit, "size=", size, "count=", count)

    for size in range(5, 13):
        for _ in range(3000):
            new_tuple = tuple(sorted(random.sample(candidates, size)))
            result = check(new_tuple)
            if result is not None:
                print("found random", "size=", size, "new=", new_tuple, "result=", result)
                return
        print("checked random", "size=", size, "trials=", 3000)

    print("no third-stage extension found in extended bounded/random search")


if __name__ == "__main__":
    if "--extend" in sys.argv:
        extended_third_stage_check()
    else:
        main()
