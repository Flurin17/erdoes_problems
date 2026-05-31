#!/usr/bin/env python3
"""Lattice-aligned exact-cover test for equilateral candidates.

Coordinates use the triangular lattice axial norm `x^2 + x*y + y^2`.  The
outer equilateral triangle has vertices `(0,0), (L,0), (0,L)`.

For a 2pi/3 tile with sides `(a,b,c)`, use vertices
`(0,0), (a,0), (-b,b)`.

For a pi/3 tile with sides `(a,b,c)`, use vertices
`(0,0), (a,0), (0,b)`.

The test enumerates all dihedral images and lattice translations of the tile
inside the outer triangle, then solves exact cover on unit triangular cells.
Failure is only a lattice-aligned obstruction.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from math import isqrt


Point = tuple[int, int]
Cell = tuple[int, int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]


@dataclass(frozen=True)
class Instance:
    n: int
    angle: str
    a: int
    b: int

    @property
    def c(self) -> int:
        sign = 1 if self.angle == "2pi/3" else -1
        c2 = self.a * self.a + sign * self.a * self.b + self.b * self.b
        c = isqrt(c2)
        if c * c != c2:
            raise ValueError("side data do not satisfy the requested angle relation")
        return c

    @property
    def outer_side(self) -> int:
        side2 = self.n * self.a * self.b
        side = isqrt(side2)
        if side * side != side2:
            raise ValueError("area equation does not give an integer outer side")
        return side

    @property
    def tile(self) -> list[Point]:
        if self.angle == "2pi/3":
            return [(0, 0), (self.a, 0), (-self.b, self.b)]
        if self.angle == "pi/3":
            return [(0, 0), (self.a, 0), (0, self.b)]
        raise ValueError("angle must be pi/3 or 2pi/3")

    @property
    def outer(self) -> list[Point]:
        side = self.outer_side
        return [(0, 0), (side, 0), (0, side)]


def orient(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def normalize(poly: list[Point]) -> list[Point]:
    area2 = sum(orient((0, 0), poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly)))
    return poly if area2 > 0 else list(reversed(poly))


def unit_cells(poly: list[Point]) -> frozenset[Cell]:
    poly = normalize(poly)
    scaled = [(3 * x, 3 * y) for x, y in poly]
    min_x = min(x for x, _ in poly) - 1
    max_x = max(x for x, _ in poly) + 1
    min_y = min(y for _, y in poly) - 1
    max_y = max(y for _, y in poly) + 1
    cells: set[Cell] = set()
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            for orientation, centroid3 in (
                (0, (3 * i + 1, 3 * j + 1)),
                (1, (3 * i + 2, 3 * j + 2)),
            ):
                if all(
                    orient(scaled[k], scaled[(k + 1) % len(poly)], centroid3) >= 0
                    for k in range(len(poly))
                ):
                    cells.add((i, j, orientation))
    return frozenset(cells)


def matmul(matrix: Matrix, point: Point) -> Point:
    return (
        matrix[0][0] * point[0] + matrix[0][1] * point[1],
        matrix[1][0] * point[0] + matrix[1][1] * point[1],
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def dihedral_matrices() -> list[Matrix]:
    rotate60 = ((0, -1), (1, 1))
    reflect = ((0, 1), (1, 0))
    identity = ((1, 0), (0, 1))
    rotations: list[Matrix] = []
    matrix = identity
    for _ in range(6):
        rotations.append(matrix)
        matrix = matrix_multiply(rotate60, matrix)
    out: list[Matrix] = []
    for matrix in rotations:
        out.append(matrix)
        out.append(matrix_multiply(reflect, matrix))
    unique: list[Matrix] = []
    for matrix in out:
        if matrix not in unique:
            unique.append(matrix)
    return unique


def placements(instance: Instance, outer_cells: frozenset[Cell]) -> list[tuple[list[Point], frozenset[Cell]]]:
    out: list[tuple[list[Point], frozenset[Cell]]] = []
    seen: set[tuple[Cell, ...]] = set()
    side = instance.outer_side
    expected_cells = instance.a * instance.b
    for matrix in dihedral_matrices():
        base = [matmul(matrix, point) for point in instance.tile]
        min_base_x = min(x for x, _ in base)
        max_base_x = max(x for x, _ in base)
        min_base_y = min(y for _, y in base)
        max_base_y = max(y for _, y in base)
        for dx in range(-max_base_x - 1, side - min_base_x + 2):
            for dy in range(-max_base_y - 1, side - min_base_y + 2):
                poly = [(x + dx, y + dy) for x, y in base]
                cells = unit_cells(poly)
                if len(cells) != expected_cells or not cells <= outer_cells:
                    continue
                key = tuple(sorted(cells))
                if key in seen:
                    continue
                seen.add(key)
                out.append((poly, cells))
    return out


def orientation_difference(cells: frozenset[Cell]) -> int:
    return sum(1 if orientation == 0 else -1 for _i, _j, orientation in cells)


def tile_orientation_differences(instance: Instance) -> list[int]:
    out: list[int] = []
    for matrix in dihedral_matrices():
        cells = unit_cells([matmul(matrix, point) for point in instance.tile])
        diff = orientation_difference(cells)
        if diff not in out:
            out.append(diff)
    return sorted(out)


def coloring_can_match(n: int, target: int, options: list[int]) -> bool:
    reachable = {0}
    for _ in range(n):
        reachable = {value + option for value in reachable for option in options}
    return target in reachable


def exact_cover(
    outer_cells: frozenset[Cell],
    rows: list[tuple[list[Point], frozenset[Cell]]],
    max_nodes: int,
) -> tuple[list[int] | None, int, bool]:
    cell_to_rows: dict[Cell, list[int]] = defaultdict(list)
    for index, (_poly, cells) in enumerate(rows):
        for cell in cells:
            cell_to_rows[cell].append(index)

    used: list[int] = []
    nodes = 0

    def search(remaining: frozenset[Cell]) -> bool:
        nonlocal nodes
        nodes += 1
        if nodes > max_nodes:
            return False
        if not remaining:
            return True
        cell = min(
            remaining,
            key=lambda item: sum(1 for row_index in cell_to_rows[item] if rows[row_index][1] <= remaining),
        )
        options = [row_index for row_index in cell_to_rows[cell] if rows[row_index][1] <= remaining]
        for row_index in options:
            used.append(row_index)
            if search(frozenset(remaining - rows[row_index][1])):
                return True
            used.pop()
            if nodes > max_nodes:
                return False
        return False

    solved = search(outer_cells)
    exhausted = nodes <= max_nodes
    return (used[:] if solved else None), nodes, exhausted


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("angle", choices=("pi/3", "2pi/3"))
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("--max-nodes", type=int, default=2_000_000)
    args = parser.parse_args()

    instance = Instance(args.n, args.angle, args.a, args.b)
    outer_cells = unit_cells(instance.outer)
    outer_diff = orientation_difference(outer_cells)
    tile_diffs = tile_orientation_differences(instance)
    rows = placements(instance, outer_cells)
    solution, nodes, exhausted = exact_cover(outer_cells, rows, args.max_nodes)

    print(
        f"N={instance.n} equilateral {instance.angle} tile "
        f"{(instance.a, instance.b, instance.c)} lattice exact-cover check"
    )
    print(f"outer side={instance.outer_side}")
    print(f"outer unit cells={len(outer_cells)}")
    print(f"tile unit cells={instance.a * instance.b}")
    print(f"outer up-minus-down={outer_diff}")
    print(f"tile orientation differences={tile_diffs}")
    print(f"candidate placements={len(rows)}")
    print(f"search nodes={nodes}")
    if not coloring_can_match(instance.n, outer_diff, tile_diffs):
        print("lattice orientation-coloring obstruction applies")
    if solution is None:
        if exhausted:
            print("no lattice-aligned exact cover found")
        else:
            print("search stopped at max node limit without finding a cover")
        print("limitation: arbitrary non-lattice tilings are not excluded")
        return
    print(f"solution uses {len(solution)} placements:")
    for row_index in solution:
        print(f"  {rows[row_index][0]}")


if __name__ == "__main__":
    main()
