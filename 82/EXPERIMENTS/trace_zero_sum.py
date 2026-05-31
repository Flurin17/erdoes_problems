#!/usr/bin/env python3
"""Brute force distinct trace families with no balanced subfamily.

For a minimal repeated-degree host, outside vertices give 0/1 trace vectors on
the equal-degree class A.  No nonempty set of outside vertices may have
coordinate-sum equal to a constant vector.  This script studies the simplified
case where trace vectors are distinct.
"""

from __future__ import annotations

import argparse
from itertools import combinations


def vectors(k: int) -> list[tuple[int, ...]]:
    out = []
    for mask in range(1, (1 << k) - 1):
        out.append(tuple((mask >> i) & 1 for i in range(k)))
    return out


def is_balanced(subset: tuple[tuple[int, ...], ...]) -> bool:
    sums = [sum(v[i] for v in subset) for i in range(len(subset[0]))]
    return min(sums) == max(sums)


def family_is_admissible(family: tuple[tuple[int, ...], ...]) -> bool:
    for r in range(1, len(family) + 1):
        for subset in combinations(family, r):
            if is_balanced(subset):
                return False
    return True


def brute(k: int) -> None:
    vs = vectors(k)
    best_size = 0
    best_examples: list[tuple[tuple[int, ...], ...]] = []
    for mask in range(1 << len(vs)):
        size = mask.bit_count()
        if size < best_size:
            continue
        family = tuple(vs[i] for i in range(len(vs)) if (mask >> i) & 1)
        if family_is_admissible(family):
            if size > best_size:
                best_size = size
                best_examples = [family]
            elif len(best_examples) < 5:
                best_examples.append(family)
    print(f"k={k}")
    print(f"num_nonconstant_vectors={len(vs)}")
    print(f"max_distinct_admissible_size={best_size}")
    for family in best_examples:
        print("example=" + " ".join("".join(map(str, v)) for v in family))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("k", type=int)
    args = parser.parse_args()
    if args.k > 4:
        parser.error("brute force is capped at k=4")
    brute(args.k)


if __name__ == "__main__":
    main()
