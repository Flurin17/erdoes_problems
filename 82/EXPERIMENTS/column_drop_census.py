#!/usr/bin/env python3
"""Exact small census for the column-drop ordered parameter C_drop(P,h)."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations
from time import monotonic


@dataclass(frozen=True)
class Precomp:
    n: int
    edges: list[tuple[int, int]]
    edge_index: dict[tuple[int, int], int]
    subsets_by_size: list[tuple[int, list[tuple[int, tuple[int, ...]]]]]


def precompute(n: int) -> Precomp:
    edges = list(combinations(range(n), 2))
    edge_index = {edge: index for index, edge in enumerate(edges)}
    subsets_by_size = []
    for size in range(n, 0, -1):
        entries = []
        for subset in range(1, 1 << n):
            if subset.bit_count() == size:
                vertices = tuple(v for v in range(n) if (subset >> v) & 1)
                entries.append((subset, vertices))
        subsets_by_size.append((size, entries))
    return Precomp(n, edges, edge_index, subsets_by_size)


def adjacency(n: int, mask: int, pc: Precomp) -> list[int]:
    adj = [0] * n
    for index, (u, v) in enumerate(pc.edges):
        if (mask >> index) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def max_column_drop(adj: list[int], n: int) -> int:
    maximum = 0
    for j in range(n):
        for k in range(j + 1, n):
            drop = 0
            for i in range(j):
                if ((adj[i] >> j) & 1) and not ((adj[i] >> k) & 1):
                    drop += 1
            maximum = max(maximum, drop)
    return maximum


def max_homogeneous(adj: list[int], pc: Precomp) -> tuple[int, str, tuple[int, ...]]:
    for size, entries in pc.subsets_by_size:
        clique_degree = size - 1
        for subset, vertices in entries:
            degree = (adj[vertices[0]] & subset).bit_count()
            if degree not in (0, clique_degree):
                continue
            if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                kind = "independent" if degree == 0 else "clique"
                return size, kind, vertices
    return 1, "single", (0,)


def max_regular(adj: list[int], pc: Precomp) -> tuple[int, int, tuple[int, ...]]:
    for size, entries in pc.subsets_by_size:
        for subset, vertices in entries:
            degree = (adj[vertices[0]] & subset).bit_count()
            if all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                return size, degree, vertices
    return 1, 0, (0,)


def clique_ranks(adj: list[int], n: int) -> list[int]:
    ranks = [1] * n
    for v in range(n):
        best = 1
        earlier_neighbors = [u for u in range(v) if (adj[v] >> u) & 1]
        for size in range(len(earlier_neighbors), 0, -1):
            found = False
            for combo in combinations(earlier_neighbors, size):
                subset = sum(1 << x for x in combo)
                if all((adj[x] & subset).bit_count() == size - 1 for x in combo):
                    best = size + 1
                    found = True
                    break
            if found:
                break
        ranks[v] = best
    return ranks


def independent_ranks(adj: list[int], n: int) -> list[int]:
    ranks = [1] * n
    for v in range(n):
        best = 1
        earlier_nonneighbors = [u for u in range(v) if not ((adj[v] >> u) & 1)]
        for size in range(len(earlier_nonneighbors), 0, -1):
            found = False
            for combo in combinations(earlier_nonneighbors, size):
                subset = sum(1 << x for x in combo)
                if all((adj[x] & subset).bit_count() == 0 for x in combo):
                    best = size + 1
                    found = True
                    break
            if found:
                break
        ranks[v] = best
    return ranks


def histogram(values: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for value in values:
        out[value] = out.get(value, 0) + 1
    return dict(sorted(out.items()))


def columns_to_adjacency(columns: list[int]) -> list[int]:
    adj = []
    for k, mask in enumerate(columns):
        adj.append(mask)
        for i in range(k):
            if (mask >> i) & 1:
                adj[i] |= 1 << k
    return adj


def columns_to_mask(columns: list[int], pc: Precomp) -> int:
    mask = 0
    for k, column in enumerate(columns):
        for i in range(k):
            if (column >> i) & 1:
                mask |= 1 << pc.edge_index[(i, k)]
    return mask


def creates_homogeneous(
    adj: list[int], k: int, column: int, homogeneous_order: int
) -> bool:
    for previous in combinations(range(k), homogeneous_order - 1):
        subset = sum(1 << v for v in previous)
        new_degree = (column & subset).bit_count()
        if new_degree == 0 and all((adj[v] & subset).bit_count() == 0 for v in previous):
            return True
        if new_degree == homogeneous_order - 1 and all(
            (adj[v] & subset).bit_count() == homogeneous_order - 2
            for v in previous
        ):
            return True
    return False


def creates_regular(adj: list[int], k: int, regular_order: int, column: int) -> bool:
    for order in range(regular_order, k + 2):
        for previous in combinations(range(k), order - 1):
            subset = sum(1 << v for v in previous)
            new_degree = (column & subset).bit_count()
            ok = True
            for v in previous:
                degree = (adj[v] & subset).bit_count() + ((column >> v) & 1)
                if degree != new_degree:
                    ok = False
                    break
            if ok:
                return True
    return False


def legal_new_column(adj: list[int], k: int, column: int, p: int) -> bool:
    for j in range(k):
        earlier_neighbors_of_j = adj[j] & ((1 << j) - 1)
        if (earlier_neighbors_of_j & ~column).bit_count() >= p:
            return False
    return True


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
        if not legal_new_column(adj, k, column, p):
            continue
        if forbidden_kind == "homogeneous":
            forbidden = creates_homogeneous(adj, k, column, forbidden_order)
        else:
            forbidden = creates_regular(adj, k, forbidden_order, column)
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


def exact(n: int, p: int, progress: int) -> None:
    pc = precompute(n)
    total = 1 << len(pc.edges)
    checked = 0
    best_homogeneous = n
    examples: list[tuple[int, str, tuple[int, ...], int]] = []
    start = monotonic()

    for mask in range(total):
        adj = adjacency(n, mask, pc)
        if max_column_drop(adj, n) >= p:
            continue
        checked += 1
        homogeneous, kind, vertices = max_homogeneous(adj, pc)
        if homogeneous < best_homogeneous:
            best_homogeneous = homogeneous
            examples = [(mask, kind, vertices, max_column_drop(adj, n))]
            print(
                "new_best "
                f"mask={mask} max_homogeneous={homogeneous} kind={kind} "
                f"vertices={vertices}",
                flush=True,
            )
        elif homogeneous == best_homogeneous and len(examples) < 5:
            examples.append((mask, kind, vertices, max_column_drop(adj, n)))

        if progress and mask and mask % progress == 0:
            print(
                f"progress mask={mask}/{total} checked={checked} "
                f"best={best_homogeneous} elapsed={monotonic() - start:.1f}s",
                flush=True,
            )

    print(f"n={n}")
    print(f"P={p}")
    print(f"labelled_graphs={total}")
    print(f"checked_column_drop={checked}")
    print(f"min_max_homogeneous={best_homogeneous}")
    for mask, kind, vertices, drop in examples:
        print(
            f"example mask={mask} max_drop={drop} "
            f"homogeneous_kind={kind} homogeneous_vertices="
            + ",".join(map(str, vertices))
        )


def fixed(n: int, mask: int) -> None:
    pc = precompute(n)
    adj = adjacency(n, mask, pc)
    homogeneous, kind, vertices = max_homogeneous(adj, pc)
    regular, regular_degree, regular_vertices = max_regular(adj, pc)
    clique = clique_ranks(adj, n)
    independent = independent_ranks(adj, n)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"max_column_drop={max_column_drop(adj, n)}")
    print(f"max_homogeneous={homogeneous}")
    print(f"homogeneous_kind={kind}")
    print("homogeneous_vertices=" + ",".join(map(str, vertices)))
    print(f"max_regular={regular}")
    print(f"regular_degree={regular_degree}")
    print("regular_vertices=" + ",".join(map(str, regular_vertices)))
    print("clique_ranks=" + ",".join(map(str, clique)))
    print(f"clique_rank_histogram={histogram(clique)}")
    print("independent_ranks=" + ",".join(map(str, independent)))
    print(f"independent_rank_histogram={histogram(independent)}")


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
        pc = precompute(n)
        adj = columns_to_adjacency(result)
        homogeneous, kind, vertices = max_homogeneous(adj, pc)
        regular, regular_degree, regular_vertices = max_regular(adj, pc)
        clique = clique_ranks(adj, n)
        independent = independent_ranks(adj, n)
        print("columns=" + ",".join(map(str, result)))
        print(f"mask={columns_to_mask(result, pc)}")
        print(f"max_column_drop={max_column_drop(adj, n)}")
        print(f"max_homogeneous={homogeneous}")
        print(f"homogeneous_kind={kind}")
        print("homogeneous_vertices=" + ",".join(map(str, vertices)))
        print(f"max_regular={regular}")
        print(f"regular_degree={regular_degree}")
        print("regular_vertices=" + ",".join(map(str, regular_vertices)))
        print("clique_ranks=" + ",".join(map(str, clique)))
        print(f"clique_rank_histogram={histogram(clique)}")
        print("independent_ranks=" + ",".join(map(str, independent)))
        print(f"independent_rank_histogram={histogram(independent)}")


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
