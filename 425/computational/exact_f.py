#!/usr/bin/env python3
"""Deterministic exact experiments for Erdős Problem 425.

For r=2, admissible sets are independent sets in the 4-uniform hypergraph
whose edges are four distinct integers w<x<y<z with w*z=x*y.  The maximum
independent set is the complement of a minimum hitting set, which is solved
by an exact memoized branch-and-bound recursion.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import time
from pathlib import Path


def pair_bucket_edges(n: int) -> tuple[tuple[int, int, int, int], ...]:
    buckets: dict[int, list[tuple[int, int]]] = {}
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            buckets.setdefault(a * b, []).append((a, b))
    out: set[tuple[int, int, int, int]] = set()
    for reps in buckets.values():
        for (a, b), (c, d) in itertools.combinations(reps, 2):
            vertices = (a, b, c, d)
            if len(set(vertices)) == 4:
                out.add(tuple(sorted(vertices)))
    return tuple(sorted(out))


def rectangle_edges(n: int) -> tuple[tuple[int, int, int, int], ...]:
    out: set[tuple[int, int, int, int]] = set()
    for b in range(2, n + 1):
        for a in range(1, b):
            if math.gcd(a, b) != 1:
                continue
            for h in range(1, n // b + 1):
                # bg < ah is exactly the middle-order condition.
                gmax = min(h - 1, (a * h - 1) // b)
                for g in range(1, gmax + 1):
                    edge = (a * g, b * g, a * h, b * h)
                    assert edge[0] < edge[1] < edge[2] < edge[3] <= n
                    assert edge[0] * edge[3] == edge[1] * edge[2]
                    out.add(edge)
    return tuple(sorted(out))


def edge_masks(edges: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(sum(1 << (v - 1) for v in edge) for edge in edges)


def independent(mask: int, masks: tuple[int, ...]) -> bool:
    return all(mask & edge != edge for edge in masks)


class ExactHittingSet:
    def __init__(self, n: int, masks: tuple[int, ...]) -> None:
        self.n = n
        self.masks = masks
        self.incidence = [0] * n
        for eid, edge in enumerate(masks):
            bit = 1 << eid
            for v in bits(edge):
                self.incidence[v] |= bit
        self.memo: dict[int, tuple[int, tuple[int, ...]]] = {}
        self.nodes = 0

    def disjoint_lower_bound(self, uncovered: int) -> int:
        used_vertices = 0
        count = 0
        u = uncovered
        while u:
            lsb = u & -u
            eid = lsb.bit_length() - 1
            edge = self.masks[eid]
            if not edge & used_vertices:
                used_vertices |= edge
                count += 1
            u ^= lsb
        return count

    def greedy_cover(self, uncovered: int) -> tuple[int, ...]:
        chosen: list[int] = []
        u = uncovered
        while u:
            best_v = max(
                range(self.n),
                key=lambda v: ((u & self.incidence[v]).bit_count(), -v),
            )
            assert u & self.incidence[best_v]
            chosen.append(best_v)
            u &= ~self.incidence[best_v]
        return tuple(chosen)

    def branch_edge(self, uncovered: int) -> int:
        best_eid = -1
        best_score = -1
        u = uncovered
        while u:
            lsb = u & -u
            eid = lsb.bit_length() - 1
            score = sum(
                (uncovered & self.incidence[v]).bit_count()
                for v in bits(self.masks[eid])
            )
            if score > best_score:
                best_score = score
                best_eid = eid
            u ^= lsb
        return best_eid

    def solve_state(self, uncovered: int) -> tuple[int, tuple[int, ...]]:
        if not uncovered:
            return 0, ()
        cached = self.memo.get(uncovered)
        if cached is not None:
            return cached
        self.nodes += 1

        greedy = self.greedy_cover(uncovered)
        best_k = len(greedy)
        best_vertices = greedy

        eid = self.branch_edge(uncovered)
        branch_vertices = sorted(
            bits(self.masks[eid]),
            key=lambda v: (-(uncovered & self.incidence[v]).bit_count(), v),
        )
        for v in branch_vertices:
            child = uncovered & ~self.incidence[v]
            if 1 + self.disjoint_lower_bound(child) >= best_k:
                continue
            child_k, child_vertices = self.solve_state(child)
            if 1 + child_k < best_k:
                best_k = 1 + child_k
                best_vertices = (v,) + child_vertices

        result = best_k, best_vertices
        self.memo[uncovered] = result
        return result

    def solve(self) -> tuple[int, tuple[int, ...]]:
        return self.solve_state((1 << len(self.masks)) - 1)


def bits(mask: int):
    while mask:
        lsb = mask & -mask
        yield lsb.bit_length() - 1
        mask ^= lsb


def exact_f(n: int) -> dict[str, object]:
    edges = pair_bucket_edges(n)
    masks = edge_masks(edges)
    solver = ExactHittingSet(n, masks)
    start = time.perf_counter()
    tau, deleted0 = solver.solve()
    seconds = time.perf_counter() - start
    deleted = tuple(sorted(v + 1 for v in deleted0))
    deleted_set = set(deleted)
    witness = tuple(v for v in range(1, n + 1) if v not in deleted_set)
    witness_mask = sum(1 << (v - 1) for v in witness)
    assert independent(witness_mask, masks)
    assert len(witness) == n - tau
    return {
        "n": n,
        "F": n - tau,
        "witness": witness,
        "deleted": deleted,
        "edge_count": len(edges),
        "edge_sha256": digest_edges(edges),
        "search_nodes": solver.nodes,
        "seconds": seconds,
    }


def digest_edges(edges: tuple[tuple[int, ...], ...]) -> str:
    payload = "".join(",".join(map(str, edge)) + "\n" for edge in edges)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def valid_products(subset: tuple[int, ...], r: int) -> bool:
    seen: set[int] = set()
    for choice in itertools.combinations(subset, r):
        product = math.prod(choice)
        if product in seen:
            return False
        seen.add(product)
    return True


def brute_f(n: int, r: int = 2) -> tuple[int, tuple[int, ...]]:
    best: tuple[int, ...] = ()
    for size in range(n, -1, -1):
        for subset in itertools.combinations(range(1, n + 1), size):
            if valid_products(subset, r):
                return size, subset
    return 0, best


def self_test(edge_max: int, brute_n: int, fixed_n: int) -> None:
    start = time.perf_counter()
    for n in range(1, edge_max + 1):
        a = pair_bucket_edges(n)
        b = rectangle_edges(n)
        assert a == b, (n, set(a) ^ set(b))
    expected = [1, 2, 3, 4, 5, 5, 6, 6, 7]
    for n, value in enumerate(expected, 1):
        got = exact_f(n)["F"]
        assert got == value, (n, got, value)
    for n in range(1, brute_n + 1):
        exact = exact_f(n)
        brute, witness = brute_f(n, 2)
        assert exact["F"] == brute, (n, exact, brute, witness)
    for r in range(2, 5):
        for n in range(1, fixed_n + 1):
            value, witness = brute_f(n, r)
            assert len(witness) == value and valid_products(witness, r)
    elapsed = time.perf_counter() - start
    print(json.dumps({
        "status": "ok",
        "edge_generator_max": edge_max,
        "pair_bruteforce_max": brute_n,
        "fixed_r_max": 4,
        "fixed_n_max": fixed_n,
        "seconds": elapsed,
    }, sort_keys=True))


def table(n_max: int, output: Path | None) -> None:
    start = time.perf_counter()
    entries = []
    for n in range(1, n_max + 1):
        row = exact_f(n)
        entries.append(row)
        print(
            f"n={n:3d} F={row['F']:3d} edges={row['edge_count']:6d} "
            f"nodes={row['search_nodes']:8d} sec={row['seconds']:.4f}",
            flush=True,
        )
    payload = {
        "schema": "erdos-425-exact-v1",
        "semantics": "unordered_distinct",
        "algorithm": "exact minimum hitting set on collision hypergraph",
        "n_max": n_max,
        "total_seconds": time.perf_counter() - start,
        "entries": entries,
    }
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(f"wrote {output}")


def verify(
    path: Path,
    max_n: int | None = None,
    witness_only: bool = False,
) -> None:
    payload = json.loads(path.read_text())
    assert payload["schema"] == "erdos-425-exact-v1"
    checked = 0
    for row in payload["entries"]:
        n = row["n"]
        if max_n is not None and n > max_n:
            continue
        edges = pair_bucket_edges(n)
        assert digest_edges(edges) == row["edge_sha256"]
        witness = tuple(row["witness"])
        assert len(witness) == row["F"]
        assert valid_products(witness, 2)
        if not witness_only:
            rerun = exact_f(n)
            assert rerun["F"] == row["F"]
        checked += 1
    print(json.dumps({
        "status": "verified",
        "path": str(path),
        "entries_checked": checked,
        "optimization_rerun": not witness_only,
    }, sort_keys=True))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    test = sub.add_parser("self-test")
    test.add_argument("--edge-max", type=int, default=80)
    test.add_argument("--brute-n", type=int, default=16)
    test.add_argument("--fixed-n", type=int, default=11)

    tab = sub.add_parser("table")
    tab.add_argument("--n-max", type=int, default=35)
    tab.add_argument("--output", type=Path)

    ver = sub.add_parser("verify")
    ver.add_argument("path", type=Path)
    ver.add_argument("--max-n", type=int)
    ver.add_argument("--witness-only", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "self-test":
        self_test(args.edge_max, args.brute_n, args.fixed_n)
    elif args.command == "table":
        table(args.n_max, args.output)
    elif args.command == "verify":
        verify(args.path, args.max_n, args.witness_only)
    else:
        raise AssertionError(args.command)


if __name__ == "__main__":
    main()
