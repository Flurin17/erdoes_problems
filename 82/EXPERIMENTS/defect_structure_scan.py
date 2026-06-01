#!/usr/bin/env python3
"""Structural diagnostics for connected spectrum-mass defect graphs."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations

import column_drop_census as cdc
from regular_spectrum_mass import (
    connected_after_deleting,
    is_connected,
    spectrum_mass,
)
from spectrum_partition import maximum_regular_sets
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


def essential_vertices_by_degree(
    adj: list[int], pc: cdc.Precomp, by_degree: dict[int, int]
) -> dict[int, tuple[int, ...]]:
    out: dict[int, tuple[int, ...]] = {}
    for degree, order in by_degree.items():
        sets = maximum_regular_sets(adj, pc, degree, order)
        if not sets:
            out[degree] = ()
            continue
        intersection = sets[0]
        for subset in sets[1:]:
            intersection &= subset
        out[degree] = tuple(v for v in range(pc.n) if (intersection >> v) & 1)
    return out


def essential_vertex_union(
    adj: list[int], pc: cdc.Precomp, by_degree: dict[int, int]
) -> tuple[int, ...]:
    essential = essential_vertices_by_degree(adj, pc, by_degree)
    return tuple(sorted({v for vertices in essential.values() for v in vertices}))


def fixed(n: int, mask: int) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    essential = essential_vertices_by_degree(adj, pc, by_degree)
    essential_union = tuple(sorted({v for vertices in essential.values() for v in vertices}))
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
    print(f"essential_vertices_by_degree={essential}")
    print(f"essential_vertex_union={essential_union}")
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


def exact(n: int, max_examples: int, essential_scan: bool) -> None:
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
    no_noncut_nonessential_count = 0
    below_full_no_noncut_nonessential_count = 0
    no_noncut_nonessential_mass_hist: Counter[int] = Counter()
    no_noncut_nonessential_examples = []
    all_noncut_nonessential_count = 0
    below_defect_one_all_noncut_nonessential_count = 0
    all_noncut_nonessential_mass_hist: Counter[int] = Counter()
    all_noncut_nonessential_examples = []

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        if not is_connected(adj):
            continue
        connected_count += 1
        mass, by_degree = spectrum_mass(adj, pc)
        cuts = set(cut_vertices(adj))

        if essential_scan:
            essential_union = set(essential_vertex_union(adj, pc, by_degree))
            noncut_vertices = set(range(n)) - cuts
            has_noncut_nonessential = bool(noncut_vertices - essential_union)
            all_noncut_nonessential = not bool(noncut_vertices & essential_union)
            if not has_noncut_nonessential:
                no_noncut_nonessential_count += 1
                no_noncut_nonessential_mass_hist[mass] += 1
                if len(no_noncut_nonessential_examples) < max_examples:
                    no_noncut_nonessential_examples.append(
                        (mask, mass, by_degree, tuple(sorted(cuts)), tuple(sorted(essential_union)))
                    )
                if mass < n:
                    below_full_no_noncut_nonessential_count += 1
            if all_noncut_nonessential:
                all_noncut_nonessential_count += 1
                all_noncut_nonessential_mass_hist[mass] += 1
                if len(all_noncut_nonessential_examples) < max_examples:
                    all_noncut_nonessential_examples.append(
                        (mask, mass, by_degree, tuple(sorted(cuts)), tuple(sorted(essential_union)))
                    )
                if mass < n - 1:
                    below_defect_one_all_noncut_nonessential_count += 1

        if mass >= n:
            continue
        below_full_count += 1
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
    print(f"essential_scan={essential_scan}")
    if essential_scan:
        print(f"no_noncut_nonessential_count={no_noncut_nonessential_count}")
        print(
            "below_full_no_noncut_nonessential_count="
            f"{below_full_no_noncut_nonessential_count}"
        )
        print(
            "no_noncut_nonessential_mass_histogram="
            f"{dict(sorted(no_noncut_nonessential_mass_hist.items()))}"
        )
        print(f"all_noncut_nonessential_count={all_noncut_nonessential_count}")
        print(
            "below_defect_one_all_noncut_nonessential_count="
            f"{below_defect_one_all_noncut_nonessential_count}"
        )
        print(
            "all_noncut_nonessential_mass_histogram="
            f"{dict(sorted(all_noncut_nonessential_mass_hist.items()))}"
        )
        for mask, mass, by_degree, cuts, essential_union in no_noncut_nonessential_examples:
            print(
                f"no_noncut_nonessential_example mask={mask} mass={mass} "
                f"by_degree={by_degree} cuts={cuts} essential_union={essential_union}"
            )
        for mask, mass, by_degree, cuts, essential_union in all_noncut_nonessential_examples:
            print(
                f"all_noncut_nonessential_example mask={mask} mass={mass} "
                f"by_degree={by_degree} cuts={cuts} essential_union={essential_union}"
            )
    for mask, mass, by_degree in below_full_examples:
        print(f"below_full_example mask={mask} mass={mass} by_degree={by_degree}")
    for mask, by_degree in examples:
        print(f"defect_one_example mask={mask} by_degree={by_degree}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--max-examples", type=int, default=10)
    parser.add_argument("--essential-scan", action="store_true")
    args = parser.parse_args()

    if args.mask is None:
        exact(args.n, args.max_examples, args.essential_scan)
    else:
        fixed(args.n, args.mask)


if __name__ == "__main__":
    main()
