#!/usr/bin/env python3
"""Exact-cover check for the tempting N=15 Zhang tile candidate.

The primitive 2pi/3 tile `(a,b,c)=(3,5,7)` has area exactly 1/15 of an
equilateral triangle of side 15.  Zhang's theorem proves the family
`15m^2` only for `m >= 9`; this script tests the smallest area-compatible
lattice case `m=1`.

Coordinates use the triangular lattice axial model with squared length
`x^2 + xy + y^2`.  The outer triangle is

    (0,0), (15,0), (0,15),

and one tile orientation is

    (0,0), (3,0), (-5,5).

The script enumerates every dihedral image and translation of the tile whose
unit-triangle cells lie inside the outer triangle, then runs exact cover.
Failure is only a lattice-aligned obstruction, not a proof against arbitrary
non-lattice tilings.
"""

from __future__ import annotations

from collections import defaultdict


Point = tuple[int, int]
Cell = tuple[int, int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]

OUTER = [(0, 0), (15, 0), (0, 15)]
TILE = [(0, 0), (3, 0), (-5, 5)]


def orient(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def normalize(poly: list[Point]) -> list[Point]:
    area2 = sum(orient((0, 0), poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly)))
    return poly if area2 > 0 else list(reversed(poly))


def unit_cells(poly: list[Point]) -> frozenset[Cell]:
    """Return unit triangular cells as `(i,j,orientation)`, orientation 0/1."""
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


def placements(outer_cells: frozenset[Cell]) -> list[tuple[list[Point], frozenset[Cell]]]:
    out: list[tuple[list[Point], frozenset[Cell]]] = []
    seen: set[tuple[Cell, ...]] = set()
    for matrix in dihedral_matrices():
        base = [matmul(matrix, point) for point in TILE]
        for dx in range(-10, 26):
            for dy in range(-10, 26):
                poly = [(x + dx, y + dy) for x, y in base]
                cells = unit_cells(poly)
                if len(cells) != 15 or not cells <= outer_cells:
                    continue
                key = tuple(sorted(cells))
                if key in seen:
                    continue
                seen.add(key)
                out.append((poly, cells))
    return out


def exact_cover(
    outer_cells: frozenset[Cell], rows: list[tuple[list[Point], frozenset[Cell]]]
) -> list[int] | None:
    cell_to_rows: dict[Cell, list[int]] = defaultdict(list)
    for index, (_poly, cells) in enumerate(rows):
        for cell in cells:
            cell_to_rows[cell].append(index)

    used: list[int] = []

    def search(remaining: frozenset[Cell]) -> bool:
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
        return False

    return used[:] if search(outer_cells) else None


def main() -> None:
    outer_cells = unit_cells(OUTER)
    rows = placements(outer_cells)
    solution = exact_cover(outer_cells, rows)
    print("N=15 equilateral (3,5,7) lattice exact-cover check")
    print(f"outer unit cells={len(outer_cells)}")
    print(f"candidate placements={len(rows)}")
    if solution is None:
        print("no lattice-aligned exact cover found")
        print("limitation: arbitrary non-lattice tilings are not excluded")
        return
    print(f"solution uses {len(solution)} placements:")
    for row_index in solution:
        print(f"  {rows[row_index][0]}")


if __name__ == "__main__":
    main()
