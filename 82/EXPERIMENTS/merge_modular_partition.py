#!/usr/bin/env python3
"""Greedy merge heuristic for modular induced partitions.

Start from singleton target-modular parts and repeatedly merge two parts whose
union is still target-modular.  This does not prove optimality, but it tests
whether hard modular partitions can be obtained by a simple compression
process.
"""

from __future__ import annotations

import argparse
import random

import modular_partition
import regular_induced as ri


def residue_on(graph_mask: int, subset: int, modulus: int, pc: ri.Precomp) -> int | None:
    return modular_partition.residue_on(graph_mask, subset, modulus, pc)


def greedy_merge(
    n: int,
    graph_mask: int,
    modulus: int,
    rng: random.Random,
    strategy: str,
    pc: ri.Precomp,
    residue_cache: dict[int, int | None],
) -> list[int]:
    parts = [1 << vertex for vertex in range(n)]
    for part in parts:
        residue_cache[part] = 0

    def residue(subset: int) -> int | None:
        if subset not in residue_cache:
            residue_cache[subset] = residue_on(graph_mask, subset, modulus, pc)
        return residue_cache[subset]

    while True:
        candidates: list[tuple[int, int, int]] = []
        for i in range(len(parts)):
            for j in range(i + 1, len(parts)):
                union = parts[i] | parts[j]
                if residue(union) is not None:
                    candidates.append((union.bit_count(), i, j))
        if not candidates:
            return parts

        if strategy == "largest":
            _, i, j = max(candidates)
        elif strategy == "smallest":
            _, i, j = min(candidates)
        else:
            _, i, j = rng.choice(candidates)

        parts[i] |= parts[j]
        parts.pop(j)


def assignment_from_parts(n: int, parts: list[int]) -> list[int]:
    assignment = [-1] * n
    for color, part in enumerate(parts):
        for vertex in range(n):
            if (part >> vertex) & 1:
                assignment[vertex] = color
    return assignment


def run_fixed(
    n: int,
    graph_mask: int,
    modulus: int,
    restarts: int,
    seed: int,
    strategy: str,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    residue_cache: dict[int, int | None] = {}
    best_parts: list[int] | None = None
    histogram: dict[int, int] = {}
    for _ in range(restarts):
        parts = greedy_merge(n, graph_mask, modulus, rng, strategy, pc, residue_cache)
        count = len(parts)
        histogram[count] = histogram.get(count, 0) + 1
        if best_parts is None or count < len(best_parts):
            best_parts = parts

    assert best_parts is not None
    assignment = assignment_from_parts(n, best_parts)
    print(f"n={n}")
    print(f"mask={graph_mask}")
    print(f"modulus={modulus}")
    print(f"strategy={strategy}")
    print(f"restarts={restarts}")
    print(f"best_parts={len(best_parts)}")
    print("histogram=parts:count")
    for key in sorted(histogram):
        print(f"  {key}: {histogram[key]}")
    print("assignment=" + ",".join(map(str, assignment)))
    stats = modular_partition.assignment_stats(n, graph_mask, assignment, modulus)
    print(
        "parts="
        + " ".join(
            f"color{color}:size{size}:residue{residue}"
            for color, size, residue in stats
        )
    )


def sample_parity(
    n: int,
    modulus: int,
    trials: int,
    restarts: int,
    seed: int,
    strategy: str,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    worst_count = -1
    worst_mask = 0
    histogram: dict[int, int] = {}
    for _ in range(trials):
        graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        assert graph_mask is not None
        residue_cache: dict[int, int | None] = {}
        best = n + 1
        for _ in range(restarts):
            parts = greedy_merge(n, graph_mask, modulus, rng, strategy, pc, residue_cache)
            best = min(best, len(parts))
        histogram[best] = histogram.get(best, 0) + 1
        if best > worst_count:
            worst_count = best
            worst_mask = graph_mask

    print(f"n={n}")
    print("parity=even")
    print(f"modulus={modulus}")
    print(f"strategy={strategy}")
    print(f"trials={trials}")
    print(f"restarts={restarts}")
    print(f"worst_parts={worst_count}")
    print(f"worst_mask={worst_mask}")
    print("histogram=best_parts:count")
    for key in sorted(histogram):
        print(f"  {key}: {histogram[key]}")


def sample_full_modular(
    n: int,
    full_modulus: int,
    modulus: int,
    trials: int,
    restarts: int,
    seed: int,
    strategy: str,
    max_attempts: int,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    full = (1 << n) - 1
    edge_count = len(pc.edges)
    accepted = 0
    attempts = 0
    worst_count = -1
    worst_mask = 0
    histogram: dict[int, int] = {}
    while accepted < trials and attempts < max_attempts:
        attempts += 1
        graph_mask = modular_partition.random_full_modular_candidate(
            n, full_modulus, edge_count, rng, pc, edge_index
        )
        if graph_mask is None:
            continue
        if not ri.is_modular_on(graph_mask, full, full_modulus, pc):
            continue
        accepted += 1
        residue_cache: dict[int, int | None] = {}
        best = n + 1
        for _ in range(restarts):
            parts = greedy_merge(n, graph_mask, modulus, rng, strategy, pc, residue_cache)
            best = min(best, len(parts))
        histogram[best] = histogram.get(best, 0) + 1
        if best > worst_count:
            worst_count = best
            worst_mask = graph_mask

    print(f"n={n}")
    print(f"full_modulus={full_modulus}")
    print(f"modulus={modulus}")
    print(f"strategy={strategy}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"accepted={accepted}")
    print(f"restarts={restarts}")
    print(f"worst_parts={worst_count}")
    print(f"worst_mask={worst_mask}")
    print("histogram=best_parts:count")
    for key in sorted(histogram):
        print(f"  {key}: {histogram[key]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("mask", type=int, nargs="?")
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument("--restarts", type=int, default=100)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--strategy", choices=["random", "largest", "smallest"], default="random")
    parser.add_argument("--sample-parity", type=int, default=0)
    parser.add_argument("--sample-full-modular", type=int, default=0)
    parser.add_argument("--full-modulus", type=int)
    parser.add_argument("--max-attempts", type=int, default=1000000)
    args = parser.parse_args()

    if args.sample_parity:
        sample_parity(
            args.n,
            args.modulus,
            args.sample_parity,
            args.restarts,
            args.seed,
            args.strategy,
        )
        return

    if args.sample_full_modular:
        if args.full_modulus is None:
            parser.error("--sample-full-modular requires --full-modulus")
        sample_full_modular(
            args.n,
            args.full_modulus,
            args.modulus,
            args.sample_full_modular,
            args.restarts,
            args.seed,
            args.strategy,
            args.max_attempts,
        )
        return

    if args.mask is None:
        parser.error("mask is required unless --sample-parity is used")
    run_fixed(args.n, args.mask, args.modulus, args.restarts, args.seed, args.strategy)


if __name__ == "__main__":
    main()
