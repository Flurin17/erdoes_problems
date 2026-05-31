#!/usr/bin/env python3
"""Small checks for regular induced subgraphs.

The exhaustive mode enumerates labelled graphs, so it is intended only for
small n.  It is useful for checking proposed lemmas against all graphs up to
six vertices and, with patience, seven vertices.
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Precomp:
    n: int
    edges: list[tuple[int, int]]
    vertices: list[list[int]]
    incident: list[list[int]]
    subsets_by_size_desc: list[int]


def precompute(n: int) -> Precomp:
    edges = list(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    vertices = [[] for _ in range(1 << n)]
    incident = [[0] * n for _ in range(1 << n)]

    for subset in range(1, 1 << n):
        vs = [v for v in range(n) if (subset >> v) & 1]
        vertices[subset] = vs
        for v in vs:
            mask = 0
            for w in vs:
                if v == w:
                    continue
                a, b = sorted((v, w))
                mask |= 1 << edge_index[(a, b)]
            incident[subset][v] = mask

    subsets_by_size_desc = sorted(
        range(1, 1 << n), key=lambda s: (len(vertices[s]), s), reverse=True
    )
    return Precomp(n, edges, vertices, incident, subsets_by_size_desc)


def is_regular_on(graph_mask: int, subset: int, pc: Precomp) -> bool:
    vs = pc.vertices[subset]
    first = (graph_mask & pc.incident[subset][vs[0]]).bit_count()
    return all((graph_mask & pc.incident[subset][v]).bit_count() == first for v in vs[1:])


def is_modular_on(graph_mask: int, subset: int, modulus: int, pc: Precomp) -> bool:
    vs = pc.vertices[subset]
    first = (graph_mask & pc.incident[subset][vs[0]]).bit_count() % modulus
    return all(
        (graph_mask & pc.incident[subset][v]).bit_count() % modulus == first
        for v in vs[1:]
    )


def max_regular_order(graph_mask: int, pc: Precomp) -> int:
    for subset in pc.subsets_by_size_desc:
        if is_regular_on(graph_mask, subset, pc):
            return len(pc.vertices[subset])
    return 0


def has_regular_order_at_least(graph_mask: int, threshold: int, pc: Precomp) -> bool:
    for subset in pc.subsets_by_size_desc:
        if len(pc.vertices[subset]) < threshold:
            return False
        if is_regular_on(graph_mask, subset, pc):
            return True
    return False


def max_modular_order(graph_mask: int, modulus: int, pc: Precomp) -> int:
    for subset in pc.subsets_by_size_desc:
        if is_modular_on(graph_mask, subset, modulus, pc):
            return len(pc.vertices[subset])
    return 0


def has_modular_order_at_least(
    graph_mask: int, modulus: int, threshold: int, pc: Precomp
) -> bool:
    for subset in pc.subsets_by_size_desc:
        if len(pc.vertices[subset]) < threshold:
            return False
        if is_modular_on(graph_mask, subset, modulus, pc):
            return True
    return False


def exhaustive(n: int, modulus: int | None, require_full_modulus: int | None) -> None:
    pc = precompute(n)
    total = 1 << len(pc.edges)
    full = (1 << n) - 1
    best = n
    histogram: dict[int, int] = {}
    witnesses: list[int] = []
    checked = 0

    for graph_mask in range(total):
        if require_full_modulus is not None and not is_modular_on(
            graph_mask, full, require_full_modulus, pc
        ):
            continue
        checked += 1
        value = (
            max_modular_order(graph_mask, modulus, pc)
            if modulus is not None
            else max_regular_order(graph_mask, pc)
        )
        histogram[value] = histogram.get(value, 0) + 1
        if value < best:
            best = value
            witnesses = [graph_mask]
        elif value == best and len(witnesses) < 5:
            witnesses.append(graph_mask)

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    if require_full_modulus is not None:
        print(f"checked_full_{require_full_modulus}_modular_graphs={checked}")
    if modulus is None:
        print(f"F(n)={best}")
        print("histogram=max_regular_order:count")
    else:
        print(f"minimum_max_{modulus}_modular_order={best}")
        print(f"histogram=max_{modulus}_modular_order:count")
    for key in sorted(histogram):
        print(f"  {key}: {histogram[key]}")
    print("sample_extremal_graph_masks=" + ",".join(map(str, witnesses)))


def sample(
    n: int, trials: int, seed: int, modulus: int | None, require_full_modulus: int | None
) -> None:
    rng = random.Random(seed)
    pc = precompute(n)
    m = len(pc.edges)
    best = n
    best_mask = 0
    histogram: dict[int, int] = {}

    attempts = 0
    while sum(histogram.values()) < trials:
        attempts += 1
        graph_mask = rng.getrandbits(m)
        if require_full_modulus is not None and not is_modular_on(
            graph_mask, (1 << n) - 1, require_full_modulus, pc
        ):
            continue
        value = (
            max_modular_order(graph_mask, modulus, pc)
            if modulus is not None
            else max_regular_order(graph_mask, pc)
        )
        histogram[value] = histogram.get(value, 0) + 1
        if value < best:
            best = value
            best_mask = graph_mask

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    if modulus is not None:
        print(f"modulus={modulus}")
    if require_full_modulus is not None:
        print(f"required_full_modulus={require_full_modulus}")
    print(f"minimum_seen={best}")
    print(f"sample_witness_mask={best_mask}")
    if modulus is None:
        print("histogram=max_regular_order:count")
    else:
        print(f"histogram=max_{modulus}_modular_order:count")
    for key in sorted(histogram):
        print(f"  {key}: {histogram[key]}")


def fixed_mask(n: int, graph_mask: int, modulus: int | None) -> None:
    pc = precompute(n)
    full = (1 << n) - 1
    degrees = [
        (graph_mask & pc.incident[full][vertex]).bit_count()
        for vertex in range(n)
    ]
    print(f"n={n}")
    print(f"mask={graph_mask}")
    print("degree_sequence=" + ",".join(map(str, sorted(degrees))))
    print(f"max_regular_order={max_regular_order(graph_mask, pc)}")
    if modulus is not None:
        print(f"modulus={modulus}")
        print(f"max_{modulus}_modular_order={max_modular_order(graph_mask, modulus, pc)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--modulus", type=int)
    parser.add_argument("--require-full-modulus", type=int)
    args = parser.parse_args()

    if args.mask is not None:
        fixed_mask(args.n, args.mask, args.modulus)
    elif args.sample:
        sample(args.n, args.sample, args.seed, args.modulus, args.require_full_modulus)
    else:
        exhaustive(args.n, args.modulus, args.require_full_modulus)


if __name__ == "__main__":
    main()
