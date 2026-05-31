#!/usr/bin/env python3
"""Search finite windows for the moving-anchor bridge repair.

Lemma 8.2a' gives a way to prove that deleting B={b_j} still leaves an
order-3 basis.  With a fixed padder t, each new deleted b_j needs retained
e_j,q_j such that

    t + b_j = e_j + q_j
    e_j + b_i in 2C for all i <= j.

This script checks finite windows for such bridge data.  It is a local
diagnostic: passing here does not prove an infinite construction, but
failure on a finite obstruction shows why reflected rows alone are not
enough.
"""

from __future__ import annotations

import argparse
from itertools import combinations, permutations


def sums2(elements: set[int]) -> set[int]:
    return {a + b for a in elements for b in elements}


def bridge_data(
    elements: set[int],
    deletion: tuple[int, ...],
) -> list[tuple[int, list[tuple[int, int, int]]]]:
    deleted = set(deletion)
    kept = elements - deleted
    two_kept = sums2(kept)
    out: list[tuple[int, list[tuple[int, int, int]]]] = []
    for t in sorted(kept):
        rows: list[tuple[int, int, int]] = []
        ok = True
        for j, b in enumerate(deletion):
            previous = deletion[: j + 1]
            choices: list[tuple[int, int]] = []
            for e in sorted(kept):
                q = t + b - e
                if q not in kept:
                    continue
                if all(e + old_b in two_kept for old_b in previous):
                    choices.append((e, q))
            if not choices:
                ok = False
                break
            e, q = choices[0]
            rows.append((b, e, q))
        if ok:
            out.append((t, rows))
    return out


def bridge_data_any_order(
    elements: set[int],
    deletion: tuple[int, ...],
) -> list[tuple[tuple[int, ...], int, list[tuple[int, int, int]]]]:
    out: list[tuple[tuple[int, ...], int, list[tuple[int, int, int]]]] = []
    for ordered_deletion in permutations(deletion):
        for t, rows in bridge_data(elements, ordered_deletion):
            out.append((ordered_deletion, t, rows))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-value", type=int, default=22)
    parser.add_argument("--max-size", type=int, default=10)
    parser.add_argument("--rank", type=int, default=2)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument(
        "--examples",
        action="store_true",
        help="check the named finite delayed-barrier examples",
    )
    parser.add_argument(
        "--all-orders",
        action="store_true",
        help="try every ordering of each finite deletion",
    )
    args = parser.parse_args()

    if args.examples:
        examples = [
            ("delayed-pair", {1, 2, 3, 5, 6, 7}, (5, 7)),
            ("delayed-rank3", {1, 2, 3, 4, 5, 6, 7, 8}, (4, 5, 6)),
            ("alternating-hole", {1, 2, 3, 6, 7, 8}, (6, 8)),
            ("first-schreier-pair", {1, 2, 3, 4, 8}, (1, 4)),
            ("first-schreier-triple", {1, 2, 3, 4, 8}, (2, 3, 4)),
            (
                "tail-p5-pair",
                {1, 2, 4, 5, 8, 10, 15, 18, 19, 30},
                (10, 30),
            ),
            (
                "p6-pair-escape",
                {1, 2, 4, 5, 8, 10, 15, 18, 19, 30, 38, 40, 43, 44},
                (10, 38),
            ),
        ]
        for name, elements, deletion in examples:
            if args.all_orders:
                all_data = bridge_data_any_order(elements, deletion)
                data = [(order, t, rows) for order, t, rows in all_data]
            else:
                data = [(deletion, t, rows) for t, rows in bridge_data(elements, deletion)]
            print(name)
            print("  S=", sorted(elements), "F=", deletion)
            if not data:
                print("  no bridge data")
            for order, t, rows in data[: args.limit]:
                print("  order=", order, "t=", t, "rows=", rows)
        return

    found = 0
    for max_value in range(max(6, args.rank + 3), args.max_value + 1):
        for size in range(args.rank + 2, min(max_value, args.max_size) + 1):
            for tuple_s in combinations(range(1, max_value + 1), size):
                if tuple_s[-1] != max_value:
                    continue
                elements = set(tuple_s)
                for deletion in combinations(tuple_s, args.rank):
                    if args.all_orders:
                        all_data = bridge_data_any_order(elements, deletion)
                        data = [(order, t, rows) for order, t, rows in all_data]
                    else:
                        data = [(deletion, t, rows) for t, rows in bridge_data(elements, deletion)]
                    if not data:
                        continue
                    print("finite bridge repair data")
                    print("S=", sorted(elements), "F=", deletion)
                    for order, t, rows in data[:3]:
                        print("  order=", order, "t=", t, "rows=", rows)
                    found += 1
                    if found >= args.limit:
                        return
    print("no bridge repair data found within searched bounds")


if __name__ == "__main__":
    main()
