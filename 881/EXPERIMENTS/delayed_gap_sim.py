#!/usr/bin/env python3
"""Toy finite simulation for delayed-gap deletion behavior.

Given a finite A subset [1,N], this script deletes each candidate a and
computes the first tail point after which 3(A\\{a}) covers continuously up
to N. This is a finite analogue of a deletion threshold. Large thresholds
relative to a are the delayed-gap phenomenon discussed in PROOF.md.

The simulation is heuristic only: finite windows can create artificial
thresholds and cannot prove asymptotic behavior.
"""

from __future__ import annotations

import random


def hsum_bounded(A: set[int], h: int, limit: int) -> set[int]:
    out = {0}
    for _ in range(h):
        out = {x + y for x in out for y in A if x + y <= limit}
    return out


def finite_tail_threshold(values: set[int], limit: int) -> int | None:
    for start in range(1, limit + 1):
        if all(n in values for n in range(start, limit + 1)):
            return start
    return None


def demo(limit: int = 140, trials: int = 500) -> None:
    random.seed(881)
    best: tuple[float, int, int, set[int]] | None = None
    for _ in range(trials):
        density = random.uniform(0.08, 0.25)
        A = {x for x in range(1, limit + 1) if random.random() < density}
        if finite_tail_threshold(hsum_bounded(A, 2, limit), limit) is None:
            continue
        for a in A:
            if a < 5:
                continue
            threshold = finite_tail_threshold(hsum_bounded(A - {a}, 3, limit), limit)
            if threshold is None:
                continue
            ratio = threshold / a
            if best is None or ratio > best[0]:
                best = (ratio, a, threshold, set(A))
    if best is None:
        print("no sample found")
        return
    ratio, a, threshold, A = best
    print(f"limit={limit} |A|={len(A)} deleted={a} threshold={threshold} ratio={ratio:.2f}")
    print(f"A={sorted(A)}")


if __name__ == "__main__":
    demo()
