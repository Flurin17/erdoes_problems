#!/usr/bin/env python3
"""Verify a high-sided shadow escape set counterexample.

This checks the finite family from Warning 8.5a.7z.12h.4.  The example has
initial two-sum coverage through p-1 and a genuine terminal hole, but the
split escape set E={z not in A : d+z not in 2C} lies entirely above p/2.
Thus cardinality or interval coverage alone cannot force a complementary
escape pair x+y=p.
"""

from __future__ import annotations

import argparse


def pair_sums(elements: set[int], cap: int) -> set[int]:
    values = sorted(elements)
    out: set[int] = set()
    for i, first in enumerate(values):
        for second in values[i:]:
            total = first + second
            if total > cap:
                break
            out.add(total)
    return out


def triple_sums(elements: set[int], cap: int) -> set[int]:
    values = sorted(elements)
    out: set[int] = set()
    for first in values:
        for second in values:
            if first + second > cap:
                break
            for third in values:
                total = first + second + third
                if total > cap:
                    break
                out.add(total)
    return out


def cover_end(sums: set[int], start: int, cap: int) -> int:
    point = start
    while point <= cap and point in sums:
        point += 1
    return point - 1


def build_example(l_value: int, n_value: int) -> dict[str, object]:
    if l_value < 2:
        raise ValueError("L must be at least 2")
    if n_value <= 3 * l_value:
        raise ValueError("N must be greater than 3L")

    low = set(range(1, l_value + 1))
    high = set(range(n_value, n_value + l_value))
    retained = low | high
    p_gap = 2 * l_value + 1
    q_gate = n_value + 2 * l_value
    deleted = {p_gap, q_gate}
    full = retained | deleted
    defect = 2 * n_value + l_value - 2
    witness = p_gap + defect

    two_retained = pair_sums(retained, witness)
    two_full = pair_sums(full, witness)
    three_retained = triple_sums(retained, witness)

    old_row_escapes = []
    for old in sorted(full):
        candidate = p_gap - old
        if (
            candidate > 0
            and candidate not in full
            and defect + old not in two_retained
        ):
            old_row_escapes.append((old, candidate))

    escape_set = [
        item
        for item in range(1, p_gap)
        if item not in full and defect + item not in two_retained
    ]
    escape_lookup = set(escape_set)
    complementary_pairs = [
        (item, p_gap - item)
        for item in escape_set
        if item < p_gap - item and p_gap - item in escape_lookup
    ]
    low_escapes = [item for item in escape_set if 2 * item < p_gap]

    return {
        "L": l_value,
        "N": n_value,
        "C": sorted(retained),
        "F": sorted(deleted),
        "p": p_gap,
        "q": q_gate,
        "d": defect,
        "w": witness,
        "cover_end_2A": cover_end(two_full, 2, witness),
        "p_in_2A": p_gap in two_full,
        "w_in_3C": witness in three_retained,
        "restore_p_repairs": (
            n_value in retained and n_value + l_value - 2 in retained
        ),
        "restore_q_repairs": (
            1 in retained and n_value + l_value - 2 in retained
        ),
        "old_row_escape_count": len(old_row_escapes),
        "old_row_escapes": old_row_escapes,
        "escape_set": escape_set,
        "escape_set_count": len(escape_set),
        "low_escape_count": len(low_escapes),
        "low_escapes": low_escapes,
        "complementary_pair_count": len(complementary_pairs),
        "complementary_pairs": complementary_pairs,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--L", type=int, default=5)
    parser.add_argument("--N", type=int, default=20)
    args = parser.parse_args()

    data = build_example(args.L, args.N)
    print("shadow escape counterexample")
    for key, value in data.items():
        print(f"{key}={value}")

    if data["cover_end_2A"] != data["p"] - 1:
        raise AssertionError("initial two-sum coverage does not stop at p-1")
    if data["p_in_2A"]:
        raise AssertionError("p should be the first two-sum gap")
    if data["w_in_3C"]:
        raise AssertionError("w should be a retained three-sum hole")
    if not data["restore_p_repairs"] or not data["restore_q_repairs"]:
        raise AssertionError("deleted gates should both repair w")
    if data["old_row_escape_count"] != 0:
        raise AssertionError("old-row escapes should be absent")
    if data["complementary_pair_count"] != 0:
        raise AssertionError("escape set should have no complementary pair")


if __name__ == "__main__":
    main()
