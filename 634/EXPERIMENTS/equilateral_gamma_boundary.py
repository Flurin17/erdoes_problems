#!/usr/bin/env python3
"""Boundary-star check for equilateral outer triangles and gamma=2pi/3 tiles.

This checks only the outer boundary.  It assumes the generic irrational
`alpha,beta` setting for a tile with angles `(alpha,beta,gamma)` and
`gamma=2pi/3`, so the straight boundary vertex types are

    alpha + beta + gamma = pi,        3alpha + 3beta = pi.

The straight side-label transition table is the same one used in
`isosceles_prime_boundary_words.py`.  At an equilateral corner, the outer angle
is `pi/3 = alpha + beta`; the two incident boundary tiles must contribute one
`alpha` and one `beta` angle, and their interior sides from the corner must
have the same label.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import cache
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

STRAIGHT_NEXT: dict[State, tuple[State, ...]] = {
    STATES[0]: (STATES[0],),
    STATES[1]: (STATES[1], STATES[2]),
    STATES[2]: (STATES[2],),
    STATES[3]: (STATES[0], STATES[3]),
    STATES[4]: (STATES[4],),
    STATES[5]: (STATES[5],),
}


def length_of(state: State, sides: tuple[int, int, int]) -> int:
    return sides["abc".index(state.label)]


def other_side_at_angle(state: State, angle: Angle) -> str:
    if angle == "alpha":
        return "c" if state.label == "b" else "b"
    if angle == "beta":
        return "c" if state.label == "a" else "a"
    if angle == "gamma":
        return "b" if state.label == "a" else "a"
    raise ValueError(angle)


def corner_transition(prev: State, nxt: State) -> bool:
    if {prev.end, nxt.start} != {"alpha", "beta"}:
        return False
    return other_side_at_angle(prev, prev.end) == other_side_at_angle(nxt, nxt.start)


def valid_gamma_tile(sides: tuple[int, int, int]) -> bool:
    a, b, c = sides
    return c * c == a * a + a * b + b * b


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
    c2 = a * a + a * b + b * b
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

    c2 = args.a * args.a + args.a * args.b + args.b * args.b
    c = isqrt(c2)
    sides = (args.a, args.b, c)
    if not valid_gamma_tile(sides):
        raise SystemExit("not a gamma=2pi/3 integer-side tile")
    outer2 = args.n * args.a * args.b
    side = isqrt(outer2)
    if side * side != outer2:
        raise SystemExit("area equation does not give an integer equilateral side")

    paths = side_paths(side, sides)
    cycles = boundary_cycles(side, sides)
    print(f"N={args.n} equilateral gamma=2pi/3 boundary-star check")
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
