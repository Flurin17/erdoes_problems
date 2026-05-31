#!/usr/bin/env python3
"""Finite toy search for robust private two-sum gadgets.

For k=2, a counterexample block would benefit from finite sets T for which
T+T covers a long interval and each element of T appears in a sum not made
without it. This script searches small D for T subset [0,D] with:

  * T+T contains every integer in [0, 2D];
  * for every t in T, some sum s has exactly one unordered representation
    from T+T and that representation uses t.

This is not a proof of anything infinite; it is a sanity check for the local
"private witness" condition.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations


def pair_sums(tset: tuple[int, ...]) -> dict[int, list[tuple[int, int]]]:
    sums: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for i, a in enumerate(tset):
        for b in tset[i:]:
            sums[a + b].append((a, b))
    return sums


def is_full_interval_basis(tset: tuple[int, ...], dmax: int) -> bool:
    sums = pair_sums(tset)
    return all(n in sums for n in range(2 * dmax + 1))


def private_sums(tset: tuple[int, ...]) -> dict[int, list[int]]:
    sums = pair_sums(tset)
    out: dict[int, list[int]] = {}
    for t in tset:
        witnesses = [
            n
            for n, reps in sums.items()
            if len(reps) == 1 and t in reps[0]
        ]
        if witnesses:
            out[t] = sorted(witnesses)
    return out


def exhaustive_search(limit_d: int = 12, min_d: int = 4) -> None:
    for dmax in range(min_d, limit_d + 1):
        interior = range(1, dmax)
        for size in range(2, dmax + 2):
            for middle in combinations(interior, size - 2):
                tset = (0, *middle, dmax)
                if not is_full_interval_basis(tset, dmax):
                    continue
                priv = private_sums(tset)
                if len(priv) == len(tset):
                    print(f"D={dmax} size={len(tset)} T={list(tset)}")
                    for t in tset:
                        print(f"  t={t}: private sums {priv[t][:5]}")
                    return
    print(f"No gadget found for {min_d} <= D <= {limit_d}")


def product_gadget(base: tuple[int, ...], levels: int) -> tuple[int, ...]:
    out = base
    for _ in range(1, levels):
        dmax = max(out)
        q = 2 * dmax + 1
        out = tuple(sorted(t + q * s for s in base for t in out))
    return out


def demo_product(levels: int = 4) -> None:
    base = (0, 1, 3, 4)
    for level in range(1, levels + 1):
        tset = product_gadget(base, level)
        dmax = max(tset)
        priv = private_sums(tset)
        print(
            f"product level={level} D={dmax} size={len(tset)} "
            f"full={is_full_interval_basis(tset, dmax)} "
            f"all_private={len(priv) == len(tset)}"
        )


if __name__ == "__main__":
    exhaustive_search()
    demo_product()
