#!/usr/bin/env python3
"""Check a finite rank-3 product cover by terminal-gap holes.

This is a local diagnostic for the obstruction isolated in Corollaries
8.5a.7v--8.5a.7y.  It verifies one small finite window where:

* 2A covers a test interval;
* every singleton and pair deletion is harmless on a later window;
* three two-point packets form a complete rank-3 product cover, because
  every selector triple has an inclusion-minimal three-sum hole with the
  terminal-gap normal form.

The example is not an infinite construction.  It only shows that the final
large-spread rank-3 product obstruction is locally compatible.
"""

from __future__ import annotations

from itertools import combinations, product


SET_A = {1, 3, 4, 5, 8, 10, 11, 12}
BLOCKS = ((4, 10), (5, 11), (8, 12))
ORDER2_THRESHOLD = 4
WITNESS_WINDOW = (14, 23)


def hsum(elements: set[int], order: int, cap: int) -> set[int]:
    sums = {0}
    ordered = tuple(sorted(elements))
    for _ in range(order):
        sums = {
            value + element
            for value in sums
            for element in ordered
            if value + element <= cap
        }
    return sums


def covers(values: set[int], start: int, end: int) -> bool:
    return all(target in values for target in range(start, end + 1))


def cover_end(values: set[int], start: int, cap: int) -> int:
    target = start
    while target <= cap and target in values:
        target += 1
    return target - 1


def minimal_hole(elements: set[int], deletion: tuple[int, ...], witness: int) -> bool:
    removed = set(deletion)
    if witness in hsum(elements - removed, 3, witness):
        return False
    return all(
        witness in hsum(elements - (removed - {point}), 3, witness)
        for point in removed
    )


def terminal_gap(
    elements: set[int],
    deletion: tuple[int, ...],
    witness: int,
    order2_threshold: int,
) -> tuple[bool, tuple[int, int]]:
    removed = set(deletion)
    left = witness - min(deletion) - min(elements)
    right = witness - order2_threshold
    return (
        not any(left < point <= right for point in elements - removed),
        (left, right),
    )


def selector_witnesses(
    elements: set[int],
    blocks: tuple[tuple[int, ...], ...],
    witness_window: tuple[int, int],
    order2_threshold: int,
) -> dict[tuple[int, ...], list[tuple[int, tuple[int, int]]]]:
    out: dict[tuple[int, ...], list[tuple[int, tuple[int, int]]]] = {}
    for selector in product(*blocks):
        witnesses: list[tuple[int, tuple[int, int]]] = []
        for witness in range(witness_window[0], witness_window[1] + 1):
            ok_gap, gap = terminal_gap(elements, selector, witness, order2_threshold)
            if ok_gap and minimal_hole(elements, selector, witness):
                witnesses.append((witness, gap))
        out[selector] = witnesses
    return out


def main() -> None:
    cap = 3 * max(SET_A)
    two_sums = hsum(SET_A, 2, cap)
    two_end = cover_end(two_sums, ORDER2_THRESHOLD, cap)
    if not covers(two_sums, ORDER2_THRESHOLD, two_end):
        raise AssertionError("order-2 coverage interval is inconsistent")

    window_start, window_end = WITNESS_WINDOW
    if window_end > two_end:
        raise AssertionError("test window extends past two-sum coverage")
    if two_end < window_end + min(SET_A):
        raise AssertionError("positive-summand stage buffer is missing")

    lower_ok = True
    bad_lower: list[tuple[int, ...]] = []
    for rank in (1, 2):
        for deletion in combinations(sorted(SET_A), rank):
            if not covers(hsum(SET_A - set(deletion), 3, cap), window_start, window_end):
                lower_ok = False
                bad_lower.append(deletion)

    witnesses = selector_witnesses(SET_A, BLOCKS, WITNESS_WINDOW, ORDER2_THRESHOLD)
    missing = [selector for selector, data in witnesses.items() if not data]
    if bad_lower or missing:
        raise AssertionError(f"bad_lower={bad_lower} missing={missing}")

    print("rank-3 product terminal-cover window")
    print(f"A={sorted(SET_A)}")
    print(f"blocks={BLOCKS}")
    print(f"two_coverage=({ORDER2_THRESHOLD}, {two_end})")
    print(f"witness_window={WITNESS_WINDOW}")
    print(f"stage_buffer={two_end - window_end}")
    print(f"singleton_pair_harmless={lower_ok}")
    for selector, data in witnesses.items():
        print(f"selector={selector} witnesses={data}")


if __name__ == "__main__":
    main()
