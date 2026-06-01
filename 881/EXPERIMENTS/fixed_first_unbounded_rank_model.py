#!/usr/bin/env python3
"""Local fixed-first unbounded-rank active-hole model.

This constructs finite sets with a fixed deleted endpoint d=1 and an
arbitrarily far suffix H such that F={d} union H is inclusion-minimal for
one order-3 hole.  It is a local diagnostic for Target 13.1l.2k, not a
counterexample: the finite set has large two-sum coverage gaps.
"""

from __future__ import annotations

import argparse
from itertools import combinations_with_replacement


def sums_h(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    for _ in range(h):
        sums = {s + a for s in sums for a in elements if s + a <= cap}
    return sums


def reps3(elements: set[int], target: int) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    for rep in combinations_with_replacement(sorted(elements), 3):
        if sum(rep) == target:
            out.append(rep)
    return out


def repairs_after_adding(retained: set[int], x: int, witness: int) -> bool:
    return bool(reps3(retained | {x}, witness))


def build(rank: int, start: int) -> tuple[set[int], set[int], set[int], int]:
    if rank < 1:
        raise ValueError("rank must be positive")
    if start <= 4 * rank:
        raise ValueError("start must exceed 4*rank for the clean gap check")

    d = 1
    h_set = set(range(start + 1, start + rank + 1))
    witness = start + 2 * rank + 2
    retained = set(range(2, 2 * rank + 1)) | {witness - 2}
    deleted = {d} | h_set
    return retained | deleted, retained, deleted, witness


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, default=6)
    parser.add_argument("--start", type=int, default=40)
    args = parser.parse_args()

    a_set, retained, deleted, witness = build(args.rank, args.start)
    cap = witness
    retained_sums = sums_h(retained, 3, cap)

    print("fixed-first unbounded-rank local model")
    print("rank=", args.rank)
    print("start=", args.start)
    print("A=", sorted(a_set))
    print("deleted F=", sorted(deleted))
    print("retained C=", sorted(retained))
    print("witness=", witness)
    print("witness_in_3C=", witness in retained_sums)

    minimal = witness not in retained_sums
    for f in sorted(deleted):
        reps = reps3(retained | {f}, witness)
        print("restore", f, "repairs=", reps[:5])
        minimal = minimal and bool(reps)
    print("inclusion_minimal=", minimal)

    two = sums_h(a_set, 2, 2 * max(a_set))
    cover = 2
    while cover in two:
        cover += 1
    print("two_sum_initial_coverage_end=", cover - 1)

    suffix_start = args.start + 1
    gap_candidates = [
        x
        for x in range(2 * args.rank + 1, suffix_start)
        if x not in a_set
    ]
    unsafe = [
        x
        for x in gap_candidates
        if repairs_after_adding(retained, x, witness)
    ]
    print("gap_candidate_count=", len(gap_candidates))
    print("unsafe_gap_fillers=", unsafe)
    if unsafe:
        print("unsafe_interval=", (unsafe[0], unsafe[-1]))


if __name__ == "__main__":
    main()
