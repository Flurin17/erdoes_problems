#!/usr/bin/env python3
"""Search for forest plus distinct-regular-core partitions.

The target decomposition is a partition

    V(G)=F union R_1 union ... union R_t

where G[F] is a forest and every nonempty G[R_i] is induced d_i-regular with
distinct d_i at least a requested lower bound.  Such a partition proves the
spectrum-mass inequality when the regular degrees are at least 2, and it is
stable under one-vertex extension when they are at least 3.
"""

from __future__ import annotations

import argparse
from functools import lru_cache

import column_drop_census as cdc
from regular_spectrum_mass import spectrum_mass


def is_forest(adj: list[int], subset: int) -> bool:
    vertices = [v for v in range(len(adj)) if (subset >> v) & 1]
    edge_count = sum((adj[v] & subset).bit_count() for v in vertices) // 2
    seen = 0
    components = 0
    for start in vertices:
        if (seen >> start) & 1:
            continue
        components += 1
        seen |= 1 << start
        stack = [start]
        while stack:
            v = stack.pop()
            unseen = adj[v] & subset & ~seen
            while unseen:
                bit = unseen & -unseen
                unseen ^= bit
                seen |= bit
                stack.append(bit.bit_length() - 1)
    return edge_count == len(vertices) - components


def regular_degree(adj: list[int], subset: int, min_degree: int) -> int | None:
    if subset == 0:
        return None
    vertices = [v for v in range(len(adj)) if (subset >> v) & 1]
    degree = (adj[vertices[0]] & subset).bit_count()
    if degree < min_degree:
        return None
    if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
        return degree
    return None


def subset_vertices(subset: int, n: int) -> tuple[int, ...]:
    return tuple(v for v in range(n) if (subset >> v) & 1)


def feedback_partition(
    adj: list[int], min_degree: int
) -> tuple[int, list[tuple[int, int]]] | None:
    n = len(adj)
    full = (1 << n) - 1
    candidates: list[tuple[int, int, int]] = []
    for subset in range(1, 1 << n):
        degree = regular_degree(adj, subset, min_degree)
        if degree is not None:
            candidates.append((subset, degree, subset.bit_count()))
    candidates.sort(key=lambda item: -item[2])

    @lru_cache(maxsize=None)
    def search(
        remainder: int, used_degrees: tuple[int, ...]
    ) -> tuple[tuple[int, int], ...] | None:
        if is_forest(adj, remainder):
            return ()
        used = set(used_degrees)
        for subset, degree, _ in candidates:
            if degree in used or (subset & remainder) != subset:
                continue
            next_used = tuple(sorted((*used_degrees, degree)))
            suffix = search(remainder ^ subset, next_used)
            if suffix is not None:
                return ((degree, subset), *suffix)
        return None

    choice = search(full, ())
    if choice is None:
        return None

    core = 0
    for _, subset in choice:
        core |= subset
    return full ^ core, sorted(choice)


def fixed(n: int, mask: int, min_degree: int) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    partition = feedback_partition(adj, min_degree)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"min_degree={min_degree}")
    print(f"spectrum_mass={mass}")
    print(f"by_degree={by_degree}")
    print(f"feedback_partition_exists={partition is not None}")
    if partition is not None:
        forest, core_parts = partition
        print(f"forest vertices={subset_vertices(forest, n)}")
        for degree, subset in core_parts:
            print(f"core degree={degree} vertices={subset_vertices(subset, n)}")


def exact(n: int, equality_only: bool, min_degree: int) -> None:
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
        if feedback_partition(adj, min_degree) is not None:
            passed += 1
        elif len(bad_examples) < 10:
            bad_examples.append((mask, mass, by_degree))
    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"equality_only={equality_only}")
    print(f"min_degree={min_degree}")
    print(f"checked={checked}")
    print(f"feedback_partition_count={passed}")
    print(f"all_checked_have_feedback_partition={passed == checked}")
    for mask, mass, by_degree in bad_examples:
        print(f"bad mask={mask} mass={mass} by_degree={by_degree}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--equality-only", action="store_true")
    parser.add_argument("--min-degree", type=int, default=2)
    args = parser.parse_args()

    if args.mask is None:
        exact(args.n, args.equality_only, args.min_degree)
    else:
        fixed(args.n, args.mask, args.min_degree)


if __name__ == "__main__":
    main()
