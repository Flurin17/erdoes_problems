#!/usr/bin/env python3
"""Exact searches for the complete-multipartite q+2 bin model.

State vectors are complete-multipartite class sizes.  A legal bin is either

* a rectangle r * 1_I with r |I| <= q+2, or
* a special two-class bin (q+1)e_i + e_j.

These are exactly the q-modular complete-multipartite induced subgraphs of
order at most q+2.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations


class SearchLimitExceeded(RuntimeError):
    pass


Bin = tuple[tuple[int, int], ...]


def normalize(vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted((value for value in vector if value > 0), reverse=True))


def subtract_bin(vector: tuple[int, ...], bin_counts: Bin) -> tuple[int, ...]:
    out = list(vector)
    for index, count in bin_counts:
        out[index] -= count
        if out[index] < 0:
            raise ValueError("bin exceeds vector")
    return normalize(tuple(out))


def candidates(vector: tuple[int, ...], q: int):
    """Yield legal bins that use the pivot coordinate 0."""

    if not vector:
        return
    cap = q + 2
    pivot = 0

    # Rectangle bins r * 1_I.
    max_height = min(vector[pivot], cap)
    for height in range(max_height, 0, -1):
        eligible = [index for index, value in enumerate(vector) if value >= height]
        if not eligible or eligible[0] != pivot:
            continue
        max_width = min(len(eligible), cap // height)
        for width in range(max_width, 0, -1):
            for rest in combinations(eligible[1:], width - 1):
                yield tuple((index, height) for index in (pivot,) + rest)

    # Special bins where the pivot supplies q+1 vertices.
    if vector[pivot] >= q + 1:
        for other, value in enumerate(vector[1:], start=1):
            if value >= 1:
                yield ((pivot, q + 1), (other, 1))

    # Special bins where the pivot supplies the singleton.
    if vector[pivot] >= 1:
        for other, value in enumerate(vector[1:], start=1):
            if value >= q + 1:
                yield ((pivot, 1), (other, q + 1))


def singly_coverable(state: tuple[int, ...], q: int, left: int) -> bool:
    cap = q + 2
    return sum((value + cap - 1) // cap for value in state) <= left


def unit_layer_coverable(state: tuple[int, ...], q: int, left: int) -> bool:
    return bool(state) and state[0] <= left and sum(state) <= left * (q + 2)


def find_cover(
    vector: tuple[int, ...],
    q: int,
    bins: int,
    op_limit: int | None,
) -> tuple[list[Bin] | None, int, int]:
    vector = normalize(vector)
    chosen: dict[tuple[tuple[int, ...], int], Bin] = {}
    nodes = 0
    branches = 0

    @lru_cache(maxsize=None)
    def rec(state: tuple[int, ...], left: int) -> bool:
        nonlocal nodes, branches
        nodes += 1
        if op_limit is not None and nodes + branches > op_limit:
            raise SearchLimitExceeded
        if not state:
            return True
        if left == 0:
            return False
        if sum(state) > left * (q + 2):
            return False

        for bin_counts in candidates(state, q):
            branches += 1
            if op_limit is not None and nodes + branches > op_limit:
                raise SearchLimitExceeded
            next_state = subtract_bin(state, bin_counts)
            if rec(next_state, left - 1):
                chosen[(state, left)] = bin_counts
                return True
        return False

    if not rec(vector, bins):
        return None, nodes, branches

    cover: list[Bin] = []
    state = vector
    left = bins
    while state:
        bin_counts = chosen[(state, left)]
        cover.append(bin_counts)
        state = subtract_bin(state, bin_counts)
        left -= 1
    return cover, nodes, branches


def integer_partitions(total: int, max_part: int | None = None):
    if total == 0:
        yield ()
        return
    if max_part is None or max_part > total:
        max_part = total
    for first in range(max_part, 0, -1):
        for rest in integer_partitions(total - first, min(first, total - first)):
            yield (first,) + rest


def format_bin(bin_counts: Bin) -> str:
    return ",".join(f"{index}:{count}" for index, count in bin_counts)


def exhaustive(
    q: int,
    max_total: int,
    op_limit: int | None,
    progress_every: int | None,
) -> None:
    nodes = 0
    branches = 0

    @lru_cache(maxsize=None)
    def rec(state: tuple[int, ...], left: int) -> bool:
        nonlocal nodes, branches
        nodes += 1
        if op_limit is not None and nodes + branches > op_limit:
            raise SearchLimitExceeded
        if not state:
            return True
        if left == 0:
            return False
        if sum(state) > left * (q + 2):
            return False
        if singly_coverable(state, q, left):
            return True
        if unit_layer_coverable(state, q, left):
            return True

        for bin_counts in candidates(state, q):
            branches += 1
            if op_limit is not None and nodes + branches > op_limit:
                raise SearchLimitExceeded
            next_state = subtract_bin(state, bin_counts)
            if rec(next_state, left - 1):
                return True
        return False

    checked = 0
    for total in range(1, max_total + 1):
        for vector in integer_partitions(total):
            checked += 1
            try:
                cover_exists = rec(normalize(vector), q)
            except SearchLimitExceeded:
                print(f"checked={checked}")
                print(f"unknown_vector={','.join(map(str, vector))}")
                print("result=unknown_op_limit")
                print(f"nodes={nodes}")
                print(f"branches={branches}")
                print(f"cache_info={rec.cache_info()}")
                return
            if not cover_exists:
                print(f"checked={checked}")
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
    print(f"nodes={nodes}")
    print(f"branches={branches}")
    print(f"cache_info={rec.cache_info()}")
    print("counterexample=none")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--vector", help="comma-separated positive integers")
    parser.add_argument("--max-total", type=int)
    parser.add_argument("--op-limit", type=int)
    parser.add_argument("--progress-every", type=int)
    args = parser.parse_args()

    if args.vector:
        vector = tuple(int(item) for item in args.vector.split(",") if item)
        cover, nodes, branches = find_cover(vector, args.q, args.q, args.op_limit)
        print("vector=" + ",".join(map(str, normalize(vector))))
        print(f"q={args.q}")
        print(f"nodes={nodes}")
        print(f"branches={branches}")
        print(f"cover_exists={cover is not None}")
        if cover is not None:
            print("cover=" + " ".join(format_bin(item) for item in cover))
        return

    if args.max_total is None:
        parser.error("provide --vector or --max-total")
    exhaustive(args.q, args.max_total, args.op_limit, args.progress_every)


if __name__ == "__main__":
    main()
