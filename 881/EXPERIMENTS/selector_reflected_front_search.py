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


def selector_candidates(
    elements: set[int],
    selector: tuple[int, ...],
    witness_range: tuple[int, int],
    threshold: int,
    require_retained_mirrors: bool,
    require_all_gates_active: bool,
    require_pair_harmless: bool,
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
        out.append(
            {
                "witness": witness,
                "gap": gap,
                "rows": rows,
                "retained_counts": retained_counts,
                "deleted_pair_rows": deleted_pair_rows,
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
            )
            total += len(candidates)
            if not candidates:
                missing.append(selector)
            print(f"selector={selector} candidates={candidates}")
    print(f"total_candidates={total}")
    print(f"missing_selectors={missing}")


if __name__ == "__main__":
    main()
