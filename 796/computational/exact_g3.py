#!/usr/bin/env python3
"""Deterministic exact solver for g_3(n).

The forbidden hyperedges are the six-element unions of three distinct
factor-pairs of one product.  An admissible set is exactly an independent
set in this hypergraph.  The recursive solver chooses a contained hyperedge;
every independent subset must omit at least one of its six vertices, so the
six branches are exhaustive.

For small n, a logically independent scan of every subset checks the answer.
Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import functools
import itertools
import time
from collections import Counter, defaultdict
from typing import Dict, Iterable, List, Sequence, Tuple


def values(mask: int) -> Tuple[int, ...]:
    return tuple(i + 1 for i in range(mask.bit_length()) if mask & (1 << i))


def admissible_direct(mask: int) -> bool:
    counts = Counter(a * b for a, b in itertools.combinations(values(mask), 2))
    return max(counts.values(), default=0) <= 2


def forbidden_hyperedges(n: int) -> Tuple[int, ...]:
    fibers: Dict[int, List[int]] = defaultdict(list)
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            pair = (1 << (a - 1)) | (1 << (b - 1))
            fibers[a * b].append(pair)

    edges = set()
    for pairs in fibers.values():
        for triple in itertools.combinations(pairs, 3):
            edge = triple[0] | triple[1] | triple[2]
            # Equal-product pairs are matchings, so every witness has 6 points.
            if edge.bit_count() != 6:
                raise AssertionError("factor-pair overlap invariant failed")
            edges.add(edge)
    return tuple(sorted(edges))


def exact_independence(n: int) -> Tuple[int, int, int]:
    edges = forbidden_hyperedges(n)
    full = (1 << n) - 1
    calls = 0

    @functools.lru_cache(maxsize=None)
    def solve(mask: int) -> Tuple[int, int]:
        nonlocal calls
        calls += 1
        edge = next((edge for edge in edges if mask & edge == edge), None)
        if edge is None:
            return mask.bit_count(), mask

        best_size = -1
        best_mask = 0
        remaining = edge
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            size, candidate = solve(mask ^ bit)
            if size > best_size or (size == best_size and candidate < best_mask):
                best_size, best_mask = size, candidate
        return best_size, best_mask

    size, mask = solve(full)
    if not admissible_direct(mask):
        raise AssertionError("reported extremal set is not admissible")
    return size, mask, calls


def exhaustive_independence(n: int) -> Tuple[int, int]:
    best_size = -1
    best_mask = 0
    for mask in range(1 << n):
        size = mask.bit_count()
        if size < best_size:
            continue
        if admissible_direct(mask):
            if size > best_size or mask < best_mask:
                best_size, best_mask = size, mask
    return best_size, best_mask


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-n", type=int, default=1)
    parser.add_argument("--max-n", type=int, default=30)
    parser.add_argument(
        "--bruteforce-through",
        type=int,
        default=14,
        help="independently scan all subsets through this n",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 1 <= args.min_n <= args.max_n:
        raise SystemExit("require 1 <= min-n <= max-n")
    if args.max_n > 63:
        raise SystemExit("this bit-mask implementation is limited to n <= 63")

    total_start = time.perf_counter()
    previous = 0
    for n in range(args.min_n, args.max_n + 1):
        start = time.perf_counter()
        size, mask, calls = exact_independence(n)
        if not previous <= size <= previous + 1 and n > args.min_n:
            raise AssertionError("monotonicity/increment invariant failed")
        previous = size

        brute = ""
        if n <= args.bruteforce_through:
            brute_size, _ = exhaustive_independence(n)
            if brute_size != size:
                raise AssertionError(
                    f"branch solver gives {size}, brute force gives {brute_size}"
                )
            brute = " brute_force=PASS"

        edges = len(forbidden_hyperedges(n))
        elapsed = time.perf_counter() - start
        print(
            f"n={n:2d} g3={size:2d} forbidden_edges={edges:5d} "
            f"states={calls:7d} runtime={elapsed:.6f}s{brute} "
            f"A={values(mask)}"
        )
    print(f"total_runtime={time.perf_counter()-total_start:.6f}s")


if __name__ == "__main__":
    main()
