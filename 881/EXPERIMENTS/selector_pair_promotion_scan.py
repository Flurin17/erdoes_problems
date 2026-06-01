#!/usr/bin/env python3
"""Scan shifted-overlap branches for pair promotion windows.

This is a compact companion to selector_reflected_front_search.py.  The
existing script reports branch and promotion data per selector candidate; this
one aggregates directed shifted-overlap branches and classifies whether pair
holes occur at the original witness, across the original witness window, or in
a nearby/custom scan window.
"""

from __future__ import annotations

import argparse
from itertools import combinations, product

from product_rank3_terminal_cover import (
    BLOCKS,
    ORDER2_THRESHOLD,
    SET_A,
    WITNESS_WINDOW,
    hsum,
    terminal_gap,
)
from selector_reflected_front_search import (
    parse_ints,
    parse_range,
    selector_candidates,
)


def representations3(elements: set[int], target: int) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    values = sorted(elements)
    element_set = set(elements)
    for i, first in enumerate(values):
        for j in range(i, len(values)):
            second = values[j]
            third = target - first - second
            if third < second:
                continue
            if third in element_set:
                out.append((first, second, third))
    return out


def scan_targets(
    mode: str,
    witness: int,
    witness_range: tuple[int, int],
    radius: int,
    explicit_range: tuple[int, int] | None,
) -> range:
    if mode == "same":
        start, end = witness_range
    elif mode == "nearby":
        start, end = witness - radius, witness + radius
    else:
        if explicit_range is None:
            raise ValueError("--scan-range is required with --promotion-window range")
        start, end = explicit_range
    return range(max(1, start), end + 1)


def pair_holes(
    elements: set[int],
    pair: set[int],
    targets: range,
) -> list[int]:
    remaining = elements - pair
    return [
        target
        for target in targets
        if target not in hsum(remaining, 3, max(target, 3 * max(remaining)))
    ]


def terminal_pair_status(
    elements: set[int],
    pair: tuple[int, int],
    witness: int,
    threshold: int,
) -> dict[str, object]:
    first, second = pair
    without_pair = elements - set(pair)
    singleton_repairs = {
        first: witness in hsum(elements - {first}, 3, max(witness, 3 * max(elements))),
        second: witness
        in hsum(elements - {second}, 3, max(witness, 3 * max(elements))),
    }
    ok_gap, gap = terminal_gap(elements, pair, witness, threshold)
    return {
        "minimal_pair_hole": (
            witness not in hsum(without_pair, 3, max(witness, 3 * max(without_pair)))
            and all(singleton_repairs.values())
        ),
        "singleton_repairs": singleton_repairs,
        "terminal_gap": ok_gap,
        "gap": gap,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", default=",".join(str(x) for x in sorted(SET_A)))
    parser.add_argument(
        "--packets",
        nargs="*",
        default=[",".join(str(x) for x in block) for block in BLOCKS],
    )
    parser.add_argument("--front", nargs="*", default=None)
    parser.add_argument(
        "--witness-range",
        default=f"{WITNESS_WINDOW[0]}:{WITNESS_WINDOW[1]}",
    )
    parser.add_argument("--threshold", type=int, default=ORDER2_THRESHOLD)
    parser.add_argument("--require-retained-mirrors", action="store_true")
    parser.add_argument("--require-all-gates-active", action="store_true")
    parser.add_argument("--no-pair-harmless", action="store_true")
    parser.add_argument("--min-shifted-rows", type=int, default=1)
    parser.add_argument(
        "--promotion-window",
        choices=("same", "nearby", "range"),
        default="nearby",
    )
    parser.add_argument("--nearby-radius", type=int, default=5)
    parser.add_argument("--scan-range", default=None)
    parser.add_argument("--require-terminal-pair", action="store_true")
    args = parser.parse_args()

    elements = set(parse_ints(args.prefix))
    packets = tuple(parse_ints(packet) for packet in args.packets)
    if args.front is None:
        front = (tuple(range(len(packets))),)
    else:
        front = tuple(parse_ints(support) for support in args.front)
    witness_range = parse_range(args.witness_range)
    explicit_range = parse_range(args.scan_range) if args.scan_range else None

    branches: list[dict[str, object]] = []
    selectors_with_candidates = 0
    for support in front:
        for selector in product(*(packets[index] for index in support)):
            candidates = selector_candidates(
                elements,
                selector,
                witness_range,
                args.threshold,
                args.require_retained_mirrors,
                args.require_all_gates_active,
                not args.no_pair_harmless,
                promotion_radius=0,
            )
            if candidates:
                selectors_with_candidates += 1
            for candidate in candidates:
                witness = int(candidate["witness"])
                branch_summary = candidate["branch_summary"]
                for gate, data in branch_summary.items():
                    shifted_rows = data["shifted_rows"]
                    for other, rows in shifted_rows.items():
                        if len(rows) < args.min_shifted_rows:
                            continue
                        pair = tuple(sorted((int(gate), int(other))))
                        targets = scan_targets(
                            args.promotion_window,
                            witness,
                            witness_range,
                            args.nearby_radius,
                            explicit_range,
                        )
                        holes = pair_holes(elements, set(pair), targets)
                        if args.require_terminal_pair:
                            holes = [
                                hole
                                for hole in holes
                                if terminal_pair_status(
                                    elements, pair, hole, args.threshold
                                )["minimal_pair_hole"]
                                and terminal_pair_status(
                                    elements, pair, hole, args.threshold
                                )["terminal_gap"]
                            ]
                        remaining = elements - set(pair)
                        repairs = representations3(remaining, witness)
                        other_active = sorted(set(selector) - set(pair))
                        branches.append(
                            {
                                "selector": selector,
                                "witness": witness,
                                "directed_pair": (int(gate), int(other)),
                                "pair": pair,
                                "rows": rows,
                                "hole_at_witness": witness
                                not in hsum(
                                    remaining, 3, max(witness, 3 * max(remaining))
                                ),
                                "scan_holes": holes,
                                "repairs_at_witness": repairs,
                                "uses_other_active": [
                                    active
                                    for active in other_active
                                    if any(active in repair for repair in repairs)
                                ],
                            }
                        )

    pair_set = sorted({branch["pair"] for branch in branches})
    hole_at_witness = [branch for branch in branches if branch["hole_at_witness"]]
    with_scan_holes = [branch for branch in branches if branch["scan_holes"]]

    print("selector pair promotion scan")
    print(f"A={sorted(elements)}")
    print(f"packets={packets}")
    print(f"front={front}")
    print(f"witness_range={witness_range}")
    print(f"require_retained_mirrors={args.require_retained_mirrors}")
    print(f"require_all_gates_active={args.require_all_gates_active}")
    print(f"require_pair_harmless={not args.no_pair_harmless}")
    print(f"min_shifted_rows={args.min_shifted_rows}")
    print(f"promotion_window={args.promotion_window}")
    print(f"nearby_radius={args.nearby_radius}")
    print(f"scan_range={explicit_range}")
    print(f"selectors_with_candidates={selectors_with_candidates}")
    print(f"directed_shifted_overlap_branches={len(branches)}")
    print(f"distinct_unordered_pairs={pair_set}")
    print(f"pair_hole_at_original_witness={len(hole_at_witness)}/{len(branches)}")
    print(f"pair_holes_on_scan_window={len(with_scan_holes)}/{len(branches)}")
    for branch in branches:
        print(
            "branch="
            f"selector={branch['selector']} w={branch['witness']} "
            f"directed_pair={branch['directed_pair']} rows={branch['rows']} "
            f"hole_at_witness={branch['hole_at_witness']} "
            f"scan_holes={branch['scan_holes']} "
            f"uses_other_active={branch['uses_other_active']} "
            f"repairs_at_witness={branch['repairs_at_witness'][:5]}"
        )


if __name__ == "__main__":
    main()
