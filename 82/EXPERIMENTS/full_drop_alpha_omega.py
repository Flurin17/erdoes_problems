#!/usr/bin/env python3
"""DFS census for alpha+omega in full-drop ordered graphs."""

from __future__ import annotations

import argparse
from time import monotonic

import column_drop_census as cdc
import full_drop_census as fdc


def search(
    n: int,
    p: int,
    progress: int,
    max_terminals: int | None,
) -> None:
    pc = cdc.precompute(n)
    stats: dict[str, object] = {
        "terminals": 0,
        "nodes": 0,
        "best_sum": 2 * n + 1,
        "best_alpha": None,
        "best_omega": None,
        "best_columns": None,
        "best_mask": None,
        "best_by_omega": {},
        "best_by_omega_first_degree": {},
    }
    start = monotonic()

    def dfs(adj: list[int], columns: list[int]) -> bool:
        stats["nodes"] = int(stats["nodes"]) + 1
        k = len(columns)
        if k == n:
            stats["terminals"] = int(stats["terminals"]) + 1
            clique, _clique_vertices, independent, _independent_vertices = (
                fdc.max_clique_independent(adj, pc)
            )
            total = clique + independent
            if total < int(stats["best_sum"]):
                stats["best_sum"] = total
                stats["best_alpha"] = independent
                stats["best_omega"] = clique
                stats["best_columns"] = columns[:]
                stats["best_mask"] = cdc.columns_to_mask(columns, pc)
                print(
                    "new_best "
                    f"terminals={stats['terminals']} alpha={independent} "
                    f"omega={clique} sum={total} columns="
                    + ",".join(map(str, columns)),
                    flush=True,
                )
            best_by_omega = stats["best_by_omega"]
            assert isinstance(best_by_omega, dict)
            previous = best_by_omega.get(clique)
            if previous is None or independent < previous[0]:
                best_by_omega[clique] = (
                    independent,
                    total,
                    columns[:],
                    cdc.columns_to_mask(columns, pc),
                )
            first_degree = adj[0].bit_count() if adj else 0
            best_by_omega_first_degree = stats["best_by_omega_first_degree"]
            assert isinstance(best_by_omega_first_degree, dict)
            key = (clique, first_degree)
            previous_fd = best_by_omega_first_degree.get(key)
            if previous_fd is None or independent < previous_fd[0]:
                best_by_omega_first_degree[key] = (
                    independent,
                    total,
                    columns[:],
                    cdc.columns_to_mask(columns, pc),
                )
            if progress and int(stats["terminals"]) % progress == 0:
                print(
                    f"progress terminals={stats['terminals']} nodes={stats['nodes']} "
                    f"best_sum={stats['best_sum']} elapsed={monotonic() - start:.1f}s",
                    flush=True,
                )
            return max_terminals is not None and int(stats["terminals"]) >= max_terminals

        for column in range(1 << k):
            if not fdc.legal_new_column_full(adj, k, column, p):
                continue
            next_adj = adj[:]
            next_adj.append(column)
            for i in range(k):
                if (column >> i) & 1:
                    next_adj[i] |= 1 << k
            should_stop = dfs(next_adj, columns + [column])
            if should_stop:
                return True
        return False

    stopped_early = dfs([], [])
    print(f"n={n}")
    print(f"P={p}")
    print(f"nodes={stats['nodes']}")
    print(f"terminals={stats['terminals']}")
    print(f"stopped_early={stopped_early}")
    print(f"best_alpha={stats['best_alpha']}")
    print(f"best_omega={stats['best_omega']}")
    print(f"best_sum={stats['best_sum']}")
    print(f"best_mask={stats['best_mask']}")
    print("best_columns=" + ",".join(map(str, stats["best_columns"] or [])))
    best_by_omega = stats["best_by_omega"]
    assert isinstance(best_by_omega, dict)
    for omega in sorted(best_by_omega):
        alpha, total, columns, mask = best_by_omega[omega]
        print(
            f"omega_bucket omega={omega} min_alpha={alpha} "
            f"min_sum={total} mask={mask} columns="
            + ",".join(map(str, columns))
        )
    best_by_omega_first_degree = stats["best_by_omega_first_degree"]
    assert isinstance(best_by_omega_first_degree, dict)
    for omega, first_degree in sorted(best_by_omega_first_degree):
        alpha, total, columns, mask = best_by_omega_first_degree[(omega, first_degree)]
        print(
            f"omega_first_degree_bucket omega={omega} first_degree={first_degree} "
            f"min_alpha={alpha} min_sum={total} mask={mask} columns="
            + ",".join(map(str, columns))
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--p", type=int, default=2)
    parser.add_argument("--progress", type=int, default=0)
    parser.add_argument("--max-terminals", type=int)
    args = parser.parse_args()
    if args.n < 1:
        raise SystemExit("n must be positive")
    if args.p < 1:
        raise SystemExit("--p must be positive")
    search(args.n, args.p, args.progress, args.max_terminals)


if __name__ == "__main__":
    main()
