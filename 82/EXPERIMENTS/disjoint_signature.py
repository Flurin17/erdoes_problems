#!/usr/bin/env python3
"""Residue-signature compatibility for disjoint unions.

If graphs are disjointly unioned, a global target-modular color can combine
local color classes only when their target residues agree.  This script
computes all residue signatures of bounded modular partitions of small
components and searches for components whose signatures cannot share one set
of global residue slots.
"""

from __future__ import annotations

import argparse
import random
from functools import lru_cache
from itertools import combinations_with_replacement

import modular_partition
import regular_induced as ri


def add_residue(signature: tuple[int, ...], residue: int) -> tuple[int, ...]:
    return tuple(sorted(signature + (residue,)))


def residue_signatures(
    n: int,
    graph_mask: int,
    modulus: int,
    colors: int,
) -> set[tuple[int, ...]]:
    pc = ri.precompute(n)
    full = (1 << n) - 1
    residues: dict[int, int] = {}
    for subset in range(1, 1 << n):
        residue = modular_partition.residue_on(graph_mask, subset, modulus, pc)
        if residue is not None:
            residues[subset] = residue

    @lru_cache(maxsize=None)
    def rec(remaining: int, left: int) -> frozenset[tuple[int, ...]]:
        if remaining == 0:
            return frozenset({()})
        if left == 0:
            return frozenset()
        pivot = remaining & -remaining
        signatures: set[tuple[int, ...]] = set()
        sub = remaining
        while sub:
            if sub & pivot and sub in residues:
                for tail in rec(remaining ^ sub, left - 1):
                    signatures.add(add_residue(tail, residues[sub]))
            sub = (sub - 1) & remaining
        return frozenset(signatures)

    return set(rec(full, colors))


def is_submultiset(needles: tuple[int, ...], haystack: tuple[int, ...]) -> bool:
    i = 0
    for value in haystack:
        if i < len(needles) and needles[i] == value:
            i += 1
    return i == len(needles)


def compatible_slots(
    signatures: set[tuple[int, ...]],
    modulus: int,
    colors: int,
) -> set[tuple[int, ...]]:
    slots: set[tuple[int, ...]] = set()
    for size in range(1, colors + 1):
        for candidate in combinations_with_replacement(range(modulus), size):
            if any(is_submultiset(signature, candidate) for signature in signatures):
                slots.add(candidate)
    return slots


def random_source_modular_masks(
    n: int,
    source_modulus: int,
    count: int,
    seed: int,
) -> list[int]:
    rng = random.Random(seed)
    pc = ri.precompute(n)
    edge_index = {edge: i for i, edge in enumerate(pc.edges)}
    full = (1 << n) - 1
    masks: list[int] = []
    attempts = 0
    while len(masks) < count:
        attempts += 1
        if source_modulus == 2:
            graph_mask = modular_partition.random_parity_mask(n, False, rng, pc, edge_index)
            if graph_mask is None:
                continue
        else:
            graph_mask = rng.getrandbits(len(pc.edges))
            if not ri.is_modular_on(graph_mask, full, source_modulus, pc):
                continue
        masks.append(graph_mask)
    print(f"generated_masks={len(masks)}")
    print(f"generation_attempts={attempts}")
    return masks


def search(
    n: int,
    source_modulus: int,
    target_modulus: int,
    colors: int,
    samples: int,
    seed: int,
    masks: list[int],
) -> None:
    if not masks:
        masks = random_source_modular_masks(n, source_modulus, samples, seed)

    data: list[tuple[int, set[tuple[int, ...]], set[tuple[int, ...]]]] = []
    for index, graph_mask in enumerate(masks):
        signatures = residue_signatures(n, graph_mask, target_modulus, colors)
        slots = compatible_slots(signatures, target_modulus, colors)
        data.append((graph_mask, signatures, slots))
        print(
            f"component={index} mask={graph_mask} "
            f"signatures={len(signatures)} compatible_slots={len(slots)}"
        )

    best_pair: tuple[int, int, int] | None = None
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            common = data[i][2] & data[j][2]
            score = len(common)
            if best_pair is None or score < best_pair[0]:
                best_pair = (score, i, j)
            if not common:
                print("pair_obstruction=yes")
                print(f"pair={i},{j}")
                print(f"masks={data[i][0]},{data[j][0]}")
                return

    print("pair_obstruction=no")
    if best_pair is not None:
        score, i, j = best_pair
        print(f"best_pair_common_slots={score}")
        print(f"best_pair={i},{j}")
        print(f"best_pair_masks={data[i][0]},{data[j][0]}")

    best_triple: tuple[int, int, int, int] | None = None
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            common_ij = data[i][2] & data[j][2]
            for k in range(j + 1, len(data)):
                common = common_ij & data[k][2]
                score = len(common)
                if best_triple is None or score < best_triple[0]:
                    best_triple = (score, i, j, k)
                if not common:
                    print("triple_obstruction=yes")
                    print(f"triple={i},{j},{k}")
                    print(f"masks={data[i][0]},{data[j][0]},{data[k][0]}")
                    return
    print("triple_obstruction=no")
    if best_triple is not None:
        score, i, j, k = best_triple
        print(f"best_triple_common_slots={score}")
        print(f"best_triple={i},{j},{k}")
        print(f"best_triple_masks={data[i][0]},{data[j][0]},{data[k][0]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--source-modulus", type=int, default=2)
    parser.add_argument("--target-modulus", type=int, default=4)
    parser.add_argument("--colors", type=int, default=4)
    parser.add_argument("--samples", type=int, default=20)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--masks", type=str, default="")
    args = parser.parse_args()
    masks = [int(item) for item in args.masks.split(",") if item]
    search(
        args.n,
        args.source_modulus,
        args.target_modulus,
        args.colors,
        args.samples,
        args.seed,
        masks,
    )


if __name__ == "__main__":
    main()
