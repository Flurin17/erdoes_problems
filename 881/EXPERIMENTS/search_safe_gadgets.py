#!/usr/bin/env python3
"""Random finite search for private sums safe against earlier shifts.

For a shifted block M+T and an earlier retained element e, a two-sum witness
2M+u can be repaired as e + (2M+u-e) whenever u-e lies in T+T. More generally
we can test safety against a finite forbidden shift set E.

This script looks for T subset [0,D] such that:

  * T+T contains a long interval;
  * every t in T has a unique two-sum u using t;
  * u-e is not in T+T for every e in E.

This is still only a local condition. A true infinite construction would
also need to control one-current plus two-previous repairs and arrange the
coverage intervals with no gaps.
"""

from __future__ import annotations

from collections import defaultdict
import random


def pair_sums(tset: set[int]) -> dict[int, list[tuple[int, int]]]:
    values = sorted(tset)
    sums: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for i, a in enumerate(values):
        for b in values[i:]:
            if len(sums[a + b]) < 3:
                sums[a + b].append((a, b))
    return sums


def longest_interval(values: set[int]) -> tuple[int, int, int]:
    if not values:
        return (0, 0, -1)
    ordered = sorted(values)
    best_len = 1
    best_start = ordered[0]
    start = ordered[0]
    prev = ordered[0]
    current_len = 1
    for value in ordered[1:]:
        if value == prev + 1:
            current_len += 1
        else:
            if current_len > best_len:
                best_len = current_len
                best_start = start
            start = value
            current_len = 1
        prev = value
    if current_len > best_len:
        best_len = current_len
        best_start = start
    return (best_len, best_start, best_start + best_len - 1)


def safe_private_count(tset: set[int], forbidden: set[int]) -> tuple[int, dict[int, list[int]]]:
    sums = pair_sums(tset)
    sum_values = set(sums)
    witnesses: dict[int, list[int]] = {}
    for t in sorted(tset):
        good = []
        for u, reps in sums.items():
            if len(reps) != 1 or t not in reps[0]:
                continue
            if all((u - e) not in sum_values for e in forbidden):
                good.append(u)
        if good:
            witnesses[t] = sorted(good)
    return len(witnesses), witnesses


def random_search(
    dmax: int = 80,
    trials: int = 50_000,
    forbidden: set[int] | None = None,
) -> None:
    forbidden = forbidden or {1}
    best: tuple[int, int, int, set[int], dict[int, list[int]]] | None = None
    for _ in range(trials):
        density = random.uniform(0.12, 0.45)
        tset = {0, dmax}
        for x in range(1, dmax):
            if random.random() < density:
                tset.add(x)
        interval = longest_interval(set(pair_sums(tset)))
        safe_count, witnesses = safe_private_count(tset, forbidden)
        score = (safe_count, interval[0], -len(tset))
        if best is None or score > (best[0], best[1], best[2]):
            best = (safe_count, interval[0], -len(tset), set(tset), witnesses)
        if safe_count == len(tset) and interval[0] >= dmax // 2:
            print(f"D={dmax} forbidden={sorted(forbidden)}")
            print(f"T={sorted(tset)}")
            print(f"longest_interval={interval}")
            for t in sorted(tset):
                print(f"  t={t}: safe private sums {witnesses[t][:5]}")
            return
    assert best is not None
    safe_count, interval_len, neg_size, tset, witnesses = best
    print(
        f"best D={dmax} forbidden={sorted(forbidden)} "
        f"safe={safe_count}/{len(tset)} longest_interval={interval_len}"
    )
    print(f"T={sorted(tset)}")


if __name__ == "__main__":
    random.seed(881)
    random_search(dmax=20, trials=20_000, forbidden={1})
