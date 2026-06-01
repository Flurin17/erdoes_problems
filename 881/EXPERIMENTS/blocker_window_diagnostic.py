#!/usr/bin/env python3
"""Diagnose finite blocker-window families for cross-block gate packets.

This script checks the finite geometry used in Corollary 16.67.  A tested
interval I and retained intervals J contribute affine blocker windows for
active gates.  Gates inside those windows have a deep overlap between I and
2J-f, so they cannot support a dense gate-dependent packet.  Clustered
palettes contained in one blocker window have a common forbidden band.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Interval:
    lo: int
    hi: int

    @property
    def length(self) -> int:
        return self.hi - self.lo + 1

    def points(self) -> set[int]:
        return set(range(self.lo, self.hi + 1))


def blocker_window(test: Interval, retained: Interval, eta_num: int, eta_den: int) -> Interval:
    n = test.length
    m_eta = ((eta_den - eta_num) * n) // eta_den + 1
    return Interval(
        2 * retained.lo - test.hi + m_eta - 1,
        2 * retained.hi - test.lo - m_eta + 1,
    )


def doubled_band(retained: Interval, gate: int) -> Interval:
    return Interval(2 * retained.lo - gate, 2 * retained.hi - gate)


def overlap(a: Interval, b: Interval) -> int:
    lo = max(a.lo, b.lo)
    hi = min(a.hi, b.hi)
    return max(0, hi - lo + 1)


def check_single_gates(test: Interval, retained: Interval, eta_num: int, eta_den: int) -> int:
    window = blocker_window(test, retained, eta_num, eta_den)
    n = test.length
    m_eta = ((eta_den - eta_num) * n) // eta_den + 1
    checked = 0
    for gate in range(window.lo, window.hi + 1):
        band = doubled_band(retained, gate)
        ov = overlap(test, band)
        checked += 1
        if ov < m_eta:
            raise AssertionError((test, retained, gate, window, ov, m_eta))
    print(
        f"single I=[{test.lo},{test.hi}] J=[{retained.lo},{retained.hi}] "
        f"eta={eta_num}/{eta_den} window=[{window.lo},{window.hi}] checked={checked}"
    )
    return checked


def check_palette(test: Interval, retained: Interval, eta_num: int, eta_den: int) -> int:
    window = blocker_window(test, retained, eta_num, eta_den)
    n = test.length
    m_eta = ((eta_den - eta_num) * n) // eta_den + 1
    max_span = 2 * retained.length - 1 - m_eta
    if max_span < 0:
        return 0
    checked = 0
    for f_min in range(window.lo, window.hi + 1):
        for f_max in range(f_min, min(window.hi, f_min + max_span) + 1):
            common = Interval(2 * retained.lo - f_min, 2 * retained.hi - f_max)
            ov = overlap(test, common)
            checked += 1
            if ov < m_eta:
                raise AssertionError((test, retained, f_min, f_max, common, ov, m_eta))
    print(
        f"palette I=[{test.lo},{test.hi}] J=[{retained.lo},{retained.hi}] "
        f"eta={eta_num}/{eta_den} max_span={max_span} checked={checked}"
    )
    return checked


def main() -> None:
    cases = [
        (Interval(50, 80), [Interval(1, 20), Interval(95, 120)], 1, 2),
        (Interval(100, 140), [Interval(30, 70), Interval(155, 190)], 2, 3),
        (Interval(20, 35), [Interval(1, 10), Interval(8, 18)], 3, 4),
    ]
    total = 0
    for test, blockers, eta_num, eta_den in cases:
        windows = [blocker_window(test, retained, eta_num, eta_den) for retained in blockers]
        print(
            "family",
            f"I=[{test.lo},{test.hi}]",
            "windows=",
            [(w.lo, w.hi) for w in windows],
        )
        for retained in blockers:
            total += check_single_gates(test, retained, eta_num, eta_den)
            total += check_palette(test, retained, eta_num, eta_den)
    print("blocker-window diagnostic passed")
    print("total_checked=", total)


if __name__ == "__main__":
    main()
