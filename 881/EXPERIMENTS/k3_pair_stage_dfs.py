#!/usr/bin/env python3
"""Bounded DFS for general k=3 cross-stage pair stages.

This removes the modulo-10 booster restriction from
``robust_booster_pair_stage_search.py``.  A stage must:

* extend 3-sum coverage with the two-point buffer from Lemma 13.1d;
* pass the new-block frontier test from Lemma 13.1d.1;
* give every old-new pair a local 4-sum witness below the declared endpoint.

The search is intentionally small and diagnostic.  It is not a proof of
existence or nonexistence of stages.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from itertools import combinations


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def cover_end(values: set[int], start: int, cap: int) -> int:
    x = start
    while x <= cap and x in values:
        x += 1
    return x - 1


def pair_witnesses(
    old: set[int],
    new: set[int],
    previous_endpoint: int,
    declared_endpoint: int,
    cap: int,
) -> dict[tuple[int, int], list[int]] | None:
    elements = old | new
    four_all = hsum(elements, 4, cap)
    result: dict[tuple[int, int], list[int]] = {}
    for a in sorted(old):
        for b in sorted(new):
            without = hsum(elements - {a, b}, 4, cap)
            found = [
                w
                for w in range(previous_endpoint + 1, declared_endpoint + 1)
                if w in four_all and w not in without
            ]
            if not found:
                return None
            result[(a, b)] = found[:3]
    return result


def bootstraps_from_old(old: set[int], new_tuple: tuple[int, ...]) -> bool:
    """Return whether each new point is 3-covered by old plus earlier new."""

    current = set(old)
    for point in new_tuple:
        if point not in hsum(current, 3, point):
            return False
        current.add(point)
    return True


@dataclass(frozen=True)
class Stage:
    old: tuple[int, ...]
    new: tuple[int, ...]
    endpoint: int
    coverage: int
    oldcov: int
    witnesses: tuple[tuple[tuple[int, int], tuple[int, ...]], ...]


def extensions(
    old: set[int],
    endpoint: int,
    base: int,
    slack: int,
    max_new_size: int,
    max_candidate: int,
) -> list[Stage]:
    cap0 = max(5 * max(old) + 120, endpoint + 120)
    oldcov = cover_end(hsum(old, 3, cap0), base, cap0)
    candidates = [
        x
        for x in range(endpoint + 1, min(max_candidate, oldcov + slack) + 1)
        if x not in old
    ]
    out: list[Stage] = []
    for size in range(1, max_new_size + 1):
        for new_tuple in combinations(candidates, size):
            if not bootstraps_from_old(old, new_tuple):
                continue
            new = set(new_tuple)
            elements = old | new
            cap = max(5 * max(elements) + 180, oldcov + slack + 180)
            newcov = cover_end(hsum(elements, 3, cap), base, cap)
            last_declared = newcov - 2 * min(elements)
            if last_declared < max(endpoint + 1, max(new)):
                continue
            for declared in range(max(endpoint + 1, max(new)), last_declared + 1):
                witnesses = pair_witnesses(old, new, endpoint, declared, cap)
                if witnesses is None:
                    continue
                out.append(
                    Stage(
                        old=tuple(sorted(old)),
                        new=tuple(sorted(new)),
                        endpoint=declared,
                        coverage=newcov,
                        oldcov=oldcov,
                        witnesses=tuple(
                            (pair, tuple(values))
                            for pair, values in sorted(witnesses.items())
                        ),
                    )
                )
                break
    out.sort(key=lambda stage: (stage.endpoint, len(stage.new), stage.new))
    return out


def search(
    start: set[int],
    base: int,
    endpoint: int,
    depth: int = 4,
    slack: int = 28,
    max_new_size: int = 2,
    max_candidate: int = 55,
    branch_limit: int = 50,
) -> None:
    best: list[Stage] = []
    seen: set[tuple[tuple[int, ...], int]] = set()

    def dfs(old: set[int], current_endpoint: int, chain: list[Stage]) -> bool:
        nonlocal best
        if len(chain) > len(best):
            best = list(chain)
            print("best depth", len(best), flush=True)
            for stage in best:
                print(
                    "  old=",
                    list(stage.old),
                    "new=",
                    list(stage.new),
                    "endpoint=",
                    stage.endpoint,
                    "oldcov=",
                    stage.oldcov,
                    "coverage=",
                    stage.coverage,
                    "sample=",
                    list(stage.witnesses)[:4],
                    flush=True,
                )
        if len(chain) >= depth:
            return True
        key = (tuple(sorted(old)), current_endpoint)
        if key in seen:
            return False
        seen.add(key)
        found = extensions(
            old,
            current_endpoint,
            base,
            slack,
            max_new_size,
            max_candidate,
        )
        for stage in found[:branch_limit]:
            if dfs(old | set(stage.new), stage.endpoint, [*chain, stage]):
                return True
        return False

    dfs(set(start), endpoint, [])
    print("done best", len(best))


if __name__ == "__main__":
    if "--depth5" in sys.argv:
        search(
            {1, 2, 3},
            base=3,
            endpoint=3,
            depth=5,
            slack=40,
            max_new_size=2,
            max_candidate=90,
            branch_limit=300,
        )
        raise SystemExit

    for start, base, endpoint in [
        ({1, 2, 3}, 3, 3),
        ({1, 2, 3, 4}, 3, 4),
        ({1, 2, 3, 6}, 3, 7),
    ]:
        print("start", sorted(start), "base", base, "endpoint", endpoint)
        search(start, base, endpoint)
