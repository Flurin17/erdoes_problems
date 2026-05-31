#!/usr/bin/env python3
"""Primitive collinear overhang components for `gamma=2alpha` diagnostics.

The strict boundary endpoint automaton assumes clean edge-to-edge fans.  This
script enumerates the smallest equal-length side-string pairs that can create
non-strict collinear interfaces such as `a+c = k b`.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from itertools import product
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import candidates_for_n  # noqa: E402
from gamma_2alpha_endpoint_automaton import orientations, straight_transition  # noqa: E402


SideString = tuple[str, ...]
SideLengths = tuple[int, int, int]

SIDE_INDEX = {"a": 0, "b": 1, "c": 2}


@dataclass(frozen=True)
class Component:
    left: SideString
    right: SideString
    length: int
    left_endpoint_pairs: int
    right_endpoint_pairs: int


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


def side_counts(seq: SideString) -> tuple[int, int, int]:
    return (seq.count("a"), seq.count("b"), seq.count("c"))


def endpoint_pair_count(seq: SideString, mode: str) -> int:
    """Count first/last oriented edge pairs for this exact side-label string."""
    if not seq:
        return 0
    current = [(placed, placed) for placed in orientations(seq[0])]
    for side in seq[1:]:
        next_current = []
        for first, previous in current:
            for placed in orientations(side):
                if straight_transition(previous, placed, mode):
                    next_current.append((first, placed))
        current = next_current
        if not current:
            break
    return len(set(current))


def is_primitive_pair(left: SideString, right: SideString, sides: SideLengths) -> bool:
    return side_string_cuts(left, sides).isdisjoint(side_string_cuts(right, sides))


def canonical_pair(left: SideString, right: SideString) -> tuple[SideString, SideString]:
    return (left, right) if side_string_text(left) <= side_string_text(right) else (right, left)


def strings_up_to(max_pieces: int) -> list[SideString]:
    out: list[SideString] = []
    for size in range(1, max_pieces + 1):
        out.extend(tuple(seq) for seq in product(("a", "b", "c"), repeat=size))
    return out


def primitive_components(
    sides: SideLengths,
    *,
    max_pieces: int,
    mode: str,
    require_distinct_counts: bool,
) -> tuple[Component, ...]:
    strings = strings_up_to(max_pieces)
    by_length: dict[int, list[SideString]] = {}
    for seq in strings:
        if endpoint_pair_count(seq, mode) == 0:
            continue
        by_length.setdefault(side_string_length(seq, sides), []).append(seq)

    seen: set[tuple[SideString, SideString]] = set()
    out: list[Component] = []
    for length, seqs in by_length.items():
        for i, left in enumerate(seqs):
            for right in seqs[i:]:
                if left == right:
                    continue
                if require_distinct_counts and side_counts(left) == side_counts(right):
                    continue
                if not is_primitive_pair(left, right, sides):
                    continue
                first, second = canonical_pair(left, right)
                key = (first, second)
                if key in seen:
                    continue
                seen.add(key)
                out.append(
                    Component(
                        left=first,
                        right=second,
                        length=length,
                        left_endpoint_pairs=endpoint_pair_count(first, mode),
                        right_endpoint_pairs=endpoint_pair_count(second, mode),
                    )
                )
    return tuple(sorted(out, key=lambda row: (row.length, len(row.left) + len(row.right), row.left, row.right)))


def format_component(row: Component) -> str:
    return (
        f"{side_string_text(row.left)} | {side_string_text(row.right)} "
        f"length={row.length} endpoint_pairs=({row.left_endpoint_pairs},{row.right_endpoint_pairs})"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--max-pieces", type=int, default=6)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--mode", choices=("angle", "fan"), default="angle")
    parser.add_argument(
        "--allow-same-counts",
        action="store_true",
        help="include pairs that use the same multiset of side labels",
    )
    args = parser.parse_args()

    for n in args.n:
        rows = candidates_for_n(n)
        print(f"N={n}: {len(rows)} gamma=2alpha boundary candidate(s)")
        for row in rows:
            components = primitive_components(
                row.tile,
                max_pieces=args.max_pieces,
                mode=args.mode,
                require_distinct_counts=not args.allow_same_counts,
            )
            print(
                f"  tile={row.tile}: {len(components)} primitive overhang component(s) "
                f"with <= {args.max_pieces} pieces [{args.mode}]"
            )
            for component in components[: args.limit]:
                print(f"    {format_component(component)}")
            if len(components) > args.limit:
                print(f"    ... {len(components) - args.limit} more")


if __name__ == "__main__":
    main()
