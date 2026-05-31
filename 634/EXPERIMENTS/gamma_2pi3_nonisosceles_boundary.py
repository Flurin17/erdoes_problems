#!/usr/bin/env python3
"""Boundary-star checks for selected non-isosceles gamma=2pi/3 candidates.

The exact arithmetic filter gives four BLZ templates.  This script checks the
local boundary-side obstruction common to all four: every outer side is a chain
of full tile sides, every straight boundary vertex has a legal side-label star,
and the three outer corners have the prescribed angle stars.

The endpoint-pair implementation is equivalent to enumerating full boundary
side decompositions for this local obstruction, but it keeps only the first and
last oriented tile side on each outer side.  That is enough for the corner
compatibility checks and keeps larger composite candidates tractable.  Corner
compatibility allows a single tile to occupy the outer corner only when that
outer corner is exactly one tile angle.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache


Angle = str
Side = str
PlacedEdge = tuple[Side, Angle, Angle]
EndpointPair = tuple[PlacedEdge, PlacedEdge]

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
    "2alpha": Counter({"alpha": 2}),
    "2beta": Counter({"beta": 2}),
    "3beta": Counter({"beta": 3}),
    "alpha+beta": Counter({"alpha": 1, "beta": 1}),
    "alpha+2beta": Counter({"alpha": 1, "beta": 2}),
    "2alpha+beta": Counter({"alpha": 2, "beta": 1}),
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


def same_tile_corner_type(left: PlacedEdge, right: PlacedEdge, target_label: str) -> bool:
    """Can `left` and `right` be the two boundary sides of one corner tile?"""
    target = TARGETS[target_label]
    if sum(target.values()) != 1:
        return False
    (target_angle,) = target.elements()
    left_side, _left_start, left_angle = left
    right_side, right_angle, _right_end = right
    if left_angle != target_angle or right_angle != target_angle:
        return False
    return {left_side, right_side} == set(ANGLE_SIDES[target_angle])


def corner_transition_types(left: PlacedEdge, right: PlacedEdge, targets: list[str]) -> set[str]:
    """Return legal corner types, allowing a single tile to occupy the corner."""
    out = transition_types(left, right, targets)
    for label in targets:
        if same_tile_corner_type(left, right, label):
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


@lru_cache(maxsize=None)
def _oriented_boundary_endpoint_pairs_cached(
    length: int, side_lengths_items: tuple[tuple[Side, int], ...]
) -> frozenset[EndpointPair]:
    straight_targets = ["straight-no-gamma", "straight-gamma"]
    side_lengths = dict(side_lengths_items)
    states_by_length: list[set[EndpointPair]] = [set() for _ in range(length + 1)]
    for side, side_length in side_lengths.items():
        if side_length > length:
            continue
        for edge in orientations(side):
            states_by_length[side_length].add((edge, edge))

    for total in range(length + 1):
        for first, last in tuple(states_by_length[total]):
            for side, side_length in side_lengths.items():
                next_total = total + side_length
                if next_total > length:
                    continue
                for edge in orientations(side):
                    if transition_types(last, edge, straight_targets):
                        states_by_length[next_total].add((first, edge))
    return frozenset(states_by_length[length])


def oriented_boundary_endpoint_pairs(length: int, side_lengths: dict[Side, int]) -> set[EndpointPair]:
    """Return possible `(first,last)` oriented edges on a straight boundary side."""
    items = tuple(sorted(side_lengths.items()))
    return set(_oriented_boundary_endpoint_pairs_cached(length, items))


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


def feasible_boundary_endpoint_cycles(
    sides: tuple[int, int, int],
    vertex_angles: tuple[str, str, str],
    opposite_side_lengths: tuple[int, int, int],
) -> set[tuple[EndpointPair, EndpointPair, EndpointPair]]:
    """Return feasible boundary endpoint cycles for a labelled outer triangle.

    This is the finite-state version of `feasible_boundary_by_vertices`: it
    records only the first and last oriented tile side on each outer side.  That
    is enough for the same local straight-boundary and corner-star obstruction.
    """
    side_lengths = dict(zip(("a", "b", "c"), sides, strict=True))
    length_01 = opposite_side_lengths[2]
    length_12 = opposite_side_lengths[0]
    length_20 = opposite_side_lengths[1]
    pairs_01 = oriented_boundary_endpoint_pairs(length_01, side_lengths)
    pairs_12 = oriented_boundary_endpoint_pairs(length_12, side_lengths)
    pairs_20 = oriented_boundary_endpoint_pairs(length_20, side_lengths)
    out: set[tuple[EndpointPair, EndpointPair, EndpointPair]] = set()
    for pair_01 in pairs_01:
        for pair_12 in pairs_12:
            if not corner_transition_types(pair_01[1], pair_12[0], [vertex_angles[1]]):
                continue
            for pair_20 in pairs_20:
                if not corner_transition_types(pair_12[1], pair_20[0], [vertex_angles[2]]):
                    continue
                if not corner_transition_types(pair_20[1], pair_01[0], [vertex_angles[0]]):
                    continue
                out.add((pair_01, pair_12, pair_20))
    return out


def opposite_side_lengths_for_template(
    template: str, sides: tuple[int, int, int], scale: int
) -> tuple[tuple[str, str, str], tuple[int, int, int]]:
    """Return `(vertex_angles, opposite_side_lengths)` for a BLZ template."""
    a, b, c = sides
    vertex_angles = tuple(template.split(","))
    if template == "alpha,alpha+beta,alpha+2beta":
        return (vertex_angles, (scale * a, scale * c, scale * (a + b)))
    if template == "2alpha,2beta,alpha+beta":
        return (
            vertex_angles,
            (scale * a * (a + 2 * b), scale * b * (b + 2 * a), scale * c * c),
        )
    if template == "alpha,2beta,2alpha+beta":
        return (
            vertex_angles,
            (scale * a * c, scale * b * (b + 2 * a), scale * c * (a + b)),
        )
    if template == "alpha,2alpha,3beta":
        return (
            vertex_angles,
            (scale * c * c, scale * c * (a + 2 * b), scale * 3 * b * (a + b)),
        )
    raise ValueError(template)


def feasible_endpoint_cycles_for_template(
    template: str, sides: tuple[int, int, int], scale: int
) -> set[tuple[EndpointPair, EndpointPair, EndpointPair]]:
    vertex_angles, opposite = opposite_side_lengths_for_template(template, sides, scale)
    return feasible_boundary_endpoint_cycles(sides, vertex_angles, opposite)


def boundary_star_obstructed(template: str, sides: tuple[int, int, int], scale: int) -> bool:
    return not feasible_endpoint_cycles_for_template(template, sides, scale)


def feasible_boundary_by_vertices(
    sides: tuple[int, int, int],
    vertex_angles: tuple[str, str, str],
    opposite_side_lengths: tuple[int, int, int],
) -> list[tuple[tuple[PlacedEdge, ...], tuple[PlacedEdge, ...], tuple[PlacedEdge, ...]]]:
    """Return feasible boundary cycles for a triangle with labelled vertex angles.

    The vertices are `V0,V1,V2`.  `opposite_side_lengths[i]` is the side length
    opposite `Vi`.
    """
    side_lengths = dict(zip(("a", "b", "c"), sides, strict=True))
    length_01 = opposite_side_lengths[2]
    length_12 = opposite_side_lengths[0]
    length_20 = opposite_side_lengths[1]
    paths_01 = oriented_boundary_paths(length_01, side_lengths)
    paths_12 = oriented_boundary_paths(length_12, side_lengths)
    paths_20 = oriented_boundary_paths(length_20, side_lengths)
    out = []
    for path_01 in paths_01:
        for path_12 in paths_12:
            if not corner_transition_types(path_01[-1], path_12[0], [vertex_angles[1]]):
                continue
            for path_20 in paths_20:
                if not corner_transition_types(path_12[-1], path_20[0], [vertex_angles[2]]):
                    continue
                if not corner_transition_types(path_20[-1], path_01[0], [vertex_angles[0]]):
                    continue
                out.append((path_01, path_12, path_20))
    return out


def feasible_alpha_2beta_2alpha_beta(
    sides: tuple[int, int, int], scale: int
) -> list[tuple[tuple[PlacedEdge, ...], tuple[PlacedEdge, ...], tuple[PlacedEdge, ...]]]:
    a, b, c = sides
    opposite = (
        scale * a * c,
        scale * b * (b + 2 * a),
        scale * c * (a + b),
    )
    return feasible_boundary_by_vertices(sides, ("alpha", "2beta", "2alpha+beta"), opposite)


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


def report_alpha_2beta_2alpha_beta(n: int, sides: tuple[int, int, int], scale: int) -> None:
    a, b, c = sides
    side_lengths = {"a": a, "b": b, "c": c}
    opposite = (
        scale * a * c,
        scale * b * (b + 2 * a),
        scale * c * (a + b),
    )
    edge_lengths = [opposite[2], opposite[0], opposite[1]]
    path_counts = {length: len(oriented_boundary_paths(length, side_lengths)) for length in edge_lengths}
    feasible = feasible_alpha_2beta_2alpha_beta(sides, scale)
    print(f"N={n} non-isosceles gamma=2pi/3 boundary-star check")
    print(f"tile sides (a,b,c)={sides}; scale={scale}; outer sides={opposite}")
    print("outer angles: (alpha, 2beta, 2alpha+beta)")
    print(f"oriented side paths passing straight-vertex stars: {path_counts}")
    print(f"feasible full boundary cycles: {len(feasible)}")
    if not feasible:
        print("boundary-star obstruction: candidate cannot be a tiling")


def report_endpoint_template(n: int, template: str, sides: tuple[int, int, int], scale: int) -> None:
    vertex_angles, opposite = opposite_side_lengths_for_template(template, sides, scale)
    side_lengths = dict(zip(("a", "b", "c"), sides, strict=True))
    edge_lengths = [opposite[2], opposite[0], opposite[1]]
    pair_counts = {
        length: len(oriented_boundary_endpoint_pairs(length, side_lengths)) for length in edge_lengths
    }
    feasible = feasible_endpoint_cycles_for_template(template, sides, scale)
    print(f"N={n} non-isosceles gamma=2pi/3 endpoint boundary-star check")
    print(f"tile sides (a,b,c)={sides}; scale={scale}; outer sides={opposite}")
    print(f"outer angles: {vertex_angles}")
    print(f"endpoint-pair states passing straight-vertex stars: {pair_counts}")
    print(f"feasible full boundary endpoint cycles: {len(feasible)}")
    if not feasible:
        print("boundary-star obstruction: candidate cannot be a tiling")


def main() -> None:
    checks = (
        (21, "alpha,alpha+beta,alpha+2beta", (5, 16, 19), 4),
        (30, "alpha,alpha+beta,alpha+2beta", (7, 8, 13), 4),
        (55, "alpha,alpha+beta,alpha+2beta", (39, 16, 49), 4),
        (105, "alpha,alpha+beta,alpha+2beta", (8, 7, 13), 7),
        (105, "alpha,alpha+beta,alpha+2beta", (16, 5, 19), 5),
        (120, "alpha,alpha+beta,alpha+2beta", (7, 8, 13), 8),
        (88, "alpha,2beta,2alpha+beta", (3, 5, 7), 1),
        (143, "2alpha,2beta,alpha+beta", (3, 5, 7), 1),
        (143, "2alpha,2beta,alpha+beta", (5, 3, 7), 1),
    )
    for index, (n, template, sides, scale) in enumerate(checks):
        if index:
            print()
        report_endpoint_template(n, template, sides, scale)


if __name__ == "__main__":
    main()
