#!/usr/bin/env python3
"""Complete multipartite count model for the matching-slot target.

For complete multipartite class sizes s_i, an induced set using c_i vertices
from class i gives each selected vertex in class i internal degree
sum_j c_j - c_i.  The matching-slot target asks for at most two 0 mod 4 bins,
one exact induced matching bin, and one 2 mod 4 bin.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations_with_replacement


Slot = int
ZERO: Slot = 0
MATCHING: Slot = 1
TWO: Slot = 2


def is_even_complete_multipartite(sizes: tuple[int, ...]) -> bool:
    total = sum(sizes)
    return all((total - size) % 2 == 0 for size in sizes)


def residue_of_bin(counts: tuple[int, ...]) -> int | None:
    positives = [count for count in counts if count]
    if not positives:
        return None
    if len(positives) == 1:
        return 0
    residues = {count % 4 for count in positives}
    if len(residues) != 1:
        return None
    count_residue = next(iter(residues))
    return (sum(positives) - count_residue) % 4


def is_exact_matching_bin(counts: tuple[int, ...]) -> bool:
    return sorted(count for count in counts if count) == [1, 1]


def legal_choices(sizes: tuple[int, ...], slot: Slot) -> list[tuple[int, ...]]:
    choices: list[tuple[int, ...]] = []
    current = [0] * len(sizes)

    def rec(index: int) -> None:
        if index == len(sizes):
            counts = tuple(current)
            if slot == MATCHING:
                if is_exact_matching_bin(counts):
                    choices.append(counts)
                return
            residue = residue_of_bin(counts)
            if residue == slot:
                choices.append(counts)
            return
        for value in range(sizes[index] + 1):
            current[index] = value
            rec(index + 1)
        current[index] = 0

    rec(0)
    choices.sort(key=lambda item: (sum(item), item), reverse=True)
    return choices


def can_partition(sizes: tuple[int, ...]) -> bool:
    slots = (ZERO, ZERO, MATCHING, TWO)
    choices = {slot: legal_choices(sizes, slot) for slot in set(slots)}

    def remove_slot(state: tuple[Slot, ...], slot: Slot) -> tuple[Slot, ...]:
        out = list(state)
        out.remove(slot)
        return tuple(out)

    @lru_cache(maxsize=None)
    def rec(remaining: tuple[int, ...], state: tuple[Slot, ...]) -> bool:
        if all(value == 0 for value in remaining):
            return True
        if not state:
            return False
        pivot = next(i for i, value in enumerate(remaining) if value)
        for slot in sorted(set(state)):
            next_state = remove_slot(state, slot)
            # Empty slots are allowed.
            if rec(remaining, next_state):
                return True
            for choice in choices[slot]:
                if choice[pivot] == 0:
                    continue
                if all(choice[i] <= remaining[i] for i in range(len(sizes))):
                    nxt = tuple(remaining[i] - choice[i] for i in range(len(sizes)))
                    if rec(nxt, next_state):
                        return True
        return False

    return rec(sizes, slots)


def find_partition(sizes: tuple[int, ...]) -> list[tuple[Slot, tuple[int, ...]]] | None:
    slots = (ZERO, ZERO, MATCHING, TWO)
    choices = {slot: legal_choices(sizes, slot) for slot in set(slots)}
    selected: dict[tuple[tuple[int, ...], tuple[Slot, ...]], tuple[Slot, tuple[int, ...] | None]] = {}

    def remove_slot(state: tuple[Slot, ...], slot: Slot) -> tuple[Slot, ...]:
        out = list(state)
        out.remove(slot)
        return tuple(out)

    @lru_cache(maxsize=None)
    def rec(remaining: tuple[int, ...], state: tuple[Slot, ...]) -> bool:
        if all(value == 0 for value in remaining):
            return True
        if not state:
            return False
        pivot = next(i for i, value in enumerate(remaining) if value)
        for slot in sorted(set(state)):
            next_state = remove_slot(state, slot)
            if rec(remaining, next_state):
                selected[(remaining, state)] = (slot, None)
                return True
            for choice in choices[slot]:
                if choice[pivot] == 0:
                    continue
                if all(choice[i] <= remaining[i] for i in range(len(sizes))):
                    nxt = tuple(remaining[i] - choice[i] for i in range(len(sizes)))
                    if rec(nxt, next_state):
                        selected[(remaining, state)] = (slot, choice)
                        return True
        return False

    if not rec(sizes, slots):
        return None
    out: list[tuple[Slot, tuple[int, ...]]] = []
    remaining = sizes
    state = slots
    while any(remaining):
        slot, choice = selected[(remaining, state)]
        state = remove_slot(state, slot)
        if choice is None:
            continue
        out.append((slot, choice))
        remaining = tuple(remaining[i] - choice[i] for i in range(len(sizes)))
    return out


def search(max_classes: int, max_size: int, max_total: int | None) -> None:
    checked = 0
    for classes in range(1, max_classes + 1):
        for sizes in combinations_with_replacement(range(1, max_size + 1), classes):
            if max_total is not None and sum(sizes) > max_total:
                continue
            if not is_even_complete_multipartite(sizes):
                continue
            checked += 1
            if not can_partition(sizes):
                print(f"max_classes={max_classes}")
                print(f"max_size={max_size}")
                if max_total is not None:
                    print(f"max_total={max_total}")
                print(f"checked_before_counterexample={checked}")
                print("counterexample=" + ",".join(map(str, sizes)))
                return
    print(f"max_classes={max_classes}")
    print(f"max_size={max_size}")
    if max_total is not None:
        print(f"max_total={max_total}")
    print(f"checked={checked}")
    print("no_counterexample_seen")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", help="comma-separated complete multipartite class sizes")
    parser.add_argument("--max-classes", type=int, default=5)
    parser.add_argument("--max-size", type=int, default=10)
    parser.add_argument("--max-total", type=int)
    args = parser.parse_args()

    if args.sizes:
        sizes = tuple(sorted(int(item) for item in args.sizes.split(",") if item))
        print("sizes=" + ",".join(map(str, sizes)))
        print(f"even_complete_multipartite={is_even_complete_multipartite(sizes)}")
        partition = find_partition(sizes)
        print(f"matching_partition={partition is not None}")
        if partition is not None:
            for slot, choice in partition:
                print(f"slot={slot} counts=" + ",".join(map(str, choice)))
        return

    search(args.max_classes, args.max_size, args.max_total)


if __name__ == "__main__":
    main()
