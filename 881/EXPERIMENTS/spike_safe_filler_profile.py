#!/usr/bin/env python3
"""Profile safe retained fillers for the no-promotion spike gadget.

The maximal low interval below the first private two-sum does not repair the
protected witness.  A second retained band above all private two-sums can
bridge the next full two-sum coverage gap, provided it avoids middle-packet
complements such as w-43N-43N.

This is not a stage construction: the protected witness is still far above
the verified coverage endpoint.  The diagnostic only separates the easy
initial coverage burden from the harder terminal/frozen-witness burden.
"""

from __future__ import annotations

from spike_no_promotion_gadget import representations3


def pair_sums(elements: set[int], cap: int) -> set[int]:
    values = sorted(elements)
    sums: set[int] = set()
    for i, first in enumerate(values):
        for second in values[i:]:
            total = first + second
            if total > cap:
                break
            sums.add(total)
    return sums


def cover_end(sums: set[int], start: int, cap: int) -> int:
    point = start
    while point <= cap and point in sums:
        point += 1
    return point - 1


def first_gaps(sums: set[int], start: int, cap: int, limit: int = 20) -> list[int]:
    return [point for point in range(start, cap + 1) if point not in sums][:limit]


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
    repairs = {37 * scale, 43 * scale}
    base_retained = rows | shifted | mirrors | repairs

    private_sums = {f + row for row in rows}
    low_radius = (min(private_sums) - 1) // 2
    low_band = set(range(1, low_radius + 1))

    upper_start = max(private_sums) + 1
    upper_stop = 15 * scale
    dangerous_middle_complement = witness - 2 * 43 * scale
    upper_band = set(range(upper_start, upper_stop + 1))
    upper_band.discard(dangerous_middle_complement)

    retained = base_retained | low_band | upper_band
    full = retained | deleted

    retained_pair_sums = pair_sums(retained, 30 * scale)
    full_pair_sums = pair_sums(full, 30 * scale)
    witness_repairs = representations3(retained, witness)

    print("spike safe filler profile")
    print(f"scale={scale} shift={shift}")
    print(f"witness={witness}")
    print(f"deleted={{'f': {f}, 'g': {g}, 'k': {k}}}")
    print(f"private_sums={sorted(private_sums)}")
    print(f"low_band=[1,{low_radius}]")
    print(
        "upper_band="
        f"[{upper_start},{upper_stop}] without {dangerous_middle_complement}"
    )
    print(
        "private_sums_in_retained_2sum="
        f"{[(value, value in retained_pair_sums) for value in sorted(private_sums)]}"
    )
    print(
        "retained_2sum_cover_from_2="
        f"{cover_end(retained_pair_sums, 2, 30 * scale)}"
    )
    print(
        "full_2sum_cover_from_2="
        f"{cover_end(full_pair_sums, 2, 30 * scale)}"
    )
    print(f"retained_first_gaps={first_gaps(retained_pair_sums, 2, 30 * scale)}")
    print(f"full_first_gaps={first_gaps(full_pair_sums, 2, 30 * scale)}")
    print(f"witness_repaired_without_deleted_gates={bool(witness_repairs)}")
    print(f"witness_repairs={witness_repairs[:5]}")

    if any(value in retained_pair_sums for value in private_sums):
        raise AssertionError("a private spike sum is covered by retained fillers")
    if witness_repairs:
        raise AssertionError("safe filler profile repaired the protected witness")
    if cover_end(full_pair_sums, 2, 30 * scale) < 30 * scale:
        raise AssertionError("full two-sum coverage did not reach 30N")
    if dangerous_middle_complement in upper_band:
        raise AssertionError("dangerous middle complement was not removed")


if __name__ == "__main__":
    main()
