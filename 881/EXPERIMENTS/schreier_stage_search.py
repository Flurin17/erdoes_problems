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
from itertools import combinations, permutations


def parse_int_set(value: str) -> set[int]:
    return {int(part) for part in value.split(",") if part}


def parse_int_tuple(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in value.split(",") if part)


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


def schreier_edges_in_order(order: tuple[int, ...]) -> list[tuple[int, ...]]:
    return schreier_edges(list(order))


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


def find_pair_edge_extension(
    seed: set[int],
    lower: int,
    p: int,
    w: int,
    max_nodes: int,
) -> tuple[tuple[int, ...] | None, int]:
    """Try to fill two-sum coverage up to w while preserving one pair hole."""
    base = seed | {p}
    edge = (lower, p)
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

        for addition in sorted(additions, key=lambda item: (len(item), sum(item), item)):
            next_fillers = tuple(sorted(fillers | set(addition)))
            result = dfs(next_fillers)
            if result is not None:
                return result
        return None

    return dfs(tuple()), nodes


def pair_edge_search(max_p: int, max_u: int, max_nodes: int, max_found: int) -> None:
    """Search high-excess pair holes for the P5 seed edge {10,p}."""
    seed = {1, 2, 4, 5, 8, 10, 15, 18, 19, 30}
    old_vertices = (10, 15, 18, 19, 30)
    lower = 10
    found = 0
    checked = 0
    skipped_poisoned = 0
    print("P5 seed pair-edge extension search")
    print("  seed=", sorted(seed), "lower=", lower)
    print("  max_p=", max_p, "max_u=", max_u, "max_nodes=", max_nodes)

    for p in range(31, max_p + 1):
        for u in range(2, max_u + 1):
            w = p + u
            base = seed | {p}
            if w in hsum(base - {lower, p}, 3, w):
                skipped_poisoned += 1
                continue
            checked += 1
            fillers, nodes = find_pair_edge_extension(seed, lower, p, w, max_nodes)
            if fillers is None:
                continue
            elements = base | set(fillers)
            coverage = cover_end(elements, 2, w)
            vertices = tuple(x for x in sorted(elements) if x >= lower)
            core_vertices = (*old_vertices, p)
            core_order = supported_order(elements, core_vertices, coverage)
            core_failures = [
                edge
                for edge in schreier_edges(list(core_vertices))
                if witnesses_for_edges(elements, [edge], coverage) is None
            ]
            order = supported_order(elements, vertices, coverage)
            lower_pair_failures = [
                q
                for q in vertices
                if q != lower and witnesses_for_edges(elements, [(lower, q)], coverage) is None
            ]
            print(
                "  extension:",
                "p=", p,
                "u=", u,
                "w=", w,
                "fillers=", list(fillers),
                "coverage=", coverage,
                "core_order=", core_order,
                "core_failures=", core_failures[:8],
                "order=", order,
                "lower_pair_failures=", lower_pair_failures[:8],
                "nodes=", nodes,
            )
            found += 1
            if found >= max_found:
                print(
                    "stopped after max_found",
                    "checked=", checked,
                    "skipped_poisoned=", skipped_poisoned,
                )
                return

    print("no pair-edge extension found")
    print("  checked=", checked, "skipped_poisoned=", skipped_poisoned)


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


def p6_order_diagnostic() -> None:
    """Try all enumeration orders for the six P6 protected vertices."""
    elements = {1, 2, 4, 5, 8, 10, 15, 18, 19, 30, 38, 40, 43, 44}
    vertices = (10, 15, 18, 19, 30, 38)
    coverage = cover_end(elements, 2, 3 * max(elements))
    good_pairs = {
        frozenset(pair)
        for pair in combinations(vertices, 2)
        if witnesses_for_edges(elements, [pair], coverage) is not None
    }
    good_triples = {
        frozenset(triple)
        for triple in combinations(vertices, 3)
        if witnesses_for_edges(elements, [triple], coverage) is not None
    }
    first_candidates = [
        v
        for v in vertices
        if all(frozenset({v, u}) in good_pairs for u in vertices if u != v)
    ]
    print("order-prefix constraints")
    print("  first candidates=", first_candidates)
    for first in first_candidates:
        second_candidates = []
        after_first = tuple(v for v in vertices if v != first)
        for second in after_first:
            tail = tuple(v for v in after_first if v != second)
            if all(
                frozenset({second, a, b}) in good_triples
                for a, b in combinations(tail, 2)
            ):
                second_candidates.append(second)
        print("  after first=", first, "second candidates=", second_candidates)
    best: list[tuple[int, tuple[int, ...], list[tuple[int, ...]]]] = []
    for order in permutations(vertices):
        failed: list[tuple[int, ...]] = []
        for edge in schreier_edges_in_order(order):
            if witnesses_for_edges(elements, [edge], coverage) is None:
                failed.append(edge)
        if not failed:
            print("P6 enumeration-order success")
            print("  order=", order, "coverage_end=", coverage)
            return
        if not best or len(failed) < best[0][0]:
            best = [(len(failed), order, failed)]
        elif len(failed) == best[0][0] and len(best) < 5:
            best.append((len(failed), order, failed))

    print("no P6 enumeration order succeeds")
    print("  elements=", sorted(elements), "coverage_end=", coverage)
    print("  vertices=", vertices)
    print("  best failures:")
    for count, order, failed in best:
        print("   ", "count=", count, "order=", order, "failed=", failed[:10])


def supported_order(
    elements: set[int],
    vertices: tuple[int, ...],
    coverage: int,
) -> tuple[int, ...] | None:
    cache: dict[frozenset[int], bool] = {}

    def good(edge: frozenset[int]) -> bool:
        if edge not in cache:
            cache[edge] = (
                witnesses_for_edges(elements, [tuple(sorted(edge))], coverage)
                is not None
            )
        return cache[edge]

    def search(prefix: tuple[int, ...], remaining: tuple[int, ...]) -> tuple[int, ...] | None:
        position = len(prefix) + 1
        for vertex in remaining:
            tail = tuple(x for x in remaining if x != vertex)
            if position <= len(tail):
                if not all(
                    good(frozenset((vertex, *rest)))
                    for rest in combinations(tail, position)
                ):
                    continue
                result = search((*prefix, vertex), tail)
                if result is not None:
                    return result
            else:
                return (*prefix, vertex, *tail)
        return None

    return search(tuple(), vertices)


def generalized_prefix_order(
    elements: set[int],
    vertices: tuple[int, ...],
    coverage: int,
    min_tail_slack: int,
) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    cache: dict[frozenset[int], bool] = {}

    def good(edge: frozenset[int]) -> bool:
        if edge not in cache:
            cache[edge] = (
                witnesses_for_edges(elements, [tuple(sorted(edge))], coverage)
                is not None
            )
        return cache[edge]

    def rank_options(vertex: int, tail: tuple[int, ...]) -> list[int]:
        max_rank = len(tail) - min_tail_slack
        if max_rank < 1:
            return []
        options: list[int] = []
        for rank in range(1, max_rank + 1):
            if all(
                good(frozenset((vertex, *rest)))
                for rest in combinations(tail, rank)
            ):
                options.append(rank)
        return options

    def search(
        prefix: tuple[int, ...],
        ranks: tuple[int, ...],
        remaining: tuple[int, ...],
    ) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
        if not remaining:
            return prefix, ranks
        for vertex in remaining:
            tail = tuple(x for x in remaining if x != vertex)
            options = rank_options(vertex, tail)
            if not options:
                if len(tail) <= min_tail_slack:
                    return (*prefix, vertex, *tail), ranks
                continue
            for rank in options:
                result = search((*prefix, vertex), (*ranks, rank), tail)
                if result is not None:
                    return result
        return None

    return search(tuple(), tuple(), vertices)


def general_prefix_diagnostic(
    elements: set[int],
    vertices: tuple[int, ...],
    min_tail_slack: int,
) -> None:
    coverage = cover_end(elements, 2, 3 * max(elements))
    first_options: dict[int, list[int]] = {}
    for vertex in vertices:
        tail = tuple(x for x in vertices if x != vertex)
        options: list[int] = []
        max_rank = len(tail) - min_tail_slack
        for rank in range(1, max_rank + 1):
            edges = [(vertex, *rest) for rest in combinations(tail, rank)]
            if witnesses_for_edges(elements, edges, coverage) is not None:
                options.append(rank)
        first_options[vertex] = options

    general = generalized_prefix_order(
        elements,
        vertices,
        coverage,
        min_tail_slack,
    )
    schreier = supported_order(elements, vertices, coverage)
    print("generalized prefix-link diagnostic")
    print("  elements=", sorted(elements))
    print("  vertices=", vertices)
    print("  coverage_end=", coverage)
    print("  min_tail_slack=", min_tail_slack)
    print("  first_rank_options=", first_options)
    print("  first_schreier_order=", schreier)
    if general is None:
        print("  generalized_shell=None")
    else:
        order, ranks = general
        print("  generalized_shell_order=", order)
        print("  ranks=", ranks)


def p6_enum_search(max_p6: int, max_extra_count: int, max_extra_value: int) -> None:
    """Bounded search for a P6 extension with arbitrary enumeration order."""
    seed = {1, 2, 4, 5, 8, 10, 15, 18, 19, 30}
    old_vertices = (10, 15, 18, 19, 30)
    checked = 0
    for p6 in range(31, max_p6 + 1):
        vertices = (*old_vertices, p6)
        extra_pool = range(p6 + 1, max_extra_value + 1)
        for extra_count in range(max_extra_count + 1):
            for extras in combinations(extra_pool, extra_count):
                elements = seed | {p6} | set(extras)
                coverage = cover_end(elements, 2, 3 * max(elements) + 40)
                if coverage < max(vertices):
                    continue
                checked += 1
                order = supported_order(elements, vertices, coverage)
                if order is not None:
                    print("P6 enumeration extension")
                    print(
                        "  p6=", p6,
                        "extras=", extras,
                        "coverage_end=", coverage,
                        "order=", order,
                    )
                    return
        print("checked p6=", p6, "total_candidates=", checked)
    print("no P6 enumeration extension found")
    print(
        "  max_p6=", max_p6,
        "max_extra_count=", max_extra_count,
        "max_extra_value=", max_extra_value,
        "checked=", checked,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extend-first", action="store_true")
    parser.add_argument("--tail-chain", action="store_true")
    parser.add_argument("--p6-pair-diagnostic", action="store_true")
    parser.add_argument("--p6-order-diagnostic", action="store_true")
    parser.add_argument("--p6-enum-search", action="store_true")
    parser.add_argument("--pair-edge-search", action="store_true")
    parser.add_argument("--general-prefix-diagnostic", action="store_true")
    parser.add_argument("--max-value", type=int, default=23)
    parser.add_argument("--max-size", type=int, default=10)
    parser.add_argument("--protected-count", type=int, default=4)
    parser.add_argument("--min-protected", type=int)
    parser.add_argument("--max-new", type=int, default=4)
    parser.add_argument("--max-candidate", type=int, default=35)
    parser.add_argument("--max-p6", type=int, default=120)
    parser.add_argument("--max-extra", type=int, default=3)
    parser.add_argument("--max-extra-value", type=int, default=151)
    parser.add_argument("--max-u", type=int, default=80)
    parser.add_argument("--max-nodes", type=int, default=50_000)
    parser.add_argument("--max-found", type=int, default=5)
    parser.add_argument("--min-tail-slack", type=int, default=0)
    parser.add_argument(
        "--diagnostic-elements",
        default="1,2,4,5,8,10,15,18,19,30,38,40,43,44",
    )
    parser.add_argument("--diagnostic-vertices", default="10,15,18,19,30,38")
    args = parser.parse_args()
    if args.extend_first:
        extend_first(args.max_new, args.max_candidate)
    elif args.tail_chain:
        check_tail_chain(args.max_p6, args.max_extra, args.max_extra_value)
    elif args.p6_pair_diagnostic:
        p6_pair_diagnostic()
    elif args.p6_order_diagnostic:
        p6_order_diagnostic()
    elif args.p6_enum_search:
        p6_enum_search(args.max_p6, args.max_extra, args.max_extra_value)
    elif args.pair_edge_search:
        pair_edge_search(args.max_p6, args.max_u, args.max_nodes, args.max_found)
    elif args.general_prefix_diagnostic:
        general_prefix_diagnostic(
            parse_int_set(args.diagnostic_elements),
            parse_int_tuple(args.diagnostic_vertices),
            args.min_tail_slack,
        )
    else:
        search_protected(
            args.max_value,
            args.max_size,
            args.protected_count,
            args.min_protected,
        )


if __name__ == "__main__":
    main()
