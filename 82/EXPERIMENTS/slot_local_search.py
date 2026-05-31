#!/usr/bin/env python3
"""Heuristic search for fixed residue-slot modular partitions.

For a fixed slot multiset R=(r_0,...,r_{c-1}), a coloring is valid when every
vertex in color i has internal degree congruent to r_i modulo M.  This script
uses simulated annealing on the coloring space.  It is only a falsification
aid: a positive score is not a certificate that no slot partition exists.
"""

from __future__ import annotations

import argparse
import random

import modular_partition
import regular_induced as ri


DEFAULT_CANDIDATES = (
    (0, 0, 0, 1),
    (0, 0, 0, 2),
    (0, 0, 1, 1),
    (0, 0, 1, 2),
    (0, 0, 1, 3),
    (0, 0, 2, 2),
    (0, 0, 2, 3),
    (0, 1, 1, 1),
    (0, 1, 1, 2),
    (0, 1, 1, 3),
    (0, 1, 2, 2),
)


def parse_candidates(text: str | None, modulus: int) -> list[tuple[int, ...]]:
    if not text:
        return list(DEFAULT_CANDIDATES)
    candidates: list[tuple[int, ...]] = []
    for block in text.split(";"):
        if block:
            candidates.append(tuple(int(item) % modulus for item in block.split(",")))
    return candidates


def subsets_from_assignment(assignment: list[int], colors: int) -> list[int]:
    subsets = [0] * colors
    for vertex, color in enumerate(assignment):
        subsets[color] |= 1 << vertex
    return subsets


def score_assignment(
    n: int,
    graph_mask: int,
    modulus: int,
    slots: tuple[int, ...],
    assignment: list[int],
    pc: ri.Precomp,
) -> int:
    subsets = subsets_from_assignment(assignment, len(slots))
    score = 0
    for vertex, color in enumerate(assignment):
        degree = (graph_mask & pc.incident[subsets[color]][vertex]).bit_count()
        if degree % modulus != slots[color]:
            score += 1
    return score


def local_search(
    n: int,
    graph_mask: int,
    modulus: int,
    slots: tuple[int, ...],
    restarts: int,
    steps: int,
    seed: int,
    pc: ri.Precomp,
) -> tuple[int, list[int]]:
    rng = random.Random(seed)
    colors = len(slots)
    best_score = n + 1
    best_assignment: list[int] = []
    for restart in range(restarts):
        assignment = [rng.randrange(colors) for _ in range(n)]
        current = score_assignment(n, graph_mask, modulus, slots, assignment, pc)
        temperature = max(1.0, n / 3)
        for step in range(steps):
            if current < best_score:
                best_score = current
                best_assignment = assignment[:]
                if best_score == 0:
                    return best_score, best_assignment
            vertex = rng.randrange(n)
            old_color = assignment[vertex]
            new_color = rng.randrange(colors - 1)
            if new_color >= old_color:
                new_color += 1
            assignment[vertex] = new_color
            candidate = score_assignment(n, graph_mask, modulus, slots, assignment, pc)
            accept = candidate <= current
            if not accept:
                accept = rng.random() < 2 ** ((current - candidate) / temperature)
            if accept:
                current = candidate
            else:
                assignment[vertex] = old_color
            temperature *= 0.999
    return best_score, best_assignment


def sample_even(
    n: int,
    modulus: int,
    candidates: list[tuple[int, ...]],
    trials: int,
    restarts: int,
    steps: int,
    seed: int,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    worst: dict[tuple[int, ...], tuple[int, int, list[int]]] = {
        slots: (-1, 0, []) for slots in candidates
    }
    failures = 0
    for trial in range(1, trials + 1):
        graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        if graph_mask is None:
            continue
        for idx, slots in enumerate(candidates):
            score, assignment = local_search(
                n,
                graph_mask,
                modulus,
                slots,
                restarts,
                steps,
                seed + 1009 * trial + idx,
                pc,
            )
            if score > worst[slots][0]:
                worst[slots] = (score, graph_mask, assignment)
            if score:
                failures += 1
                print(
                    "heuristic_failure "
                    f"trial={trial} slots={','.join(map(str, slots))} "
                    f"score={score} mask={graph_mask}"
                )
                break
    print(f"n={n}")
    print(f"modulus={modulus}")
    print(f"sample_even_checked={trials}")
    print(f"heuristic_failures={failures}")
    for slots in candidates:
        score, graph_mask, assignment = worst[slots]
        print(
            "worst "
            f"slots={','.join(map(str, slots))} score={score} mask={graph_mask}"
        )
        if score > 0 and assignment:
            print("assignment=" + ",".join(map(str, assignment)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("mask", type=int, nargs="?")
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument("--slots", default="0,0,1,2")
    parser.add_argument("--candidates")
    parser.add_argument("--sample-even", type=int, default=0)
    parser.add_argument("--restarts", type=int, default=100)
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()

    if args.sample_even:
        sample_even(
            args.n,
            args.modulus,
            parse_candidates(args.candidates, args.modulus),
            args.sample_even,
            args.restarts,
            args.steps,
            args.seed,
        )
        return

    if args.mask is None:
        parser.error("mask is required unless --sample-even is used")
    slots = tuple(int(item) % args.modulus for item in args.slots.split(","))
    pc = ri.precompute(args.n)
    score, assignment = local_search(
        args.n,
        args.mask,
        args.modulus,
        slots,
        args.restarts,
        args.steps,
        args.seed,
        pc,
    )
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"modulus={args.modulus}")
    print("slots=" + ",".join(map(str, slots)))
    print(f"best_score={score}")
    if assignment:
        print("assignment=" + ",".join(map(str, assignment)))


if __name__ == "__main__":
    main()
