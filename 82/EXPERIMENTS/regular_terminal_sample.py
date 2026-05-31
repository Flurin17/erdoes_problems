#!/usr/bin/env python3
"""Sample regular graphs for exact terminal regular induced subgraphs.

This tests the regular-graph hard core of the dyadic terminal-window route:
does a regular graph on q^2 vertices contain a regular induced subgraph on
exactly 2q vertices?  The generator starts from a circulant regular graph and
applies degree-preserving switches.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations

from weighted_blowup import circulant_edges, switched_edges


def has_regular_exact(
    n: int,
    edges: list[tuple[int, int]],
    target: int,
) -> tuple[bool, tuple[int, ...] | None, int | None]:
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    for vertices in combinations(range(n), target):
        mask = 0
        for vertex in vertices:
            mask |= 1 << vertex
        degree = (adj[vertices[0]] & mask).bit_count()
        if all((adj[vertex] & mask).bit_count() == degree for vertex in vertices[1:]):
            return True, vertices, degree
    return False, None, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--degree", type=int)
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--switches", type=int)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()

    n = args.q * args.q
    target = 2 * args.q
    degree = args.degree if args.degree is not None else n // 2
    if degree % 2 and n % 2:
        degree -= 1
    switches = args.switches if args.switches is not None else 30 * n
    rng = random.Random(args.seed)

    failures = 0
    for trial in range(args.trials):
        edges = circulant_edges(n, degree)
        if edges is None:
            raise SystemExit("could not generate circulant base")
        edges = switched_edges(n, edges, switches, rng)
        ok, vertices, regular_degree = has_regular_exact(n, edges, target)
        if not ok:
            failures += 1
            print(f"failure_trial={trial}")
            break
        if trial == 0:
            print("first_witness=" + ",".join(map(str, vertices)))
            print(f"first_witness_degree={regular_degree}")

    print(f"q={args.q}")
    print(f"n={n}")
    print(f"target={target}")
    print(f"degree={degree}")
    print(f"trials={args.trials}")
    print(f"switches={switches}")
    print(f"failures={failures}")


if __name__ == "__main__":
    main()
