#!/usr/bin/env python3
"""Loss-graph diagnostics for P=2 full-drop ordered graphs."""

from __future__ import annotations

import argparse
from collections import Counter
from time import monotonic

import column_drop_census as cdc
import full_drop_census as fdc
import full_drop_p2_regular_construction as regfam


def loss_graph(adj: list[int]) -> list[int]:
    n = len(adj)
    loss_adj = [0] * n
    full_mask = (1 << n) - 1
    for i in range(n):
        for j in range(i + 1, n):
            allowed = full_mask & ~(1 << i) & ~(1 << j)
            drop = (adj[i] & ~adj[j] & allowed).bit_count()
            if drop == 1:
                loss_adj[i] |= 1 << j
                loss_adj[j] |= 1 << i
            elif drop > 1:
                raise ValueError(f"pair {(i, j)} has loss {drop}, not P=2 full-drop")
    return loss_adj


def edge_count(adj: list[int]) -> int:
    return sum(row.bit_count() for row in adj) // 2


def degree_histogram(adj: list[int]) -> dict[int, int]:
    return dict(sorted(Counter(row.bit_count() for row in adj).items()))


def mask_to_columns(n: int, mask: int, pc: cdc.Precomp) -> list[int]:
    columns = [0] * n
    for index, (u, v) in enumerate(pc.edges):
        if (mask >> index) & 1:
            columns[v] |= 1 << u
    return columns


def print_stats(columns: list[int]) -> None:
    n = len(columns)
    pc = cdc.precompute(n)
    adj = cdc.columns_to_adjacency(columns)
    loss_adj = loss_graph(adj)
    regular, regular_degree, regular_vertices = cdc.max_regular(adj, pc)
    clique, clique_vertices, independent, independent_vertices = fdc.max_clique_independent(
        loss_adj, pc
    )
    print(f"n={n}")
    print("columns=" + ",".join(map(str, columns)))
    print(f"mask={cdc.columns_to_mask(columns, pc)}")
    print(f"max_full_drop={fdc.max_full_drop(adj, n)}")
    print(f"max_regular={regular}")
    print(f"regular_degree={regular_degree}")
    print("regular_vertices=" + ",".join(map(str, regular_vertices)))
    print(f"loss_edges={edge_count(loss_adj)}")
    print(f"loss_degree_histogram={degree_histogram(loss_adj)}")
    print(f"loss_clique_number={clique}")
    print("loss_clique_vertices=" + ",".join(map(str, clique_vertices)))
    print(f"loss_independence_number={independent}")
    print("loss_independent_vertices=" + ",".join(map(str, independent_vertices)))


def add_loss_histograms(
    stats: dict[str, object], adj: list[int], pc: cdc.Precomp
) -> tuple[int, int, int, dict[int, int]]:
    loss_adj = loss_graph(adj)
    loss_clique, _, loss_independent, _ = fdc.max_clique_independent(loss_adj, pc)
    loss_edges = edge_count(loss_adj)
    loss_degree_hist = degree_histogram(loss_adj)
    stats["loss_alpha_hist"][loss_independent] += 1  # type: ignore[index]
    stats["loss_omega_hist"][loss_clique] += 1  # type: ignore[index]
    stats["loss_edges_hist"][loss_edges] += 1  # type: ignore[index]
    return loss_edges, loss_clique, loss_independent, loss_degree_hist


def enumerate_minimal(n: int, progress: int, max_terminals: int | None) -> None:
    pc = cdc.precompute(n)
    stats: dict[str, object] = {
        "nodes": 0,
        "terminals": 0,
        "best_regular": n + 1,
        "examples": [],
        "loss_alpha_hist": Counter(),
        "loss_omega_hist": Counter(),
        "loss_edges_hist": Counter(),
    }
    start = monotonic()

    def add_example(adj: list[int], columns: list[int]) -> None:
        regular, regular_degree, regular_vertices = cdc.max_regular(adj, pc)
        loss_edges, loss_clique, loss_independent, loss_degree_hist = add_loss_histograms(
            stats, adj, pc
        )
        if regular < int(stats["best_regular"]):
            stats["best_regular"] = regular
            stats["examples"] = []
        if regular == int(stats["best_regular"]) and len(stats["examples"]) < 10:
            stats["examples"].append(  # type: ignore[union-attr]
                (
                    columns[:],
                    cdc.columns_to_mask(columns, pc),
                    regular_degree,
                    regular_vertices,
                    loss_edges,
                    loss_clique,
                    loss_independent,
                    loss_degree_hist,
                )
            )

    def dfs(adj: list[int], columns: list[int]) -> bool:
        stats["nodes"] = int(stats["nodes"]) + 1
        k = len(columns)
        if k == n:
            stats["terminals"] = int(stats["terminals"]) + 1
            add_example(adj, columns)
            if progress and int(stats["terminals"]) % progress == 0:
                print(
                    f"progress terminals={stats['terminals']} nodes={stats['nodes']} "
                    f"best_regular={stats['best_regular']} "
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
    print("P=2")
    print(f"nodes={stats['nodes']}")
    print(f"terminals={stats['terminals']}")
    print(f"stopped_early={stopped_early}")
    print(f"min_max_regular={stats['best_regular']}")
    print(f"loss_alpha_histogram={dict(sorted(stats['loss_alpha_hist'].items()))}")
    print(f"loss_omega_histogram={dict(sorted(stats['loss_omega_hist'].items()))}")
    print(f"loss_edges_histogram={dict(sorted(stats['loss_edges_hist'].items()))}")
    for item in stats["examples"]:  # type: ignore[union-attr]
        (
            columns,
            mask,
            regular_degree,
            regular_vertices,
            loss_edges,
            loss_clique,
            loss_independent,
            loss_degree_hist,
        ) = item
        print(
            "best_example "
            f"mask={mask} regular_degree={regular_degree} "
            "regular_vertices="
            + ",".join(map(str, regular_vertices))
            + f" loss_edges={loss_edges} loss_clique={loss_clique} "
            f"loss_independent={loss_independent} "
            f"loss_degree_histogram={loss_degree_hist} "
            "columns="
            + ",".join(map(str, columns))
        )


def enumerate_obstructions(
    n: int, forbidden_order: int, progress: int, max_terminals: int | None
) -> None:
    pc = cdc.precompute(n)
    stats: dict[str, object] = {
        "nodes": 0,
        "terminals": 0,
        "loss_alpha_hist": Counter(),
        "loss_omega_hist": Counter(),
        "loss_edges_hist": Counter(),
        "examples": [],
    }
    start = monotonic()

    def add_example(adj: list[int], columns: list[int]) -> None:
        regular, regular_degree, regular_vertices = cdc.max_regular(adj, pc)
        if regular >= forbidden_order:
            raise AssertionError("terminal graph is not an obstruction")
        loss_edges, loss_clique, loss_independent, loss_degree_hist = add_loss_histograms(
            stats, adj, pc
        )
        if len(stats["examples"]) < 10:
            stats["examples"].append(  # type: ignore[union-attr]
                (
                    columns[:],
                    cdc.columns_to_mask(columns, pc),
                    regular,
                    regular_degree,
                    regular_vertices,
                    loss_edges,
                    loss_clique,
                    loss_independent,
                    loss_degree_hist,
                )
            )

    def dfs(adj: list[int], columns: list[int]) -> bool:
        stats["nodes"] = int(stats["nodes"]) + 1
        k = len(columns)
        if k == n:
            stats["terminals"] = int(stats["terminals"]) + 1
            add_example(adj, columns)
            if progress and int(stats["terminals"]) % progress == 0:
                print(
                    f"progress terminals={stats['terminals']} nodes={stats['nodes']} "
                    f"elapsed={monotonic() - start:.1f}s",
                    flush=True,
                )
            return max_terminals is not None and int(stats["terminals"]) >= max_terminals

        for column in range(1 << k):
            if not fdc.legal_new_column_full(adj, k, column, 2):
                continue
            if cdc.creates_regular(adj, k, forbidden_order, column):
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
    print("P=2")
    print(f"forbidden_regular_order={forbidden_order}")
    print(f"nodes={stats['nodes']}")
    print(f"terminals={stats['terminals']}")
    print(f"stopped_early={stopped_early}")
    print(f"loss_alpha_histogram={dict(sorted(stats['loss_alpha_hist'].items()))}")
    print(f"loss_omega_histogram={dict(sorted(stats['loss_omega_hist'].items()))}")
    print(f"loss_edges_histogram={dict(sorted(stats['loss_edges_hist'].items()))}")
    for item in stats["examples"]:  # type: ignore[union-attr]
        (
            columns,
            mask,
            regular,
            regular_degree,
            regular_vertices,
            loss_edges,
            loss_clique,
            loss_independent,
            loss_degree_hist,
        ) = item
        print(
            "obstruction_example "
            f"mask={mask} max_regular={regular} regular_degree={regular_degree} "
            "regular_vertices="
            + ",".join(map(str, regular_vertices))
            + f" loss_edges={loss_edges} loss_clique={loss_clique} "
            f"loss_independent={loss_independent} "
            f"loss_degree_histogram={loss_degree_hist} "
            "columns="
            + ",".join(map(str, columns))
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family-h", type=int)
    parser.add_argument("--n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--columns")
    parser.add_argument("--enumerate", action="store_true")
    parser.add_argument("--avoid-regular-h", type=int)
    parser.add_argument("--progress", type=int, default=0)
    parser.add_argument("--max-terminals", type=int)
    args = parser.parse_args()

    modes = [
        args.family_h is not None,
        args.mask is not None,
        args.columns is not None,
        args.enumerate,
        args.avoid_regular_h is not None,
    ]
    if sum(modes) != 1:
        raise SystemExit(
            "choose exactly one of --family-h, --mask, --columns, "
            "--enumerate, --avoid-regular-h"
        )

    if args.family_h is not None:
        print_stats(regfam.build_columns(args.family_h))
    elif args.mask is not None:
        if args.n is None:
            raise SystemExit("--mask requires --n")
        pc = cdc.precompute(args.n)
        columns = mask_to_columns(args.n, args.mask, pc)
        print_stats(columns)
    elif args.columns is not None:
        columns = [int(x) for x in args.columns.split(",") if x]
        print_stats(columns)
    else:
        if args.avoid_regular_h is not None:
            if args.n is None:
                raise SystemExit("--avoid-regular-h requires --n")
            enumerate_obstructions(
                args.n, args.avoid_regular_h, args.progress, args.max_terminals
            )
            return
        if args.n is None:
            raise SystemExit("--enumerate requires --n")
        enumerate_minimal(args.n, args.progress, args.max_terminals)


if __name__ == "__main__":
    main()
