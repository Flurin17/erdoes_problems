#!/usr/bin/env python3
"""Brute-force automorphism orbit diagnostics for small fixed graph masks."""

from __future__ import annotations

import argparse

import regular_bitset


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.parent[rb] = ra


def degree_sequence(adj: list[int], n: int) -> list[int]:
    full = (1 << n) - 1
    return [(adj[v] & full).bit_count() for v in range(n)]


def can_map(adj: list[int], degrees: list[int], source: int, target: int) -> bool:
    n = len(adj)
    if degrees[source] != degrees[target]:
        return False

    image = [-1] * n
    preimage = [-1] * n
    image[source] = target
    preimage[target] = source

    def compatible(v: int, w: int) -> bool:
        if degrees[v] != degrees[w] or preimage[w] != -1:
            return False
        for u, mapped in enumerate(image):
            if mapped == -1:
                continue
            if ((adj[v] >> u) & 1) != ((adj[w] >> mapped) & 1):
                return False
        return True

    def search() -> bool:
        next_vertex = -1
        next_candidates: list[int] | None = None
        for v in range(n):
            if image[v] != -1:
                continue
            candidates = [w for w in range(n) if compatible(v, w)]
            if not candidates:
                return False
            if next_candidates is None or len(candidates) < len(next_candidates):
                next_vertex = v
                next_candidates = candidates
        if next_candidates is None:
            return True

        v = next_vertex
        for w in next_candidates:
            image[v] = w
            preimage[w] = v
            if search():
                return True
            image[v] = -1
            preimage[w] = -1
        return False

    return search()


def automorphism_orbits(adj: list[int]) -> list[list[int]]:
    n = len(adj)
    degrees = degree_sequence(adj, n)
    dsu = DSU(n)
    for source in range(n):
        for target in range(source + 1, n):
            if can_map(adj, degrees, source, target):
                dsu.union(source, target)
    groups: dict[int, list[int]] = {}
    for vertex in range(n):
        groups.setdefault(dsu.find(vertex), []).append(vertex)
    return sorted(groups.values(), key=lambda group: (len(group), group), reverse=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    args = parser.parse_args()

    adj = regular_bitset.build_adjacency(args.n, args.mask)
    orbits = automorphism_orbits(adj)
    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"orbit_count={len(orbits)}")
    print(f"max_orbit_size={max(len(orbit) for orbit in orbits)}")
    for orbit in orbits:
        print("orbit size={} vertices={}".format(len(orbit), ",".join(map(str, orbit))))


if __name__ == "__main__":
    main()
