#!/usr/bin/env python3
"""Exact regular spectrum for two graphs glued at one root vertex.

The glued graph can be much larger than the subset-enumeration limit, but the
one-cut structure lets us compute the spectrum from rooted signatures of the
two sides.  For a fixed target degree d, a rooted signature records induced
sets containing the root in which all non-root vertices have degree d and the
root has a specified partial degree into that side.
"""

from __future__ import annotations

import argparse
from collections import defaultdict

import column_drop_census as cdc
from regular_spectrum_mass import spectrum_mass
from spectrum_mass_critical import delete_vertex


RootedSignature = tuple[dict[int, int], dict[int, dict[int, int]]]


def rooted_signature(adj: list[int], root: int, max_degree: int) -> RootedSignature:
    n = len(adj)
    avoid: dict[int, int] = {d: 0 for d in range(max_degree + 1)}
    include: dict[int, dict[int, int]] = {
        d: {0: 1} for d in range(max_degree + 1)
    }

    for subset in range(1, 1 << n):
        vertices = [v for v in range(n) if (subset >> v) & 1]
        if (subset >> root) & 1:
            nonroot = [v for v in vertices if v != root]
            if not nonroot:
                continue
            degree = (adj[nonroot[0]] & subset).bit_count()
            if degree > max_degree:
                continue
            if not all((adj[v] & subset).bit_count() == degree for v in nonroot[1:]):
                continue
            root_degree = (adj[root] & subset).bit_count()
            current = include.setdefault(degree, {}).get(root_degree, 0)
            if len(vertices) > current:
                include[degree][root_degree] = len(vertices)
        else:
            degree = (adj[vertices[0]] & subset).bit_count()
            if degree > max_degree:
                continue
            if not all((adj[v] & subset).bit_count() == degree for v in vertices[1:]):
                continue
            if len(vertices) > avoid.get(degree, 0):
                avoid[degree] = len(vertices)

    return avoid, include


def glued_spectrum(
    left: RootedSignature, right: RootedSignature, max_degree: int
) -> dict[int, int]:
    avoid_left, include_left = left
    avoid_right, include_right = right
    by_degree: dict[int, int] = {}

    for degree in range(max_degree + 1):
        best = avoid_left.get(degree, 0) + avoid_right.get(degree, 0)
        for root_degree_left, size_left in include_left.get(degree, {}).items():
            root_degree_right = degree - root_degree_left
            size_right = include_right.get(degree, {}).get(root_degree_right)
            if size_right is None:
                continue
            best = max(best, size_left + size_right - 1)
        if best:
            by_degree[degree] = best

    return by_degree


def bouquet_spectrum(signature: RootedSignature, copies: int, max_degree: int) -> dict[int, int]:
    avoid, include = signature
    by_degree: dict[int, int] = {}

    for degree in range(max_degree + 1):
        best = copies * avoid.get(degree, 0)
        partial: dict[int, int] = {0: 0}
        for _ in range(copies):
            next_partial: dict[int, int] = {}
            for root_degree_so_far, size_so_far in partial.items():
                for root_degree, size in include.get(degree, {}).items():
                    new_root_degree = root_degree_so_far + root_degree
                    new_size = size_so_far + size
                    if new_size > next_partial.get(new_root_degree, -1):
                        next_partial[new_root_degree] = new_size
            partial = next_partial
        if degree in partial:
            best = max(best, partial[degree] - (copies - 1))
        if best:
            by_degree[degree] = best

    return by_degree


def fixed(
    n1: int,
    mask1: int,
    root1: int,
    n2: int,
    mask2: int,
    root2: int,
    copies: int,
    brute_force_check: bool,
) -> None:
    if copies < 2:
        raise ValueError("--copies must be at least 2")
    if copies != 2 and (n2 != n1 or mask2 != mask1 or root2 != root1):
        raise ValueError("--copies above 2 is only supported for one repeated rooted graph")

    pc1 = cdc.precompute(n1)
    pc2 = cdc.precompute(n2)
    adj1 = cdc.adjacency(n1, mask1, pc1)
    adj2 = cdc.adjacency(n2, mask2, pc2)
    glued_order = n1 + n2 - 1 if copies == 2 else 1 + copies * (n1 - 1)
    max_degree = glued_order - 1

    mass1, by1 = spectrum_mass(adj1, pc1)
    root_deleted1 = delete_vertex(adj1, root1)
    mass1_deleted, by1_deleted = spectrum_mass(root_deleted1, cdc.precompute(n1 - 1))
    sig1 = rooted_signature(adj1, root1, max_degree)

    if copies == 2:
        mass2, by2 = spectrum_mass(adj2, pc2)
        root_deleted2 = delete_vertex(adj2, root2)
        mass2_deleted, by2_deleted = spectrum_mass(root_deleted2, cdc.precompute(n2 - 1))
        sig2 = rooted_signature(adj2, root2, max_degree)
        by_glued = glued_spectrum(sig1, sig2, max_degree)
    else:
        mass2, by2 = mass1, by1
        mass2_deleted, by2_deleted = mass1_deleted, by1_deleted
        by_glued = bouquet_spectrum(sig1, copies, max_degree)

    mass_glued = sum(by_glued.values())

    print(f"copies={copies}")
    print(f"n1={n1}")
    print(f"mask1={mask1}")
    print(f"root1={root1}")
    print(f"mass1={mass1}")
    print(f"by_degree1={by1}")
    print(f"mass1_minus_root={mass1_deleted}")
    print(f"by_degree1_minus_root={by1_deleted}")
    print(f"n2={n2}")
    print(f"mask2={mask2}")
    print(f"root2={root2}")
    print(f"mass2={mass2}")
    print(f"by_degree2={by2}")
    print(f"mass2_minus_root={mass2_deleted}")
    print(f"by_degree2_minus_root={by2_deleted}")
    print(f"glued_order={glued_order}")
    print(f"glued_spectrum_mass={mass_glued}")
    print(f"glued_defect={glued_order - mass_glued}")
    print(f"glued_by_degree={by_glued}")

    if brute_force_check:
        if copies != 2:
            raise ValueError("brute-force check is only implemented for two-copy gluing")
        if glued_order > 22:
            raise ValueError("brute-force check is too large")
        glued = materialize_gluing(adj1, root1, adj2, root2)
        brute_mass, brute_by_degree = spectrum_mass(glued, cdc.precompute(glued_order))
        print(f"brute_force_mass={brute_mass}")
        print(f"brute_force_by_degree={brute_by_degree}")
        print(f"brute_force_matches={brute_by_degree == by_glued}")


def materialize_gluing(
    adj1: list[int], root1: int, adj2: list[int], root2: int
) -> list[int]:
    n1 = len(adj1)
    n2 = len(adj2)
    root_map = {root2: root1}
    next_vertex = n1
    for v in range(n2):
        if v == root2:
            continue
        root_map[v] = next_vertex
        next_vertex += 1

    out = [0] * (n1 + n2 - 1)
    for i in range(n1):
        for j in range(i + 1, n1):
            if (adj1[i] >> j) & 1:
                out[i] |= 1 << j
                out[j] |= 1 << i
    for i in range(n2):
        for j in range(i + 1, n2):
            if (adj2[i] >> j) & 1:
                a = root_map[i]
                b = root_map[j]
                out[a] |= 1 << b
                out[b] |= 1 << a
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n1", type=int)
    parser.add_argument("--mask1", type=int, required=True)
    parser.add_argument("--root1", type=int, required=True)
    parser.add_argument("--n2", type=int)
    parser.add_argument("--mask2", type=int)
    parser.add_argument("--root2", type=int)
    parser.add_argument("--copies", type=int, default=2)
    parser.add_argument("--brute-force-check", action="store_true")
    args = parser.parse_args()

    fixed(
        args.n1,
        args.mask1,
        args.root1,
        args.n2 if args.n2 is not None else args.n1,
        args.mask2 if args.mask2 is not None else args.mask1,
        args.root2 if args.root2 is not None else args.root1,
        args.copies,
        args.brute_force_check,
    )


if __name__ == "__main__":
    main()
