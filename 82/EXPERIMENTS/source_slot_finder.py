#!/usr/bin/env python3
"""Search source-residue slot families in complete multipartite models."""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations, combinations_with_replacement


def slot_weight(residue: int, modulus: int) -> int:
    value = (residue + 1) % modulus
    return modulus if value == 0 else value


def subset_sum(slots: tuple[int, ...], modulus: int, target: int) -> bool:
    weights = [slot_weight(residue, modulus) for residue in slots]
    possible = {0}
    for weight in weights:
        possible |= {value + weight for value in list(possible)}
    return target in possible


def passes_clique_test(
    slots: tuple[int, ...],
    source_modulus: int,
    source_residue: int,
    target_modulus: int,
) -> bool:
    first = (source_residue + 1) % target_modulus
    if first == 0:
        first = target_modulus
    second = first + source_modulus
    if second > target_modulus:
        second -= target_modulus
    if second == 0:
        second = target_modulus
    return subset_sum(slots, target_modulus, first) and subset_sum(
        slots, target_modulus, second
    )


def source_degree_residue(sizes: tuple[int, ...], source_modulus: int) -> int:
    return (sum(sizes) - sizes[0]) % source_modulus


def source_vectors(
    source_modulus: int,
    source_residue: int,
    max_classes: int,
    max_size: int,
) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for classes in range(1, max_classes + 1):
        for sizes in combinations_with_replacement(range(1, max_size + 1), classes):
            if len({size % source_modulus for size in sizes}) > 1:
                continue
            if source_degree_residue(sizes, source_modulus) != source_residue % source_modulus:
                continue
            out.append(sizes)
    return out


def legal_bins_by_residue(
    sizes: tuple[int, ...],
    target_modulus: int,
    slots: tuple[int, ...],
) -> dict[int, list[tuple[int, ...]]]:
    slot_set = set(slots)
    bins: dict[int, set[tuple[int, ...]]] = {slot: set() for slot in slot_set}

    # A bin meeting a single multipartite class is independent, regardless of
    # how many vertices it takes from that class.
    if 0 in slot_set:
        for index, size in enumerate(sizes):
            for count in range(1, size + 1):
                vector = [0] * len(sizes)
                vector[index] = count
                bins[0].add(tuple(vector))

    # A bin meeting at least two classes is target-modular exactly when all
    # positive class intersections are congruent modulo the target modulus.
    for count_residue in range(target_modulus):
        choices: list[list[int]] = []
        for size in sizes:
            first = count_residue if count_residue else target_modulus
            choices.append(list(range(first, size + 1, target_modulus)))

        current = [0] * len(sizes)

        def rec(index: int, positive: int, total: int) -> None:
            if index == len(sizes):
                if positive >= 2:
                    residue = (total - count_residue) % target_modulus
                    if residue in slot_set:
                        bins[residue].add(tuple(current))
                return
            rec(index + 1, positive, total)
            for count in choices[index]:
                current[index] = count
                rec(index + 1, positive + 1, total + count)
                current[index] = 0

        rec(0, 0, 0)

    out = {residue: list(values) for residue, values in bins.items()}
    for residue in out:
        out[residue].sort(key=lambda item: (sum(item), item), reverse=True)
    return out


def can_slot_partition_fast(
    sizes: tuple[int, ...],
    target_modulus: int,
    slots: tuple[int, ...],
) -> bool:
    if max(sizes) <= target_modulus:
        return can_slot_partition_canonical(sizes, target_modulus, slots)
    slots = tuple(sorted(slots))
    choices = legal_bins_by_residue(sizes, target_modulus, slots)

    def remove_slot(state: tuple[int, ...], residue: int) -> tuple[int, ...]:
        out = list(state)
        out.remove(residue)
        return tuple(out)

    @lru_cache(maxsize=None)
    def rec(remaining: tuple[int, ...], state: tuple[int, ...]) -> bool:
        if all(value == 0 for value in remaining):
            return True
        if not state:
            return False
        pivot = next(i for i, value in enumerate(remaining) if value)
        for residue in sorted(set(state)):
            next_state = remove_slot(state, residue)
            for choice in choices[residue]:
                if choice[pivot] == 0:
                    continue
                if all(choice[i] <= remaining[i] for i in range(len(sizes))):
                    nxt = tuple(remaining[i] - choice[i] for i in range(len(sizes)))
                    if rec(nxt, next_state):
                        return True
        return False

    return rec(sizes, slots)


def can_slot_partition_symmetric(
    class_size: int,
    classes: int,
    target_modulus: int,
    slots: tuple[int, ...],
) -> bool:
    return can_slot_partition_canonical(tuple([class_size] * classes), target_modulus, slots)


def can_slot_partition_canonical(
    sizes: tuple[int, ...],
    target_modulus: int,
    slots: tuple[int, ...],
) -> bool:
    """Check bounded-size multipartite vectors using class symmetry.

    The general checker distinguishes labelled multipartite classes.  When all
    class sizes are at most the target modulus, every multi-class legal bin
    uses the same positive count in every class it meets.  Then only the sorted
    vector of remaining class capacities matters, which avoids a large amount
    of repeated work.
    """
    slots = tuple(sorted(slots))
    initial = tuple(sorted(sizes, reverse=True))
    max_count = max(sizes)

    @lru_cache(maxsize=None)
    def rec(remaining: tuple[int, ...], state: tuple[int, ...]) -> bool:
        if all(value == 0 for value in remaining):
            return True
        if not state:
            return False
        positive_indices = [i for i, value in enumerate(remaining) if value > 0]
        for index, residue in enumerate(state):
            next_state = state[:index] + state[index + 1 :]

            if residue == 0:
                singleton_seen: set[tuple[int, ...]] = set()
                for i in positive_indices:
                    for count in range(1, remaining[i] + 1):
                        nxt = list(remaining)
                        nxt[i] -= count
                        canonical = tuple(sorted(nxt, reverse=True))
                        if canonical in singleton_seen:
                            continue
                        singleton_seen.add(canonical)
                        if rec(canonical, next_state):
                            return True

            seen: set[tuple[int, ...]] = set()
            for count in range(1, max_count + 1):
                usable = [i for i, value in enumerate(remaining) if value >= count]
                for take in range(2, len(usable) + 1):
                    if ((take - 1) * count) % target_modulus != residue:
                        continue
                    for indices in combinations(usable, take):
                        nxt = list(remaining)
                        for i in indices:
                            nxt[i] -= count
                        canonical = tuple(sorted(nxt, reverse=True))
                        if canonical in seen:
                            continue
                        seen.add(canonical)
                        if rec(canonical, next_state):
                            return True
        return False

    return rec(initial, slots)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-modulus", type=int, required=True)
    parser.add_argument("--target-modulus", type=int, required=True)
    parser.add_argument("--source-residue", type=int, required=True)
    parser.add_argument("--slot-count", type=int, required=True)
    parser.add_argument(
        "--candidates",
        help="semicolon-separated residue multisets, e.g. 0,0,0,8;0,0,8,8",
    )
    parser.add_argument("--max-classes", type=int, default=5)
    parser.add_argument("--max-size", type=int, default=16)
    parser.add_argument("--max-vectors", type=int)
    parser.add_argument("--max-survivors", type=int, default=20)
    parser.add_argument("--no-clique-filter", action="store_true")
    args = parser.parse_args()

    if args.candidates:
        candidates = [
            tuple(int(item) % args.target_modulus for item in block.split(",") if item)
            for block in args.candidates.split(";")
            if block
        ]
    else:
        candidates = list(
            combinations_with_replacement(range(args.target_modulus), args.slot_count)
        )
    if not args.no_clique_filter:
        candidates = [
            slots
            for slots in candidates
            if passes_clique_test(
                slots,
                args.source_modulus,
                args.source_residue,
                args.target_modulus,
            )
        ]

    vectors = source_vectors(
        args.source_modulus,
        args.source_residue,
        args.max_classes,
        args.max_size,
    )

    @lru_cache(maxsize=None)
    def can_partition(sizes: tuple[int, ...], slots: tuple[int, ...]) -> bool:
        return can_slot_partition_fast(sizes, args.target_modulus, slots)

    survivors = list(candidates)
    killed_by: dict[tuple[int, ...], tuple[int, ...]] = {}
    checked_vectors = 0
    truncated = False
    for sizes in vectors:
        if args.max_vectors is not None and checked_vectors >= args.max_vectors:
            truncated = True
            break
        checked_vectors += 1
        next_survivors: list[tuple[int, ...]] = []
        for slots in survivors:
            if can_partition(sizes, slots):
                next_survivors.append(slots)
            else:
                killed_by.setdefault(slots, sizes)
        survivors = next_survivors
        if not survivors:
            break

    print(f"source_modulus={args.source_modulus}")
    print(f"source_residue={args.source_residue % args.source_modulus}")
    print(f"target_modulus={args.target_modulus}")
    print(f"slot_count={args.slot_count}")
    print(f"max_classes={args.max_classes}")
    print(f"max_size={args.max_size}")
    print(f"clique_filter={not args.no_clique_filter}")
    print(f"candidate_count={len(candidates)}")
    print(f"source_vectors={len(vectors)}")
    print(f"checked_vectors={checked_vectors}")
    print(f"truncated={truncated}")
    print(f"survivor_count={len(survivors)}")
    for slots in survivors[: args.max_survivors]:
        print("survivor=" + ",".join(map(str, slots)))
    if len(survivors) > args.max_survivors:
        print(f"survivor_omitted={len(survivors) - args.max_survivors}")
    if not survivors and killed_by:
        # The last vector considered killed the final survivors; report it as
        # a compact obstruction seed for reproducing the failure.
        print("last_killer=" + ",".join(map(str, sizes)))


if __name__ == "__main__":
    main()
