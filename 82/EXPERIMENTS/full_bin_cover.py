#!/usr/bin/env python3
"""Full capped complete-multipartite bin-cover checks.

For modulus q and cap C=q+2, a valid complete-multipartite bin is either

* a rectangle r*1_I with r|I| <= C, or
* a special bin (q+1)e_i + e_j for distinct i,j.

This is the q+2 complete-multipartite packing model after excluding the
rectangle-only simplification.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations


def normalize(vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted((value for value in vector if value > 0), reverse=True))


def subtract(
    vector: tuple[int, ...],
    changes: tuple[tuple[int, int], ...],
) -> tuple[int, ...]:
    out = list(vector)
    for index, value in changes:
        out[index] -= value
    return normalize(tuple(out))


def candidates(vector: tuple[int, ...], q: int):
    """Yield canonical bins containing the largest remaining coordinate."""

    if not vector:
        return
    cap = q + 2
    special_height = q + 1
    pivot = 0

    # Rectangles r*1_I containing the pivot.
    max_height = min(vector[pivot], cap)
    for height in range(max_height, 0, -1):
        eligible = [index for index, value in enumerate(vector) if value >= height]
        if not eligible or eligible[0] != pivot:
            continue
        max_width = min(len(eligible), cap // height)
        for width in range(max_width, 0, -1):
            for rest in combinations(eligible[1:], width - 1):
                indices = (pivot,) + rest
                yield tuple((index, height) for index in indices)

    # Special bin with the pivot as the large endpoint.
    if vector[pivot] >= special_height:
        for index in range(1, len(vector)):
            if vector[index] >= 1:
                yield ((pivot, special_height), (index, 1))

    # Special bin with the pivot as the small endpoint.
    if vector[pivot] >= 1:
        for index in range(1, len(vector)):
            if vector[index] >= special_height:
                yield ((pivot, 1), (index, special_height))


def find_cover(
    vector: tuple[int, ...],
    q: int,
    bins: int,
) -> list[tuple[tuple[int, int], ...]] | None:
    vector = normalize(vector)
    cap = q + 2
    chosen: dict[tuple[tuple[int, ...], int], tuple[tuple[int, int], ...]] = {}

    @lru_cache(maxsize=None)
    def rec(state: tuple[int, ...], left: int) -> bool:
        if not state:
            return True
        if left == 0:
            return False
        if sum(state) > left * cap:
            return False
        if state[0] > left * cap:
            return False

        for choice in candidates(state, q):
            next_state = subtract(state, choice)
            if rec(next_state, left - 1):
                chosen[(state, left)] = choice
                return True
        return False

    if not rec(vector, bins):
        return None

    cover = []
    state = vector
    left = bins
    while state:
        choice = chosen[(state, left)]
        cover.append(choice)
        state = subtract(state, choice)
        left -= 1
    return cover


def integer_partitions(total: int, max_part: int | None = None):
    if total == 0:
        yield ()
        return
    if max_part is None or max_part > total:
        max_part = total
    for first in range(max_part, 0, -1):
        next_max = min(first, total - first) if total != first else 0
        for rest in integer_partitions(total - first, next_max):
            yield (first,) + rest


def format_bin(choice: tuple[tuple[int, int], ...]) -> str:
    values = sorted((value for _, value in choice), reverse=True)
    return "(" + ",".join(map(str, values)) + ")"


def exhaustive(q: int, max_total: int | None) -> None:
    if max_total is None:
        max_total = q * q
    cap = q + 2

    @lru_cache(maxsize=None)
    def rec(state: tuple[int, ...], left: int) -> bool:
        if not state:
            return True
        if left == 0:
            return False
        if sum(state) > left * cap:
            return False
        if state[0] > left * cap:
            return False
        if sum((value + cap - 1) // cap for value in state) <= left:
            return True
        if state[0] <= left:
            return True

        for choice in candidates(state, q):
            if rec(subtract(state, choice), left - 1):
                return True
        return False

    checked = 0
    bad: tuple[int, ...] | None = None
    for total in range(1, max_total + 1):
        for vector in integer_partitions(total):
            checked += 1
            if not rec(normalize(vector), q):
                bad = vector
                break
        if bad is not None:
            break
    print(f"q={q}")
    print(f"bins={q}")
    print(f"cap={q + 2}")
    print(f"max_total={max_total}")
    print(f"checked={checked}")
    print(f"cache_info={rec.cache_info()}")
    if bad is None:
        print("counterexample=none")
    else:
        print("counterexample=" + ",".join(map(str, bad)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--vector", help="comma-separated positive integers")
    parser.add_argument("--bins", type=int)
    parser.add_argument("--max-total", type=int)
    args = parser.parse_args()

    if args.vector:
        vector = tuple(int(item) for item in args.vector.split(",") if item)
        bins = args.bins if args.bins is not None else args.q
        cover = find_cover(vector, args.q, bins)
        print("vector=" + ",".join(map(str, normalize(vector))))
        print(f"q={args.q}")
        print(f"bins={bins}")
        print(f"cap={args.q + 2}")
        print(f"cover_exists={cover is not None}")
        if cover is not None:
            print("cover=" + " ".join(format_bin(choice) for choice in cover))
        return

    exhaustive(args.q, args.max_total)


if __name__ == "__main__":
    main()
