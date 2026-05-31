#!/usr/bin/env python3
"""Search for efficient finite blocks for the k=2 counterexample route.

A block T is scored by:

  * a long interval [L,U] contained in T+T;
  * for every t in T, a witness w in [L,U] such that w has a two-sum
    representation using t, and w-e is not in T+T for all earlier shifts e.

The condition is only a local proxy. A real infinite construction would
also have to handle two earlier summands, later blocks, and exact thresholds.
"""

from __future__ import annotations

from collections import defaultdict
import random


def pair_sums(T: set[int]) -> dict[int, list[tuple[int, int]]]:
    values = sorted(T)
    out: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for i, a in enumerate(values):
        for b in values[i:]:
            out[a + b].append((a, b))
    return out


def intervals(values: set[int]) -> list[tuple[int, int]]:
    if not values:
        return []
    ordered = sorted(values)
    out = []
    start = prev = ordered[0]
    for value in ordered[1:]:
        if value == prev + 1:
            prev = value
        else:
            out.append((start, prev))
            start = prev = value
    out.append((start, prev))
    return out


def best_block_score(T: set[int], earlier: set[int]) -> tuple[int, int, int] | None:
    sums = pair_sums(T)
    sum_values = set(sums)
    best: tuple[int, int, int] | None = None
    for L, U in intervals(sum_values):
        max_witness = -1
        ok = True
        for t in T:
            witnesses = [
                w
                for w, reps in sums.items()
                if L <= w <= U
                and any(t in rep for rep in reps)
                and all((w - e) not in sum_values for e in earlier)
            ]
            if not witnesses:
                ok = False
                break
            max_witness = max(max_witness, min(witnesses))
        if not ok:
            continue
        score = (U - max_witness, U - L + 1, -len(T))
        if best is None or score > best:
            best = score
    return best


def random_search(diameter: int = 80, trials: int = 10_000) -> None:
    random.seed(881)
    earlier = {1, 2, 3}
    best: tuple[tuple[int, int, int], set[int]] | None = None
    for _ in range(trials):
        density = random.uniform(0.08, 0.35)
        T = {0, diameter}
        T.update(x for x in range(1, diameter) if random.random() < density)
        score = best_block_score(T, earlier)
        if score is not None and (best is None or score > best[0]):
            best = (score, T)
    if best is None:
        print(f"no block found for diameter={diameter}, earlier={sorted(earlier)}")
        return
    score, T = best
    print(f"diameter={diameter} earlier={sorted(earlier)} score={score}")
    print(f"T={sorted(T)}")


if __name__ == "__main__":
    random_search()
