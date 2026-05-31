#!/usr/bin/env python3
"""Finite cyclic search for barrier-style counterexample analogues.

For k=2 and a fixed q, search for residue sets S in Z/mZ such that:

  * 2S = Z/mZ;
  * for every q-subset F of S, 3(S\\F) != Z/mZ.

This is only a residue-level analogue. It does not solve the integer
problem, because deleting finitely many integers does not delete whole
residue classes.
"""

from __future__ import annotations

from itertools import combinations


def hsum(S: set[int], h: int, mod: int) -> set[int]:
    out = {0}
    for _ in range(h):
        out = {(x + y) % mod for x in out for y in S}
    return out


def main(limit_mod: int = 17, q: int = 2) -> None:
    for mod in range(2, limit_mod + 1):
        group = set(range(mod))
        total = 0
        examples: list[list[int]] = []
        for mask in range(1, 1 << mod):
            S = {i for i in range(mod) if (mask >> i) & 1}
            if len(S) < q or hsum(S, 2, mod) != group:
                continue
            if all(hsum(S - set(F), 3, mod) != group for F in combinations(S, q)):
                total += 1
                if len(examples) < 3:
                    examples.append(sorted(S))
        if total:
            print(f"mod={mod} q={q} examples={total} sample={examples}")


if __name__ == "__main__":
    main()
