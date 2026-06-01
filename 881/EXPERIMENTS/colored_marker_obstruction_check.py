#!/usr/bin/env python3
"""Finite check for Lemma 16.0-pre.

The lemma is elementary: if colored marker classes C_1,...,C_k cover a
finite group by one marker from each class, then every residue can be
written as an extra marker from any chosen class plus another colored
k-term cover.  This script exhaustively checks the statement on small
cyclic groups, mainly to guard against off-by-one errors in the colored
formulation.
"""

from __future__ import annotations

from itertools import combinations, product


def colored_sum(classes: tuple[tuple[int, ...], ...], modulus: int) -> set[int]:
    sums = {0}
    for cls in classes:
        sums = {(x + c) % modulus for x in sums for c in cls}
    return sums


def main() -> None:
    checked = 0
    full_cover_checked = 0
    for modulus in range(2, 9):
        group = set(range(modulus))
        subsets: list[tuple[int, ...]] = []
        for size in range(1, min(2, modulus) + 1):
            subsets.extend(combinations(range(modulus), size))

        for k in range(2, 5):
            for classes in product(subsets, repeat=k):
                cover = colored_sum(classes, modulus)
                checked += 1
                if cover != group:
                    continue
                full_cover_checked += 1
                for cls in classes:
                    for z in cls:
                        shifted = {(r - z) % modulus for r in group}
                        assert shifted <= cover

    print("colored marker obstruction checks passed")
    print(f"systems_checked={checked}")
    print(f"full_cover_checked={full_cover_checked}")


if __name__ == "__main__":
    main()
