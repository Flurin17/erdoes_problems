#!/usr/bin/env python3
"""Boundary-star checks for selected non-isosceles gamma=2pi/3 candidates.

The exact arithmetic filter leaves small candidates in the
`(alpha,alpha+beta,alpha+2beta)` template, notably:

- `N=21`, tile `(a,b,c)=(5,16,19)`, scale `m=4`;
- `N=30`, tile `(a,b,c)=(7,8,13)`, scale `m=4`.

For this template the primitive outer side ratios are `(a,c,a+b)`, opposite
`(alpha, alpha+beta, alpha+2beta)` respectively.  This script enumerates full
boundary side decompositions and local side-label stars.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache


Angle = str
Side = str
PlacedEdge = tuple[Side, Angle, Angle]

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
    "alpha+beta": Counter({"alpha": 1, "beta": 1}),
    "alpha+2beta": Counter({"alpha": 1, "beta": 2}),
    "straight-no-gamma": Counter({"alpha": 3, "beta": 3}),
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


def feasible_alpha_alpha_beta_alpha_2beta(
    sides: tuple[int, int, int], scale: int
) -> list[tuple[tuple[PlacedEdge, ...], tuple[PlacedEdge, ...], tuple[PlacedEdge, ...]]]:
    a, b, c = sides
    side_lengths = {"a": a, "b": b, "c": c}
    # V0=alpha, V1=alpha+beta, V2=alpha+2beta.
    # Edges V0-V1, V1-V2, V2-V0 are opposite V2,V0,V1.
    length_01 = scale * (a + b)
    length_12 = scale * a
    length_20 = scale * c
    paths_01 = oriented_boundary_paths(length_01, side_lengths)
    paths_12 = oriented_boundary_paths(length_12, side_lengths)
    paths_20 = oriented_boundary_paths(length_20, side_lengths)
    out = []
    for path_01 in paths_01:
        for path_12 in paths_12:
            if not transition_types(path_01[-1], path_12[0], ["alpha+beta"]):
                continue
            for path_20 in paths_20:
                if not transition_types(path_12[-1], path_20[0], ["alpha+2beta"]):
                    continue
                if not transition_types(path_20[-1], path_01[0], ["alpha"]):
                    continue
                out.append((path_01, path_12, path_20))
    return out


def report(n: int, sides: tuple[int, int, int], scale: int) -> None:
    a, b, c = sides
    side_lengths = {"a": a, "b": b, "c": c}
    lengths = [scale * (a + b), scale * a, scale * c]
    path_counts = {length: len(oriented_boundary_paths(length, side_lengths)) for length in lengths}
    feasible = feasible_alpha_alpha_beta_alpha_2beta(sides, scale)
    print(f"N={n} non-isosceles gamma=2pi/3 boundary-star check")
    print(f"tile sides (a,b,c)={sides}; scale={scale}; outer sides={tuple(lengths)}")
    print("outer angles: (alpha, alpha+beta, alpha+2beta)")
    print(f"oriented side paths passing straight-vertex stars: {path_counts}")
    print(f"feasible full boundary cycles: {len(feasible)}")
    if not feasible:
        print("boundary-star obstruction: candidate cannot be a tiling")


def main() -> None:
    report(21, (5, 16, 19), 4)
    print()
    report(30, (7, 8, 13), 4)


if __name__ == "__main__":
    main()
