#!/usr/bin/env python3
"""Search fixed residue-slot multisets for small source-modular graphs."""

from __future__ import annotations

import argparse
import random
from functools import lru_cache
from itertools import combinations_with_replacement

import modular_partition
import regular_induced as ri


def even_masks(n: int, pc: ri.Precomp) -> list[int]:
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    free_edges = [(i, j) for i in range(n - 1) for j in range(i + 1, n - 1)]
    out: list[int] = []
    for bits in range(1 << len(free_edges)):
        mask = 0
        parities = [0] * n
        for k, (i, j) in enumerate(free_edges):
            if (bits >> k) & 1:
                idx = edge_index[(i, j)]
                mask |= 1 << idx
                parities[i] ^= 1
                parities[j] ^= 1
        for i in range(n - 1):
            if parities[i]:
                idx = edge_index[(i, n - 1)]
                mask |= 1 << idx
                parities[i] ^= 1
                parities[n - 1] ^= 1
        if not parities[n - 1]:
            out.append(mask)
    return out


def has_slot_partition(
    n: int,
    graph_mask: int,
    modulus: int,
    slots: tuple[int, ...],
    pc: ri.Precomp,
) -> bool:
    slots = tuple(sorted(slots))
    by_residue: dict[int, list[int]] = {residue: [] for residue in set(slots)}
    by_residue_pivot: dict[int, list[list[int]]] = {
        residue: [[] for _ in range(n)] for residue in set(slots)
    }
    for subset in range(1, 1 << n):
        residue = modular_partition.residue_on(graph_mask, subset, modulus, pc)
        if residue is not None and residue in by_residue:
            by_residue[residue].append(subset)
            rest = subset
            while rest:
                bit = rest & -rest
                pivot = bit.bit_length() - 1
                by_residue_pivot[residue][pivot].append(subset)
                rest ^= bit
    for residue in by_residue:
        by_residue[residue].sort(key=lambda subset: (subset.bit_count(), subset), reverse=True)
        for pivot in range(n):
            by_residue_pivot[residue][pivot].sort(
                key=lambda subset: (subset.bit_count(), subset),
                reverse=True,
            )

    def remove_slot(state: tuple[int, ...], residue: int) -> tuple[int, ...]:
        state_list = list(state)
        state_list.remove(residue)
        return tuple(state_list)

    @lru_cache(maxsize=None)
    def rec(remaining: int, state: tuple[int, ...]) -> bool:
        if remaining == 0:
            return True
        if not state:
            return False
        pivot = remaining & -remaining
        pivot_index = pivot.bit_length() - 1
        for residue in sorted(set(state)):
            next_state = remove_slot(state, residue)
            for subset in by_residue_pivot[residue][pivot_index]:
                if subset & ~remaining == 0:
                    if rec(remaining ^ subset, next_state):
                        return True
        return False

    return rec((1 << n) - 1, slots)


def search(n: int, modulus: int, candidates: list[tuple[int, ...]]) -> None:
    pc = ri.precompute(n)
    masks = even_masks(n, pc)
    print(f"n={n}")
    print(f"modulus={modulus}")
    print(f"even_graphs={len(masks)}")
    good: list[tuple[int, ...]] = []
    for slots in candidates:
        bad = None
        for graph_mask in masks:
            if not has_slot_partition(n, graph_mask, modulus, slots, pc):
                bad = graph_mask
                break
        print(
            "slots="
            + ",".join(map(str, slots))
            + " "
            + ("ok" if bad is None else f"bad={bad}")
        )
        if bad is None:
            good.append(slots)
    print(f"good_count={len(good)}")
    for slots in good:
        print("good=" + ",".join(map(str, slots)))


def sample(
    n: int,
    modulus: int,
    candidates: list[tuple[int, ...]],
    trials: int,
    seed: int,
    score_all: bool,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    survivors = list(candidates)
    successes = {slots: 0 for slots in candidates}
    failures = {slots: 0 for slots in candidates}
    first_failure: dict[tuple[int, ...], tuple[int, int]] = {}
    checked = 0
    for _ in range(trials):
        graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
        if graph_mask is None:
            continue
        checked += 1
        if score_all:
            for slots in candidates:
                if has_slot_partition(n, graph_mask, modulus, slots, pc):
                    successes[slots] += 1
                else:
                    failures[slots] += 1
                    first_failure.setdefault(slots, (graph_mask, checked))
            continue
        next_survivors: list[tuple[int, ...]] = []
        for slots in survivors:
            if has_slot_partition(n, graph_mask, modulus, slots, pc):
                next_survivors.append(slots)
            else:
                print(
                    "killed="
                    + ",".join(map(str, slots))
                    + f" mask={graph_mask} trial={checked}"
                )
        survivors = next_survivors
        if not survivors:
            break
    print(f"n={n}")
    print(f"modulus={modulus}")
    print(f"sample_even_checked={checked}")
    if score_all:
        print("candidate_scores=slots:successes:failures:first_failure")
        for slots in candidates:
            prefix = ",".join(map(str, slots))
            if slots in first_failure:
                graph_mask, trial = first_failure[slots]
                suffix = f"{graph_mask}@{trial}"
            else:
                suffix = "none"
            print(f"  {prefix}:{successes[slots]}:{failures[slots]}:{suffix}")
        return
    print(f"survivor_count={len(survivors)}")
    for slots in survivors:
        print("survivor=" + ",".join(map(str, slots)))


def sample_source_modular(
    n: int,
    source_modulus: int,
    target_modulus: int,
    candidates: list[tuple[int, ...]],
    trials: int,
    seed: int,
    max_attempts: int,
) -> None:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    edge_count = len(pc.edges)
    full = (1 << n) - 1
    survivors = list(candidates)
    attempts = 0
    checked = 0
    while checked < trials and attempts < max_attempts and survivors:
        attempts += 1
        graph_mask = modular_partition.random_full_modular_candidate(
            n,
            source_modulus,
            edge_count,
            rng,
            pc,
            edge_index,
        )
        if graph_mask is None:
            continue
        if not ri.is_modular_on(graph_mask, full, source_modulus, pc):
            continue
        checked += 1
        next_survivors: list[tuple[int, ...]] = []
        for slots in survivors:
            if has_slot_partition(n, graph_mask, target_modulus, slots, pc):
                next_survivors.append(slots)
            else:
                print(
                    "killed="
                    + ",".join(map(str, slots))
                    + f" mask={graph_mask} trial={checked}"
                )
        survivors = next_survivors
    print(f"n={n}")
    print(f"source_modulus={source_modulus}")
    print(f"target_modulus={target_modulus}")
    print(f"attempts={attempts}")
    print(f"sample_source_modular_checked={checked}")
    print(f"survivor_count={len(survivors)}")
    for slots in survivors:
        print("survivor=" + ",".join(map(str, slots)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--modulus", type=int, default=4)
    parser.add_argument(
        "--slot-count",
        type=int,
        help="number of slots to generate when --candidates is omitted",
    )
    parser.add_argument(
        "--candidates",
        help="semicolon-separated residue multisets, e.g. 0,0,1,2;0,1,2,3",
    )
    parser.add_argument("--sample-even", type=int, default=0)
    parser.add_argument("--sample-source-modular", type=int, default=0)
    parser.add_argument("--source-modulus", type=int)
    parser.add_argument("--max-attempts", type=int, default=1000000)
    parser.add_argument("--score-all", action="store_true")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    if args.candidates:
        candidates = [
            tuple(int(item) % args.modulus for item in block.split(",") if item)
            for block in args.candidates.split(";")
            if block
        ]
    else:
        slot_count = args.slot_count if args.slot_count is not None else args.modulus
        candidates = list(combinations_with_replacement(range(args.modulus), slot_count))
    if args.sample_source_modular:
        if args.source_modulus is None:
            parser.error("--sample-source-modular requires --source-modulus")
        sample_source_modular(
            args.n,
            args.source_modulus,
            args.modulus,
            candidates,
            args.sample_source_modular,
            args.seed,
            args.max_attempts,
        )
        return
    if args.sample_even:
        sample(
            args.n,
            args.modulus,
            candidates,
            args.sample_even,
            args.seed,
            args.score_all,
        )
    else:
        search(args.n, args.modulus, candidates)


if __name__ == "__main__":
    main()
