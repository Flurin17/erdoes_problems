#!/usr/bin/env python3
"""Check the small gap between deletion-minimality and cone separation.

The family

    e1, -1_{1,2}, -1_{1,3}, 1_{2,3}

has no nonempty 0/1 subfamily summing to zero, but it has a positive integer
dependence with coefficients (2,1,1,1).  Hence a strict separating functional
need not exist for a deletion-minimal trace family.
"""

from __future__ import annotations

from itertools import combinations


Vector = tuple[int, ...]


FAMILY: list[Vector] = [
    (1, 0, 0),
    (-1, -1, 0),
    (-1, 0, -1),
    (0, 1, 1),
]

DEPENDENCE = [2, 1, 1, 1]


def add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))


def scale(c: int, v: Vector) -> Vector:
    return tuple(c * x for x in v)


def main() -> None:
    zero = (0, 0, 0)
    zero_subsets: list[tuple[int, ...]] = []
    for r in range(1, len(FAMILY) + 1):
        for subset in combinations(range(len(FAMILY)), r):
            total = zero
            for index in subset:
                total = add(total, FAMILY[index])
            if total == zero:
                zero_subsets.append(subset)

    dependence_total = zero
    for coefficient, vector in zip(DEPENDENCE, FAMILY):
        dependence_total = add(dependence_total, scale(coefficient, vector))

    print("family=" + " ".join(str(v) for v in FAMILY))
    print(f"zero_01_subsets={zero_subsets}")
    print(f"positive_dependence={DEPENDENCE}")
    print(f"dependence_total={dependence_total}")
    assert not zero_subsets
    assert dependence_total == zero


if __name__ == "__main__":
    main()
