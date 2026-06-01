#!/usr/bin/env python3
"""Search the spectrum-mass parameter mu(G)=sum_d s_d(G)."""

from __future__ import annotations

import argparse
import random
from collections import Counter
from time import monotonic

import column_drop_census as cdc


def spectrum_by_degree(adj: list[int], pc: cdc.Precomp) -> dict[int, int]:
    by_degree: dict[int, int] = {}
    for size, entries in pc.subsets_by_size:
        for subset, vertices in entries:
            degree = (adj[vertices[0]] & subset).bit_count()
            if degree in by_degree:
                continue
            if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                by_degree[degree] = size
        if len(by_degree) >= pc.n:
            break
    return dict(sorted(by_degree.items()))


def spectrum_mass(adj: list[int], pc: cdc.Precomp) -> tuple[int, dict[int, int]]:
    by_degree = spectrum_by_degree(adj, pc)
    return sum(by_degree.values()), by_degree


def exact(n: int, progress: int) -> None:
    pc = cdc.precompute(n)
    total = 1 << len(pc.edges)
    histogram: Counter[int] = Counter()
    best = n * n
    best_examples: list[tuple[int, dict[int, int]]] = []
    start = monotonic()

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        mass, by_degree = spectrum_mass(adj, pc)
        histogram[mass] += 1
        if mass < best:
            best = mass
            best_examples = []
        if mass == best and len(best_examples) < 10:
            best_examples.append((mask, by_degree))
        if progress and mask and mask % progress == 0:
            print(
                f"progress mask={mask}/{total} best={best} "
                f"elapsed={monotonic() - start:.1f}s",
                flush=True,
            )

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"min_spectrum_mass={best}")
    print(f"violates_mu_ge_n={best < n}")
    print(f"histogram={dict(sorted(histogram.items()))}")
    for mask, by_degree in best_examples:
        print(f"example mask={mask} by_degree={by_degree}")


def sample(n: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = cdc.precompute(n)
    bits = len(pc.edges)
    histogram: Counter[int] = Counter()
    best = n * n
    best_example: tuple[int, dict[int, int]] | None = None

    for _ in range(trials):
        mask = rng.getrandbits(bits)
        adj = cdc.adjacency(n, mask, pc)
        mass, by_degree = spectrum_mass(adj, pc)
        histogram[mass] += 1
        if mass < best:
            best = mass
            best_example = (mask, by_degree)

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"min_seen={best}")
    print(f"violates_mu_ge_n={best < n}")
    print(f"histogram={dict(sorted(histogram.items()))}")
    if best_example is not None:
        mask, by_degree = best_example
        print(f"best_example mask={mask} by_degree={by_degree}")


def local_search(n: int, steps: int, restarts: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = cdc.precompute(n)
    bits = len(pc.edges)
    global_best = n * n
    global_example: tuple[int, dict[int, int]] | None = None

    for restart in range(restarts):
        mask = rng.getrandbits(bits)
        adj = cdc.adjacency(n, mask, pc)
        value, by_degree = spectrum_mass(adj, pc)
        temperature = 0.02
        for step in range(steps):
            bit = rng.randrange(bits)
            candidate = mask ^ (1 << bit)
            candidate_adj = cdc.adjacency(n, candidate, pc)
            candidate_value, candidate_by_degree = spectrum_mass(candidate_adj, pc)
            if candidate_value <= value or rng.random() < temperature:
                mask = candidate
                value = candidate_value
                by_degree = candidate_by_degree
            if value < global_best:
                global_best = value
                global_example = (mask, by_degree)
                print(
                    f"new_best restart={restart} step={step} "
                    f"mass={value} mask={mask} by_degree={by_degree}",
                    flush=True,
                )
                if global_best < n:
                    break
        if global_best < n:
            break

    print(f"n={n}")
    print(f"steps={steps}")
    print(f"restarts={restarts}")
    print(f"min_seen={global_best}")
    print(f"violates_mu_ge_n={global_best < n}")
    if global_example is not None:
        mask, by_degree = global_example
        print(f"best_example mask={mask} by_degree={by_degree}")


def fixed(n: int, mask: int) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"spectrum_mass={mass}")
    print(f"violates_mu_ge_n={mass < n}")
    print(f"by_degree={by_degree}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--local-steps", type=int, default=0)
    parser.add_argument("--restarts", type=int, default=1)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--progress", type=int, default=0)
    args = parser.parse_args()

    if args.mask is not None:
        fixed(args.n, args.mask)
    elif args.local_steps:
        local_search(args.n, args.local_steps, args.restarts, args.seed)
    elif args.sample:
        sample(args.n, args.sample, args.seed)
    else:
        exact(args.n, args.progress)


if __name__ == "__main__":
    main()
