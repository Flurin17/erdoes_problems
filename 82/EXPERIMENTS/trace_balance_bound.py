#!/usr/bin/env python3
"""Search trace families with no balanced subfamily and small total imbalance.

For a repeated-degree class A of size k, each outside vertex gives a trace in
{0,1}^k.  A deletable outside set preserving equal degrees is a nonempty set
of traces whose coordinate sum is constant.  Lemma 12 in PROOF.md adds the
necessary condition that the total coordinate-sum spread is at most k-1.

This script brute-forces distinct trace families for small k under that
additional total-imbalance constraint.
"""

from __future__ import annotations

import argparse


Vector = tuple[int, ...]


def trace_vectors(k: int) -> list[Vector]:
    """All nonconstant traces, represented by differences from coordinate k-1."""
    out: list[Vector] = []
    for mask in range(1 << k):
        bits = tuple((mask >> i) & 1 for i in range(k))
        if all(bit == bits[0] for bit in bits):
            continue
        base = bits[-1]
        out.append(tuple(bit - base for bit in bits[:-1]))
    return out


def add(u: Vector, v: Vector) -> Vector:
    return tuple(a + b for a, b in zip(u, v))


def neg(v: Vector) -> Vector:
    return tuple(-x for x in v)


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
    """Whether trace imbalance can be offset by degrees inside A.

    The difference coordinates are t_i - t_k.  Equal total degrees require
    e_i - e_k = -(t_i - t_k), where e_i is the degree of a_i in G[A].
    """
    for base_degree in range(k):
        sequence = [base_degree - x for x in total] + [base_degree]
        if all(0 <= x < k for x in sequence) and is_graphical(sequence):
            return True
    return False


class NodeLimitReached(Exception):
    pass


def search(k: int, bound: int, require_graphical: bool, max_nodes: int | None) -> None:
    vectors = trace_vectors(k)
    zero = tuple(0 for _ in range(k - 1))
    best_size = 0
    best_family: list[Vector] = []
    nodes = 0

    # Try vectors with larger support first; this tends to find strong lower
    # bounds early and improves the branch-and-bound cutoff.
    vectors.sort(key=lambda v: (sum(abs(x) for x in v), v), reverse=True)

    def dfs(index: int, chosen: list[Vector], subset_sums: set[Vector], total: Vector) -> None:
        nonlocal best_size, best_family, nodes
        nodes += 1
        if max_nodes is not None and nodes > max_nodes:
            raise NodeLimitReached
        if len(chosen) + (len(vectors) - index) < best_size:
            return

        if index == len(vectors):
            if (
                len(chosen) > best_size
                and total_ok(total, bound)
                and (not require_graphical or has_graphical_compensator(k, total))
            ):
                best_size = len(chosen)
                best_family = chosen.copy()
            return

        v = vectors[index]

        # Include v if it creates no zero subset.  The empty subset sum is in
        # subset_sums, and v is nonzero, so this also handles singleton sets.
        if neg(v) not in subset_sums:
            new_sums = set(subset_sums)
            for s in subset_sums:
                new_sums.add(add(s, v))
            chosen.append(v)
            dfs(index + 1, chosen, new_sums, add(total, v))
            chosen.pop()

        dfs(index + 1, chosen, subset_sums, total)

    complete = True
    try:
        dfs(0, [], {zero}, zero)
    except NodeLimitReached:
        complete = False

    print(f"k={k}")
    print(f"num_nonconstant_traces={len(vectors)}")
    print(f"total_imbalance_bound={bound}")
    print(f"require_graphical_compensator={require_graphical}")
    print(f"complete={complete}")
    print(f"search_nodes={nodes}")
    print(f"max_distinct_admissible_size={best_size}")
    if best_family:
        print("example=" + " ".join(",".join(map(str, v)) for v in best_family))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("k", type=int)
    parser.add_argument("--bound", type=int)
    parser.add_argument("--require-graphical", action="store_true")
    parser.add_argument("--max-nodes", type=int)
    args = parser.parse_args()
    if args.k > 5:
        parser.error("brute force is capped at k=5")
    search(
        args.k,
        args.bound if args.bound is not None else args.k - 1,
        args.require_graphical,
        args.max_nodes,
    )


if __name__ == "__main__":
    main()
