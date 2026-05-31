#!/usr/bin/env python3
"""Exact overlap-cause sampler for high-mixed `gamma=2alpha` shells.

The high-mixed boundary-shell space is too large to enumerate naively.  This
diagnostic samples valid boundary shells and records the first exact
positive-area shell overlap, grouped by outer-side pair and boundary-tile
positions.  The goal is to identify local overlap patterns that may become
proof-level lemmas.
"""

from __future__ import annotations

import argparse
import random
import sys
from collections import Counter
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamma_2alpha_quadratic_shell_census as exact  # noqa: E402
from gamma_2alpha_boundary import refined_survivors_for_n  # noqa: E402
from gamma_2alpha_boundary import RefinedGamma2AlphaSurvivor  # noqa: E402
from gamma_2alpha_boundary_transition_demand import BoundaryDemand, path_labels  # noqa: E402
from gamma_2alpha_random_shell_search import mixed_transitions, weighted_valid_demands  # noqa: E402


def label_position(label: str) -> str:
    return label.split(":", 1)[0]


def side_pair(left: str, right: str) -> str:
    return "".join(sorted((left[0], right[0])))


def first_exact_overlap(
    survivor: RefinedGamma2AlphaSurvivor,
    demand: BoundaryDemand,
    radicand: int,
) -> tuple[str, str] | None:
    exact.RADICAND = radicand
    shell = exact.place_boundary_shell(survivor, demand, radicand)
    outer = exact.outer_vertices(survivor, radicand)
    if shell is None or outer is None:
        return None
    integer_shell, _integer_outer, _scale = exact.kscale_shell(shell, outer)
    boxes = tuple(exact.kbbox(tile.polygon) for tile in integer_shell)
    for left in range(len(integer_shell)):
        for right in range(left + 1, len(integer_shell)):
            if exact.kbbox_disjoint(boxes[left], boxes[right]):
                continue
            if exact.ksame_triangle(integer_shell[left].polygon, integer_shell[right].polygon):
                continue
            if exact.kpositive_overlap(integer_shell[left].polygon, integer_shell[right].polygon):
                return integer_shell[left].label, integer_shell[right].label
    return None


def print_example(label: str, demand: BoundaryDemand) -> None:
    print(
        f"    {label}: L={path_labels(demand.left_path)} "
        f"R={path_labels(demand.right_path)} "
        f"B={path_labels(demand.base_path)} "
        f"mixed={mixed_transitions(demand.left_path) + mixed_transitions(demand.right_path) + mixed_transitions(demand.base_path)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--samples", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=634)
    parser.add_argument("--max-total-mixed", type=int)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--show-examples", action="store_true")
    parser.add_argument(
        "--classify-non-overlap",
        action="store_true",
        help="also run the residual classifier for sampled shells with no proper overlap",
    )
    args = parser.parse_args()

    rng = random.Random(args.seed)
    for n in args.n:
        survivors = refined_survivors_for_n(n)
        print(f"N={n}: {len(survivors)} refined gamma=2alpha survivor(s)", flush=True)
        for survivor in survivors:
            radicand = exact.field_radicand(survivor)
            if radicand is None:
                print("  exact quadratic classifier unavailable", flush=True)
                continue
            demands = weighted_valid_demands(
                survivor,
                rng=rng,
                samples=args.samples,
                max_total_mixed=args.max_total_mixed,
            )
            status_counts: Counter[str] = Counter()
            pair_counts: Counter[str] = Counter()
            label_counts: Counter[tuple[str, str]] = Counter()
            position_counts: Counter[tuple[str, str]] = Counter()
            mixed_counts: Counter[int] = Counter()
            examples: dict[str, BoundaryDemand] = {}
            for demand in demands:
                overlap = first_exact_overlap(survivor, demand, radicand)
                if overlap is None:
                    if args.classify_non_overlap:
                        result = exact.classify_quadratic_shell(survivor, demand, radicand)
                        status_counts[result.status] += 1
                        examples.setdefault(result.status, demand)
                    else:
                        status_counts["no-proper-overlap"] += 1
                        examples.setdefault("no-proper-overlap", demand)
                    continue
                left, right = overlap
                status_counts["proper-overlap"] += 1
                pair = side_pair(left, right)
                pair_counts[pair] += 1
                label_counts[(left, right)] += 1
                position_pair = (label_position(left), label_position(right))
                position_counts[position_pair] += 1
                mixed_counts[demand.mixed_transitions] += 1
                examples.setdefault(f"overlap {pair}", demand)

            print(f"  valid-weighted samples={len(demands)} from {args.samples} attempts")
            print(f"  status counts={dict(sorted(status_counts.items()))}")
            print(f"  overlap side-pair counts={dict(sorted(pair_counts.items()))}")
            print(f"  overlap mixed counts={dict(sorted(mixed_counts.items()))}")
            print("  top overlap positions:")
            for (left, right), count in position_counts.most_common(args.top):
                print(f"    {left} with {right}: {count}")
            print("  top overlap labels:")
            for (left, right), count in label_counts.most_common(args.top):
                print(f"    {left} with {right}: {count}")
            if args.show_examples:
                for label, demand in sorted(examples.items()):
                    print_example(label, demand)


if __name__ == "__main__":
    main()
