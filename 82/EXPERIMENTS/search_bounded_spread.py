#!/usr/bin/env python3
"""Local search for bounded-spread graphs with small regular induced subgraphs."""

from __future__ import annotations

import argparse
import random

import degree_spread
import regular_induced as ri


def flip(mask: int, edge_idx: int) -> int:
    return mask ^ (1 << edge_idx)


def score(mask: int, pc: ri.Precomp, max_spread: int) -> tuple[int, int]:
    full = (1 << pc.n) - 1
    spread = degree_spread.degree_spread(mask, full, pc)
    penalty = max(0, spread - max_spread)
    reg = ri.max_regular_order(mask, pc)
    return penalty, reg


def threshold_score(mask: int, pc: ri.Precomp, max_spread: int, target: int) -> tuple[int, int]:
    full = (1 << pc.n) - 1
    spread = degree_spread.degree_spread(mask, full, pc)
    penalty = max(0, spread - max_spread)
    if penalty:
        return penalty, target
    has_large = ri.has_regular_order_at_least(mask, target, pc)
    return 0, target if has_large else target - 1


def neighborhood_search(
    n: int, max_spread: int, steps: int, restarts: int, seed: int, target: int
) -> None:
    """Local search biased toward feasible graphs with regular order below target."""
    rng = random.Random(seed)
    pc = ri.precompute(n)
    m = len(pc.edges)
    best: tuple[int, int] | None = None
    best_mask = 0

    for restart in range(restarts):
        mask = rng.getrandbits(m)
        current = score(mask, pc, max_spread)
        current_energy = current[0] * (pc.n + 1) + current[1]
        for step in range(steps):
            candidates = [rng.randrange(m) for _ in range(min(10, m))]
            chosen_mask = mask
            chosen_score = current
            chosen_energy = current_energy
            for edge_idx in candidates:
                candidate_mask = flip(mask, edge_idx)
                candidate_score = score(candidate_mask, pc, max_spread)
                candidate_energy = candidate_score[0] * (pc.n + 1) + candidate_score[1]
                if candidate_energy < chosen_energy:
                    chosen_mask = candidate_mask
                    chosen_score = candidate_score
                    chosen_energy = candidate_energy
            if chosen_mask == mask:
                edge_idx = rng.randrange(m)
                chosen_mask = flip(mask, edge_idx)
                chosen_score = score(chosen_mask, pc, max_spread)
                chosen_energy = chosen_score[0] * (pc.n + 1) + chosen_score[1]
            mask = chosen_mask
            current = chosen_score
            current_energy = chosen_energy

            if current[0] == 0:
                if best is None or current[1] < best[1]:
                    best = current
                    best_mask = mask
                    print(
                        f"restart={restart} step={step} "
                        f"best_regular={current[1]} mask={best_mask}",
                        flush=True,
                    )
                if current[1] < target:
                    print("target_counterexample_found")
                    print(f"n={n}")
                    print(f"max_spread={max_spread}")
                    print(f"target={target}")
                    print(f"regular_order={current[1]}")
                    print(f"mask={mask}")
                    return

    print(f"n={n}")
    print(f"max_spread={max_spread}")
    print(f"steps={steps}")
    print(f"restarts={restarts}")
    print(f"target={target}")
    if best is None:
        print("no_feasible_graph_found")
    else:
        print(f"best_regular={best[1]}")
        print(f"best_mask={best_mask}")


def threshold_search(
    n: int, max_spread: int, steps: int, restarts: int, seed: int, target: int
) -> None:
    """Search using a cheaper threshold predicate before exact verification."""
    rng = random.Random(seed)
    pc = ri.precompute(n)
    m = len(pc.edges)
    best_candidate = 0
    for restart in range(restarts):
        mask = rng.getrandbits(m)
        current = threshold_score(mask, pc, max_spread, target)
        current_energy = current[0] * 2 + current[1]
        for step in range(steps):
            candidates = [rng.randrange(m) for _ in range(min(20, m))]
            chosen_mask = mask
            chosen_score = current
            chosen_energy = current_energy
            for edge_idx in candidates:
                candidate_mask = flip(mask, edge_idx)
                candidate_score = threshold_score(candidate_mask, pc, max_spread, target)
                candidate_energy = candidate_score[0] * 2 + candidate_score[1]
                if candidate_energy < chosen_energy:
                    chosen_mask = candidate_mask
                    chosen_score = candidate_score
                    chosen_energy = candidate_energy
            if chosen_mask == mask:
                edge_idx = rng.randrange(m)
                chosen_mask = flip(mask, edge_idx)
                chosen_score = threshold_score(chosen_mask, pc, max_spread, target)
                chosen_energy = chosen_score[0] * 2 + chosen_score[1]
            mask = chosen_mask
            current = chosen_score
            current_energy = chosen_energy
            if current == (0, target - 1):
                exact = ri.max_regular_order(mask, pc)
                print("target_counterexample_found")
                print(f"n={n}")
                print(f"max_spread={max_spread}")
                print(f"target={target}")
                print(f"regular_order={exact}")
                print(f"mask={mask}")
                return
            if current[0] == 0:
                best_candidate = mask
    print(f"n={n}")
    print(f"max_spread={max_spread}")
    print(f"steps={steps}")
    print(f"restarts={restarts}")
    print(f"target={target}")
    print("no_target_counterexample_found")
    if best_candidate:
        print(f"sample_feasible_mask={best_candidate}")


def search(n: int, max_spread: int, steps: int, restarts: int, seed: int) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    m = len(pc.edges)
    best_feasible: tuple[int, int] | None = None
    best_mask = 0

    for restart in range(restarts):
        mask = rng.getrandbits(m)
        current = score(mask, pc, max_spread)
        temperature = 1.0
        for step in range(steps):
            edge_idx = rng.randrange(m)
            candidate_mask = flip(mask, edge_idx)
            candidate = score(candidate_mask, pc, max_spread)

            delta = (candidate[0] - current[0], candidate[1] - current[1])
            accept = candidate <= current
            if not accept and rng.random() < temperature / (1.0 + abs(delta[0]) * 10 + abs(delta[1])):
                accept = True
            if accept:
                mask = candidate_mask
                current = candidate

            if current[0] == 0:
                feasible = (current[1], step)
                if best_feasible is None or feasible[0] < best_feasible[0]:
                    best_feasible = feasible
                    best_mask = mask
                    print(
                        f"restart={restart} step={step} "
                        f"best_regular={current[1]} mask={best_mask}",
                        flush=True,
                    )
            temperature *= 0.9995

    print(f"n={n}")
    print(f"max_spread={max_spread}")
    print(f"steps={steps}")
    print(f"restarts={restarts}")
    if best_feasible is None:
        print("no_feasible_graph_found")
    else:
        print(f"best_regular={best_feasible[0]}")
        print(f"best_mask={best_mask}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--max-spread", type=int, required=True)
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--restarts", type=int, default=20)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--target", type=int)
    parser.add_argument("--threshold-only", action="store_true")
    args = parser.parse_args()
    if args.target is not None:
        if args.threshold_only:
            threshold_search(
                args.n, args.max_spread, args.steps, args.restarts, args.seed, args.target
            )
            return
        neighborhood_search(
            args.n, args.max_spread, args.steps, args.restarts, args.seed, args.target
        )
        return
    search(args.n, args.max_spread, args.steps, args.restarts, args.seed)


if __name__ == "__main__":
    main()
