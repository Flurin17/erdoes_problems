#!/usr/bin/env python3
"""Search robust finite-booster residue patterns by order.

For a possible negative construction in order k>=3, look for a finite
cyclic model with residues S and one retained booster f such that:

  * (k+1)S covers the group;
  * k(S union {f}) covers the group;
  * deleting any residue s in S leaves a (k+1)-fold residue hole even with
    the booster retained.

This is only a residue obstruction. It does not lift elementwise to an
integer basis without an endpoint/block mechanism that prevents replacement
by another integer in the same residue class.
"""

from __future__ import annotations

import argparse
from itertools import combinations


def hsum(residues: set[int], h: int, modulus: int) -> set[int]:
    sums = {0}
    for _ in range(h):
        sums = {(x + r) % modulus for x in sums for r in residues}
    return sums


def find_patterns(
    k: int,
    limit_modulus: int,
    max_size: int,
    max_hits: int,
) -> list[tuple[int, list[int], int, dict[int, list[int]]]]:
    h = k + 1
    hits: list[tuple[int, list[int], int, dict[int, list[int]]]] = []
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
                        hits.append((modulus, sorted(S), f, holes))
                        if len(hits) >= max_hits:
                            return hits
    return hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=7)
    parser.add_argument("--limit-modulus", type=int, default=80)
    parser.add_argument("--max-size", type=int, default=10)
    parser.add_argument("--max-hits", type=int, default=3)
    args = parser.parse_args()

    for k in range(args.min_k, args.max_k + 1):
        print(f"==== k={k}")
        hits = find_patterns(k, args.limit_modulus, args.max_size, args.max_hits)
        if not hits:
            print("  no pattern found")
            continue
        for modulus, residues, booster, holes in hits:
            preview = {s: holes[s][:8] for s in holes}
            print(
                "  modulus=", modulus,
                "S=", residues,
                "f=", booster,
                "holes=", preview,
            )


if __name__ == "__main__":
    main()
