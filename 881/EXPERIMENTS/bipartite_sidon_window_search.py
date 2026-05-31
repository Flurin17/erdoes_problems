#!/usr/bin/env python3
"""Finite search for bipartite certificate-free order-2 windows.

The remaining Schreier/pair obstruction can force a cofinite tail to split
into two certificate-free, Sidon-like colors with large mixed two-sum spikes.
This script searches small integer windows for that local shape.
"""

from __future__ import annotations

import argparse
from itertools import combinations


def is_certificate_free(subset: set[int], ambient: set[int]) -> bool:
    for e in subset:
        for y1 in subset:
            if y1 == e:
                continue
            for y2 in subset:
                if y2 == e:
                    continue
                if y1 + y2 - e in ambient:
                    return False
    return True


def two_sums(elements: set[int]) -> set[int]:
    ordered = sorted(elements)
    return {a + b for i, a in enumerate(ordered) for b in ordered[i:]}


def longest_interval(values: set[int]) -> tuple[int, int]:
    if not values:
        return (0, -1)
    best = (0, -1)
    start = prev = None
    for value in sorted(values):
        if start is None:
            start = prev = value
            continue
        if value == prev + 1:
            prev = value
            continue
        if prev - start > best[1] - best[0]:
            best = (start, prev)
        start = prev = value
    assert start is not None and prev is not None
    if prev - start > best[1] - best[0]:
        best = (start, prev)
    return best


def mixed_counts(c_set: set[int], d_set: set[int]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for c in c_set:
        for d in d_set:
            counts[c + d] = counts.get(c + d, 0) + 1
    return counts


def best_cross_reflection(c_set: set[int], d_set: set[int]) -> tuple[int, int]:
    counts = mixed_counts(c_set, d_set)
    if not counts:
        return (0, 0)
    center, count = max(counts.items(), key=lambda item: (item[1], -item[0]))
    return center, count


def supports_for_cross_residual(
    primary: set[int],
    residual: set[int],
    target: int,
) -> set[frozenset[int]]:
    edges: set[frozenset[int]] = set()
    ordered = sorted(primary)
    for i, a in enumerate(ordered):
        for b in ordered[i:]:
            if target - a - b in residual:
                edges.add(frozenset((a, b)))
    return edges


def exact_matching_size(edges: set[frozenset[int]]) -> int:
    ordered = tuple(sorted(edges, key=lambda item: (len(item), tuple(sorted(item)))))
    memo: dict[tuple[int, frozenset[int]], int] = {}

    def search(index: int, used: frozenset[int]) -> int:
        key = (index, used)
        if key in memo:
            return memo[key]
        if index == len(ordered):
            return 0
        best = search(index + 1, used)
        edge = ordered[index]
        if edge.isdisjoint(used):
            best = max(best, 1 + search(index + 1, used | edge))
        memo[key] = best
        return best

    return search(0, frozenset())


def cross_matching_summary(
    c_set: set[int],
    d_set: set[int],
    interval: tuple[int, int],
) -> tuple[int, int, int]:
    lo, hi = interval
    if lo > hi:
        return (0, 0, 0)
    c_min = d_min = 10**9
    both_min = 10**9
    for target in range(lo, hi + 1):
        c_match = exact_matching_size(
            supports_for_cross_residual(c_set, d_set, target)
        )
        d_match = exact_matching_size(
            supports_for_cross_residual(d_set, c_set, target)
        )
        c_min = min(c_min, c_match)
        d_min = min(d_min, d_match)
        both_min = min(both_min, max(c_match, d_match))
    return (c_min, d_min, both_min)


def search(max_value: int, size: int, limit: int, sort_mode: str) -> None:
    found = 0
    best_rows: list[
        tuple[
            int,
            int,
            int,
            int,
            int,
            int,
            tuple[int, ...],
            tuple[int, ...],
            tuple[int, int],
        ]
    ] = []
    for tuple_a in combinations(range(1, max_value + 1), size):
        ambient = set(tuple_a)
        masks = range(1, (1 << size) - 1)
        for mask in masks:
            c_set = {tuple_a[i] for i in range(size) if mask & (1 << i)}
            d_set = ambient - c_set
            if len(c_set) > len(d_set):
                continue
            if not is_certificate_free(c_set, ambient):
                continue
            if not is_certificate_free(d_set, ambient):
                continue
            lo, hi = longest_interval(two_sums(ambient))
            interval_len = hi - lo + 1
            center, spike = best_cross_reflection(c_set, d_set)
            if spike < 2 or interval_len < size:
                continue
            c_match, d_match, both_match = cross_matching_summary(
                c_set,
                d_set,
                (lo, hi),
            )
            row = (
                interval_len,
                spike,
                both_match,
                c_match,
                d_match,
                center,
                tuple(sorted(c_set)),
                tuple(sorted(d_set)),
                (lo, hi),
            )
            best_rows.append(row)
            if sort_mode == "matching":
                best_rows.sort(
                    key=lambda item: (
                        item[2],
                        min(item[3], item[4]),
                        item[0],
                        item[1],
                        item[5],
                    ),
                    reverse=True,
                )
            else:
                best_rows.sort(reverse=True)
            del best_rows[limit:]
            found += 1

    print(
        "bipartite certificate-free windows",
        "max_value=", max_value,
        "size=", size,
        "sort=", sort_mode,
        "found=", found,
    )
    for (
        interval_len,
        spike,
        both_match,
        c_match,
        d_match,
        center,
        c_tuple,
        d_tuple,
        interval,
    ) in best_rows:
        print(
            "  interval=",
            interval,
            "len=",
            interval_len,
            "mixed_center=",
            center,
            "spike=",
            spike,
            "match_min=",
            (c_match, d_match),
            "best_color_min=",
            both_match,
            "C=",
            list(c_tuple),
            "D=",
            list(d_tuple),
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-value", type=int, default=16)
    parser.add_argument("--size", type=int, default=6)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--sort", choices=("interval", "matching"), default="interval")
    args = parser.parse_args()
    search(args.max_value, args.size, args.limit, args.sort)


if __name__ == "__main__":
    main()
