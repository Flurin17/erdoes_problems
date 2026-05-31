#!/usr/bin/env python3
"""Boundary-star check for equilateral outer triangles and pi/3 tiles.

For a tile with angles `(alpha,beta,gamma)` and `gamma=pi/3`, the generic
relations are `alpha+beta=2pi/3` with `alpha/pi,beta/pi` irrational.  Hence a
straight boundary vertex has one of the two angle types

    alpha + beta + gamma = pi,        3gamma = pi.

At an equilateral corner the outer angle is exactly one `gamma` tile angle, so
the incident boundary side labels must be `a` and `b` around that corner.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import cache, lru_cache
from math import isqrt


Angle = str


@dataclass(frozen=True)
class State:
    label: str
    start: Angle
    end: Angle

    def __str__(self) -> str:
        return f"{self.label}:{self.start}->{self.end}"


STATES = (
    State("a", "beta", "gamma"),
    State("a", "gamma", "beta"),
    State("b", "alpha", "gamma"),
    State("b", "gamma", "alpha"),
    State("c", "alpha", "beta"),
    State("c", "beta", "alpha"),
)

ANGLE_SIDES = {
    "alpha": ("b", "c"),
    "beta": ("a", "c"),
    "gamma": ("a", "b"),
}

STRAIGHT_TYPES = (
    {"alpha": 1, "beta": 1, "gamma": 1},
    {"alpha": 0, "beta": 0, "gamma": 3},
)


def length_of(state: State, sides: tuple[int, int, int]) -> int:
    return sides["abc".index(state.label)]


def other_side(label: str, angle: Angle) -> str:
    left, right = ANGLE_SIDES[angle]
    if label == left:
        return right
    if label == right:
        return left
    raise ValueError((label, angle))


def straight_transition(prev: State, nxt: State) -> bool:
    for straight_type in STRAIGHT_TYPES:
        counts = dict(straight_type)
        counts[prev.end] -= 1
        counts[nxt.start] -= 1
        if any(value < 0 for value in counts.values()):
            continue

        start_label = other_side(prev.label, prev.end)
        target_label = other_side(nxt.label, nxt.start)
        middle_angles: list[Angle] = []
        for angle, count in counts.items():
            middle_angles.extend([angle] * count)

        @lru_cache(maxsize=None)
        def can_chain(current_label: str, remaining: tuple[Angle, ...]) -> bool:
            if not remaining:
                return current_label == target_label
            remaining_list = list(remaining)
            for index, angle in enumerate(remaining_list):
                if current_label not in ANGLE_SIDES[angle]:
                    continue
                next_label = other_side(current_label, angle)
                reduced = tuple(remaining_list[:index] + remaining_list[index + 1 :])
                if can_chain(next_label, reduced):
                    return True
            return False

        if can_chain(start_label, tuple(sorted(middle_angles))):
            return True
    return False


STRAIGHT_NEXT: dict[State, tuple[State, ...]] = {
    state: tuple(candidate for candidate in STATES if straight_transition(state, candidate))
    for state in STATES
}


def corner_transition(prev: State, nxt: State) -> bool:
    return (
        prev.end == "gamma"
        and nxt.start == "gamma"
        and {prev.label, nxt.label} == {"a", "b"}
    )


def valid_pi_tile(sides: tuple[int, int, int]) -> bool:
    a, b, c = sides
    return c * c == a * a - a * b + b * b


def side_paths(side_length: int, sides: tuple[int, int, int]) -> list[tuple[State, ...]]:
    @cache
    def extend(current: State, remaining: int) -> tuple[tuple[State, ...], ...]:
        if remaining == 0:
            return ((current,),)
        out: list[tuple[State, ...]] = []
        for nxt in STRAIGHT_NEXT[current]:
            length = length_of(nxt, sides)
            if length <= remaining:
                for tail in extend(nxt, remaining - length):
                    out.append((current,) + tail)
        return tuple(out)

    out: list[tuple[State, ...]] = []
    for state in STATES:
        length = length_of(state, sides)
        if length <= side_length:
            out.extend(extend(state, side_length - length))
    return out


def boundary_cycles(side_length: int, sides: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    paths = side_paths(side_length, sides)
    start_ok: dict[int, list[int]] = {}
    for i, left in enumerate(paths):
        start_ok[i] = [
            j for j, right in enumerate(paths) if corner_transition(left[-1], right[0])
        ]
    cycles: list[tuple[int, int, int]] = []
    for i in range(len(paths)):
        for j in start_ok[i]:
            for k in start_ok[j]:
                if i in start_ok[k]:
                    cycles.append((i, j, k))
    return cycles


def feasible_boundary(n: int, a: int, b: int) -> bool:
    c2 = a * a - a * b + b * b
    c = isqrt(c2)
    if c * c != c2:
        return False
    outer2 = n * a * b
    side = isqrt(outer2)
    if side * side != outer2:
        return False
    return bool(boundary_cycles(side, (a, b, c)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args()

    c2 = args.a * args.a - args.a * args.b + args.b * args.b
    c = isqrt(c2)
    sides = (args.a, args.b, c)
    if not valid_pi_tile(sides):
        raise SystemExit("not a gamma=pi/3 integer-side tile")
    outer2 = args.n * args.a * args.b
    side = isqrt(outer2)
    if side * side != outer2:
        raise SystemExit("area equation does not give an integer equilateral side")

    paths = side_paths(side, sides)
    cycles = boundary_cycles(side, sides)
    print(f"N={args.n} equilateral gamma=pi/3 boundary-star check")
    print(f"tile sides={sides}; outer side={side}")
    print(f"oriented side paths passing straight-vertex stars: {len(paths)}")
    print(f"feasible full boundary cycles: {len(cycles)}")
    if cycles:
        print("first cycles, by side-path indexes:")
        for cycle in cycles[:10]:
            print(f"  {cycle}")
    else:
        print("boundary-star obstruction: no compatible equilateral boundary")


if __name__ == "__main__":
    main()
