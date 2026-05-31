#!/usr/bin/env python3
"""Check the finite-accelerator residue obstruction.

This script searches small cyclic groups for a residue set S and an
accelerator f such that:

  * S union {f} is a k-basis of residues;
  * some residue has no (k+1)-term representation using f.

Lemma 6 in PROOF.md proves this is impossible. The script is a finite sanity
check for k=2 in small moduli.
"""

from __future__ import annotations

from itertools import combinations


def hsum(residues: set[int], h: int, mod: int) -> set[int]:
    out = {0}
    for _ in range(h):
        out = {(x + y) % mod for x in out for y in residues}
    return out


def accelerator_reachable(S: set[int], f: int, k: int, mod: int) -> set[int]:
    """Residues with a (k+1)-term representation using at least one f."""
    out: set[int] = set()
    for copies in range(1, k + 2):
        rest = k + 1 - copies
        out |= {((copies * f) + x) % mod for x in hsum(S, rest, mod)}
    return out


def main(limit_mod: int = 14, k: int = 2) -> None:
    for mod in range(2, limit_mod + 1):
        group = set(range(mod))
        for size in range(1, mod + 1):
            for raw in combinations(range(mod), size):
                S = set(raw)
                for f in range(mod):
                    A = S | {f}
                    if hsum(A, k, mod) != group:
                        continue
                    reachable = accelerator_reachable(S, f, k, mod)
                    if reachable != group:
                        print("unexpected counterexample")
                        print(f"mod={mod} k={k} S={sorted(S)} f={f}")
                        print(f"missing={sorted(group - reachable)}")
                        return
        print(f"mod={mod}: no counterexample")


if __name__ == "__main__":
    main()
