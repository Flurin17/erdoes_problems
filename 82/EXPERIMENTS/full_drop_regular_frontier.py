#!/usr/bin/env python3
"""Frontier search for regular full-drop obstructions."""

from __future__ import annotations

import argparse
from time import monotonic

import column_drop_census as cdc
import full_drop_census as fdc


def search(base_n: int, p: int, h: int, max_nodes: int, progress: int) -> None:
    pc = cdc.precompute(base_n)
    stats: dict[str, object] = {
        "nodes": 0,
        "terminals": 0,
        "extendable": 0,
        "best_extension_count": 0,
        "best_columns": None,
        "best_extensions": None,
        "stopped": False,
    }
    start = monotonic()

    def dfs(adj: list[int], columns: list[int]) -> bool:
        stats["nodes"] = int(stats["nodes"]) + 1
        if int(stats["nodes"]) > max_nodes:
            stats["stopped"] = True
            return True
        if progress and int(stats["nodes"]) % progress == 0:
            print(
                f"progress nodes={stats['nodes']} depth={len(columns)} "
                f"terminals={stats['terminals']} extendable={stats['extendable']} "
                f"elapsed={monotonic() - start:.1f}s",
                flush=True,
            )

        k = len(columns)
        if k == base_n:
            stats["terminals"] = int(stats["terminals"]) + 1
            extensions = []
            for column in range(1 << k):
                if not fdc.legal_new_column_full(adj, k, column, p):
                    continue
                if cdc.creates_regular(adj, k, h, column):
                    continue
                extensions.append(column)
            if len(extensions) > int(stats["best_extension_count"]):
                stats["best_extension_count"] = len(extensions)
                stats["best_columns"] = columns[:]
                stats["best_extensions"] = extensions[:]
                print(
                    "new_best_extension_count "
                    f"count={len(extensions)} columns="
                    + ",".join(map(str, columns))
                    + " extensions="
                    + ",".join(map(str, extensions[:20])),
                    flush=True,
                )
            if extensions:
                stats["extendable"] = int(stats["extendable"]) + 1
                print(
                    "extendable_terminal columns="
                    + ",".join(map(str, columns))
                    + " extensions="
                    + ",".join(map(str, extensions[:20])),
                    flush=True,
                )
                return True
            return False

        candidates = []
        for column in range(1 << k):
            if not fdc.legal_new_column_full(adj, k, column, p):
                continue
            if cdc.creates_regular(adj, k, h, column):
                continue
            candidates.append(column)
        candidates.sort(key=lambda x: (abs(x.bit_count() - k / 2), x))

        for column in candidates:
            next_adj = adj[:]
            next_adj.append(column)
            for i in range(k):
                if (column >> i) & 1:
                    next_adj[i] |= 1 << k
            if dfs(next_adj, columns + [column]):
                return True
        return False

    dfs([], [])
    print(f"base_n={base_n}")
    print(f"P={p}")
    print(f"h={h}")
    print(f"nodes={stats['nodes']}")
    print(f"max_nodes={max_nodes}")
    print(f"stopped={stats['stopped']}")
    print(f"terminals={stats['terminals']}")
    print(f"extendable={stats['extendable']}")
    print(f"best_extension_count={stats['best_extension_count']}")
    if stats["best_columns"] is not None:
        print("best_columns=" + ",".join(map(str, stats["best_columns"])))
        print("best_extensions=" + ",".join(map(str, stats["best_extensions"] or [])))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base_n", type=int)
    parser.add_argument("--p", type=int, default=2)
    parser.add_argument("--h", type=int, required=True)
    parser.add_argument("--max-nodes", type=int, default=1_000_000)
    parser.add_argument("--progress", type=int, default=0)
    args = parser.parse_args()
    search(args.base_n, args.p, args.h, args.max_nodes, args.progress)


if __name__ == "__main__":
    main()
