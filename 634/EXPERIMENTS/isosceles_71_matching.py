#!/usr/bin/env python3
"""Length-only interior side-matching constraints for the prime-71 candidate.

After the forced outer boundary is removed from the candidate with tile sides
(a,b,c)=(39,16,49), the remaining interior side incidences are

    a: 67, b: 63, c: 63.

An interior matched segment is modeled only by the two multisets of tile sides
on its two sides. This deliberately ignores geometry and angle order, so it is
a necessary condition only. The useful output is the minimum maximum segment
length forced by `c`-parity: below length `195`, every equal-length component
has even total `c`-incidence, but the remaining interior `c`-incidence count is
odd.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass


SIDES = (39, 16, 49)  # a,b,c
INTERIOR_COUNTS = (67, 63, 63)


@dataclass(frozen=True)
class Component:
    counts: tuple[int, int, int]
    length: int
    left: tuple[int, int, int]
    right: tuple[int, int, int]


def side_decompositions(max_length: int) -> dict[int, list[tuple[int, int, int]]]:
    by_length: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    a, b, c = SIDES
    for na in range(max_length // a + 1):
        for nb in range(max_length // b + 1):
            for nc in range(max_length // c + 1):
                if na == nb == nc == 0:
                    continue
                length = a * na + b * nb + c * nc
                if length <= max_length:
                    by_length[length].append((na, nb, nc))
    return by_length


def component_types(max_length: int) -> dict[tuple[int, int, int], Component]:
    out: dict[tuple[int, int, int], Component] = {}
    for length, decomps in side_decompositions(max_length).items():
        for i, left in enumerate(decomps):
            for right in decomps[i:]:
                counts = tuple(left[k] + right[k] for k in range(3))
                out.setdefault(counts, Component(counts, length, left, right))
    return out


def odd_c_components(max_length: int) -> list[Component]:
    return [
        component
        for component in component_types(max_length).values()
        if component.counts[2] % 2 == 1
    ]


def explicit_partition_at_195() -> list[Component]:
    """A length-only partition of all interior incidences with max length 195."""
    return (
        [Component((0, 6, 6), 195, (0, 3, 3), (0, 3, 3))] * 8
        + [Component((10, 0, 0), 195, (5, 0, 0), (5, 0, 0))] * 6
        + [Component((0, 12, 4), 194, (0, 6, 2), (0, 6, 2))]
        + [Component((5, 3, 3), 195, (0, 3, 3), (5, 0, 0))]
        + [Component((2, 0, 6), 186, (1, 0, 3), (1, 0, 3))]
        + [Component((0, 0, 2), 49, (0, 0, 1), (0, 0, 1))]
    )


def verify_partition(partition: list[Component]) -> None:
    totals = [0, 0, 0]
    for component in partition:
        assert sum(SIDES[i] * component.left[i] for i in range(3)) == component.length
        assert sum(SIDES[i] * component.right[i] for i in range(3)) == component.length
        assert component.counts == tuple(component.left[i] + component.right[i] for i in range(3))
        for i in range(3):
            totals[i] += component.counts[i]
    assert tuple(totals) == INTERIOR_COUNTS


def main() -> None:
    print("prime-71 interior length-only side-matching model")
    print(f"tile sides (a,b,c)={SIDES}")
    print(f"interior side incidences (a,b,c)={INTERIOR_COUNTS}")
    assert 2 * SIDES[0] + 2 * SIDES[2] == 11 * SIDES[1]
    assert 5 * SIDES[0] == 3 * SIDES[1] + 3 * SIDES[2]
    print("relation basis: 2a+2c=11b and 5a=3b+3c")
    odd_before_195 = odd_c_components(194)
    assert not odd_before_195
    first_odd = odd_c_components(195)
    assert first_odd == [Component((5, 3, 3), 195, (0, 3, 3), (5, 0, 0))]
    print("components of length <= 194 have even c-incidence")
    print(f"first odd-c component: length {first_odd[0].length}, {first_odd[0].left} | {first_odd[0].right}")
    solution = explicit_partition_at_195()
    verify_partition(solution)
    print("minimum possible max segment length from c-parity: 195")
    print(f"one length-only partition uses {len(solution)} matched segment(s):")
    for component, multiplicity in Counter(solution).most_common():
        print(
            f"  {multiplicity} x length {component.length}: "
            f"{component.left} | {component.right} -> counts {component.counts}"
        )
    print("limitation: this ignores segment placement, order along the segment, and vertex angles")


if __name__ == "__main__":
    main()
