#!/usr/bin/env python3
"""Finite cyclic analogue for minimal 2-bases and 3-basis deletions.

This is not a model of the asymptotic problem, but it tracks a useful
warning: in finite cyclic groups, a minimal 2-basis need not have a
one-point deletion that remains a 3-basis. The asymptotic problem has
additional order/size constraints absent from finite groups.
"""

from __future__ import annotations


def hsum(S: set[int], h: int, mod: int) -> set[int]:
    out = {0}
    for _ in range(h):
        out = {(x + y) % mod for x in out for y in S}
    return out


def main(limit_mod: int = 15) -> None:
    for mod in range(2, limit_mod + 1):
        group = set(range(mod))
        minimal = 0
        good = 0
        bad_examples: list[list[int]] = []
        for mask in range(1, 1 << mod):
            S = {i for i in range(mod) if (mask >> i) & 1}
            if hsum(S, 2, mod) != group:
                continue
            if any(hsum(S - {s}, 2, mod) == group for s in S):
                continue
            minimal += 1
            if any(hsum(S - {s}, 3, mod) == group for s in S):
                good += 1
            elif len(bad_examples) < 2:
                bad_examples.append(sorted(S))
        if minimal:
            print(
                f"mod={mod} minimal_2={minimal} "
                f"one_deletion_3={good} bad_examples={bad_examples}"
            )


if __name__ == "__main__":
    main()
