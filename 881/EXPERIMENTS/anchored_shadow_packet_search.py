#!/usr/bin/env python3
"""Search finite order-3 windows for sparse anchored-shadow packets.

This is a diagnostic for Corollary 3.4d.19.  It shows that local finite
three-sum coverage does not by itself force anchored-shadow expansion.
The default search reproduces Warning 3.4d.20.
"""

from __future__ import annotations

from itertools import combinations


def hsum(values: tuple[int, ...], length: int, cap: int) -> set[int]:
    sums = {0}
    for _ in range(length):
        sums = {s + v for s in sums for v in values if s + v <= cap}
    return sums


def covers_window(values: tuple[int, ...], start: int, end: int) -> bool:
    sums = hsum(values, 3, end)
    return all(n in sums for n in range(start, end + 1))


def shadow_bound(values: tuple[int, ...], gate: int, packet: tuple[int, ...]) -> int:
    value_set = set(values)
    return max(
        len({gate + u - anchor for u in packet} & value_set)
        for anchor in packet
    )


def main() -> None:
    for end_base in range(8, 21):
        window = (end_base, 2 * end_base)
        values_range = range(1, end_base + 1)
        for size in range(5, min(end_base, 10) + 1):
            for values in combinations(values_range, size):
                if not covers_window(values, *window):
                    continue
                for gate in values:
                    rest = tuple(v for v in values if v != gate)
                    for packet_size in range(4, min(7, len(rest)) + 1):
                        for packet in combinations(rest, packet_size):
                            bound = shadow_bound(values, gate, packet)
                            if bound <= 2:
                                print("anchored shadow packet found")
                                print(f"A={values}")
                                print(f"window={window}")
                                print(f"g={gate}")
                                print(f"U={packet}")
                                print(f"shadow_bound={bound}")
                                return
    raise SystemExit("no packet found in default bounds")


if __name__ == "__main__":
    main()
