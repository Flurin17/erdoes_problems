#!/usr/bin/env python3
"""Search finite residue patterns for two-center pair holes.

This isolates the residue-level ingredients behind Example 8.7d:

* a background residue set R;
* two exceptional residues x,y;
* R plus x,y is a two-fold basis of the cyclic group;
* deleting x,y leaves a three-fold hole h outside 3R;
* shifted two-sum domination holds residue-wise:
  every background residue e has h-e in x+R or y+R.

These patterns are only local residue diagnostics. Integer lifts must still
handle individual representatives, old exceptional elements, carries, and
stage coverage.
"""

from __future__ import annotations

from itertools import combinations


def sumset(values: set[int], h: int, modulus: int) -> set[int]:
    sums = {0}
    for _ in range(h):
        sums = {(s + v) % modulus for s in sums for v in values}
    return sums


def search(max_modulus: int = 18) -> None:
    for modulus in range(5, max_modulus + 1):
        residues = set(range(modulus))
        for size in range(2, modulus - 1):
            for tuple_r in combinations(range(modulus), size):
                background = set(tuple_r)
                for x, y in combinations(sorted(residues - background), 2):
                    full = background | {x, y}
                    if sumset(full, 2, modulus) != residues:
                        continue
                    holes = sorted(residues - sumset(background, 3, modulus))
                    for h in holes:
                        cover_x = {(x + r) % modulus for r in background}
                        cover_y = {(y + r) % modulus for r in background}
                        if all((h - e) % modulus in cover_x | cover_y for e in background):
                            print("two-center residue pair hole")
                            print("modulus=", modulus)
                            print("R=", sorted(background), "x=", x, "y=", y, "hole=", h)
                            print("2(R+exceptions)=G:", sumset(full, 2, modulus) == residues)
                            print("3R misses:", holes)
                            print("x+R=", sorted(cover_x))
                            print("y+R=", sorted(cover_y))
                            return
    print("no two-center residue pair hole found")


def separation_diagnostic() -> None:
    """Check complete-pair separation by translates of {0,1,4} mod 8."""
    modulus = 8
    background = {0, 1, 4}
    residues = set(range(modulus))
    translates = [
        {(alpha + r) % modulus for r in background}
        for alpha in range(modulus)
    ]
    best: tuple[int, tuple[int, ...], list[tuple[int, int]]] | None = None
    for protected in combinations(range(modulus), 4):
        protected_set = set(protected)
        separated: list[tuple[int, int]] = []
        for x, y in combinations(protected, 2):
            for translate in translates:
                if x in translate or y in translate:
                    continue
                if protected_set - {x, y} <= translate:
                    separated.append((x, y))
                    break
        score = len(separated)
        if best is None or score > best[0]:
            best = (score, protected, separated)
    assert best is not None
    print("Z/8 translate separation diagnostic for R={0,1,4}")
    print("best separated pairs among four residues=", best[0], "of 6")
    print("protected=", list(best[1]), "separated=", best[2])


if __name__ == "__main__":
    search()
    separation_diagnostic()
