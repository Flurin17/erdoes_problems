#!/usr/bin/env python3
"""Deletion-critical diagnostics for the spectrum-mass parameter."""

from __future__ import annotations

import argparse
from collections import Counter

import column_drop_census as cdc
from regular_spectrum_mass import spectrum_mass


def delete_vertex(adj: list[int], removed: int) -> list[int]:
    n = len(adj)
    old_to_new: dict[int, int] = {}
    for v in range(n):
        if v != removed:
            old_to_new[v] = len(old_to_new)

    out = [0] * (n - 1)
    for u in range(n):
        if u == removed:
            continue
        nu = old_to_new[u]
        for v in range(u + 1, n):
            if v == removed or not ((adj[u] >> v) & 1):
                continue
            nv = old_to_new[v]
            out[nu] |= 1 << nv
            out[nv] |= 1 << nu
    return out


def deletion_drops(adj: list[int], pc: cdc.Precomp, pc_minus: cdc.Precomp) -> list[int]:
    mass, _ = spectrum_mass(adj, pc)
    drops = []
    for v in range(len(adj)):
        smaller = delete_vertex(adj, v)
        smaller_mass, _ = spectrum_mass(smaller, pc_minus)
        drops.append(mass - smaller_mass)
    return drops


def exact(n: int) -> None:
    pc = cdc.precompute(n)
    pc_minus = cdc.precompute(n - 1) if n > 1 else None
    total = 1 << len(pc.edges)
    mass_hist: Counter[int] = Counter()
    excess_hist: Counter[int] = Counter()
    max_drop_hist: Counter[int] = Counter()
    best_examples: list[tuple[int, int, dict[int, int], list[int]]] = []
    best_mass = n * n

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        mass, by_degree = spectrum_mass(adj, pc)
        mass_hist[mass] += 1
        excess_hist[mass - n] += 1
        if pc_minus is None:
            drops: list[int] = []
        else:
            drops = deletion_drops(adj, pc, pc_minus)
            max_drop_hist[max(drops)] += 1
        if mass < best_mass:
            best_mass = mass
            best_examples = []
        if mass == best_mass and len(best_examples) < 10:
            best_examples.append((mask, mass, by_degree, drops))

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"min_spectrum_mass={best_mass}")
    print(f"violates_mu_ge_n={best_mass < n}")
    print(f"mass_histogram={dict(sorted(mass_hist.items()))}")
    print(f"excess_histogram={dict(sorted(excess_hist.items()))}")
    if pc_minus is not None:
        print(f"max_deletion_drop_histogram={dict(sorted(max_drop_hist.items()))}")
    for mask, mass, by_degree, drops in best_examples:
        print(
            f"example mask={mask} mass={mass} "
            f"by_degree={by_degree} deletion_drops={drops}"
        )


def extend_mask(mask: int, n: int, column: int, pc: cdc.Precomp, pc_plus: cdc.Precomp) -> int:
    out = 0
    for index, (u, v) in enumerate(pc.edges):
        if (mask >> index) & 1:
            out |= 1 << pc_plus.edge_index[(u, v)]
    for u in range(n):
        if (column >> u) & 1:
            out |= 1 << pc_plus.edge_index[(u, n)]
    return out


def equality_extensions(n: int, limit: int | None) -> None:
    pc = cdc.precompute(n)
    pc_plus = cdc.precompute(n + 1)
    total = 1 << len(pc.edges)
    histogram: Counter[int] = Counter()
    equality_count = 0
    checked = 0
    bad_examples: list[tuple[int, int, int, dict[int, int]]] = []

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        mass, _ = spectrum_mass(adj, pc)
        if mass != n:
            continue
        equality_count += 1
        best = (n + 1) * (n + 1)
        best_column = 0
        best_by_degree: dict[int, int] = {}
        for column in range(1 << n):
            extended = extend_mask(mask, n, column, pc, pc_plus)
            extended_adj = cdc.adjacency(n + 1, extended, pc_plus)
            extended_mass, by_degree = spectrum_mass(extended_adj, pc_plus)
            if extended_mass < best:
                best = extended_mass
                best_column = column
                best_by_degree = by_degree
            if best < n + 1:
                break
        histogram[best - n] += 1
        checked += 1
        if best < n + 1 and len(bad_examples) < 10:
            bad_examples.append((mask, best_column, best, best_by_degree))
        if limit is not None and checked >= limit:
            break

    print(f"n={n}")
    print(f"equality_graphs_seen={equality_count}")
    print(f"equality_graphs_checked={checked}")
    print(f"extension_increment_histogram={dict(sorted(histogram.items()))}")
    print(f"violates_extension_lemma={bool(bad_examples)}")
    for mask, column, best, by_degree in bad_examples:
        print(
            f"bad mask={mask} column={column} "
            f"extended_mass={best} by_degree={by_degree}"
        )


def fixed(n: int, mask: int) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"spectrum_mass={mass}")
    print(f"excess={mass - n}")
    print(f"by_degree={by_degree}")
    if n > 1:
        pc_minus = cdc.precompute(n - 1)
        print(f"deletion_drops={deletion_drops(adj, pc, pc_minus)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--equality-extensions", action="store_true")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    if args.equality_extensions:
        equality_extensions(args.n, args.limit)
    elif args.mask is None:
        exact(args.n)
    else:
        fixed(args.n, args.mask)


if __name__ == "__main__":
    main()
