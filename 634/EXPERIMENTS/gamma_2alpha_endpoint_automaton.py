#!/usr/bin/env python3
"""Boundary endpoint automaton for Beeson's `gamma=2alpha` isosceles branch.

This is an experimental necessary-condition checker layered on top of
`gamma_2alpha_boundary.py`.  It does not search the interior of the tiling.

The key conservative convention is that Beeson's Lemma 11.11 bounds only one of
the two equal sides of the outer isosceles triangle.  Therefore, when testing a
candidate, one equal side is taken from the bounded `X` representations produced
by Lemma 11.14, while the other equal side may use any representation of the
same length satisfying the Lemma 11.13 `b`- and `c`-edge condition.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Iterable, NamedTuple


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import (  # noqa: E402
    BoundaryCandidate,
    candidates_for_n,
    side_representations,
)


Angle = str
Side = str
Triple = tuple[int, int, int]


class PlacedEdge(NamedTuple):
    side: Side
    start: Angle
    end: Angle


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

# At a straight boundary point the total angle is pi = 3*alpha + beta.
STRAIGHT_TYPES: tuple[Counter[Angle], ...] = (
    Counter({"alpha": 3, "beta": 1}),
    Counter({"alpha": 1, "beta": 1, "gamma": 1}),
)


def rep_text(rep: Triple) -> str:
    return f"{rep[0]}a+{rep[1]}b+{rep[2]}c"


def orientations(side: Side) -> tuple[PlacedEdge, PlacedEdge]:
    start, end = SIDE_ENDPOINTS[side]
    return (PlacedEdge(side, start, end), PlacedEdge(side, end, start))


def other_side(edge: PlacedEdge, angle: Angle) -> Side:
    first, second = ANGLE_SIDES[angle]
    if edge.side == first:
        return second
    if edge.side == second:
        return first
    raise ValueError((edge, angle))


def trail_possible(internal: Counter[Angle], start: Side, end: Side) -> bool:
    """Return whether remaining vertex angles can connect two inward side labels."""

    counts = Counter(internal)

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
                counts[angle] += 1
                return True
            counts[angle] += 1
        return False

    return rec(start, sum(counts.values()))


def straight_transition(left: PlacedEdge, right: PlacedEdge, mode: str) -> bool:
    visible = Counter([left.end, right.start])
    if mode == "angle":
        return any(
            all(visible[key] <= target[key] for key in visible)
            for target in STRAIGHT_TYPES
        )

    start = other_side(left, left.end)
    end = other_side(right, right.start)
    for target in STRAIGHT_TYPES:
        if any(visible[key] > target[key] for key in visible):
            continue
        if trail_possible(target - visible, start, end):
            return True
    return False


@lru_cache(maxsize=None)
def path_endpoint_pairs(rep: Triple, mode: str) -> frozenset[tuple[PlacedEdge, PlacedEdge]]:
    """All possible first/last oriented boundary edges for a valid side path."""

    @lru_cache(maxsize=None)
    def completions(remaining: Triple, previous: PlacedEdge) -> frozenset[PlacedEdge]:
        if remaining == (0, 0, 0):
            return frozenset([previous])

        out: set[PlacedEdge] = set()
        counts = {"a": remaining[0], "b": remaining[1], "c": remaining[2]}
        for side in ("a", "b", "c"):
            if counts[side] == 0:
                continue
            next_counts = dict(counts)
            next_counts[side] -= 1
            next_remaining = (next_counts["a"], next_counts["b"], next_counts["c"])
            for placed in orientations(side):
                if not straight_transition(previous, placed, mode):
                    continue
                out.update(completions(next_remaining, placed))
        return frozenset(out)

    out: set[tuple[PlacedEdge, PlacedEdge]] = set()
    counts = {"a": rep[0], "b": rep[1], "c": rep[2]}
    for side in ("a", "b", "c"):
        if counts[side] == 0:
            continue
        next_counts = dict(counts)
        next_counts[side] -= 1
        remaining = (next_counts["a"], next_counts["b"], next_counts["c"])
        for first in orientations(side):
            for last in completions(remaining, first):
                out.add((first, last))
    return frozenset(out)


def alpha_corner(incoming: PlacedEdge, outgoing: PlacedEdge) -> bool:
    """A base corner has one tile angle `alpha`, hence boundary sides `b` and `c`."""

    return (
        incoming.end == "alpha"
        and outgoing.start == "alpha"
        and {incoming.side, outgoing.side} == {"b", "c"}
    )


def apex_corner(incoming: PlacedEdge, outgoing: PlacedEdge) -> bool:
    """The apex angle is `alpha+beta`, realized by two tiles sharing an edge."""

    if Counter([incoming.end, outgoing.start]) != Counter(["alpha", "beta"]):
        return False
    return other_side(incoming, incoming.end) == other_side(outgoing, outgoing.start)


class Witness(NamedTuple):
    short_side: str
    left_rep: Triple
    right_rep: Triple
    base_rep: Triple
    left_endpoints: tuple[PlacedEdge, PlacedEdge]
    right_endpoints: tuple[PlacedEdge, PlacedEdge]
    base_endpoints: tuple[PlacedEdge, PlacedEdge]


def rejected_by_beeson_one_c_corner(witness: Witness) -> bool:
    """Combination-level extension of the first half of Beeson Lemma 11.17.

    If both equal sides have exactly one `c` edge, Beeson proves at each base
    corner that the corner tile cannot put its `c` edge on the equal side.
    Hence the base must contain the `c` edge from both base-corner tiles.  The
    zero-`c` base case is therefore impossible; the one- and two-`c` cases are
    exactly the stated Lemma 11.17 obstruction.
    """

    return witness.left_rep[2] == witness.right_rep[2] == 1 and witness.base_rep[2] <= 2


def any_rep_paths(
    reps: Iterable[Triple],
    mode: str,
) -> dict[Triple, frozenset[tuple[PlacedEdge, PlacedEdge]]]:
    return {rep: path_endpoint_pairs(rep, mode) for rep in reps}


def witnesses_for_candidate(row: BoundaryCandidate, mode: str) -> list[Witness]:
    bounded_x_reps = row.x_representations
    all_x_reps = side_representations(row.x, row.tile, require_qr=True)
    y_reps = tuple(rep for rep in row.y_representations if sum(rep) >= 4)

    left_short_pairs = any_rep_paths(bounded_x_reps, mode)
    free_x_pairs = any_rep_paths(all_x_reps, mode)
    base_pairs = any_rep_paths(y_reps, mode)

    witnesses: list[Witness] = []

    def combine(
        *,
        short_side: str,
        left_pairs: dict[Triple, frozenset[tuple[PlacedEdge, PlacedEdge]]],
        right_pairs: dict[Triple, frozenset[tuple[PlacedEdge, PlacedEdge]]],
    ) -> None:
        for left_rep, left_options in left_pairs.items():
            for right_rep, right_options in right_pairs.items():
                for base_rep, base_options in base_pairs.items():
                    for left in left_options:
                        for right in right_options:
                            if not apex_corner(left[1], right[0]):
                                continue
                            for base in base_options:
                                if not alpha_corner(base[1], left[0]):
                                    continue
                                if not alpha_corner(right[1], base[0]):
                                    continue
                                witnesses.append(
                                    Witness(
                                        short_side=short_side,
                                        left_rep=left_rep,
                                        right_rep=right_rep,
                                        base_rep=base_rep,
                                        left_endpoints=left,
                                        right_endpoints=right,
                                        base_endpoints=base,
                                    )
                                )

    combine(short_side="left", left_pairs=left_short_pairs, right_pairs=free_x_pairs)
    combine(short_side="right", left_pairs=free_x_pairs, right_pairs=left_short_pairs)
    return witnesses


def edge_text(edge: PlacedEdge) -> str:
    return f"{edge.side}:{edge.start}->{edge.end}"


def witness_text(witness: Witness) -> str:
    return (
        f"short={witness.short_side}; "
        f"L={rep_text(witness.left_rep)} [{edge_text(witness.left_endpoints[0])} ... "
        f"{edge_text(witness.left_endpoints[1])}], "
        f"R={rep_text(witness.right_rep)} [{edge_text(witness.right_endpoints[0])} ... "
        f"{edge_text(witness.right_endpoints[1])}], "
        f"B={rep_text(witness.base_rep)} [{edge_text(witness.base_endpoints[0])} ... "
        f"{edge_text(witness.base_endpoints[1])}]"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument(
        "--mode",
        choices=("angle", "fan"),
        default="angle",
        help=(
            "`angle` checks only endpoint angle compatibility at straight "
            "boundary points; `fan` also checks a local side-label fan."
        ),
    )
    parser.add_argument(
        "--beeson-corner-filter",
        action="store_true",
        help=(
            "drop combinations with one `c` on both equal sides and at most "
            "two on the base"
        ),
    )
    args = parser.parse_args()

    for n in args.n:
        rows = candidates_for_n(n)
        print(f"N={n}: {len(rows)} boundary-arithmetic candidate(s)")
        for row in rows:
            witnesses = witnesses_for_candidate(row, args.mode)
            if args.beeson_corner_filter:
                witnesses = [
                    witness
                    for witness in witnesses
                    if not rejected_by_beeson_one_c_corner(witness)
                ]
            print(
                f"  tile={row.tile}, X={row.x}, Y={row.y}: "
                f"{len(witnesses)} endpoint witness(es) [{args.mode}]"
            )
            for witness in witnesses[: args.limit]:
                print(f"    {witness_text(witness)}")
            if len(witnesses) > args.limit:
                print(f"    ... {len(witnesses) - args.limit} more")


if __name__ == "__main__":
    main()
