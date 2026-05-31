#!/usr/bin/env python3
"""Local search for a fixed-color modular partition.

This attacks modular partitioning as a coloring problem.  For a coloring,
each color class is scored by the number of vertices outside its most common
internal-degree residue modulo the target modulus.  Score zero is a valid
modular partition.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations, product

import modular_partition
import regular_induced as ri


def residues_for_assignment(
    n: int,
    graph_mask: int,
    modulus: int,
    assignment: list[int],
    colors: int,
    pc: ri.Precomp,
) -> list[list[int]]:
    subsets = [0] * colors
    for vertex, color in enumerate(assignment):
        subsets[color] |= 1 << vertex
    residues: list[list[int]] = [[] for _ in range(colors)]
    for vertex, color in enumerate(assignment):
        residue = (graph_mask & pc.incident[subsets[color]][vertex]).bit_count() % modulus
        residues[color].append(residue)
    return residues


def score_residues(residues: list[list[int]], modulus: int) -> int:
    score = 0
    for part in residues:
        if not part:
            continue
        counts = [0] * modulus
        for residue in part:
            counts[residue] += 1
        score += len(part) - max(counts)
    return score


def score_assignment(
    n: int,
    graph_mask: int,
    modulus: int,
    assignment: list[int],
    colors: int,
    pc: ri.Precomp,
) -> int:
    return score_residues(
        residues_for_assignment(n, graph_mask, modulus, assignment, colors, pc),
        modulus,
    )


def search(
    n: int,
    graph_mask: int,
    modulus: int,
    colors: int,
    restarts: int,
    steps: int,
    seed: int,
) -> tuple[int, list[int]]:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    best_score = n + 1
    best_assignment: list[int] = []

    for restart in range(restarts):
        assignment = [rng.randrange(colors) for _ in range(n)]
        current = score_assignment(n, graph_mask, modulus, assignment, colors, pc)
        temperature = max(1.0, n / 4)
        for step in range(steps):
            if current < best_score:
                best_score = current
                best_assignment = assignment[:]
                print(
                    f"restart={restart} step={step} best_score={best_score} "
                    + "assignment="
                    + ",".join(map(str, best_assignment)),
                    flush=True,
                )
                if best_score == 0:
                    return best_score, best_assignment

            vertex = rng.randrange(n)
            old_color = assignment[vertex]
            new_color = rng.randrange(colors - 1)
            if new_color >= old_color:
                new_color += 1
            assignment[vertex] = new_color
            candidate = score_assignment(n, graph_mask, modulus, assignment, colors, pc)
            accept = candidate <= current
            if not accept:
                accept = rng.random() < 2 ** ((current - candidate) / temperature)
            if accept:
                current = candidate
            else:
                assignment[vertex] = old_color
            temperature *= 0.9995

    return best_score, best_assignment


def search_with_repair(
    n: int,
    graph_mask: int,
    modulus: int,
    colors: int,
    restarts: int,
    steps: int,
    repair_depth: int,
    seed: int,
) -> tuple[int, list[int], str]:
    best_score, assignment = search(n, graph_mask, modulus, colors, restarts, steps, seed)
    repair_note = ""
    if repair_depth and assignment and best_score:
        best_score, assignment, repair_note = repair(
            n,
            graph_mask,
            modulus,
            colors,
            assignment,
            repair_depth,
        )
    return best_score, assignment, repair_note


def repair(
    n: int,
    graph_mask: int,
    modulus: int,
    colors: int,
    assignment: list[int],
    max_depth: int,
) -> tuple[int, list[int], str]:
    pc = ri.precompute(n)
    best_score = score_assignment(n, graph_mask, modulus, assignment, colors, pc)
    best_assignment = assignment[:]
    if best_score == 0:
        return best_score, best_assignment, "already_valid"

    for depth in range(1, max_depth + 1):
        for vertices in combinations(range(n), depth):
            choices = []
            for vertex in vertices:
                old = assignment[vertex]
                choices.append([color for color in range(colors) if color != old])
            for new_colors in product(*choices):
                candidate_assignment = assignment[:]
                for vertex, color in zip(vertices, new_colors):
                    candidate_assignment[vertex] = color
                candidate_score = score_assignment(
                    n, graph_mask, modulus, candidate_assignment, colors, pc
                )
                if candidate_score < best_score:
                    best_score = candidate_score
                    best_assignment = candidate_assignment
                    if best_score == 0:
                        return (
                            best_score,
                            best_assignment,
                            "changed="
                            + ",".join(
                                f"{vertex}->{color}"
                                for vertex, color in zip(vertices, new_colors)
                            ),
                        )
        assignment = best_assignment
    return best_score, best_assignment, "not_repaired"


def sample_full_modular(
    n: int,
    full_modulus: int,
    modulus: int,
    colors: int,
    trials: int,
    restarts: int,
    steps: int,
    repair_depth: int,
    seed: int,
    max_attempts: int,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    full = (1 << n) - 1
    edge_count = len(pc.edges)
    attempts = 0
    accepted = 0
    failures = 0
    worst_score = -1
    worst_mask = 0
    score_histogram: dict[int, int] = {}

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
        score, assignment, repair_note = search_with_repair(
            n,
            graph_mask,
            modulus,
            colors,
            restarts,
            steps,
            repair_depth,
            seed + accepted,
        )
        score_histogram[score] = score_histogram.get(score, 0) + 1
        if score > worst_score:
            worst_score = score
            worst_mask = graph_mask
        if score:
            failures += 1
            print(f"failure_trial={accepted}")
            print(f"failure_score={score}")
            print(f"failure_mask={graph_mask}")
            if assignment:
                print("failure_assignment=" + ",".join(map(str, assignment)))
            if repair_note:
                print(f"failure_repair_note={repair_note}")
            break

    print(f"n={n}")
    print(f"full_modulus={full_modulus}")
    print(f"modulus={modulus}")
    print(f"colors={colors}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"accepted={accepted}")
    print(f"failures={failures}")
    print(f"worst_score={worst_score}")
    print(f"worst_mask={worst_mask}")
    print("histogram=score:count")
    for score in sorted(score_histogram):
        print(f"  {score}: {score_histogram[score]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("mask", type=int, nargs="?")
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument("--colors", type=int, default=4)
    parser.add_argument("--restarts", type=int, default=100)
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--repair-depth", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--sample-full-modular", type=int, default=0)
    parser.add_argument("--full-modulus", type=int)
    parser.add_argument("--max-attempts", type=int, default=1000000)
    args = parser.parse_args()

    if args.sample_full_modular:
        if args.full_modulus is None:
            parser.error("--sample-full-modular requires --full-modulus")
        sample_full_modular(
            args.n,
            args.full_modulus,
            args.modulus,
            args.colors,
            args.sample_full_modular,
            args.restarts,
            args.steps,
            args.repair_depth,
            args.seed,
            args.max_attempts,
        )
        return

    if args.mask is None:
        parser.error("mask is required unless --sample-full-modular is used")

    best_score, assignment, repair_note = search_with_repair(
        args.n,
        args.mask,
        args.modulus,
        args.colors,
        args.restarts,
        args.steps,
        args.repair_depth,
        args.seed,
    )
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"modulus={args.modulus}")
    print(f"colors={args.colors}")
    print(f"restarts={args.restarts}")
    print(f"steps={args.steps}")
    if args.repair_depth:
        print(f"repair_depth={args.repair_depth}")
        print(f"repair_note={repair_note}")
    print(f"best_score={best_score}")
    if assignment:
        print("assignment=" + ",".join(map(str, assignment)))
        if best_score == 0:
            stats = modular_partition.assignment_stats(
                args.n, args.mask, assignment, args.modulus
            )
            print(
                "parts="
                + " ".join(
                    f"color{color}:size{size}:residue{residue}"
                    for color, size, residue in stats
                )
            )


if __name__ == "__main__":
    main()
