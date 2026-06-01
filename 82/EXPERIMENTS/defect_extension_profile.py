#!/usr/bin/env python3
"""Profile one-vertex extensions of defect-one spectrum-mass graphs."""

from __future__ import annotations

import argparse
from collections import Counter

import column_drop_census as cdc
from regular_spectrum_mass import is_connected, spectrum_mass
from spectrum_mass_critical import extend_mask


def degree_sequence(adj: list[int]) -> tuple[int, ...]:
    return tuple(sorted(row.bit_count() for row in adj))


def profile(n: int, mask: int, connected_only: bool) -> None:
    pc = cdc.precompute(n)
    pc_plus = cdc.precompute(n + 1)
    adj = cdc.adjacency(n, mask, pc)
    mass, by_degree = spectrum_mass(adj, pc)

    hist: Counter[int] = Counter()
    connected_hist: Counter[int] = Counter()
    s0_delta_hist: Counter[int] = Counter()
    changed_coordinate_hist: Counter[tuple[tuple[int, int], ...]] = Counter()
    worst_changed_coordinate_hist: Counter[tuple[tuple[int, int], ...]] = Counter()
    worst: list[tuple[int, int, dict[int, int], bool, tuple[int, ...]]] = []
    worst_mass = (n + 1) * (n + 1)

    for column in range(1 << n):
        extended = extend_mask(mask, n, column, pc, pc_plus)
        extended_adj = cdc.adjacency(n + 1, extended, pc_plus)
        connected = is_connected(extended_adj)
        if connected_only and not connected:
            continue
        extended_mass, extended_by_degree = spectrum_mass(extended_adj, pc_plus)
        hist[extended_mass] += 1
        if connected:
            connected_hist[extended_mass] += 1
        s0_delta_hist[extended_by_degree.get(0, 0) - by_degree.get(0, 0)] += 1
        deltas = []
        for degree in sorted(set(by_degree) | set(extended_by_degree)):
            delta = extended_by_degree.get(degree, 0) - by_degree.get(degree, 0)
            if delta:
                deltas.append((degree, delta))
        changed_coordinate_hist[tuple(deltas)] += 1
        if extended_mass < worst_mass:
            worst_mass = extended_mass
            worst = []
            worst_changed_coordinate_hist.clear()
        if extended_mass == worst_mass:
            worst_changed_coordinate_hist[tuple(deltas)] += 1
        if extended_mass == worst_mass and len(worst) < 20:
            worst.append(
                (
                    column,
                    extended,
                    extended_by_degree,
                    connected,
                    degree_sequence(extended_adj),
                )
            )

    print(f"n={n}")
    print(f"mask={mask}")
    print(f"connected={is_connected(adj)}")
    print(f"spectrum_mass={mass}")
    print(f"defect={n - mass}")
    print(f"by_degree={by_degree}")
    print(f"connected_only={connected_only}")
    print(f"extension_mass_histogram={dict(sorted(hist.items()))}")
    print(f"connected_extension_mass_histogram={dict(sorted(connected_hist.items()))}")
    print(f"s0_delta_histogram={dict(sorted(s0_delta_hist.items()))}")
    print(f"changed_coordinate_top={changed_coordinate_hist.most_common(30)}")
    print(f"worst_changed_coordinate_histogram={dict(worst_changed_coordinate_hist)}")
    print(f"worst_mass={worst_mass}")
    for column, extended, extended_by_degree, connected, degrees in worst:
        print(
            f"worst column={column} mask={extended} connected={connected} "
            f"by_degree={extended_by_degree} degree_sequence={degrees}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--mask", type=int, required=True)
    parser.add_argument("--connected-only", action="store_true")
    args = parser.parse_args()
    profile(args.n, args.mask, args.connected_only)


if __name__ == "__main__":
    main()
