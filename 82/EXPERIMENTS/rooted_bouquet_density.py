#!/usr/bin/env python3
"""Search asymptotic spectrum density of rooted bouquet constructions.

For a rooted graph (H,r), form B_t by identifying the roots of t copies of H.
For fixed H and t -> infinity, the coefficient of t in s_d(B_t) is

    max(a_d^0, a_{d,0}^1 - 1),

when the final root degree d can be supplied by finitely many positive
partial-root branches.  Otherwise only the root-avoiding coefficient a_d^0 is
valid.  Here a_d^0 is the largest d-regular induced set avoiding r, and
a_{d,0}^1 is the largest rooted partial witness containing r, with every
non-root vertex having degree d and the root having partial degree 0 in that
copy.  Positive partial root degrees can occur in only O_d(1) copies, so they
only decide reachability and do not affect the asymptotic coefficient.
"""

from __future__ import annotations

import argparse
import random
from collections import Counter

import column_drop_census as cdc
from regular_spectrum_mass import is_connected, spectrum_mass
from rooted_gluing_spectrum import rooted_signature


def bouquet_coefficient(
    adj: list[int], root: int, pc: cdc.Precomp
) -> tuple[int, dict[int, int]]:
    avoid, include = rooted_signature(adj, root, pc.n - 1)
    by_degree: dict[int, int] = {}
    for degree in range(pc.n):
        rooted_value = 0
        if degree_reachable_from_root_partials(degree, include.get(degree, {})):
            rooted_value = include.get(degree, {}).get(0, 0) - 1
        value = max(avoid.get(degree, 0), rooted_value)
        if value > 0:
            by_degree[degree] = value
    return sum(by_degree.values()), by_degree


def degree_reachable_from_root_partials(degree: int, partials: dict[int, int]) -> bool:
    if degree == 0:
        return True
    positive = [p for p in partials if p > 0]
    reachable = [False] * (degree + 1)
    reachable[0] = True
    for total in range(degree + 1):
        if not reachable[total]:
            continue
        for p in positive:
            if total + p <= degree:
                reachable[total + p] = True
    return reachable[degree]


def inspect(n: int, mask: int, root: int | None) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    roots = range(n) if root is None else (root,)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"connected={is_connected(adj)}")
    print(f"spectrum_mass={mass}")
    print(f"by_degree={by_degree}")
    for r in roots:
        coefficient, coefficient_by_degree = bouquet_coefficient(adj, r, pc)
        print(
            f"root={r} coefficient={coefficient} "
            f"ratio={coefficient/(n-1):.12g} "
            f"coefficient_by_degree={coefficient_by_degree}"
        )


def exact(n: int, connected_only: bool, progress: int) -> None:
    pc = cdc.precompute(n)
    total = 1 << len(pc.edges)
    checked_graphs = 0
    checked_roots = 0
    best_coefficient = n * n
    best_examples: list[tuple[int, int, dict[int, int], dict[int, int]]] = []
    coefficient_hist: Counter[int] = Counter()

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        if connected_only and not is_connected(adj):
            continue
        checked_graphs += 1
        mass, by_degree = spectrum_mass(adj, pc)
        for root in range(n):
            checked_roots += 1
            coefficient, coefficient_by_degree = bouquet_coefficient(adj, root, pc)
            coefficient_hist[coefficient] += 1
            if coefficient < best_coefficient:
                best_coefficient = coefficient
                best_examples = []
            if coefficient == best_coefficient and len(best_examples) < 10:
                best_examples.append((mask, root, by_degree, coefficient_by_degree))
        if progress and mask and mask % progress == 0:
            print(
                f"progress mask={mask}/{total} best={best_coefficient} "
                f"ratio={best_coefficient/(n-1):.12g}",
                flush=True,
            )

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"connected_only={connected_only}")
    print(f"checked_graphs={checked_graphs}")
    print(f"checked_roots={checked_roots}")
    print(f"min_coefficient={best_coefficient}")
    print(f"min_ratio={best_coefficient/(n-1):.12g}")
    print(f"coefficient_histogram={dict(sorted(coefficient_hist.items()))}")
    for mask, root, by_degree, coefficient_by_degree in best_examples:
        print(
            f"example mask={mask} root={root} by_degree={by_degree} "
            f"coefficient_by_degree={coefficient_by_degree}"
        )


def sample(n: int, trials: int, seed: int, connected_only: bool) -> None:
    rng = random.Random(seed)
    pc = cdc.precompute(n)
    bits = len(pc.edges)
    checked_graphs = 0
    attempts = 0
    best_coefficient = n * n
    best_example: tuple[int, int, dict[int, int], dict[int, int]] | None = None
    coefficient_hist: Counter[int] = Counter()

    while checked_graphs < trials:
        attempts += 1
        mask = rng.getrandbits(bits)
        adj = cdc.adjacency(n, mask, pc)
        if connected_only and not is_connected(adj):
            continue
        checked_graphs += 1
        mass, by_degree = spectrum_mass(adj, pc)
        best_for_graph = n * n
        best_root = 0
        best_by: dict[int, int] = {}
        for root in range(n):
            coefficient, coefficient_by_degree = bouquet_coefficient(adj, root, pc)
            if coefficient < best_for_graph:
                best_for_graph = coefficient
                best_root = root
                best_by = coefficient_by_degree
        coefficient_hist[best_for_graph] += 1
        if best_for_graph < best_coefficient:
            best_coefficient = best_for_graph
            best_example = (mask, best_root, by_degree, best_by)

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"connected_only={connected_only}")
    print(f"min_coefficient={best_coefficient}")
    print(f"min_ratio={best_coefficient/(n-1):.12g}")
    print(f"coefficient_histogram={dict(sorted(coefficient_hist.items()))}")
    if best_example is not None:
        mask, root, by_degree, coefficient_by_degree = best_example
        print(
            f"best_example mask={mask} root={root} by_degree={by_degree} "
            f"coefficient_by_degree={coefficient_by_degree}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--root", type=int)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=82)
    parser.add_argument("--connected-only", action="store_true")
    parser.add_argument("--progress", type=int, default=0)
    args = parser.parse_args()

    if args.mask is not None:
        inspect(args.n, args.mask, args.root)
    elif args.sample:
        sample(args.n, args.sample, args.seed, args.connected_only)
    else:
        exact(args.n, args.connected_only, args.progress)


if __name__ == "__main__":
    main()
