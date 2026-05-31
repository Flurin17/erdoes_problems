#!/usr/bin/env python3
"""Local angle feasibility for the forced odd-c interface in the 71 candidate.

The length-only matching constraint for the 71 candidate forces at least one
odd-c interior component.  The smallest such component is

    5a = 3b + 3c = 195.

This script checks whether that component is already locally impossible from
straight-boundary angle constraints.  It is not: both sides can be oriented so
that each breakpoint can be completed to one of the straight angle types

    alpha + beta + gamma = pi,
    3alpha + 3beta = pi.

Thus the remaining obstruction, if any, must use global placement, incidence, or
stronger vertex constraints.
"""

from __future__ import annotations

from itertools import combinations, product


ANGLE_INDEX = {"alpha": 0, "beta": 1, "gamma": 2}
STRAIGHT_TYPES = ((1, 1, 1), (3, 3, 0))
EDGE_ENDPOINTS = {
    "a": (("beta", "gamma"), ("gamma", "beta")),
    "b": (("alpha", "gamma"), ("gamma", "alpha")),
    "c": (("alpha", "beta"), ("beta", "alpha")),
}
LENGTHS = {"a": 39, "b": 16, "c": 49}


def angle_counts(angles: tuple[str, ...]) -> tuple[int, int, int]:
    counts = [0, 0, 0]
    for angle in angles:
        counts[ANGLE_INDEX[angle]] += 1
    return tuple(counts)


def pair_can_complete_to_straight(left: str, right: str) -> bool:
    pair = angle_counts((left, right))
    return any(all(pair[i] <= straight[i] for i in range(3)) for straight in STRAIGHT_TYPES)


def feasible_orientations(sequence: str) -> list[tuple[tuple[str, str], ...]]:
    out: list[tuple[tuple[str, str], ...]] = []
    for choices in product((0, 1), repeat=len(sequence)):
        endpoints = tuple(EDGE_ENDPOINTS[edge][choice] for edge, choice in zip(sequence, choices))
        if all(pair_can_complete_to_straight(endpoints[i][1], endpoints[i + 1][0]) for i in range(len(sequence) - 1)):
            out.append(endpoints)
    return out


def positions(sequence: str) -> list[int]:
    total = 0
    out = []
    for edge in sequence:
        total += LENGTHS[edge]
        out.append(total)
    return out[:-1]


def bc_sequences() -> list[str]:
    out = []
    for b_positions in combinations(range(6), 3):
        out.append("".join("b" if i in b_positions else "c" for i in range(6)))
    return out


def main() -> None:
    a_side = "aaaaa"
    a_positions = positions(a_side)
    a_feasible = feasible_orientations(a_side)
    feasible_bc = [(sequence, feasible_orientations(sequence)) for sequence in bc_sequences()]
    feasible_bc = [(sequence, orientations) for sequence, orientations in feasible_bc if orientations]

    print("prime-71 forced odd-c interface local angle check")
    print("interface length: 5a = 3b + 3c = 195")
    print(f"5a breakpoints: {a_positions}")
    print(f"5a feasible endpoint orientations: {len(a_feasible)}")
    print(f"3b+3c feasible edge orders: {len(feasible_bc)} of 20")
    shared_counts = []
    for sequence, orientations in feasible_bc:
        shared = sorted(set(a_positions) & set(positions(sequence)))
        shared_counts.append(len(shared))
        print(
            f"  {sequence}: breakpoints={positions(sequence)}, "
            f"shared_with_5a={shared}, feasible_orientations={len(orientations)}"
        )
    assert len(a_feasible) == 6
    assert len(feasible_bc) == 20
    assert set(shared_counts) == {0}
    print("all 20 orders are locally straight-angle feasible")
    print("no breakpoints coincide, so the minimal component has 4+5=9 T-junctions")
    print("limitation: this is local only and ignores global placement/incidence")


if __name__ == "__main__":
    main()
