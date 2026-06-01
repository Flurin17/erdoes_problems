#!/usr/bin/env python3
"""Search power sums of the regular spectrum.

For p>=1 this evaluates

    Phi_p(G) = sum_d s_d(G)^p

where s_d(G) is the largest order of an induced d-regular subgraph.  The
case p=2 is useful because a quadratic lower bound Phi_2(G) >= c|G|^2 would
imply a polynomial upper bound for the spectrum-matching parameter.
"""

from __future__ import annotations

import argparse
import random
from collections import Counter

import column_drop_census as cdc
from regular_spectrum_mass import is_connected, spectrum_mass
from spectrum_mass_critical import delete_vertex, extend_mask


def power_value(by_degree: dict[int, int], power: int) -> int:
    return sum(order**power for order in by_degree.values())


def delete_vertex_mask(
    mask: int,
    vertex: int,
    pc: cdc.Precomp,
    pc_minus: cdc.Precomp,
) -> int:
    out = 0
    for small_index, (u, v) in enumerate(pc_minus.edges):
        old_u = u if u < vertex else u + 1
        old_v = v if v < vertex else v + 1
        old_edge = (old_u, old_v)
        if (mask >> pc.edge_index[old_edge]) & 1:
            out |= 1 << small_index
    return out


def precompute_power_values(n: int, power: int) -> list[int]:
    pc = cdc.precompute(n)
    values: list[int] = []
    for mask in range(1 << len(pc.edges)):
        adj = cdc.adjacency(n, mask, pc)
        _mass, by_degree = spectrum_mass(adj, pc)
        values.append(power_value(by_degree, power))
    return values


def fixed(n: int, mask: int, power: int) -> None:
    pc = cdc.precompute(n)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    value = power_value(by_degree, power)
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"connected={is_connected(adj)}")
    print(f"spectrum_mass={mass}")
    print(f"power={power}")
    print(f"power_sum={value}")
    print(f"normalized={value / (n**power)}")
    print(f"by_degree={by_degree}")


def deletion_profile(n: int, mask: int, power: int) -> None:
    pc = cdc.precompute(n)
    pc_minus = cdc.precompute(n - 1)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    value = power_value(by_degree, power)
    bound = sum(order ** (power + 1) for order in by_degree.values())
    total_drop = 0
    print(f"n={n}")
    print(f"mask={mask}")
    print(f"connected={is_connected(adj)}")
    print(f"spectrum_mass={mass}")
    print(f"power={power}")
    print(f"power_sum={value}")
    print(f"by_degree={by_degree}")
    for vertex in range(n):
        smaller = delete_vertex(adj, vertex)
        smaller_mass, smaller_by_degree = spectrum_mass(smaller, pc_minus)
        smaller_value = power_value(smaller_by_degree, power)
        drop = value - smaller_value
        total_drop += drop
        print(
            f"delete vertex={vertex} mass={smaller_mass} "
            f"power_sum={smaller_value} drop={drop} "
            f"by_degree={smaller_by_degree}"
        )
    print(f"total_drop={total_drop}")
    print(f"drop_bound=sum_s_d_power_{power + 1}={bound}")
    print(f"bound_holds={total_drop <= bound}")


def extension_profile(
    n: int,
    mask: int,
    power: int,
    max_columns: int | None,
    extension_sample: int,
    seed: int,
) -> None:
    pc = cdc.precompute(n)
    pc_plus = cdc.precompute(n + 1)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)
    value = power_value(by_degree, power)
    total_columns = 1 << n
    if extension_sample:
        rng = random.Random(seed)
        columns = [rng.randrange(total_columns) for _ in range(extension_sample)]
    else:
        column_count = (
            total_columns if max_columns is None else min(max_columns, total_columns)
        )
        columns = list(range(column_count))
    histogram: Counter[int] = Counter()
    best_value = (n + 1) ** (power + 2)
    best_mass = (n + 1) ** 2
    best_examples: list[tuple[int, int, int, int, dict[int, int]]] = []

    for column in columns:
        extended = extend_mask(mask, n, column, pc, pc_plus)
        extended_adj = cdc.adjacency(n + 1, extended, pc_plus)
        extended_mass, extended_by_degree = spectrum_mass(extended_adj, pc_plus)
        extended_value = power_value(extended_by_degree, power)
        increment = extended_value - value
        histogram[increment] += 1
        if extended_value < best_value:
            best_value = extended_value
            best_mass = extended_mass
            best_examples = []
        if extended_value == best_value and len(best_examples) < 10:
            best_examples.append(
                (column, extended, extended_mass, extended_value, extended_by_degree)
            )

    print(f"n={n}")
    print(f"mask={mask}")
    print(f"connected={is_connected(adj)}")
    print(f"spectrum_mass={mass}")
    print(f"power={power}")
    print(f"power_sum={value}")
    print(f"by_degree={by_degree}")
    print(f"total_columns={total_columns}")
    print(f"checked_columns={len(columns)}")
    print(f"sampled_columns={bool(extension_sample)}")
    print(f"extension_increment_histogram={dict(sorted(histogram.items()))}")
    print(f"minimum_extended_mass={best_mass}")
    print(f"minimum_extended_power_sum={best_value}")
    print(f"minimum_power_increment={best_value - value}")
    for (
        column,
        extended,
        extended_mass,
        extended_value,
        extended_by_degree,
    ) in best_examples:
        print(
            f"best column={column} mask={extended} mass={extended_mass} "
            f"power_sum={extended_value} by_degree={extended_by_degree}"
        )


def exact(n: int, power: int, connected_only: bool) -> None:
    pc = cdc.precompute(n)
    total = 1 << len(pc.edges)
    best = 10**100
    best_examples: list[tuple[int, int, dict[int, int]]] = []
    histogram: Counter[int] = Counter()
    checked = 0

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        if connected_only and not is_connected(adj):
            continue
        checked += 1
        _, by_degree = spectrum_mass(adj, pc)
        value = power_value(by_degree, power)
        histogram[value] += 1
        if value < best:
            best = value
            best_examples = []
        if value == best and len(best_examples) < 10:
            best_examples.append((mask, value, by_degree))

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"checked_graphs={checked}")
    print(f"connected_only={connected_only}")
    print(f"power={power}")
    print(f"min_power_sum={best}")
    print(f"normalized={best / (n**power)}")
    print(f"histogram={dict(sorted(histogram.items()))}")
    for mask, value, by_degree in best_examples:
        print(f"example mask={mask} power_sum={value} by_degree={by_degree}")


def deletion_tight_scan(
    n: int,
    power: int,
    connected_only: bool,
    max_graphs: int | None,
    max_examples: int,
) -> None:
    pc = cdc.precompute(n)
    pc_minus = cdc.precompute(n - 1) if n > 1 else None
    smaller_power_values = (
        precompute_power_values(n - 1, power)
        if pc_minus is not None and len(pc_minus.edges) <= 22
        else None
    )
    total = 1 << len(pc.edges)
    checked = 0
    tight_count = 0
    zero_drop_histogram: Counter[int] = Counter()
    min_tight_value = 10**100
    min_tight_examples: list[tuple[int, int, dict[int, int], list[int]]] = []
    min_positive_drop = 10**100
    min_positive_examples: list[tuple[int, int, dict[int, int], list[int]]] = []

    for mask in range(total):
        adj = cdc.adjacency(n, mask, pc)
        if connected_only and not is_connected(adj):
            continue
        checked += 1
        _mass, by_degree = spectrum_mass(adj, pc)
        value = power_value(by_degree, power)
        drops: list[int] = []
        if pc_minus is None:
            drops = [0]
        else:
            for vertex in range(n):
                if smaller_power_values is not None:
                    smaller_mask = delete_vertex_mask(mask, vertex, pc, pc_minus)
                    smaller_value = smaller_power_values[smaller_mask]
                else:
                    smaller = delete_vertex(adj, vertex)
                    _smaller_mass, smaller_by_degree = spectrum_mass(smaller, pc_minus)
                    smaller_value = power_value(smaller_by_degree, power)
                drops.append(value - smaller_value)

        zero_drops = sum(1 for drop in drops if drop == 0)
        zero_drop_histogram[zero_drops] += 1
        if zero_drops == len(drops):
            tight_count += 1
            if value < min_tight_value:
                min_tight_value = value
                min_tight_examples = []
            if value == min_tight_value and len(min_tight_examples) < max_examples:
                min_tight_examples.append((mask, value, by_degree, drops))
        else:
            positive = min(drop for drop in drops if drop > 0)
            if positive < min_positive_drop:
                min_positive_drop = positive
                min_positive_examples = []
            if positive == min_positive_drop and len(min_positive_examples) < max_examples:
                min_positive_examples.append((mask, value, by_degree, drops))

        if max_graphs is not None and checked >= max_graphs:
            break

    print(f"n={n}")
    print(f"labelled_graphs={total}")
    print(f"checked_graphs={checked}")
    print(f"connected_only={connected_only}")
    print(f"power={power}")
    print(f"cached_deletion_values={smaller_power_values is not None}")
    print(f"deletion_tight_count={tight_count}")
    print(f"zero_drop_histogram={dict(sorted(zero_drop_histogram.items()))}")
    print(f"min_tight_power_sum={None if tight_count == 0 else min_tight_value}")
    if tight_count:
        print(f"min_tight_normalized={min_tight_value / (n**power)}")
    print(
        "min_positive_drop="
        f"{None if min_positive_drop == 10**100 else min_positive_drop}"
    )
    for mask, value, by_degree, drops in min_tight_examples:
        print(
            f"tight_example mask={mask} power_sum={value} "
            f"by_degree={by_degree} drops={drops}"
        )
    for mask, value, by_degree, drops in min_positive_examples:
        print(
            f"min_positive_example mask={mask} power_sum={value} "
            f"by_degree={by_degree} drops={drops}"
        )


def sample(
    n: int,
    power: int,
    trials: int,
    seed: int,
    connected_only: bool,
) -> None:
    rng = random.Random(seed)
    pc = cdc.precompute(n)
    bits = len(pc.edges)
    best = 10**100
    best_example: tuple[int, int, dict[int, int]] | None = None
    histogram: Counter[int] = Counter()
    checked = 0
    attempts = 0

    while checked < trials:
        attempts += 1
        mask = rng.getrandbits(bits)
        adj = cdc.adjacency(n, mask, pc)
        if connected_only and not is_connected(adj):
            continue
        checked += 1
        _, by_degree = spectrum_mass(adj, pc)
        value = power_value(by_degree, power)
        histogram[value] += 1
        if value < best:
            best = value
            best_example = (mask, value, by_degree)

    print(f"n={n}")
    print(f"trials={trials}")
    print(f"attempts={attempts}")
    print(f"connected_only={connected_only}")
    print(f"power={power}")
    print(f"min_seen={best}")
    print(f"normalized={best / (n**power)}")
    print(f"histogram={dict(sorted(histogram.items()))}")
    if best_example is not None:
        mask, value, by_degree = best_example
        print(f"best_example mask={mask} power_sum={value} by_degree={by_degree}")


def local_search(
    n: int,
    power: int,
    steps: int,
    restarts: int,
    seed: int,
    connected_only: bool,
    start_mask: int | None,
) -> None:
    rng = random.Random(seed)
    pc = cdc.precompute(n)
    bits = len(pc.edges)
    best = 10**100
    best_example: tuple[int, dict[int, int], int] | None = None

    for restart in range(restarts):
        if restart == 0 and start_mask is not None:
            mask = start_mask
        else:
            mask = rng.getrandbits(bits)
        adj = cdc.adjacency(n, mask, pc)
        if connected_only:
            attempts = 0
            while not is_connected(adj):
                if restart == 0 and start_mask is not None:
                    raise ValueError("start mask is not connected")
                attempts += 1
                if attempts > 10_000:
                    raise RuntimeError("failed to sample connected graph")
                mask = rng.getrandbits(bits)
                adj = cdc.adjacency(n, mask, pc)

        _, by_degree = spectrum_mass(adj, pc)
        value = power_value(by_degree, power)
        if value < best:
            best = value
            best_example = (mask, by_degree, value)
            print(
                f"new_best restart={restart} step=start value={value} "
                f"normalized={value / (n**power)} mask={mask} by_degree={by_degree}",
                flush=True,
            )

        temperature = 0.02
        for step in range(steps):
            bit = rng.randrange(bits)
            candidate = mask ^ (1 << bit)
            candidate_adj = cdc.adjacency(n, candidate, pc)
            if connected_only and not is_connected(candidate_adj):
                continue
            _, candidate_by_degree = spectrum_mass(candidate_adj, pc)
            candidate_value = power_value(candidate_by_degree, power)
            if candidate_value <= value or rng.random() < temperature:
                mask = candidate
                value = candidate_value
                by_degree = candidate_by_degree
            if value < best:
                best = value
                best_example = (mask, by_degree, value)
                print(
                    f"new_best restart={restart} step={step} value={value} "
                    f"normalized={value / (n**power)} mask={mask} "
                    f"by_degree={by_degree}",
                    flush=True,
                )

    print(f"n={n}")
    print(f"power={power}")
    print(f"steps={steps}")
    print(f"restarts={restarts}")
    print(f"connected_only={connected_only}")
    print(f"min_seen={best}")
    print(f"normalized={best / (n**power)}")
    if best_example is not None:
        mask, by_degree, value = best_example
        print(f"best_example mask={mask} power_sum={value} by_degree={by_degree}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--power", type=int, default=2)
    parser.add_argument("--mask", type=int)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--deletion-profile", action="store_true")
    parser.add_argument("--deletion-tight-scan", action="store_true")
    parser.add_argument("--extension-profile", action="store_true")
    parser.add_argument("--max-columns", type=int)
    parser.add_argument("--max-graphs", type=int)
    parser.add_argument("--max-examples", type=int, default=10)
    parser.add_argument("--extension-sample", type=int, default=0)
    parser.add_argument("--local-steps", type=int, default=0)
    parser.add_argument("--restarts", type=int, default=1)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--connected-only", action="store_true")
    parser.add_argument("--start-mask", type=int)
    args = parser.parse_args()

    if args.power < 1:
        parser.error("--power must be positive")

    if args.mask is not None and args.deletion_profile:
        deletion_profile(args.n, args.mask, args.power)
    elif args.mask is not None and args.extension_profile:
        if args.n > 12 and args.max_columns is None and not args.extension_sample:
            parser.error(
                "--extension-profile is exhaustive; use --max-columns or "
                "--extension-sample for n > 12"
            )
        extension_profile(
            args.n,
            args.mask,
            args.power,
            args.max_columns,
            args.extension_sample,
            args.seed,
        )
    elif args.mask is not None:
        fixed(args.n, args.mask, args.power)
    elif args.deletion_tight_scan:
        deletion_tight_scan(
            args.n,
            args.power,
            args.connected_only,
            args.max_graphs,
            args.max_examples,
        )
    elif args.sample:
        sample(args.n, args.power, args.sample, args.seed, args.connected_only)
    elif args.local_steps:
        local_search(
            args.n,
            args.power,
            args.local_steps,
            args.restarts,
            args.seed,
            args.connected_only,
            args.start_mask,
        )
    else:
        exact(args.n, args.power, args.connected_only)


if __name__ == "__main__":
    main()
