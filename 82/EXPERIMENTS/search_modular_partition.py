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


def score_label(value: int, max_colors: int) -> str:
    if value == 0:
        return "unknown"
    if value <= max_colors:
        return str(value)
    return "none<=max"


def score(
    mask: int,
    n: int,
    modulus: int,
    max_colors: int,
    min_part_size: int,
    max_part_size: int | None,
    cache: dict[int, int],
    node_limit: int | None,
    merge_restarts: int,
    rng: random.Random,
) -> int:
    """Return a certified score, or 0 when the exact check hit node limits.

    Values 1..max_colors are certified minimum color counts up to max_colors.
    The value max_colors+1 means the exact search certified no partition with
    at most max_colors colors.  The value 0 means unknown.
    """
    if mask in cache:
        return cache[mask]
    try:
        result = modular_partition.find_min_colors(
            n, mask, modulus, max_colors, None, min_part_size, max_part_size, node_limit
        )
    except modular_partition.SearchLimitExceeded:
        if merge_restarts and min_part_size == 0 and max_part_size is None:
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
        cache[mask] = 0
        return 0
    value = max_colors + 1 if result is None else result[0]
    cache[mask] = value
    return value


def search(
    n: int,
    modulus: int,
    max_colors: int,
    min_part_size: int,
    max_part_size: int | None,
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
    unknown = 0

    for restart in range(restarts):
        mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        if mask is None:
            continue
        current = score(
            mask,
            n,
            modulus,
            max_colors,
            min_part_size,
            max_part_size,
            cache,
            node_limit,
            merge_restarts,
            rng,
        )
        if current == 0:
            unknown += 1
        for step in range(steps):
            if current > 0 and current > best_score:
                best_score = current
                best_mask = mask
                print(
                    f"restart={restart} step={step} "
                    f"best_min_colors={score_label(best_score, max_colors)} "
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
                min_part_size,
                max_part_size,
                cache,
                node_limit,
                merge_restarts,
                rng,
            )
            if candidate_score == 0:
                unknown += 1
            if candidate_score >= current or rng.randrange(10) == 0:
                mask = candidate
                current = candidate_score
        if best_score > max_colors:
            break

    print(f"n={n}")
    print(f"modulus={modulus}")
    print(f"max_colors={max_colors}")
    if min_part_size:
        print(f"min_part_size={min_part_size}")
    if max_part_size is not None:
        print(f"max_part_size={max_part_size}")
    print(f"steps={steps}")
    print(f"restarts={restarts}")
    if node_limit is not None:
        print(f"node_limit={node_limit}")
    if merge_restarts:
        print(f"merge_restarts={merge_restarts}")
    print(f"evaluated_masks={len(cache)}")
    print(f"unknown_evaluations={unknown}")
    if best_score <= 0:
        print("best_min_colors=unknown")
    else:
        print(f"best_min_colors={score_label(best_score, max_colors)}")
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
    parser.add_argument("--min-part-size", type=int, default=0)
    parser.add_argument("--max-part-size", type=int)
    args = parser.parse_args()
    search(
        args.n,
        args.modulus,
        args.max_colors,
        args.min_part_size,
        args.max_part_size,
        args.steps,
        args.restarts,
        args.seed,
        args.node_limit,
        args.merge_restarts,
    )


if __name__ == "__main__":
    main()
