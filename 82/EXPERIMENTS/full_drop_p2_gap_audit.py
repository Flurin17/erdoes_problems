#!/usr/bin/env python3
"""Audit the remaining gap in the P=2 full-drop alpha+omega conjecture."""

from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations
from time import monotonic

import column_drop_census as cdc
import full_drop_census as fdc


def target(n: int) -> int:
    return (n + 4) // 2


def clique_independent_on_subset(
    adj: list[int], pc: cdc.Precomp, subset_mask: int
) -> tuple[int, int]:
    clique = 0
    independent = 0
    for size, entries in pc.subsets_by_size:
        if size <= clique and size <= independent:
            break
        for subset, vertices in entries:
            if subset & ~subset_mask:
                continue
            degree = (adj[vertices[0]] & subset).bit_count()
            if size > independent and degree == 0 and all(
                (adj[v] & subset).bit_count() == 0 for v in vertices[1:]
            ):
                independent = size
            if size > clique and degree == size - 1 and all(
                (adj[v] & subset).bit_count() == size - 1 for v in vertices[1:]
            ):
                clique = size
            if size <= clique and size <= independent:
                break
    return clique, independent


def first_neighborhood_parts(adj: list[int], a_neighbors: list[int]) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    parts: list[tuple[int, ...]] = []
    for x in a_neighbors:
        if x in seen:
            continue
        part = [x]
        seen.add(x)
        for y in a_neighbors:
            if y in seen:
                continue
            if not ((adj[x] >> y) & 1):
                part.append(y)
                seen.add(y)
                break
        parts.append(tuple(part))
    return parts


def clique_vertices_of_order(adj: list[int], vertices: list[int], order: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for combo in combinations(vertices, order):
        if all((adj[u] >> v) & 1 for u, v in combinations(combo, 2)):
            out.append(combo)
    return out


def audit(n: int, progress: int, max_terminals: int | None) -> None:
    if n < 1:
        raise SystemExit("n must be positive")
    pc = cdc.precompute(n)
    full_mask = (1 << n) - 1
    stats: dict[str, object] = {
        "nodes": 0,
        "terminals": 0,
        "violations": 0,
        "uncovered": 0,
        "max_induction_gap": -10**9,
        "max_induction_gap_example": None,
        "max_actual_gap": -10**9,
        "max_actual_gap_example": None,
        "part_rule_violations": 0,
        "singleton_order_violations": 0,
        "uncovered_buckets": defaultdict(int),
        "gap_buckets": defaultdict(int),
    }
    start = monotonic()

    def dfs(adj: list[int], columns: list[int]) -> bool:
        stats["nodes"] = int(stats["nodes"]) + 1
        k = len(columns)
        if k == n:
            stats["terminals"] = int(stats["terminals"]) + 1
            omega, _omega_vertices, alpha, _alpha_vertices = fdc.max_clique_independent(
                adj, pc
            )
            total = alpha + omega
            if total < target(n):
                stats["violations"] = int(stats["violations"]) + 1
                print(
                    "violation "
                    f"alpha={alpha} omega={omega} target={target(n)} "
                    "columns=" + ",".join(map(str, columns)),
                    flush=True,
                )
                return True

            first_degree = adj[0].bit_count()
            covered = omega <= 3 or first_degree >= 2 * omega - 3
            if not covered:
                stats["uncovered"] = int(stats["uncovered"]) + 1
                uncovered_buckets = stats["uncovered_buckets"]
                assert isinstance(uncovered_buckets, defaultdict)
                uncovered_buckets[(omega, first_degree)] += 1

                b_mask = full_mask & ~1 & ~adj[0]
                b_size = b_mask.bit_count()
                a_vertices = [v for v in range(1, n) if (adj[0] >> v) & 1]
                b_vertices = [v for v in range(1, n) if not ((adj[0] >> v) & 1)]
                omega_b, alpha_b = clique_independent_on_subset(adj, pc, b_mask)
                parts = first_neighborhood_parts(adj, a_vertices)
                max_cliques = clique_vertices_of_order(adj, b_vertices, omega_b)
                for clique in max_cliques:
                    covered_parts = []
                    for part in parts:
                        if all(
                            any(not ((adj[t] >> x) & 1) for t in clique)
                            for x in part
                        ):
                            covered_parts.append(part)
                    size_two_covered = [part for part in covered_parts if len(part) == 2]
                    if size_two_covered and len(covered_parts) > 1:
                        stats["part_rule_violations"] = (
                            int(stats["part_rule_violations"]) + 1
                        )
                        print(
                            "part_rule_violation columns="
                            + ",".join(map(str, columns))
                            + f" clique={clique} covered={covered_parts}",
                            flush=True,
                        )
                        return True
                    singleton_parts = [part for part in covered_parts if len(part) == 1]
                    for (x,), (y,) in combinations(singleton_parts, 2):
                        tx = next(t for t in clique if not ((adj[t] >> x) & 1))
                        ty = next(t for t in clique if not ((adj[t] >> y) & 1))
                        if not (tx < y and ty < x):
                            stats["singleton_order_violations"] = (
                                int(stats["singleton_order_violations"]) + 1
                            )
                            print(
                                "singleton_order_violation columns="
                                + ",".join(map(str, columns))
                                + f" clique={clique} x={x} y={y} tx={tx} ty={ty}",
                                flush=True,
                            )
                            return True
                induction_lower = 1 + target(b_size) + (omega - omega_b)
                gap = target(n) - induction_lower
                gap_buckets = stats["gap_buckets"]
                assert isinstance(gap_buckets, defaultdict)
                gap_buckets[(omega, first_degree, omega_b, gap)] += 1
                if gap > int(stats["max_induction_gap"]):
                    stats["max_induction_gap"] = gap
                    stats["max_induction_gap_example"] = (
                        alpha,
                        omega,
                        first_degree,
                        omega_b,
                        alpha_b,
                        columns[:],
                    )
                actual_gap = target(n) - (1 + alpha_b + omega)
                if actual_gap > int(stats["max_actual_gap"]):
                    stats["max_actual_gap"] = actual_gap
                    stats["max_actual_gap_example"] = (
                        alpha,
                        omega,
                        first_degree,
                        omega_b,
                        alpha_b,
                        columns[:],
                    )

            if progress and int(stats["terminals"]) % progress == 0:
                print(
                    f"progress terminals={stats['terminals']} nodes={stats['nodes']} "
                    f"violations={stats['violations']} uncovered={stats['uncovered']} "
                    f"elapsed={monotonic() - start:.1f}s",
                    flush=True,
                )
            return max_terminals is not None and int(stats["terminals"]) >= max_terminals

        for column in range(1 << k):
            if not fdc.legal_new_column_full(adj, k, column, 2):
                continue
            next_adj = adj[:]
            next_adj.append(column)
            for i in range(k):
                if (column >> i) & 1:
                    next_adj[i] |= 1 << k
            if dfs(next_adj, columns + [column]):
                return True
        return False

    stopped_early = dfs([], [])
    print(f"n={n}")
    print(f"terminals={stats['terminals']}")
    print(f"nodes={stats['nodes']}")
    print(f"stopped_early={stopped_early}")
    print(f"violations={stats['violations']}")
    print(f"uncovered={stats['uncovered']}")
    print(f"max_induction_gap={stats['max_induction_gap']}")
    print(f"max_actual_gap={stats['max_actual_gap']}")
    print(f"part_rule_violations={stats['part_rule_violations']}")
    print(f"singleton_order_violations={stats['singleton_order_violations']}")
    example = stats["max_induction_gap_example"]
    if example is not None:
        alpha, omega, first_degree, omega_b, alpha_b, columns = example
        print(
            "max_induction_gap_example "
            f"alpha={alpha} omega={omega} first_degree={first_degree} "
            f"omega_B={omega_b} alpha_B={alpha_b} columns="
            + ",".join(map(str, columns))
        )
    actual_example = stats["max_actual_gap_example"]
    if actual_example is not None:
        alpha, omega, first_degree, omega_b, alpha_b, columns = actual_example
        print(
            "max_actual_gap_example "
            f"alpha={alpha} omega={omega} first_degree={first_degree} "
            f"omega_B={omega_b} alpha_B={alpha_b} columns="
            + ",".join(map(str, columns))
        )
    uncovered_buckets = stats["uncovered_buckets"]
    assert isinstance(uncovered_buckets, defaultdict)
    for omega, first_degree in sorted(uncovered_buckets):
        print(
            f"uncovered_bucket omega={omega} first_degree={first_degree} "
            f"count={uncovered_buckets[(omega, first_degree)]}"
        )
    gap_buckets = stats["gap_buckets"]
    assert isinstance(gap_buckets, defaultdict)
    for omega, first_degree, omega_b, gap in sorted(gap_buckets):
        if gap >= 0:
            print(
                f"gap_bucket omega={omega} first_degree={first_degree} "
                f"omega_B={omega_b} gap={gap} "
                f"count={gap_buckets[(omega, first_degree, omega_b, gap)]}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--progress", type=int, default=0)
    parser.add_argument("--max-terminals", type=int)
    args = parser.parse_args()
    audit(args.n, args.progress, args.max_terminals)


if __name__ == "__main__":
    main()
