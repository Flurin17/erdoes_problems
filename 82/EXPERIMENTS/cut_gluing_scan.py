#!/usr/bin/env python3
"""Check spectrum mass under one-vertex cut gluing."""

from __future__ import annotations

import argparse
import random
from itertools import product

import column_drop_census as cdc
from regular_spectrum_mass import is_connected, spectrum_mass


GraphRecord = tuple[int, list[int], int, dict[int, int]]


def connected_graphs(n: int) -> list[GraphRecord]:
    pc = cdc.precompute(n)
    out: list[GraphRecord] = []
    for mask in range(1 << len(pc.edges)):
        adj = cdc.adjacency(n, mask, pc)
        if is_connected(adj):
            mass, by_degree = spectrum_mass(adj, pc)
            out.append((mask, adj, mass, by_degree))
    return out


def glue_at_roots(adj1: list[int], root1: int, adj2: list[int], root2: int) -> list[int]:
    n1 = len(adj1)
    n2 = len(adj2)
    root_map = {root2: root1}
    next_vertex = n1
    for v in range(n2):
        if v == root2:
            continue
        root_map[v] = next_vertex
        next_vertex += 1

    out = [0] * (n1 + n2 - 1)

    for i in range(n1):
        for j in range(i + 1, n1):
            if (adj1[i] >> j) & 1:
                out[i] |= 1 << j
                out[j] |= 1 << i

    for i in range(n2):
        for j in range(i + 1, n2):
            if (adj2[i] >> j) & 1:
                a = root_map[i]
                b = root_map[j]
                out[a] |= 1 << b
                out[b] |= 1 << a

    return out


def scan(n1: int, n2: int, samples: int | None, seed: int) -> None:
    graphs1 = connected_graphs(n1)
    graphs2 = connected_graphs(n2)
    total_exact = len(graphs1) * len(graphs2) * n1 * n2
    rng = random.Random(seed)
    pc_glued = cdc.precompute(n1 + n2 - 1)
    checked = 0
    min_surplus = n1 + n2
    best = None

    if samples is None:
        iterator = product(graphs1, range(n1), graphs2, range(n2))
        planned = total_exact
    else:
        iterator = (
            (
                rng.choice(graphs1),
                rng.randrange(n1),
                rng.choice(graphs2),
                rng.randrange(n2),
            )
            for _ in range(samples)
        )
        planned = samples

    for (mask1, adj1, mass1, by1), root1, (mask2, adj2, mass2, by2), root2 in iterator:
        glued = glue_at_roots(adj1, root1, adj2, root2)
        mass, by_degree = spectrum_mass(glued, pc_glued)
        surplus = mass - ((n1 + n2 - 1) - 1)
        checked += 1
        if surplus < min_surplus:
            min_surplus = surplus
            best = (mask1, root1, mass1, by1, mask2, root2, mass2, by2, mass, by_degree)
        if surplus < 0:
            break

    print(f"n1={n1}")
    print(f"n2={n2}")
    print(f"connected_graphs1={len(graphs1)}")
    print(f"connected_graphs2={len(graphs2)}")
    print(f"planned_checks={planned}")
    print(f"checked={checked}")
    print(f"min_surplus_over_defect_one={min_surplus}")
    if best is not None:
        mask1, root1, mass1, by1, mask2, root2, mass2, by2, mass, by_degree = best
        print(
            f"best left mask={mask1} root={root1} mass={mass1} by_degree={by1}"
        )
        print(
            f"best right mask={mask2} root={root2} mass={mass2} by_degree={by2}"
        )
        print(f"best glued mass={mass} by_degree={by_degree}")
    print(f"violation_found={min_surplus < 0}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n1", type=int)
    parser.add_argument("n2", type=int)
    parser.add_argument("--samples", type=int)
    parser.add_argument("--seed", type=int, default=82)
    args = parser.parse_args()
    scan(args.n1, args.n2, args.samples, args.seed)


if __name__ == "__main__":
    main()
