#!/usr/bin/env python3
"""Boundary-word automaton for isosceles gamma=2pi/3 prime candidates.

For the remaining prime candidates in Beeson's isosceles gamma=2pi/3 filter,
the equal sides are empirically forced to be t copies of c in the searched
range.  Under that condition, each base corner forces a b-edge at its alpha
endpoint.  This script checks whether any base decomposition admits an oriented
boundary word between those two forced b-edges.

Endpoint labels:

    a = (beta,gamma), b = (alpha,gamma), c = (alpha,beta).

At a straight boundary transition, the visible endpoint angles must fit into one
of the straight types alpha+beta+gamma or 3alpha+3beta.  The stronger check
implemented here also enforces the local side-label star: after the two boundary
tiles use their boundary sides, the inward side labels must be connectable by
the remaining tile angles at that vertex.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache

from gamma_2pi3_isosceles_filter import Candidate, prime_candidates
from isosceles_prime_family import decompositions, recover_parameters


Angle = str
Side = str
OrientedEdge = tuple[Angle, Angle]
PlacedEdge = tuple[Side, Angle, Angle]


SIDE_ENDPOINTS: dict[Side, tuple[Angle, Angle]] = {
    "a": ("beta", "gamma"),
    "b": ("alpha", "gamma"),
    "c": ("alpha", "beta"),
}
ANGLE_SIDES: dict[Angle, tuple[Side, Side]] = {
    "alpha": ("b", "c"),
    "beta": ("a", "c"),
    "gamma": ("a", "b"),
}

S0 = Counter({"alpha": 3, "beta": 3})
S1 = Counter({"alpha": 1, "beta": 1, "gamma": 1})


def orientations(side: Side) -> tuple[OrientedEdge, OrientedEdge]:
    left, right = SIDE_ENDPOINTS[side]
    return ((left, right), (right, left))


def placed_orientations(side: Side) -> tuple[PlacedEdge, PlacedEdge]:
    return tuple((side, start, end) for start, end in orientations(side))  # type: ignore[return-value]


def other_side(boundary_side: Side, endpoint_angle: Angle) -> Side:
    first, second = ANGLE_SIDES[endpoint_angle]
    if boundary_side == first:
        return second
    if boundary_side == second:
        return first
    raise ValueError((boundary_side, endpoint_angle))


def trail_possible(edge_counts: Counter[Angle], start: Side, end: Side) -> bool:
    """Can the internal angle multiset connect inward side labels start -> end?"""
    counts = Counter(edge_counts)
    total = sum(counts.values())

    def rec(current: Side, remaining: int) -> bool:
        if remaining == 0:
            return current == end
        for angle in ("alpha", "beta", "gamma"):
            if counts[angle] == 0:
                continue
            first, second = ANGLE_SIDES[angle]
            if current not in (first, second):
                continue
            counts[angle] -= 1
            next_side = second if current == first else first
            if rec(next_side, remaining - 1):
                return True
            counts[angle] += 1
        return False

    return rec(start, total)


def transition_types(left: PlacedEdge, right: PlacedEdge) -> set[str]:
    """Straight boundary vertex types compatible with side labels and angles."""
    left_side, _, left_angle = left
    right_side, right_angle, _ = right
    visible = Counter([left_angle, right_angle])
    start = other_side(left_side, left_angle)
    end = other_side(right_side, right_angle)
    out: set[str] = set()
    for label, target in (("S0", S0), ("S1", S1)):
        if not all(visible[key] <= target[key] for key in visible):
            continue
        internal = target - visible
        if trail_possible(internal, start, end):
            out.add(label)
    return out


def has_base_word(nb: int, na: int, nc: int) -> bool:
    """Can a base with these side counts start/end with b at alpha endpoints?"""
    if nb < 2:
        return False

    # Reserve the forced first edge b: alpha -> gamma and final edge
    # b: gamma -> alpha.  The DP fills the middle and checks the transition into
    # the final forced b-edge.
    start_edge: PlacedEdge = ("b", "alpha", "gamma")
    final_edge: PlacedEdge = ("b", "gamma", "alpha")

    @lru_cache(maxsize=None)
    def can(
        remaining_b: int,
        remaining_a: int,
        remaining_c: int,
        prev_side: Side,
        prev_start: Angle,
        prev_end: Angle,
    ) -> bool:
        previous = (prev_side, prev_start, prev_end)
        if remaining_b == remaining_a == remaining_c == 0:
            return bool(transition_types(previous, final_edge))
        for side, remaining in (
            ("b", remaining_b),
            ("a", remaining_a),
            ("c", remaining_c),
        ):
            if remaining == 0:
                continue
            for placed in placed_orientations(side):
                if not transition_types(previous, placed):
                    continue
                next_b = remaining_b - (side == "b")
                next_a = remaining_a - (side == "a")
                next_c = remaining_c - (side == "c")
                if can(next_b, next_a, next_c, *placed):
                    return True
        return False

    return can(nb - 2, na, nc, *start_edge)


def viable_base_decompositions(candidate: Candidate) -> list[tuple[int, int, int, int]]:
    a, b, c = candidate.sides
    equal = decompositions(candidate.outer_equal_side, candidate.sides)
    equal_unique_c = equal == [(0, 0, candidate.m, candidate.m)]
    base = decompositions(candidate.outer_base, candidate.sides)
    if not equal_unique_c:
        return []
    return [row for row in base if row[0] >= 2]


def candidate_report(candidate: Candidate) -> tuple[list[str], bool]:
    params = recover_parameters(candidate)
    lines = [
        (
            f"N={candidate.n}, (r,s)=({params.r},{params.s}), "
            f"sides={candidate.sides}, t={candidate.m}"
        )
    ]
    any_word = False
    viable = viable_base_decompositions(candidate)
    if not viable:
        lines.append("  no viable base decompositions after forcing b at both base corners")
        return lines, False
    for nb, na, nc, edge_count in viable:
        ok = has_base_word(nb, na, nc)
        any_word = any_word or ok
        status = "boundary word exists" if ok else "boundary-word obstructed"
        lines.append(f"  base (b,a,c)=({nb},{na},{nc}), edges={edge_count}: {status}")
    return lines, any_word


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=20_000)
    args = parser.parse_args()

    candidates = prime_candidates(args.limit)
    obstructed: list[int] = []
    survivors: list[int] = []
    print(f"prime isosceles boundary-word check up to {args.limit}: {len(candidates)}")
    for candidate in candidates:
        lines, any_word = candidate_report(candidate)
        for line in lines:
            print(line)
        if any_word:
            survivors.append(candidate.n)
        else:
            obstructed.append(candidate.n)
    print(f"boundary-word obstructed candidates: {obstructed}")
    print(f"boundary-word survivors: {survivors}")


if __name__ == "__main__":
    main()
