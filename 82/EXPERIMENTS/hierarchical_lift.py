#!/usr/bin/env python3
"""Test hierarchical first-lift partitions.

For an even graph, first choose a parity-pattern bipartition x satisfying
A*x = a*1 + b*x over F_2.  Then try to split each side into two induced
target-modular parts.  Success gives a structured four-part modular
partition.
"""

from __future__ import annotations

import argparse

import modular_partition
import parity_split


def induced_with_vertices(graph_mask: int, n: int, subset: int) -> tuple[list[int], int]:
    vertices = [v for v in range(n) if (subset >> v) & 1]
    edge_to_bit = {
        edge: idx
        for idx, edge in enumerate((i, j) for i in range(n) for j in range(i + 1, n))
    }
    new_mask = 0
    bit = 0
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            old_edge = (vertices[i], vertices[j])
            if (graph_mask >> edge_to_bit[old_edge]) & 1:
                new_mask |= 1 << bit
            bit += 1
    return vertices, new_mask


def lift_assignment(
    n: int,
    side0_vertices: list[int],
    side0_assignment: list[int],
    side1_vertices: list[int],
    side1_assignment: list[int],
) -> list[int]:
    assignment = [-1] * n
    for local, vertex in enumerate(side0_vertices):
        assignment[vertex] = side0_assignment[local]
    for local, vertex in enumerate(side1_vertices):
        assignment[vertex] = 2 + side1_assignment[local]
    return assignment


def try_hierarchical(
    n: int,
    graph_mask: int,
    target_modulus: int,
    node_limit: int | None,
    max_split_solutions: int,
) -> tuple[list[int] | None, str]:
    rows = parity_split.adjacency_rows(n, graph_mask)
    full = (1 << n) - 1
    seen: set[int] = set()
    checked = 0
    for a in (0, 1):
        for b in (0, 1):
            system_rows = [row ^ ((1 << i) if b else 0) for i, row in enumerate(rows)]
            solution, basis = parity_split.solve_affine(system_rows, [a] * n, n)
            if solution is None:
                continue
            limit = 1 << min(len(basis), 20)
            for mask in range(limit):
                split = parity_split.sample_solution(solution, basis, mask)
                if split in (0, full) or split in seen or (full ^ split) in seen:
                    continue
                seen.add(split)
                checked += 1
                if checked > max_split_solutions:
                    return None, f"split_limit checked={checked-1}"

                side0 = full ^ split
                side1 = split
                side0_vertices, side0_mask = induced_with_vertices(graph_mask, n, side0)
                side1_vertices, side1_mask = induced_with_vertices(graph_mask, n, side1)
                try:
                    side0_assignment = modular_partition.find_partition(
                        len(side0_vertices),
                        side0_mask,
                        target_modulus,
                        2,
                        node_limit=node_limit,
                    )
                    side1_assignment = modular_partition.find_partition(
                        len(side1_vertices),
                        side1_mask,
                        target_modulus,
                        2,
                        node_limit=node_limit,
                    )
                except modular_partition.SearchLimitExceeded:
                    continue
                if side0_assignment is not None and side1_assignment is not None:
                    return (
                        lift_assignment(
                            n,
                            side0_vertices,
                            side0_assignment,
                            side1_vertices,
                            side1_assignment,
                        ),
                        f"a={a} b={b} split={split} checked={checked}",
                    )
    return None, f"checked={checked}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("mask", type=int)
    parser.add_argument("--target-modulus", type=int, default=4)
    parser.add_argument("--node-limit", type=int)
    parser.add_argument("--max-split-solutions", type=int, default=100000)
    args = parser.parse_args()
    assignment, note = try_hierarchical(
        args.n,
        args.mask,
        args.target_modulus,
        args.node_limit,
        args.max_split_solutions,
    )
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"target_modulus={args.target_modulus}")
    if args.node_limit is not None:
        print(f"node_limit={args.node_limit}")
    print(f"note={note}")
    print(f"hierarchical_partition_exists={assignment is not None}")
    if assignment is not None:
        print("assignment=" + ",".join(map(str, assignment)))
        stats = modular_partition.assignment_stats(
            args.n, args.mask, assignment, args.target_modulus
        )
        print(
            "parts="
            + " ".join(
                f"color{color}:size{size}:residue{residue}"
                for color, size, residue in stats
            )
        )


if __name__ == "__main__":
    main()
