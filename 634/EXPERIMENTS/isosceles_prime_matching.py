#!/usr/bin/env python3
"""Length-only matching diagnostics for surviving isosceles prime candidates.

This generalizes the prime-71 matching check.  For each base decomposition that
survives the boundary-word automaton, remove the forced boundary side
incidences and inspect which interior side counts are odd.  The script then
finds the first equal-length two-sided component with the corresponding odd
side incidence.

For the parametrized prime candidates the small relation

    u a = v b + v c,    u=s^2+r^2, v=s^2-r^2

is expected to be the first odd-parity component.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass

from gamma_2pi3_isosceles_filter import Candidate, prime_candidates
from isosceles_prime_boundary_words import has_base_word, viable_base_decompositions
from isosceles_prime_family import recover_parameters


@dataclass(frozen=True)
class Component:
    length: int
    counts: tuple[int, int, int]
    left: tuple[int, int, int]
    right: tuple[int, int, int]


def side_decompositions(
    sides: tuple[int, int, int], max_length: int
) -> dict[int, list[tuple[int, int, int]]]:
    by_length: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    a, b, c = sides
    for na in range(max_length // a + 1):
        for nb in range(max_length // b + 1):
            for nc in range(max_length // c + 1):
                if na == nb == nc == 0:
                    continue
                length = na * a + nb * b + nc * c
                if length <= max_length:
                    by_length[length].append((na, nb, nc))
    return by_length


def first_odd_component(
    sides: tuple[int, int, int], side_index: int, max_length: int
) -> Component | None:
    by_length = side_decompositions(sides, max_length)
    for length in sorted(by_length):
        decomps = by_length[length]
        for i, left in enumerate(decomps):
            for right in decomps[i:]:
                counts = tuple(left[k] + right[k] for k in range(3))
                if counts[side_index] % 2 == 1:
                    return Component(length, counts, left, right)
    return None


def report_candidate(candidate: Candidate) -> list[str]:
    params = recover_parameters(candidate)
    a, b, c = candidate.sides
    relation_length = params.u * a
    lines = [
        (
            f"N={candidate.n}, (r,s)=({params.r},{params.s}), "
            f"u={params.u}, v={params.v}, sides={candidate.sides}"
        ),
        f"  relation: {params.u}a = {params.v}b + {params.v}c = {relation_length}",
    ]
    for nb, na, nc, edge_count in viable_base_decompositions(candidate):
        if not has_base_word(nb, na, nc):
            continue
        interior = (candidate.n - na, candidate.n - nb, candidate.n - 2 * candidate.m - nc)
        odd_indices = [idx for idx, value in enumerate(interior) if value % 2 == 1]
        lines.append(
            f"  base (b,a,c)=({nb},{na},{nc}), edges={edge_count}, "
            f"interior (a,b,c)={interior}, odd indices={odd_indices}"
        )
        for idx in odd_indices:
            component = first_odd_component(candidate.sides, idx, relation_length)
            if component is None:
                lines.append(f"    no odd component for index {idx} up to {relation_length}")
                continue
            lines.append(
                f"    first odd index {idx}: length={component.length}, "
                f"{component.left} | {component.right}, counts={component.counts}"
            )
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=20_000)
    args = parser.parse_args()

    candidates = prime_candidates(args.limit)
    print(f"length-only matching diagnostics up to {args.limit}")
    for candidate in candidates:
        if not any(has_base_word(nb, na, nc) for nb, na, nc, _ in viable_base_decompositions(candidate)):
            continue
        for line in report_candidate(candidate):
            print(line)


if __name__ == "__main__":
    main()
