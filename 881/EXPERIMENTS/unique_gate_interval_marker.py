#!/usr/bin/env python3
"""Verify the interval-marker unique-gate packet from Example 16.23."""

from __future__ import annotations


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def interval_marker_checks(L: int) -> dict[str, object]:
    A = set(range(1, L + 1)) | {2 * L}
    q = 2 * L
    d = 2 * L + 2
    w = q + d
    C = A - {q}
    U = set(range(1, L + 1))
    two_c = hsum(C, 2, w)
    three_a = hsum(A, 3, w)
    four_c = hsum(C, 4, w)
    unique_gate = all(q + p not in two_c for p in U)
    private = w not in four_c
    shifted_covered = all(w - p in three_a for p in U)
    independence_violations = [
        (p, r, p + q - r)
        for p in sorted(U)
        for r in sorted(U)
        if p != r and p + q - r in A
    ]
    certificate = (1, 2, 2, 2)
    e, y1, y2, y3 = certificate
    certificate_ok = (
        y1 + y2 - e in A
        and y1 + y2 + y3 - 2 * e in A
        and all(y != e for y in (y1, y2, y3))
    )
    return {
        "L": L,
        "A": sorted(A),
        "q": q,
        "w": w,
        "private": private,
        "shifted_covered": shifted_covered,
        "unique_gate": unique_gate,
        "independence_violations": independence_violations,
        "certificate": certificate,
        "certificate_ok": certificate_ok,
    }


def main() -> None:
    for L in (4, 5, 8, 13):
        print(interval_marker_checks(L))


if __name__ == "__main__":
    main()
