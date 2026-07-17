#!/usr/bin/env python3
"""Independent exact search for Erdos problem 1005.

This implementation deliberately does not use the Farey-neighbour recurrence.
It enumerates all coprime (a,b), sorts by exact cross multiplication, and tests
the displayed product inequality.  A two-dimensional Fenwick tree finds the
latest incompatible earlier fraction exactly.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from array import array
from functools import cmp_to_key


def fraction_cmp(x: tuple[int, int], y: tuple[int, int]) -> int:
    z = x[0] * y[1] - y[0] * x[1]
    return (z > 0) - (z < 0)


def farey_by_enumeration(n: int, left: bool = True, right: bool = True):
    """Enumerate and exactly sort reduced fractions in [0,1]."""
    f = []
    for b in range(1, n + 1):
        for a in range(0, b + 1):
            if math.gcd(a, b) == 1:
                if (a == 0 and not left) or (a == b and not right):
                    continue
                f.append((a, b))
    f.sort(key=cmp_to_key(fraction_cmp))
    assert len(f) == len(set(f))
    assert all(fraction_cmp(f[i], f[i + 1]) < 0 for i in range(len(f) - 1))
    return f


class Fenwick2DMax:
    """Point-update/prefix-rectangle-maximum Fenwick tree."""

    def __init__(self, size: int):
        self.size = size
        self.t = [array("i", [-1]) * (size + 1) for _ in range(size + 1)]

    def update(self, x: int, y: int, value: int) -> None:
        size, t = self.size, self.t
        xx = x
        while xx <= size:
            row = t[xx]
            yy = y
            while yy <= size:
                if value > row[yy]:
                    row[yy] = value
                yy += yy & -yy
            xx += xx & -xx

    def query(self, x: int, y: int) -> int:
        """Maximum over 1 <= x' <= x, 1 <= y' <= y."""
        ans, t = -1, self.t
        xx = x
        while xx > 0:
            row = t[xx]
            yy = y
            while yy > 0:
                if row[yy] > ans:
                    ans = row[yy]
                yy -= yy & -yy
            xx -= xx & -xx
        return ans


def compatible(x: tuple[int, int], y: tuple[int, int]) -> bool:
    return (x[0] - y[0]) * (x[1] - y[1]) >= 0


def extremum_fast(fractions: list[tuple[int, int]], n: int):
    """Return maximum cardinality, all maximizing intervals, universal span.

    If j is the new right endpoint, an earlier i is incompatible exactly when
    a_i < a_j and b_i > b_j.  With y=n+1-b, this is a prefix rectangle.
    """
    bit = Fenwick2DMax(n + 1)
    start = 0
    best_card = 0
    maximizers: list[tuple[int, int]] = []
    nearest_bad_distance = None

    for j, (a, b) in enumerate(fractions):
        latest_bad = bit.query(a, n - b)
        if latest_bad >= 0:
            distance = j - latest_bad
            if nearest_bad_distance is None or distance < nearest_bad_distance:
                nearest_bad_distance = distance
            start = max(start, latest_bad + 1)
        card = j - start + 1
        if card > best_card:
            best_card = card
            maximizers = [(start, j)]
        elif card == best_card:
            maximizers.append((start, j))
        bit.update(a + 1, n + 1 - b, j)

    universal_span = (
        len(fractions) - 1
        if nearest_bad_distance is None
        else nearest_bad_distance - 1
    )
    for lo, hi in maximizers:
        assert all(
            compatible(fractions[i], fractions[j])
            for i in range(lo, hi + 1)
            for j in range(i + 1, hi + 1)
        )
    return best_card, maximizers, universal_span


def extremum_naive(fractions: list[tuple[int, int]]):
    """Direct product-test implementation used only as an independent oracle."""
    best_card = 0
    maximizers = []
    nearest_bad_distance = None
    for lo in range(len(fractions)):
        for hi in range(lo, len(fractions)):
            if all(compatible(fractions[i], fractions[hi]) for i in range(lo, hi)):
                card = hi - lo + 1
                if card > best_card:
                    best_card, maximizers = card, [(lo, hi)]
                elif card == best_card:
                    maximizers.append((lo, hi))
            else:
                break
        for hi in range(lo + 1, len(fractions)):
            if not compatible(fractions[lo], fractions[hi]):
                d = hi - lo
                if nearest_bad_distance is None or d < nearest_bad_distance:
                    nearest_bad_distance = d
    universal_span = (
        len(fractions) - 1
        if nearest_bad_distance is None
        else nearest_bad_distance - 1
    )
    return best_card, maximizers, universal_span


def format_result(n: int, left: bool, right: bool, fractions, result, elapsed):
    best_card, maximizers, universal_span = result
    return {
        "n": n,
        "include_0/1": left,
        "include_1/1": right,
        "fraction_count": len(fractions),
        "best_cardinality": best_card,
        "best_span": best_card - 1,
        "ratio_span_over_n": (best_card - 1) / n,
        "literal_universal_span": universal_span,
        "maximizers": [
            {
                "indices_0_based": [lo, hi],
                "left": f"{fractions[lo][0]}/{fractions[lo][1]}",
                "right": f"{fractions[hi][0]}/{fractions[hi][1]}",
            }
            for lo, hi in maximizers
        ],
        "elapsed_seconds": round(elapsed, 6),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--max-n", type=int, default=200)
    p.add_argument("--min-n", type=int, default=4)
    p.add_argument("--step", type=int, default=1)
    p.add_argument("--verify-up-to", type=int, default=18)
    p.add_argument(
        "--endpoint-modes",
        action="store_true",
        help="compute all four choices of including/excluding 0/1 and 1/1",
    )
    p.add_argument("--only-records", action="store_true")
    args = p.parse_args()

    modes = [(True, True)]
    if args.endpoint_modes:
        modes = [(l, r) for l in (True, False) for r in (True, False)]

    old_best = {mode: -1 for mode in modes}
    for n in range(args.min_n, args.max_n + 1, args.step):
        for mode in modes:
            t0 = time.perf_counter()
            fractions = farey_by_enumeration(n, *mode)
            result = extremum_fast(fractions, n)
            elapsed = time.perf_counter() - t0
            if n <= args.verify_up_to:
                naive = extremum_naive(fractions)
                assert result == naive, (n, mode, result, naive)
            if not args.only_records or result[0] > old_best[mode]:
                print(json.dumps(format_result(n, *mode, fractions, result, elapsed)))
            old_best[mode] = max(old_best[mode], result[0])


if __name__ == "__main__":
    main()
