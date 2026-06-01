#!/usr/bin/env python3
"""DFS for inversion-free ordered graphs avoiding large regular sets.

For column-drop parameter P=1, ordered graphs are exactly suffix-threshold
graphs: in the fixed order, each vertex's later-neighborhood is a suffix.
This script searches that restricted family directly.  It is intended for
small exact calibrations of C_reg(1,h), where the general column-drop DFS has
too much overhead.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations
from time import monotonic


@dataclass
class SearchState:
    n: int
    h: int
    adj: list[int]
    columns: list[int]
    nodes: int = 0
    start: float = 0.0


def precompute_masks(n: int) -> list[list[list[tuple[int, tuple[int, ...]]]]]:
    """subset data by prefix size and subset size."""
    masks_by_k_size: list[list[list[tuple[int, tuple[int, ...]]]]] = []
    for k in range(n + 1):
        by_size = [[] for _ in range(k + 1)]
        for size in range(k + 1):
            for combo in combinations(range(k), size):
                mask = 0
                for v in combo:
                    mask |= 1 << v
                by_size[size].append((mask, combo))
        masks_by_k_size.append(by_size)
    return masks_by_k_size


def bits(mask: int) -> list[int]:
    out = []
    while mask:
        bit = mask & -mask
        out.append(bit.bit_length() - 1)
        mask ^= bit
    return out


def is_regular_after_adding(
    adj: list[int], subset: int, subset_vertices: tuple[int, ...], column: int
) -> bool:
    """Check regularity of subset union {new_vertex} after adding its column."""
    new_degree = (column & subset).bit_count()
    for v in subset_vertices:
        degree = (adj[v] & subset).bit_count() + ((column >> v) & 1)
        if degree != new_degree:
            return False
    return True


def creates_regular(
    adj: list[int],
    k: int,
    h: int,
    column: int,
    masks_by_k_size: list[list[list[tuple[int, tuple[int, ...]]]]],
) -> bool:
    for order in range(h, k + 2):
        for subset, subset_vertices in masks_by_k_size[k][order - 1]:
            if is_regular_after_adding(adj, subset, subset_vertices, column):
                return True
    return False


def candidate_columns(k: int, previous_column: int) -> list[int]:
    """All suffix-threshold legal columns for new vertex k.

    A previous row that was already adjacent to k-1 must remain adjacent to k.
    Every previous row that was not adjacent to k-1 may either switch on at k
    or remain off.  The immediate predecessor k-1 is also free.
    """
    if k == 0:
        return [0]
    old_mask = (1 << (k - 1)) - 1
    optional_mask = old_mask & ~previous_column
    optional_bits = bits(optional_mask) + [k - 1]
    candidates = []
    for choice in range(1 << len(optional_bits)):
        column = previous_column
        for index, bit_index in enumerate(optional_bits):
            if (choice >> index) & 1:
                column |= 1 << bit_index
        candidates.append(column)
    candidates.sort(key=lambda c: (abs(c.bit_count() - k / 2), c))
    return candidates


def columns_to_thresholds(columns: list[int], n: int) -> tuple[int, ...]:
    thresholds = []
    for i in range(n):
        threshold = n
        for k in range(i + 1, n):
            if (columns[k] >> i) & 1:
                threshold = k
                break
        thresholds.append(threshold)
    return tuple(thresholds)


def dfs(
    state: SearchState,
    masks_by_k_size: list[list[list[tuple[int, tuple[int, ...]]]]],
    max_nodes: int,
    progress: int,
) -> list[int] | None | bool:
    state.nodes += 1
    if progress and state.nodes % progress == 0:
        print(
            f"progress nodes={state.nodes} depth={len(state.columns)} "
            f"elapsed={monotonic() - state.start:.1f}s",
            flush=True,
        )
    if max_nodes and state.nodes > max_nodes:
        return None
    if len(state.columns) == state.n:
        return state.columns[:]

    k = len(state.columns)
    previous_column = state.columns[-1] if state.columns else 0
    for column in candidate_columns(k, previous_column):
        if creates_regular(state.adj, k, state.h, column, masks_by_k_size):
            continue
        saved_adj = state.adj
        next_adj = state.adj[:]
        next_adj.append(column)
        for i in range(k):
            if (column >> i) & 1:
                next_adj[i] |= 1 << k
        state.adj = next_adj
        state.columns.append(column)
        result = dfs(state, masks_by_k_size, max_nodes, progress)
        if isinstance(result, list):
            return result
        state.columns.pop()
        state.adj = saved_adj
        if result is None:
            return None
    return False


def verify_columns(columns: list[int], n: int) -> list[int]:
    adj = [0] * n
    for k, column in enumerate(columns):
        for i in range(k):
            if (column >> i) & 1:
                adj[i] |= 1 << k
                adj[k] |= 1 << i
    return adj


def max_regular_order(adj: list[int], n: int) -> tuple[int, int, tuple[int, ...]]:
    for order in range(n, 0, -1):
        for combo in combinations(range(n), order):
            subset = 0
            for v in combo:
                subset |= 1 << v
            degree = (adj[combo[0]] & subset).bit_count()
            if all((adj[v] & subset).bit_count() == degree for v in combo[1:]):
                return order, degree, combo
    return 1, 0, (0,)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--h", type=int, required=True)
    parser.add_argument("--max-nodes", type=int, default=0)
    parser.add_argument("--progress", type=int, default=100000)
    args = parser.parse_args()

    state = SearchState(n=args.n, h=args.h, adj=[], columns=[], start=monotonic())
    masks_by_k_size = precompute_masks(args.n)
    result = dfs(state, masks_by_k_size, args.max_nodes, args.progress)
    print(f"n={args.n}")
    print(f"h={args.h}")
    print(f"nodes={state.nodes}")
    print(f"elapsed={monotonic() - state.start:.3f}s")
    if result is None:
        print("status=unknown_node_limit")
    elif result is False:
        print("status=unsat")
    else:
        adj = verify_columns(result, args.n)
        regular, degree, witness = max_regular_order(adj, args.n)
        print("status=found")
        print("columns=" + ",".join(map(str, result)))
        print("thresholds=" + ",".join(map(str, columns_to_thresholds(result, args.n))))
        print(f"max_regular_order={regular}")
        print(f"regular_degree={degree}")
        print("regular_vertices=" + ",".join(map(str, witness)))


if __name__ == "__main__":
    main()
