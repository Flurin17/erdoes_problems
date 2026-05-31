#!/usr/bin/env python3
"""Linear algebra for parity-pattern bipartitions of even graphs.

For an even graph with adjacency matrix A over F_2, a two-coloring x has
constant same-color degree parity on each side iff A x = a*1 + b*x for some
a,b in F_2.  This script solves the four affine systems.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations

import modular_partition
import regular_induced as ri


def adjacency_rows(n: int, graph_mask: int) -> list[int]:
    rows = [0] * n
    for idx, (u, v) in enumerate(combinations(range(n), 2)):
        if (graph_mask >> idx) & 1:
            rows[u] ^= 1 << v
            rows[v] ^= 1 << u
    return rows


def solve_affine(rows: list[int], rhs: list[int], n: int) -> tuple[int | None, list[int]]:
    """Return one solution and a nullspace basis for rows*x=rhs over F_2."""
    mat = rows[:]
    rhs = rhs[:]
    pivot_cols: list[int] = []
    row = 0
    for col in range(n):
        pivot = None
        for r in range(row, n):
            if (mat[r] >> col) & 1:
                pivot = r
                break
        if pivot is None:
            continue
        mat[row], mat[pivot] = mat[pivot], mat[row]
        rhs[row], rhs[pivot] = rhs[pivot], rhs[row]
        for r in range(n):
            if r != row and ((mat[r] >> col) & 1):
                mat[r] ^= mat[row]
                rhs[r] ^= rhs[row]
        pivot_cols.append(col)
        row += 1

    for r in range(row, n):
        if mat[r] == 0 and rhs[r]:
            return None, []

    pivot_set = set(pivot_cols)
    solution = 0
    for r, col in enumerate(pivot_cols):
        if rhs[r]:
            solution |= 1 << col

    basis: list[int] = []
    for free_col in range(n):
        if free_col in pivot_set:
            continue
        vector = 1 << free_col
        for r, col in enumerate(pivot_cols):
            if (mat[r] >> free_col) & 1:
                vector |= 1 << col
        basis.append(vector)

    return solution, basis


def sample_solution(solution: int, basis: list[int], mask: int) -> int:
    out = solution
    bit = 0
    while mask:
        if mask & 1:
            out ^= basis[bit]
        mask >>= 1
        bit += 1
    return out


def first_nontrivial(solution: int, basis: list[int], n: int) -> int | None:
    full = (1 << n) - 1
    limit = 1 << min(len(basis), 20)
    for mask in range(limit):
        candidate = sample_solution(solution, basis, mask)
        if candidate not in (0, full):
            return candidate
    if len(basis) > 20:
        # Deterministic fallback using individual basis vectors.
        for vector in basis:
            candidate = solution ^ vector
            if candidate not in (0, full):
                return candidate
    return None


def induced_mask(graph_mask: int, n: int, subset: int) -> tuple[int, int]:
    vertices = [v for v in range(n) if (subset >> v) & 1]
    index = {v: i for i, v in enumerate(vertices)}
    new_mask = 0
    new_idx = 0
    old_edges = list(combinations(range(n), 2))
    edge_bits = {edge: idx for idx, edge in enumerate(old_edges)}
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            old = (vertices[i], vertices[j])
            if (graph_mask >> edge_bits[old]) & 1:
                new_mask |= 1 << new_idx
            new_idx += 1
    return len(vertices), new_mask


def analyze(n: int, graph_mask: int) -> None:
    rows = adjacency_rows(n, graph_mask)
    full = (1 << n) - 1
    degrees = [row.bit_count() for row in rows]
    print(f"n={n}")
    print(f"mask={graph_mask}")
    print("degree_parities=" + ",".join(str(deg % 2) for deg in degrees))
    for a in (0, 1):
        for b in (0, 1):
            system_rows = [row ^ ((1 << i) if b else 0) for i, row in enumerate(rows)]
            rhs = [a] * n
            solution, basis = solve_affine(system_rows, rhs, n)
            print(f"system a={a} b={b}")
            if solution is None:
                print("  solvable=False")
                continue
            nontrivial = first_nontrivial(solution, basis, n)
            print("  solvable=True")
            print(f"  dimension={len(basis)}")
            print(f"  solution_count=2^{len(basis)}")
            print(f"  sample={solution}")
            print(f"  nontrivial_sample={nontrivial if nontrivial is not None else 'None'}")
            if nontrivial is not None:
                part0 = full ^ nontrivial
                part1 = nontrivial
                for label, subset in (("zero", part0), ("one", part1)):
                    sub_n, sub_mask = induced_mask(graph_mask, n, subset)
                    pc = ri.precompute(sub_n)
                    sub_full = (1 << sub_n) - 1
                    residue = modular_partition.residue_on(sub_mask, sub_full, 2, pc)
                    print(f"  {label}_size={sub_n} parity_residue={residue}")


def system_summary(n: int, graph_mask: int) -> tuple[int, int, int]:
    rows = adjacency_rows(n, graph_mask)
    full = (1 << n) - 1
    solvable = 0
    nontrivial = 0
    max_dimension = -1
    for a in (0, 1):
        for b in (0, 1):
            system_rows = [row ^ ((1 << i) if b else 0) for i, row in enumerate(rows)]
            rhs = [a] * n
            solution, basis = solve_affine(system_rows, rhs, n)
            if solution is None:
                continue
            solvable += 1
            max_dimension = max(max_dimension, len(basis))
            sample = first_nontrivial(solution, basis, n)
            if sample is not None and sample not in (0, full):
                nontrivial += 1
    return solvable, nontrivial, max_dimension


def sample_parity(n: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    hist: dict[tuple[int, int, int], int] = {}
    worst_key = (5, 5, 99)
    worst_mask = 0
    for _ in range(trials):
        graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        assert graph_mask is not None
        key = system_summary(n, graph_mask)
        hist[key] = hist.get(key, 0) + 1
        rank_key = (key[1], key[0], key[2])
        if rank_key < worst_key:
            worst_key = rank_key
            worst_mask = graph_mask

    print(f"n={n}")
    print("parity=even")
    print(f"trials={trials}")
    print(f"worst_mask={worst_mask}")
    print("histogram=solvable_systems,nontrivial_systems,max_dimension:count")
    for key in sorted(hist):
        print(f"  {key[0]},{key[1]},{key[2]}: {hist[key]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("mask", type=int, nargs="?")
    parser.add_argument("--sample-parity", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    if args.sample_parity:
        sample_parity(args.n, args.sample_parity, args.seed)
        return
    if args.mask is None:
        parser.error("mask is required unless --sample-parity is used")
    analyze(args.n, args.mask)


if __name__ == "__main__":
    main()
