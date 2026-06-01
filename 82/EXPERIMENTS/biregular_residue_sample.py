#!/usr/bin/env python3
"""Sample row-residue dependence in regular bipartite graphs.

The model is a simple d-regular bipartite graph with N rows and N columns.
It starts from a circulant d-regular graph and applies degree-preserving
2-switches.  For a fixed row set X0 and column set Y0, it estimates the
probability that all rows in X0 have the same number of neighbors in Y0
modulo M, comparing against the prediction from independent hypergeometric
rows with the same one-row marginal.
"""

from __future__ import annotations

import argparse
import math
import random


def log_comb(n: int, k: int) -> float:
    if k < 0 or k > n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def hypergeom_residue_distribution(
    population: int, marked: int, draws: int, modulus: int
) -> list[float]:
    low = max(0, draws - (population - marked))
    high = min(marked, draws)
    denominator = log_comb(population, draws)
    residues = [0.0] * modulus
    for hits in range(low, high + 1):
        probability = math.exp(
            log_comb(marked, hits)
            + log_comb(population - marked, draws - hits)
            - denominator
        )
        residues[hits % modulus] += probability
    return residues


def independent_equal_probability(distribution: list[float], row_count: int) -> float:
    return sum(probability**row_count for probability in distribution)


def circulant_rows(n: int, degree: int) -> list[set[int]]:
    return [{(row + offset) % n for offset in range(degree)} for row in range(n)]


def switch_once(rows: list[set[int]], rng: random.Random) -> bool:
    n = len(rows)
    r1, r2 = rng.sample(range(n), 2)
    only1 = tuple(rows[r1] - rows[r2])
    only2 = tuple(rows[r2] - rows[r1])
    if not only1 or not only2:
        return False
    c1 = rng.choice(only1)
    c2 = rng.choice(only2)
    rows[r1].remove(c1)
    rows[r1].add(c2)
    rows[r2].remove(c2)
    rows[r2].add(c1)
    return True


def run_switches(rows: list[set[int]], count: int, rng: random.Random) -> None:
    attempts = 0
    accepted = 0
    # In dense identical rows many attempted switches are invalid; cap attempts.
    while accepted < count and attempts < 20 * count + 100:
        attempts += 1
        if switch_once(rows, rng):
            accepted += 1


def residue_event(rows: list[set[int]], row_count: int, marked: int, modulus: int) -> bool:
    marked_set = set(range(marked))
    residues = [
        len(rows[row] & marked_set) % modulus
        for row in range(row_count)
    ]
    return all(residue == residues[0] for residue in residues[1:])


def hit_histogram(rows: list[set[int]], row_count: int, marked: int) -> dict[int, int]:
    marked_set = set(range(marked))
    out: dict[int, int] = {}
    for row in range(row_count):
        hits = len(rows[row] & marked_set)
        out[hits] = out.get(hits, 0) + 1
    return dict(sorted(out.items()))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--degree", type=int, required=True)
    parser.add_argument("--marked", type=int, required=True)
    parser.add_argument("--rows", type=int, required=True)
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--burnin", type=int, default=10000)
    parser.add_argument("--between", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()

    if not (0 <= args.degree <= args.n):
        parser.error("need 0 <= degree <= n")
    if not (0 <= args.marked <= args.n):
        parser.error("need 0 <= marked <= n")
    if not (1 <= args.rows <= args.n):
        parser.error("need 1 <= rows <= n")

    rng = random.Random(args.seed)
    rows = circulant_rows(args.n, args.degree)
    run_switches(rows, args.burnin, rng)

    hits = 0
    first_hist: dict[int, int] = {}
    last_hist: dict[int, int] = {}
    for sample in range(args.samples):
        run_switches(rows, args.between, rng)
        if residue_event(rows, args.rows, args.marked, args.modulus):
            hits += 1
        if sample == 0:
            first_hist = hit_histogram(rows, args.rows, args.marked)
        if sample == args.samples - 1:
            last_hist = hit_histogram(rows, args.rows, args.marked)

    distribution = hypergeom_residue_distribution(
        args.n, args.marked, args.degree, args.modulus
    )
    independent = independent_equal_probability(distribution, args.rows)
    empirical = hits / args.samples if args.samples else 0.0

    print(f"n={args.n}")
    print(f"degree={args.degree}")
    print(f"marked={args.marked}")
    print(f"rows={args.rows}")
    print(f"modulus={args.modulus}")
    print(f"samples={args.samples}")
    print(f"burnin={args.burnin}")
    print(f"between={args.between}")
    print(f"seed={args.seed}")
    print(f"empirical_equal_residue_probability={empirical:.12g}")
    print(f"independent_row_prediction={independent:.12g}")
    if independent > 0:
        print(f"empirical_over_independent={empirical / independent:.12g}")
    print(
        "one_row_residue_distribution="
        + ",".join(f"{i}:{p:.12g}" for i, p in enumerate(distribution))
    )
    print(f"first_sample_hit_histogram={first_hist}")
    print(f"last_sample_hit_histogram={last_hist}")


if __name__ == "__main__":
    main()
