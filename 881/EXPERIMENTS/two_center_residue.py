#!/usr/bin/env python3
"""Verify the residue-level two-center pair-barrier obstruction.

The set S={0,1,2,4} in Z/7Z is a finite model for the remaining k=2
finitely-bad obstruction:

  * 2S is the whole group;
  * deleting any singleton leaves a 3-basis;
  * deleting {0,1} creates a 3-sum hole at residue 2;
  * the reflected cover uses two centers and cannot be reduced to one.

This is not an integer counterexample; thick residue lifts lose
single-integer privacy as explained by Lemma 6.1 in PROOF.md.
"""

from __future__ import annotations


MOD = 7
S = {0, 1, 2, 4}


def hsum(values: set[int], h: int) -> set[int]:
    out = {0}
    for _ in range(h):
        out = {(x + y) % MOD for x in out for y in values}
    return out


def main() -> None:
    group = set(range(MOD))
    print("S=", sorted(S), "mod", MOD)
    print("2S whole group:", hsum(S, 2) == group)
    print(
        "all singleton deletions are 3-bases:",
        all(hsum(S - {s}, 3) == group for s in S),
    )
    pair = {0, 1}
    print("3(S\\{0,1})=", sorted(hsum(S - pair, 3)))
    print("2 is pair-deletion hole:", 2 not in hsum(S - pair, 3))

    two_center_cover = all(
        ((2 - e) % MOD in S) or ((1 - e) % MOD in S)
        for e in S
    )
    print("two-center reflected cover:", two_center_cover)

    one_centers = [
        c
        for c in group
        if all((c - e) % MOD in S for e in S)
    ]
    print("one reflected centers:", one_centers)


if __name__ == "__main__":
    main()
