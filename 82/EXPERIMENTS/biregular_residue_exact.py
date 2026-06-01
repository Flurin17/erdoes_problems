#!/usr/bin/env python3
"""Exact residue probabilities in small simple regular bipartite graphs.

The DP counts labelled simple d-regular bipartite graphs with N left and N
right vertices, grouped only by the remaining column-capacity histograms in
the marked and unmarked right-side classes.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, getcontext
from functools import lru_cache
from fractions import Fraction
from math import comb


def decimal_ratio(numerator: int, denominator: int, precision: int = 24) -> Decimal:
    getcontext().prec = precision
    return Decimal(numerator) / Decimal(denominator)


def fraction_to_decimal(value: Fraction, precision: int = 24) -> Decimal:
    getcontext().prec = precision
    return Decimal(value.numerator) / Decimal(value.denominator)


@lru_cache(maxsize=None)
def selections(hist: tuple[int, ...], total: int) -> tuple[tuple[tuple[int, ...], int], ...]:
    """Return all ways to choose `total` columns from a capacity histogram."""
    if total < 0:
        return ()
    result: list[tuple[tuple[int, ...], int]] = []
    current = [0] * len(hist)

    def rec(index: int, remaining: int, ways: int) -> None:
        if index == len(hist):
            if remaining == 0:
                result.append((tuple(current), ways))
            return
        limit = min(hist[index], remaining)
        for chosen in range(limit + 1):
            current[index] = chosen
            rec(index + 1, remaining - chosen, ways * comb(hist[index], chosen))
        current[index] = 0

    rec(0, total, 1)
    return tuple(result)


@lru_cache(maxsize=None)
def apply_selection(hist: tuple[int, ...], selected: tuple[int, ...]) -> tuple[int, ...]:
    next_hist = list(hist)
    for index, chosen in enumerate(selected):
        if chosen == 0:
            continue
        next_hist[index] -= chosen
        if index > 0:
            next_hist[index - 1] += chosen
    return tuple(next_hist)


def count_graphs(
    n: int,
    degree: int,
    marked: int,
    tested_rows: int,
    modulus: int,
) -> tuple[int, int]:
    initial_marked = [0] * degree
    initial_unmarked = [0] * degree
    initial_marked[degree - 1] = marked
    initial_unmarked[degree - 1] = n - marked
    zero_hist = (0,) * degree

    @lru_cache(maxsize=None)
    def dp(
        row: int,
        marked_hist: tuple[int, ...],
        unmarked_hist: tuple[int, ...],
        residue: int,
    ) -> int:
        if row == n:
            return int(marked_hist == zero_hist and unmarked_hist == zero_hist)

        total = 0
        for marked_hits in range(degree + 1):
            unmarked_hits = degree - marked_hits
            marked_choices = selections(marked_hist, marked_hits)
            if not marked_choices:
                continue
            unmarked_choices = selections(unmarked_hist, unmarked_hits)
            if not unmarked_choices:
                continue

            next_residue = residue
            if row < tested_rows:
                row_residue = marked_hits % modulus
                if residue == -1:
                    next_residue = row_residue
                elif row_residue != residue:
                    continue

            for selected_marked, marked_ways in marked_choices:
                next_marked_hist = apply_selection(marked_hist, selected_marked)
                for selected_unmarked, unmarked_ways in unmarked_choices:
                    next_unmarked_hist = apply_selection(unmarked_hist, selected_unmarked)
                    total += (
                        marked_ways
                        * unmarked_ways
                        * dp(row + 1, next_marked_hist, next_unmarked_hist, next_residue)
                    )
        return total

    @lru_cache(maxsize=None)
    def total_dp(
        row: int,
        marked_hist: tuple[int, ...],
        unmarked_hist: tuple[int, ...],
    ) -> int:
        if row == n:
            return int(marked_hist == zero_hist and unmarked_hist == zero_hist)

        total = 0
        for marked_hits in range(degree + 1):
            unmarked_hits = degree - marked_hits
            for selected_marked, marked_ways in selections(marked_hist, marked_hits):
                next_marked_hist = apply_selection(marked_hist, selected_marked)
                for selected_unmarked, unmarked_ways in selections(
                    unmarked_hist, unmarked_hits
                ):
                    next_unmarked_hist = apply_selection(unmarked_hist, selected_unmarked)
                    total += (
                        marked_ways
                        * unmarked_ways
                        * total_dp(row + 1, next_marked_hist, next_unmarked_hist)
                    )
        return total

    marked_tuple = tuple(initial_marked)
    unmarked_tuple = tuple(initial_unmarked)
    return (
        dp(0, marked_tuple, unmarked_tuple, -1),
        total_dp(0, marked_tuple, unmarked_tuple),
    )


def count_prefix_next_distribution(
    n: int,
    degree: int,
    marked: int,
    prefix_rows: int,
    modulus: int,
) -> tuple[list[int], int]:
    initial_marked = [0] * degree
    initial_unmarked = [0] * degree
    initial_marked[degree - 1] = marked
    initial_unmarked[degree - 1] = n - marked
    zero_hist = (0,) * degree

    @lru_cache(maxsize=None)
    def dp(
        row: int,
        marked_hist: tuple[int, ...],
        unmarked_hist: tuple[int, ...],
        prefix_residue: int,
        next_residue: int,
    ) -> int:
        if row == n:
            return int(marked_hist == zero_hist and unmarked_hist == zero_hist)

        total = 0
        for marked_hits in range(degree + 1):
            unmarked_hits = degree - marked_hits
            marked_choices = selections(marked_hist, marked_hits)
            if not marked_choices:
                continue
            unmarked_choices = selections(unmarked_hist, unmarked_hits)
            if not unmarked_choices:
                continue

            row_residue = marked_hits % modulus
            next_prefix_residue = prefix_residue
            if row < prefix_rows:
                if prefix_residue == -1:
                    next_prefix_residue = row_residue
                elif row_residue != prefix_residue:
                    continue
            elif row == prefix_rows and row_residue != next_residue:
                continue

            for selected_marked, marked_ways in marked_choices:
                next_marked_hist = apply_selection(marked_hist, selected_marked)
                for selected_unmarked, unmarked_ways in unmarked_choices:
                    next_unmarked_hist = apply_selection(unmarked_hist, selected_unmarked)
                    total += (
                        marked_ways
                        * unmarked_ways
                        * dp(
                            row + 1,
                            next_marked_hist,
                            next_unmarked_hist,
                            next_prefix_residue,
                            next_residue,
                        )
                    )
        return total

    marked_tuple = tuple(initial_marked)
    unmarked_tuple = tuple(initial_unmarked)
    counts = [
        dp(0, marked_tuple, unmarked_tuple, -1, residue)
        for residue in range(modulus)
    ]
    return counts, sum(counts)


def independent_equal_probability(
    n: int, degree: int, marked: int, tested_rows: int, modulus: int
) -> Fraction:
    denominator = comb(n, degree)
    residues = [Fraction(0, 1) for _ in range(modulus)]
    low = max(0, degree - (n - marked))
    high = min(marked, degree)
    for hits in range(low, high + 1):
        residues[hits % modulus] += Fraction(
            comb(marked, hits) * comb(n - marked, degree - hits),
            denominator,
        )
    return sum(value**tested_rows for value in residues)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--degree", type=int, required=True)
    parser.add_argument("--marked", type=int, required=True)
    parser.add_argument("--rows", type=int, required=True)
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument(
        "--prefix-next",
        type=int,
        help="Also print the next-row residue distribution after this many prefix rows are equal.",
    )
    args = parser.parse_args()

    if not 0 <= args.marked <= args.n:
        raise SystemExit("--marked must lie between 0 and n")
    if not 0 <= args.degree <= args.n:
        raise SystemExit("--degree must lie between 0 and n")
    if args.rows < 0 or args.rows > args.n:
        raise SystemExit("--rows must lie between 0 and n")

    event_count, total_count = count_graphs(
        args.n, args.degree, args.marked, args.rows, args.modulus
    )
    exact_probability = decimal_ratio(event_count, total_count)
    independent_probability = independent_equal_probability(
        args.n, args.degree, args.marked, args.rows, args.modulus
    )
    independent_decimal = fraction_to_decimal(independent_probability)

    print(f"n={args.n}")
    print(f"degree={args.degree}")
    print(f"marked={args.marked}")
    print(f"rows={args.rows}")
    print(f"modulus={args.modulus}")
    print(f"simple_biregular_count={total_count}")
    print(f"equal_residue_count={event_count}")
    print(f"exact_equal_residue_probability={exact_probability}")
    print(f"independent_row_prediction={independent_decimal}")
    if independent_probability:
        ratio = Fraction(event_count, total_count) / independent_probability
        print(f"ratio_to_independent={fraction_to_decimal(ratio)}")

    if args.prefix_next is not None:
        if args.prefix_next < 0 or args.prefix_next >= args.n:
            raise SystemExit("--prefix-next must lie between 0 and n-1")
        counts, denominator = count_prefix_next_distribution(
            args.n, args.degree, args.marked, args.prefix_next, args.modulus
        )
        print(f"prefix_rows={args.prefix_next}")
        print(f"prefix_next_denominator={denominator}")
        print(
            "prefix_next_counts="
            + ",".join(f"{residue}:{count}" for residue, count in enumerate(counts))
        )
        print(
            "prefix_next_distribution="
            + ",".join(
                f"{residue}:{decimal_ratio(count, denominator)}"
                for residue, count in enumerate(counts)
            )
        )
        print(
            "prefix_next_max_probability="
            + str(decimal_ratio(max(counts), denominator))
        )


if __name__ == "__main__":
    main()
