#!/usr/bin/env python3
"""Exact finite rational-grid model for Erdos problem 143.

For a denominator Q and cutoff X, the vertices m represent x=m/Q in
[2,X].  This is the relevant range for an infinite admissible set: a point in
(1,2) conflicts with every larger point.  For m<n, the defining inequalities
hold for this pair exactly when

    Q <= n mod m <= m-Q.

Thus feasible grid sets are precisely independent sets in the conflict graph
built below.  The program solves two maximum-weight independent-set problems
using exact Fraction arithmetic:

  harmonic:       sum Q/m = sum 1/x;
  dyadic-log:      sum Q/(m*(floor(log_2(m/Q))+1)).

For x>=2 the second summand is within a factor two (after multiplication by
1/log(2)) of 1/(x log x).  No floating-point comparisons enter the optimizer.
"""

from __future__ import annotations

import argparse
import functools
import json
import time
from fractions import Fraction
from typing import Callable, Iterable


def compatible(m: int, n: int, q: int) -> bool:
    """Return exact compatibility for q < m < n on the denominator-q grid."""
    assert q < m < n
    r = n % m
    return q <= r <= m - q


def direct_compatible(m: int, n: int, q: int) -> bool:
    """Independent finite-k check used only to assert graph construction."""
    assert q < m < n
    # Once k*m >= n+q, all later k have distance at least q.
    k_max = (n + q - 1 + m - 1) // m
    return all(abs(k * m - n) >= q for k in range(1, k_max + 1))


def dyadic_index(m: int, q: int) -> int:
    """floor(log_2(m/q)), computed with integers only."""
    assert m >= 2 * q
    j = 0
    while (q << (j + 1)) <= m:
        j += 1
    return j


def build_graph(q: int, x: int) -> tuple[list[int], list[int]]:
    """Vertices and bit-mask conflict adjacency for [2,x] intersect (1/q)Z."""
    vertices = list(range(2 * q, q * x + 1))
    size = len(vertices)
    adjacency = [0] * size
    for i, m in enumerate(vertices):
        for j in range(i + 1, size):
            n = vertices[j]
            conflict = not compatible(m, n, q)
            assert conflict == (not direct_compatible(m, n, q))
            if conflict:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    return vertices, adjacency


def components(mask: int, adjacency: list[int]) -> list[int]:
    """Connected components of the induced conflict graph."""
    result: list[int] = []
    unseen = mask
    while unseen:
        seed = unseen & -unseen
        comp = 0
        frontier = seed
        unseen ^= seed
        while frontier:
            comp |= frontier
            neighbors = 0
            todo = frontier
            while todo:
                bit = todo & -todo
                todo ^= bit
                i = bit.bit_length() - 1
                neighbors |= adjacency[i]
            frontier = neighbors & unseen
            unseen &= ~frontier
        result.append(comp)
    return result


def maximum_weight_independent_set(
    adjacency: list[int], weights: list[Fraction]
) -> tuple[Fraction, int, int]:
    """Exact memoized include/exclude solution; return weight, mask, states."""
    assert len(adjacency) == len(weights)

    @functools.lru_cache(maxsize=None)
    def solve(mask: int) -> tuple[Fraction, int]:
        if not mask:
            return Fraction(0), 0

        comps = components(mask, adjacency)
        if len(comps) > 1:
            total = Fraction(0)
            selected = 0
            for comp in comps:
                value, choice = solve(comp)
                total += value
                selected |= choice
            return total, selected

        # A high induced degree tends to make both branches shrink quickly.
        todo = mask
        best_i = -1
        best_score = (-1, Fraction(0))
        while todo:
            bit = todo & -todo
            todo ^= bit
            i = bit.bit_length() - 1
            score = ((adjacency[i] & mask).bit_count(), weights[i])
            if score > best_score:
                best_score = score
                best_i = i
        bit = 1 << best_i

        out_value, out_choice = solve(mask ^ bit)
        in_mask = mask & ~bit & ~adjacency[best_i]
        in_value, in_choice = solve(in_mask)
        in_value += weights[best_i]
        in_choice |= bit
        # Deterministic tie break: numerically smaller bit mask.
        if in_value > out_value or (in_value == out_value and in_choice < out_choice):
            return in_value, in_choice
        return out_value, out_choice

    full = (1 << len(weights)) - 1
    value, chosen = solve(full)
    return value, chosen, solve.cache_info().currsize


def brute_force_value(adjacency: list[int], weights: list[Fraction]) -> Fraction:
    """Independent exhaustive verifier, used automatically on small graphs."""
    best = Fraction(0)
    size = len(weights)
    for mask in range(1 << size):
        independent = True
        value = Fraction(0)
        todo = mask
        while todo:
            bit = todo & -todo
            todo ^= bit
            i = bit.bit_length() - 1
            if adjacency[i] & todo:
                independent = False
                break
            value += weights[i]
        if independent and value > best:
            best = value
    return best


def assert_independent(choice: Iterable[int], q: int) -> None:
    chosen = sorted(choice)
    for i, m in enumerate(chosen):
        for n in chosen[i + 1 :]:
            assert compatible(m, n, q)


def solve_instance(q: int, x: int, objective: str) -> dict[str, object]:
    vertices, adjacency = build_graph(q, x)
    if objective == "harmonic":
        weight_fn: Callable[[int], Fraction] = lambda m: Fraction(q, m)
    elif objective == "dyadic-log":
        weight_fn = lambda m: Fraction(q, m * (dyadic_index(m, q) + 1))
    else:
        raise ValueError(objective)
    weights = [weight_fn(m) for m in vertices]

    started = time.perf_counter()
    value, mask, states = maximum_weight_independent_set(adjacency, weights)
    elapsed = time.perf_counter() - started
    choice = [m for i, m in enumerate(vertices) if mask & (1 << i)]
    assert_independent(choice, q)
    assert value == sum((weight_fn(m) for m in choice), Fraction(0))
    brute_force_verified = len(vertices) <= 16
    if brute_force_verified:
        assert value == brute_force_value(adjacency, weights)

    return {
        "Q": q,
        "X": x,
        "objective": objective,
        "vertices": len(vertices),
        "edges": sum(a.bit_count() for a in adjacency) // 2,
        "optimum_fraction": f"{value.numerator}/{value.denominator}",
        "optimum_decimal": float(value),
        "chosen_numerators": choice,
        "chosen_points": [f"{m}/{q}" for m in choice],
        "states": states,
        "runtime_seconds": elapsed,
        "brute_force_verified": brute_force_verified,
    }


def parse_int_list(raw: str) -> list[int]:
    values = [int(part) for part in raw.split(",") if part]
    if not values or any(v < 2 for v in values):
        raise argparse.ArgumentTypeError("cutoffs must be comma-separated integers >=2")
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-max", type=int, default=4)
    parser.add_argument("--x-values", type=parse_int_list, default=[4, 6, 8, 10])
    parser.add_argument(
        "--objectives", choices=("both", "harmonic", "dyadic-log"), default="both"
    )
    parser.add_argument(
        "--compact", action="store_true", help="print one exact tab-separated row per instance"
    )
    args = parser.parse_args()
    if args.q_max < 1:
        parser.error("--q-max must be positive")
    objectives = (
        ["harmonic", "dyadic-log"] if args.objectives == "both" else [args.objectives]
    )
    output = {
        "model": "vertices m/Q in [2,X], conflict iff min_k |km-n| < Q",
        "command_parameters": {
            "q_max": args.q_max,
            "x_values": args.x_values,
            "objectives": objectives,
        },
        "instances": [],
    }
    for q in range(1, args.q_max + 1):
        for x in args.x_values:
            for objective in objectives:
                output["instances"].append(solve_instance(q, x, objective))
    if args.compact:
        print("Q\tX\tobjective\toptimum\tchosen_numerators\tstates\truntime_seconds")
        for row in output["instances"]:
            print(
                f"{row['Q']}\t{row['X']}\t{row['objective']}\t"
                f"{row['optimum_fraction']}\t"
                f"{','.join(str(m) for m in row['chosen_numerators'])}\t"
                f"{row['states']}\t{row['runtime_seconds']:.6f}"
            )
    else:
        print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
