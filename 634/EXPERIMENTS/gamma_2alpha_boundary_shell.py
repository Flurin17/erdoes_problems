#!/usr/bin/env python3
"""Floating boundary-shell geometry for `gamma=2alpha` survivors.

This diagnostic places the boundary-adjacent tiles dictated by the current
transition-demand witness.  It is meant to seed residual searches and catch
immediate geometric inconsistencies.  It is not a proof of extendability: the
coordinates are floating-point and only the forced boundary shell is checked.
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import RefinedGamma2AlphaSurvivor, refined_survivors_for_n  # noqa: E402
from gamma_2alpha_boundary_transition_demand import (  # noqa: E402
    BoundaryDemand,
    best_demand_for_survivor,
    path_labels,
)
from gamma_2alpha_endpoint_automaton import PlacedEdge, other_side  # noqa: E402


Point = tuple[float, float]
Polygon = tuple[Point, ...]
SIDE_INDEX = {"a": 0, "b": 1, "c": 2}
EPS = 1e-8


@dataclass(frozen=True)
class ShellTile:
    label: str
    edge: PlacedEdge
    polygon: Polygon


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1])


def mul(scale: float, point: Point) -> Point:
    return (scale * point[0], scale * point[1])


def cross(left: Point, right: Point) -> float:
    return left[0] * right[1] - left[1] * right[0]


def norm(point: Point) -> float:
    return math.hypot(point[0], point[1])


def signed_area(poly: Polygon) -> float:
    if len(poly) < 3:
        return 0.0
    return 0.5 * sum(cross(poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly)))


def area(poly: Polygon) -> float:
    return abs(signed_area(poly))


def clip_polygon(poly: list[Point], start: Point, end: Point, *, keep_right: bool) -> list[Point]:
    def inside(point: Point) -> bool:
        value = cross(sub(end, start), sub(point, start))
        return value <= EPS if keep_right else value >= -EPS

    def intersect(left: Point, right: Point) -> Point:
        ray = sub(right, left)
        edge = sub(end, start)
        denominator = cross(ray, edge)
        if abs(denominator) < EPS:
            return left
        factor = cross(sub(start, left), edge) / denominator
        return add(left, mul(factor, ray))

    if not poly:
        return []
    out: list[Point] = []
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


def intersection_area(left: Polygon, right: Polygon) -> float:
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
            return 0.0
    return area(tuple(clipped))


def outer_vertices(survivor: RefinedGamma2AlphaSurvivor) -> tuple[Point, Point, Point]:
    candidate = survivor.candidate
    half_base = candidate.y / 2
    height = math.sqrt(candidate.x * candidate.x - half_base * half_base)
    left_base = (-half_base, 0.0)
    apex = (0.0, height)
    right_base = (half_base, 0.0)
    return left_base, apex, right_base


def place_edge_tile(
    *,
    label: str,
    edge: PlacedEdge,
    start: Point,
    direction: Point,
    offset: float,
    sides: tuple[int, int, int],
) -> ShellTile:
    side_length = sides[SIDE_INDEX[edge.side]]
    endpoint = add(start, mul(offset, direction))
    next_endpoint = add(start, mul(offset + side_length, direction))
    right_normal = (direction[1], -direction[0])
    from_start = sides[SIDE_INDEX[other_side(edge, edge.start)]]
    from_end = sides[SIDE_INDEX[other_side(edge, edge.end)]]
    along = (from_start * from_start + side_length * side_length - from_end * from_end) / (2 * side_length)
    perpendicular_sq = max(0.0, from_start * from_start - along * along)
    third = add(endpoint, add(mul(along, direction), mul(math.sqrt(perpendicular_sq), right_normal)))
    return ShellTile(label=label, edge=edge, polygon=(endpoint, next_endpoint, third))


def place_boundary_shell(survivor: RefinedGamma2AlphaSurvivor, demand: BoundaryDemand) -> tuple[ShellTile, ...]:
    left_base, apex, right_base = outer_vertices(survivor)
    sides = survivor.candidate.tile
    boundary_sides = (
        ("L", left_base, apex, demand.left_path),
        ("R", apex, right_base, demand.right_path),
        ("B", right_base, left_base, demand.base_path),
    )
    tiles: list[ShellTile] = []
    for side_name, start, end, path in boundary_sides:
        vector = sub(end, start)
        length = norm(vector)
        direction = (vector[0] / length, vector[1] / length)
        offset = 0.0
        for index, edge in enumerate(path, start=1):
            tiles.append(
                place_edge_tile(
                    label=f"{side_name}{index}:{edge.side}:{edge.start}->{edge.end}",
                    edge=edge,
                    start=start,
                    direction=direction,
                    offset=offset,
                    sides=sides,
                )
            )
            offset += sides[SIDE_INDEX[edge.side]]
        if abs(offset - length) > 1e-6:
            raise ValueError((side_name, offset, length))
    return tuple(tiles)


def overlap_report(tiles: tuple[ShellTile, ...], tile_area: float) -> tuple[int, list[tuple[float, str, str]], list[tuple[float, str, str]]]:
    dsu = DisjointSet(len(tiles))
    proper: list[tuple[float, str, str]] = []
    duplicates: list[tuple[float, str, str]] = []
    duplicate_threshold = tile_area * (1 - 1e-7)
    overlap_threshold = tile_area * 1e-9
    for left in range(len(tiles)):
        for right in range(left + 1, len(tiles)):
            shared = intersection_area(tiles[left].polygon, tiles[right].polygon)
            if shared >= duplicate_threshold:
                dsu.union(left, right)
                duplicates.append((shared, tiles[left].label, tiles[right].label))
            elif shared > overlap_threshold:
                proper.append((shared, tiles[left].label, tiles[right].label))
    unique_count = len({dsu.find(index) for index in range(len(tiles))})
    return unique_count, duplicates, proper


def tile_area_from_sides(sides: tuple[int, int, int]) -> float:
    a, b, c = sides
    semi = (a + b + c) / 2
    return math.sqrt(semi * (semi - a) * (semi - b) * (semi - c))


def format_point(point: Point) -> str:
    return f"({point[0]:.9g},{point[1]:.9g})"


def print_shell(n: int, survivor: RefinedGamma2AlphaSurvivor, demand: BoundaryDemand, *, show_tiles: bool) -> None:
    tiles = place_boundary_shell(survivor, demand)
    tile_area = tile_area_from_sides(survivor.candidate.tile)
    unique_count, duplicates, proper = overlap_report(tiles, tile_area)
    remaining_tiles = n - unique_count
    print(f"N={n}: tile={survivor.candidate.tile}, X={survivor.candidate.x}, Y={survivor.candidate.y}")
    print(
        f"  boundary words: L={path_labels(demand.left_path)} "
        f"R={path_labels(demand.right_path)} B={path_labels(demand.base_path)}"
    )
    print(
        f"  boundary edges={len(tiles)}, duplicate corner pairs={len(duplicates)}, "
        f"unique boundary-shell tiles={unique_count}, remaining tile areas={remaining_tiles}"
    )
    if duplicates:
        for shared, left, right in duplicates:
            print(f"    duplicate: {left} == {right} shared_area={shared:.12g}")
    if proper:
        print(f"  proper positive-area overlaps={len(proper)}")
        for shared, left, right in sorted(proper, reverse=True)[:12]:
            print(f"    overlap: {left} with {right} area={shared:.12g}")
    else:
        print("  proper positive-area overlaps=0")
    if show_tiles:
        for tile in tiles:
            vertices = " ".join(format_point(point) for point in tile.polygon)
            print(f"    {tile.label}: {vertices}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--show-tiles", action="store_true")
    args = parser.parse_args()

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
        for survivor in survivors:
            demand = best_demand_for_survivor(survivor)
            if demand is None:
                print("  no transition-demand witness")
                continue
            print_shell(n, survivor, demand, show_tiles=args.show_tiles)


if __name__ == "__main__":
    main()
