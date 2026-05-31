#!/usr/bin/env python3
"""Boundary sequence check for the remaining prime-71 candidate.

The candidate has tile sides

    a=(beta,gamma), b=(alpha,gamma), c=(alpha,beta)

and outer sides 4c, 4c, and 8b+4a.  At both base corners the boundary b-edge
must use its alpha endpoint, because the equal side is forced to use c and the
corner angle is alpha.

This script enumerates all base orders and orientations.  A straight boundary
point cannot have two gamma endpoints, since 2 gamma = 4pi/3 > pi.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product


ANGLE = str
Side = str
OrientedEdge = tuple[ANGLE, ANGLE]


SIDE_ENDPOINTS: dict[Side, tuple[ANGLE, ANGLE]] = {
    "a": ("beta", "gamma"),
    "b": ("alpha", "gamma"),
    "c": ("alpha", "beta"),
}

S0 = Counter({"alpha": 3, "beta": 3})
S1 = Counter({"alpha": 1, "beta": 1, "gamma": 1})


def orientations(side: Side) -> tuple[OrientedEdge, OrientedEdge]:
    left, right = SIDE_ENDPOINTS[side]
    return ((left, right), (right, left))


def straight_types(left_endpoint: ANGLE, right_endpoint: ANGLE) -> set[str]:
    """Return the straight vertex types compatible with two boundary endpoints."""
    used = Counter([left_endpoint, right_endpoint])
    out: set[str] = set()
    if all(used[key] <= S0[key] for key in used):
        out.add("S0")
    if all(used[key] <= S1[key] for key in used):
        out.add("S1")
    return out


def base_orders() -> list[tuple[Side, ...]]:
    """All base orders with eight b-edges and four a-edges, b at both corners."""
    orders: list[tuple[Side, ...]] = []
    inner_positions = range(1, 11)
    for a_positions in combinations(inner_positions, 4):
        row = ["b"] * 12
        for idx in a_positions:
            row[idx] = "a"
        orders.append(tuple(row))
    return orders


def oriented_rows(order: tuple[Side, ...]) -> list[tuple[OrientedEdge, ...]]:
    """Orient a base order from left to right with alpha endpoints at corners."""
    options: list[tuple[OrientedEdge, ...]] = []
    for side in order:
        options.append(orientations(side))

    rows: list[tuple[OrientedEdge, ...]] = []
    for choice in product(*options):
        if choice[0][0] != "alpha":
            continue
        if choice[-1][1] != "alpha":
            continue
        rows.append(choice)
    return rows


def feasible_type_counts_for_row(row: tuple[OrientedEdge, ...]) -> set[tuple[int, int]]:
    """Feasible (b0,b1) counts for the eleven non-corner base vertices."""
    possible: set[tuple[int, int]] = {(0, 0)}
    for left_edge, right_edge in zip(row, row[1:]):
        types = straight_types(left_edge[1], right_edge[0])
        if not types:
            return set()
        next_possible: set[tuple[int, int]] = set()
        for b0, b1 in possible:
            if "S0" in types:
                next_possible.add((b0 + 1, b1))
            if "S1" in types:
                next_possible.add((b0, b1 + 1))
        possible = next_possible
    return possible


def equal_side_type_counts() -> set[tuple[int, int]]:
    """Feasible (b0,b1) totals over both forced 4c equal sides.

    The six non-corner equal-side vertices are included here.  The base-corner
    endpoint is alpha on each equal side.  The apex must not present alpha
    endpoints from both equal sides, because the apex angle has only one alpha
    in the generic alpha+3beta representation.
    """
    out: set[tuple[int, int]] = set()
    for left_choices in product(orientations("c"), repeat=4):
        if left_choices[0][0] != "alpha":
            continue
        left_counts = feasible_type_counts_for_equal_side(left_choices)
        if not left_counts:
            continue
        left_apex_endpoint = left_choices[-1][1]
        for right_choices in product(orientations("c"), repeat=4):
            # Traverse the right equal side from apex to the right base corner.
            if right_choices[-1][1] != "alpha":
                continue
            right_counts = feasible_type_counts_for_equal_side(right_choices)
            if not right_counts:
                continue
            right_apex_endpoint = right_choices[0][0]
            if left_apex_endpoint == right_apex_endpoint == "alpha":
                continue
            for l0, l1 in left_counts:
                for r0, r1 in right_counts:
                    out.add((l0 + r0, l1 + r1))
    return out


def feasible_type_counts_for_equal_side(row: tuple[OrientedEdge, ...]) -> set[tuple[int, int]]:
    counts: set[tuple[int, int]] = {(0, 0)}
    for left_edge, right_edge in zip(row, row[1:]):
        types = straight_types(left_edge[1], right_edge[0])
        if not types:
            return set()
        next_counts: set[tuple[int, int]] = set()
        for b0, b1 in counts:
            if "S0" in types:
                next_counts.add((b0 + 1, b1))
            if "S1" in types:
                next_counts.add((b0, b1 + 1))
        counts = next_counts
    return counts


def main() -> None:
    orders = base_orders()
    oriented_total = 0
    locally_valid_rows = 0
    base_counts: set[tuple[int, int]] = set()

    for order in orders:
        rows = oriented_rows(order)
        oriented_total += len(rows)
        for row in rows:
            counts = feasible_type_counts_for_row(row)
            if counts:
                locally_valid_rows += 1
                base_counts.update(counts)

    equal_counts = equal_side_type_counts()
    total_counts = {
        (e0 + b0, e1 + b1)
        for e0, e1 in equal_counts
        for b0, b1 in base_counts
    }

    print("prime-71 boundary sequence orientation check")
    print("base decomposition: 8 b-edges and 4 a-edges, with b at both corners")
    print(f"base orders checked: {len(orders)}")
    print(f"base orientations with alpha endpoints at both corners: {oriented_total}")
    print(f"valid base orientations: {locally_valid_rows}")
    print(f"feasible base (b0,b1) counts: {sorted(base_counts)}")
    print(f"feasible equal-side (b0,b1) counts: {sorted(equal_counts)}")
    print(f"feasible full-boundary (b0,b1) counts: {sorted(total_counts)}")
    print(
        "obstruction: a and b each have exactly one gamma endpoint; starting "
        "with alpha at the left base corner and forbidding gamma-gamma at a "
        "straight boundary vertex forces every base edge to end at gamma, "
        "contradicting the required alpha endpoint at the right base corner"
    )


if __name__ == "__main__":
    main()
