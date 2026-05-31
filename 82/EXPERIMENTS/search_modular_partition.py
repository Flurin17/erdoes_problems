#!/usr/bin/env python3
"""Local search for parity graphs with high modular partition color number."""

from __future__ import annotations

import argparse
import random

import merge_modular_partition
import modular_partition
import regular_induced as ri


def triangle_indices(n: int, edge_index: dict[tuple[int, int], int]) -> list[tuple[int, int, int]]:
    triples = []
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                triples.append(
                    (
                        edge_index[(a, b)],
                        edge_index[(a, c)],
                        edge_index[(b, c)],
                    )
                )
    return triples


def flip_triangle(mask: int, triple: tuple[int, int, int]) -> int:
    for edge in triple:
        mask ^= 1 << edge
    return mask


def score(
    mask: int,
    n: int,
    modulus: int,
    max_colors: int,
    cache: dict[int, int],
    node_limit: int | None,
    merge_restarts: int,
    rng: random.Random,
) -> int:
    if mask in cache:
        return cache[mask]
    try:
        result = modular_partition.find_min_colors(
            n, mask, modulus, max_colors, None, 0, None, node_limit
        )
    except modular_partition.SearchLimitExceeded:
        result = None
        if merge_restarts:
            pc = ri.precompute(n)
            merge_cache: dict[int, int | None] = {}
            best = n + 1
            for _ in range(merge_restarts):
                parts = merge_modular_partition.greedy_merge(
                    n, mask, modulus, rng, "random", pc, merge_cache
                )
                best = min(best, len(parts))
            if best <= max_colors:
                value = best
                cache[mask] = value
                return value
    value = max_colors + 1 if result is None else result[0]
    cache[mask] = value
    return value


def search(
    n: int,
    modulus: int,
    max_colors: int,
    steps: int,
    restarts: int,
    seed: int,
    node_limit: int | None,
    merge_restarts: int,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    moves = triangle_indices(n, edge_index)
    cache: dict[int, int] = {}
    best_score = -1
    best_mask = 0

    for restart in range(restarts):
        mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        if mask is None:
            continue
        current = score(mask, n, modulus, max_colors, cache, node_limit, merge_restarts, rng)
        for step in range(steps):
            if current > best_score:
                best_score = current
                best_mask = mask
                print(
                    f"restart={restart} step={step} "
                    f"best_min_colors={best_score if best_score <= max_colors else 'NA'} "
                    f"mask={best_mask}",
                    flush=True,
                )
                if best_score > max_colors:
                    break

            candidate = flip_triangle(mask, rng.choice(moves))
            candidate_score = score(
                candidate,
                n,
                modulus,
                max_colors,
                cache,
                node_limit,
                merge_restarts,
                rng,
            )
            if candidate_score >= current or rng.randrange(10) == 0:
                mask = candidate
                current = candidate_score
        if best_score > max_colors:
            break

    print(f"n={n}")
    print(f"modulus={modulus}")
    print(f"max_colors={max_colors}")
    print(f"steps={steps}")
    print(f"restarts={restarts}")
    if node_limit is not None:
        print(f"node_limit={node_limit}")
    if merge_restarts:
        print(f"merge_restarts={merge_restarts}")
    print(f"evaluated_masks={len(cache)}")
    print(f"best_min_colors={best_score if best_score <= max_colors else 'NA'}")
    print(f"best_mask={best_mask}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument("--max-colors", type=int, default=4)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--restarts", type=int, default=10)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--node-limit", type=int)
    parser.add_argument("--merge-restarts", type=int, default=0)
    args = parser.parse_args()
    search(
        args.n,
        args.modulus,
        args.max_colors,
        args.steps,
        args.restarts,
        args.seed,
        args.node_limit,
        args.merge_restarts,
    )


if __name__ == "__main__":
    main()
