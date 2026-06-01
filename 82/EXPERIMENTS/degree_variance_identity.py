#!/usr/bin/env python3
"""Verify the degree-variance counting identity from PROOF.md.

For each h-set S, let

    V(S) = sum_{u<v in S} (deg_S(u)-deg_S(v))^2.

The script compares the direct sum of V(S) over all h-subsets with the
pair-expanded formula involving global degree differences and neighborhood
symmetries.
"""

from __future__ import annotations

import argparse
import math
import random
from itertools import combinations

import regular_induced as ri


def graph_degrees(mask: int, pc: ri.Precomp) -> list[int]:
    full = (1 << pc.n) - 1
    return [(mask & pc.incident[full][v]).bit_count() for v in range(pc.n)]


def has_edge(mask: int, u: int, v: int, edge_index: dict[tuple[int, int], int]) -> bool:
    if u > v:
        u, v = v, u
    return bool(mask & (1 << edge_index[(u, v)]))


def direct_total(mask: int, h: int, pc: ri.Precomp) -> int:
    total = 0
    for vertices in combinations(range(pc.n), h):
        subset = sum(1 << v for v in vertices)
        degrees = {
            v: (mask & pc.incident[subset][v]).bit_count()
            for v in vertices
        }
        for u, v in combinations(vertices, 2):
            total += (degrees[u] - degrees[v]) ** 2
    return total


def pair_formula_total(mask: int, h: int, pc: ri.Precomp) -> tuple[int, int, int]:
    n = pc.n
    edge_index = {edge: index for index, edge in enumerate(pc.edges)}
    degrees = graph_degrees(mask, pc)
    degree_term = 0
    symmetry_term = 0
    for u, v in combinations(range(n), 2):
        degree_term += (degrees[u] - degrees[v]) ** 2
        symdiff = 0
        for w in range(n):
            if w == u or w == v:
                continue
            if has_edge(mask, u, w, edge_index) != has_edge(mask, v, w, edge_index):
                symdiff += 1
        symmetry_term += symdiff

    c4 = math.comb(n - 4, h - 4) if h >= 4 and n >= 4 else 0
    c3 = math.comb(n - 4, h - 3) if h >= 3 and n >= 4 else 0
    return c4 * degree_term + c3 * symmetry_term, degree_term, symmetry_term


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("h", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    if not (2 <= args.h <= args.n):
        parser.error("need 2 <= h <= n")

    pc = ri.precompute(args.n)
    rng = random.Random(args.seed)
    mask = args.mask
    if mask is None:
        mask = rng.getrandbits(len(pc.edges))

    direct = direct_total(mask, args.h, pc)
    formula, degree_term, symmetry_term = pair_formula_total(mask, args.h, pc)
    max_regular = ri.max_regular_order(mask, pc)
    lower = (args.h - 1) * math.comb(args.n, args.h) if max_regular < args.h else 0

    print(f"n={args.n}")
    print(f"h={args.h}")
    print(f"mask={mask}")
    print(f"max_regular_order={max_regular}")
    print(f"direct_total={direct}")
    print(f"formula_total={formula}")
    print(f"degree_difference_term={degree_term}")
    print(f"neighborhood_symdiff_term={symmetry_term}")
    print(f"counterexample_variance_lower_bound={lower}")
    assert direct == formula
    assert max_regular >= args.h or direct >= lower


if __name__ == "__main__":
    main()
