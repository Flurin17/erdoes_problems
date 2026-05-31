#!/usr/bin/env python3
"""Depth-first search for k=2 cross-stage pair-barrier chains.

The greedy search in ``cross_stage_pair_search.py`` finds a short chain and
then stalls. This script explores alternative early stages within bounded
parameters. It is only a finite diagnostic for Proposition 13.1c in
``PROOF.md``.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def cover_end(elements: set[int], start: int, cap: int) -> int:
    two_sums = hsum(elements, 2, cap)
    x = start
    while x <= cap and x in two_sums:
        x += 1
    return x - 1


def pair_witnesses(
    old: set[int],
    new: set[int],
    previous_endpoint: int,
    declared_endpoint: int,
    cap: int,
) -> dict[tuple[int, int], int] | None:
    elements = old | new
    two_sums = hsum(elements, 2, cap)
    witnesses: dict[tuple[int, int], int] = {}
    for a in sorted(old):
        for b in sorted(new):
            without = hsum(elements - {a, b}, 3, cap)
            found = next(
                (
                    w
                    for w in range(previous_endpoint + 1, declared_endpoint + 1)
                    if w in two_sums and w not in without
                ),
                None,
            )
            if found is None:
                return None
            witnesses[(a, b)] = found
    return witnesses


@dataclass(frozen=True)
class Stage:
    old: tuple[int, ...]
    new: tuple[int, ...]
    endpoint: int
    coverage: int
    witnesses: tuple[tuple[tuple[int, int], int], ...]


def extensions(
    old: set[int],
    endpoint: int,
    base: int,
    slack: int,
    max_new_size: int,
    max_candidate: int,
) -> list[Stage]:
    oldcov = cover_end(old, base, max(500, 4 * max(old) + 200))
    hi = min(max_candidate, oldcov + slack)
    candidates = [x for x in range(endpoint + 1, hi + 1) if x not in old]
    out: list[Stage] = []
    for size in range(1, max_new_size + 1):
        for new_tuple in combinations(candidates, size):
            new = set(new_tuple)
            elements = old | new
            cap = max(500, 4 * max(elements) + 200, oldcov + slack + 200)
            newcov = cover_end(elements, base, cap)
            if newcov <= endpoint:
                continue
            first_declared = max(endpoint + 1, max(new))
            for declared in range(first_declared, newcov + 1):
                witnesses = pair_witnesses(old, new, endpoint, declared, cap)
                if witnesses is None:
                    continue
                out.append(
                    Stage(
                        old=tuple(sorted(old)),
                        new=tuple(sorted(new)),
                        endpoint=declared,
                        coverage=newcov,
                        witnesses=tuple(sorted(witnesses.items())),
                    )
                )
                break
    out.sort(key=lambda s: (s.endpoint, len(s.new), s.new))
    return out


def search(
    depth: int = 4,
    slack: int = 20,
    max_new_size: int = 3,
    max_candidate: int = 30,
    branch_limit: int = 80,
) -> None:
    base = 2
    best: list[Stage] = []
    seen: set[tuple[tuple[int, ...], int]] = set()

    def dfs(old: set[int], endpoint: int, chain: list[Stage]) -> bool:
        nonlocal best
        if len(chain) > len(best):
            best = list(chain)
            print("best depth", len(best))
            for stage in best:
                print(
                    "  old=", list(stage.old),
                    "new=", list(stage.new),
                    "endpoint=", stage.endpoint,
                    "coverage=", stage.coverage,
                    "sample=", list(stage.witnesses)[:4],
                )
        if len(chain) >= depth:
            return True
        key = (tuple(sorted(old)), endpoint)
        if key in seen:
            return False
        seen.add(key)
        found = extensions(old, endpoint, base, slack, max_new_size, max_candidate)
        for stage in found[:branch_limit]:
            next_old = set(old) | set(stage.new)
            if dfs(next_old, stage.endpoint, [*chain, stage]):
                return True
        return False

    dfs({1, 2}, 2, [])
    if len(best) < depth:
        print("no chain of requested depth found")


if __name__ == "__main__":
    search()
