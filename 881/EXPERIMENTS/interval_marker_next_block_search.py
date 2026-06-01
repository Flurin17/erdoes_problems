#!/usr/bin/env python3
"""Search strict singleton continuations of the interval-marker seed.

The seed is A=[1,L] union {2L}, with previous endpoint 4L+2.  The search
adds one finite block P above that endpoint and asks whether every new
element q in P has a strict singleton order-4 witness below the new
declared endpoint.

This is a bounded finite diagnostic only.
"""

from __future__ import annotations

import argparse
from itertools import combinations


def hsum_bits(elements: set[int], order: int, cap: int) -> int:
    bits = 1
    mask = (1 << (cap + 1)) - 1
    ordered = tuple(sorted(elements))
    for _ in range(order):
        out = 0
        for element in ordered:
            out |= (bits << element) & mask
        bits = out
    return bits


def contains(bits: int, value: int) -> bool:
    return value >= 0 and bool((bits >> value) & 1)


def cover_end(bits: int, start: int, cap: int) -> int:
    value = start
    while value <= cap and contains(bits, value):
        value += 1
    return value - 1


def strict_witnesses(
    elements: set[int],
    target: int,
    previous_endpoint: int,
    declared: int,
    four_all: int,
    cap: int,
) -> list[int]:
    without = hsum_bits(elements - {target}, 4, cap)
    largest = max(elements)
    smallest = min(elements)
    return [
        witness
        for witness in range(previous_endpoint + 1, declared + 1)
        if contains(four_all, witness)
        and not contains(without, witness)
        and witness - target - 2 * smallest >= largest
    ]


def search(L: int, max_size: int, max_candidate: int, cap: int) -> None:
    old = set(range(1, L + 1)) | {2 * L}
    previous_endpoint = 4 * L + 2
    candidates = [value for value in range(previous_endpoint + 1, max_candidate + 1)]
    checked_by_size: dict[int, int] = {}
    eligible_by_size: dict[int, int] = {}

    for size in range(1, max_size + 1):
        checked = 0
        eligible = 0
        for block in combinations(candidates, size):
            checked += 1
            elements = old | set(block)
            three = hsum_bits(elements, 3, cap)
            coverage_end = cover_end(three, 3, cap)
            declared = coverage_end - 2 * min(elements)
            if declared < max(previous_endpoint + 1, max(block)):
                continue

            eligible += 1
            four_all = hsum_bits(elements, 4, cap)
            witnesses: dict[int, list[int]] = {}
            for target in block:
                found = strict_witnesses(
                    elements,
                    target,
                    previous_endpoint,
                    declared,
                    four_all,
                    cap,
                )
                if not found:
                    break
                witnesses[target] = found[:3]
            else:
                print("interval-marker continuation found")
                print(f"L={L}")
                print(f"old={sorted(old)}")
                print(f"block={block}")
                print(f"coverage_end={coverage_end}")
                print(f"declared={declared}")
                print(f"witnesses={witnesses}")
                return

        checked_by_size[size] = checked
        eligible_by_size[size] = eligible

    print("no interval-marker continuation found")
    print(f"L={L}")
    print(f"max_size={max_size}")
    print(f"max_candidate={max_candidate}")
    print(f"checked_by_size={checked_by_size}")
    print(f"eligible_by_size={eligible_by_size}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--L", type=int, default=4)
    parser.add_argument("--max-size", type=int, default=5)
    parser.add_argument("--max-candidate", type=int, default=55)
    parser.add_argument("--cap", type=int, default=180)
    args = parser.parse_args()
    search(args.L, args.max_size, args.max_candidate, args.cap)


if __name__ == "__main__":
    main()
