#!/usr/bin/env python3
"""Measure finite balanced-certificate independence for k=3.

Corollary 16.20 uses finite test sets in which every half-sized subset
contains e,y1,y2,y3 with

    y1 + y2 - e in A,
    y1 + y2 + y3 - 2e in A.

This diagnostic brute-forces the largest subset avoiding such certificates
inside a small finite ambient set.  Repetitions among y1,y2,y3 are allowed,
as in the certificate identities; each yi must differ from e.
"""

from __future__ import annotations

import argparse
from itertools import combinations, product


def has_certificate(subset: set[int], ambient: set[int]) -> bool:
    for e in subset:
        choices = [x for x in subset if x != e]
        for y1, y2, y3 in product(choices, repeat=3):
            if y1 + y2 - e in ambient and y1 + y2 + y3 - 2 * e in ambient:
                return True
    return False


def max_certificate_free(test: list[int], ambient: set[int]) -> tuple[int, tuple[int, ...]]:
    best: tuple[int, ...] = ()
    for size in range(len(test) + 1):
        found = None
        for combo in combinations(test, size):
            if not has_certificate(set(combo), ambient):
                found = combo
        if found is not None:
            best = found
    return len(best), best


def parse_elements(raw: str) -> list[int]:
    return [int(part) for part in raw.replace(",", " ").split()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ambient",
        default="1,2,3,4,8,19,20,28,33",
        help="comma/space separated ambient finite set",
    )
    parser.add_argument(
        "--test",
        default=None,
        help="comma/space separated test set; defaults to ambient",
    )
    args = parser.parse_args()

    ambient = set(parse_elements(args.ambient))
    test = parse_elements(args.test) if args.test else sorted(ambient)
    if not set(test) <= ambient:
        raise SystemExit("test set must be contained in ambient")

    alpha, witness = max_certificate_free(test, ambient)
    threshold = (len(test) + 1) // 2
    print("ambient=", sorted(ambient))
    print("test=", test)
    print("max_balanced_certificate_free_size=", alpha)
    print("witness=", witness)
    print("half_threshold=", threshold)
    print("every_half_subset_has_certificate=", alpha < threshold)


if __name__ == "__main__":
    main()
