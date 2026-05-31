#!/usr/bin/env python3
"""Triangular-lattice coloring obstruction for the prime-71 candidate.

The candidate with tile sides (39,16,49) and outer sides (196,196,284) has a
natural triangular-lattice model.  In axial coordinates the outer triangle has
vertices

    (0,0), (284,0), (64,156),

and one tile orientation has vertices

    (0,0), (39,0), (-16,16).

Color unit lattice triangles by orientation (up/down).  The outer triangle has
up-minus-down count 92, while every lattice-oriented copy of the tile has
up-minus-down count +/-8.  Since 92 is not divisible by 8, no tiling whose tile
vertices all lie in this lattice exists.

Limitation: this includes strict edge-to-edge tilings, but it is not a full
non-strict/T-junction obstruction; a T-junction on a primitive c-edge can
introduce a shifted lattice coset.
"""

from __future__ import annotations


OUTER = [(0, 0), (284, 0), (64, 156)]
TILE = [(0, 0), (39, 0), (-16, 16)]


def orient(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def normalize(poly: list[tuple[int, int]]) -> list[tuple[int, int]]:
    area2 = sum(orient((0, 0), poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly)))
    return poly if area2 > 0 else list(reversed(poly))


def unit_cells(poly: list[tuple[int, int]]) -> list[tuple[int, int, int]]:
    """Return unit triangular cells as (i,j,orientation), orientation 0=up, 1=down."""
    poly = normalize(poly)
    scaled = [(3 * x, 3 * y) for x, y in poly]
    min_x = min(x for x, _ in poly) - 1
    max_x = max(x for x, _ in poly) + 1
    min_y = min(y for _, y in poly) - 1
    max_y = max(y for _, y in poly) + 1
    cells: list[tuple[int, int, int]] = []
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            for orientation, centroid3 in ((0, (3 * i + 1, 3 * j + 1)), (1, (3 * i + 2, 3 * j + 2))):
                if all(orient(scaled[k], scaled[(k + 1) % len(scaled)], centroid3) >= 0 for k in range(len(poly))):
                    cells.append((i, j, orientation))
    return cells


def up_down_difference(poly: list[tuple[int, int]]) -> tuple[int, int, int]:
    cells = unit_cells(poly)
    up = sum(1 for _, _, orientation in cells if orientation == 0)
    down = len(cells) - up
    return up, down, up - down


def matmul(matrix: tuple[tuple[int, int], tuple[int, int]], point: tuple[int, int]) -> tuple[int, int]:
    return (
        matrix[0][0] * point[0] + matrix[0][1] * point[1],
        matrix[1][0] * point[0] + matrix[1][1] * point[1],
    )


def matrix_multiply(
    left: tuple[tuple[int, int], tuple[int, int]],
    right: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
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


def dihedral_matrices() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    rotate60 = ((0, -1), (1, 1))
    reflect = ((0, 1), (1, 0))
    identity = ((1, 0), (0, 1))
    rotations = []
    matrix = identity
    for _ in range(6):
        rotations.append(matrix)
        matrix = matrix_multiply(rotate60, matrix)
    out = []
    for matrix in rotations:
        out.append(matrix)
        out.append(matrix_multiply(reflect, matrix))
    unique = []
    for matrix in out:
        if matrix not in unique:
            unique.append(matrix)
    return unique


def main() -> None:
    outer_up, outer_down, outer_diff = up_down_difference(OUTER)
    print("prime-71 triangular-lattice orientation coloring")
    print(f"outer up={outer_up}, down={outer_down}, difference={outer_diff}")
    tile_diffs = set()
    for matrix in dihedral_matrices():
        poly = [matmul(matrix, point) for point in TILE]
        up, down, diff = up_down_difference(poly)
        assert up + down == 624
        tile_diffs.add(diff)
    print(f"tile orientation differences={sorted(tile_diffs)}")
    print(f"outer difference mod 8 = {outer_diff % 8}")
    assert tile_diffs == {-8, 8}
    assert outer_diff % 8 != 0
    print("lattice-vertex tilings are impossible by orientation-coloring")
    print("limitation: arbitrary non-strict T-junction tilings may use shifted lattice cosets")


if __name__ == "__main__":
    main()
