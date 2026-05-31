#!/usr/bin/env python3
"""Weighted terminal witnesses in regular twin blowups.

For a base graph B and cluster cap L, an exact terminal witness of size T in
the independent L-blowup is a vector x with

    0 <= x_i <= L,  sum x_i = T,
    (A_B x)_i is constant over all i with x_i > 0.

This script searches for such vectors in small fixed or random regular bases.
It is a finite model for the terminal dyadic hard core recorded in PROOF.md.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations


def edges_from_mask(n: int, mask: int) -> list[tuple[int, int]]:
    edges = list(combinations(range(n), 2))
    return [edge for index, edge in enumerate(edges) if (mask >> index) & 1]


def adjacency(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


class SearchLimitExceeded(RuntimeError):
    pass


def equal_weight_witness(
    adj: list[list[int]],
    cap: int,
    target: int,
    combination_limit: int | None,
) -> tuple[int, ...] | None:
    n = len(adj)
    adj_sets = [set(row) for row in adj]
    checked = 0
    for size in range(max(1, (target + cap - 1) // cap), min(n, target) + 1):
        if target % size:
            continue
        weight = target // size
        if weight > cap:
            continue
        for support in combinations(range(n), size):
            checked += 1
            if combination_limit is not None and checked > combination_limit:
                raise SearchLimitExceeded
            degrees = [
                sum(1 for other in support if other in adj_sets[vertex])
                for vertex in support
            ]
            if all(degree == degrees[0] for degree in degrees[1:]):
                out = [0] * n
                for vertex in support:
                    out[vertex] = weight
                return tuple(out)
    return None


def random_regular_edges(n: int, degree: int, rng: random.Random, tries: int) -> list[tuple[int, int]] | None:
    if n * degree % 2:
        return None
    for _ in range(tries):
        stubs = [vertex for vertex in range(n) for _ in range(degree)]
        rng.shuffle(stubs)
        edges: set[tuple[int, int]] = set()
        ok = True
        for index in range(0, len(stubs), 2):
            u, v = stubs[index], stubs[index + 1]
            if u == v:
                ok = False
                break
            if u > v:
                u, v = v, u
            if (u, v) in edges:
                ok = False
                break
            edges.add((u, v))
        if ok:
            return sorted(edges)
    return None


def circulant_edges(n: int, degree: int) -> list[tuple[int, int]] | None:
    if degree >= n:
        return None
    if degree % 2 == 1 and n % 2 == 1:
        return None
    edges: set[tuple[int, int]] = set()
    half = degree // 2
    for shift in range(1, half + 1):
        for vertex in range(n):
            other = (vertex + shift) % n
            u, v = sorted((vertex, other))
            edges.add((u, v))
    if degree % 2 == 1:
        shift = n // 2
        for vertex in range(n):
            other = (vertex + shift) % n
            u, v = sorted((vertex, other))
            edges.add((u, v))
    if any(0 <= u < n and 0 <= v < n and u != v for u, v in edges):
        return sorted(edges)
    return None


def switched_edges(
    n: int,
    edges: list[tuple[int, int]],
    switches: int,
    rng: random.Random,
) -> list[tuple[int, int]]:
    edge_set = set(edges)
    edge_list = list(edges)
    for _ in range(switches):
        first = rng.randrange(len(edge_list))
        second = rng.randrange(len(edge_list))
        if first == second:
            continue
        a, b = edge_list[first]
        c, d = edge_list[second]
        if len({a, b, c, d}) < 4:
            continue
        if rng.randrange(2):
            new_edges = tuple(sorted((tuple(sorted((a, c))), tuple(sorted((b, d))))))
        else:
            new_edges = tuple(sorted((tuple(sorted((a, d))), tuple(sorted((b, c))))))
        if new_edges[0] in edge_set or new_edges[1] in edge_set:
            continue
        old_edges = (edge_list[first], edge_list[second])
        edge_set.remove(old_edges[0])
        edge_set.remove(old_edges[1])
        edge_set.add(new_edges[0])
        edge_set.add(new_edges[1])
        edge_list[first] = new_edges[0]
        edge_list[second] = new_edges[1]
    return sorted(edge_set)


def witness(adj: list[list[int]], cap: int, target: int, node_limit: int | None) -> tuple[int, ...] | None:
    n = len(adj)
    quick = equal_weight_witness(adj, cap, target, node_limit)
    if quick is not None:
        return quick

    x = [0] * n
    neighbor_sum = [0] * n
    nodes = 0

    order = sorted(range(n), key=lambda vertex: len(adj[vertex]), reverse=True)

    def rec(position: int, remaining: int, active: list[int]) -> tuple[int, ...] | None:
        nonlocal nodes
        nodes += 1
        if node_limit is not None and nodes > node_limit:
            raise SearchLimitExceeded
        if remaining == 0:
            if not active:
                return None
            value = neighbor_sum[active[0]]
            if all(neighbor_sum[vertex] == value for vertex in active[1:]):
                return tuple(x)
            return None
        if position == n:
            return None
        if remaining > (n - position) * cap:
            return None

        vertex = order[position]
        # Try positive values first; larger weights tend to hit the target with
        # smaller support and stronger pruning.
        upper = min(cap, remaining)
        for value in range(upper, -1, -1):
            x[vertex] = value
            changed = []
            if value:
                active.append(vertex)
                for nbr in adj[vertex]:
                    neighbor_sum[nbr] += value
                    changed.append(nbr)

            # If all currently active vertices already have different fixed
            # neighbor sums and none of their unassigned neighbors remain, this
            # branch cannot recover.  This is intentionally conservative.
            result = rec(position + 1, remaining - value, active)
            if result is not None:
                return result

            if value:
                for nbr in changed:
                    neighbor_sum[nbr] -= value
                active.pop()
            x[vertex] = 0
        return None

    return rec(0, target, [])


def format_edges(edges: list[tuple[int, int]]) -> str:
    return " ".join(f"{u}-{v}" for u, v in edges)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--cap", type=int, required=True)
    parser.add_argument("--target", type=int, required=True)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--random-regular-degree", type=int)
    parser.add_argument("--circulant-degree", type=int)
    parser.add_argument("--switches", type=int, default=0)
    parser.add_argument("--trials", type=int, default=1)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--pairing-tries", type=int, default=1000)
    parser.add_argument("--node-limit", type=int)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    successes = 0
    unknown = 0
    failures = 0

    for trial in range(args.trials):
        if args.mask is not None:
            edges = edges_from_mask(args.n, args.mask)
        elif args.circulant_degree is not None:
            edges = circulant_edges(args.n, args.circulant_degree)
            if edges is None:
                unknown += 1
                continue
            if args.switches:
                edges = switched_edges(args.n, edges, args.switches, rng)
        elif args.random_regular_degree is not None:
            edges = random_regular_edges(
                args.n, args.random_regular_degree, rng, args.pairing_tries
            )
            if edges is None:
                unknown += 1
                continue
        else:
            parser.error("provide --mask, --circulant-degree, or --random-regular-degree")

        adj = adjacency(args.n, edges)
        try:
            found = witness(adj, args.cap, args.target, args.node_limit)
        except SearchLimitExceeded:
            unknown += 1
            continue
        if found is None:
            failures += 1
            print(f"failure_trial={trial}")
            print("edges=" + format_edges(edges))
            if args.mask is not None:
                break
        else:
            successes += 1
            if trial == 0 or args.mask is not None:
                print("witness=" + ",".join(map(str, found)))

    print(f"n={args.n}")
    print(f"cap={args.cap}")
    print(f"target={args.target}")
    print(f"trials={args.trials}")
    print(f"successes={successes}")
    print(f"failures={failures}")
    print(f"unknown={unknown}")


if __name__ == "__main__":
    main()
