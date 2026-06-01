#!/usr/bin/env python3
"""Exact DFS minimum of the largest regular induced subgraph in full-drop graphs."""

from __future__ import annotations

import argparse
from time import monotonic

import column_drop_census as cdc
import full_drop_census as fdc


def search(n: int, p: int, progress: int, max_terminals: int | None) -> None:
    pc = cdc.precompute(n)
    stats: dict[str, object] = {
        "nodes": 0,
        "terminals": 0,
        "best_regular": n + 1,
        "best_degree": None,
        "best_vertices": None,
        "best_columns": None,
        "best_mask": None,
        "best_clique": None,
        "best_independent": None,
    }
    start = monotonic()

    def dfs(adj: list[int], columns: list[int]) -> bool:
        stats["nodes"] = int(stats["nodes"]) + 1
        k = len(columns)
        if k == n:
            stats["terminals"] = int(stats["terminals"]) + 1
            regular, degree, vertices = cdc.max_regular(adj, pc)
            if regular < int(stats["best_regular"]):
                clique, _clique_vertices, independent, _independent_vertices = (
                    fdc.max_clique_independent(adj, pc)
                )
                stats["best_regular"] = regular
                stats["best_degree"] = degree
                stats["best_vertices"] = vertices
                stats["best_columns"] = columns[:]
                stats["best_mask"] = cdc.columns_to_mask(columns, pc)
                stats["best_clique"] = clique
                stats["best_independent"] = independent
                print(
                    "new_best "
                    f"terminals={stats['terminals']} regular={regular} "
                    f"degree={degree} clique={clique} independent={independent} "
                    "columns=" + ",".join(map(str, columns)),
                    flush=True,
                )
            if progress and int(stats["terminals"]) % progress == 0:
                print(
                    f"progress terminals={stats['terminals']} nodes={stats['nodes']} "
                    f"best_regular={stats['best_regular']} "
                    f"elapsed={monotonic() - start:.1f}s",
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
            if dfs(next_adj, columns + [column]):
                return True
        return False

    stopped_early = dfs([], [])
    print(f"n={n}")
    print(f"P={p}")
    print(f"nodes={stats['nodes']}")
    print(f"terminals={stats['terminals']}")
    print(f"stopped_early={stopped_early}")
    print(f"min_max_regular={stats['best_regular']}")
    print(f"regular_degree={stats['best_degree']}")
    print("regular_vertices=" + ",".join(map(str, stats["best_vertices"] or [])))
    print(f"clique_number={stats['best_clique']}")
    print(f"independence_number={stats['best_independent']}")
    print(f"best_mask={stats['best_mask']}")
    print("best_columns=" + ",".join(map(str, stats["best_columns"] or [])))


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
