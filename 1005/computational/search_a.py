#!/usr/bin/env python3
"""Exact search A for Erdős problem 1005.

The primary implementation streams the standard Farey-successor recurrence and
finds every longest contiguous pairwise-compatible block using a sliding window.
An independent enumerative Farey generator and a direct quadratic checker are
used for self-tests on small orders.

Examples:
    python3 search_a.py --self-test 60
    python3 search_a.py --range 4 2000 --step 1 --output search_a.tsv
    python3 search_a.py --orders 100 200 500 1000 --show-maximizers
"""

from __future__ import annotations

import argparse
import heapq
import math
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Iterator, Sequence


Point = tuple[int, int]


def farey_recurrence(n: int) -> Iterator[Point]:
    """Yield F_n from 0/1 through 1/1 by the exact successor recurrence."""
    if n < 1:
        raise ValueError("Farey order must be positive")
    a, b = 0, 1
    c, d = 1, n
    yield a, b
    while True:
        yield c, d
        if c == 1 and d == 1:
            return
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b


def farey_enumerative(n: int) -> list[Point]:
    """Independent reference generator: enumerate reduced fractions and sort."""
    if n < 1:
        raise ValueError("Farey order must be positive")
    points = [(0, 1)]
    for b in range(1, n + 1):
        for a in range(1, b + 1):
            if math.gcd(a, b) == 1:
                points.append((a, b))
    points.sort(key=lambda p: Fraction(p[0], p[1]))
    return points


def compatible(p: Point, q: Point) -> bool:
    return (p[0] - q[0]) * (p[1] - q[1]) >= 0


class RangeMaximum:
    """Iterative segment tree for point assignment and half-open range maximum."""

    def __init__(self, size: int) -> None:
        width = 1
        while width < size:
            width <<= 1
        self.width = width
        self.data = [-1] * (2 * width)

    def assign(self, pos: int, value: int) -> None:
        i = pos + self.width
        self.data[i] = value
        i >>= 1
        while i:
            new = max(self.data[2 * i], self.data[2 * i + 1])
            if self.data[i] == new:
                # Ancestors cannot change once this node's value is unchanged.
                break
            self.data[i] = new
            i >>= 1

    def query(self, lo: int, hi: int) -> int:
        """Return max on lo <= pos < hi, or -1 for an empty interval."""
        if lo >= hi:
            return -1
        lo += self.width
        hi += self.width
        answer = -1
        while lo < hi:
            if lo & 1:
                answer = max(answer, self.data[lo])
                lo += 1
            if hi & 1:
                hi -= 1
                answer = max(answer, self.data[hi])
            lo >>= 1
            hi >>= 1
        return answer


@dataclass(frozen=True)
class Maximizer:
    start_index: int
    end_index: int
    start: Point
    end: Point

    @property
    def cardinality(self) -> int:
        return self.end_index - self.start_index + 1

    @property
    def span(self) -> int:
        return self.end_index - self.start_index


@dataclass(frozen=True)
class SearchResult:
    n: int
    farey_cardinality: int
    maximum_cardinality: int
    maximizers: tuple[Maximizer, ...]

    @property
    def maximum_span(self) -> int:
        return self.maximum_cardinality - 1


def longest_blocks_streaming(n: int) -> SearchResult:
    """Find all maximum blocks exactly in O(|F_n| log n) time and O(|F_n|) space.

    At the start of each iteration, the active deque is the unique longest
    suffix of the processed prefix that is pairwise compatible.  For every
    numerator a, heaps[a] stores (-denominator,index), lazily discarding points
    left of the active window; the range tree stores its active maximum
    denominator.  A new (c,d) conflicts precisely with an active point having
    numerator < c and denominator > d.
    """
    from collections import deque

    tree = RangeMaximum(n + 1)
    heaps: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    active: deque[tuple[int, int, int]] = deque()
    left = 0
    best = 0
    maximizers: list[Maximizer] = []

    for index, (a, b) in enumerate(farey_recurrence(n)):
        while tree.query(0, a) > b:
            old_index, old_a, _old_b = active.popleft()
            assert old_index == left
            left += 1
            heap = heaps[old_a]
            while heap and heap[0][1] < left:
                heapq.heappop(heap)
            tree.assign(old_a, -heap[0][0] if heap else -1)

        heapq.heappush(heaps[a], (-b, index))
        tree.assign(a, -heaps[a][0][0])
        active.append((index, a, b))

        card = index - left + 1
        if card >= best:
            candidate = Maximizer(left, index, (active[0][1], active[0][2]), (a, b))
            if card > best:
                best = card
                maximizers.clear()
            maximizers.append(candidate)

    farey_cardinality = index + 1
    return SearchResult(n, farey_cardinality, best, tuple(maximizers))


def longest_blocks_bruteforce(points: Sequence[Point]) -> tuple[int, list[tuple[int, int]]]:
    """Independent direct checker, quadratic in the Farey-sequence length."""
    best = 0
    maximizers: list[tuple[int, int]] = []
    for start in range(len(points)):
        for end in range(start, len(points)):
            if any(not compatible(points[i], points[end]) for i in range(start, end)):
                break
            card = end - start + 1
            if card > best:
                best = card
                maximizers = [(start, end)]
            elif card == best:
                maximizers.append((start, end))
    return best, maximizers


def validate_recurrence(n: int, points: Sequence[Point]) -> None:
    assert points[0] == (0, 1) and points[-1] == (1, 1)
    assert len(points) == 1 + sum(
        1 for b in range(1, n + 1) for a in range(1, b + 1) if math.gcd(a, b) == 1
    )
    for i, (a, b) in enumerate(points):
        assert 0 <= a <= b <= n
        assert math.gcd(a, b) == 1
        if i:
            c, d = points[i - 1]
            assert c * b < a * d
            assert a * d - c * b == 1
            assert b + d > n


def self_test(limit: int) -> None:
    for n in range(1, limit + 1):
        recurrence = list(farey_recurrence(n))
        enumeration = farey_enumerative(n)
        assert recurrence == enumeration, (n, recurrence, enumeration)
        validate_recurrence(n, recurrence)
        fast = longest_blocks_streaming(n)
        brute_best, brute_pairs = longest_blocks_bruteforce(enumeration)
        fast_pairs = [(m.start_index, m.end_index) for m in fast.maximizers]
        assert fast.maximum_cardinality == brute_best, (n, fast, brute_best)
        assert fast_pairs == brute_pairs, (n, fast_pairs, brute_pairs)
    print(f"self-test passed for every 1 <= n <= {limit}", file=sys.stderr)


def render_point(p: Point) -> str:
    return f"{p[0]}/{p[1]}"


def result_row(result: SearchResult) -> str:
    encoded = ";".join(
        f"{m.start_index}:{m.end_index}:{render_point(m.start)}:{render_point(m.end)}"
        for m in result.maximizers
    )
    return "\t".join(
        map(
            str,
            (
                result.n,
                result.farey_cardinality,
                result.maximum_cardinality,
                result.maximum_span,
                len(result.maximizers),
                encoded,
            ),
        )
    )


def selected_orders(args: argparse.Namespace) -> Iterable[int]:
    if args.orders:
        yield from args.orders
    if args.range:
        lo, hi = args.range
        yield from range(lo, hi + 1, args.step)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", type=int, metavar="N")
    parser.add_argument("--orders", nargs="*", type=int, default=[])
    parser.add_argument("--range", nargs=2, type=int, metavar=("LO", "HI"))
    parser.add_argument("--step", type=int, default=1)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--show-maximizers", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.self_test is not None:
        self_test(args.self_test)
    orders = list(selected_orders(args))
    if not orders:
        return
    if any(n < 1 for n in orders):
        raise SystemExit("all Farey orders must be positive")

    header = "n\t|F_n|\tmax_cardinality\tmax_span\tnumber_of_maximizers\tmaximizers"
    rows = [header]
    started = time.perf_counter()
    for n in orders:
        result = longest_blocks_streaming(n)
        row = result_row(result)
        rows.append(row)
        if args.show_maximizers:
            print(row)
    elapsed = time.perf_counter() - started
    if args.output:
        args.output.write_text("\n".join(rows) + "\n", encoding="utf-8")
    elif not args.show_maximizers:
        print("\n".join(rows))
    print(f"computed {len(orders)} order(s) in {elapsed:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()
