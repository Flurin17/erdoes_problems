#!/usr/bin/env python3
"""Boundary arithmetic for the remaining prime-71 isosceles candidate.

This is not a full obstruction for arbitrary non-strict tilings.  It records the
exact boundary constraints and the immediate side-to-side parity obstruction for
Beeson's remaining gamma=2pi/3 isosceles candidate:

    tile sides (a,b,c) = (39,16,49), N=71,
    outer isosceles sides (196,196,284).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Candidate71:
    n: int = 71
    a: int = 39
    b: int = 16
    c: int = 49
    equal_side: int = 196
    base: int = 284


def decompositions(length: int, sides: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    """Return counts of (b,a,c)-edges summing to length."""
    b, a, c = sides
    out: list[tuple[int, int, int]] = []
    for nb in range(length // b + 1):
        for na in range(length // a + 1):
            rem = length - nb * b - na * a
            if rem >= 0 and rem % c == 0:
                out.append((nb, na, rem // c))
    return out


def strict_boundary_edge_count(candidate: Candidate71) -> int:
    """Boundary tile-edge count forced in an edge-to-edge tiling."""
    equal = decompositions(candidate.equal_side, (candidate.b, candidate.a, candidate.c))
    base = decompositions(candidate.base, (candidate.b, candidate.a, candidate.c))
    assert equal == [(0, 0, 4)]
    # At each base corner exactly one alpha tile occurs.  Its adjacent sides are
    # b and c.  Since each equal side is forced to be four c-edges, the base must
    # use b at both ends; this excludes the no-b decomposition.
    feasible_base = [row for row in base if row[0] >= 2]
    assert feasible_base == [(8, 4, 0)]
    nb, na, nc = feasible_base[0]
    return 2 * 4 + nb + na + nc


def angle_vertex_types() -> dict[str, list[tuple[int, int, int]]]:
    """Angle-count types assuming alpha/pi is irrational.

    Tuples are counts of (alpha,beta,gamma) tile angles.
    """
    return {
        "base corner angle alpha": [(1, 0, 0)],
        "apex angle alpha+3beta": [(1, 3, 0)],
        "straight boundary angle pi": [(1, 1, 1), (3, 3, 0)],
        "simple interior T-junction tile-angle sum pi": [(1, 1, 1), (3, 3, 0)],
        "interior angle 2pi": [(0, 0, 3), (2, 2, 2), (4, 4, 1), (6, 6, 0)],
    }


def main() -> None:
    candidate = Candidate71()
    equal = decompositions(candidate.equal_side, (candidate.b, candidate.a, candidate.c))
    base = decompositions(candidate.base, (candidate.b, candidate.a, candidate.c))
    boundary_edges = strict_boundary_edge_count(candidate)
    print("p=71 isosceles gamma=2pi/3 candidate")
    print(f"tile sides (a,b,c)=({candidate.a},{candidate.b},{candidate.c})")
    print(f"outer sides=({candidate.equal_side},{candidate.equal_side},{candidate.base})")
    print(f"equal-side decompositions as (b,a,c): {equal}")
    print(f"base decompositions as (b,a,c): {base}")
    print("base corners force a b-edge on the base, so the feasible base decomposition is (8,4,0)")
    print(f"side-to-side boundary tile-edge count B={boundary_edges}")
    print(f"3N-B={3 * candidate.n - boundary_edges}")
    if (3 * candidate.n - boundary_edges) % 2:
        print("strict edge-to-edge tilings are impossible by parity")
    else:
        print("strict edge-to-edge parity does not obstruct")
    boundary_noncorner_vertices = 2 * (4 - 1) + (8 + 4 - 1)
    print(f"forced non-corner boundary vertices={boundary_noncorner_vertices}")
    print(
        "alpha-angle parity: corners and boundary non-corners contribute even total; "
        "simple interior T-junctions would have to occur in odd number"
    )
    print("angle vertex types:")
    for label, types in angle_vertex_types().items():
        print(f"  {label}: {types}")
    print("stronger follow-up: isosceles_71_boundary_sequences.py rules out the non-strict case")


if __name__ == "__main__":
    main()
