#!/usr/bin/env python3
"""Search the spectrum-mass parameter mu(G)=sum_d s_d(G)."""

from __future__ import annotations

import argparse
import random
from collections import Counter
from itertools import combinations
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


def is_connected(adj: list[int]) -> bool:
    n = len(adj)
    if n <= 1:
        return True
    seen = 1
    stack = [0]
    while stack:
        v = stack.pop()
        unseen_neighbors = adj[v] & ~seen
        while unseen_neighbors:
            bit = unseen_neighbors & -unseen_neighbors
            w = bit.bit_length() - 1
            seen |= bit
            stack.append(w)
            unseen_neighbors ^= bit
    return seen == (1 << n) - 1


def min_degree_at_least(adj: list[int], threshold: int) -> bool:
    return all(row.bit_count() >= threshold for row in adj)


def connected_after_deleting(adj: list[int], deleted: tuple[int, ...]) -> bool:
    n = len(adj)
    deleted_mask = 0
    for v in deleted:
        deleted_mask |= 1 << v
    remaining = ((1 << n) - 1) & ~deleted_mask
    if remaining == 0 or remaining & (remaining - 1) == 0:
        return True
    start_bit = remaining & -remaining
    seen = start_bit
    stack = [start_bit.bit_length() - 1]
    while stack:
        v = stack.pop()
        unseen_neighbors = adj[v] & remaining & ~seen
        while unseen_neighbors:
            bit = unseen_neighbors & -unseen_neighbors
            w = bit.bit_length() - 1
            seen |= bit
            stack.append(w)
            unseen_neighbors ^= bit
    return seen == remaining


def vertex_connectivity_at_least(adj: list[int], threshold: int) -> bool:
    if threshold <= 1:
        return is_connected(adj)
    n = len(adj)
    if n <= threshold:
        return False
    if min(row.bit_count() for row in adj) < threshold:
        return False
    for size in range(threshold):
        for deleted in combinations(range(n), size):
            if not connected_after_deleting(adj, deleted):
                return False
    return True


def passes_filters(
    adj: list[int],
    connected_only: bool,
    min_degree: int,
    vertex_connectivity: int,
) -> bool:
    if connected_only and not is_connected(adj):
        return False
    if min_degree and not min_degree_at_least(adj, min_degree):
        return False
    if vertex_connectivity and not vertex_connectivity_at_least(
        adj, vertex_connectivity
    ):
        return False
    return True


def exact(
    n: int,
    progress: int,
    connected_only: bool,
    min_degree: int,
    vertex_connectivity: int,
) -> None:
    pc = cdc.precompute(n)
    total = 1 << len(pc.edges)
    histogram: Counter[int] = Counter()
    best = n * n
    best_examples: list[tuple[int, dict[int, int]]] = []
    checked = 0
    start = monotonic()

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        if not passes_filters(adj, connected_only, min_degree, vertex_connectivity):
            continue
        checked += 1
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
    print(f"connected_only={connected_only}")
    print(f"min_degree_filter={min_degree}")
    print(f"vertex_connectivity_filter={vertex_connectivity}")
    print(f"checked_graphs={checked}")
    print(f"min_spectrum_mass={best}")
    print(f"violates_mu_ge_n={best < n}")
    print(f"histogram={dict(sorted(histogram.items()))}")
    for mask, by_degree in best_examples:
        print(f"example mask={mask} by_degree={by_degree}")


def sample(
    n: int,
    trials: int,
    seed: int,
    connected_only: bool,
    min_degree: int,
    vertex_connectivity: int,
) -> None:
    rng = random.Random(seed)
    pc = cdc.precompute(n)
    bits = len(pc.edges)
    histogram: Counter[int] = Counter()
    best = n * n
    best_example: tuple[int, dict[int, int]] | None = None
    attempts = 0

    while sum(histogram.values()) < trials:
        attempts += 1
        mask = rng.getrandbits(bits)
        adj = cdc.adjacency(n, mask, pc)
        if not passes_filters(adj, connected_only, min_degree, vertex_connectivity):
            continue
        mass, by_degree = spectrum_mass(adj, pc)
        histogram[mass] += 1
        if mass < best:
            best = mass
            best_example = (mask, by_degree)

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"connected_only={connected_only}")
    print(f"min_degree_filter={min_degree}")
    print(f"vertex_connectivity_filter={vertex_connectivity}")
    print(f"min_seen={best}")
    print(f"violates_mu_ge_n={best < n}")
    print(f"histogram={dict(sorted(histogram.items()))}")
    if best_example is not None:
        mask, by_degree = best_example
        print(f"best_example mask={mask} by_degree={by_degree}")


def local_search(
    n: int,
    steps: int,
    restarts: int,
    seed: int,
    connected_only: bool,
    start_mask: int | None,
    min_degree: int,
    vertex_connectivity: int,
) -> None:
    rng = random.Random(seed)
    pc = cdc.precompute(n)
    bits = len(pc.edges)
    global_best = n * n
    global_example: tuple[int, dict[int, int]] | None = None

    for restart in range(restarts):
        if restart == 0 and start_mask is not None:
            mask = start_mask
        else:
            mask = rng.getrandbits(bits)
        adj = cdc.adjacency(n, mask, pc)
        if connected_only or min_degree or vertex_connectivity:
            attempts = 0
            while not passes_filters(
                adj, connected_only, min_degree, vertex_connectivity
            ):
                if restart == 0 and start_mask is not None:
                    raise ValueError("start mask does not satisfy filters")
                attempts += 1
                if attempts > 10_000:
                    raise RuntimeError("failed to sample a connected starting graph")
                mask = rng.getrandbits(bits)
                adj = cdc.adjacency(n, mask, pc)
        value, by_degree = spectrum_mass(adj, pc)
        if value < global_best:
            global_best = value
            global_example = (mask, by_degree)
            print(
                f"new_best restart={restart} step=start "
                f"mass={value} mask={mask} by_degree={by_degree}",
                flush=True,
            )
        temperature = 0.02
        for step in range(steps):
            bit = rng.randrange(bits)
            candidate = mask ^ (1 << bit)
            candidate_adj = cdc.adjacency(n, candidate, pc)
            if not passes_filters(
                candidate_adj, connected_only, min_degree, vertex_connectivity
            ):
                continue
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
    print(f"connected_only={connected_only}")
    print(f"min_degree_filter={min_degree}")
    print(f"vertex_connectivity_filter={vertex_connectivity}")
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
    print(f"connected={is_connected(adj)}")
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
    parser.add_argument("--connected-only", action="store_true")
    parser.add_argument("--min-degree", type=int, default=0)
    parser.add_argument("--vertex-connectivity", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--progress", type=int, default=0)
    parser.add_argument("--start-mask", type=int)
    args = parser.parse_args()

    if args.mask is not None:
        fixed(args.n, args.mask)
    elif args.local_steps:
        local_search(
            args.n,
            args.local_steps,
            args.restarts,
            args.seed,
            args.connected_only,
            args.start_mask,
            args.min_degree,
            args.vertex_connectivity,
        )
    elif args.sample:
        sample(
            args.n,
            args.sample,
            args.seed,
            args.connected_only,
            args.min_degree,
            args.vertex_connectivity,
        )
    else:
        exact(
            args.n,
            args.progress,
            args.connected_only,
            args.min_degree,
            args.vertex_connectivity,
        )


if __name__ == "__main__":
    main()
