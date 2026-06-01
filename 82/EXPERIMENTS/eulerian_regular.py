#!/usr/bin/env python3
"""Enumerate or sample fixed degree-parity graphs for regular witnesses."""

from __future__ import annotations

import argparse
import random
from collections import Counter
from itertools import combinations
from time import monotonic

import column_drop_census as cdc


def parity_columns(n: int, free_mask: int, parity: int) -> list[int] | None:
    """Return columns for a graph with all degrees parity, or None if impossible."""
    if parity not in (0, 1):
        raise ValueError("parity must be 0 or 1")
    if (n * parity) % 2:
        return None

    columns = [0] * n
    free_edges = list(combinations(range(n - 1), 2))
    degree_parities = [0] * n
    for index, (u, v) in enumerate(free_edges):
        if (free_mask >> index) & 1:
            columns[v] |= 1 << u
            degree_parities[u] ^= 1
            degree_parities[v] ^= 1

    for v in range(n - 1):
        if degree_parities[v] != parity:
            columns[n - 1] |= 1 << v
            degree_parities[v] ^= 1
            degree_parities[n - 1] ^= 1

    if degree_parities[n - 1] != parity:
        return None
    return columns


def exact(n: int, parity: int, progress: int) -> None:
    pc = cdc.precompute(n)
    free_count = (n - 1) * (n - 2) // 2
    total = 1 << free_count
    histogram: Counter[int] = Counter()
    best = n + 1
    best_examples: list[tuple[int, int, int, tuple[int, ...], list[int]]] = []
    start = monotonic()

    for free_mask in range(total):
        columns = parity_columns(n, free_mask, parity)
        if columns is None:
            continue
        adj = cdc.columns_to_adjacency(columns)
        regular, degree, vertices = cdc.max_regular(adj, pc)
        histogram[regular] += 1
        if regular < best:
            best = regular
            best_examples = []
        if regular == best and len(best_examples) < 10:
            best_examples.append(
                (free_mask, cdc.columns_to_mask(columns, pc), degree, vertices, columns)
            )
        if progress and free_mask and free_mask % progress == 0:
            print(
                f"progress free_mask={free_mask}/{total} best={best} "
                f"elapsed={monotonic() - start:.1f}s",
                flush=True,
            )

    print(f"n={n}")
    print(f"degree_parity={parity}")
    print(f"free_graphs={total}")
    print(f"min_max_regular={best}")
    print(f"histogram={dict(sorted(histogram.items()))}")
    for free_mask, mask, degree, vertices, columns in best_examples:
        print(
            f"example free_mask={free_mask} mask={mask} regular_degree={degree} "
            "regular_vertices="
            + ",".join(map(str, vertices))
            + " columns="
            + ",".join(map(str, columns))
        )


def sample(n: int, parity: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = cdc.precompute(n)
    free_count = (n - 1) * (n - 2) // 2
    histogram: Counter[int] = Counter()
    best = n + 1
    best_example: tuple[int, int, int, tuple[int, ...], list[int]] | None = None

    for _ in range(trials):
        free_mask = rng.getrandbits(free_count)
        columns = parity_columns(n, free_mask, parity)
        if columns is None:
            continue
        adj = cdc.columns_to_adjacency(columns)
        regular, degree, vertices = cdc.max_regular(adj, pc)
        histogram[regular] += 1
        if regular < best:
            best = regular
            best_example = (
                free_mask,
                cdc.columns_to_mask(columns, pc),
                degree,
                vertices,
                columns,
            )

    print(f"n={n}")
    print(f"degree_parity={parity}")
    print(f"trials={trials}")
    print(f"min_seen={best}")
    print(f"histogram={dict(sorted(histogram.items()))}")
    if best_example is not None:
        free_mask, mask, degree, vertices, columns = best_example
        print(
            f"best_example free_mask={free_mask} mask={mask} regular_degree={degree} "
            "regular_vertices="
            + ",".join(map(str, vertices))
            + " columns="
            + ",".join(map(str, columns))
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--parity", type=int, choices=[0, 1], default=0)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--progress", type=int, default=0)
    args = parser.parse_args()

    if args.sample:
        sample(args.n, args.parity, args.sample, args.seed)
    else:
        exact(args.n, args.parity, args.progress)


if __name__ == "__main__":
    main()
