#!/usr/bin/env python3
"""Random finite interval tests for one-point deletion.

For finite A subset [1,N], treat A as a finite h-basis above a cutoff if hA
covers [cutoff,N]. Search random examples where 2A covers a long tail and
many one-point deletions fail to cover the same tail at order 3.

This is only a heuristic finite analogue. The infinite problem is sensitive
to thresholds and future elements.
"""

from __future__ import annotations

import random


def bounded_hsum(A: set[int], h: int, limit: int) -> set[int]:
    out = {0}
    for _ in range(h):
        out = {x + y for x in out for y in A if x + y <= limit}
    return out


def covers_tail(A: set[int], h: int, cutoff: int, limit: int) -> bool:
    sums = bounded_hsum(A, h, limit)
    return all(n in sums for n in range(cutoff, limit + 1))


def trial(limit: int, cutoff: int, density: float) -> tuple[set[int], list[int]] | None:
    A = {x for x in range(1, limit + 1) if random.random() < density}
    if not covers_tail(A, 2, cutoff, limit):
        return None
    bad = [a for a in sorted(A) if not covers_tail(A - {a}, 3, cutoff, limit)]
    return A, bad


def main(limit: int = 120, cutoff: int = 70, trials: int = 5_000) -> None:
    random.seed(881)
    best: tuple[int, int, set[int], list[int]] | None = None
    for _ in range(trials):
        density = random.uniform(0.08, 0.35)
        result = trial(limit, cutoff, density)
        if result is None:
            continue
        A, bad = result
        score = (len(bad), -len(A))
        if best is None or score > (best[0], best[1]):
            best = (len(bad), -len(A), A, bad)
    if best is None:
        print("no finite 2-basis samples found")
        return
    bad_count, neg_size, A, bad = best
    print(
        f"limit={limit} cutoff={cutoff} |A|={len(A)} "
        f"bad_one_point_deletions={bad_count}"
    )
    print(f"A={sorted(A)}")
    print(f"bad={bad}")


if __name__ == "__main__":
    main()
