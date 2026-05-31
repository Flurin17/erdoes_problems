#!/usr/bin/env python3
"""Finite diagnostics for higher front barriers.

This checks finite shadows of Warning 8.5a.1:

* the second-element front B2 has the barrier property on long enough
  finite sequences;
* B2 does not contain first-Schreier prefix links on any tested tail.

These are finite sanity checks only. The proof in PROOF.md is the infinite
argument.
"""

from __future__ import annotations

from itertools import combinations


def first_schreier_edges(sequence: tuple[int, ...]) -> set[tuple[int, ...]]:
    edges: set[tuple[int, ...]] = set()
    for index, value in enumerate(sequence, start=1):
        size = index + 1
        tail = sequence[index:]
        if len(tail) >= size - 1:
            for rest in combinations(tail, size - 1):
                edges.add((value, *rest))
    return edges


def second_element_edges(sequence: tuple[int, ...]) -> set[tuple[int, ...]]:
    edges: set[tuple[int, ...]] = set()
    for size in range(2, len(sequence) + 1):
        for edge in combinations(sequence, size):
            if len(edge) == edge[1]:
                edges.add(edge)
    return edges


def has_initial_edge(subsequence: tuple[int, ...], edges: set[tuple[int, ...]]) -> bool:
    for size in range(1, len(subsequence) + 1):
        if subsequence[:size] in edges:
            return True
    return False


def finite_barrier_failures(
    sequence: tuple[int, ...],
    edges: set[tuple[int, ...]],
    min_length: int,
) -> list[tuple[int, ...]]:
    failures: list[tuple[int, ...]] = []
    for size in range(min_length, len(sequence) + 1):
        for subsequence in combinations(sequence, size):
            if not has_initial_edge(subsequence, edges):
                failures.append(subsequence)
                if len(failures) >= 8:
                    return failures
    return failures


def schreier_subbarrier_witnesses(
    sequence: tuple[int, ...],
    edges: set[tuple[int, ...]],
    tail_size: int,
) -> list[tuple[int, ...]]:
    witnesses: list[tuple[int, ...]] = []
    for tail in combinations(sequence, tail_size):
        if first_schreier_edges(tail) <= edges:
            witnesses.append(tail)
            if len(witnesses) >= 8:
                return witnesses
    return witnesses


def main() -> None:
    sequence = tuple(range(2, 13))
    b2 = second_element_edges(sequence)
    min_length = max(sequence)

    print("front barrier diagnostic")
    print("sequence=", sequence)
    print("B2 edge count=", len(b2))
    print("first B2 edges=", sorted(b2, key=lambda e: (len(e), e))[:12])

    failures = finite_barrier_failures(sequence, b2, min_length)
    print("finite barrier test min_length=", min_length)
    print("barrier failures=", failures if failures else "none")

    for tail_size in range(3, 7):
        witnesses = schreier_subbarrier_witnesses(sequence, b2, tail_size)
        print(
            "first-Schreier subbarrier tails",
            "tail_size=", tail_size,
            "witnesses=", witnesses if witnesses else "none",
        )

    sample_tail = sequence[:5]
    print("sample tail=", sample_tail)
    print("S1(sample)=", sorted(first_schreier_edges(sample_tail)))
    print("S1(sample) subset B2=", first_schreier_edges(sample_tail) <= b2)


if __name__ == "__main__":
    main()
