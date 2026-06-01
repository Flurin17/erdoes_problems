#!/usr/bin/env python3
"""Finite checks for the spike-descent bookkeeping in PROOF.md.

The script is not a search for counterexamples.  It exhaustively verifies,
on small finite sets, the two purely finite facts used in Lemma 3.4d.1:

* an r-term representation family either has retained representations or
  descends through one deleted gate to (r-1)-term representations;
* a retained repair inside an h-term hole cannot have any deleted subblock
  plus retained subblock replaced by retained summands of the same length.
* a retained pair bank behind two deleted gates in a four-term hole contains
  a large one-gate low-count star.
* every one-gate low-count packet is finite-palette independent and has
  sparse anchored shadows.
* the lower-order hypergraph target matches the direct finite-deletion
  condition from Corollary 3.4d.12.
* finite lower-order holes can be shrunk to inclusion-minimal active
  barriers, as used in Corollary 3.4d.13.
* minimal two-sum barriers reflect every barrier vertex, as used in
  Corollary 3.4d.14.
* active lower-order barriers have lower-sumset shadows after removing one
  active barrier vertex, as used in Corollary 3.4d.15.
* the triple-shadow branch need not collapse to the two-term pair branch,
  as in Warning 3.4d.17.
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


def check_pair_bank_star(A: tuple[int, ...], D: tuple[int, ...]) -> int:
    C = tuple(a for a in A if a not in D)
    checked = 0
    for w in range(1, 4 * max(A) + 1):
        if reps(C, 4, w):
            continue
        for p in D:
            for q in D:
                m = w - p - q
                if m <= 0:
                    continue
                pairs = reps(C, 2, m)
                if not pairs:
                    continue
                low_by_gate: dict[int, set[int]] = {p: set(), q: set()}
                for a, b in pairs:
                    incidences = []
                    for gate, endpoint in ((p, a), (p, b), (q, a), (q, b)):
                        if not reps(C, 2, gate + endpoint):
                            incidences.append((gate, endpoint))
                    assert incidences
                    for gate, endpoint in incidences:
                        low_by_gate.setdefault(gate, set()).add(endpoint)

                best = max(len(points) for points in low_by_gate.values())
                assert best * 2 >= len(pairs)
                for gate, points in low_by_gate.items():
                    for endpoint in points:
                        assert reps(A, 2, gate + endpoint)
                        assert len(reps(A, 2, gate + endpoint)) <= len(D)
                checked += 1
    return checked


def check_sparse_shadow(A: tuple[int, ...], D: tuple[int, ...]) -> int:
    C = tuple(a for a in A if a not in D)
    checked = 0
    for gate in D:
        U = tuple(u for u in C if not reps(C, 2, gate + u))
        if not U:
            continue
        for u in U:
            for v in U:
                x = u + gate - v
                if x in A:
                    assert x in D
        for u0 in U:
            shadow = [u for u in U if gate + u - u0 in A]
            assert len(shadow) <= len(D)
            retained_shadow = [u for u in U if gate + u - u0 in C]
            assert not retained_shadow
        checked += 1
    return checked


def supports_outside_core(
    A: tuple[int, ...], core: tuple[int, ...], length: int, target: int
) -> list[frozenset[int]]:
    core_set = set(core)
    edges: set[frozenset[int]] = set()
    for rep in reps(A, length, target):
        outside = frozenset(x for x in rep if x not in core_set)
        if outside:
            edges.add(outside)
    return list(edges)


def check_lower_hypergraph_equivalence(A: tuple[int, ...], core: tuple[int, ...]) -> int:
    outside = tuple(a for a in A if a not in core)
    checked = 0
    for length in range(2, 5):
        core_bound = length * max(core) if core else 0
        for target in range(1, length * max(A) + 1):
            if target <= core_bound:
                continue
            if not reps(outside, length, target):
                continue
            edges = supports_outside_core(A, core, length, target)
            for d_size in range(0, min(3, len(outside)) + 1):
                for D in combinations(outside, d_size):
                    D_set = set(D)
                    hit_all = all(edge & D_set for edge in edges)
                    direct_hole = not reps(tuple(a for a in A if a not in D_set), length, target)
                    assert hit_all == direct_hole
                    checked += 1
    return checked


def check_minimal_barrier_extraction(A: tuple[int, ...], D: tuple[int, ...]) -> int:
    checked = 0
    D_set = set(D)
    for length in range(2, 5):
        for target in range(1, length * max(A) + 1):
            if not reps(A, length, target):
                continue
            if reps(tuple(a for a in A if a not in D_set), length, target):
                continue
            minimal: tuple[int, ...] | None = None
            for size in range(1, len(D) + 1):
                for F in combinations(D, size):
                    F_set = set(F)
                    if not reps(tuple(a for a in A if a not in F_set), length, target):
                        minimal = F
                        break
                if minimal is not None:
                    break
            assert minimal is not None
            F_set = set(minimal)
            for f in minimal:
                restored = tuple(a for a in A if a not in (F_set - {f}))
                assert reps(restored, length, target)
            checked += 1
    return checked


def check_pair_barrier_reflection(A: tuple[int, ...], F: tuple[int, ...]) -> int:
    checked = 0
    F_set = set(F)
    C = tuple(a for a in A if a not in F_set)
    A_set = set(A)
    for target in range(1, 2 * max(A) + 1):
        if not reps(A, 2, target):
            continue
        if reps(C, 2, target):
            continue

        active = True
        for f in F:
            restored = tuple(a for a in A if a not in (F_set - {f}))
            if not reps(restored, 2, target):
                active = False
                break
        if not active:
            continue

        for f in F:
            assert target - f in A_set
        for a, b in reps(A, 2, target):
            assert a in F_set or b in F_set
        checked += 1
    return checked


def check_active_lower_shadow(A: tuple[int, ...], F: tuple[int, ...]) -> int:
    checked = 0
    F_set = set(F)
    for length in range(2, 5):
        for target in range(1, length * max(A) + 1):
            if not reps(A, length, target):
                continue
            if reps(tuple(a for a in A if a not in F_set), length, target):
                continue

            active = True
            for f in F:
                restored = tuple(a for a in A if a not in (F_set - {f}))
                if not reps(restored, length, target):
                    active = False
                    break
            if not active:
                continue

            for f in F:
                restored = tuple(a for a in A if a not in (F_set - {f}))
                assert reps(restored, length - 1, target - f)
            checked += 1
    return checked


def check_triple_shadow_not_pair_example() -> None:
    A = (1, 2, 3, 4)
    F = {1}
    C = tuple(a for a in A if a not in F)
    tau = 2
    u = 3
    target = tau + u
    assert reps(A, 3, target)
    assert not reps(C, 3, target)
    assert reps(A, 2, target - 1)
    assert reps(C, 2, 1 + u)


def main() -> None:
    check_triple_shadow_not_pair_example()
    sets_checked = 0
    decomposition_checked = 0
    obstruction_checked = 0
    pair_star_checked = 0
    sparse_shadow_checked = 0
    lower_hypergraph_checked = 0
    minimal_barrier_checked = 0
    pair_barrier_reflection_checked = 0
    active_lower_shadow_checked = 0
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
                    pair_star_checked += check_pair_bank_star(A, D)
                    sparse_shadow_checked += check_sparse_shadow(A, D)
                    minimal_barrier_checked += check_minimal_barrier_extraction(A, D)
                    pair_barrier_reflection_checked += check_pair_barrier_reflection(A, D)
                    active_lower_shadow_checked += check_active_lower_shadow(A, D)
            for core_size in range(0, min(3, size) + 1):
                for core in combinations(A, core_size):
                    lower_hypergraph_checked += check_lower_hypergraph_equivalence(A, core)
    print("finite hole descent checks passed")
    print(f"sets_checked={sets_checked}")
    print(f"decomposition_checked={decomposition_checked}")
    print(f"obstruction_checked={obstruction_checked}")
    print(f"pair_star_checked={pair_star_checked}")
    print(f"sparse_shadow_checked={sparse_shadow_checked}")
    print(f"lower_hypergraph_checked={lower_hypergraph_checked}")
    print(f"minimal_barrier_checked={minimal_barrier_checked}")
    print(f"pair_barrier_reflection_checked={pair_barrier_reflection_checked}")
    print(f"active_lower_shadow_checked={active_lower_shadow_checked}")


if __name__ == "__main__":
    main()
