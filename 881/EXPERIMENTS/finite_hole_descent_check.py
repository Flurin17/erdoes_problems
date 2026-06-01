#!/usr/bin/env python3
"""Finite checks for the spike-descent bookkeeping in PROOF.md.

The script is not a search for counterexamples.  It exhaustively verifies,
on small finite sets, the two purely finite facts used in Lemma 3.4d.1:

* an r-term representation family either has retained representations or
  descends through one deleted gate to (r-1)-term representations;
* a retained repair inside an h-term hole cannot have any deleted subblock
  plus retained subblock replaced by retained summands of the same length.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, combinations_with_replacement


def reps(values: tuple[int, ...], length: int, target: int) -> list[tuple[int, ...]]:
    if length == 0:
        return [()] if target == 0 else []
    return [
        rep
        for rep in combinations_with_replacement(values, length)
        if sum(rep) == target
    ]


def submultisets(rep: tuple[int, ...]) -> set[tuple[int, ...]]:
    out: set[tuple[int, ...]] = {()}
    for r in range(1, len(rep) + 1):
        out.update(combinations(rep, r))
    return out


def check_decomposition(A: tuple[int, ...], D: tuple[int, ...], max_h: int) -> int:
    C = tuple(a for a in A if a not in D)
    checked = 0
    for h in range(2, max_h + 1):
        max_target = h * max(A)
        for r in range(1, h):
            for target in range(1, max_target + 1):
                all_reps = reps(A, r, target)
                retained = reps(C, r, target)
                buckets: dict[int, set[tuple[int, ...]]] = defaultdict(set)
                contaminated = 0
                for rep in all_reps:
                    if all(x not in D for x in rep):
                        continue
                    contaminated += 1
                    gate = min(x for x in rep if x in D)
                    rest = list(rep)
                    rest.remove(gate)
                    buckets[gate].add(tuple(rest))

                assert len(all_reps) == len(retained) + contaminated
                assert contaminated == sum(len(v) for v in buckets.values())
                for gate, rest_reps in buckets.items():
                    expected = set(reps(A, r - 1, target - gate))
                    assert rest_reps <= expected
                checked += 1
    return checked


def check_hole_obstruction(A: tuple[int, ...], D: tuple[int, ...], max_h: int) -> int:
    C = tuple(a for a in A if a not in D)
    checked = 0
    for h in range(2, max_h + 1):
        max_target = h * max(A)
        for w in range(1, max_target + 1):
            if reps(C, h, w):
                continue
            for s in range(1, h):
                for deleted_block in combinations_with_replacement(D, s):
                    target = w - sum(deleted_block)
                    if target < 0:
                        continue
                    r = h - s
                    for retained_rep in reps(C, r, target):
                        for retained_block in submultisets(retained_rep):
                            t = len(retained_block)
                            replacement_len = s + t
                            replacement_target = sum(deleted_block) + sum(retained_block)
                            assert not reps(C, replacement_len, replacement_target)
                            checked += 1
    return checked


def main() -> None:
    sets_checked = 0
    decomposition_checked = 0
    obstruction_checked = 0
    universe = range(1, 10)
    for size in range(4, 8):
        for A_raw in combinations(universe, size):
            A = tuple(A_raw)
            for d_size in range(1, min(4, size)):
                for D_raw in combinations(A, d_size):
                    D = tuple(D_raw)
                    sets_checked += 1
                    decomposition_checked += check_decomposition(A, D, max_h=5)
                    obstruction_checked += check_hole_obstruction(A, D, max_h=5)
    print("finite hole descent checks passed")
    print(f"sets_checked={sets_checked}")
    print(f"decomposition_checked={decomposition_checked}")
    print(f"obstruction_checked={obstruction_checked}")


if __name__ == "__main__":
    main()
