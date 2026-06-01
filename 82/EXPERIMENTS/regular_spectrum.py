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
    return max_same_degree_total(spectrum_a, spectrum_b) < h


def max_same_degree_total(
    spectrum_a: set[tuple[int, int]],
    spectrum_b: set[tuple[int, int]],
) -> int:
    by_degree_a = spectrum_by_degree(spectrum_a)
    by_degree_b = spectrum_by_degree(spectrum_b)
    best = 0
    for degree in by_degree_a.keys() & by_degree_b.keys():
        best = max(best, by_degree_a[degree] + by_degree_b[degree])
    return best


def spectrum_by_degree(spectrum: set[tuple[int, int]]) -> dict[int, int]:
    by_degree: dict[int, int] = {}
    for order, degree in spectrum:
        by_degree[degree] = max(by_degree.get(degree, 0), order)
    return dict(sorted(by_degree.items()))


def format_by_degree(spectrum: set[tuple[int, int]]) -> str:
    return " ".join(
        f"{degree}:{order}" for degree, order in spectrum_by_degree(spectrum).items()
    )


def spectrum_mass(spectrum: set[tuple[int, int]]) -> int:
    return sum(spectrum_by_degree(spectrum).values())


def format_spectrum(spectrum: set[tuple[int, int]]) -> str:
    return " ".join(f"{order}:{degree}" for order, degree in sorted(spectrum))


def inspect(args: argparse.Namespace) -> None:
    spectrum_a = regular_spectrum(args.n, args.mask_a)
    print(f"n={args.n}")
    print(f"h={args.h}")
    print(f"mask_a={args.mask_a}")
    print("spectrum_a=" + format_spectrum(spectrum_a))
    print("by_degree_a=" + format_by_degree(spectrum_a))
    print(f"spectrum_mass_a={spectrum_mass(spectrum_a)}")
    if args.mask_b is None:
        return
    spectrum_b = regular_spectrum(args.n, args.mask_b)
    print(f"mask_b={args.mask_b}")
    print("spectrum_b=" + format_spectrum(spectrum_b))
    print("by_degree_b=" + format_by_degree(spectrum_b))
    print(f"spectrum_mass_b={spectrum_mass(spectrum_b)}")
    print(f"max_same_degree_total={max_same_degree_total(spectrum_a, spectrum_b)}")
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
    best_value: int | None = None
    best_pair: tuple[int, set[tuple[int, int]], int, set[tuple[int, int]]] | None = None
    for i, (mask_a, spectrum_a) in enumerate(spectra):
        for mask_b, spectrum_b in spectra[i:]:
            value = max_same_degree_total(spectrum_a, spectrum_b)
            if best_value is None or value < best_value:
                best_value = value
                best_pair = (mask_a, spectrum_a, mask_b, spectrum_b)
            if value < args.h:
                print("disjoint_union_obstruction_found=True")
                print(f"mask_a={mask_a}")
                print(f"mask_b={mask_b}")
                print(f"max_same_degree_total={value}")
                print("spectrum_a=" + format_spectrum(spectrum_a))
                print("spectrum_b=" + format_spectrum(spectrum_b))
                return
    print("disjoint_union_obstruction_found=False")
    if best_pair is not None:
        mask_a, spectrum_a, mask_b, spectrum_b = best_pair
        print(f"best_max_same_degree_total={best_value}")
        print(f"best_mask_a={mask_a}")
        print(f"best_mask_b={mask_b}")
        print("best_spectrum_a=" + format_spectrum(spectrum_a))
        print("best_spectrum_b=" + format_spectrum(spectrum_b))


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
