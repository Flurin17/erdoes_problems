#!/usr/bin/env python3
"""Exact rational shell census for rational `gamma=2alpha` survivors.

This is an exact-arithmetic counterpart to the floating shell classifier used
by `gamma_2alpha_low_mixed_shell_census.py`.  It applies only when the outer
triangle and every boundary-adjacent tile placement have rational coordinates.
The benchmark `N=99` survivor has this property.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import RefinedGamma2AlphaSurvivor, refined_survivors_for_n  # noqa: E402
from gamma_2alpha_boundary_shell import DisjointSet  # noqa: E402
from gamma_2alpha_boundary_transition_demand import BoundaryDemand, path_labels  # noqa: E402
from gamma_2alpha_endpoint_automaton import PlacedEdge, other_side  # noqa: E402
from gamma_2alpha_low_mixed_shell_census import low_mixed_demands  # noqa: E402
from gamma_2alpha_min_shell_census import endpoint_min_demands  # noqa: E402
from gamma_2alpha_random_shell_search import mixed_transitions  # noqa: E402


FPoint = tuple[Fraction, Fraction]
FPolygon = tuple[FPoint, ...]
FSegment = tuple[FPoint, FPoint]
SIDE_INDEX = {"a": 0, "b": 1, "c": 2}
ANGLE_SIDES: dict[str, frozenset[str]] = {
    "alpha": frozenset(("b", "c")),
    "beta": frozenset(("a", "c")),
    "gamma": frozenset(("a", "b")),
}


@dataclass(frozen=True)
class RationalTile:
    label: str
    edge: PlacedEdge
    polygon: FPolygon


@dataclass(frozen=True)
class RationalShellResult:
    status: str
    forced_corners: int = 0
    label_violations: int = 0


def sqrt_fraction(value: Fraction) -> Fraction | None:
    if value < 0:
        return None
    numerator = isqrt(value.numerator)
    denominator = isqrt(value.denominator)
    if numerator * numerator == value.numerator and denominator * denominator == value.denominator:
        return Fraction(numerator, denominator)
    return None


def add(left: FPoint, right: FPoint) -> FPoint:
    return (left[0] + right[0], left[1] + right[1])


def sub(left: FPoint, right: FPoint) -> FPoint:
    return (left[0] - right[0], left[1] - right[1])


def mul(scale: Fraction, point: FPoint) -> FPoint:
    return (scale * point[0], scale * point[1])


def dot(left: FPoint, right: FPoint) -> Fraction:
    return left[0] * right[0] + left[1] * right[1]


def cross(left: FPoint, right: FPoint) -> Fraction:
    return left[0] * right[1] - left[1] * right[0]


def norm_sq(point: FPoint) -> Fraction:
    return dot(point, point)


def signed_area(poly: FPolygon) -> Fraction:
    if len(poly) < 3:
        return Fraction(0)
    return Fraction(1, 2) * sum(cross(poly[index], poly[(index + 1) % len(poly)]) for index in range(len(poly)))


def area(poly: FPolygon) -> Fraction:
    value = signed_area(poly)
    return value if value >= 0 else -value


def outer_vertices(survivor: RefinedGamma2AlphaSurvivor) -> tuple[FPoint, FPoint, FPoint] | None:
    candidate = survivor.candidate
    half_base = Fraction(candidate.y, 2)
    height = sqrt_fraction(Fraction(candidate.x * candidate.x) - half_base * half_base)
    if height is None:
        return None
    return ((-half_base, Fraction(0)), (Fraction(0), height), (half_base, Fraction(0)))


def place_edge_tile(
    *,
    label: str,
    edge: PlacedEdge,
    start: FPoint,
    direction: FPoint,
    offset: Fraction,
    sides: tuple[int, int, int],
) -> RationalTile | None:
    side_length = Fraction(sides[SIDE_INDEX[edge.side]])
    endpoint = add(start, mul(offset, direction))
    next_endpoint = add(start, mul(offset + side_length, direction))
    right_normal = (direction[1], -direction[0])
    from_start = Fraction(sides[SIDE_INDEX[other_side(edge, edge.start)]])
    from_end = Fraction(sides[SIDE_INDEX[other_side(edge, edge.end)]])
    along = (from_start * from_start + side_length * side_length - from_end * from_end) / (2 * side_length)
    perpendicular = sqrt_fraction(from_start * from_start - along * along)
    if perpendicular is None:
        return None
    third = add(endpoint, add(mul(along, direction), mul(perpendicular, right_normal)))
    return RationalTile(label=label, edge=edge, polygon=(endpoint, next_endpoint, third))


def place_boundary_shell(survivor: RefinedGamma2AlphaSurvivor, demand: BoundaryDemand) -> tuple[RationalTile, ...] | None:
    vertices = outer_vertices(survivor)
    if vertices is None:
        return None
    left_base, apex, right_base = vertices
    sides = survivor.candidate.tile
    boundary_sides = (
        ("L", left_base, apex, demand.left_path, Fraction(survivor.candidate.x)),
        ("R", apex, right_base, demand.right_path, Fraction(survivor.candidate.x)),
        ("B", right_base, left_base, demand.base_path, Fraction(survivor.candidate.y)),
    )
    tiles: list[RationalTile] = []
    for side_name, start, end, path, length in boundary_sides:
        vector = sub(end, start)
        direction = (vector[0] / length, vector[1] / length)
        offset = Fraction(0)
        for index, edge in enumerate(path, start=1):
            tile = place_edge_tile(
                label=f"{side_name}{index}:{edge.side}:{edge.start}->{edge.end}",
                edge=edge,
                start=start,
                direction=direction,
                offset=offset,
                sides=sides,
            )
            if tile is None:
                return None
            tiles.append(tile)
            offset += sides[SIDE_INDEX[edge.side]]
        if offset != length:
            raise ValueError((side_name, offset, length))
    return tuple(tiles)


def clip_polygon(poly: list[FPoint], start: FPoint, end: FPoint, *, keep_right: bool) -> list[FPoint]:
    def inside(point: FPoint) -> bool:
        value = cross(sub(end, start), sub(point, start))
        return value <= 0 if keep_right else value >= 0

    def intersect(left: FPoint, right: FPoint) -> FPoint:
        ray = sub(right, left)
        edge = sub(end, start)
        denominator = cross(ray, edge)
        if denominator == 0:
            return left
        factor = cross(sub(start, left), edge) / denominator
        return add(left, mul(factor, ray))

    if not poly:
        return []
    out: list[FPoint] = []
    previous = poly[-1]
    previous_inside = inside(previous)
    for current in poly:
        current_inside = inside(current)
        if current_inside:
            if not previous_inside:
                out.append(intersect(previous, current))
            out.append(current)
        elif previous_inside:
            out.append(intersect(previous, current))
        previous = current
        previous_inside = current_inside
    return out


def intersection_area(left: FPolygon, right: FPolygon) -> Fraction:
    right_is_ccw = signed_area(right) > 0
    clipped = list(left)
    for index in range(len(right)):
        clipped = clip_polygon(
            clipped,
            right[index],
            right[(index + 1) % len(right)],
            keep_right=not right_is_ccw,
        )
        if not clipped:
            return Fraction(0)
    return area(tuple(clipped))


def tile_area_from_sides(sides: tuple[int, int, int]) -> Fraction | None:
    a, b, c = map(Fraction, sides)
    semi = (a + b + c) / 2
    return sqrt_fraction(semi * (semi - a) * (semi - b) * (semi - c))


def bbox(poly: FPolygon) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    return (
        min(point[0] for point in poly),
        max(point[0] for point in poly),
        min(point[1] for point in poly),
        max(point[1] for point in poly),
    )


def bbox_disjoint(left: tuple[Fraction, Fraction, Fraction, Fraction], right: tuple[Fraction, Fraction, Fraction, Fraction]) -> bool:
    return left[1] <= right[0] or right[1] <= left[0] or left[3] <= right[2] or right[3] <= left[2]


def ccw(poly: FPolygon) -> FPolygon:
    return poly if signed_area(poly) > 0 else tuple(reversed(poly))


def separated_or_touching(axis_poly: FPolygon, other: FPolygon) -> bool:
    axis_poly = ccw(axis_poly)
    for index in range(len(axis_poly)):
        start = axis_poly[index]
        end = axis_poly[(index + 1) % len(axis_poly)]
        edge = sub(end, start)
        values = [cross(edge, sub(point, start)) for point in other]
        if max(values) <= 0:
            return True
    return False


def positive_overlap(left: FPolygon, right: FPolygon) -> bool:
    """Return whether two non-identical triangles overlap in positive area."""
    return not separated_or_touching(left, right) and not separated_or_touching(right, left)


def same_triangle(left: FPolygon, right: FPolygon) -> bool:
    return frozenset(left) == frozenset(right)


def unique_tiles_or_overlap(tiles: tuple[RationalTile, ...], _tile_area: Fraction) -> tuple[RationalTile, ...] | str:
    disjoint = DisjointSet(len(tiles))
    boxes = tuple(bbox(tile.polygon) for tile in tiles)
    for left in range(len(tiles)):
        for right in range(left + 1, len(tiles)):
            if bbox_disjoint(boxes[left], boxes[right]):
                continue
            if same_triangle(tiles[left].polygon, tiles[right].polygon):
                disjoint.union(left, right)
            elif positive_overlap(tiles[left].polygon, tiles[right].polygon):
                return "proper-overlap"
    return tuple(tile for index, tile in enumerate(tiles) if disjoint.find(index) == index)


def point_on_segment(point: FPoint, start: FPoint, end: FPoint) -> bool:
    direction = sub(end, start)
    return cross(direction, sub(point, start)) == 0 and dot(sub(point, start), direction) >= 0 and dot(sub(point, end), direction) <= 0


def split_segment(start: FPoint, end: FPoint, points: tuple[FPoint, ...]) -> tuple[FSegment, ...]:
    direction = sub(end, start)
    length_sq = norm_sq(direction)
    cuts = {Fraction(0), Fraction(1)}
    for point in points:
        if point_on_segment(point, start, end):
            parameter = dot(sub(point, start), direction) / length_sq
            if 0 < parameter < 1:
                cuts.add(parameter)
    ordered = sorted(cuts)
    return tuple(
        (add(start, mul(ordered[index], direction)), add(start, mul(ordered[index + 1], direction)))
        for index in range(len(ordered) - 1)
        if ordered[index] != ordered[index + 1]
    )


def segment_key(start: FPoint, end: FPoint) -> FSegment:
    return (start, end) if start <= end else (end, start)


def segment_on_outer(segment: FSegment, outer: tuple[FPoint, FPoint, FPoint]) -> bool:
    start, end = segment
    return any(
        point_on_segment(start, outer[index], outer[(index + 1) % 3])
        and point_on_segment(end, outer[index], outer[(index + 1) % 3])
        for index in range(3)
    )


def edge_labels_for_tile(tile: RationalTile) -> tuple[str, str, str]:
    return (
        tile.edge.side,
        other_side(tile.edge, tile.edge.end),
        other_side(tile.edge, tile.edge.start),
    )


def residual_segments_with_labels(
    tiles: tuple[RationalTile, ...],
    outer: tuple[FPoint, FPoint, FPoint],
) -> dict[FSegment, str]:
    all_points = tuple(point for tile in tiles for point in tile.polygon)
    counts: Counter[FSegment] = Counter()
    labels: dict[FSegment, str] = {}
    for tile in tiles:
        for index, label in enumerate(edge_labels_for_tile(tile)):
            start = tile.polygon[index]
            end = tile.polygon[(index + 1) % 3]
            for atom_start, atom_end in split_segment(start, end, all_points):
                key = segment_key(atom_start, atom_end)
                counts[key] += 1
                labels[key] = label
    return {
        key: labels[key]
        for key, count in counts.items()
        if count == 1 and not segment_on_outer(key, outer)
    }


def simple_cycle(segments: list[FSegment]) -> list[FPoint] | None:
    graph: dict[FPoint, list[FPoint]] = {}
    for start, end in segments:
        graph.setdefault(start, []).append(end)
        graph.setdefault(end, []).append(start)
    if not graph or any(len(neighbors) != 2 for neighbors in graph.values()):
        return None
    start = min(graph)
    cycle = [start]
    previous: FPoint | None = None
    current = start
    while True:
        first, second = graph[current]
        following = first if first != previous else second
        if following == start:
            break
        cycle.append(following)
        previous, current = current, following
        if len(cycle) > len(graph):
            return None
    if len(cycle) != len(graph):
        return None
    if signed_area(tuple(cycle)) < 0:
        cycle.reverse()
    return cycle


def side_decomposable(segment: FSegment, sides: tuple[int, int, int]) -> bool:
    length_sq = norm_sq(sub(segment[1], segment[0]))
    length = sqrt_fraction(length_sq)
    if length is None:
        return False
    limit = int(length // min(sides)) + 1
    for a_count in range(limit + 1):
        for b_count in range(limit + 1):
            for c_count in range(limit + 1):
                if a_count + b_count + c_count < 2:
                    continue
                if a_count * sides[0] + b_count * sides[1] + c_count * sides[2] == length:
                    return True
    return False


def single_angle_name(cycle: list[FPoint], index: int, sides: tuple[int, int, int]) -> str | None:
    point = cycle[index]
    previous = cycle[index - 1]
    following = cycle[(index + 1) % len(cycle)]
    first = sub(previous, point)
    second = sub(following, point)
    # A one-tile angle is less than pi; for a CCW residual cycle this means a
    # right turn from the incoming residual edge to the outgoing one.
    if cross(first, second) >= 0:
        return None
    first_length = sqrt_fraction(norm_sq(first))
    second_length = sqrt_fraction(norm_sq(second))
    if first_length is None or second_length is None:
        return None
    a, b, c = map(Fraction, sides)
    cosines = {
        "alpha": (b * b + c * c - a * a) / (2 * b * c),
        "beta": (a * a + c * c - b * b) / (2 * a * c),
        "gamma": (a * a + b * b - c * c) / (2 * a * b),
    }
    value = dot(first, second)
    for name, cosine in cosines.items():
        # In this branch gamma=2alpha, so a gamma-sized residual angle is not a
        # uniquely forced one-tile corner.
        if name == "gamma":
            continue
        if value == first_length * second_length * cosine:
            return name
    return None


def cycle_edge_key(cycle: list[FPoint], index: int) -> FSegment:
    return segment_key(cycle[index], cycle[(index + 1) % len(cycle)])


def classify_rational_shell(
    survivor: RefinedGamma2AlphaSurvivor,
    demand: BoundaryDemand,
) -> RationalShellResult:
    shell = place_boundary_shell(survivor, demand)
    tile_area = tile_area_from_sides(survivor.candidate.tile)
    outer = outer_vertices(survivor)
    if shell is None or tile_area is None or outer is None:
        return RationalShellResult("not-rational")
    unique_or_status = unique_tiles_or_overlap(shell, tile_area)
    if unique_or_status == "proper-overlap":
        return RationalShellResult("proper-overlap")
    unique = unique_or_status
    assert isinstance(unique, tuple)
    residual_labels = residual_segments_with_labels(unique, outer)
    cycle = simple_cycle(list(residual_labels))
    if cycle is None:
        return RationalShellResult("not-simple-cycle")
    if any(side_decomposable(segment, survivor.candidate.tile) for segment in residual_labels):
        return RationalShellResult("decomposable-residual-atom")
    forced = 0
    violations = 0
    for index in range(len(cycle)):
        angle_name = single_angle_name(cycle, index, survivor.candidate.tile)
        if angle_name is None:
            continue
        forced += 1
        side_pair = frozenset(
            (
                residual_labels[cycle_edge_key(cycle, index - 1)],
                residual_labels[cycle_edge_key(cycle, index)],
            )
        )
        if side_pair != ANGLE_SIDES[angle_name]:
            violations += 1
    if violations:
        return RationalShellResult("corner-label-violation", forced, violations)
    return RationalShellResult("passes-corner-label-check", forced, violations)


def print_example(status: str, demand: BoundaryDemand, result: RationalShellResult) -> None:
    print(
        f"    {status}: forced={result.forced_corners}, "
        f"violations={result.label_violations}, "
        f"L={path_labels(demand.left_path)} "
        f"R={path_labels(demand.right_path)} "
        f"B={path_labels(demand.base_path)} "
        f"mixed={mixed_transitions(demand.left_path) + mixed_transitions(demand.right_path) + mixed_transitions(demand.base_path)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--max-total-mixed", type=int, default=4)
    parser.add_argument("--endpoint-minimal", action="store_true")
    parser.add_argument("--limit", type=int, help="classify only the first LIMIT shells")
    parser.add_argument("--show-examples", action="store_true")
    args = parser.parse_args()

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
        for survivor in survivors:
            if outer_vertices(survivor) is None or tile_area_from_sides(survivor.candidate.tile) is None:
                print("  rational shell classifier unavailable for this survivor")
                continue
            demands = (
                endpoint_min_demands(survivor)
                if args.endpoint_minimal
                else low_mixed_demands(survivor, max_total_mixed=args.max_total_mixed)
            )
            if args.limit is not None:
                demands = demands[: args.limit]
            counts: Counter[str] = Counter()
            examples: dict[str, tuple[BoundaryDemand, RationalShellResult]] = {}
            suffix = ""
            if args.limit is not None:
                suffix = f" (first {args.limit})"
            if args.endpoint_minimal:
                print(f"  rational endpoint-minimal shells: {len(demands)}{suffix}", flush=True)
            else:
                print(f"  rational exact shells with total mixed <= {args.max_total_mixed}: {len(demands)}{suffix}", flush=True)
            for demand in demands:
                result = classify_rational_shell(survivor, demand)
                counts[result.status] += 1
                examples.setdefault(result.status, (demand, result))
            print(f"  status counts={dict(sorted(counts.items()))}", flush=True)
            if args.show_examples:
                for status, (demand, result) in sorted(examples.items()):
                    print_example(status, demand, result)


if __name__ == "__main__":
    main()
