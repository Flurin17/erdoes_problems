#!/usr/bin/env python3
"""Dyadic modular partitions for finite twin-class blow-up models.

A twin blow-up is described by class sizes, a loop bit for each class
(independent or clique inside the class), and complete/empty adjacency between
class pairs.  The model is exact for graphs whose vertices are partitioned
into twin classes and searches for obstructions to bounded q -> 2q modular
partitions that are invisible in complete multipartite graphs.
"""

from __future__ import annotations

import argparse
import random
from functools import lru_cache
from itertools import product


def edge_bit(edges: int, classes: int, i: int, j: int) -> int:
    if i > j:
        i, j = j, i
    index = 0
    for a in range(classes):
        for b in range(a + 1, classes):
            if a == i and b == j:
                return (edges >> index) & 1
            index += 1
    raise IndexError((classes, i, j))


def degree_residues(
    counts: tuple[int, ...],
    loops: int,
    edges: int,
    modulus: int,
) -> list[int]:
    residues: list[int] = []
    classes = len(counts)
    for i, count in enumerate(counts):
        if count == 0:
            continue
        degree = ((loops >> i) & 1) * (count - 1)
        for j, other in enumerate(counts):
            if i != j and edge_bit(edges, classes, i, j):
                degree += other
        residues.append(degree % modulus)
    return residues


def is_modular(
    counts: tuple[int, ...],
    loops: int,
    edges: int,
    modulus: int,
) -> bool:
    residues = degree_residues(counts, loops, edges, modulus)
    return bool(residues) and len(set(residues)) == 1


def all_valid_bins(
    sizes: tuple[int, ...],
    loops: int,
    edges: int,
    target_modulus: int,
) -> list[tuple[int, ...]]:
    ranges = [range(size + 1) for size in sizes]
    bins = [
        counts
        for counts in product(*ranges)
        if any(counts) and is_modular(counts, loops, edges, target_modulus)
    ]
    bins.sort(key=lambda item: (sum(item), item), reverse=True)
    return bins


def can_partition(
    sizes: tuple[int, ...],
    loops: int,
    edges: int,
    target_modulus: int,
    bins: int,
) -> bool:
    choices = all_valid_bins(sizes, loops, edges, target_modulus)

    @lru_cache(maxsize=None)
    def rec(remaining: tuple[int, ...], left: int) -> bool:
        if all(value == 0 for value in remaining):
            return True
        if left == 0:
            return False
        pivot = next(i for i, value in enumerate(remaining) if value)
        for choice in choices:
            if choice[pivot] == 0:
                continue
            if all(choice[i] <= remaining[i] for i in range(len(sizes))):
                nxt = tuple(remaining[i] - choice[i] for i in range(len(sizes)))
                if rec(nxt, left - 1):
                    return True
        return False

    return rec(sizes, bins)


def min_bins(
    sizes: tuple[int, ...],
    loops: int,
    edges: int,
    target_modulus: int,
    cap: int,
) -> int | None:
    for bins in range(1, cap + 1):
        if can_partition(sizes, loops, edges, target_modulus, bins):
            return bins
    return None


def edge_count(classes: int) -> int:
    return classes * (classes - 1) // 2


def format_edges(classes: int, edges: int) -> str:
    pairs = []
    for i in range(classes):
        for j in range(i + 1, classes):
            if edge_bit(edges, classes, i, j):
                pairs.append(f"{i}-{j}")
    return ",".join(pairs) if pairs else "none"


def search(
    source_modulus: int,
    target_modulus: int,
    max_classes: int,
    max_size: int,
    cap: int,
    stop_first: bool,
    max_checked: int | None,
) -> None:
    histogram: dict[int | str, int] = {}
    worst = -1
    worst_data: tuple[tuple[int, ...], int, int] | None = None
    checked = 0
    source_modular = 0
    truncated = False
    for classes in range(1, max_classes + 1):
        for loops in range(1 << classes):
            for edges in range(1 << edge_count(classes)):
                for sizes in product(range(1, max_size + 1), repeat=classes):
                    checked += 1
                    if not is_modular(sizes, loops, edges, source_modulus):
                        continue
                    source_modular += 1
                    value = min_bins(sizes, loops, edges, target_modulus, cap)
                    key: int | str = value if value is not None else "NA"
                    histogram[key] = histogram.get(key, 0) + 1
                    numeric = cap + 1 if value is None else value
                    if numeric > worst:
                        worst = numeric
                        worst_data = (sizes, loops, edges)
                    if value is None and stop_first:
                        print_result(
                            source_modulus,
                            target_modulus,
                            max_classes,
                            max_size,
                            cap,
                            checked,
                            source_modular,
                            histogram,
                            worst,
                            worst_data,
                            truncated,
                        )
                        return
                    if max_checked is not None and checked >= max_checked:
                        truncated = True
                        break
                if truncated:
                    break
            if truncated:
                break
        if truncated:
            break

    print_result(
        source_modulus,
        target_modulus,
        max_classes,
        max_size,
        cap,
        checked,
        source_modular,
        histogram,
        worst,
        worst_data,
        truncated,
    )


def sample(
    source_modulus: int,
    target_modulus: int,
    classes: int,
    max_size: int,
    cap: int,
    samples: int,
    max_attempts: int,
    seed: int,
) -> None:
    rng = random.Random(seed)
    histogram: dict[int | str, int] = {}
    worst = -1
    worst_data: tuple[tuple[int, ...], int, int] | None = None
    accepted = 0
    attempts = 0
    while accepted < samples and attempts < max_attempts:
        attempts += 1
        loops = rng.randrange(1 << classes)
        edges = rng.randrange(1 << edge_count(classes))
        sizes = tuple(rng.randint(1, max_size) for _ in range(classes))
        if not is_modular(sizes, loops, edges, source_modulus):
            continue
        accepted += 1
        value = min_bins(sizes, loops, edges, target_modulus, cap)
        key: int | str = value if value is not None else "NA"
        histogram[key] = histogram.get(key, 0) + 1
        numeric = cap + 1 if value is None else value
        if numeric > worst:
            worst = numeric
            worst_data = (sizes, loops, edges)
        if value is None:
            break

    print(f"source_modulus={source_modulus}")
    print(f"target_modulus={target_modulus}")
    print(f"classes={classes}")
    print(f"max_size={max_size}")
    print(f"cap={cap}")
    print(f"seed={seed}")
    print(f"attempts={attempts}")
    print(f"accepted={accepted}")
    print(f"worst_value={worst if worst <= cap else 'NA'}")
    if worst_data is not None:
        sizes, loops, edges = worst_data
        print("worst_sizes=" + ",".join(map(str, sizes)))
        print(f"worst_loops={loops:b}")
        print(f"worst_edges={format_edges(len(sizes), edges)}")
    print("histogram=min_bins:count")
    for key in sorted(histogram, key=lambda item: cap + 1 if item == "NA" else item):
        print(f"  {key}: {histogram[key]}")


def print_result(
    source_modulus: int,
    target_modulus: int,
    max_classes: int,
    max_size: int,
    cap: int,
    checked: int,
    source_modular: int,
    histogram: dict[int | str, int],
    worst: int,
    worst_data: tuple[tuple[int, ...], int, int] | None,
    truncated: bool,
) -> None:
    print(f"source_modulus={source_modulus}")
    print(f"target_modulus={target_modulus}")
    print(f"max_classes={max_classes}")
    print(f"max_size={max_size}")
    print(f"cap={cap}")
    print(f"checked_models={checked}")
    print(f"source_modular_models={source_modular}")
    print(f"truncated={truncated}")
    print(f"worst_value={worst if worst <= cap else 'NA'}")
    if worst_data is not None:
        sizes, loops, edges = worst_data
        print("worst_sizes=" + ",".join(map(str, sizes)))
        print(f"worst_loops={loops:b}")
        print(f"worst_edges={format_edges(len(sizes), edges)}")
    print("histogram=min_bins:count")
    for key in sorted(histogram, key=lambda item: cap + 1 if item == "NA" else item):
        print(f"  {key}: {histogram[key]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-modulus", type=int, default=2)
    parser.add_argument("--target-modulus", type=int, default=4)
    parser.add_argument("--max-classes", type=int, default=4)
    parser.add_argument("--max-size", type=int, default=5)
    parser.add_argument("--cap", type=int, default=4)
    parser.add_argument("--stop-first", action="store_true")
    parser.add_argument(
        "--max-checked",
        type=int,
        help="stop after this many labelled blow-up models",
    )
    parser.add_argument(
        "--samples",
        type=int,
        default=0,
        help="run this many accepted random source-modular samples instead of exhaustive search",
    )
    parser.add_argument("--classes", type=int, default=5)
    parser.add_argument("--max-attempts", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    if args.samples:
        sample(
            args.source_modulus,
            args.target_modulus,
            args.classes,
            args.max_size,
            args.cap,
            args.samples,
            args.max_attempts,
            args.seed,
        )
        return
    search(
        args.source_modulus,
        args.target_modulus,
        args.max_classes,
        args.max_size,
        args.cap,
        args.stop_first,
        args.max_checked,
    )


if __name__ == "__main__":
    main()
