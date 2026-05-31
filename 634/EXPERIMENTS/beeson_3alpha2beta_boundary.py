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
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt


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


def feasible_triquadratic_boundaries(
    tile_sides: tuple[int, int, int],
    outer_sides: tuple[int, int, int],
) -> list[tuple[tuple[PlacedEdge, ...], tuple[PlacedEdge, ...], tuple[PlacedEdge, ...]]]:
    """Return feasible boundary cycles for outer angles `(2alpha,beta,alpha+beta)`.

    `outer_sides` are ordered by opposite angle:

    - side opposite `2alpha`,
    - side opposite `beta`,
    - side opposite `alpha+beta`.
    """
    side_lengths = dict(zip(("a", "b", "c"), tile_sides, strict=True))
    opposite_2alpha, opposite_beta, opposite_alpha_beta = outer_sides

    # Vertices are ordered V0=2alpha, V1=beta, V2=alpha+beta.
    paths_01 = oriented_boundary_paths(opposite_alpha_beta, side_lengths)
    paths_12 = oriented_boundary_paths(opposite_2alpha, side_lengths)
    paths_20 = oriented_boundary_paths(opposite_beta, side_lengths)
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


def feasible_n46_triquadratic_boundaries() -> list[
    tuple[tuple[PlacedEdge, ...], tuple[PlacedEdge, ...], tuple[PlacedEdge, ...]]
]:
    return feasible_triquadratic_boundaries((10, 21, 25), (92, 105, 125))


def feasible_n56_triquadratic_boundaries() -> list[
    tuple[tuple[PlacedEdge, ...], tuple[PlacedEdge, ...], tuple[PlacedEdge, ...]]
]:
    return feasible_triquadratic_boundaries((6, 5, 9), (56, 30, 54))


def heron4(sides: tuple[int, int, int]) -> int:
    a, b, c = sides
    return (a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c)


def primitive_outer_ratio(case: str, tile: tuple[int, int, int]) -> tuple[int, int, int] | None:
    """Return primitive sine-law outer side ratios for selected cases.

    The order is the same as the angle tuple displayed by `case`.
    """
    a, b, c = tile
    if case == "(2a,b,a+b)":
        # Outer angles (2alpha,beta,alpha+beta).
        raw = (a * (b * b + c * c - a * a), b * b * c, b * c * c)
    elif case == "(b,b,3a)":
        # Outer angles (beta,beta,3alpha).  Since 3alpha=pi-2beta,
        # sin(3alpha)/sin(beta)=2cos(beta).
        raw = (a * b * c, a * b * c, b * (a * a + c * c - b * b))
    elif case == "(a,a,a+2b)":
        # Outer angles (alpha,alpha,alpha+2beta)= (alpha,alpha,pi-2alpha).
        raw = (b * c, b * c, b * b + c * c - a * a)
    else:
        return None
    g = abs(raw[0])
    for value in raw[1:]:
        g = gcd(g, abs(value))
    return tuple(value // g for value in raw)


def rational_square_root(value: Fraction) -> Fraction | None:
    if value <= 0:
        return None
    numerator_root = isqrt(value.numerator)
    denominator_root = isqrt(value.denominator)
    if numerator_root * numerator_root != value.numerator:
        return None
    if denominator_root * denominator_root != value.denominator:
        return None
    return Fraction(numerator_root, denominator_root)


def area_normalized_outer_sides(
    n: int, case: str, tile: tuple[int, int, int]
) -> tuple[Fraction, Fraction, Fraction] | None:
    primitive = primitive_outer_ratio(case, tile)
    if primitive is None:
        return None
    scale2 = Fraction(n * heron4(tile), heron4(primitive))
    scale = rational_square_root(scale2)
    if scale is None:
        return None
    return tuple(scale * side for side in primitive)


def boundary_integrality_obstructed(n: int, case: str, tile: tuple[int, int, int]) -> bool:
    if primitive_outer_ratio(case, tile) is None:
        return False
    outer = area_normalized_outer_sides(n, case, tile)
    return outer is None or any(side.denominator != 1 for side in outer)


def n39_isosceles_beta_outer_sides() -> tuple[Fraction, Fraction, Fraction] | None:
    """Return the area-normalized outer sides for the N=39 survivor.

    The candidate has tile `(a,b,c)=(12,7,16)` and outer angles
    `(beta,beta,3alpha)`.  The primitive sine-law ratio is `(448,448,819)`.
    Scaling this ratio to area ratio `N=39` requires an irrational side scale,
    so the function returns `None`.
    """
    outer = area_normalized_outer_sides(39, "(b,b,3a)", (12, 7, 16))
    return outer


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

    print()
    print("N=39 isosceles-beta 3alpha+2beta boundary-integrality check")
    print("tile sides (a,b,c)=(12,7,16); outer angles (beta,beta,3alpha)")
    outer_39 = n39_isosceles_beta_outer_sides()
    print(f"area-normalized outer sides: {outer_39}")
    if outer_39 is None:
        print("boundary-integrality obstruction: area normalization requires an irrational side scale")
    elif any(side.denominator != 1 for side in outer_39):
        print("boundary-integrality obstruction: outer sides are not integer sums of primitive tile sides")

    print()
    print("N=111 isosceles-beta 3alpha+2beta boundary-integrality check")
    print("tile sides (a,b,c)=(42,13,49); outer angles (beta,beta,3alpha)")
    outer_111 = area_normalized_outer_sides(111, "(b,b,3a)", (42, 13, 49))
    print(f"area-normalized outer sides: {outer_111}")
    if outer_111 is None:
        print("boundary-integrality obstruction: area normalization requires an irrational side scale")
    elif any(side.denominator != 1 for side in outer_111):
        print("boundary-integrality obstruction: outer sides are not integer sums of primitive tile sides")

    print()
    print("N=119 triquadratic 3alpha+2beta boundary-integrality checks")
    for tile in ((24, 55, 64), (90, 19, 100)):
        outer_119 = area_normalized_outer_sides(119, "(2a,b,a+b)", tile)
        print(f"tile sides (a,b,c)={tile}; outer angles (2alpha,beta,alpha+beta)")
        print(f"area-normalized outer sides: {outer_119}")
        if outer_119 is None:
            print("boundary-integrality obstruction: area normalization requires an irrational side scale")
        elif any(side.denominator != 1 for side in outer_119):
            print("boundary-integrality obstruction: outer sides are not integer sums of primitive tile sides")

    print()
    print("N=124 triquadratic 3alpha+2beta boundary-integrality check")
    print("tile sides (a,b,c)=(4,15,16); outer angles (2alpha,beta,alpha+beta)")
    outer_124 = area_normalized_outer_sides(124, "(2a,b,a+b)", (4, 15, 16))
    print(f"area-normalized outer sides: {outer_124}")
    if outer_124 is None:
        print("boundary-integrality obstruction: area normalization requires an irrational side scale")
    elif any(side.denominator != 1 for side in outer_124):
        print("boundary-integrality obstruction: outer sides are not integer sums of primitive tile sides")

    for n, tile_sides, outer_sides, feasible_fn in (
        (46, (10, 21, 25), (92, 105, 125), feasible_n46_triquadratic_boundaries),
        (56, (6, 5, 9), (56, 30, 54), feasible_n56_triquadratic_boundaries),
    ):
        side_lengths = dict(zip(("a", "b", "c"), tile_sides, strict=True))
        opposite_2alpha, opposite_beta, opposite_alpha_beta = outer_sides
        paths_a = oriented_boundary_paths(opposite_2alpha, side_lengths)
        paths_b = oriented_boundary_paths(opposite_beta, side_lengths)
        paths_ab = oriented_boundary_paths(opposite_alpha_beta, side_lengths)
        feasible_more = feasible_fn()
        print()
        print(f"N={n} triquadratic 3alpha+2beta boundary-star check")
        print(f"tile sides (a,b,c)={tile_sides}; outer sides {outer_sides}")
        print("outer angles: (2alpha, beta, alpha+beta)")
        print("oriented side paths passing straight-vertex stars:")
        print(f"  opposite 2alpha length {opposite_2alpha}: {len(paths_a)}")
        print(f"  opposite beta length {opposite_beta}: {len(paths_b)}")
        print(f"  opposite alpha+beta length {opposite_alpha_beta}: {len(paths_ab)}")
        print(f"feasible full boundary cycles: {len(feasible_more)}")
        if not feasible_more:
            print("boundary-star obstruction: candidate cannot be a tiling")


if __name__ == "__main__":
    main()
