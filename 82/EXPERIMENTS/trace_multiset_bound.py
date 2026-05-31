#!/usr/bin/env python3
"""Bounded search for zero-sum-free trace multisets.

The trace obstruction in PROOF.md gives vectors in {-1,0,1}^{k-1}.  A balanced
deletion is a nonempty submultiset with sum zero.  Lemma 13 also forces the
total vector to have small infinity norm, and Lemma 14 optionally requires
graphical compensation by the internal graph on the repeated-degree class.

This script searches with an explicit per-vector multiplicity cap.  It is not
a proof tool by itself; it is meant to detect small counterexamples to proposed
strong trace bounds.
"""

from __future__ import annotations

import argparse
from itertools import product


Vector = tuple[int, ...]


class NodeLimitReached(Exception):
    pass


def add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))


def scale(c: int, v: Vector) -> Vector:
    return tuple(c * x for x in v)


def neg(v: Vector) -> Vector:
    return tuple(-x for x in v)


def vectors(d: int) -> list[Vector]:
    out = [v for v in product([-1, 0, 1], repeat=d) if any(v)]
    out.sort(key=lambda v: (sum(abs(x) for x in v), v), reverse=True)
    return out


def trace_cone_vectors(d: int) -> list[Vector]:
    """Actual trace-difference vectors relative to one base coordinate.

    If an outside vertex is nonadjacent to the base vertex, its difference
    vector is a nonzero {0,1}-indicator.  If it is adjacent to the base vertex,
    its difference vector is a nonzero {0,-1}-indicator.
    """
    out: list[Vector] = []
    for mask in range(1, 1 << d):
        positive = tuple((mask >> i) & 1 for i in range(d))
        out.append(positive)
        out.append(tuple(-x for x in positive))
    out.sort(key=lambda v: (sum(abs(x) for x in v), v), reverse=True)
    return out


def total_ok(total: Vector, bound: int) -> bool:
    return all(abs(x) <= bound for x in total)


def is_graphical(sequence: list[int]) -> bool:
    seq = sorted(sequence, reverse=True)
    while seq and seq[0] > 0:
        degree = seq.pop(0)
        if degree < 0 or degree > len(seq):
            return False
        for i in range(degree):
            seq[i] -= 1
            if seq[i] < 0:
                return False
        seq.sort(reverse=True)
    return all(x == 0 for x in seq)


def has_graphical_compensator(k: int, total: Vector) -> bool:
    for base_degree in range(k):
        sequence = [base_degree - x for x in total] + [base_degree]
        if all(0 <= x < k for x in sequence) and is_graphical(sequence):
            return True
    return False


def trace_cone_stats(counts: list[int], support: list[Vector]) -> tuple[int, int, int]:
    positive = [0] * len(support[0])
    negative = [0] * len(support[0])
    for count, v in zip(counts, support):
        if not count:
            continue
        if all(x >= 0 for x in v):
            for i, value in enumerate(v):
                positive[i] += count * value
        elif all(x <= 0 for x in v):
            for i, value in enumerate(v):
                negative[i] += count * (-value)
    incidence = sum(positive) + sum(negative)
    cancellation = sum(min(p, n) for p, n in zip(positive, negative))
    imbalance_l1 = sum(abs(p - n) for p, n in zip(positive, negative))
    return incidence, cancellation, imbalance_l1


def extend_sums(
    sums: set[Vector], v: Vector, count: int, max_subset_sums: int | None
) -> set[Vector] | None:
    """Add count copies of v to a zero-sum-free subset-sum set."""
    out = set(sums)
    for t in range(1, count + 1):
        tv = scale(t, v)
        for s in sums:
            new_sum = add(s, tv)
            if new_sum == tuple(0 for _ in v):
                return None
            out.add(new_sum)
            if max_subset_sums is not None and len(out) > max_subset_sums:
                return None
    return out


def search(
    d: int,
    total_bound: int,
    multiplicity_cap: int,
    require_graphical: bool,
    max_nodes: int | None,
    max_subset_sums: int | None,
    trace_cone: bool,
) -> None:
    support = trace_cone_vectors(d) if trace_cone else vectors(d)
    zero = tuple(0 for _ in range(d))
    best_size = -1
    best_counts: list[int] = []
    best_total = zero
    nodes = 0

    def dfs(index: int, counts: list[int], sums: set[Vector], total: Vector, size: int) -> None:
        nonlocal best_size, best_counts, best_total, nodes
        nodes += 1
        if max_nodes is not None and nodes > max_nodes:
            raise NodeLimitReached

        if (
            size > best_size
            and total_ok(total, total_bound)
            and (
                not require_graphical
                or has_graphical_compensator(d + 1, total)
            )
        ):
            best_size = size
            best_counts = counts.copy() + [0] * (len(support) - len(counts))
            best_total = total

        if size + multiplicity_cap * (len(support) - index) < best_size:
            return

        if index == len(support):
            return

        v = support[index]
        for count in range(multiplicity_cap, -1, -1):
            new_sums = extend_sums(sums, v, count, max_subset_sums)
            if new_sums is None:
                continue
            counts.append(count)
            dfs(index + 1, counts, new_sums, add(total, scale(count, v)), size + count)
            counts.pop()

    complete = True
    try:
        dfs(0, [], {zero}, zero, 0)
    except NodeLimitReached:
        complete = False

    print(f"d={d}")
    print(f"k={d + 1}")
    print(f"support_size={len(support)}")
    print(f"total_bound={total_bound}")
    print(f"multiplicity_cap={multiplicity_cap}")
    print(f"trace_cone={trace_cone}")
    print(f"max_subset_sums={max_subset_sums}")
    print(f"require_graphical_compensator={require_graphical}")
    print(f"complete={complete}")
    print(f"search_nodes={nodes}")
    print(f"best_size={best_size}")
    print("best_total=" + ",".join(map(str, best_total)))
    if trace_cone and best_counts:
        incidence, cancellation, imbalance_l1 = trace_cone_stats(best_counts, support)
        print(f"best_trace_incidence={incidence}")
        print(f"best_cancellation_mass={cancellation}")
        print(f"best_imbalance_l1={imbalance_l1}")
    if best_counts:
        example = []
        for count, v in zip(best_counts, support):
            if count:
                example.append(f"{count}*" + ",".join(map(str, v)))
        print("example=" + " ".join(example))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("d", type=int, help="trace difference dimension k-1")
    parser.add_argument("--total-bound", type=int)
    parser.add_argument("--multiplicity-cap", type=int, default=3)
    parser.add_argument("--require-graphical", action="store_true")
    parser.add_argument("--trace-cone", action="store_true")
    parser.add_argument("--max-nodes", type=int)
    parser.add_argument("--max-subset-sums", type=int)
    args = parser.parse_args()

    search(
        args.d,
        args.total_bound if args.total_bound is not None else args.d,
        args.multiplicity_cap,
        args.require_graphical,
        args.max_nodes,
        args.max_subset_sums,
        args.trace_cone,
    )


if __name__ == "__main__":
    main()
