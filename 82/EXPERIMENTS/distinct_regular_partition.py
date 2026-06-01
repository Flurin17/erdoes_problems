#!/usr/bin/env python3
"""Search for vertex partitions into regular parts of distinct degrees."""

from __future__ import annotations

import argparse
from functools import lru_cache

import column_drop_census as cdc
from regular_feedback_partition import regular_degree, subset_vertices
from regular_spectrum_mass import spectrum_mass


def distinct_regular_partition(
    adj: list[int], min_degree: int
) -> tuple[tuple[int, int], ...] | None:
    n = len(adj)
    full = (1 << n) - 1
    candidates: list[tuple[int, int, int]] = []
    for subset in range(1, 1 << n):
        degree = regular_degree(adj, subset, min_degree)
        if degree is not None:
            candidates.append((subset, degree, subset.bit_count()))
    candidates.sort(key=lambda item: -item[2])

    @lru_cache(maxsize=None)
    def search(remainder: int, used_degrees: tuple[int, ...]) -> tuple[tuple[int, int], ...] | None:
        if remainder == 0:
            return ()
        pivot = remainder & -remainder
        used = set(used_degrees)
        for subset, degree, _size in candidates:
            if degree in used:
                continue
            if (subset & remainder) != subset or not (subset & pivot):
                continue
            suffix = search(remainder ^ subset, tuple(sorted((*used_degrees, degree))))
            if suffix is not None:
                return ((degree, subset), *suffix)
        return None

    return search(full, ())


def fixed(n: int, mask: int, min_degree: int) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    partition = distinct_regular_partition(adj, min_degree)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"min_degree={min_degree}")
    print(f"spectrum_mass={mass}")
    print(f"by_degree={by_degree}")
    print(f"distinct_regular_partition_exists={partition is not None}")
    if partition is not None:
        for degree, subset in partition:
            print(f"part degree={degree} vertices={subset_vertices(subset, n)}")


def exact(n: int, equality_only: bool, min_degree: int, max_examples: int) -> None:
    pc = cdc.precompute(n)
    total = 1 << len(pc.edges)
    checked = 0
    passed = 0
    bad_examples: list[tuple[int, int, dict[int, int]]] = []
    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        mass, by_degree = spectrum_mass(adj, pc)
        if equality_only and mass != n:
            continue
        checked += 1
        if distinct_regular_partition(adj, min_degree) is not None:
            passed += 1
        elif len(bad_examples) < max_examples:
            bad_examples.append((mask, mass, by_degree))

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"equality_only={equality_only}")
    print(f"min_degree={min_degree}")
    print(f"checked={checked}")
    print(f"distinct_regular_partition_count={passed}")
    print(f"all_checked_have_distinct_regular_partition={passed == checked}")
    for mask, mass, by_degree in bad_examples:
        print(f"bad mask={mask} mass={mass} by_degree={by_degree}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--equality-only", action="store_true")
    parser.add_argument("--min-degree", type=int, default=0)
    parser.add_argument("--max-examples", type=int, default=10)
    args = parser.parse_args()

    if args.mask is None:
        exact(args.n, args.equality_only, args.min_degree, args.max_examples)
    else:
        fixed(args.n, args.mask, args.min_degree)


if __name__ == "__main__":
    main()
