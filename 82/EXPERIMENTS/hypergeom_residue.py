#!/usr/bin/env python3
"""Residue mixing for hypergeometric cross-degrees.

This models one row of a bipartite graph after conditioning on a fixed row
degree: a row chooses `draws` neighbors uniformly from a population of
`population` vertices, of which `marked` lie in the tested subset.
"""

from __future__ import annotations

import argparse
import cmath
import math


def log_comb(n: int, k: int) -> float:
    if k < 0 or k > n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def residue_distribution(
    population: int,
    marked: int,
    draws: int,
    modulus: int,
) -> list[float]:
    low = max(0, draws - (population - marked))
    high = min(marked, draws)
    log_denominator = log_comb(population, draws)
    residues = [0.0] * modulus
    for hits in range(low, high + 1):
        log_probability = (
            log_comb(marked, hits)
            + log_comb(population - marked, draws - hits)
            - log_denominator
        )
        residues[hits % modulus] += math.exp(log_probability)
    return residues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--population", type=int, required=True)
    parser.add_argument("--marked", type=int, required=True)
    parser.add_argument("--draws", type=int, required=True)
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()

    distribution = residue_distribution(
        args.population, args.marked, args.draws, args.modulus
    )
    uniform = 1.0 / args.modulus
    max_probability = max(distribution)
    min_probability = min(distribution)
    total_variation = 0.5 * sum(abs(value - uniform) for value in distribution)
    variance = (
        args.draws
        * (args.marked / args.population)
        * (1.0 - args.marked / args.population)
        * ((args.population - args.draws) / (args.population - 1))
        if args.population > 1
        else 0.0
    )

    print(f"population={args.population}")
    print(f"marked={args.marked}")
    print(f"draws={args.draws}")
    print(f"modulus={args.modulus}")
    print(f"variance={variance:.6g}")
    print(f"max_residue_probability={max_probability:.12g}")
    print(f"min_residue_probability={min_probability:.12g}")
    print(f"uniform_probability={uniform:.12g}")
    print(f"max_over_uniform={max_probability / uniform:.12g}")
    print(f"total_variation={total_variation:.12g}")
    fourier = []
    for frequency in range(1, args.modulus):
        value = sum(
            probability
            * cmath.exp(2j * math.pi * frequency * residue / args.modulus)
            for residue, probability in enumerate(distribution)
        )
        fourier.append(abs(value))
    max_fourier = max(fourier, default=0.0)
    print(f"max_nontrivial_fourier_bias={max_fourier:.12g}")
    if args.show:
        print(
            "distribution="
            + ",".join(f"{index}:{value:.12g}" for index, value in enumerate(distribution))
        )


if __name__ == "__main__":
    main()
