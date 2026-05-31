#!/usr/bin/env python3
"""Boundary-star checks for selected 3alpha+2beta=pi candidates.

The first targets are raw 3alpha+2beta candidates left after stronger
source filters:

    tile sides (a,b,c) = (6,5,9),
    outer angles (2alpha, beta, alpha+beta),
    outer side lengths (28,15,27),

and

    tile sides (a,b,c) = (2,3,4),
    outer angles (alpha, alpha, alpha+2beta),
    outer side lengths (12,12,21).

The side labels follow the usual convention: side `a` is opposite `alpha`,
side `b` opposite `beta`, and side `c` opposite `gamma=2alpha+beta`.

At each boundary vertex the visible endpoint angles must complete to the
required boundary angle, and the inward side labels must be connectable by the
remaining incident tile angles.  This is the same local side-label star check
used by the gamma=2pi/3 boundary automata.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache


Angle = str
Side = str
PlacedEdge = tuple[Side, Angle, Angle]

SIDE_LENGTHS_14 = {"a": 6, "b": 5, "c": 9}
SIDE_ENDPOINTS: dict[Side, tuple[Angle, Angle]] = {
    "a": ("beta", "gamma"),
    "b": ("alpha", "gamma"),
    "c": ("alpha", "beta"),
}
ANGLE_SIDES: dict[Angle, tuple[Side, Side]] = {
    "alpha": ("b", "c"),
    "beta": ("a", "c"),
    "gamma": ("a", "b"),
}

TARGETS: dict[str, Counter[Angle]] = {
    "alpha": Counter({"alpha": 1}),
    "beta": Counter({"beta": 1}),
    "2alpha": Counter({"alpha": 2}),
    "alpha+beta": Counter({"alpha": 1, "beta": 1}),
    "alpha+2beta": Counter({"alpha": 1, "beta": 2}),
    "straight-no-gamma": Counter({"alpha": 3, "beta": 2}),
    "straight-gamma": Counter({"alpha": 1, "beta": 1, "gamma": 1}),
}


def orientations(side: Side) -> tuple[PlacedEdge, PlacedEdge]:
    left, right = SIDE_ENDPOINTS[side]
    return ((side, left, right), (side, right, left))


def other_side(boundary_side: Side, endpoint_angle: Angle) -> Side:
    first, second = ANGLE_SIDES[endpoint_angle]
    if boundary_side == first:
        return second
    if boundary_side == second:
        return first
    raise ValueError((boundary_side, endpoint_angle))


def trail_possible(edge_counts: Counter[Angle], start: Side, end: Side) -> bool:
    counts = Counter(edge_counts)
    total = sum(counts.values())

    @lru_cache(maxsize=None)
    def rec(current: Side, remaining: int, alpha: int, beta: int, gamma: int) -> bool:
        if remaining == 0:
            return current == end
        available = {"alpha": alpha, "beta": beta, "gamma": gamma}
        for angle, count in available.items():
            if count == 0:
                continue
            first, second = ANGLE_SIDES[angle]
            if current not in (first, second):
                continue
            next_available = dict(available)
            next_available[angle] -= 1
            next_side = second if current == first else first
            if rec(
                next_side,
                remaining - 1,
                next_available["alpha"],
                next_available["beta"],
                next_available["gamma"],
            ):
                return True
        return False

    return rec(start, total, counts["alpha"], counts["beta"], counts["gamma"])


def transition_types(left: PlacedEdge, right: PlacedEdge, targets: list[str]) -> set[str]:
    left_side, _left_start, left_angle = left
    right_side, right_angle, _right_end = right
    visible = Counter([left_angle, right_angle])
    start = other_side(left_side, left_angle)
    end = other_side(right_side, right_angle)
    out: set[str] = set()
    for label in targets:
        target = TARGETS[label]
        if not all(visible[key] <= target[key] for key in visible):
            continue
        if trail_possible(target - visible, start, end):
            out.add(label)
    return out


def side_label_sequences(length: int, side_lengths: dict[Side, int]) -> list[tuple[Side, ...]]:
    out: list[tuple[Side, ...]] = []

    def rec(remaining: int, current: list[Side]) -> None:
        if remaining == 0:
            out.append(tuple(current))
            return
        for side, side_length in side_lengths.items():
            if side_length <= remaining:
                current.append(side)
                rec(remaining - side_length, current)
                current.pop()

    rec(length, [])
    return out


def oriented_boundary_paths(length: int, side_lengths: dict[Side, int]) -> list[tuple[PlacedEdge, ...]]:
    paths: list[tuple[PlacedEdge, ...]] = []
    straight_targets = ["straight-no-gamma", "straight-gamma"]
    for sequence in side_label_sequences(length, side_lengths):
        choices = [orientations(side) for side in sequence]

        def rec(index: int, current: list[PlacedEdge]) -> None:
            if index == len(choices):
                paths.append(tuple(current))
                return
            for edge in choices[index]:
                if current and not transition_types(current[-1], edge, straight_targets):
                    continue
                current.append(edge)
                rec(index + 1, current)
                current.pop()

        rec(0, [])
    return paths


def feasible_n14_triquadratic_boundaries() -> list[
    tuple[tuple[PlacedEdge, ...], tuple[PlacedEdge, ...], tuple[PlacedEdge, ...]]
]:
    """Return feasible boundary cycles for the N=14 triquadratic candidate.

    Vertices are ordered as:

    - V0 has angle 2alpha,
    - V1 has angle beta,
    - V2 has angle alpha+beta.

    Therefore side V0-V1 has length 27, V1-V2 length 28, and V2-V0 length 15.
    """
    paths_01 = oriented_boundary_paths(27, SIDE_LENGTHS_14)
    paths_12 = oriented_boundary_paths(28, SIDE_LENGTHS_14)
    paths_20 = oriented_boundary_paths(15, SIDE_LENGTHS_14)
    out = []
    for path_01 in paths_01:
        for path_12 in paths_12:
            if not transition_types(path_01[-1], path_12[0], ["beta"]):
                continue
            for path_20 in paths_20:
                if not transition_types(path_12[-1], path_20[0], ["alpha+beta"]):
                    continue
                if not transition_types(path_20[-1], path_01[0], ["2alpha"]):
                    continue
                out.append((path_01, path_12, path_20))
    return out


def feasible_n21_isosceles_alpha_boundaries() -> list[
    tuple[tuple[PlacedEdge, ...], tuple[PlacedEdge, ...], tuple[PlacedEdge, ...]]
]:
    """Return feasible boundary cycles for the N=21 isosceles-alpha candidate.

    Vertices are ordered as:

    - V0 has angle alpha,
    - V1 has angle alpha,
    - V2 has angle alpha+2beta.

    Therefore side V0-V1 has length 21, and the two equal sides have length 12.
    """
    side_lengths = {"a": 2, "b": 3, "c": 4}
    paths_01 = oriented_boundary_paths(21, side_lengths)
    paths_12 = oriented_boundary_paths(12, side_lengths)
    paths_20 = oriented_boundary_paths(12, side_lengths)
    out = []
    for path_01 in paths_01:
        for path_12 in paths_12:
            if not transition_types(path_01[-1], path_12[0], ["alpha"]):
                continue
            for path_20 in paths_20:
                if not transition_types(path_12[-1], path_20[0], ["alpha+2beta"]):
                    continue
                if not transition_types(path_20[-1], path_01[0], ["alpha"]):
                    continue
                out.append((path_01, path_12, path_20))
    return out


def main() -> None:
    paths_27 = oriented_boundary_paths(27, SIDE_LENGTHS_14)
    paths_28 = oriented_boundary_paths(28, SIDE_LENGTHS_14)
    paths_15 = oriented_boundary_paths(15, SIDE_LENGTHS_14)
    feasible = feasible_n14_triquadratic_boundaries()
    print("N=14 triquadratic 3alpha+2beta boundary-star check")
    print("tile sides (a,b,c)=(6,5,9); outer sides (28,15,27)")
    print("outer angles: (2alpha, beta, alpha+beta)")
    print("side-label decompositions by length:")
    for length in (27, 28, 15):
        print(f"  length {length}: {len(side_label_sequences(length, SIDE_LENGTHS_14))}")
    print("oriented side paths passing straight-vertex stars:")
    print(f"  length 27: {len(paths_27)}")
    print(f"  length 28: {len(paths_28)}")
    print(f"  length 15: {len(paths_15)}")
    print(f"feasible full boundary cycles: {len(feasible)}")
    if not feasible:
        print("boundary-star obstruction: candidate cannot be a tiling")

    side_lengths_21 = {"a": 2, "b": 3, "c": 4}
    paths_21 = oriented_boundary_paths(21, side_lengths_21)
    paths_12 = oriented_boundary_paths(12, side_lengths_21)
    feasible_21 = feasible_n21_isosceles_alpha_boundaries()
    print()
    print("N=21 isosceles-alpha 3alpha+2beta boundary-star check")
    print("tile sides (a,b,c)=(2,3,4); outer sides (12,12,21)")
    print("outer angles: (alpha, alpha, alpha+2beta)")
    print("side-label decompositions by length:")
    for length in (21, 12):
        print(f"  length {length}: {len(side_label_sequences(length, side_lengths_21))}")
    print("oriented side paths passing straight-vertex stars:")
    print(f"  length 21: {len(paths_21)}")
    print(f"  length 12: {len(paths_12)}")
    print(f"feasible full boundary cycles: {len(feasible_21)}")
    if not feasible_21:
        print("boundary-star obstruction: candidate cannot be a tiling")


if __name__ == "__main__":
    main()
