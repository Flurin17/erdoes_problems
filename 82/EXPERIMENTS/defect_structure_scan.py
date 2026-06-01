#!/usr/bin/env python3
"""Structural diagnostics for connected spectrum-mass defect graphs."""

from __future__ import annotations

import argparse
from itertools import combinations

import column_drop_census as cdc
from regular_spectrum_mass import (
    connected_after_deleting,
    is_connected,
    spectrum_mass,
)
from spectrum_mass_critical import delete_vertex


def degree_sequence(adj: list[int]) -> tuple[int, ...]:
    return tuple(sorted(row.bit_count() for row in adj))


def cut_vertices(adj: list[int]) -> list[int]:
    return [v for v in range(len(adj)) if not connected_after_deleting(adj, (v,))]


def first_vertex_cut(adj: list[int], size: int) -> tuple[int, ...] | None:
    for deleted in combinations(range(len(adj)), size):
        if not connected_after_deleting(adj, deleted):
            return deleted
    return None


def simplicial_degree_two_vertices(adj: list[int]) -> list[tuple[int, tuple[int, int]]]:
    out: list[tuple[int, tuple[int, int]]] = []
    n = len(adj)
    for v in range(n):
        if adj[v].bit_count() != 2:
            continue
        neighbors = tuple(u for u in range(n) if (adj[v] >> u) & 1)
        if (adj[neighbors[0]] >> neighbors[1]) & 1:
            out.append((v, neighbors))
    return out


def fixed(n: int, mask: int) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    pc_minus = cdc.precompute(n - 1) if n > 1 else None
    cuts = cut_vertices(adj) if is_connected(adj) else []
    full_mass_deletions: list[int] = []
    noncut_full_mass_deletions: list[int] = []
    deletion_rows: list[tuple[int, int, dict[int, int], bool]] = []

    if pc_minus is not None:
        for v in range(n):
            smaller = delete_vertex(adj, v)
            smaller_mass, smaller_by_degree = spectrum_mass(smaller, pc_minus)
            full = smaller_mass >= n - 1
            noncut = v not in cuts
            if full:
                full_mass_deletions.append(v)
            if full and noncut:
                noncut_full_mass_deletions.append(v)
            deletion_rows.append((v, smaller_mass, smaller_by_degree, noncut))

    print(f"n={n}")
    print(f"mask={mask}")
    print(f"connected={is_connected(adj)}")
    print(f"degree_sequence={degree_sequence(adj)}")
    print(f"spectrum_mass={mass}")
    print(f"defect={n - mass}")
    print(f"by_degree={by_degree}")
    print(f"cut_vertices={cuts}")
    print(f"first_2_cut={first_vertex_cut(adj, 2)}")
    print(f"simplicial_degree_two_vertices={simplicial_degree_two_vertices(adj)}")
    print(f"full_mass_deletions={full_mass_deletions}")
    print(f"noncut_full_mass_deletions={noncut_full_mass_deletions}")
    for v, smaller_mass, smaller_by_degree, noncut in deletion_rows:
        print(
            f"delete vertex={v} noncut={noncut} "
            f"mass={smaller_mass} by_degree={smaller_by_degree}"
        )


def exact(n: int, max_examples: int) -> None:
    pc = cdc.precompute(n)
    pc_minus = cdc.precompute(n - 1) if n > 1 else None
    total = 1 << len(pc.edges)
    connected_count = 0
    below_full_count = 0
    below_full_without_noncut_full = 0
    defect_one_count = 0
    without_noncut_full = 0
    below_full_examples = []
    examples = []

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        if not is_connected(adj):
            continue
        connected_count += 1
        mass, by_degree = spectrum_mass(adj, pc)
        if mass >= n:
            continue
        below_full_count += 1
        cuts = set(cut_vertices(adj))
        has_noncut_full = False
        assert pc_minus is not None
        for v in range(n):
            if v in cuts:
                continue
            smaller = delete_vertex(adj, v)
            smaller_mass, _ = spectrum_mass(smaller, pc_minus)
            if smaller_mass >= n - 1:
                has_noncut_full = True
                break
        if not has_noncut_full:
            below_full_without_noncut_full += 1
            if len(below_full_examples) < max_examples:
                below_full_examples.append((mask, mass, by_degree))

        if mass == n - 1:
            defect_one_count += 1
            if not has_noncut_full:
                without_noncut_full += 1
            if not has_noncut_full and len(examples) < max_examples:
                examples.append((mask, by_degree))

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"connected_count={connected_count}")
    print(f"below_full_count={below_full_count}")
    print(f"below_full_without_noncut_full_deletion={below_full_without_noncut_full}")
    print(f"defect_one_count={defect_one_count}")
    print(f"without_noncut_full_deletion={without_noncut_full}")
    for mask, mass, by_degree in below_full_examples:
        print(f"below_full_example mask={mask} mass={mass} by_degree={by_degree}")
    for mask, by_degree in examples:
        print(f"defect_one_example mask={mask} by_degree={by_degree}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--max-examples", type=int, default=10)
    args = parser.parse_args()

    if args.mask is None:
        exact(args.n, args.max_examples)
    else:
        fixed(args.n, args.mask)


if __name__ == "__main__":
    main()
