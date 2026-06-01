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

from collections import defaultdict
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


def transversals(
    elements: set[int],
    selector_family: tuple[tuple[int, ...], ...],
) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for size in (1, 2):
        for support in combinations(sorted(elements), size):
            if all(set(support) & set(selector) for selector in selector_family):
                out.append(support)
    return out


def pair_supports(elements: set[int], target: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    ordered = sorted(elements)
    for index, first in enumerate(ordered):
        for second in ordered[index:]:
            if first + second == target:
                if first == second:
                    out.append((first,))
                else:
                    out.append((first, second))
    return out


def report_shared_witnesses(
    elements: set[int],
    witnesses: dict[tuple[int, ...], list[tuple[int, tuple[int, int]]]],
) -> None:
    by_witness: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    for selector, data in witnesses.items():
        for witness, _gap in data:
            by_witness[witness].append(selector)

    print("shared_witness_transversals:")
    for witness, selectors in sorted(by_witness.items()):
        if len(selectors) < 2:
            continue
        selector_family = tuple(selectors)
        supports = transversals(elements, selector_family)
        common_core = sorted(
            set(selector_family[0]).intersection(
                *(set(selector) for selector in selector_family[1:])
            )
        )
        singleton_supports = [support for support in supports if len(support) == 1]
        sums = sorted(
            {
                support[0] * 2 if len(support) == 1 else support[0] + support[1]
                for support in supports
            }
        )
        noncommon_sums = sorted(
            {
                support[0] + support[1]
                for support in supports
                if len(support) == 2 and not set(support) & set(common_core)
            }
        )
        union = set().union(*(set(selector) for selector in selector_family))
        outside_points = sorted(
            point
            for point in elements - union
            if witness - point >= ORDER2_THRESHOLD
        )
        outside_shifts = sorted(
            witness - point
            for point in outside_points
        )
        support_set = set(supports)
        shift_supports = {
            shift: pair_supports(elements, shift) for shift in outside_shifts
        }
        all_shift_supports_transversal = all(
            set(representations) <= support_set
            for representations in shift_supports.values()
        )
        if not all_shift_supports_transversal:
            raise AssertionError(
                f"witness={witness} has non-transversal shifted supports: "
                f"{shift_supports}"
            )
        common_spikes = {
            core: [
                (point, witness - core - point)
                for point in outside_points
                if witness - core - point in elements
            ]
            for core in common_core
        }
        spike_or_noncommon = all(
            witness - point in noncommon_sums
            or any(witness - core - point in elements for core in common_core)
            for point in outside_points
        )
        if not spike_or_noncommon:
            raise AssertionError(
                f"witness={witness} violates common-core spike dichotomy"
            )
        print(
            f"  witness={witness} selectors={selector_family} "
            f"common_core={common_core} "
            f"singleton_transversals={singleton_supports} "
            f"transversal_sums={sums} outside_shifts={outside_shifts} "
            f"shift_supports={shift_supports} "
            f"all_shift_supports_transversal={all_shift_supports_transversal} "
            f"noncommon_transversal_sums={noncommon_sums} "
            f"common_spikes={common_spikes} "
            f"spike_or_noncommon={spike_or_noncommon}"
        )


def report_gate_maps(
    elements: set[int],
    witnesses: dict[tuple[int, ...], list[tuple[int, tuple[int, int]]]],
) -> None:
    print("selector_gate_maps:")
    for selector, data in witnesses.items():
        deletion = set(selector)
        for witness, _gap in data:
            rows: dict[int, dict[str, list[int]]] = {}
            for point in sorted(elements - deletion):
                shift = witness - point
                if shift < ORDER2_THRESHOLD:
                    continue
                representations = pair_supports(elements, shift)
                if not representations:
                    raise AssertionError(
                        f"missing two-sum support for selector={selector} "
                        f"witness={witness} point={point}"
                    )
                if not all(set(support) & deletion for support in representations):
                    raise AssertionError(
                        f"non-gated support for selector={selector} "
                        f"witness={witness} point={point}: {representations}"
                    )
                retained_gates = sorted(
                    gate
                    for gate in deletion
                    if witness - point - gate in elements - deletion
                )
                deleted_pair_gates = sorted(
                    gate
                    for gate in deletion
                    if witness - point - gate in deletion
                )
                if not retained_gates and not deleted_pair_gates:
                    raise AssertionError(
                        f"no gate for selector={selector} witness={witness} "
                        f"point={point}"
                    )
                rows[point] = {
                    "retained": retained_gates,
                    "deleted_pair": deleted_pair_gates,
                }
            gate_counts = {
                gate: sum(gate in row["retained"] for row in rows.values())
                for gate in selector
            }
            deleted_pair_rows = [
                point for point, row in rows.items() if row["deleted_pair"]
            ]
            print(
                f"  selector={selector} witness={witness} "
                f"rows={rows} retained_gate_counts={gate_counts} "
                f"deleted_pair_rows={deleted_pair_rows}"
            )


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
    report_shared_witnesses(SET_A, witnesses)
    report_gate_maps(SET_A, witnesses)


if __name__ == "__main__":
    main()
