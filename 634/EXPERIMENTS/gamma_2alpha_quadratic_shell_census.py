#!/usr/bin/env python3
"""Exact quadratic-field shell census for `gamma=2alpha` survivors.

This extends the rational shell classifier to benchmark survivors whose
boundary-shell coordinates lie in a real quadratic field.  The `N=63` survivor
has coordinates in `Q(sqrt(5))`, so exact signs are still decidable by rational
comparisons.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import cmp_to_key
from math import gcd, isqrt, lcm
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import RefinedGamma2AlphaSurvivor, refined_survivors_for_n  # noqa: E402
from gamma_2alpha_boundary_shell import DisjointSet  # noqa: E402
from gamma_2alpha_boundary_transition_demand import BoundaryDemand, path_labels  # noqa: E402
from gamma_2alpha_endpoint_automaton import PlacedEdge, other_side  # noqa: E402
from gamma_2alpha_low_mixed_shell_census import low_mixed_demands  # noqa: E402
from gamma_2alpha_min_shell_census import endpoint_min_demands  # noqa: E402
from gamma_2alpha_random_shell_search import mixed_transitions  # noqa: E402


SIDE_INDEX = {"a": 0, "b": 1, "c": 2}
ANGLE_SIDES: dict[str, frozenset[str]] = {
    "alpha": frozenset(("b", "c")),
    "beta": frozenset(("a", "c")),
    "gamma": frozenset(("a", "b")),
}
RADICAND = 1


@dataclass(frozen=True, order=True)
class Quad:
    rational: Fraction
    radical: Fraction = Fraction(0)


QPoint = tuple[Quad, Quad]
QPolygon = tuple[QPoint, ...]
QSegment = tuple[QPoint, QPoint]
KQuad = tuple[int, int]
KPoint = tuple[KQuad, KQuad]
KPolygon = tuple[KPoint, ...]
KSegment = tuple[KPoint, KPoint]
KLineKey = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


@dataclass(frozen=True)
class QuadraticTile:
    label: str
    edge: PlacedEdge
    polygon: QPolygon


@dataclass(frozen=True)
class IntegerQuadraticTile:
    label: str
    edge: PlacedEdge
    polygon: KPolygon


@dataclass(frozen=True)
class QuadraticShellResult:
    status: str
    forced_corners: int = 0
    label_violations: int = 0


def q(value: int | Fraction, radical: int | Fraction = 0) -> Quad:
    return Quad(Fraction(value), Fraction(radical))


def qneg(value: Quad) -> Quad:
    return Quad(-value.rational, -value.radical)


def qadd(left: Quad, right: Quad) -> Quad:
    return Quad(left.rational + right.rational, left.radical + right.radical)


def qsub(left: Quad, right: Quad) -> Quad:
    return Quad(left.rational - right.rational, left.radical - right.radical)


def qmul(left: Quad, right: Quad) -> Quad:
    return Quad(
        left.rational * right.rational + left.radical * right.radical * RADICAND,
        left.rational * right.radical + left.radical * right.rational,
    )


def qmul_fraction(scale: Fraction, value: Quad) -> Quad:
    return Quad(scale * value.rational, scale * value.radical)


def qdiv_fraction(value: Quad, divisor: Fraction) -> Quad:
    return Quad(value.rational / divisor, value.radical / divisor)


def qsign(value: Quad) -> int:
    """Return the exact sign of `a+b*sqrt(RADICAND)`."""
    a = value.rational
    b = value.radical
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    left = a * a
    right = b * b * RADICAND
    if left == right:
        return 0
    if a > 0:
        return 1 if left > right else -1
    return 1 if right > left else -1


def qcmp(left: Quad, right: Quad) -> int:
    return qsign(qsub(left, right))


def qle(left: Quad, right: Quad) -> bool:
    return qcmp(left, right) <= 0


def qzero(value: Quad) -> bool:
    return value.rational == 0 and value.radical == 0


def qpadd(left: QPoint, right: QPoint) -> QPoint:
    return (qadd(left[0], right[0]), qadd(left[1], right[1]))


def qpsub(left: QPoint, right: QPoint) -> QPoint:
    return (qsub(left[0], right[0]), qsub(left[1], right[1]))


def qpmul(scale: Quad, point: QPoint) -> QPoint:
    return (qmul(scale, point[0]), qmul(scale, point[1]))


def qpdiv_fraction(point: QPoint, divisor: Fraction) -> QPoint:
    return (qdiv_fraction(point[0], divisor), qdiv_fraction(point[1], divisor))


def qdot(left: QPoint, right: QPoint) -> Quad:
    return qadd(qmul(left[0], right[0]), qmul(left[1], right[1]))


def qcross(left: QPoint, right: QPoint) -> Quad:
    return qsub(qmul(left[0], right[1]), qmul(left[1], right[0]))


def qnorm_sq(point: QPoint) -> Quad:
    return qdot(point, point)


def qsigned_area2(poly: QPolygon | tuple[QPoint, ...]) -> Quad:
    total = q(0)
    for index in range(len(poly)):
        total = qadd(total, qcross(poly[index], poly[(index + 1) % len(poly)]))
    return total


def squarefree_int(value: int) -> tuple[int, int]:
    coefficient = 1
    radical = 1
    remaining = value
    factor = 2
    while factor * factor <= remaining:
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        if exponent:
            coefficient *= factor ** (exponent // 2)
            if exponent % 2:
                radical *= factor
        factor += 1
    if remaining > 1:
        radical *= remaining
    return coefficient, radical


def sqrt_fraction_parts(value: Fraction) -> tuple[Fraction, int] | None:
    if value < 0:
        return None
    if value == 0:
        return Fraction(0), 1
    numerator_coeff, numerator_radical = squarefree_int(value.numerator)
    denominator_coeff, denominator_radical = squarefree_int(value.denominator)
    coefficient = Fraction(numerator_coeff, denominator_coeff * denominator_radical)
    return coefficient, numerator_radical * denominator_radical


def sqrt_fraction(value: Fraction) -> Fraction | None:
    parts = sqrt_fraction_parts(value)
    if parts is None:
        return None
    coefficient, radicand = parts
    return coefficient if radicand == 1 else None


def sqrt_quad(value: Fraction, radicand: int) -> Quad | None:
    parts = sqrt_fraction_parts(value)
    if parts is None:
        return None
    coefficient, value_radicand = parts
    if value_radicand == 1:
        return q(coefficient)
    if value_radicand == radicand:
        return q(0, coefficient)
    return None


def field_radicand(survivor: RefinedGamma2AlphaSurvivor) -> int | None:
    candidate = survivor.candidate
    half_base = Fraction(candidate.y, 2)
    outer_height_sq = Fraction(candidate.x * candidate.x) - half_base * half_base
    a, b, c = map(Fraction, candidate.tile)
    semiperimeter = (a + b + c) / 2
    tile_area_sq = semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)
    radicands: set[int] = set()
    for value in (outer_height_sq, tile_area_sq):
        parts = sqrt_fraction_parts(value)
        if parts is None:
            return None
        coefficient, radicand = parts
        if coefficient != 0 and radicand != 1:
            radicands.add(radicand)
    if len(radicands) > 1:
        return None
    return next(iter(radicands), 1)


def outer_vertices(survivor: RefinedGamma2AlphaSurvivor, radicand: int) -> tuple[QPoint, QPoint, QPoint] | None:
    candidate = survivor.candidate
    half_base = Fraction(candidate.y, 2)
    height_sq = Fraction(candidate.x * candidate.x) - half_base * half_base
    height = sqrt_quad(height_sq, radicand)
    if height is None:
        return None
    return ((q(-half_base), q(0)), (q(0), height), (q(half_base), q(0)))


def place_edge_tile(
    *,
    label: str,
    edge: PlacedEdge,
    start: QPoint,
    direction: QPoint,
    offset: Fraction,
    sides: tuple[int, int, int],
    radicand: int,
) -> QuadraticTile | None:
    side_length = Fraction(sides[SIDE_INDEX[edge.side]])
    endpoint = qpadd(start, qpmul(q(offset), direction))
    next_endpoint = qpadd(start, qpmul(q(offset + side_length), direction))
    right_normal = (direction[1], qneg(direction[0]))
    from_start = Fraction(sides[SIDE_INDEX[other_side(edge, edge.start)]])
    from_end = Fraction(sides[SIDE_INDEX[other_side(edge, edge.end)]])
    along = (from_start * from_start + side_length * side_length - from_end * from_end) / (2 * side_length)
    perpendicular = sqrt_quad(from_start * from_start - along * along, radicand)
    if perpendicular is None:
        return None
    third = qpadd(endpoint, qpadd(qpmul(q(along), direction), qpmul(perpendicular, right_normal)))
    return QuadraticTile(label=label, edge=edge, polygon=(endpoint, next_endpoint, third))


def place_boundary_shell(
    survivor: RefinedGamma2AlphaSurvivor,
    demand: BoundaryDemand,
    radicand: int,
) -> tuple[QuadraticTile, ...] | None:
    vertices = outer_vertices(survivor, radicand)
    if vertices is None:
        return None
    left_base, apex, right_base = vertices
    sides = survivor.candidate.tile
    boundary_sides = (
        ("L", left_base, apex, demand.left_path, Fraction(survivor.candidate.x)),
        ("R", apex, right_base, demand.right_path, Fraction(survivor.candidate.x)),
        ("B", right_base, left_base, demand.base_path, Fraction(survivor.candidate.y)),
    )
    tiles: list[QuadraticTile] = []
    for side_name, start, end, path, length in boundary_sides:
        vector = qpsub(end, start)
        direction = qpdiv_fraction(vector, length)
        offset = Fraction(0)
        for index, edge in enumerate(path, start=1):
            tile = place_edge_tile(
                label=f"{side_name}{index}:{edge.side}:{edge.start}->{edge.end}",
                edge=edge,
                start=start,
                direction=direction,
                offset=offset,
                sides=sides,
                radicand=radicand,
            )
            if tile is None:
                return None
            tiles.append(tile)
            offset += sides[SIDE_INDEX[edge.side]]
        if offset != length:
            raise ValueError((side_name, offset, length))
    return tuple(tiles)


def qbbox(poly: QPolygon) -> tuple[Quad, Quad, Quad, Quad]:
    min_x = max_x = poly[0][0]
    min_y = max_y = poly[0][1]
    for x_coord, y_coord in poly[1:]:
        if qcmp(x_coord, min_x) < 0:
            min_x = x_coord
        if qcmp(x_coord, max_x) > 0:
            max_x = x_coord
        if qcmp(y_coord, min_y) < 0:
            min_y = y_coord
        if qcmp(y_coord, max_y) > 0:
            max_y = y_coord
    return min_x, max_x, min_y, max_y


def qbbox_disjoint(
    left: tuple[Quad, Quad, Quad, Quad],
    right: tuple[Quad, Quad, Quad, Quad],
) -> bool:
    return qle(left[1], right[0]) or qle(right[1], left[0]) or qle(left[3], right[2]) or qle(right[3], left[2])


def qccw(poly: QPolygon) -> QPolygon:
    return poly if qsign(qsigned_area2(poly)) > 0 else tuple(reversed(poly))


def qseparated_or_touching(axis_poly: QPolygon, other: QPolygon) -> bool:
    axis_poly = qccw(axis_poly)
    for index in range(len(axis_poly)):
        start = axis_poly[index]
        end = axis_poly[(index + 1) % len(axis_poly)]
        edge = qpsub(end, start)
        if all(qsign(qcross(edge, qpsub(point, start))) <= 0 for point in other):
            return True
    return False


def qpositive_overlap(left: QPolygon, right: QPolygon) -> bool:
    return not qseparated_or_touching(left, right) and not qseparated_or_touching(right, left)


def qsame_triangle(left: QPolygon, right: QPolygon) -> bool:
    return frozenset(left) == frozenset(right)


def qunique_tiles_or_overlap(tiles: tuple[QuadraticTile, ...]) -> tuple[QuadraticTile, ...] | str:
    disjoint = DisjointSet(len(tiles))
    boxes = tuple(qbbox(tile.polygon) for tile in tiles)
    for left in range(len(tiles)):
        for right in range(left + 1, len(tiles)):
            if qbbox_disjoint(boxes[left], boxes[right]):
                continue
            if qsame_triangle(tiles[left].polygon, tiles[right].polygon):
                disjoint.union(left, right)
            elif qpositive_overlap(tiles[left].polygon, tiles[right].polygon):
                return "proper-overlap"
    return tuple(tile for index, tile in enumerate(tiles) if disjoint.find(index) == index)


def qpoint_on_segment(point: QPoint, start: QPoint, end: QPoint) -> bool:
    direction = qpsub(end, start)
    return (
        qzero(qcross(direction, qpsub(point, start)))
        and qsign(qdot(qpsub(point, start), direction)) >= 0
        and qsign(qdot(qpsub(point, end), direction)) <= 0
    )


def qsplit_segment(start: QPoint, end: QPoint, points: tuple[QPoint, ...]) -> tuple[QSegment, ...]:
    direction = qpsub(end, start)
    cuts = {point for point in points if qpoint_on_segment(point, start, end)}

    def compare(left: QPoint, right: QPoint) -> int:
        left_parameter = qdot(qpsub(left, start), direction)
        right_parameter = qdot(qpsub(right, start), direction)
        return qcmp(left_parameter, right_parameter)

    ordered = sorted(cuts, key=cmp_to_key(compare))
    return tuple((ordered[index], ordered[index + 1]) for index in range(len(ordered) - 1) if ordered[index] != ordered[index + 1])


def qsegment_key(start: QPoint, end: QPoint) -> QSegment:
    return (start, end) if start <= end else (end, start)


def qsegment_on_outer(segment: QSegment, outer: tuple[QPoint, QPoint, QPoint]) -> bool:
    start, end = segment
    return any(
        qpoint_on_segment(start, outer[index], outer[(index + 1) % 3])
        and qpoint_on_segment(end, outer[index], outer[(index + 1) % 3])
        for index in range(3)
    )


def edge_labels_for_tile(tile: QuadraticTile) -> tuple[str, str, str]:
    return (
        tile.edge.side,
        other_side(tile.edge, tile.edge.end),
        other_side(tile.edge, tile.edge.start),
    )


def qresidual_segments_with_labels(
    tiles: tuple[QuadraticTile, ...],
    outer: tuple[QPoint, QPoint, QPoint],
) -> dict[QSegment, str]:
    all_points = tuple(point for tile in tiles for point in tile.polygon)
    counts: Counter[QSegment] = Counter()
    labels: dict[QSegment, str] = {}
    for tile in tiles:
        for index, label in enumerate(edge_labels_for_tile(tile)):
            start = tile.polygon[index]
            end = tile.polygon[(index + 1) % 3]
            for atom_start, atom_end in qsplit_segment(start, end, all_points):
                key = qsegment_key(atom_start, atom_end)
                counts[key] += 1
                labels[key] = label
    return {
        key: labels[key]
        for key, count in counts.items()
        if count == 1 and not qsegment_on_outer(key, outer)
    }


def qsimple_cycle(segments: list[QSegment]) -> list[QPoint] | None:
    graph: dict[QPoint, list[QPoint]] = {}
    for start, end in segments:
        graph.setdefault(start, []).append(end)
        graph.setdefault(end, []).append(start)
    if not graph or any(len(neighbors) != 2 for neighbors in graph.values()):
        return None
    start = next(iter(graph))
    cycle = [start]
    previous: QPoint | None = None
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
    if qsign(qsigned_area2(tuple(cycle))) < 0:
        cycle.reverse()
    return cycle


def qside_decomposable(segment: QSegment, sides: tuple[int, int, int]) -> bool:
    length_sq = qnorm_sq(qpsub(segment[1], segment[0]))
    if length_sq.radical != 0:
        return False
    length = sqrt_fraction(length_sq.rational)
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


def qsingle_angle_name(cycle: list[QPoint], index: int, sides: tuple[int, int, int]) -> str | None:
    point = cycle[index]
    previous = cycle[index - 1]
    following = cycle[(index + 1) % len(cycle)]
    first = qpsub(previous, point)
    second = qpsub(following, point)
    if qsign(qcross(first, second)) >= 0:
        return None
    first_length_sq = qnorm_sq(first)
    second_length_sq = qnorm_sq(second)
    if first_length_sq.radical != 0 or second_length_sq.radical != 0:
        return None
    first_length = sqrt_fraction(first_length_sq.rational)
    second_length = sqrt_fraction(second_length_sq.rational)
    if first_length is None or second_length is None:
        return None
    a, b, c = sides
    cosines = {
        "alpha": (b * b + c * c - a * a, 2 * b * c),
        "beta": (a * a + c * c - b * b, 2 * a * c),
    }
    value = qdot(first, second)
    for name, (numerator, denominator) in cosines.items():
        common = gcd(numerator, denominator)
        target = first_length * second_length * Fraction(numerator // common, denominator // common)
        if value == q(target):
            return name
    return None


def qcycle_edge_key(cycle: list[QPoint], index: int) -> QSegment:
    return qsegment_key(cycle[index], cycle[(index + 1) % len(cycle)])


def denominator_scale(shell: tuple[QuadraticTile, ...], outer: tuple[QPoint, QPoint, QPoint]) -> int:
    scale = 1
    for value in (
        coordinate
        for point in (*outer, *(point for tile in shell for point in tile.polygon))
        for coordinate in point
    ):
        if RADICAND == 1:
            scale = lcm(scale, (value.rational + value.radical).denominator)
        else:
            scale = lcm(scale, value.rational.denominator, value.radical.denominator)
    return scale


def kscale_quad(value: Quad, scale: int) -> KQuad:
    if RADICAND == 1:
        scaled = (value.rational + value.radical) * scale
        assert scaled.denominator == 1
        return scaled.numerator, 0
    scaled_rational = value.rational * scale
    scaled_radical = value.radical * scale
    assert scaled_rational.denominator == 1 and scaled_radical.denominator == 1
    return scaled_rational.numerator, scaled_radical.numerator


def kscale_point(point: QPoint, scale: int) -> KPoint:
    return kscale_quad(point[0], scale), kscale_quad(point[1], scale)


def kscale_shell(
    shell: tuple[QuadraticTile, ...],
    outer: tuple[QPoint, QPoint, QPoint],
) -> tuple[tuple[IntegerQuadraticTile, ...], tuple[KPoint, KPoint, KPoint], int]:
    scale = denominator_scale(shell, outer)
    return (
        tuple(
            IntegerQuadraticTile(
                label=tile.label,
                edge=tile.edge,
                polygon=tuple(kscale_point(point, scale) for point in tile.polygon),
            )
            for tile in shell
        ),
        tuple(kscale_point(point, scale) for point in outer),  # type: ignore[return-value]
        scale,
    )


def kadd(left: KQuad, right: KQuad) -> KQuad:
    return left[0] + right[0], left[1] + right[1]


def kneg(value: KQuad) -> KQuad:
    return -value[0], -value[1]


def ksub(left: KQuad, right: KQuad) -> KQuad:
    return left[0] - right[0], left[1] - right[1]


def kmul(left: KQuad, right: KQuad) -> KQuad:
    return left[0] * right[0] + left[1] * right[1] * RADICAND, left[0] * right[1] + left[1] * right[0]


def ksign(value: KQuad) -> int:
    a, b = value
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    left = a * a
    right = b * b * RADICAND
    if left == right:
        return 0
    if a > 0:
        return 1 if left > right else -1
    return 1 if right > left else -1


def kcmp(left: KQuad, right: KQuad) -> int:
    return ksign(ksub(left, right))


def kle(left: KQuad, right: KQuad) -> bool:
    return kcmp(left, right) <= 0


def kzero(value: KQuad) -> bool:
    return value[0] == 0 and value[1] == 0


def kquad_ratio(left: KQuad, right: KQuad) -> tuple[Fraction, Fraction]:
    denominator = right[0] * right[0] - right[1] * right[1] * RADICAND
    if denominator == 0:
        raise ZeroDivisionError(right)
    rational = Fraction(left[0] * right[0] - left[1] * right[1] * RADICAND, denominator)
    radical = Fraction(left[1] * right[0] - left[0] * right[1], denominator)
    return rational, radical


def kpsub(left: KPoint, right: KPoint) -> KPoint:
    return ksub(left[0], right[0]), ksub(left[1], right[1])


def kdot(left: KPoint, right: KPoint) -> KQuad:
    return kadd(kmul(left[0], right[0]), kmul(left[1], right[1]))


def kcross(left: KPoint, right: KPoint) -> KQuad:
    return ksub(kmul(left[0], right[1]), kmul(left[1], right[0]))


def knorm_sq(point: KPoint) -> KQuad:
    return kdot(point, point)


def ksigned_area2(poly: KPolygon | tuple[KPoint, ...]) -> KQuad:
    total = (0, 0)
    for index in range(len(poly)):
        total = kadd(total, kcross(poly[index], poly[(index + 1) % len(poly)]))
    return total


def kbbox(poly: KPolygon) -> tuple[KQuad, KQuad, KQuad, KQuad]:
    min_x = max_x = poly[0][0]
    min_y = max_y = poly[0][1]
    for x_coord, y_coord in poly[1:]:
        if kcmp(x_coord, min_x) < 0:
            min_x = x_coord
        if kcmp(x_coord, max_x) > 0:
            max_x = x_coord
        if kcmp(y_coord, min_y) < 0:
            min_y = y_coord
        if kcmp(y_coord, max_y) > 0:
            max_y = y_coord
    return min_x, max_x, min_y, max_y


def kbbox_disjoint(
    left: tuple[KQuad, KQuad, KQuad, KQuad],
    right: tuple[KQuad, KQuad, KQuad, KQuad],
) -> bool:
    return kle(left[1], right[0]) or kle(right[1], left[0]) or kle(left[3], right[2]) or kle(right[3], left[2])


def kccw(poly: KPolygon) -> KPolygon:
    return poly if ksign(ksigned_area2(poly)) > 0 else tuple(reversed(poly))


def kseparated_or_touching(axis_poly: KPolygon, other: KPolygon) -> bool:
    axis_poly = kccw(axis_poly)
    for index in range(len(axis_poly)):
        start = axis_poly[index]
        end = axis_poly[(index + 1) % len(axis_poly)]
        edge = kpsub(end, start)
        if all(ksign(kcross(edge, kpsub(point, start))) <= 0 for point in other):
            return True
    return False


def kpositive_overlap(left: KPolygon, right: KPolygon) -> bool:
    return not kseparated_or_touching(left, right) and not kseparated_or_touching(right, left)


def ksame_triangle(left: KPolygon, right: KPolygon) -> bool:
    return frozenset(left) == frozenset(right)


def kunique_tiles_or_overlap(tiles: tuple[IntegerQuadraticTile, ...]) -> tuple[IntegerQuadraticTile, ...] | str:
    disjoint = DisjointSet(len(tiles))
    boxes = tuple(kbbox(tile.polygon) for tile in tiles)
    for left in range(len(tiles)):
        for right in range(left + 1, len(tiles)):
            if kbbox_disjoint(boxes[left], boxes[right]):
                continue
            if ksame_triangle(tiles[left].polygon, tiles[right].polygon):
                disjoint.union(left, right)
            elif kpositive_overlap(tiles[left].polygon, tiles[right].polygon):
                return "proper-overlap"
    return tuple(tile for index, tile in enumerate(tiles) if disjoint.find(index) == index)


def kpoint_on_segment(point: KPoint, start: KPoint, end: KPoint) -> bool:
    direction = kpsub(end, start)
    return (
        kzero(kcross(direction, kpsub(point, start)))
        and ksign(kdot(kpsub(point, start), direction)) >= 0
        and ksign(kdot(kpsub(point, end), direction)) <= 0
    )


def kline_coefficients(start: KPoint, end: KPoint) -> tuple[KQuad, KQuad, KQuad]:
    direction = kpsub(end, start)
    a_coeff = kneg(direction[1])
    b_coeff = direction[0]
    c_coeff = ksub(kmul(direction[1], start[0]), kmul(direction[0], start[1]))
    return a_coeff, b_coeff, c_coeff


def kline_key(start: KPoint, end: KPoint) -> KLineKey:
    coefficients = kline_coefficients(start, end)
    pivot = next(coefficient for coefficient in coefficients if not kzero(coefficient))
    return (
        kquad_ratio(coefficients[0], pivot),
        kquad_ratio(coefficients[1], pivot),
        kquad_ratio(coefficients[2], pivot),
    )


def kpoint_on_line_coefficients(point: KPoint, coefficients: tuple[KQuad, KQuad, KQuad]) -> bool:
    a_coeff, b_coeff, c_coeff = coefficients
    return kzero(kadd(kadd(kmul(a_coeff, point[0]), kmul(b_coeff, point[1])), c_coeff))


def ksplit_segment_from_candidates(
    start: KPoint,
    end: KPoint,
    candidates: tuple[KPoint, ...],
) -> tuple[KSegment, ...]:
    direction = kpsub(end, start)
    cuts = {
        point
        for point in candidates
        if ksign(kdot(kpsub(point, start), direction)) >= 0
        and ksign(kdot(kpsub(point, end), direction)) <= 0
    }

    def compare(left: KPoint, right: KPoint) -> int:
        left_parameter = kdot(kpsub(left, start), direction)
        right_parameter = kdot(kpsub(right, start), direction)
        return kcmp(left_parameter, right_parameter)

    ordered = sorted(cuts, key=cmp_to_key(compare))
    return tuple((ordered[index], ordered[index + 1]) for index in range(len(ordered) - 1) if ordered[index] != ordered[index + 1])


def ksplit_segment(start: KPoint, end: KPoint, points: tuple[KPoint, ...]) -> tuple[KSegment, ...]:
    direction = kpsub(end, start)
    cuts = {point for point in points if kpoint_on_segment(point, start, end)}

    def compare(left: KPoint, right: KPoint) -> int:
        left_parameter = kdot(kpsub(left, start), direction)
        right_parameter = kdot(kpsub(right, start), direction)
        return kcmp(left_parameter, right_parameter)

    ordered = sorted(cuts, key=cmp_to_key(compare))
    return tuple((ordered[index], ordered[index + 1]) for index in range(len(ordered) - 1) if ordered[index] != ordered[index + 1])


def ksegment_key(start: KPoint, end: KPoint) -> KSegment:
    return (start, end) if start <= end else (end, start)


def ksegment_on_outer(segment: KSegment, outer: tuple[KPoint, KPoint, KPoint]) -> bool:
    start, end = segment
    return any(
        kpoint_on_segment(start, outer[index], outer[(index + 1) % 3])
        and kpoint_on_segment(end, outer[index], outer[(index + 1) % 3])
        for index in range(3)
    )


def kedge_labels_for_tile(tile: IntegerQuadraticTile) -> tuple[str, str, str]:
    return (
        tile.edge.side,
        other_side(tile.edge, tile.edge.end),
        other_side(tile.edge, tile.edge.start),
    )


def kresidual_segments_with_labels(
    tiles: tuple[IntegerQuadraticTile, ...],
    outer: tuple[KPoint, KPoint, KPoint],
) -> dict[KSegment, str]:
    all_points = tuple(point for tile in tiles for point in tile.polygon)
    line_points_cache: dict[KLineKey, tuple[KPoint, ...]] = {}
    counts: Counter[KSegment] = Counter()
    labels: dict[KSegment, str] = {}
    for tile in tiles:
        for index, label in enumerate(kedge_labels_for_tile(tile)):
            start = tile.polygon[index]
            end = tile.polygon[(index + 1) % 3]
            line_key = kline_key(start, end)
            candidates = line_points_cache.get(line_key)
            if candidates is None:
                coefficients = kline_coefficients(start, end)
                candidates = tuple(point for point in all_points if kpoint_on_line_coefficients(point, coefficients))
                line_points_cache[line_key] = candidates
            for atom_start, atom_end in ksplit_segment_from_candidates(start, end, candidates):
                key = ksegment_key(atom_start, atom_end)
                counts[key] += 1
                labels[key] = label
    return {
        key: labels[key]
        for key, count in counts.items()
        if count == 1 and not ksegment_on_outer(key, outer)
    }


def ksimple_cycle(segments: list[KSegment]) -> list[KPoint] | None:
    graph: dict[KPoint, list[KPoint]] = {}
    for start, end in segments:
        graph.setdefault(start, []).append(end)
        graph.setdefault(end, []).append(start)
    if not graph or any(len(neighbors) != 2 for neighbors in graph.values()):
        return None
    start = next(iter(graph))
    cycle = [start]
    previous: KPoint | None = None
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
    if ksign(ksigned_area2(tuple(cycle))) < 0:
        cycle.reverse()
    return cycle


def kside_decomposable(segment: KSegment, sides: tuple[int, int, int], scale: int) -> bool:
    length_sq = knorm_sq(kpsub(segment[1], segment[0]))
    if length_sq[1] != 0:
        return False
    length = sqrt_fraction(Fraction(length_sq[0], scale * scale))
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


def ksingle_angle_name(cycle: list[KPoint], index: int, sides: tuple[int, int, int], scale: int) -> str | None:
    point = cycle[index]
    previous = cycle[index - 1]
    following = cycle[(index + 1) % len(cycle)]
    first = kpsub(previous, point)
    second = kpsub(following, point)
    if ksign(kcross(first, second)) >= 0:
        return None
    first_length_sq = knorm_sq(first)
    second_length_sq = knorm_sq(second)
    if first_length_sq[1] != 0 or second_length_sq[1] != 0:
        return None
    first_length = sqrt_fraction(Fraction(first_length_sq[0], scale * scale))
    second_length = sqrt_fraction(Fraction(second_length_sq[0], scale * scale))
    if first_length is None or second_length is None:
        return None
    a, b, c = sides
    cosines = {
        "alpha": (b * b + c * c - a * a, 2 * b * c),
        "beta": (a * a + c * c - b * b, 2 * a * c),
    }
    value = kdot(first, second)
    if value[1] != 0:
        return None
    for name, (numerator, denominator) in cosines.items():
        common = gcd(numerator, denominator)
        target = first_length * second_length * Fraction(numerator // common, denominator // common)
        if Fraction(value[0], scale * scale) == target:
            return name
    return None


def kcycle_edge_key(cycle: list[KPoint], index: int) -> KSegment:
    return ksegment_key(cycle[index], cycle[(index + 1) % len(cycle)])


def classify_quadratic_shell(
    survivor: RefinedGamma2AlphaSurvivor,
    demand: BoundaryDemand,
    radicand: int,
) -> QuadraticShellResult:
    global RADICAND
    RADICAND = radicand
    shell = place_boundary_shell(survivor, demand, radicand)
    outer = outer_vertices(survivor, radicand)
    if shell is None or outer is None:
        return QuadraticShellResult("not-quadratic")
    integer_shell, integer_outer, scale = kscale_shell(shell, outer)
    unique_or_status = kunique_tiles_or_overlap(integer_shell)
    if unique_or_status == "proper-overlap":
        return QuadraticShellResult("proper-overlap")
    unique = unique_or_status
    assert isinstance(unique, tuple)
    residual_labels = kresidual_segments_with_labels(unique, integer_outer)
    cycle = ksimple_cycle(list(residual_labels))
    if cycle is None:
        return QuadraticShellResult("not-simple-cycle")
    if any(kside_decomposable(segment, survivor.candidate.tile, scale) for segment in residual_labels):
        return QuadraticShellResult("decomposable-residual-atom")
    forced = 0
    violations = 0
    for index in range(len(cycle)):
        angle_name = ksingle_angle_name(cycle, index, survivor.candidate.tile, scale)
        if angle_name is None:
            continue
        forced += 1
        side_pair = frozenset(
            (
                residual_labels[kcycle_edge_key(cycle, index - 1)],
                residual_labels[kcycle_edge_key(cycle, index)],
            )
        )
        if side_pair != ANGLE_SIDES[angle_name]:
            violations += 1
    if violations:
        return QuadraticShellResult("corner-label-violation", forced, violations)
    return QuadraticShellResult("passes-corner-label-check", forced, violations)


def print_example(status: str, demand: BoundaryDemand, result: QuadraticShellResult) -> None:
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
            radicand = field_radicand(survivor)
            if radicand is None:
                print("  quadratic shell classifier unavailable for this survivor")
                continue
            demands = (
                endpoint_min_demands(survivor)
                if args.endpoint_minimal
                else low_mixed_demands(survivor, max_total_mixed=args.max_total_mixed)
            )
            if args.limit is not None:
                demands = demands[: args.limit]
            counts: Counter[str] = Counter()
            examples: dict[str, tuple[BoundaryDemand, QuadraticShellResult]] = {}
            suffix = ""
            if args.limit is not None:
                suffix = f" (first {args.limit})"
            if args.endpoint_minimal:
                print(f"  Q(sqrt({radicand})) endpoint-minimal shells: {len(demands)}{suffix}", flush=True)
            else:
                print(f"  Q(sqrt({radicand})) shells with total mixed <= {args.max_total_mixed}: {len(demands)}{suffix}", flush=True)
            for demand in demands:
                result = classify_quadratic_shell(survivor, demand, radicand)
                counts[result.status] += 1
                examples.setdefault(result.status, (demand, result))
            print(f"  status counts={dict(sorted(counts.items()))}", flush=True)
            if args.show_examples:
                for status, (demand, result) in sorted(examples.items()):
                    print_example(status, demand, result)


if __name__ == "__main__":
    main()
