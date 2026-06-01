#!/usr/bin/env python3
"""Diagnose the old-gate shadow rows forced by k=3 pair witnesses.

This finite check illustrates Lemmas 16.3--16.4 from PROOF.md.  For a pair
{a,b} and witness w with w notin 4(A\\{a,b}), every retained padder p in
the interval where b is too large to participate must force
w-a-p in 2(A\\{b}).
"""

from __future__ import annotations

from itertools import combinations_with_replacement


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def has_two_sum(elements: set[int], target: int) -> bool:
    for x in elements:
        if target - x in elements:
            return True
    return False


def reps3_using(elements: set[int], target: int, required: set[int]) -> bool:
    ordered = sorted(elements)
    for triple in combinations_with_replacement(ordered, 3):
        if sum(triple) == target and set(triple) & required:
            return True
    return False


def diagnose(A: set[int], a: int, b: int, w: int, threshold: int) -> None:
    m0 = min(A)
    C = A - {a, b}
    cap = max(4 * max(A), w) + 20
    without = hsum(C, 4, cap)
    print("A=", sorted(A))
    print("pair=", (a, b), "w=", w, "w in 4(A\\pair)=", w in without)
    forced = []
    terminal = []
    for p in sorted(C):
        if w - p < threshold:
            continue
        if p > w - a - 2 * m0:
            terminal.append(p)
            continue
        if p > w - b - 2 * m0:
            target = w - a - p
            forced.append((p, target, has_two_sum(A - {b}, target)))
    print("forced old-gate rows (p, w-a-p, in 2(A\\{b}))=", forced)
    print("terminal-gap retained p=", terminal)
    print("three-rep uses pair for checked p=")
    for p, _, _ in forced:
        print("  p=", p, reps3_using(A, w - p, {a, b}))


def classify_candidate(
    A: set[int],
    a: int,
    b: int,
    w: int,
    threshold: int,
) -> str:
    m0 = min(A)
    cap = max(4 * max(A), w) + 20
    if w not in hsum(A, 4, cap):
        return "not4A"
    C = A - {a, b}
    if w not in hsum(C, 4, cap):
        return "success"
    for p in C:
        if w - p < threshold:
            continue
        if p > w - a - 2 * m0:
            return "terminal"
        if p > w - b - 2 * m0 and not has_two_sum(A - {b}, w - a - p):
            return "shadow"
    return "repaired_other"


def scan_third_stage() -> None:
    old = {1, 3, 5, 20, 21, 23, 30, 31}
    threshold = 22
    witness_range = range(41, 48)
    for b in (41, 43):
        A = old | {b}
        print("candidate b=", b)
        for a in sorted(old):
            buckets = {
                "success": [],
                "terminal": [],
                "shadow": [],
                "repaired_other": [],
                "not4A": [],
            }
            for w in witness_range:
                buckets[classify_candidate(A, a, b, w, threshold)].append(w)
            print("  old a=", a, buckets)


def main() -> None:
    # Robust-booster pair-stage diagnostic after adding candidate b=41.
    old = {1, 3, 5, 20, 21, 23, 30, 31}
    A = old | {41}
    diagnose(A, a=20, b=41, w=47, threshold=22)
    print()
    scan_third_stage()


if __name__ == "__main__":
    main()
