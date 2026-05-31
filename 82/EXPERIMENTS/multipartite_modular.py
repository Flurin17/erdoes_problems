#!/usr/bin/env python3
"""Modular partitions for complete multipartite graphs.

For a complete multipartite graph with class sizes s_i, an induced subgraph
using c_i vertices from class i has internal degree |C|-c_i on class i.
It is M-modular iff all positive c_i are congruent modulo M; the one-class
case is independent and therefore modular for every M.

This script searches the resulting integer bin-packing model for lower-bound
obstructions to modular partition theorems, including dyadic lifts and
terminal-size capped partitions.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations_with_replacement, product


def full_is_modular(sizes: tuple[int, ...], modulus: int) -> bool:
    residues = {size % modulus for size in sizes}
    return len(residues) <= 1


def residue_group_partition(
    sizes: tuple[int, ...],
    source_modulus: int,
    target_modulus: int,
) -> list[tuple[int, ...]] | None:
    """Partition whole multipartite classes by their target residue.

    When all sizes are congruent modulo q and the target modulus is 2q, there
    are at most two target residues.  Grouping whole classes with the same
    target residue gives an immediate target-modular partition.
    """

    if not full_is_modular(sizes, source_modulus):
        return None
    by_residue: dict[int, list[int]] = {}
    for index, size in enumerate(sizes):
        by_residue.setdefault(size % target_modulus, []).append(index)
    parts: list[tuple[int, ...]] = []
    for indices in by_residue.values():
        counts = [0] * len(sizes)
        for index in indices:
            counts[index] = sizes[index]
        parts.append(tuple(counts))
    return parts


def valid_bin(
    counts: tuple[int, ...],
    target_modulus: int,
    max_bin_size: int | None,
) -> bool:
    positives = [count for count in counts if count]
    if not positives:
        return False
    if max_bin_size is not None and sum(positives) > max_bin_size:
        return False
    if len(positives) == 1:
        return True
    residues = {count % target_modulus for count in positives}
    return len(residues) == 1


def bin_residue(counts: tuple[int, ...], target_modulus: int) -> int | None:
    positives = [count for count in counts if count]
    if not positives:
        return None
    total = sum(positives)
    if len(positives) == 1:
        return 0
    residues = {count % target_modulus for count in positives}
    if len(residues) != 1:
        return None
    count_residue = next(iter(residues))
    return (total - count_residue) % target_modulus


def all_bins(sizes: tuple[int, ...], target_modulus: int) -> list[tuple[int, ...]]:
    return all_bins_with_cap(sizes, target_modulus, None)


def all_bins_with_cap(
    sizes: tuple[int, ...],
    target_modulus: int,
    max_bin_size: int | None,
) -> list[tuple[int, ...]]:
    ranges = [range(size + 1) for size in sizes]
    bins = []
    for counts in product(*ranges):
        if valid_bin(counts, target_modulus, max_bin_size):
            bins.append(counts)
    bins.sort(key=lambda item: (sum(item), item), reverse=True)
    return bins


def all_bins_by_residue(
    sizes: tuple[int, ...],
    target_modulus: int,
    slots: tuple[int, ...],
) -> dict[int, list[tuple[int, ...]]]:
    by_residue: dict[int, list[tuple[int, ...]]] = {slot: [] for slot in set(slots)}
    ranges = [range(size + 1) for size in sizes]
    for counts in product(*ranges):
        residue = bin_residue(counts, target_modulus)
        if residue in by_residue:
            by_residue[residue].append(counts)
    for residue in by_residue:
        by_residue[residue].sort(key=lambda item: (sum(item), item), reverse=True)
    return by_residue


def can_partition(
    sizes: tuple[int, ...],
    target_modulus: int,
    bins: int,
    max_bin_size: int | None = None,
) -> bool:
    choices = all_bins_with_cap(sizes, target_modulus, max_bin_size)

    @lru_cache(maxsize=None)
    def rec(remaining: tuple[int, ...], left: int) -> bool:
        if all(value == 0 for value in remaining):
            return True
        if left == 0:
            return False

        # Symmetry-breaking: require the first nonzero remaining coordinate to
        # be used in the next bin.
        pivot = next(i for i, value in enumerate(remaining) if value)
        for choice in choices:
            if choice[pivot] == 0:
                continue
            if all(choice[i] <= remaining[i] for i in range(len(sizes))):
                nxt = tuple(remaining[i] - choice[i] for i in range(len(sizes)))
                if rec(nxt, left - 1):
                    return True
        return False

    return rec(sizes, bins)


def find_partition(
    sizes: tuple[int, ...],
    target_modulus: int,
    bins: int,
    max_bin_size: int | None = None,
) -> list[tuple[int, ...]] | None:
    choices = all_bins_with_cap(sizes, target_modulus, max_bin_size)
    selected: dict[tuple[tuple[int, ...], int], tuple[int, ...]] = {}

    @lru_cache(maxsize=None)
    def rec(remaining: tuple[int, ...], left: int) -> bool:
        if all(value == 0 for value in remaining):
            return True
        if left == 0:
            return False

        pivot = next(i for i, value in enumerate(remaining) if value)
        for choice in choices:
            if choice[pivot] == 0:
                continue
            if all(choice[i] <= remaining[i] for i in range(len(sizes))):
                nxt = tuple(remaining[i] - choice[i] for i in range(len(sizes)))
                if rec(nxt, left - 1):
                    selected[(remaining, left)] = choice
                    return True
        return False

    if not rec(sizes, bins):
        return None

    out = []
    remaining = sizes
    left = bins
    while any(value for value in remaining):
        choice = selected[(remaining, left)]
        out.append(choice)
        remaining = tuple(remaining[i] - choice[i] for i in range(len(sizes)))
        left -= 1
    return out


def can_slot_partition(
    sizes: tuple[int, ...],
    target_modulus: int,
    slots: tuple[int, ...],
) -> bool:
    slots = tuple(sorted(slots))
    choices = all_bins_by_residue(sizes, target_modulus, slots)

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


def min_bins(
    sizes: tuple[int, ...],
    target_modulus: int,
    cap: int,
    max_bin_size: int | None,
) -> int | None:
    for bins in range(1, cap + 1):
        if can_partition(sizes, target_modulus, bins, max_bin_size):
            return bins
    return None


def search(
    source_modulus: int,
    target_modulus: int,
    max_classes: int,
    max_size: int,
    cap: int,
    exact: bool,
    max_bin_size: int | None,
    max_total_size: int | None,
    max_checked: int | None,
) -> None:
    worst = -1
    worst_sizes: tuple[int, ...] = ()
    histogram: dict[int | str, int] = {}
    checked = 0
    truncated = False
    for classes in range(1, max_classes + 1):
        for sizes in combinations_with_replacement(range(1, max_size + 1), classes):
            if max_total_size is not None and sum(sizes) > max_total_size:
                continue
            if not full_is_modular(sizes, source_modulus):
                continue
            checked += 1
            if exact:
                value = min_bins(sizes, target_modulus, cap, max_bin_size)
            else:
                parts = residue_group_partition(sizes, source_modulus, target_modulus)
                assert parts is not None
                value = len(parts) if len(parts) <= cap else None
            key: int | str = value if value is not None else "NA"
            histogram[key] = histogram.get(key, 0) + 1
            numeric = cap + 1 if value is None else value
            if numeric > worst:
                worst = numeric
                worst_sizes = sizes
            if max_checked is not None and checked >= max_checked:
                truncated = True
                break
        if truncated:
            break

    print(f"source_modulus={source_modulus}")
    print(f"target_modulus={target_modulus}")
    print(f"max_classes={max_classes}")
    print(f"max_size={max_size}")
    print(f"cap={cap}")
    if max_bin_size is not None:
        print(f"max_bin_size={max_bin_size}")
    if max_total_size is not None:
        print(f"max_total_size={max_total_size}")
    print(f"mode={'exact_minimum' if exact else 'residue_certificate'}")
    print(f"checked={checked}")
    print(f"truncated={truncated}")
    print(f"worst_value={worst if worst <= cap else 'NA'}")
    print("worst_sizes=" + ",".join(map(str, worst_sizes)))
    print("histogram=" + ("min_bins:count" if exact else "certified_bins:count"))
    for key in sorted(histogram, key=lambda item: cap + 1 if item == "NA" else item):
        print(f"  {key}: {histogram[key]}")


def search_slots(
    source_modulus: int,
    target_modulus: int,
    max_classes: int,
    max_size: int,
    slots: tuple[int, ...],
    max_checked: int | None,
) -> None:
    checked = 0
    bad: tuple[int, ...] | None = None
    truncated = False
    for classes in range(1, max_classes + 1):
        for sizes in combinations_with_replacement(range(1, max_size + 1), classes):
            if not full_is_modular(sizes, source_modulus):
                continue
            checked += 1
            if not can_slot_partition(sizes, target_modulus, slots):
                bad = sizes
                truncated = False
                break
            if max_checked is not None and checked >= max_checked:
                truncated = True
                break
        if bad is not None or truncated:
            break

    print(f"source_modulus={source_modulus}")
    print(f"target_modulus={target_modulus}")
    print(f"max_classes={max_classes}")
    print(f"max_size={max_size}")
    print("slots=" + ",".join(map(str, slots)))
    print(f"checked={checked}")
    print(f"truncated={truncated}")
    if bad is None:
        print("slot_counterexample=none")
    else:
        print("slot_counterexample=" + ",".join(map(str, bad)))


def run_fixed_sizes(
    sizes: tuple[int, ...],
    target_modulus: int,
    cap: int,
    max_bin_size: int | None,
    print_partition: bool,
) -> None:
    value = min_bins(sizes, target_modulus, cap, max_bin_size)
    print("sizes=" + ",".join(map(str, sizes)))
    print(f"target_modulus={target_modulus}")
    print(f"cap={cap}")
    if max_bin_size is not None:
        print(f"max_bin_size={max_bin_size}")
    print(f"min_bins={value if value is not None else 'NA'}")
    if print_partition and value is not None:
        parts = find_partition(sizes, target_modulus, value, max_bin_size)
        assert parts is not None
        print("partition=" + " ".join(",".join(map(str, part)) for part in parts))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-modulus", type=int, default=2)
    parser.add_argument("--target-modulus", type=int, default=4)
    parser.add_argument("--max-classes", type=int, default=5)
    parser.add_argument("--max-size", type=int, default=8)
    parser.add_argument("--cap", type=int, default=4)
    parser.add_argument("--max-bin-size", type=int)
    parser.add_argument("--max-total-size", type=int)
    parser.add_argument(
        "--sizes",
        help="comma-separated complete multipartite class sizes for a fixed check",
    )
    parser.add_argument("--print-partition", action="store_true")
    parser.add_argument(
        "--exact",
        action="store_true",
        help="compute exact minimum bin counts instead of the residue certificate",
    )
    parser.add_argument(
        "--max-checked",
        type=int,
        help="stop after this many source-modular size vectors",
    )
    parser.add_argument(
        "--slots",
        help="fixed target residues, e.g. 0,0,1,2; switches to slot mode",
    )
    args = parser.parse_args()
    if args.sizes:
        sizes = tuple(sorted(int(item) for item in args.sizes.split(",") if item))
        run_fixed_sizes(
            sizes,
            args.target_modulus,
            args.cap,
            args.max_bin_size,
            args.print_partition,
        )
        return
    if args.slots:
        slots = tuple(int(item) % args.target_modulus for item in args.slots.split(","))
        search_slots(
            args.source_modulus,
            args.target_modulus,
            args.max_classes,
            args.max_size,
            slots,
            args.max_checked,
        )
        return
    search(
        args.source_modulus,
        args.target_modulus,
        args.max_classes,
        args.max_size,
        args.cap,
        args.exact,
        args.max_bin_size,
        args.max_total_size,
        args.max_checked,
    )


if __name__ == "__main__":
    main()
