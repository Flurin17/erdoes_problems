#!/usr/bin/env python3
"""Compute regular induced-subgraph spectra and disjoint-union obstructions."""

from __future__ import annotations

import argparse
import random
from itertools import combinations

import regular_bitset


def subset_mask(vertices: tuple[int, ...]) -> int:
    out = 0
    for vertex in vertices:
        out |= 1 << vertex
    return out


def regular_spectrum(n: int, mask: int) -> set[tuple[int, int]]:
    adj = regular_bitset.build_adjacency(n, mask)
    spectrum: set[tuple[int, int]] = set()
    for order in range(1, n + 1):
        for vertices in combinations(range(n), order):
            degree = regular_bitset.regular_degree(adj, subset_mask(vertices), vertices)
            if degree is not None:
                spectrum.add((order, degree))
    return spectrum


def obstructs_disjoint_union(
    spectrum_a: set[tuple[int, int]],
    spectrum_b: set[tuple[int, int]],
    h: int,
) -> bool:
    if any(order >= h for order, _degree in spectrum_a | spectrum_b):
        return False
    by_degree_a: dict[int, int] = {}
    by_degree_b: dict[int, int] = {}
    for order, degree in spectrum_a:
        by_degree_a[degree] = max(by_degree_a.get(degree, 0), order)
    for order, degree in spectrum_b:
        by_degree_b[degree] = max(by_degree_b.get(degree, 0), order)
    for degree in by_degree_a.keys() & by_degree_b.keys():
        if by_degree_a[degree] + by_degree_b[degree] >= h:
            return False
    return True


def format_spectrum(spectrum: set[tuple[int, int]]) -> str:
    return " ".join(f"{order}:{degree}" for order, degree in sorted(spectrum))


def inspect(args: argparse.Namespace) -> None:
    spectrum_a = regular_spectrum(args.n, args.mask_a)
    print(f"n={args.n}")
    print(f"h={args.h}")
    print(f"mask_a={args.mask_a}")
    print("spectrum_a=" + format_spectrum(spectrum_a))
    if args.mask_b is None:
        return
    spectrum_b = regular_spectrum(args.n, args.mask_b)
    print(f"mask_b={args.mask_b}")
    print("spectrum_b=" + format_spectrum(spectrum_b))
    print(f"disjoint_union_obstruction={obstructs_disjoint_union(spectrum_a, spectrum_b, args.h)}")


def random_pairs(args: argparse.Namespace) -> None:
    rng = random.Random(args.seed)
    edge_count = args.n * (args.n - 1) // 2
    spectra: list[tuple[int, set[tuple[int, int]]]] = []
    for _ in range(args.samples):
        mask = rng.getrandbits(edge_count)
        spectrum = regular_spectrum(args.n, mask)
        if not any(order >= args.h for order, _degree in spectrum):
            spectra.append((mask, spectrum))

    print(f"n={args.n}")
    print(f"h={args.h}")
    print(f"samples={args.samples}")
    print(f"h_counterexamples={len(spectra)}")
    for i, (mask_a, spectrum_a) in enumerate(spectra):
        for mask_b, spectrum_b in spectra[i:]:
            if obstructs_disjoint_union(spectrum_a, spectrum_b, args.h):
                print("disjoint_union_obstruction_found=True")
                print(f"mask_a={mask_a}")
                print(f"mask_b={mask_b}")
                print("spectrum_a=" + format_spectrum(spectrum_a))
                print("spectrum_b=" + format_spectrum(spectrum_b))
                return
    print("disjoint_union_obstruction_found=False")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--h", type=int, required=True)
    parser.add_argument("--mask-a", type=int)
    parser.add_argument("--mask-b", type=int)
    parser.add_argument("--samples", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()

    if args.samples:
        random_pairs(args)
        return
    if args.mask_a is None:
        parser.error("--mask-a is required unless --samples is used")
    inspect(args)


if __name__ == "__main__":
    main()
