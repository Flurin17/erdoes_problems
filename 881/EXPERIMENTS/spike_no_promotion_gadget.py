#!/usr/bin/env python3
"""Verify a local spike-support gadget that does not promote to pair debt.

The construction is a finite warning for Lemma 8.5a.7z.10.  A rank-three
hole can contain a large shifted-overlap spike on a pair of deleted gates,
while the same witness is still repaired after deleting only that pair by a
third active gate.
"""

from __future__ import annotations

from itertools import combinations


def hsum(elements: set[int], order: int, target: int) -> set[int]:
    sums = {0}
    ordered = sorted(elements)
    for _ in range(order):
        sums = {
            value + element
            for value in sums
            for element in ordered
            if value + element <= target
        }
    return sums


def representations3(elements: set[int], target: int) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    ordered = sorted(elements)
    for i, first in enumerate(ordered):
        for j in range(i, len(ordered)):
            second = ordered[j]
            third = target - first - second
            if third < second:
                continue
            if third in elements:
                out.append((first, second, third))
    return out


def main() -> None:
    scale = 1000
    shift = 7
    rows = {1, 4, 9, 16, 25, 36}
    witness = 100 * scale
    f = 10 * scale + shift
    g = 10 * scale
    k = 20 * scale
    deleted = {f, g, k}

    mirrors = {90 * scale - shift - row for row in rows}
    shifted = {row + shift for row in rows}
    repairs = {30 * scale, 60 * scale, 37 * scale, 43 * scale}
    retained = rows | shifted | mirrors | repairs
    elements = retained | deleted

    if witness in hsum(retained, 3, witness):
        raise AssertionError("witness is repaired without deleted gates")

    singleton_repairs = {}
    for gate in sorted(deleted):
        reps = representations3(retained | {gate}, witness)
        if not reps:
            raise AssertionError(f"restoring {gate} does not repair witness")
        singleton_repairs[gate] = reps

    pair_harmless = {}
    for pair in combinations(sorted(deleted), 2):
        remaining = elements - set(pair)
        reps = representations3(remaining, witness)
        if not reps:
            raise AssertionError(f"pair deletion {pair} is bad at witness")
        pair_harmless[pair] = reps

    spike_rows = {}
    for row in sorted(rows):
        mirror = witness - row - f
        overlap = row + f - g
        if mirror not in retained or overlap not in retained:
            raise AssertionError(f"missing spike data for row {row}")
        if row + f in hsum(retained, 2, row + f):
            raise AssertionError(f"row {row} is not private for gate f")
        spike_rows[row] = {"mirror": mirror, "shifted_overlap": overlap}

    min_a = min(elements)
    terminal_gap = (witness - min(deleted) - min_a, witness - 1)
    gap_points = sorted(
        point for point in retained if terminal_gap[0] < point <= terminal_gap[1]
    )
    if gap_points:
        raise AssertionError(f"terminal gap is not empty: {gap_points}")

    print("spike no-promotion gadget")
    print(f"scale={scale} shift={shift}")
    print(f"witness={witness}")
    print(f"deleted={{'f': {f}, 'g': {g}, 'k': {k}}}")
    print(f"rows={sorted(rows)}")
    print(f"shifted_overlap_rows={spike_rows}")
    print(f"witness_not_in_3retained=True")
    print(f"singleton_repairs={singleton_repairs}")
    print(f"pair_harmless_at_witness={pair_harmless}")
    print(f"terminal_gap={terminal_gap}")


if __name__ == "__main__":
    main()
