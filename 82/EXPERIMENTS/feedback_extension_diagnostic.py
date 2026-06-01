#!/usr/bin/env python3
"""Diagnose one-vertex extensions of regular-feedback partitions."""

from __future__ import annotations

import argparse
from collections import Counter

import column_drop_census as cdc
from regular_feedback_partition import feedback_partition, subset_vertices
from regular_spectrum_mass import spectrum_mass
from spectrum_mass_critical import extend_mask


def induced_adjacency(adj: list[int], vertices: list[int]) -> list[int]:
    out = [0] * len(vertices)
    for i, u in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            v = vertices[j]
            if (adj[u] >> v) & 1:
                out[i] |= 1 << j
                out[j] |= 1 << i
    return out


def criterion_status(
    ext_by_degree: dict[int, int],
    forest_size: int,
    core_sizes: dict[int, int],
    used_degrees: set[int],
) -> tuple[bool, tuple[int, int, bool, bool]]:
    low_increment = (
        ext_by_degree.get(0, 0)
        + ext_by_degree.get(1, 0)
        - forest_size
    )
    degree2_increment = ext_by_degree.get(2, 0) - core_sizes.get(2, 0)
    old_core_increment = any(
        ext_by_degree.get(degree, 0) >= size + 1
        for degree, size in core_sizes.items()
        if degree >= 3
    )
    new_degree = any(
        degree not in used_degrees and size > 0
        for degree, size in ext_by_degree.items()
    )
    passes = (
        low_increment >= 1
        or degree2_increment >= 1
        or old_core_increment
        or new_degree
    )
    return passes, (
        low_increment,
        degree2_increment,
        old_core_increment,
        new_degree,
    )


def diagnose(n: int, mask: int, min_degree: int, max_columns: int | None) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    partition = feedback_partition(adj, min_degree)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"spectrum_mass={mass}")
    print(f"by_degree={by_degree}")
    print(f"feedback_partition_exists={partition is not None}")
    if partition is None:
        return

    forest, core_parts = partition
    print(f"forest vertices={subset_vertices(forest, n)}")
    for degree, subset in core_parts:
        print(f"core degree={degree} size={subset.bit_count()} vertices={subset_vertices(subset, n)}")

    used_degrees = {0, 1}
    core_sizes: dict[int, int] = {}
    for degree, subset in core_parts:
        used_degrees.add(degree)
        core_sizes[degree] = subset.bit_count()

    pc_plus = cdc.precompute(n + 1)
    forest_vertices = [v for v in range(n) if (forest >> v) & 1]
    histogram: Counter[tuple[int, int, int, bool, bool]] = Counter()
    failing_columns: list[tuple[int, dict[int, int], dict[int, int]]] = []
    tight_columns: list[tuple[int, dict[int, int], dict[int, int]]] = []
    column_limit = 1 << n if max_columns is None else min(max_columns, 1 << n)

    for column in range(column_limit):
        extended = extend_mask(mask, n, column, pc, pc_plus)
        ext_adj = cdc.adjacency(n + 1, extended, pc_plus)
        ext_mass, ext_by_degree = spectrum_mass(ext_adj, pc_plus)

        a_vertices = [*forest_vertices, n]
        a_adj = induced_adjacency(ext_adj, a_vertices)
        pc_a = cdc.precompute(len(a_vertices))
        _, a_by_degree = spectrum_mass(a_adj, pc_a)
        apex_low_increment = (
            a_by_degree.get(0, 0)
            + a_by_degree.get(1, 0)
            - len(forest_vertices)
        )
        criterion_passes, criterion_tuple = criterion_status(
            ext_by_degree, len(forest_vertices), core_sizes, used_degrees
        )
        low_increment, degree2_increment, old_core_increment, new_degree = criterion_tuple
        surplus = ext_mass - (n + 1)
        key = (
            surplus,
            low_increment,
            degree2_increment,
            old_core_increment,
            new_degree,
        )
        histogram[key] += 1
        if not criterion_passes and len(failing_columns) < 10:
            failing_columns.append((column, ext_by_degree, a_by_degree))
        if surplus == 0 and len(tight_columns) < 10:
            tight_columns.append((column, ext_by_degree, a_by_degree))

    print(f"columns_checked={column_limit}")
    print("histogram=(surplus, full_low_increment, degree2_increment, old_core_increment, new_degree) -> count")
    for key, count in histogram.most_common():
        print(f"{key}: {count}")
    print(f"criterion_failures={len(failing_columns)}")
    for column, ext_by_degree, a_by_degree in failing_columns:
        print(f"failure column={column} ext_by_degree={ext_by_degree} apex_by_degree={a_by_degree}")
    for column, ext_by_degree, a_by_degree in tight_columns:
        print(f"tight column={column} ext_by_degree={ext_by_degree} apex_by_degree={a_by_degree}")


def scan(
    n: int,
    min_degree: int,
    equality_only: bool,
    max_graphs: int | None,
    max_columns: int | None,
) -> None:
    pc = cdc.precompute(n)
    pc_plus = cdc.precompute(n + 1)
    total = 1 << len(pc.edges)
    graphs_with_partition = 0
    graphs_with_degree2 = 0
    extensions_checked = 0
    failures: list[tuple[int, int, dict[int, int], dict[int, int]]] = []

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        mass, by_degree = spectrum_mass(adj, pc)
        if equality_only and mass != n:
            continue
        partition = feedback_partition(adj, min_degree)
        if partition is None:
            continue
        graphs_with_partition += 1
        forest, core_parts = partition
        if not any(degree == 2 for degree, _ in core_parts):
            continue
        graphs_with_degree2 += 1
        forest_size = forest.bit_count()
        used_degrees = {0, 1}
        core_sizes: dict[int, int] = {}
        for degree, subset in core_parts:
            used_degrees.add(degree)
            core_sizes[degree] = subset.bit_count()

        column_limit = 1 << n if max_columns is None else min(max_columns, 1 << n)
        for column in range(column_limit):
            extended = extend_mask(mask, n, column, pc, pc_plus)
            ext_adj = cdc.adjacency(n + 1, extended, pc_plus)
            _, ext_by_degree = spectrum_mass(ext_adj, pc_plus)
            passes, _ = criterion_status(
                ext_by_degree, forest_size, core_sizes, used_degrees
            )
            extensions_checked += 1
            if not passes:
                failures.append((mask, column, by_degree, ext_by_degree))
                break
        if failures:
            break
        if max_graphs is not None and graphs_with_degree2 >= max_graphs:
            break

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"min_degree={min_degree}")
    print(f"equality_only={equality_only}")
    print(f"graphs_with_feedback_partition={graphs_with_partition}")
    print(f"graphs_with_degree2_core={graphs_with_degree2}")
    print(f"extensions_checked={extensions_checked}")
    print(f"criterion_failure_found={bool(failures)}")
    for mask, column, by_degree, ext_by_degree in failures[:10]:
        print(
            f"failure mask={mask} column={column} "
            f"by_degree={by_degree} ext_by_degree={ext_by_degree}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--min-degree", type=int, default=2)
    parser.add_argument("--max-columns", type=int)
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--equality-only", action="store_true")
    parser.add_argument("--max-graphs", type=int)
    args = parser.parse_args()
    if args.scan:
        scan(
            args.n,
            args.min_degree,
            args.equality_only,
            args.max_graphs,
            args.max_columns,
        )
    else:
        if args.mask is None:
            parser.error("--mask is required unless --scan is supplied")
        diagnose(args.n, args.mask, args.min_degree, args.max_columns)


if __name__ == "__main__":
    main()
