#!/usr/bin/env python3
"""Sample two-degree q-modular graphs and measure 2q-modular witnesses.

The graph is generated with a prescribed degree sequence using two degree
values `d` and `d+q`, then randomized by degree-preserving double-edge swaps.
This gives a simple dense model for q-modular graphs that are not already
2q-modular.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations

import regular_induced as ri


def havel_hakimi_random(degrees: list[int], rng: random.Random) -> set[tuple[int, int]] | None:
    remaining = list(degrees)
    edges: set[tuple[int, int]] = set()
    while True:
        active = [v for v, degree in enumerate(remaining) if degree > 0]
        if not active:
            return edges
        active.sort(key=lambda v: (remaining[v], rng.random()), reverse=True)
        v = active[0]
        degree = remaining[v]
        candidates = active[1:]
        if degree > len(candidates):
            return None
        candidates.sort(key=lambda u: (remaining[u], rng.random()), reverse=True)
        for u in candidates[:degree]:
            edge = (u, v) if u < v else (v, u)
            if edge in edges:
                return None
            edges.add(edge)
            remaining[u] -= 1
            if remaining[u] < 0:
                return None
        remaining[v] = 0


def randomize_by_swaps(
    edges: set[tuple[int, int]], n: int, swaps: int, rng: random.Random
) -> set[tuple[int, int]]:
    edges = set(edges)
    edge_list = list(edges)
    for _ in range(swaps):
        first, second = rng.sample(edge_list, 2)
        a, b = first
        c, d = second
        if len({a, b, c, d}) < 4:
            continue
        if rng.randrange(2):
            new_edges = [(min(a, c), max(a, c)), (min(b, d), max(b, d))]
        else:
            new_edges = [(min(a, d), max(a, d)), (min(b, c), max(b, c))]
        if (
            new_edges[0][0] == new_edges[0][1]
            or new_edges[1][0] == new_edges[1][1]
            or new_edges[0] == new_edges[1]
            or new_edges[0] in edges
            or new_edges[1] in edges
        ):
            continue
        edges.remove(first)
        edges.remove(second)
        edges.add(new_edges[0])
        edges.add(new_edges[1])
        edge_list.remove(first)
        edge_list.remove(second)
        edge_list.extend(new_edges)
    return edges


def mask_from_edges(edges: set[tuple[int, int]], pc: ri.Precomp) -> int:
    edge_index = {edge: idx for idx, edge in enumerate(pc.edges)}
    mask = 0
    for edge in edges:
        mask |= 1 << edge_index[edge]
    return mask


def mask_from_edges_by_order(edges: set[tuple[int, int]], n: int) -> int:
    edge_index = {edge: idx for idx, edge in enumerate(combinations(range(n), 2))}
    mask = 0
    for edge in edges:
        mask |= 1 << edge_index[edge]
    return mask


def adjacency_from_edges(edges: set[tuple[int, int]], n: int) -> list[int]:
    adjacency = [0] * n
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    return adjacency


def is_connected_adjacency(adjacency: list[int], n: int) -> bool:
    if n <= 1:
        return True
    seen = 1
    stack = [0]
    while stack:
        vertex = stack.pop()
        unseen = adjacency[vertex] & ~seen
        while unseen:
            bit = unseen & -unseen
            seen |= bit
            stack.append(bit.bit_length() - 1)
            unseen ^= bit
    return seen == (1 << n) - 1


def max_modular_order_on_the_fly(adjacency: list[int], n: int, modulus: int) -> int:
    for size in range(n, 0, -1):
        for vertices in combinations(range(n), size):
            subset = 0
            for vertex in vertices:
                subset |= 1 << vertex
            first: int | None = None
            ok = True
            for vertex in vertices:
                residue = (adjacency[vertex] & subset).bit_count() % modulus
                if first is None:
                    first = residue
                elif residue != first:
                    ok = False
                    break
            if ok:
                return size
    return 0


def sample(args: argparse.Namespace) -> None:
    rng = random.Random(args.seed)
    pc = None if args.on_the_fly else ri.precompute(args.n)
    high = args.low_degree + args.q
    degree_sequence = [args.low_degree] * args.low_count + [high] * (args.n - args.low_count)
    if len(degree_sequence) != args.n:
        raise SystemExit("--low-count must be between 0 and n")
    if sum(degree_sequence) % 2:
        raise SystemExit("degree sum is odd")

    accepted = 0
    attempts = 0
    histogram: dict[int, int] = {}
    best_value = args.n + 1
    best_mask = 0
    while accepted < args.trials and attempts < args.max_attempts:
        attempts += 1
        degrees = degree_sequence[:]
        rng.shuffle(degrees)
        edges = havel_hakimi_random(degrees, rng)
        if edges is None:
            continue
        edges = randomize_by_swaps(edges, args.n, args.swaps, rng)
        adjacency = adjacency_from_edges(edges, args.n)
        if args.connected_only and not is_connected_adjacency(adjacency, args.n):
            continue
        accepted += 1
        if args.on_the_fly:
            graph_mask = mask_from_edges_by_order(edges, args.n)
            value = max_modular_order_on_the_fly(adjacency, args.n, 2 * args.q)
        else:
            assert pc is not None
            graph_mask = mask_from_edges(edges, pc)
            value = ri.max_modular_order(graph_mask, 2 * args.q, pc)
        histogram[value] = histogram.get(value, 0) + 1
        if value < best_value:
            best_value = value
            best_mask = graph_mask

    print(f"n={args.n}")
    print(f"q={args.q}")
    print(f"low_degree={args.low_degree}")
    print(f"high_degree={high}")
    print(f"low_count={args.low_count}")
    print(f"trials={args.trials}")
    print(f"attempts={attempts}")
    print(f"accepted={accepted}")
    print(f"swaps={args.swaps}")
    if args.connected_only:
        print("connected_only=True")
    if args.on_the_fly:
        print("on_the_fly=True")
    print(f"best_max_{2 * args.q}_modular_order={best_value if accepted else 'NA'}")
    print(f"best_mask={best_mask}")
    print("histogram=max_target_modular_order:count")
    for value in sorted(histogram):
        print(f"  {value}: {histogram[value]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--low-degree", type=int, required=True)
    parser.add_argument("--low-count", type=int)
    parser.add_argument("--trials", type=int, default=5)
    parser.add_argument("--max-attempts", type=int, default=1000)
    parser.add_argument("--swaps", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--connected-only", action="store_true")
    parser.add_argument(
        "--on-the-fly",
        action="store_true",
        help="avoid the exponential incident-table precompute for larger n",
    )
    args = parser.parse_args()
    if args.low_count is None:
        args.low_count = args.n // 2
    sample(args)


if __name__ == "__main__":
    main()
