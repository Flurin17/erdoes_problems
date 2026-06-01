#!/usr/bin/env python3
"""Diagnose the old-gate shadow rows forced by k=3 pair witnesses.

This finite check illustrates Lemmas 16.3--16.4 from PROOF.md.  For a pair
{a,b} and witness w with w notin 4(A\\{a,b}), every retained padder p in
the interval where b is too large to participate must force
w-a-p in 2(A\\{b}).
"""

from __future__ import annotations

from itertools import combinations_with_replacement


def hsum(elements: set[int], h: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(h):
        sums = {s + a for s in sums for a in ordered if s + a <= cap}
    return sums


def has_two_sum(elements: set[int], target: int) -> bool:
    for x in elements:
        if target - x in elements:
            return True
    return False


def reps3_using(elements: set[int], target: int, required: set[int]) -> bool:
    ordered = sorted(elements)
    for triple in combinations_with_replacement(ordered, 3):
        if sum(triple) == target and set(triple) & required:
            return True
    return False


def row_data(
    A: set[int],
    a: int,
    b: int,
    w: int,
    threshold: int,
) -> tuple[list[tuple[int, int, bool]], list[int]]:
    """Return forced old-gate rows and terminal-gap violations."""

    m0 = min(A)
    C = A - {a, b}
    forced = []
    terminal = []
    for p in sorted(C):
        if w - p < threshold:
            continue
        if p > w - a - 2 * m0:
            terminal.append(p)
            continue
        if p > w - b - 2 * m0:
            target = w - a - p
            forced.append((p, target, has_two_sum(A - {b}, target)))
    return forced, terminal


def diagnose(A: set[int], a: int, b: int, w: int, threshold: int) -> None:
    m0 = min(A)
    C = A - {a, b}
    cap = max(4 * max(A), w) + 20
    without = hsum(C, 4, cap)
    print("A=", sorted(A))
    print("pair=", (a, b), "w=", w, "w in 4(A\\pair)=", w in without)
    forced, terminal = row_data(A, a, b, w, threshold)
    print("forced old-gate rows (p, w-a-p, in 2(A\\{b}))=", forced)
    print("terminal-gap retained p=", terminal)
    print("three-rep uses pair for checked p=")
    for p, _, _ in forced:
        print("  p=", p, reps3_using(A, w - p, {a, b}))


def classify_candidate(
    A: set[int],
    a: int,
    b: int,
    w: int,
    threshold: int,
) -> str:
    m0 = min(A)
    cap = max(4 * max(A), w) + 20
    if w not in hsum(A, 4, cap):
        return "not4A"
    C = A - {a, b}
    if w not in hsum(C, 4, cap):
        return "success"
    for p in C:
        if w - p < threshold:
            continue
        if p > w - a - 2 * m0:
            return "terminal"
        if p > w - b - 2 * m0 and not has_two_sum(A - {b}, w - a - p):
            return "shadow"
    return "repaired_other"


def is_non_singleton_pair_witness(A: set[int], a: int, b: int, w: int) -> bool:
    cap = max(4 * max(A), w) + 20
    return (
        w in hsum(A, 4, cap)
        and w not in hsum(A - {a, b}, 4, cap)
        and w in hsum(A - {b}, 4, cap)
    )


def scan_third_stage() -> None:
    old = {1, 3, 5, 20, 21, 23, 30, 31}
    threshold = 22
    witness_range = range(41, 48)
    for b in (41, 43):
        A = old | {b}
        print("candidate b=", b)
        for a in sorted(old):
            buckets = {
                "success": [],
                "terminal": [],
                "shadow": [],
                "repaired_other": [],
                "not4A": [],
            }
            for w in witness_range:
                buckets[classify_candidate(A, a, b, w, threshold)].append(w)
            print("  old a=", a, buckets)


def row_load(A: set[int], choices: dict[int, int], b: int, threshold: int) -> None:
    """Report batched row load after choosing one witness for each old a."""

    by_witness: dict[int, int] = {}
    for a, w in sorted(choices.items()):
        by_witness.setdefault(w, a)
    selected = {a: w for w, a in sorted(by_witness.items())}
    multiplicity: dict[int, int] = {}
    total_rows = 0
    empty_rows = 0
    for a, w in sorted(selected.items()):
        rows, _ = row_data(A, a, b, w, threshold)
        if not rows:
            empty_rows += 1
        total_rows += len(rows)
        for _, target, _ in rows:
            multiplicity[target] = multiplicity.get(target, 0) + 1
    print(
        "  row-load",
        "endpoints=",
        len(choices),
        "distinct_witnesses=",
        len(selected),
        "selected=",
        selected,
        "total_rows=",
        total_rows,
        "union_rows=",
        len(multiplicity),
        "max_overlap=",
        max(multiplicity.values(), default=0),
        "empty_rows=",
        empty_rows,
    )


def scan_non_singleton_row_load() -> None:
    """Track Corollary 16.6b row load in the robust-booster third stage."""

    old = {1, 3, 5, 20, 21, 23, 30, 31}
    threshold = 22
    witness_range = range(41, 48)
    for b in (41, 43):
        A = old | {b}
        choices = {}
        for a in sorted(old):
            found = [
                w
                for w in witness_range
                if is_non_singleton_pair_witness(A, a, b, w)
            ]
            if found:
                choices[a] = found[0]
        print("non-singleton row load b=", b, "choices=", choices)
        row_load(A, choices, b, threshold)


def scan_row_burdens() -> None:
    """Print the row-reflection burden behind the third-stage stall."""

    old = {1, 3, 5, 20, 21, 23, 30, 31}
    threshold = 22
    witness_range = range(41, 48)
    for b in (41, 43):
        A = old | {b}
        print("row burden b=", b)
        for a in sorted(old):
            summaries = []
            for w in witness_range:
                cls = classify_candidate(A, a, b, w, threshold)
                rows, terminal = row_data(A, a, b, w, threshold)
                missing = [(p, target) for p, target, ok in rows if not ok]
                summaries.append(
                    (
                        w,
                        cls,
                        len(rows),
                        len(missing),
                        len(terminal),
                        missing[:3],
                    )
                )
            best = min(
                summaries,
                key=lambda item: (
                    item[1] != "success",
                    item[3],
                    item[4],
                    -item[2],
                    item[0],
                ),
            )
            successes = [item for item in summaries if item[1] == "success"]
            print(
                "  old a=",
                a,
                "best=(w,class,rows,missing,terminal,first_missing)=",
                best,
                "successes=",
                successes,
            )


def main() -> None:
    # Robust-booster pair-stage diagnostic after adding candidate b=41.
    old = {1, 3, 5, 20, 21, 23, 30, 31}
    A = old | {41}
    diagnose(A, a=20, b=41, w=47, threshold=22)
    print()
    scan_third_stage()
    print()
    scan_row_burdens()
    print()
    scan_non_singleton_row_load()


if __name__ == "__main__":
    main()
