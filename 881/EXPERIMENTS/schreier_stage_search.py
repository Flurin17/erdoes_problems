#!/usr/bin/env python3
"""Finite search for initial Schreier-stage gadgets.

This searches for small finite sets A whose two-sums cover a prefix window
and whose first Schreier edges on an ordered protected tail P have genuine
minimal three-fold holes with shifted two-sum domination. It is a finite
diagnostic for Proposition 13.1b-Schreier in PROOF.md.
"""

from __future__ import annotations

from itertools import combinations


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def cover_end(elements: set[int], start: int, cap: int) -> int:
    sums = hsum(elements, 2, cap)
    x = start
    while x <= cap and x in sums:
        x += 1
    return x - 1


def two_reps(elements: set[int], target: int) -> list[tuple[int, int]]:
    ordered = sorted(elements)
    reps: list[tuple[int, int]] = []
    for i, a in enumerate(ordered):
        for b in ordered[i:]:
            if a + b == target:
                reps.append((a, b))
    return reps


def minimal_hole(elements: set[int], deletion: tuple[int, ...], witness: int) -> bool:
    removed = set(deletion)
    if witness in hsum(elements - removed, 3, witness):
        return False
    return all(witness in hsum(elements - (removed - {f}), 3, witness) for f in removed)


def dominates(elements: set[int], deletion: tuple[int, ...], witness: int, threshold: int) -> bool:
    removed = set(deletion)
    for e in elements - removed:
        if witness - e < threshold:
            continue
        for rep in two_reps(elements, witness - e):
            if set(rep).isdisjoint(removed):
                return False
    return True


def first_schreier_edges(protected: list[int]) -> list[tuple[int, ...]]:
    """Edges completed by the first four protected points."""
    if len(protected) < 4:
        return []
    p1, p2, p3, p4 = protected[:4]
    return [
        (p1, p2),
        (p1, p3),
        (p1, p4),
        (p2, p3, p4),
    ]


def main() -> None:
    for max_value in range(8, 24):
        for size in range(5, min(max_value, 10) + 1):
            for tuple_a in combinations(range(1, max_value + 1), size):
                elements = set(tuple_a)
                coverage = cover_end(elements, 2, 3 * max_value)
                if coverage < max_value:
                    continue
                protected = sorted(elements)[:4]
                edges = first_schreier_edges(protected)
                data: list[tuple[tuple[int, ...], int]] = []
                for edge in edges:
                    witness = None
                    for w in range(max(edge), coverage + 1):
                        if minimal_hole(elements, edge, w) and dominates(elements, edge, w, 2):
                            witness = w
                            break
                    if witness is None:
                        break
                    data.append((edge, witness))
                else:
                    print("finite Schreier-stage gadget")
                    print("A=", sorted(elements), "coverage_end=", coverage)
                    print("protected=", protected)
                    print("edges=", data)
                    return
    print("no finite Schreier-stage gadget found within searched bounds")


if __name__ == "__main__":
    main()
