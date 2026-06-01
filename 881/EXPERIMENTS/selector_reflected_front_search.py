#!/usr/bin/env python3
"""Search fixed finite selector windows for reflected-front witnesses.

This diagnostic targets Target 8.5a.7z.8.  It does not generate new
mirrors.  Instead it starts from a finite set A and asks which selector
edges already have terminal witnesses whose old-padder rows are blocked by
deleted gates, separating retained mirrors from F+F exception rows.
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
    minimal_hole,
    pair_supports,
    terminal_gap,
)


def parse_ints(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in value.split(",") if part)


def parse_range(value: str) -> tuple[int, int]:
    start, end = value.split(":", 1)
    return int(start), int(end)


def reflected_rows(
    elements: set[int],
    deletion: tuple[int, ...],
    witness: int,
    threshold: int,
) -> dict[int, dict[str, list[int]]]:
    deleted = set(deletion)
    rows: dict[int, dict[str, list[int]]] = {}
    for point in sorted(elements - deleted):
        shift = witness - point
        if shift < threshold:
            continue
        representations = pair_supports(elements, shift)
        if not representations:
            return {}
        if not all(set(support) & deleted for support in representations):
            return {}
        retained = sorted(
            gate for gate in deleted if witness - point - gate in elements - deleted
        )
        deleted_pair = sorted(
            gate for gate in deleted if witness - point - gate in deleted
        )
        if not retained and not deleted_pair:
            return {}
        rows[point] = {"retained": retained, "deleted_pair": deleted_pair}
    return rows


def pair_harmless_at(elements: set[int], witness: int) -> bool:
    cap = max(witness, 3 * max(elements))
    for rank in (1, 2):
        for deletion in combinations(sorted(elements), rank):
            if witness not in hsum(elements - set(deletion), 3, cap):
                return False
    return True


def branch_summary(
    elements: set[int],
    selector: tuple[int, ...],
    rows: dict[int, dict[str, list[int]]],
) -> dict[int, dict[str, object]]:
    deleted = set(selector)
    out: dict[int, dict[str, object]] = {}
    for gate in selector:
        retained_rows = [
            point for point, row in rows.items() if gate in row["retained"]
        ]
        usable_rows = [
            point
            for point in retained_rows
            if point + gate
            not in {first + second for first in deleted for second in deleted}
        ]
        unique_rows: list[int] = []
        shifted: dict[int, list[int]] = {
            other: [] for other in selector if other != gate
        }
        for point in usable_rows:
            supports = pair_supports(elements, point + gate)
            trivial = tuple(sorted((point, gate)))
            if supports == [trivial]:
                unique_rows.append(point)
                continue
            for other in selector:
                if other == gate:
                    continue
                if point + gate - other in elements - deleted:
                    shifted[other].append(point)
        out[gate] = {
            "retained_rows": retained_rows,
            "usable_rows": usable_rows,
            "unique_rows": unique_rows,
            "shifted_rows": {k: v for k, v in shifted.items() if v},
        }
    return out


def promotion_summary(
    elements: set[int],
    witness: int,
    branches: dict[int, dict[str, object]],
    radius: int,
) -> dict[int, dict[str, object]]:
    out: dict[int, dict[str, object]] = {}
    for gate, data in branches.items():
        unique_rows = data["unique_rows"]
        shifted_rows = data["shifted_rows"]
        gate_data: dict[str, object] = {}
        if unique_rows:
            gate_data["singleton_hole_at_witness"] = (
                witness not in hsum(elements - {gate}, 3, witness)
            )
            if radius:
                gate_data["singleton_holes_near_witness"] = [
                    target
                    for target in range(witness - radius, witness + radius + 1)
                    if target > 0 and target not in hsum(elements - {gate}, 3, target)
                ]
        shifted_promotions: dict[int, bool] = {}
        shifted_nearby: dict[int, list[int]] = {}
        for other, rows in shifted_rows.items():
            if rows:
                shifted_promotions[other] = (
                    witness not in hsum(elements - {gate, other}, 3, witness)
                )
                if radius:
                    shifted_nearby[other] = [
                        target
                        for target in range(witness - radius, witness + radius + 1)
                        if target > 0
                        and target not in hsum(
                            elements - {gate, other}, 3, target
                        )
                    ]
        if shifted_promotions:
            gate_data["pair_hole_at_witness"] = shifted_promotions
        if shifted_nearby:
            gate_data["pair_holes_near_witness"] = shifted_nearby
        if gate_data:
            out[gate] = gate_data
    return out


def selector_candidates(
    elements: set[int],
    selector: tuple[int, ...],
    witness_range: tuple[int, int],
    threshold: int,
    require_retained_mirrors: bool,
    require_all_gates_active: bool,
    require_pair_harmless: bool,
    promotion_radius: int,
) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for witness in range(witness_range[0], witness_range[1] + 1):
        ok_gap, gap = terminal_gap(elements, selector, witness, threshold)
        if not ok_gap or not minimal_hole(elements, selector, witness):
            continue
        if require_pair_harmless and not pair_harmless_at(elements, witness):
            continue
        rows = reflected_rows(elements, selector, witness, threshold)
        if not rows:
            continue
        if require_retained_mirrors and any(not row["retained"] for row in rows.values()):
            continue
        retained_counts = {
            gate: sum(gate in row["retained"] for row in rows.values())
            for gate in selector
        }
        if require_all_gates_active and any(count == 0 for count in retained_counts.values()):
            continue
        deleted_pair_rows = [
            point for point, row in rows.items() if row["deleted_pair"]
        ]
        branches = branch_summary(elements, selector, rows)
        out.append(
            {
                "witness": witness,
                "gap": gap,
                "rows": rows,
                "retained_counts": retained_counts,
                "deleted_pair_rows": deleted_pair_rows,
                "branch_summary": branches,
                "promotion_summary": promotion_summary(
                    elements, witness, branches, promotion_radius
                ),
            }
        )
    return out


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
    parser.add_argument("--promotion-radius", type=int, default=0)
    args = parser.parse_args()

    elements = set(parse_ints(args.prefix))
    packets = tuple(parse_ints(packet) for packet in args.packets)
    if args.front is None:
        front = (tuple(range(len(packets))),)
    else:
        front = tuple(parse_ints(support) for support in args.front)
    witness_range = parse_range(args.witness_range)

    print("fixed-A reflected-front search")
    print(f"A={sorted(elements)}")
    print(f"packets={packets}")
    print(f"front={front}")
    print(f"witness_range={witness_range}")
    print(f"require_retained_mirrors={args.require_retained_mirrors}")
    print(f"require_all_gates_active={args.require_all_gates_active}")
    print(f"require_pair_harmless={not args.no_pair_harmless}")
    print(f"promotion_radius={args.promotion_radius}")

    missing: list[tuple[int, ...]] = []
    total = 0
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
                args.promotion_radius,
            )
            total += len(candidates)
            if not candidates:
                missing.append(selector)
            print(f"selector={selector} candidates={candidates}")
    print(f"total_candidates={total}")
    print(f"missing_selectors={missing}")


if __name__ == "__main__":
    main()
