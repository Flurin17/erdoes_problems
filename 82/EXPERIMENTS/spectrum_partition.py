#!/usr/bin/env python3
"""Check spectral partitions for the spectrum-mass equality case.

A spectral partition chooses, for every degree d with s_d(G)>0, a maximum
induced d-regular set, and asks that these chosen sets be disjoint and cover
V(G).  This is stronger than mu(G)=|G| and is intended as a diagnostic for
the equality-extension route.
"""

from __future__ import annotations

import argparse
from collections import Counter

import column_drop_census as cdc
from regular_spectrum_mass import spectrum_mass


def maximum_regular_sets(
    adj: list[int], pc: cdc.Precomp, degree: int, order: int
) -> list[int]:
    out: list[int] = []
    for size, entries in pc.subsets_by_size:
        if size < order:
            break
        if size > order:
            continue
        for subset, vertices in entries:
            if (adj[vertices[0]] & subset).bit_count() != degree:
                continue
            if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                out.append(subset)
    return out


def spectral_partition(
    adj: list[int], pc: cdc.Precomp, by_degree: dict[int, int]
) -> list[tuple[int, int]] | None:
    full = (1 << pc.n) - 1
    options: list[tuple[int, list[int]]] = []
    for degree, order in by_degree.items():
        sets = maximum_regular_sets(adj, pc, degree, order)
        if not sets:
            return None
        options.append((degree, sets))

    options.sort(key=lambda item: len(item[1]))
    chosen: list[tuple[int, int]] = []

    def search(index: int, covered: int) -> bool:
        if index == len(options):
            return covered == full
        degree, sets = options[index]
        for subset in sets:
            if covered & subset:
                continue
            chosen.append((degree, subset))
            if search(index + 1, covered | subset):
                return True
            chosen.pop()
        return False

    if search(0, 0):
        return sorted(chosen)
    return None


def vertices(subset: int, n: int) -> tuple[int, ...]:
    return tuple(v for v in range(n) if (subset >> v) & 1)


def fixed(n: int, mask: int) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    partition = spectral_partition(adj, pc, by_degree)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"spectrum_mass={mass}")
    print(f"equality={mass == n}")
    print(f"by_degree={by_degree}")
    print(f"spectral_partition_exists={partition is not None}")
    if partition is not None:
        for degree, subset in partition:
            print(f"part degree={degree} vertices={vertices(subset, n)}")


def exact(n: int, equality_only: bool) -> None:
    pc = cdc.precompute(n)
    total = 1 << len(pc.edges)
    checked = 0
    equality_count = 0
    partition_count = 0
    mass_hist: Counter[int] = Counter()
    bad_examples: list[tuple[int, int, dict[int, int]]] = []

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        mass, by_degree = spectrum_mass(adj, pc)
        mass_hist[mass] += 1
        if equality_only and mass != n:
            continue
        checked += 1
        if mass == n:
            equality_count += 1
        partition = spectral_partition(adj, pc, by_degree)
        if partition is not None:
            partition_count += 1
        elif len(bad_examples) < 10:
            bad_examples.append((mask, mass, by_degree))

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"equality_only={equality_only}")
    print(f"checked={checked}")
    print(f"equality_count={equality_count}")
    print(f"spectral_partition_count={partition_count}")
    print(f"all_checked_have_spectral_partition={partition_count == checked}")
    print(f"mass_histogram={dict(sorted(mass_hist.items()))}")
    for mask, mass, by_degree in bad_examples:
        print(f"bad mask={mask} mass={mass} by_degree={by_degree}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--equality-only", action="store_true")
    args = parser.parse_args()

    if args.mask is None:
        exact(args.n, args.equality_only)
    else:
        fixed(args.n, args.mask)


if __name__ == "__main__":
    main()
