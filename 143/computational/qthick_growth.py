#!/usr/bin/env python3
"""Exact growth diagnostics for the Q-thick rational-grid model.

For integers Q >= 1 and X >= 2, the vertices are the numerators

    2Q <= m <= XQ,     representing the point m/Q.

Two numerators m < n may both be selected precisely when

    Q <= n mod m <= m-Q.

The program treats compatibility as adjacency and solves an exact
maximum-weight clique problem.  Its branch-and-bound upper bound is a proper
greedy coloring: a clique uses at most one vertex of each color, so the sum of
the largest integer weight in every color is an exact (not floating-point)
upper bound.  Fractions are converted to integer weights using a common
denominator before search.

Besides one optimizer, each row computes the optimum restricted to Q | m and
the optimum required to use some Q \nmid m.  Consequently it distinguishes
"an integral-sublattice optimizer exists" from "every optimizer is on the
integral sublattice."  This is finite evidence only, not an asymptotic proof.
"""

from __future__ import annotations

import argparse
import functools
import json
import math
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Optional


def parse_positive_list(raw: str) -> list[int]:
    """Parse a nonempty comma-separated list of distinct positive integers."""
    try:
        values = [int(part) for part in raw.split(",") if part]
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    if not values or any(value < 1 for value in values):
        raise argparse.ArgumentTypeError("expected comma-separated positive integers")
    return sorted(set(values))


def parse_cutoffs(raw: str) -> list[int]:
    values = parse_positive_list(raw)
    if values[0] < 2:
        raise argparse.ArgumentTypeError("cutoffs must be at least 2")
    return values


def modular_compatible(m: int, n: int, q: int) -> bool:
    """Exact modular compatibility test, for 2q <= m < n."""
    remainder = n % m
    return q <= remainder <= m - q


def nearest_multiple_compatible(m: int, n: int, q: int) -> bool:
    """Independent O(1) check using the two nearest multiples of m."""
    quotient = n // m
    below = n - quotient * m
    above = (quotient + 1) * m - n
    return min(below, above) >= q


def build_compatibility_graph(q: int, x: int) -> tuple[list[int], list[int]]:
    """Return vertices and bit-mask adjacency in the compatibility graph."""
    vertices = list(range(2 * q, x * q + 1))
    adjacency = [0] * len(vertices)
    for i, m in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            n = vertices[j]
            compatible = modular_compatible(m, n, q)
            # This assertion checks the graph construction by a differently
            # expressed nearest-multiple calculation on every pair.
            assert compatible == nearest_multiple_compatible(m, n, q)
            if compatible:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    return vertices, adjacency


def dyadic_index(m: int, q: int) -> int:
    """Return floor(log_2(m/q)) with integer arithmetic only."""
    assert m >= 2 * q
    index = 0
    while (q << (index + 1)) <= m:
        index += 1
    return index


def fractional_weights(vertices: list[int], q: int, objective: str) -> list[Fraction]:
    if objective == "harmonic":
        return [Fraction(q, m) for m in vertices]
    if objective == "dyadic-log":
        return [Fraction(q, m * (dyadic_index(m, q) + 1)) for m in vertices]
    raise ValueError(objective)


def integerize(weights: list[Fraction]) -> tuple[list[int], int]:
    """Scale positive Fraction weights to exact positive integers."""
    scale = 1
    for weight in weights:
        assert weight > 0
        scale = math.lcm(scale, weight.denominator)
    result = [weight.numerator * (scale // weight.denominator) for weight in weights]
    assert all(Fraction(value, scale) == weight for value, weight in zip(result, weights))
    return result, scale


@dataclass
class SearchStats:
    nodes: int = 0
    colorings: int = 0
    bound_prunes: int = 0
    missing_required_prunes: int = 0
    incumbent_updates: int = 0
    maximum_depth: int = 0


class ExactWeightedClique:
    """Exact weighted clique search with integer weighted-coloring bounds."""

    def __init__(
        self,
        adjacency: list[int],
        weights: list[int],
        allowed_mask: int,
        required_mask: int = 0,
    ) -> None:
        assert len(adjacency) == len(weights)
        self.adjacency = adjacency
        self.weights = weights
        self.allowed_mask = allowed_mask
        self.required_mask = required_mask & allowed_mask
        self.require_special = bool(required_mask)
        self.best_weight = -1 if self.require_special else 0
        self.best_mask = 0
        self.stats = SearchStats()

    def _eligible(self, mask: int) -> bool:
        return not self.require_special or bool(mask & self.required_mask)

    def _consider(self, weight: int, mask: int) -> None:
        if not self._eligible(mask):
            return
        if weight > self.best_weight or (
            weight == self.best_weight and (self.best_weight < 0 or mask < self.best_mask)
        ):
            self.best_weight = weight
            self.best_mask = mask
            self.stats.incumbent_updates += 1

    def _greedy_from(self, first: Optional[int]) -> None:
        """Seed the incumbent by a deterministic weight-first maximal clique."""
        chosen = 0
        value = 0
        candidates = self.allowed_mask
        if first is not None:
            bit = 1 << first
            if not candidates & bit:
                return
            chosen |= bit
            value += self.weights[first]
            candidates &= self.adjacency[first]
        order = sorted(
            (i for i in range(len(self.weights)) if candidates & (1 << i)),
            key=lambda i: (-self.weights[i], -(self.adjacency[i] & candidates).bit_count(), i),
        )
        for vertex in order:
            bit = 1 << vertex
            if candidates & bit:
                chosen |= bit
                value += self.weights[vertex]
                candidates &= self.adjacency[vertex]
        self._consider(value, chosen)

    def _seed(self) -> None:
        if not self.require_special:
            self._greedy_from(None)
            return
        special = self.required_mask
        starters: list[int] = []
        while special:
            bit = special & -special
            special ^= bit
            starters.append(bit.bit_length() - 1)
        starters.sort(key=lambda i: (-self.weights[i], i))
        # Trying every special starter is still only linear preprocessing, and
        # supplies a useful lower bound for the constrained diagnostic.
        for vertex in starters:
            self._greedy_from(vertex)

    def _color_sort(self, candidates: int) -> tuple[list[int], list[int]]:
        """Properly color candidates and give an exact bound for each prefix."""
        self.stats.colorings += 1
        uncolored = candidates
        order: list[int] = []
        bounds: list[int] = []
        completed_color_weight = 0
        covered = 0

        while uncolored:
            available = uncolored
            color_vertices: list[int] = []
            color_mask = 0
            while available:
                # Prefer a high-weight vertex, then one with few compatibility
                # neighbors, to grow a large color class.
                scan = available
                vertex = -1
                key: tuple[int, int, int] | None = None
                while scan:
                    bit = scan & -scan
                    scan ^= bit
                    candidate = bit.bit_length() - 1
                    candidate_key = (
                        self.weights[candidate],
                        -(self.adjacency[candidate] & available).bit_count(),
                        -candidate,
                    )
                    if key is None or candidate_key > key:
                        key = candidate_key
                        vertex = candidate
                bit = 1 << vertex
                assert not (self.adjacency[vertex] & color_mask)
                color_vertices.append(vertex)
                color_mask |= bit
                covered |= bit
                uncolored ^= bit
                # A color is an independent set in the compatibility graph.
                available &= ~bit & ~self.adjacency[vertex]

            color_vertices.sort(key=lambda i: (self.weights[i], -i))
            color_maximum = 0
            for vertex in color_vertices:
                color_maximum = max(color_maximum, self.weights[vertex])
                order.append(vertex)
                bounds.append(completed_color_weight + color_maximum)
            completed_color_weight += color_maximum

        assert covered == candidates
        assert len(order) == candidates.bit_count() == len(bounds)
        assert all(bounds[i] <= bounds[i + 1] for i in range(len(bounds) - 1))
        return order, bounds

    def _expand(
        self,
        candidates: int,
        value: int,
        chosen: int,
        has_special: bool,
        depth: int,
    ) -> None:
        self.stats.nodes += 1
        self.stats.maximum_depth = max(self.stats.maximum_depth, depth)
        if not candidates:
            self._consider(value, chosen)
            return
        if self.require_special and not has_special and not (candidates & self.required_mask):
            self.stats.missing_required_prunes += 1
            return

        order, bounds = self._color_sort(candidates)
        remaining = candidates
        for position in range(len(order) - 1, -1, -1):
            # Equality can be pruned: an incumbent of this exact objective
            # value is already an optimality witness.
            if value + bounds[position] <= self.best_weight:
                self.stats.bound_prunes += 1
                return
            vertex = order[position]
            bit = 1 << vertex
            assert remaining & bit
            next_candidates = remaining & self.adjacency[vertex]
            self._expand(
                next_candidates,
                value + self.weights[vertex],
                chosen | bit,
                has_special or bool(bit & self.required_mask),
                depth + 1,
            )
            remaining ^= bit

    def solve(self) -> tuple[Optional[int], int, SearchStats]:
        self._seed()
        self._expand(self.allowed_mask, 0, 0, False, 0)
        if self.best_weight < 0:
            return None, 0, self.stats
        return self.best_weight, self.best_mask, self.stats


def reference_dynamic_program(
    adjacency: list[int], weights: list[int], allowed_mask: int
) -> int:
    """Independent exact include/exclude DP used to cross-check small rows."""

    @functools.lru_cache(maxsize=None)
    def solve(mask: int) -> int:
        if not mask:
            return 0
        bit = mask & -mask
        vertex = bit.bit_length() - 1
        without = solve(mask ^ bit)
        with_vertex = weights[vertex] + solve((mask ^ bit) & adjacency[vertex])
        return max(without, with_vertex)

    return solve(allowed_mask)


def mask_vertices(mask: int, vertices: list[int]) -> list[int]:
    return [m for i, m in enumerate(vertices) if mask & (1 << i)]


def verify_clique(choice: Iterable[int], q: int) -> None:
    chosen = sorted(choice)
    for i, m in enumerate(chosen):
        for n in chosen[i + 1 :]:
            assert nearest_multiple_compatible(m, n, q)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def stats_dict(stats: SearchStats) -> dict[str, int]:
    return {
        "nodes": stats.nodes,
        "colorings": stats.colorings,
        "bound_prunes": stats.bound_prunes,
        "missing_required_prunes": stats.missing_required_prunes,
        "incumbent_updates": stats.incumbent_updates,
        "maximum_depth": stats.maximum_depth,
    }


def solve_instance(q: int, x: int, objective: str, dp_limit: int) -> dict[str, object]:
    started = time.perf_counter()
    vertices, adjacency = build_compatibility_graph(q, x)
    fraction_weights = fractional_weights(vertices, q, objective)
    weights, scale = integerize(fraction_weights)
    full_mask = (1 << len(vertices)) - 1
    integral_mask = sum(1 << i for i, m in enumerate(vertices) if m % q == 0)
    off_lattice_mask = full_mask ^ integral_mask

    global_solver = ExactWeightedClique(adjacency, weights, full_mask)
    optimum_integer, optimum_mask, global_stats = global_solver.solve()
    assert optimum_integer is not None

    integral_solver = ExactWeightedClique(adjacency, weights, integral_mask)
    integral_integer, integral_choice_mask, integral_stats = integral_solver.solve()
    assert integral_integer is not None

    if off_lattice_mask:
        off_solver = ExactWeightedClique(
            adjacency, weights, full_mask, required_mask=off_lattice_mask
        )
        off_integer, off_choice_mask, off_stats = off_solver.solve()
    else:
        off_integer, off_choice_mask, off_stats = None, 0, SearchStats()

    optimum = Fraction(optimum_integer, scale)
    integral_optimum = Fraction(integral_integer, scale)
    off_optimum = None if off_integer is None else Fraction(off_integer, scale)
    choice = mask_vertices(optimum_mask, vertices)
    integral_choice = mask_vertices(integral_choice_mask, vertices)
    off_choice = mask_vertices(off_choice_mask, vertices)

    verify_clique(choice, q)
    verify_clique(integral_choice, q)
    assert all(m % q == 0 for m in integral_choice)
    if off_integer is not None:
        verify_clique(off_choice, q)
        assert any(m % q for m in off_choice)
    recomputed = sum(
        (fraction_weights[i] for i in range(len(vertices)) if optimum_mask & (1 << i)),
        Fraction(0),
    )
    assert recomputed == optimum

    dp_crosscheck = len(vertices) <= dp_limit
    if dp_crosscheck:
        assert reference_dynamic_program(adjacency, weights, full_mask) == optimum_integer

    residue_counts = Counter(m % q for m in choice)
    compatibility_edges = sum(mask.bit_count() for mask in adjacency) // 2
    elapsed = time.perf_counter() - started
    return {
        "Q": q,
        "X": x,
        "objective": objective,
        "vertices": len(vertices),
        "compatibility_edges": compatibility_edges,
        "conflict_edges": len(vertices) * (len(vertices) - 1) // 2 - compatibility_edges,
        "optimum_fraction": fraction_text(optimum),
        "optimum_decimal": float(optimum),
        "chosen_numerators": choice,
        "chosen_points": [f"{m}/{q}" for m in choice],
        "reported_optimizer_on_integer_sublattice": all(m % q == 0 for m in choice),
        "residue_profile": {str(r): residue_counts[r] for r in sorted(residue_counts)},
        "integer_sublattice_optimum_fraction": fraction_text(integral_optimum),
        "integer_sublattice_choice": integral_choice,
        "some_optimizer_on_integer_sublattice": integral_optimum == optimum,
        "off_lattice_optimum_fraction": (
            None if off_optimum is None else fraction_text(off_optimum)
        ),
        "off_lattice_choice": off_choice,
        "every_optimizer_on_integer_sublattice": (
            off_optimum is None or off_optimum < optimum
        ),
        "off_lattice_gap_fraction": (
            None if off_optimum is None else fraction_text(optimum - off_optimum)
        ),
        "verification": {
            "exact_integer_branch_and_bound_completed": True,
            "weighted_coloring_bounds_asserted": True,
            "all_graph_pairs_crosschecked": True,
            "chosen_cliques_pairwise_rechecked": True,
            "objective_recomputed_as_fraction": True,
            "independent_dp_crosscheck": dp_crosscheck,
        },
        "search": {
            "global": stats_dict(global_stats),
            "integer_sublattice": stats_dict(integral_stats),
            "requires_off_lattice": stats_dict(off_stats),
        },
        "runtime_seconds": elapsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--q-values", type=parse_positive_list, default=[1, 2, 4, 8])
    parser.add_argument("--x-values", type=parse_cutoffs, default=[10, 14, 18])
    parser.add_argument(
        "--objectives", choices=("both", "harmonic", "dyadic-log"), default="both"
    )
    parser.add_argument(
        "--dp-limit",
        type=int,
        default=32,
        help="cross-check rows with at most this many vertices by an independent DP",
    )
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    if args.dp_limit < 0:
        parser.error("--dp-limit must be nonnegative")

    objectives = (
        ["harmonic", "dyadic-log"]
        if args.objectives == "both"
        else [args.objectives]
    )
    rows: list[dict[str, object]] = []
    for q in args.q_values:
        for x in args.x_values:
            for objective in objectives:
                rows.append(solve_instance(q, x, objective, args.dp_limit))

    if args.compact:
        print(
            "Q\tX\tobjective\toptimum\tin_QN\tall_optima_in_QN\t"
            "residues\toff_gap\tnodes\truntime_seconds"
        )
        for row in rows:
            residues = ",".join(
                f"{residue}:{count}" for residue, count in row["residue_profile"].items()
            )
            total_nodes = sum(
                search["nodes"] for search in row["search"].values()
            )
            print(
                f"{row['Q']}\t{row['X']}\t{row['objective']}\t"
                f"{row['optimum_fraction']}\t"
                f"{row['reported_optimizer_on_integer_sublattice']}\t"
                f"{row['every_optimizer_on_integer_sublattice']}\t{residues}\t"
                f"{row['off_lattice_gap_fraction']}\t{total_nodes}\t"
                f"{row['runtime_seconds']:.6f}"
            )
    else:
        output = {
            "model": "vertices m/Q in [2,X], compatibility iff Q <= n mod m <= m-Q",
            "method": "exact integer-weight maximum clique with weighted-coloring bounds",
            "parameters": {
                "q_values": args.q_values,
                "x_values": args.x_values,
                "objectives": objectives,
                "dp_limit": args.dp_limit,
            },
            "instances": rows,
        }
        print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
