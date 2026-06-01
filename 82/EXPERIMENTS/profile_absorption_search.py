#!/usr/bin/env python3
"""Search regular witnesses across a fixed cut using profile absorption."""

from __future__ import annotations

import argparse
from itertools import combinations

import regular_induced as ri


def edge_index(pc: ri.Precomp) -> dict[tuple[int, int], int]:
    return {edge: index for index, edge in enumerate(pc.edges)}


def has_edge(mask: int, u: int, v: int, index: dict[tuple[int, int], int]) -> bool:
    if u > v:
        u, v = v, u
    return bool(mask & (1 << index[(u, v)]))


def vertices_from_mask(mask: int, n: int) -> list[int]:
    return [v for v in range(n) if (mask >> v) & 1]


def degree_to_vertices(
    mask: int,
    vertex: int,
    targets: list[int],
    index: dict[tuple[int, int], int],
) -> int:
    return sum(has_edge(mask, vertex, w, index) for w in targets if w != vertex)


def all_subsets(vertices: list[int]) -> list[int]:
    out = [0]
    for v in vertices:
        out += [subset | (1 << v) for subset in out]
    return out


def profile_regular(
    graph_mask: int,
    x_mask: int,
    y_mask: int,
    n: int,
    index: dict[tuple[int, int], int],
) -> tuple[bool, int | None, list[str], list[str]]:
    x_vertices = vertices_from_mask(x_mask, n)
    y_vertices = vertices_from_mask(y_mask, n)
    if not x_vertices and not y_vertices:
        return False, None, [], []

    degrees: list[int] = []
    x_profile: list[str] = []
    y_profile: list[str] = []
    for v in x_vertices:
        internal = degree_to_vertices(graph_mask, v, x_vertices, index)
        cross = degree_to_vertices(graph_mask, v, y_vertices, index)
        degrees.append(internal + cross)
        x_profile.append(f"{v}:{internal}+{cross}={internal + cross}")
    for v in y_vertices:
        internal = degree_to_vertices(graph_mask, v, y_vertices, index)
        cross = degree_to_vertices(graph_mask, v, x_vertices, index)
        degrees.append(internal + cross)
        y_profile.append(f"{v}:{internal}+{cross}={internal + cross}")

    regular = all(value == degrees[0] for value in degrees)
    return regular, degrees[0] if regular else None, x_profile, y_profile


def search(graph_mask: int, n: int, split: int, min_each_side: int) -> None:
    pc = ri.precompute(n)
    index = edge_index(pc)
    left = list(range(split))
    right = list(range(split, n))
    left_subsets = all_subsets(left)
    right_subsets = all_subsets(right)
    left_subsets.sort(key=lambda subset: subset.bit_count(), reverse=True)
    right_subsets.sort(key=lambda subset: subset.bit_count(), reverse=True)

    best: tuple[int, int, int, int | None, list[str], list[str]] = (0, 0, 0, None, [], [])
    for x_mask in left_subsets:
        x_size = x_mask.bit_count()
        if x_size < min_each_side:
            continue
        if x_size + len(right) < best[0]:
            break
        for y_mask in right_subsets:
            y_size = y_mask.bit_count()
            if y_size < min_each_side:
                continue
            size = x_size + y_size
            if size < best[0]:
                break
            regular, degree, x_profile, y_profile = profile_regular(
                graph_mask, x_mask, y_mask, n, index
            )
            if regular and size > best[0]:
                best = (size, x_mask, y_mask, degree, x_profile, y_profile)

    size, x_mask, y_mask, degree, x_profile, y_profile = best
    union_mask = x_mask | y_mask
    print(f"n={n}")
    print(f"mask={graph_mask}")
    print(f"split={split}")
    print(f"min_each_side={min_each_side}")
    print(f"best_split_regular_order={size}")
    print(f"best_split_regular_degree={degree}")
    print("left_vertices=" + ",".join(map(str, vertices_from_mask(x_mask, n))))
    print("right_vertices=" + ",".join(map(str, vertices_from_mask(y_mask, n))))
    print("left_profile=" + ",".join(x_profile))
    print("right_profile=" + ",".join(y_profile))
    print(f"verified_regular={ri.is_regular_on(graph_mask, union_mask, pc) if size else False}")
    print(f"global_max_regular_order={ri.max_regular_order(graph_mask, pc)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--split", type=int, required=True)
    parser.add_argument("--min-each-side", type=int, default=0)
    args = parser.parse_args()
    search(args.mask, args.n, args.split, args.min_each_side)


if __name__ == "__main__":
    main()
