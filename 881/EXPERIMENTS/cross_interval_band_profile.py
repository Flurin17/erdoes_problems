#!/usr/bin/env python3
"""Finite checks for cross-interval retained-band exclusion.

Lemma 16.63 is an interval geometry statement: if a retained interval
J=[alpha,beta] has doubled band 2J-f deeply overlapping a tested interval
I=[a,b], then a gate-dependent packet inside I must be small.  This script
checks the equivalent overlap inequality for translated and separated
finite intervals.
"""

from __future__ import annotations


def interval(a: int, b: int) -> set[int]:
    return set(range(a, b + 1))


def overlap_size(a: int, b: int, alpha: int, beta: int, gate: int) -> int:
    I = interval(a, b)
    band = interval(2 * alpha - gate, 2 * beta - gate)
    return len(I & band)


def check_case(a: int, b: int, alpha: int, beta: int, margin: int) -> int:
    n = b - a + 1
    ell = beta - alpha + 1
    band_len = 2 * ell - 1
    checked = 0
    tight = 0
    for gate in range(2 * alpha - b - margin, 2 * beta - a + margin + 1):
        overlap = overlap_size(a, b, alpha, beta, gate)
        for m in range(1, min(n, band_len) + 1):
            low = 2 * alpha - b + m - 1
            high = 2 * beta - a - m + 1
            if low <= gate <= high:
                checked += 1
                if overlap < m:
                    raise AssertionError(
                        {
                            "I": [a, b],
                            "J": [alpha, beta],
                            "gate": gate,
                            "m": m,
                            "overlap": overlap,
                            "range": [low, high],
                        }
                    )
                if overlap == m:
                    tight += 1
    print(
        f"case I=[{a},{b}] J=[{alpha},{beta}] margin={margin} "
        f"checked={checked} tight={tight}"
    )
    return checked


def check_palette_case(a: int, b: int, alpha: int, beta: int, span: int) -> int:
    n = b - a + 1
    ell = beta - alpha + 1
    common_len = 2 * ell - 1 - span
    if common_len <= 0:
        return 0

    checked = 0
    tight = 0
    start_lo = 2 * alpha - b - 5
    start_hi = 2 * beta - a + 5
    for f_min in range(start_lo, start_hi + 1):
        f_max = f_min + span
        common_band = interval(2 * alpha - f_min, 2 * beta - f_max)
        overlap = len(interval(a, b) & common_band)
        for m in range(1, min(n, common_len) + 1):
            low = 2 * alpha - b + m - 1
            high = 2 * beta - a - m + 1
            if low <= f_min and f_max <= high:
                checked += 1
                if overlap < m:
                    raise AssertionError(
                        {
                            "I": [a, b],
                            "J": [alpha, beta],
                            "palette": [f_min, f_max],
                            "span": span,
                            "m": m,
                            "overlap": overlap,
                            "range": [low, high],
                        }
                    )
                if overlap == m:
                    tight += 1
    print(
        f"palette I=[{a},{b}] J=[{alpha},{beta}] span={span} "
        f"checked={checked} tight={tight}"
    )
    return checked


def main() -> None:
    cases = [
        (20, 35, 1, 10, 12),
        (20, 35, 8, 18, 12),
        (50, 80, 100, 125, 40),
        (100, 140, 40, 70, 40),
        (10, 30, 15, 45, 20),
    ]
    total = 0
    for case in cases:
        total += check_case(*case)
    palette_cases = [
        (20, 35, 1, 10, 0),
        (20, 35, 1, 10, 5),
        (50, 80, 100, 125, 12),
        (100, 140, 40, 70, 25),
        (10, 30, 15, 45, 40),
    ]
    for case in palette_cases:
        total += check_palette_case(*case)
    print("cross-interval band profile check passed")
    print("total_checked=", total)


if __name__ == "__main__":
    main()
