#!/usr/bin/env python3
"""Fast one-vertex extension stagnation test for the regular spectrum.

For a fixed graph G on n vertices, an extension column C is spectrum-stagnant
if adding a new vertex with neighborhood C does not increase any coordinate
s_d(G).  The test avoids recomputing spectra of all extensions.  For each old
subset T, it characterizes the columns that make T plus the new vertex
regular and marks those that would improve a spectrum coordinate.
"""

from __future__ import annotations

import argparse
from collections import Counter

import column_drop_census as cdc
from regular_spectrum_mass import is_connected, spectrum_mass
from spectrum_mass_critical import extend_mask


def vertices(mask: int, n: int) -> tuple[int, ...]:
    return tuple(v for v in range(n) if (mask >> v) & 1)


def submasks(mask: int):
    sub = mask
    while True:
        yield sub
        if sub == 0:
            break
        sub = (sub - 1) & mask


def regular_extension_patterns(
    adj: list[int],
    subset: int,
) -> list[tuple[int, int]]:
    """Return pairs (degree, required_column_on_subset).

    The returned pattern means that a new extension column C makes
    subset union {new vertex} degree-regular of the returned degree exactly
    when C & subset equals required_column_on_subset.
    """
    if subset == 0:
        return [(0, 0)]
    n = len(adj)
    degs = {
        v: (adj[v] & subset).bit_count()
        for v in range(n)
        if (subset >> v) & 1
    }
    candidates = set(degs.values())
    candidates.update(d + 1 for d in degs.values())
    out: list[tuple[int, int]] = []
    for degree in sorted(candidates):
        if degree < 0:
            continue
        low = 0
        ok = True
        for v, old_degree in degs.items():
            if old_degree == degree - 1:
                low |= 1 << v
            elif old_degree == degree:
                pass
            else:
                ok = False
                break
        if ok and low.bit_count() == degree:
            out.append((degree, low))
    return out


def stagnant_columns(n: int, mask: int) -> tuple[list[int], Counter[tuple[int, int]]]:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    _mass, by_degree = spectrum_mass(adj, pc)
    total_columns = 1 << n
    forbidden = bytearray(total_columns)
    reason_counts: Counter[tuple[int, int]] = Counter()
    full = total_columns - 1

    for subset in range(0, total_columns):
        order = subset.bit_count() + 1
        for degree, required in regular_extension_patterns(adj, subset):
            if order <= by_degree.get(degree, 0):
                continue
            free = full ^ subset
            for outside in submasks(free):
                column = required | outside
                if not forbidden[column]:
                    forbidden[column] = 1
                    reason_counts[(degree, order)] += 1

    return [column for column, value in enumerate(forbidden) if not value], reason_counts


def square_value(by_degree: dict[int, int]) -> int:
    return sum(order * order for order in by_degree.values())


def chain_census(n: int, max_graphs: int | None, max_examples: int) -> None:
    pc = cdc.precompute(n)
    pc_plus = cdc.precompute(n + 1)
    total = 1 << len(pc.edges)
    checked = 0
    graphs_with_stagnation = 0
    stagnant_edges = 0
    two_step_graphs = 0
    min_two_step_square: int | None = None
    min_two_step_examples: list[tuple[int, int, int, dict[int, int], int, list[int]]] = []
    examples: list[tuple[int, int, int, list[int]]] = []

    for mask in range(total):
        checked += 1
        columns, _reason_counts = stagnant_columns(n, mask)
        if columns:
            graphs_with_stagnation += 1
            stagnant_edges += len(columns)
        for column in columns:
            extended = extend_mask(mask, n, column, pc, pc_plus)
            next_columns, _next_reasons = stagnant_columns(n + 1, extended)
            if next_columns:
                two_step_graphs += 1
                adj = cdc.adjacency(n, mask, pc)
                _mass, by_degree = spectrum_mass(adj, pc)
                square = square_value(by_degree)
                if min_two_step_square is None or square < min_two_step_square:
                    min_two_step_square = square
                    min_two_step_examples = []
                if square == min_two_step_square and len(min_two_step_examples) < max_examples:
                    min_two_step_examples.append(
                        (mask, column, extended, by_degree, square, next_columns[:10])
                    )
                if len(examples) < max_examples:
                    examples.append((mask, column, extended, next_columns[:10]))
                break
        if max_graphs is not None and checked >= max_graphs:
            break

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"checked_graphs={checked}")
    print(f"graphs_with_stagnation={graphs_with_stagnation}")
    print(f"stagnant_extension_edges={stagnant_edges}")
    print(f"two_step_stagnation_graphs={two_step_graphs}")
    print(f"min_two_step_square={min_two_step_square}")
    for mask, column, extended, next_columns in examples:
        print(
            f"two_step_example mask={mask} column={column} "
            f"extended_mask={extended} next_columns={next_columns}"
        )
    for mask, column, extended, by_degree, square, next_columns in min_two_step_examples:
        print(
            f"min_square_two_step_example mask={mask} column={column} "
            f"extended_mask={extended} square={square} by_degree={by_degree} "
            f"next_columns={next_columns}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--chain-census", action="store_true")
    parser.add_argument("--max-graphs", type=int)
    parser.add_argument("--max-examples", type=int, default=5)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--print-extended-masks", action="store_true")
    args = parser.parse_args()

    if args.chain_census:
        chain_census(args.n, args.max_graphs, args.max_examples)
        return
    if args.mask is None:
        parser.error("--mask is required unless --chain-census is used")

    pc = cdc.precompute(args.n)
    adj = cdc.adjacency(args.n, args.mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    columns, reason_counts = stagnant_columns(args.n, args.mask)
    pc_plus = cdc.precompute(args.n + 1)

    print(f"n={args.n}")
    print(f"mask={args.mask}")
    print(f"connected={is_connected(adj)}")
    print(f"spectrum_mass={mass}")
    print(f"by_degree={by_degree}")
    print(f"total_columns={1 << args.n}")
    print(f"stagnant_column_count={len(columns)}")
    print(f"stagnant_columns={columns[:args.limit]}")
    print(
        "forbidden_reason_counts="
        + ",".join(
            f"degree={degree}:order={order}:columns={count}"
            for (degree, order), count in sorted(reason_counts.items())
        )
    )
    if args.print_extended_masks:
        for column in columns[: args.limit]:
            extended = extend_mask(args.mask, args.n, column, pc, pc_plus)
            print(f"stagnant column={column} extended_mask={extended}")


if __name__ == "__main__":
    main()
