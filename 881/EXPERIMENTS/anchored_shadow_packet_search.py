#!/usr/bin/env python3
"""Search finite order-3 windows for sparse anchored-shadow packets.

This is a diagnostic for Corollaries 3.4d.19--3.4d.20.  It shows that
local finite three-sum coverage does not by itself force anchored-shadow
expansion, and that the parallel-copy branch is locally compatible with
finite coverage.  The default run checks the scalable thickened templates
from Warnings 3.4d.21--3.4d.22 and then rediscovers their base windows.
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


def scaled(base: tuple[int, ...], factor: int) -> tuple[int, ...]:
    return tuple(factor * value for value in base)


def thickened(base: tuple[int, ...], factor: int) -> tuple[int, ...]:
    return tuple(
        value
        for base_value in base
        for value in range(factor * base_value, factor * base_value + factor)
    )


def check_thickened_templates(max_factor: int = 7) -> None:
    anchored_base = (1, 2, 3, 4, 7)
    anchored_packet = (1, 3, 4, 7)
    anchored_shadows = [
        (2, 4),
        (2, 3),
        (1, 2),
        (2,),
    ]

    parallel_base = (1, 2, 3, 4, 5, 7)
    parallel_u = (1, 3, 5)
    parallel_v = (3, 5, 7)
    palette = (2, 4)

    for factor in range(1, max_factor + 1):
        values = thickened(anchored_base, factor)
        value_set = set(values)
        gate = 2 * factor
        packet = scaled(anchored_packet, factor)
        assert covers_window(values, 8 * factor, 16 * factor)
        shadows = [
            tuple(sorted({gate + u - anchor for u in packet} & value_set))
            for anchor in packet
        ]
        assert shadows == [scaled(shadow, factor) for shadow in anchored_shadows]

        values = thickened(parallel_base, factor)
        value_set = set(values)
        f = 2 * factor
        g = 4 * factor
        packet_u = scaled(parallel_u, factor)
        packet_v = scaled(parallel_v, factor)
        assert covers_window(values, 8 * factor, 16 * factor)
        assert packet_v == tuple(u + g - f for u in packet_u)
        trapped = scaled(palette, factor)
        assert (
            tuple(
                sorted(
                    {u + g - anchor for u in packet_u for anchor in packet_u}
                    & value_set
                )
            )
            == trapped
        )
        assert (
            tuple(
                sorted(
                    {v + f - anchor for v in packet_v for anchor in packet_v}
                    & value_set
                )
            )
            == trapped
        )
        assert (
            tuple(sorted({v + f - u for v in packet_v for u in packet_u} & value_set))
            == trapped
        )
        assert (
            tuple(sorted({u + g - v for u in packet_u for v in packet_v} & value_set))
            == trapped
        )

    print(f"thickened templates verified through p={max_factor}")


def find_anchored_shadow_packet() -> None:
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


def find_parallel_copy_packet() -> None:
    for end_base in range(8, 26):
        window = (end_base, 2 * end_base)
        values_range = range(1, end_base + 1)
        for size in range(6, min(end_base, 11) + 1):
            for values in combinations(values_range, size):
                value_set = set(values)
                if not covers_window(values, *window):
                    continue
                for f, g in combinations(values, 2):
                    for first, second in ((f, g), (g, f)):
                        shift = second - first
                        candidates = tuple(
                            u
                            for u in values
                            if u not in (first, second)
                            and u + shift in value_set
                            and u + shift not in (first, second)
                        )
                        for packet_size in range(3, min(6, len(candidates)) + 1):
                            for packet in combinations(candidates, packet_size):
                                shadow = {
                                    second + u - anchor
                                    for u in packet
                                    for anchor in packet
                                } & value_set
                                if len(shadow) <= 2:
                                    print("parallel copy packet found")
                                    print(f"A={values}")
                                    print(f"window={window}")
                                    print(f"f={first}")
                                    print(f"g={second}")
                                    print(f"U={packet}")
                                    print(f"V={tuple(u + shift for u in packet)}")
                                    print(f"shadow={tuple(sorted(shadow))}")
                                    return
    raise SystemExit("no parallel packet found in default bounds")


def main() -> None:
    check_thickened_templates()
    find_anchored_shadow_packet()
    find_parallel_copy_packet()


if __name__ == "__main__":
    main()
