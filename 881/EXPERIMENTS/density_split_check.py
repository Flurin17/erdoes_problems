#!/usr/bin/env python3
"""Finite checks for the no-majority density split.

Lemma 16.76 is a cardinality statement: if a bounded palette covers an
eta-fraction of a finite universe and no color has theta-density, then two
colors must carry definite positive density.  This script exhaustively
checks small universes and palettes for the integer-rounded version of that
claim.
"""

from __future__ import annotations

from itertools import combinations, product
from math import ceil


def subsets(universe: tuple[int, ...]) -> list[frozenset[int]]:
    out: list[frozenset[int]] = []
    for size in range(len(universe) + 1):
        for subset in combinations(universe, size):
            out.append(frozenset(subset))
    return out


def check_case(n: int, r: int, eta_num: int, eta_den: int, theta_num: int, theta_den: int) -> int:
    universe = tuple(range(n))
    all_subsets = subsets(universe)
    checked = 0
    eta_threshold = ceil(eta_num * n / eta_den)
    theta_bound = theta_num * n / theta_den
    first_threshold = eta_num * n / (eta_den * r)
    second_threshold = (
        (eta_num / eta_den - theta_num / theta_den) * n / (r - 1)
    )
    for palette_size in range(2, r + 1):
        for family in product(all_subsets, repeat=palette_size):
            union = frozenset().union(*family)
            if len(union) < eta_threshold:
                continue
            if any(len(part) >= theta_bound for part in family):
                continue
            checked += 1
            sizes = sorted((len(part) for part in family), reverse=True)
            if sizes[0] + 1e-12 < first_threshold:
                raise AssertionError((n, r, family, sizes, first_threshold))
            if sizes[1] + 1e-12 < second_threshold:
                raise AssertionError((n, r, family, sizes, second_threshold))
    print(
        f"case n={n} r={r} eta={eta_num}/{eta_den} theta={theta_num}/{theta_den} "
        f"checked={checked}"
    )
    return checked


def main() -> None:
    cases = [
        (5, 2, 4, 5, 3, 5),
        (6, 3, 2, 3, 1, 2),
        (5, 3, 4, 5, 3, 5),
        (5, 4, 3, 4, 1, 2),
    ]
    total = 0
    for case in cases:
        total += check_case(*case)
    print("density split check passed")
    print("total_checked=", total)


if __name__ == "__main__":
    main()
