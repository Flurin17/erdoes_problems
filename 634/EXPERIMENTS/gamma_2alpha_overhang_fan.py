#!/usr/bin/env python3
"""Overhang-aware local fan diagnostics for the `gamma=2alpha` branch.

The strict endpoint automaton assumes that every interior ray in a boundary fan
has the same side label on both sides.  This diagnostic weakens that assumption:
two adjacent fan sectors may be separated by a primitive equal-length side-string
pair, such as `a+c = k b`, emanating from the boundary point.

This is still only local evidence.  It does not prove that a full tiling exists.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import candidates_for_n  # noqa: E402
from gamma_2alpha_endpoint_automaton import (  # noqa: E402
    ANGLE_SIDES,
    SIDE_ENDPOINTS,
    STRAIGHT_TYPES,
    PlacedEdge,
    orientations,
    other_side,
    straight_transition,
)


SideString = tuple[str, ...]
SideLengths = tuple[int, int, int]

SIDE_INDEX = {"a": 0, "b": 1, "c": 2}


def side_string_text(seq: SideString) -> str:
    return "".join(seq)


def side_string_length(seq: SideString, sides: SideLengths) -> int:
    return sum(sides[SIDE_INDEX[side]] for side in seq)


def side_string_cuts(seq: SideString, sides: SideLengths) -> frozenset[int]:
    total = 0
    cuts: set[int] = set()
    for side in seq[:-1]:
        total += sides[SIDE_INDEX[side]]
        cuts.add(total)
    return frozenset(cuts)


@lru_cache(maxsize=None)
def strings_up_to(max_pieces: int) -> tuple[SideString, ...]:
    out: list[SideString] = []
    for size in range(1, max_pieces + 1):
        out.extend(tuple(seq) for seq in product(("a", "b", "c"), repeat=size))
    return tuple(out)


@lru_cache(maxsize=None)
def path_ok_with_start(seq: SideString, start_angle: str, mode: str) -> bool:
    states = [edge for edge in orientations(seq[0]) if edge.start == start_angle]
    for side in seq[1:]:
        next_states = []
        for previous in states:
            for edge in orientations(side):
                if straight_transition(previous, edge, mode):
                    next_states.append(edge)
        states = next_states
        if not states:
            return False
    return bool(states)


def primitive_component(
    left_side: str,
    left_angle: str,
    right_side: str,
    right_angle: str,
    sides: SideLengths,
    *,
    max_pieces: int,
    mode: str,
) -> tuple[SideString, SideString] | None:
    """Return one primitive interface component starting with the requested data."""
    if (
        left_side == right_side
        and left_angle in SIDE_ENDPOINTS[left_side]
        and right_angle in SIDE_ENDPOINTS[right_side]
    ):
        return ((left_side,), (right_side,))

    left_options: list[SideString] = []
    right_by_length: dict[int, list[SideString]] = {}
    for seq in strings_up_to(max_pieces):
        if seq[0] == left_side and path_ok_with_start(seq, left_angle, mode):
            left_options.append(seq)
        if seq[0] == right_side and path_ok_with_start(seq, right_angle, mode):
            right_by_length.setdefault(side_string_length(seq, sides), []).append(seq)

    for left in left_options:
        length = side_string_length(left, sides)
        left_cuts = side_string_cuts(left, sides)
        for right in right_by_length.get(length, []):
            if left_cuts.isdisjoint(side_string_cuts(right, sides)):
                return (left, right)
    return None


def other_label_at_angle(side: str, angle: str) -> str:
    first, second = ANGLE_SIDES[angle]
    if side == first:
        return second
    if side == second:
        return first
    raise ValueError((side, angle))


def visible_angle_compatible(left: PlacedEdge, right: PlacedEdge) -> bool:
    visible = Counter([left.end, right.start])
    return any(all(visible[key] <= target[key] for key in visible) for target in STRAIGHT_TYPES)


def overhang_fans(
    left: PlacedEdge,
    right: PlacedEdge,
    sides: SideLengths,
    *,
    max_pieces: int,
    mode: str,
) -> tuple[tuple[list[str], list[tuple[str, str, str, str, SideString, SideString]]], ...]:
    visible = Counter([left.end, right.start])
    out: list[tuple[list[str], list[tuple[str, str, str, str, SideString, SideString]]]] = []

    for target in STRAIGHT_TYPES:
        if any(visible[key] > target[key] for key in visible):
            continue
        internal_angles = list((target - visible).elements())
        for internal_order in set(permutations(internal_angles)):
            angles = [left.end, *internal_order, right.start]
            states: list[tuple[str, list[tuple[str, str, str, str, SideString, SideString]]]] = [
                (other_side(left, left.end), [])
            ]
            for index, angle in enumerate(internal_order, start=1):
                next_states = []
                previous_angle = angles[index - 1]
                for previous_side, components in states:
                    for incoming_side in ANGLE_SIDES[angle]:
                        component = primitive_component(
                            previous_side,
                            previous_angle,
                            incoming_side,
                            angle,
                            sides,
                            max_pieces=max_pieces,
                            mode=mode,
                        )
                        if component is None:
                            continue
                        outgoing_side = other_label_at_angle(incoming_side, angle)
                        next_states.append(
                            (
                                outgoing_side,
                                [
                                    *components,
                                    (
                                        previous_side,
                                        previous_angle,
                                        incoming_side,
                                        angle,
                                        component[0],
                                        component[1],
                                    ),
                                ],
                            )
                        )
                states = next_states

            last_incoming_side = other_side(right, right.start)
            previous_angle = angles[-2]
            for previous_side, components in states:
                component = primitive_component(
                    previous_side,
                    previous_angle,
                    last_incoming_side,
                    right.start,
                    sides,
                    max_pieces=max_pieces,
                    mode=mode,
                )
                if component is None:
                    continue
                out.append(
                    (
                        angles,
                        [
                            *components,
                            (
                                previous_side,
                                previous_angle,
                                last_incoming_side,
                                right.start,
                                component[0],
                                component[1],
                            ),
                        ],
                    )
                )
    return tuple(out)


def edge_text(edge: PlacedEdge) -> str:
    return f"{edge.side}:{edge.start}->{edge.end}"


def component_text(component: tuple[str, str, str, str, SideString, SideString]) -> str:
    left_side, left_angle, right_side, right_angle, left, right = component
    return (
        f"{left_side}:{left_angle} to {right_side}:{right_angle} via "
        f"{side_string_text(left)} | {side_string_text(right)}"
    )


def relevant_transition(left: PlacedEdge, right: PlacedEdge, only_mixed_c: bool) -> bool:
    if not visible_angle_compatible(left, right):
        return False
    if not only_mixed_c:
        return True
    return (left.side == "c") != (right.side == "c")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--max-pieces", type=int, default=6)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--mode", choices=("angle", "fan"), default="angle")
    parser.add_argument(
        "--all-transitions",
        action="store_true",
        help="also show transitions that do not mix c with a/b",
    )
    args = parser.parse_args()

    placed_edges = tuple(edge for side in ("a", "b", "c") for edge in orientations(side))
    for n in args.n:
        print(f"N={n}:")
        for row in candidates_for_n(n):
            print(f"  tile={row.tile}")
            shown = 0
            for left in placed_edges:
                for right in placed_edges:
                    if not relevant_transition(left, right, not args.all_transitions):
                        continue
                    fans = overhang_fans(
                        left,
                        right,
                        row.tile,
                        max_pieces=args.max_pieces,
                        mode=args.mode,
                    )
                    if not fans:
                        print(f"    {edge_text(left)} -> {edge_text(right)}: no local fan")
                        shown += 1
                        continue
                    angles, components = fans[0]
                    print(
                        f"    {edge_text(left)} -> {edge_text(right)}: "
                        f"{len(fans)} local fan(s); angles={','.join(angles)}"
                    )
                    for component in components:
                        left_seq = component[4]
                        right_seq = component[5]
                        if left_seq != right_seq:
                            print(f"      {component_text(component)}")
                    shown += 1
                    if shown >= args.limit:
                        break
                if shown >= args.limit:
                    break


if __name__ == "__main__":
    main()
