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


def square_coefficient(coefficient_by_degree: dict[int, int]) -> int:
    return sum(value * value for value in coefficient_by_degree.values())


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
        square = square_coefficient(coefficient_by_degree)
        print(
            f"root={r} coefficient={coefficient} "
            f"ratio={coefficient/(n-1):.12g} "
            f"square_coefficient={square} "
            f"square_ratio={square/((n-1)**2):.12g} "
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
    best_square = n**4
    best_square_examples: list[tuple[int, int, dict[int, int], dict[int, int]]] = []
    square_hist: Counter[int] = Counter()

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        if connected_only and not is_connected(adj):
            continue
        checked_graphs += 1
        mass, by_degree = spectrum_mass(adj, pc)
        for root in range(n):
            checked_roots += 1
            coefficient, coefficient_by_degree = bouquet_coefficient(adj, root, pc)
            square = square_coefficient(coefficient_by_degree)
            coefficient_hist[coefficient] += 1
            square_hist[square] += 1
            if coefficient < best_coefficient:
                best_coefficient = coefficient
                best_examples = []
            if coefficient == best_coefficient and len(best_examples) < 10:
                best_examples.append((mask, root, by_degree, coefficient_by_degree))
            if square < best_square:
                best_square = square
                best_square_examples = []
            if square == best_square and len(best_square_examples) < 10:
                best_square_examples.append((mask, root, by_degree, coefficient_by_degree))
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
    print(f"min_square_coefficient={best_square}")
    print(f"min_square_ratio={best_square/((n-1)**2):.12g}")
    print(f"coefficient_histogram={dict(sorted(coefficient_hist.items()))}")
    print(f"square_histogram={dict(sorted(square_hist.items()))}")
    for mask, root, by_degree, coefficient_by_degree in best_examples:
        print(
            f"example mask={mask} root={root} by_degree={by_degree} "
            f"coefficient_by_degree={coefficient_by_degree}"
        )
    for mask, root, by_degree, coefficient_by_degree in best_square_examples:
        print(
            f"square_example mask={mask} root={root} by_degree={by_degree} "
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
    best_square = n**4
    best_square_example: tuple[int, int, dict[int, int], dict[int, int]] | None = None
    square_hist: Counter[int] = Counter()

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
        square = square_coefficient(best_by)
        square_hist[square] += 1
        if best_for_graph < best_coefficient:
            best_coefficient = best_for_graph
            best_example = (mask, best_root, by_degree, best_by)
        if square < best_square:
            best_square = square
            best_square_example = (mask, best_root, by_degree, best_by)

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"connected_only={connected_only}")
    print(f"min_coefficient={best_coefficient}")
    print(f"min_ratio={best_coefficient/(n-1):.12g}")
    print(f"min_square_coefficient={best_square}")
    print(f"min_square_ratio={best_square/((n-1)**2):.12g}")
    print(f"coefficient_histogram={dict(sorted(coefficient_hist.items()))}")
    print(f"square_histogram={dict(sorted(square_hist.items()))}")
    if best_example is not None:
        mask, root, by_degree, coefficient_by_degree = best_example
        print(
            f"best_example mask={mask} root={root} by_degree={by_degree} "
            f"coefficient_by_degree={coefficient_by_degree}"
        )
    if best_square_example is not None:
        mask, root, by_degree, coefficient_by_degree = best_square_example
        print(
            f"best_square_example mask={mask} root={root} by_degree={by_degree} "
            f"coefficient_by_degree={coefficient_by_degree}"
        )


def local_search(
    n: int,
    steps: int,
    restarts: int,
    seed: int,
    start_mask: int | None,
    root: int | None,
    connected_only: bool,
) -> None:
    rng = random.Random(seed)
    pc = cdc.precompute(n)
    bits = len(pc.edges)
    global_best = n * n
    global_example: tuple[int, int, dict[int, int], dict[int, int]] | None = None
    global_best_square = n**4
    global_square_example: tuple[int, int, dict[int, int], dict[int, int]] | None = None

    def score(mask: int) -> tuple[int, int, dict[int, int], dict[int, int]] | None:
        adj = cdc.adjacency(n, mask, pc)
        if connected_only and not is_connected(adj):
            return None
        mass, by_degree = spectrum_mass(adj, pc)
        roots = range(n) if root is None else (root,)
        best = n * n
        best_root = 0
        best_coefficient_by_degree: dict[int, int] = {}
        for r in roots:
            coefficient, coefficient_by_degree = bouquet_coefficient(adj, r, pc)
            if coefficient < best:
                best = coefficient
                best_root = r
                best_coefficient_by_degree = coefficient_by_degree
        return best, best_root, by_degree, best_coefficient_by_degree

    for restart in range(restarts):
        if restart == 0 and start_mask is not None:
            mask = start_mask
        else:
            while True:
                mask = rng.getrandbits(bits)
                if score(mask) is not None:
                    break
        current = score(mask)
        assert current is not None
        current_score = current[0]
        temperature = max(1.0, n / 3)

        for step in range(steps + 1):
            if current_score < global_best:
                global_best = current_score
                global_example = (mask, current[1], current[2], current[3])
                print(
                    f"new_best restart={restart} step={step} "
                    f"coefficient={global_best} ratio={global_best/(n-1):.12g} "
                    f"mask={mask} root={current[1]} "
                    f"by_degree={current[2]} coefficient_by_degree={current[3]}",
                    flush=True,
                )
            current_square = square_coefficient(current[3])
            if current_square < global_best_square:
                global_best_square = current_square
                global_square_example = (mask, current[1], current[2], current[3])
                print(
                    f"new_best_square restart={restart} step={step} "
                    f"square={global_best_square} "
                    f"square_ratio={global_best_square/((n-1)**2):.12g} "
                    f"mask={mask} root={current[1]} "
                    f"by_degree={current[2]} coefficient_by_degree={current[3]}",
                    flush=True,
                )
            if step == steps:
                break

            candidate_mask = mask ^ (1 << rng.randrange(bits))
            candidate = score(candidate_mask)
            if candidate is None:
                continue
            candidate_score = candidate[0]
            if candidate_score <= current_score:
                accept = True
            else:
                accept = rng.random() < min(0.05, temperature / (steps + n))
            if accept:
                mask = candidate_mask
                current = candidate
                current_score = candidate_score

    print(f"n={n}")
    print(f"steps={steps}")
    print(f"restarts={restarts}")
    print(f"seed={seed}")
    print(f"connected_only={connected_only}")
    print(f"root_filter={root}")
    print(f"min_coefficient={global_best}")
    print(f"min_ratio={global_best/(n-1):.12g}")
    print(f"min_square_coefficient={global_best_square}")
    print(f"min_square_ratio={global_best_square/((n-1)**2):.12g}")
    if global_example is not None:
        mask, best_root, by_degree, coefficient_by_degree = global_example
        print(
            f"best_example mask={mask} root={best_root} by_degree={by_degree} "
            f"coefficient_by_degree={coefficient_by_degree}"
        )
    if global_square_example is not None:
        mask, best_root, by_degree, coefficient_by_degree = global_square_example
        print(
            f"best_square_example mask={mask} root={best_root} by_degree={by_degree} "
            f"coefficient_by_degree={coefficient_by_degree}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--root", type=int)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--local-steps", type=int, default=0)
    parser.add_argument("--restarts", type=int, default=1)
    parser.add_argument("--start-mask", type=int)
    parser.add_argument("--seed", type=int, default=82)
    parser.add_argument("--connected-only", action="store_true")
    parser.add_argument("--progress", type=int, default=0)
    args = parser.parse_args()

    if args.mask is not None:
        inspect(args.n, args.mask, args.root)
    elif args.local_steps:
        local_search(
            args.n,
            args.local_steps,
            args.restarts,
            args.seed,
            args.start_mask,
            args.root,
            args.connected_only,
        )
    elif args.sample:
        sample(args.n, args.sample, args.seed, args.connected_only)
    else:
        exact(args.n, args.connected_only, args.progress)


if __name__ == "__main__":
    main()
