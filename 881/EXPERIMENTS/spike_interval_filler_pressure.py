#!/usr/bin/env python3
"""Check low-interval filler pressure on the no-promotion spike gadget.

The range-separated no-promotion gadget has a large two-sum coverage gap.
This script adds retained low interval fillers [1,R] and verifies the first
point at which those fillers repair the protected witness.
"""

from __future__ import annotations

from spike_no_promotion_gadget import representations3


def two_sum_contains(elements: set[int], target: int) -> bool:
    return any(target - x in elements for x in elements)


def in_three_sum(elements: set[int], target: int) -> bool:
    return any(two_sum_contains(elements, target - x) for x in elements)


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

    first_private_sum = f + min(rows)
    threshold = (first_private_sum + 1) // 2

    checks = [threshold - 1, threshold]
    results = {}
    for radius in checks:
        retained = base_retained | set(range(1, radius + 1))
        repaired = in_three_sum(retained, witness)
        repairs_at_witness = representations3(retained, witness) if repaired else []
        results[radius] = {
            "guaranteed_low_interval_two_coverage": (2, 2 * radius),
            "covers_first_private_sum": 2 * radius >= first_private_sum,
            "witness_repaired_without_deleted_gates": repaired,
            "repairs": repairs_at_witness[:10],
        }

    print("spike interval filler pressure")
    print(f"scale={scale} shift={shift}")
    print(f"witness={witness}")
    print(f"deleted={{'f': {f}, 'g': {g}, 'k': {k}}}")
    print(f"rows={sorted(rows)}")
    print(f"first_private_sum=f+min(rows)={first_private_sum}")
    print(f"first_interval_radius_covering_private_sum={threshold}")
    print(f"results={results}")

    if results[threshold - 1]["witness_repaired_without_deleted_gates"]:
        raise AssertionError("witness repaired before low interval covers f+min(rows)")
    if not results[threshold]["witness_repaired_without_deleted_gates"]:
        raise AssertionError("witness not repaired once low interval covers f+min(rows)")


if __name__ == "__main__":
    main()
