#!/usr/bin/env python3
"""Exact small census for the full-drop ordered parameter C_full(P,h)."""

from __future__ import annotations

import argparse
from time import monotonic

import column_drop_census as cdc


def max_full_drop(adj: list[int], n: int) -> int:
    full_mask = (1 << n) - 1
    maximum = 0
    for i in range(n):
        for j in range(i + 1, n):
            allowed = full_mask & ~(1 << i) & ~(1 << j)
            drop = (adj[i] & ~adj[j] & allowed).bit_count()
            maximum = max(maximum, drop)
    return maximum


def legal_new_column_full(adj: list[int], k: int, column: int, p: int) -> bool:
    previous_mask = (1 << k) - 1
    for i in range(k):
        for j in range(i + 1, k):
            allowed = previous_mask & ~(1 << i) & ~(1 << j)
            drop = (adj[i] & ~adj[j] & allowed).bit_count()
            if ((column >> i) & 1) and not ((column >> j) & 1):
                drop += 1
            if drop >= p:
                return False
    for i in range(k):
        previous_neighbors = adj[i] & previous_mask
        if (previous_neighbors & ~column).bit_count() >= p:
            return False
    return True


def max_clique_independent(
    adj: list[int], pc: cdc.Precomp
) -> tuple[int, tuple[int, ...], int, tuple[int, ...]]:
    clique = 1
    clique_vertices = (0,)
    independent = 1
    independent_vertices = (0,)
    for size, entries in pc.subsets_by_size:
        if size <= clique and size <= independent:
            break
        for subset, vertices in entries:
            degree = (adj[vertices[0]] & subset).bit_count()
            if size > independent and degree == 0 and all(
                (adj[v] & subset).bit_count() == 0 for v in vertices[1:]
            ):
                independent = size
                independent_vertices = vertices
            if size > clique and degree == size - 1 and all(
                (adj[v] & subset).bit_count() == size - 1 for v in vertices[1:]
            ):
                clique = size
                clique_vertices = vertices
            if size <= clique and size <= independent:
                break
    return clique, clique_vertices, independent, independent_vertices


def exact(n: int, p: int, progress: int) -> None:
    pc = cdc.precompute(n)
    total = 1 << len(pc.edges)
    checked = 0
    best_homogeneous = n
    best_regular = n
    examples: list[tuple[int, int, str, tuple[int, ...], int, int, tuple[int, ...]]] = []
    start = monotonic()

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        drop = max_full_drop(adj, n)
        if drop >= p:
            continue
        checked += 1
        homogeneous, kind, homogeneous_vertices = cdc.max_homogeneous(adj, pc)
        regular, regular_degree, regular_vertices = cdc.max_regular(adj, pc)
        if homogeneous < best_homogeneous or regular < best_regular:
            best_homogeneous = min(best_homogeneous, homogeneous)
            best_regular = min(best_regular, regular)
            examples = [(mask, drop, kind, homogeneous_vertices, regular, regular_degree, regular_vertices)]
            print(
                "new_best "
                f"mask={mask} max_full_drop={drop} "
                f"max_homogeneous={homogeneous} max_regular={regular}",
                flush=True,
            )
        elif len(examples) < 5 and (
            homogeneous == best_homogeneous or regular == best_regular
        ):
            examples.append(
                (mask, drop, kind, homogeneous_vertices, regular, regular_degree, regular_vertices)
            )

        if progress and mask and mask % progress == 0:
            print(
                f"progress mask={mask}/{total} checked={checked} "
                f"best_homogeneous={best_homogeneous} best_regular={best_regular} "
                f"elapsed={monotonic() - start:.1f}s",
                flush=True,
            )

    print(f"n={n}")
    print(f"P={p}")
    print(f"labelled_graphs={total}")
    print(f"checked_full_drop={checked}")
    print(f"min_max_homogeneous={best_homogeneous}")
    print(f"min_max_regular={best_regular}")
    for mask, drop, kind, homogeneous_vertices, regular, regular_degree, regular_vertices in examples:
        print(
            f"example mask={mask} max_full_drop={drop} "
            f"homogeneous_kind={kind} homogeneous_vertices="
            + ",".join(map(str, homogeneous_vertices))
            + f" max_regular={regular} regular_degree={regular_degree} regular_vertices="
            + ",".join(map(str, regular_vertices))
        )


def fixed(n: int, mask: int) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    homogeneous, kind, homogeneous_vertices = cdc.max_homogeneous(adj, pc)
    clique_number, clique_vertices, independence_number, independent_vertices = (
        max_clique_independent(adj, pc)
    )
    regular, regular_degree, regular_vertices = cdc.max_regular(adj, pc)
    clique = cdc.clique_ranks(adj, n)
    independent = cdc.independent_ranks(adj, n)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"max_full_drop={max_full_drop(adj, n)}")
    print(f"max_column_drop={cdc.max_column_drop(adj, n)}")
    print(f"max_homogeneous={homogeneous}")
    print(f"homogeneous_kind={kind}")
    print("homogeneous_vertices=" + ",".join(map(str, homogeneous_vertices)))
    print(f"clique_number={clique_number}")
    print("clique_vertices=" + ",".join(map(str, clique_vertices)))
    print(f"independence_number={independence_number}")
    print("independent_vertices=" + ",".join(map(str, independent_vertices)))
    print(f"max_regular={regular}")
    print(f"regular_degree={regular_degree}")
    print("regular_vertices=" + ",".join(map(str, regular_vertices)))
    print("clique_ranks=" + ",".join(map(str, clique)))
    print(f"clique_rank_histogram={cdc.histogram(clique)}")
    print("independent_ranks=" + ",".join(map(str, independent)))
    print(f"independent_rank_histogram={cdc.histogram(independent)}")


def search_dfs(
    n: int,
    p: int,
    forbidden_order: int,
    forbidden_kind: str,
    adj: list[int],
    columns: list[int],
    nodes: list[int],
    max_nodes: int,
    progress: int,
) -> list[int] | None | bool:
    nodes[0] += 1
    if progress and nodes[0] % progress == 0:
        print(f"progress nodes={nodes[0]} depth={len(columns)}", flush=True)
    if nodes[0] > max_nodes:
        return None
    if len(columns) == n:
        return columns

    k = len(columns)
    candidates = []
    for column in range(1 << k):
        if not legal_new_column_full(adj, k, column, p):
            continue
        if forbidden_kind == "homogeneous":
            forbidden = cdc.creates_homogeneous(adj, k, column, forbidden_order)
        else:
            forbidden = cdc.creates_regular(adj, k, forbidden_order, column)
        if not forbidden:
            candidates.append(column)
    candidates.sort(key=lambda x: (abs(x.bit_count() - k / 2), x))

    for column in candidates:
        next_adj = adj[:]
        next_adj.append(column)
        for i in range(k):
            if (column >> i) & 1:
                next_adj[i] |= 1 << k
        result = search_dfs(
            n,
            p,
            forbidden_order,
            forbidden_kind,
            next_adj,
            columns + [column],
            nodes,
            max_nodes,
            progress,
        )
        if isinstance(result, list):
            return result
        if result is None:
            return None
    return False


def search(
    n: int,
    p: int,
    forbidden_order: int,
    forbidden_kind: str,
    max_nodes: int,
    progress: int,
) -> None:
    nodes = [0]
    result = search_dfs(
        n, p, forbidden_order, forbidden_kind, [], [], nodes, max_nodes, progress
    )
    print(f"n={n}")
    print(f"P={p}")
    print(f"forbidden_kind={forbidden_kind}")
    print(f"forbidden_order={forbidden_order}")
    print(f"nodes={nodes[0]}")
    print(f"max_nodes={max_nodes}")
    print(f"result={result}")
    if isinstance(result, list):
        pc = cdc.precompute(n)
        adj = cdc.columns_to_adjacency(result)
        homogeneous, kind, homogeneous_vertices = cdc.max_homogeneous(adj, pc)
        clique_number, clique_vertices, independence_number, independent_vertices = (
            max_clique_independent(adj, pc)
        )
        regular, regular_degree, regular_vertices = cdc.max_regular(adj, pc)
        print("columns=" + ",".join(map(str, result)))
        print(f"mask={cdc.columns_to_mask(result, pc)}")
        print(f"max_full_drop={max_full_drop(adj, n)}")
        print(f"max_homogeneous={homogeneous}")
        print(f"homogeneous_kind={kind}")
        print("homogeneous_vertices=" + ",".join(map(str, homogeneous_vertices)))
        print(f"clique_number={clique_number}")
        print("clique_vertices=" + ",".join(map(str, clique_vertices)))
        print(f"independence_number={independence_number}")
        print("independent_vertices=" + ",".join(map(str, independent_vertices)))
        print(f"max_regular={regular}")
        print(f"regular_degree={regular_degree}")
        print("regular_vertices=" + ",".join(map(str, regular_vertices)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--p", type=int, default=1)
    parser.add_argument("--search-h", type=int)
    parser.add_argument("--search-regular-h", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--max-nodes", type=int, default=1_000_000)
    parser.add_argument("--progress", type=int, default=0)
    args = parser.parse_args()
    if args.p < 1:
        raise SystemExit("--p must be positive")
    if args.search_h is not None and args.search_regular_h is not None:
        raise SystemExit("use at most one of --search-h and --search-regular-h")

    if args.search_h is not None:
        search(args.n, args.p, args.search_h, "homogeneous", args.max_nodes, args.progress)
    elif args.search_regular_h is not None:
        search(
            args.n,
            args.p,
            args.search_regular_h,
            "regular",
            args.max_nodes,
            args.progress,
        )
    elif args.mask is None:
        exact(args.n, args.p, args.progress)
    else:
        fixed(args.n, args.mask)


if __name__ == "__main__":
    main()
