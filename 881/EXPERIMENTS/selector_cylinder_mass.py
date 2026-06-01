#!/usr/bin/env python3
"""Finite checks for the selector cylinder mass lemma.

The lemma is a union-bound statement: if cylinders cover every selector in a
finite product, their product masses sum to at least one.  This script
exhausts the two-block binary case and samples a few larger products.
"""

from __future__ import annotations

from itertools import combinations, product
from random import Random


def nonempty_subsets(block_size: int) -> list[int]:
    masks: list[int] = []
    for mask in range(1, 1 << block_size):
        masks.append(mask)
    return masks


def all_cylinders(block_sizes: tuple[int, ...]) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    cylinders: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    indices = range(len(block_sizes))
    for width in range(1, len(block_sizes) + 1):
        for support in combinations(indices, width):
            mask_lists = [nonempty_subsets(block_sizes[i]) for i in support]
            for masks in product(*mask_lists):
                cylinders.append((support, masks))
    return cylinders


def mass(cylinder: tuple[tuple[int, ...], tuple[int, ...]], block_sizes: tuple[int, ...]) -> float:
    support, masks = cylinder
    value = 1.0
    for i, mask in zip(support, masks):
        value *= mask.bit_count() / block_sizes[i]
    return value


def catches(
    cylinder: tuple[tuple[int, ...], tuple[int, ...]],
    selector: tuple[int, ...],
) -> bool:
    support, masks = cylinder
    return all((masks[pos] >> selector[i]) & 1 for pos, i in enumerate(support))


def covers_product(
    family: list[tuple[tuple[int, ...], tuple[int, ...]]],
    block_sizes: tuple[int, ...],
) -> bool:
    for selector in product(*(range(size) for size in block_sizes)):
        if not any(catches(cylinder, selector) for cylinder in family):
            return False
    return True


def check_family(
    family: list[tuple[tuple[int, ...], tuple[int, ...]]],
    block_sizes: tuple[int, ...],
) -> None:
    total_mass = sum(mass(cylinder, block_sizes) for cylinder in family)
    if covers_product(family, block_sizes):
        assert total_mass >= 1.0 - 1e-12, (block_sizes, total_mass, family)
    if total_mass < 1.0 - 1e-12:
        assert not covers_product(family, block_sizes), (block_sizes, total_mass, family)


def exhaustive_binary_two_blocks() -> int:
    block_sizes = (2, 2)
    cylinders = all_cylinders(block_sizes)
    checked = 0
    for mask in range(1 << len(cylinders)):
        family = [cylinders[i] for i in range(len(cylinders)) if (mask >> i) & 1]
        check_family(family, block_sizes)
        checked += 1
    return checked


def sampled_checks() -> int:
    rng = Random(881)
    checked = 0
    for block_sizes in [(2, 2, 2), (2, 3, 2), (3, 3, 2), (3, 3, 3)]:
        cylinders = all_cylinders(block_sizes)
        for _ in range(2000):
            family = [c for c in cylinders if rng.random() < 0.12]
            check_family(family, block_sizes)
            checked += 1
    return checked


def main() -> None:
    exhaustive = exhaustive_binary_two_blocks()
    sampled = sampled_checks()
    print("selector cylinder mass checks passed")
    print(f"exhaustive_families={exhaustive}")
    print(f"sampled_families={sampled}")


if __name__ == "__main__":
    main()
