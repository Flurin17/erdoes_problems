#!/usr/bin/env python3
"""Inspect side spectra and cross-profile obstructions in a marked pair graph."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations

import regular_bitset


def subset_mask(vertices: tuple[int, ...]) -> int:
    out = 0
    for vertex in vertices:
        out |= 1 << vertex
    return out


def side_regular_sets(
    adj: list[int],
    vertices: tuple[int, ...],
) -> dict[int, list[tuple[int, tuple[int, ...]]]]:
    by_degree: dict[int, list[tuple[int, tuple[int, ...]]]] = {}
    for size in range(1, len(vertices) + 1):
        for choice in combinations(vertices, size):
            degree = regular_bitset.regular_degree(adj, subset_mask(choice), choice)
            if degree is not None:
                by_degree.setdefault(degree, []).append((size, choice))
    return by_degree


def cross_degrees(adj: list[int], source: tuple[int, ...], target_mask: int) -> list[int]:
    return [(adj[v] & target_mask).bit_count() for v in source]


def spread(values: list[int]) -> int:
    return max(values) - min(values) if values else 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--split", type=int, required=True)
    parser.add_argument("--h", type=int, required=True)
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    adj = regular_bitset.build_adjacency(args.n, args.mask)
    left = tuple(range(args.split))
    right = tuple(range(args.split, args.n))
    left_sets = side_regular_sets(adj, left)
    right_sets = side_regular_sets(adj, right)

    compatible = 0
    regular_unions = 0
    examples: list[str] = []
    cross_spread_histogram: Counter[int] = Counter()
    side_spread_histogram: Counter[tuple[int, int]] = Counter()
    min_cross_spread: int | None = None
    min_side_spread: tuple[int, int] | None = None
    min_spread_examples: list[str] = []
    for degree in sorted(left_sets.keys() & right_sets.keys()):
        for left_size, left_choice in left_sets[degree]:
            for right_size, right_choice in right_sets[degree]:
                if left_size + right_size < args.h:
                    continue
                compatible += 1
                left_mask = subset_mask(left_choice)
                right_mask = subset_mask(right_choice)
                union = tuple(sorted(left_choice + right_choice))
                union_degree = regular_bitset.regular_degree(adj, left_mask | right_mask, union)
                if union_degree is not None:
                    regular_unions += 1
                    continue

                left_cross = cross_degrees(adj, left_choice, right_mask)
                right_cross = cross_degrees(adj, right_choice, left_mask)
                all_cross = left_cross + right_cross
                pair_spread = spread(all_cross)
                left_spread = spread(left_cross)
                right_spread = spread(right_cross)
                cross_spread_histogram[pair_spread] += 1
                side_spread_histogram[(left_spread, right_spread)] += 1
                example = (
                    f"degree={degree} left={','.join(map(str,left_choice))} "
                    f"right={','.join(map(str,right_choice))} "
                    f"left_cross={left_cross} right_cross={right_cross} "
                    f"cross_spread={pair_spread}"
                )
                if len(examples) < args.limit:
                    examples.append(example)
                if min_cross_spread is None or pair_spread < min_cross_spread:
                    min_cross_spread = pair_spread
                    min_side_spread = (left_spread, right_spread)
                    min_spread_examples = []
                if pair_spread == min_cross_spread and len(min_spread_examples) < args.limit:
                    min_spread_examples.append(example)

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"split={args.split}")
    print(f"h={args.h}")
    print(f"side_compatible_pairs={compatible}")
    print(f"regular_unions={regular_unions}")
    print(f"blocked_pairs={compatible - regular_unions}")
    print(f"blocked_cross_spread_histogram={dict(sorted(cross_spread_histogram.items()))}")
    print(f"blocked_side_spread_histogram={dict(sorted(side_spread_histogram.items()))}")
    print(f"min_blocked_cross_spread={min_cross_spread}")
    print(f"min_blocked_side_spread={min_side_spread}")
    print("left_spectrum=" + " ".join(
        f"{degree}:{max(size for size, _choice in sets)}" for degree, sets in sorted(left_sets.items())
    ))
    print("right_spectrum=" + " ".join(
        f"{degree}:{max(size for size, _choice in sets)}" for degree, sets in sorted(right_sets.items())
    ))
    for example in examples:
        print("blocked_pair=" + example)
    for example in min_spread_examples:
        print("min_spread_blocked_pair=" + example)


if __name__ == "__main__":
    main()
