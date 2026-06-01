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
    args = parser.parse_args()

    if args.mask is None:
        exact(args.n)
    else:
        fixed(args.n, args.mask)


if __name__ == "__main__":
    main()
