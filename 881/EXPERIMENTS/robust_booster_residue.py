#!/usr/bin/env python3
"""Finite cyclic search for robust finite-booster patterns.

A negative construction for k>=3 would be suggested by a residue set S and
a finite booster f such that:

  * (k+1)S covers the cyclic group;
  * k(S union {f}) covers the cyclic group;
  * after deleting any s in S, even (k+1)((S union {f})\\{s}) misses a
    residue.

This is stronger than ordinary adjacent-order residue minimality, because
the private residue hole must survive with the booster retained.  Lifting
such a pattern to integer element deletions is still nontrivial: deleting one
integer in a residue class does not delete the whole residue class.
"""

from __future__ import annotations

from itertools import combinations


def hsum(residues: set[int], h: int, modulus: int) -> set[int]:
    sums = {0}
    for _ in range(h):
        sums = {(x + r) % modulus for x in sums for r in residues}
    return sums


def find(limit_modulus: int = 80, max_size: int = 12) -> None:
    # Start at k=3.  The k=2 case is heavily constrained by the recurrence
    # theorem in PROOF.md and is much slower to exhaust naively.
    for k in range(3, 7):
        h = k + 1
        print(f"k={k}")
        for modulus in range(2, limit_modulus + 1):
            group = set(range(modulus))
            for size in range(1, min(modulus, max_size) + 1):
                for tuple_s in combinations(range(modulus), size):
                    S = set(tuple_s)
                    if hsum(S, h, modulus) != group:
                        continue
                    for f in range(modulus):
                        if f in S:
                            continue
                        A = S | {f}
                        if hsum(A, k, modulus) != group:
                            continue
                        holes = {
                            s: sorted(group - hsum(A - {s}, h, modulus))
                            for s in sorted(S)
                        }
                        if all(holes[s] for s in holes):
                            print(
                                "  modulus=", modulus,
                                "S=", sorted(S),
                                "f=", f,
                            )
                            for s, missing in holes.items():
                                print(f"    delete {s}: holes {missing[:10]}")
                            return
        print("  no pattern found in bounds")


if __name__ == "__main__":
    find()
