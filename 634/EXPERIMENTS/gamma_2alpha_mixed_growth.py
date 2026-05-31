#!/usr/bin/env python3
"""Count boundary-shell growth by mixed-transition cap for `gamma=2alpha`.

Unlike `gamma_2alpha_low_mixed_shell_census.py`, this diagnostic does not
materialize every boundary-shell demand.  It groups boundary paths by oriented
endpoints and mixed-transition count, then multiplies group sizes.  This makes
the higher-mixed search space visible even when it is much too large to
classify shell by shell.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
from gamma_2alpha_boundary import (  # noqa: E402
    RefinedGamma2AlphaSurvivor,
    refined_survivors_for_n,
    viable_free_x_representations,
    viable_x_representations,
)
from gamma_2alpha_endpoint_automaton import PlacedEdge, alpha_corner, apex_corner  # noqa: E402
from gamma_2alpha_low_mixed_shell_census import paths_by_endpoint_and_mixed  # noqa: E402


Triple = tuple[int, int, int]
EndpointMixed = tuple[PlacedEdge, PlacedEdge, int]
PathIndex = dict[EndpointMixed, tuple[tuple[PlacedEdge, ...], ...]]


def count_for_orientation(
    *,
    cap: int,
    left_index: PathIndex,
    right_index: PathIndex,
    base_index: PathIndex,
) -> int:
    total = 0
    for (left_first, left_last, left_mixed), left_paths in left_index.items():
        for (right_first, right_last, right_mixed), right_paths in right_index.items():
            if left_mixed + right_mixed > cap - 1:
                continue
            if not apex_corner(left_last, right_first):
                continue
            for (base_first, base_last, base_mixed), base_paths in base_index.items():
                if left_mixed + right_mixed + base_mixed > cap:
                    continue
                if not alpha_corner(right_last, base_first):
                    continue
                if not alpha_corner(base_last, left_first):
                    continue
                total += len(left_paths) * len(right_paths) * len(base_paths)
    return total


def count_by_cap(survivor: RefinedGamma2AlphaSurvivor, cap: int) -> int:
    candidate = survivor.candidate
    bounded_reps = viable_x_representations(candidate)
    free_reps = viable_free_x_representations(candidate)
    base_reps = survivor.y_representations
    indexes = {
        rep: paths_by_endpoint_and_mixed(rep)
        for rep in set(bounded_reps + free_reps + base_reps)
    }
    total = 0
    for left_rep in bounded_reps:
        for right_rep in free_reps:
            for base_rep in base_reps:
                total += count_for_orientation(
                    cap=cap,
                    left_index=indexes[left_rep],
                    right_index=indexes[right_rep],
                    base_index=indexes[base_rep],
                )
    if bounded_reps != free_reps:
        for left_rep in free_reps:
            for right_rep in bounded_reps:
                for base_rep in base_reps:
                    total += count_for_orientation(
                        cap=cap,
                        left_index=indexes[left_rep],
                        right_index=indexes[right_rep],
                        base_index=indexes[base_rep],
                    )
    return total


def path_inventory(survivor: RefinedGamma2AlphaSurvivor) -> Counter[str]:
    candidate = survivor.candidate
    reps = set(viable_x_representations(candidate) + viable_free_x_representations(candidate) + survivor.y_representations)
    inventory: Counter[str] = Counter()
    for rep in reps:
        index = paths_by_endpoint_and_mixed(rep)
        inventory[f"rep={rep} groups"] = len(index)
        inventory[f"rep={rep} paths"] = sum(len(paths) for paths in index.values())
    return inventory


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--max-cap", type=int, default=12)
    parser.add_argument("--min-cap", type=int, default=4)
    args = parser.parse_args()

    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)")
        for survivor in survivors:
            print(f"  tile={survivor.candidate.tile} X={survivor.candidate.x} Y={survivor.candidate.y}")
            for label, value in sorted(path_inventory(survivor).items()):
                print(f"  {label}: {value}")
            previous = 0
            for cap in range(args.min_cap, args.max_cap + 1):
                total = count_by_cap(survivor, cap)
                print(f"  cap<={cap}: {total} (new {total - previous})")
                previous = total


if __name__ == "__main__":
    main()
