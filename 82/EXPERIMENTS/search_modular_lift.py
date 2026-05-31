#!/usr/bin/env python3
"""Local search for weak first-step dyadic-lift examples.

This searches among graphs whose full vertex set is parity-modular, looking
for small largest 4-modular induced subgraphs.  It is a heuristic complement
to the exact enumeration in modular_lift.py.
"""

from __future__ import annotations

import argparse
import math
import random

import regular_induced as ri


def free_edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n - 1) for j in range(i + 1, n - 1)]


def mask_from_free_bits(
    n: int,
    bits: int,
    odd: bool,
    edge_index: dict[tuple[int, int], int],
    free: list[tuple[int, int]],
) -> int | None:
    mask = 0
    parities = [0] * n
    target = 1 if odd else 0

    for bit, (i, j) in enumerate(free):
        if (bits >> bit) & 1:
            idx = edge_index[(i, j)]
            mask |= 1 << idx
            parities[i] ^= 1
            parities[j] ^= 1

    for i in range(n - 1):
        if parities[i] != target:
            idx = edge_index[(i, n - 1)]
            mask |= 1 << idx
            parities[i] ^= 1
            parities[n - 1] ^= 1

    if parities[n - 1] != target:
        return None
    return mask


def search(n: int, odd: bool, steps: int, restarts: int, seed: int, target: int | None) -> None:
    if odd and n % 2:
        raise SystemExit("odd parity requires even n")

    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    free = free_edges(n)
    free_count = len(free)

    best_value = n
    best_mask = 0
    best_bits = 0
    evaluations = 0

    for restart in range(restarts):
        bits = rng.getrandbits(free_count)
        mask = mask_from_free_bits(n, bits, odd, edge_index, free)
        if mask is None:
            continue
        value = ri.max_modular_order(mask, 4, pc)
        evaluations += 1
        temperature = 1.0

        for step in range(steps):
            if value < best_value:
                best_value = value
                best_mask = mask
                best_bits = bits
                print(
                    f"improved restart={restart} step={step} "
                    f"value={best_value} mask={best_mask}",
                    flush=True,
                )
                if target is not None and best_value < target:
                    break

            bit = rng.randrange(free_count)
            new_bits = bits ^ (1 << bit)
            new_mask = mask_from_free_bits(n, new_bits, odd, edge_index, free)
            if new_mask is None:
                continue
            new_value = ri.max_modular_order(new_mask, 4, pc)
            evaluations += 1

            if new_value <= value:
                accept = True
            else:
                accept = rng.random() < math.exp((value - new_value) / max(temperature, 1e-9))
            if accept:
                bits = new_bits
                mask = new_mask
                value = new_value
            temperature *= 0.999

        if target is not None and best_value < target:
            break

    print(f"n={n}")
    print(f"parity={'odd' if odd else 'even'}")
    print(f"steps={steps}")
    print(f"restarts={restarts}")
    print(f"evaluations={evaluations}")
    print(f"best_max_4_modular_order={best_value}")
    print(f"best_mask={best_mask}")
    print(f"best_free_bits={best_bits}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--odd", action="store_true")
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--restarts", type=int, default=10)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--target", type=int)
    args = parser.parse_args()
    search(args.n, args.odd, args.steps, args.restarts, args.seed, args.target)


if __name__ == "__main__":
    main()
