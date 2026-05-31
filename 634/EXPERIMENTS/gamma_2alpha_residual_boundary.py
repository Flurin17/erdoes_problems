#!/usr/bin/env python3
"""Residual boundary graph after the `gamma=2alpha` boundary shell.

This diagnostic removes duplicate base-corner tiles from the boundary shell,
splits shell edges at all shell vertices, and reports the remaining non-outer
boundary atoms.  It is a preparatory step for residual exact-cover searches.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import refined_survivors_for_n  # noqa: E402
from gamma_2alpha_boundary_shell import (  # noqa: E402
    Point,
    ShellTile,
    intersection_area,
    outer_vertices,
    place_boundary_shell,
    tile_area_from_sides,
)
from gamma_2alpha_boundary_transition_demand import best_demand_for_survivor  # noqa: E402


Segment = tuple[Point, Point]
SegmentKey = tuple[tuple[float, float], tuple[float, float]]
EPS = 1e-7


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1])


def mul(scale: float, point: Point) -> Point:
    return (scale * point[0], scale * point[1])


def dot(left: Point, right: Point) -> float:
    return left[0] * right[0] + left[1] * right[1]


def cross(left: Point, right: Point) -> float:
    return left[0] * right[1] - left[1] * right[0]


def norm_sq(point: Point) -> float:
    return dot(point, point)


def point_key(point: Point, digits: int) -> tuple[float, float]:
    return (round(point[0], digits), round(point[1], digits))


def segment_key(start: Point, end: Point, digits: int) -> SegmentKey:
    first = point_key(start, digits)
    second = point_key(end, digits)
    return (first, second) if first <= second else (second, first)


def point_on_segment(point: Point, start: Point, end: Point, *, eps: float) -> bool:
    direction = sub(end, start)
    if abs(cross(direction, sub(point, start))) > eps:
        return False
    return dot(sub(point, start), direction) >= -eps and dot(sub(point, end), direction) <= eps


def split_segment(start: Point, end: Point, points: tuple[Point, ...], *, eps: float) -> tuple[Segment, ...]:
    direction = sub(end, start)
    length_sq = norm_sq(direction)
    cuts = [0.0, 1.0]
    for point in points:
        if not point_on_segment(point, start, end, eps=eps):
            continue
        parameter = dot(sub(point, start), direction) / length_sq
        if eps < parameter < 1 - eps:
            cuts.append(parameter)
    ordered = sorted(set(round(cut, 10) for cut in cuts))
    return tuple(
        (add(start, mul(ordered[index], direction)), add(start, mul(ordered[index + 1], direction)))
        for index in range(len(ordered) - 1)
        if ordered[index + 1] - ordered[index] > eps
    )


def segment_on_outer(segment: SegmentKey, outer: tuple[Point, Point, Point], *, eps: float) -> bool:
    start, end = segment
    for index in range(3):
        if point_on_segment(start, outer[index], outer[(index + 1) % 3], eps=eps) and point_on_segment(
            end,
            outer[index],
            outer[(index + 1) % 3],
            eps=eps,
        ):
            return True
    return False


def unique_shell_tiles(tiles: tuple[ShellTile, ...], tile_area: float) -> tuple[ShellTile, ...]:
    duplicate = [False] * len(tiles)
    for left in range(len(tiles)):
        if duplicate[left]:
            continue
        for right in range(left + 1, len(tiles)):
            if duplicate[right]:
                continue
            shared = intersection_area(tiles[left].polygon, tiles[right].polygon)
            if shared > tile_area * (1 - 1e-7):
                duplicate[right] = True
    return tuple(tile for index, tile in enumerate(tiles) if not duplicate[index])


def residual_atoms(
    tiles: tuple[ShellTile, ...],
    outer: tuple[Point, Point, Point],
    *,
    digits: int,
    eps: float,
) -> tuple[
    dict[SegmentKey, int],
    list[SegmentKey],
    list[SegmentKey],
    list[SegmentKey],
    list[tuple[SegmentKey, int]],
]:
    all_points: list[Point] = []
    raw_edges: list[Segment] = []
    for tile in tiles:
        all_points.extend(tile.polygon)
        for index in range(3):
            raw_edges.append((tile.polygon[index], tile.polygon[(index + 1) % 3]))

    counts: Counter[SegmentKey] = Counter()
    for start, end in raw_edges:
        for atom_start, atom_end in split_segment(start, end, tuple(all_points), eps=eps):
            counts[segment_key(atom_start, atom_end, digits)] += 1

    residual: list[SegmentKey] = []
    outer_atoms: list[SegmentKey] = []
    shared: list[SegmentKey] = []
    weird: list[tuple[SegmentKey, int]] = []
    for atom, count in counts.items():
        if count == 1 and segment_on_outer(atom, outer, eps=eps):
            outer_atoms.append(atom)
        elif count == 1:
            residual.append(atom)
        elif count == 2:
            shared.append(atom)
        else:
            weird.append((atom, count))
    return dict(counts), residual, outer_atoms, shared, weird


def component_summaries(segments: list[SegmentKey]) -> tuple[Counter[int], list[tuple[int, int, Counter[int]]]]:
    graph: dict[tuple[float, float], list[tuple[float, float]]] = defaultdict(list)
    for start, end in segments:
        graph[start].append(end)
        graph[end].append(start)
    degree_histogram = Counter(len(neighbors) for neighbors in graph.values())
    seen: set[tuple[float, float]] = set()
    components: list[tuple[int, int, Counter[int]]] = []
    for vertex in graph:
        if vertex in seen:
            continue
        stack = [vertex]
        seen.add(vertex)
        vertices: list[tuple[float, float]] = []
        edge_sum = 0
        while stack:
            current = stack.pop()
            vertices.append(current)
            edge_sum += len(graph[current])
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        components.append((len(vertices), edge_sum // 2, Counter(len(graph[item]) for item in vertices)))
    return degree_histogram, components


def write_svg(
    path: Path,
    outer: tuple[Point, Point, Point],
    tiles: tuple[ShellTile, ...],
    residual: list[SegmentKey],
) -> None:
    points = [point for tile in tiles for point in tile.polygon] + list(outer)
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    width = max_x - min_x
    height = max_y - min_y

    def map_point(point: Point) -> tuple[float, float]:
        return (point[0] - min_x + 10, max_y - point[1] + 10)

    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width + 20:.6g} {height + 20:.6g}">',
        '<g fill="none" stroke-linejoin="round" stroke-linecap="round">',
    ]
    outer_points = " ".join(f"{x:.6g},{y:.6g}" for x, y in (map_point(point) for point in outer))
    lines.append(f'<polygon points="{outer_points}" stroke="#333" stroke-width="0.8"/>')
    for tile in tiles:
        tile_points = " ".join(f"{x:.6g},{y:.6g}" for x, y in (map_point(point) for point in tile.polygon))
        lines.append(f'<polygon points="{tile_points}" stroke="#999" stroke-width="0.35"/>')
    for start, end in residual:
        x1, y1 = map_point(start)
        x2, y2 = map_point(end)
        lines.append(f'<line x1="{x1:.6g}" y1="{y1:.6g}" x2="{x2:.6g}" y2="{y2:.6g}" stroke="#c00" stroke-width="0.9"/>')
    lines.append("</g></svg>")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--digits", type=int, default=7)
    parser.add_argument("--eps", type=float, default=1e-7)
    parser.add_argument("--svg-dir", type=Path)
    args = parser.parse_args()

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
        for survivor in survivors:
            demand = best_demand_for_survivor(survivor)
            if demand is None:
                print("  no transition-demand witness")
                continue
            shell = place_boundary_shell(survivor, demand)
            tile_area = tile_area_from_sides(survivor.candidate.tile)
            unique = unique_shell_tiles(shell, tile_area)
            outer = outer_vertices(survivor)
            atoms, residual, outer_atoms, shared, weird = residual_atoms(
                unique,
                outer,
                digits=args.digits,
                eps=args.eps,
            )
            degree_histogram, components = component_summaries(residual)
            print(
                f"  unique shell tiles={len(unique)}; atoms={len(atoms)}; "
                f"residual segments={len(residual)}; outer atoms={len(outer_atoms)}; "
                f"shared shell atoms={len(shared)}; weird atoms={len(weird)}"
            )
            print(f"  residual degree histogram={dict(sorted(degree_histogram.items()))}")
            print(f"  residual components={components}")
            if args.svg_dir is not None:
                args.svg_dir.mkdir(parents=True, exist_ok=True)
                path = args.svg_dir / f"gamma_2alpha_residual_{n}.svg"
                write_svg(path, outer, unique, residual)
                print(f"  wrote {path}")


if __name__ == "__main__":
    main()
