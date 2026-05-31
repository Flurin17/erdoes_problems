#!/usr/bin/env python3
"""Finite search for initial Schreier-stage gadgets.

This searches for small finite sets A whose two-sums cover a prefix window
and whose first Schreier edges on an ordered protected tail P have genuine
minimal three-fold holes with shifted two-sum domination. It is a finite
diagnostic for Proposition 13.1b-Schreier in PROOF.md.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def missing_from_hsum_interval(
    elements: set[int],
    h: int,
    lo: int,
    hi: int,
) -> list[int]:
    sums = hsum(elements, h, hi)
    return [x for x in range(lo, hi + 1) if x not in sums]


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


def private_colors(
    elements: set[int],
    deletion: tuple[int, ...],
    witness: int,
    retained: int,
) -> list[int]:
    removed = set(deletion)
    kept = elements - removed
    two_kept = {a + b for a in kept for b in kept}
    return [
        f
        for f in deletion
        if witness - retained - f in kept and retained + f not in two_kept
    ]


def candidate_failure(
    elements: set[int],
    deletion: tuple[int, ...],
    witness: int,
    threshold: int,
) -> str:
    removed = set(deletion)
    kept = elements - removed
    if witness in hsum(kept, 3, witness):
        return "poisoned"

    missing_repairs = [
        f
        for f in deletion
        if witness not in hsum(elements - (removed - {f}), 3, witness)
    ]
    if missing_repairs:
        return f"repair-missing:{missing_repairs}"

    pair_deleted = {a + b for a in removed for b in removed}
    for e in sorted(kept):
        if witness - e < threshold or witness - e in pair_deleted:
            continue
        reflected = [f for f in deletion if witness - e - f in kept]
        if not reflected:
            return f"no-reflection:e={e}"
        colors = private_colors(elements, deletion, witness, e)
        if not colors:
            return f"absorbed:e={e},f={reflected}"

    return "ok"


def diagnose_edge_candidates(
    elements: set[int],
    edge: tuple[int, ...],
    coverage: int,
    threshold: int = 2,
) -> list[tuple[str, int]]:
    first_by_reason: dict[str, int] = {}
    for w in range(max(edge), coverage + 1):
        reason = candidate_failure(elements, edge, w, threshold)
        key = reason.split(":", 1)[0]
        first_by_reason.setdefault(reason if key == "repair-missing" else key, w)
        if reason == "ok":
            break
    return sorted((reason, w) for reason, w in first_by_reason.items())


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


def schreier_edges(protected: list[int]) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for index, first in enumerate(protected):
        size = index + 2
        tail = protected[index + 1 :]
        if len(tail) < size - 1:
            continue
        for rest in combinations(tail, size - 1):
            out.append((first, *rest))
    return out


def witnesses_for_edges(
    elements: set[int],
    edges: list[tuple[int, ...]],
    coverage: int,
) -> list[tuple[tuple[int, ...], int]] | None:
    data: list[tuple[tuple[int, ...], int]] = []
    for edge in edges:
        witness = None
        for w in range(max(edge), coverage + 1):
            if minimal_hole(elements, edge, w) and dominates(elements, edge, w, 2):
                witness = w
                break
        if witness is None:
            return None
        data.append((edge, witness))
    return data


def choose_protected(
    elements: set[int],
    protected_count: int,
    min_protected: int | None,
) -> list[int]:
    ordered = sorted(elements)
    if min_protected is None:
        return ordered[:protected_count]
    return [x for x in ordered if x >= min_protected][:protected_count]


def search_protected(
    max_value: int,
    max_size: int,
    protected_count: int,
    min_protected: int | None,
) -> None:
    for candidate_max in range(8, max_value + 1):
        for size in range(protected_count + 1, min(candidate_max, max_size) + 1):
            for tuple_a in combinations(range(1, candidate_max + 1), size):
                elements = set(tuple_a)
                coverage = cover_end(elements, 2, 3 * candidate_max)
                if coverage < candidate_max:
                    continue
                protected = choose_protected(elements, protected_count, min_protected)
                if len(protected) < protected_count:
                    continue
                edges = (
                    first_schreier_edges(protected)
                    if protected_count == 4
                    else schreier_edges(protected)
                )
                data = witnesses_for_edges(elements, edges, coverage)
                if data is not None:
                    print("finite Schreier-stage gadget")
                    print("A=", sorted(elements), "coverage_end=", coverage)
                    print("protected=", protected)
                    print("edges=", data)
                    return
    print("no finite Schreier-stage gadget found within searched bounds")


def extend_first(max_new: int, max_candidate: int) -> None:
    base = {1, 2, 3, 4, 8}
    base_protected = [1, 2, 3, 4]
    for size in range(1, max_new + 1):
        for new_tuple in combinations(range(13, max_candidate + 1), size):
            elements = base | set(new_tuple)
            coverage = cover_end(elements, 2, 4 * max(elements) + 100)
            if coverage < max(elements) + 1:
                continue
            protected = sorted([*base_protected, *new_tuple])[:5]
            data = witnesses_for_edges(elements, schreier_edges(protected), coverage)
            if data is not None:
                print("second Schreier-stage candidate")
                print("A=", sorted(elements), "coverage_end=", coverage)
                print("protected=", protected)
                print("edges=", data)
                return
    print("no second-stage extension found within searched bounds")


def check_tail_chain(max_p6: int, max_extra: int, max_extra_value: int) -> None:
    base = {1, 2, 4, 5, 8, 10, 15, 18, 19}
    p5 = 30
    first = base | {p5}
    protected5 = [10, 15, 18, 19, 30]
    coverage = cover_end(first, 2, 200)
    data = witnesses_for_edges(first, schreier_edges(protected5), coverage)
    print("tail P5 seed")
    print("A=", sorted(first), "coverage_end=", coverage)
    print("protected=", protected5)
    print("edges=", data)

    for p6 in range(p5 + 1, max_p6 + 1):
        protected6 = [*protected5, p6]
        edges = schreier_edges(protected6)
        for extra_count in range(max_extra + 1):
            for extras in combinations(range(p6 + 1, max_extra_value + 1), extra_count):
                elements = first | {p6} | set(extras)
                cap = 4 * max(elements) + 100
                coverage = cover_end(elements, 2, cap)
                if coverage < max(elements):
                    continue
                data = witnesses_for_edges(elements, edges, coverage)
                if data is not None:
                    print("tail P6 extension")
                    print("A=", sorted(elements), "coverage_end=", coverage)
                    print("protected=", protected6)
                    print("edges=", data)
                    return
    print("no tail P6 extension found within searched bounds")


def p6_pair_diagnostic() -> None:
    """Diagnose the first new pair edge in the tail P5 seed."""
    seed = {1, 2, 4, 5, 8, 10, 15, 18, 19, 30}
    retained_seed = seed - {10}

    candidates: list[tuple[int, int]] = []
    grouped: dict[int, list[int]] = {}
    for p in range(31, 51):
        for u in range(2, 31):
            w = p + u
            if u not in hsum(retained_seed, 2, u):
                continue
            if w in hsum(retained_seed, 3, w):
                continue
            if all(
                not (u <= c) or (p + u - c - 10 in seed)
                for c in retained_seed
            ):
                candidates.append((p, w))
                grouped.setdefault(w, []).append(p)

    print("necessary low-excess candidates for edge {10,p}:")
    for w in sorted(grouped):
        print(f"  w={w}: p={grouped[w]}")

    def find_extension(p: int, w: int, max_nodes: int = 200_000) -> tuple[int, ...] | None:
        base = seed | {p}
        edge = (10, p)
        filler_range = tuple(range(p + 1, w))
        nodes = 0

        @lru_cache(maxsize=None)
        def dfs(frozen_fillers: tuple[int, ...]) -> tuple[int, ...] | None:
            nonlocal nodes
            nodes += 1
            if nodes > max_nodes:
                return None
            fillers = set(frozen_fillers)
            elements = base | fillers
            if w in hsum(elements - set(edge), 3, w):
                return None

            coverage = cover_end(elements, 2, w)
            if coverage >= w:
                if minimal_hole(elements, edge, w) and dominates(elements, edge, w, 2):
                    return tuple(sorted(fillers))
                return None

            target = coverage + 1
            additions: set[tuple[int, ...]] = set()
            for t in elements:
                q = target - t
                if p < q < w and q not in elements:
                    additions.add((q,))
            if target % 2 == 0:
                q = target // 2
                if p < q < w and q not in elements:
                    additions.add((q,))
            for q1 in filler_range:
                q2 = target - q1
                if q1 <= q2 and p < q2 < w and q1 not in elements and q2 not in elements:
                    additions.add(tuple(sorted({q1, q2})))

            for addition in sorted(additions, key=lambda item: (len(item), item)):
                next_fillers = tuple(sorted(fillers | set(addition)))
                result = dfs(next_fillers)
                if result is not None:
                    return result
            return None

        return dfs(tuple())

    print("pair-edge extensions among those candidates:")
    escapes: list[tuple[int, int, tuple[int, ...]]] = []
    for p, w in candidates:
        fillers = find_extension(p, w)
        if fillers is not None:
            escapes.append((p, w, fillers))
            print(f"  p={p}, w={w}, fillers={list(fillers)}")
    if not escapes:
        print("  none")

    if escapes:
        p, _, fillers = escapes[0]
        elements = seed | {p} | set(fillers)
        protected = [x for x in sorted(elements) if x >= 10]
        coverage = cover_end(elements, 2, 3 * max(elements))
        failed_edges = [
            edge
            for edge in schreier_edges(protected)
            if witnesses_for_edges(elements, [edge], coverage) is None
        ]
        print("treating fillers as protected:")
        print("  protected=", protected, "coverage_end=", coverage)
        print("  failed edge count=", len(failed_edges))
        print("  first failed edges=", failed_edges[:12])
        print("  first candidate failure types:")
        sample_edges = list(failed_edges[:8])
        special = (18, 19, 30, 38)
        if special in failed_edges and special not in sample_edges:
            sample_edges.append(special)
        for edge in sample_edges:
            print(f"    {edge}: {diagnose_edge_candidates(elements, edge, coverage)}")
        print("  protected-filler pair intervals:")
        for q in fillers:
            edge = (10, q)
            c = elements - set(edge)
            missing3 = missing_from_hsum_interval(c, 3, q, coverage)
            endpoint_missing = missing_from_hsum_interval(c, 2, q - p, coverage - p)
            endpoint_note = (
                f"; retained {p} alone leaves first shifted gaps="
                f"{endpoint_missing[:8]}"
                if endpoint_missing
                else f"; retained {p} already poisons the whole interval"
            )
            if missing3:
                print(
                    f"    {edge}: [q,{coverage}] has 3C gaps; "
                    f"first gaps={missing3[:8]}{endpoint_note}"
                )
            else:
                print(
                    f"    {edge}: every candidate in [{q},{coverage}] "
                    f"is already in 3C{endpoint_note}"
                )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extend-first", action="store_true")
    parser.add_argument("--tail-chain", action="store_true")
    parser.add_argument("--p6-pair-diagnostic", action="store_true")
    parser.add_argument("--max-value", type=int, default=23)
    parser.add_argument("--max-size", type=int, default=10)
    parser.add_argument("--protected-count", type=int, default=4)
    parser.add_argument("--min-protected", type=int)
    parser.add_argument("--max-new", type=int, default=4)
    parser.add_argument("--max-candidate", type=int, default=35)
    parser.add_argument("--max-p6", type=int, default=120)
    parser.add_argument("--max-extra", type=int, default=3)
    parser.add_argument("--max-extra-value", type=int, default=151)
    args = parser.parse_args()
    if args.extend_first:
        extend_first(args.max_new, args.max_candidate)
    elif args.tail_chain:
        check_tail_chain(args.max_p6, args.max_extra, args.max_extra_value)
    elif args.p6_pair_diagnostic:
        p6_pair_diagnostic()
    else:
        search_protected(
            args.max_value,
            args.max_size,
            args.protected_count,
            args.min_protected,
        )


if __name__ == "__main__":
    main()
