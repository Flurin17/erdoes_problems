#!/usr/bin/env python3
"""Search finite stages for adjacent-order minimality.

For k>=3, a counterexample to Problem 881 would follow from a set that is
an asymptotic k-basis and is minimal as a (k+1)-basis.  This script searches
small finite stage extensions: k-sum coverage through a new endpoint, and
for every new element a, a local (k+1)-sum witness below that endpoint which
is lost after deleting a.

Finite output is only heuristic; later stages may repair local witnesses.
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


def find_one_stage(
    old: set[int],
    previous_endpoint: int,
    base: int,
    k: int,
    slack: int = 30,
    max_new_size: int = 4,
) -> tuple[set[int], int, int, dict[int, list[int]]] | None:
    cap0 = max((k + 2) * max(old) + 200, previous_endpoint + 200)
    oldcov = cover_end(hsum(old, k, cap0), base, cap0)
    candidates = [
        x
        for x in range(previous_endpoint + 1, oldcov + slack + 1)
        if x not in old
    ]
    for new_size in range(1, max_new_size + 1):
        for new_tuple in combinations(candidates, new_size):
            new = set(new_tuple)
            elements = old | new
            cap = max((k + 2) * max(elements) + 200, oldcov + 250)
            k_sums = hsum(elements, k, cap)
            newcov = cover_end(k_sums, base, cap)
            if newcov <= previous_endpoint:
                continue
            kp1_sums = hsum(elements, k + 1, cap)
            first_declared = max(previous_endpoint + 1, max(new))
            for declared in range(first_declared, newcov):
                witnesses: dict[int, list[int]] = {}
                ok = True
                for a in sorted(new):
                    without = hsum(elements - {a}, k + 1, cap)
                    found = [
                        w
                        for w in range(previous_endpoint + 1, declared + 1)
                        if w in kp1_sums and w not in without
                    ]
                    if not found:
                        ok = False
                        break
                    witnesses[a] = found[:5]
                if ok:
                    return new, declared, newcov, witnesses
    return None


def find_stage(k: int = 3) -> None:
    max_old = 14
    max_old_size = 6
    max_new_size = 4
    slack = 18

    for old_max in range(k + 3, max_old + 1):
        universe = range(1, old_max + 1)
        for old_size in range(k, min(old_max, max_old_size) + 1):
            for old_tuple in combinations(universe, old_size):
                old = set(old_tuple)
                cap0 = (k + 2) * old_max + 60
                old_sums = hsum(old, k, cap0)
                starts = [x for x in range(1, cap0 + 1) if x in old_sums]
                for base in starts:
                    oldcov = cover_end(old_sums, base, cap0)
                    if oldcov - base + 1 < k + 2:
                        continue
                    for previous_endpoint in range(base, oldcov + 1):
                        candidates = [
                            x
                            for x in range(previous_endpoint + 1, oldcov + slack + 1)
                            if x not in old
                        ]
                        for new_size in range(1, max_new_size + 1):
                            for new_tuple in combinations(candidates, new_size):
                                new = set(new_tuple)
                                elements = old | new
                                cap = max((k + 2) * max(elements) + 80, oldcov + 100)
                                k_sums = hsum(elements, k, cap)
                                newcov = cover_end(k_sums, base, cap)
                                if newcov <= previous_endpoint:
                                    continue
                                kp1_sums = hsum(elements, k + 1, cap)
                                first_declared = max(previous_endpoint + 1, max(new))
                                for declared in range(first_declared, newcov):
                                    witnesses: dict[int, list[int]] = {}
                                    ok = True
                                    for a in sorted(new):
                                        without = hsum(elements - {a}, k + 1, cap)
                                        found = [
                                            w
                                            for w in range(previous_endpoint + 1, declared + 1)
                                            if w in kp1_sums and w not in without
                                        ]
                                        if not found:
                                            ok = False
                                            break
                                        witnesses[a] = found[:5]
                                    if ok:
                                        print(f"found k={k} adjacent stage")
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
                                        print("witnesses=", witnesses)
                                        return
    print(f"no k={k} adjacent stage within searched bounds")


def greedy_chain(k: int = 3) -> None:
    elements = set(range(1, k + 1))
    base = k
    endpoint = k
    for step in range(1, 8):
        found = find_one_stage(elements, endpoint, base, k)
        if found is None:
            print(
                "stalled",
                "step=", step,
                "A=", sorted(elements),
                "endpoint=", endpoint,
                "coverage=", cover_end(hsum(elements, k, 10000), base, 10000),
            )
            return
        new, declared, newcov, witnesses = found
        print(
            "stage=", step,
            "new=", sorted(new),
            "endpoint=", declared,
            "coverage=", newcov,
            "witnesses=", witnesses,
        )
        elements |= new
        endpoint = declared


if __name__ == "__main__":
    greedy_chain(3)
