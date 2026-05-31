#!/usr/bin/env python3
"""Ferrers rectangle cover checks for complete multipartite packing.

A rectangle has the form `(r^h)`: subtract `r` from `h` positive coordinates,
with area `r*h <= cap`.  This is the rectangle-only version of the
complete-multipartite capped modular packing problem.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations


class SearchLimitExceeded(RuntimeError):
    pass


def normalize(vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted((value for value in vector if value > 0), reverse=True))


def candidates(vector: tuple[int, ...], cap: int):
    if not vector:
        return
    pivot = 0
    max_height = min(vector[pivot], cap)
    for height in range(max_height, 0, -1):
        eligible = [index for index, value in enumerate(vector) if value >= height]
        if not eligible or eligible[0] != pivot:
            continue
        max_width = min(len(eligible), cap // height)
        for width in range(max_width, 0, -1):
            for rest in combinations(eligible[1:], width - 1):
                yield (pivot,) + rest, height


def subtract_rectangle(
    vector: tuple[int, ...],
    indices: tuple[int, ...],
    height: int,
) -> tuple[int, ...]:
    out = list(vector)
    for index in indices:
        out[index] -= height
    return normalize(tuple(out))


def find_cover(
    vector: tuple[int, ...],
    bins: int,
    cap: int,
    node_limit: int | None,
) -> tuple[list[tuple[int, int]] | None, int]:
    vector = normalize(vector)
    chosen: dict[tuple[tuple[int, ...], int], tuple[int, int]] = {}
    nodes = 0
    branches = 0

    @lru_cache(maxsize=None)
    def rec(state: tuple[int, ...], left: int) -> bool:
        nonlocal nodes, branches
        nodes += 1
        if node_limit is not None and nodes + branches > node_limit:
            raise SearchLimitExceeded
        if not state:
            return True
        if left == 0:
            return False
        if sum(state) > left * cap:
            return False

        for indices, height in candidates(state, cap):
            branches += 1
            if node_limit is not None and nodes + branches > node_limit:
                raise SearchLimitExceeded
            next_state = subtract_rectangle(state, indices, height)
            if rec(next_state, left - 1):
                chosen[(state, left)] = (len(indices), height)
                return True
        return False

    if not rec(vector, bins):
        return None, nodes

    cover = []
    state = vector
    left = bins
    while state:
        width, height = chosen[(state, left)]
        cover.append((width, height))
        # Reconstruct one compatible transition for display.
        for indices, candidate_height in candidates(state, cap):
            if len(indices) == width and candidate_height == height:
                next_state = subtract_rectangle(state, indices, height)
                if rec(next_state, left - 1):
                    state = next_state
                    left -= 1
                    break
        else:
            raise AssertionError("stored rectangle no longer reconstructs")
    return cover, nodes + branches


def integer_partitions(total: int, max_part: int | None = None):
    if total == 0:
        yield ()
        return
    if max_part is None or max_part > total:
        max_part = total
    for first in range(max_part, 0, -1):
        for rest in integer_partitions(total - first, min(first, total - first)):
            yield (first,) + rest


def exhaustive(
    max_total: int,
    bins: int,
    cap: int,
    node_limit: int | None,
    progress_every: int | None,
    max_first: int | None,
) -> None:
    nodes = 0
    branches = 0

    @lru_cache(maxsize=None)
    def rec(state: tuple[int, ...], left: int) -> bool:
        nonlocal nodes, branches
        nodes += 1
        if node_limit is not None and nodes + branches > node_limit:
            raise SearchLimitExceeded
        if not state:
            return True
        if left == 0:
            return False
        if sum(state) > left * cap:
            return False

        for indices, height in candidates(state, cap):
            branches += 1
            if node_limit is not None and nodes + branches > node_limit:
                raise SearchLimitExceeded
            next_state = subtract_rectangle(state, indices, height)
            if rec(next_state, left - 1):
                return True
        return False

    checked = 0
    skipped = 0
    for total in range(1, max_total + 1):
        for vector in integer_partitions(total):
            if max_first is not None and vector and vector[0] > max_first:
                skipped += 1
                continue
            checked += 1
            try:
                cover_exists = rec(normalize(vector), bins)
            except SearchLimitExceeded:
                print(f"checked={checked}")
                if max_first is not None:
                    print(f"max_first={max_first}")
                    print(f"skipped={skipped}")
                print(f"unknown_vector={','.join(map(str, vector))}")
                print("result=unknown_node_limit")
                print(f"nodes={nodes}")
                print(f"branches={branches}")
                print(f"cache_info={rec.cache_info()}")
                return
            if not cover_exists:
                print(f"checked={checked}")
                if max_first is not None:
                    print(f"max_first={max_first}")
                    print(f"skipped={skipped}")
                print(f"counterexample={','.join(map(str, vector))}")
                print(f"nodes={nodes}")
                print(f"branches={branches}")
                print(f"cache_info={rec.cache_info()}")
                return
            if progress_every is not None and checked % progress_every == 0:
                print(
                    f"progress checked={checked} total={total} "
                    f"nodes={nodes} branches={branches} cache={rec.cache_info().currsize}",
                    flush=True,
                )
    print(f"checked={checked}")
    if max_first is not None:
        print(f"max_first={max_first}")
        print(f"skipped={skipped}")
    print(f"nodes={nodes}")
    print(f"branches={branches}")
    print(f"cache_info={rec.cache_info()}")
    print("counterexample=none")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vector", help="comma-separated positive integers")
    parser.add_argument("--bins", type=int, required=True)
    parser.add_argument("--cap", type=int, required=True)
    parser.add_argument("--max-total", type=int)
    parser.add_argument("--max-first", type=int)
    parser.add_argument("--node-limit", type=int)
    parser.add_argument("--progress-every", type=int)
    args = parser.parse_args()

    if args.vector:
        vector = tuple(int(item) for item in args.vector.split(",") if item)
        cover, nodes = find_cover(vector, args.bins, args.cap, args.node_limit)
        print("vector=" + ",".join(map(str, normalize(vector))))
        print(f"bins={args.bins}")
        print(f"cap={args.cap}")
        print(f"nodes={nodes}")
        print(f"cover_exists={cover is not None}")
        if cover is not None:
            print("cover=" + " ".join(f"{height}^{width}" for width, height in cover))
        return

    if args.max_total is None:
        parser.error("provide --vector or --max-total")
    exhaustive(
        args.max_total,
        args.bins,
        args.cap,
        args.node_limit,
        args.progress_every,
        args.max_first,
    )


if __name__ == "__main__":
    main()
