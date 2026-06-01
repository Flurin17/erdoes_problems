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
    high_excess: bool = False,
) -> dict[tuple[int, int], list[int]] | None:
    A = old | new | {BOOSTER}
    m0 = min(A)
    four_all = hsum(A, 4, cap)
    result: dict[tuple[int, int], list[int]] = {}
    for a in sorted(old):
        for b in sorted(new):
            without = hsum(A - {a, b}, 4, cap)
            found = [
                w
                for w in range(previous_endpoint + 1, declared_endpoint + 1)
                if w in four_all and w not in without
                if not high_excess or w - b - 2 * m0 >= max(old)
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
    high_excess: bool = False,
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
                    high_excess=high_excess,
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


def diagnose_third_stage_failure() -> None:
    """Show which old-new pairs fail for feasible singleton next elements."""

    old = {1, 3, 20, 21, 23, 30, 31}
    previous_endpoint = 40
    base = 22
    for b in (41, 43, 50, 51, 53, 60, 61, 63):
        new = {b}
        A = old | new | {BOOSTER}
        cap = max(500, 6 * max(A) + 200)
        newcov = cover_end(hsum(A, 3, cap), base, cap)
        if newcov <= previous_endpoint or b > newcov - 2:
            print("b=", b, "coverage fail", "coverage=", newcov)
            continue
        four_all = hsum(A, 4, cap)
        failures = []
        successes: dict[int, list[int]] = {}
        for a in sorted(old):
            without = hsum(A - {a, b}, 4, cap)
            found = [
                w
                for w in range(previous_endpoint + 1, newcov - 1)
                if w in four_all and w not in without
            ]
            if found:
                successes[a] = found[:5]
            else:
                failures.append(a)
        print("b=", b, "coverage=", newcov, "fail_old=", failures, "successes=", successes)


def diagnose_high_excess_third_stage() -> None:
    """Check whether singleton next elements have high-excess pair witnesses."""

    old = {1, 3, 20, 21, 23, 30, 31}
    previous_endpoint = 40
    base = 22
    any_candidate = False
    for b in [
        x
        for x in range(previous_endpoint + 1, 261)
        if x % MODULUS in RESIDUES and x not in old and x != BOOSTER
    ]:
        new = {b}
        A = old | new | {BOOSTER}
        cap = max(700, 6 * max(A) + 200)
        newcov = cover_end(hsum(A, 3, cap), base, cap)
        if newcov <= previous_endpoint or b > newcov - 2:
            continue
        any_candidate = True
        four_all = hsum(A, 4, cap)
        successes: dict[int, list[int]] = {}
        for a in sorted(old):
            without = hsum(A - {a, b}, 4, cap)
            found = [
                w
                for w in range(previous_endpoint + 1, newcov - 1)
                if w in four_all
                and w not in without
                and w - b - 2 * min(A) >= max(old)
            ]
            if found:
                successes[a] = found[:5]
        print(
            "b=",
            b,
            "coverage=",
            newcov,
            "high_excess_success_count=",
            len(successes),
            "successes=",
            successes,
        )
    if not any_candidate:
        print("no singleton candidates extend coverage with buffer")


if __name__ == "__main__":
    if "--extend" in sys.argv:
        extended_third_stage_check()
    elif "--diagnose" in sys.argv:
        diagnose_third_stage_failure()
    elif "--high-excess" in sys.argv:
        diagnose_high_excess_third_stage()
    else:
        main()
