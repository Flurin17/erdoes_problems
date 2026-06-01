#!/usr/bin/env python3
"""Finite check for the single-core endpoint normal form.

For a finite packet P and interval cores C_i, if the common intersection of
the C_i misses P, then some C_i misses min(P) or max(P).  The script
exhausts small universes and core families.
"""

from __future__ import annotations

from itertools import combinations
from math import ceil
from random import Random


def intervals(n: int) -> list[tuple[int, int]]:
    return [(a, b) for a in range(n) for b in range(a, n)]


def contains(interval: tuple[int, int], x: int) -> bool:
    a, b = interval
    return a <= x <= b


def packet_missed(packet: tuple[int, ...], cores: tuple[tuple[int, int], ...]) -> bool:
    return not any(all(contains(core, x) for core in cores) for x in packet)


def endpoint_escaped(packet: tuple[int, ...], cores: tuple[tuple[int, int], ...]) -> bool:
    lo, hi = packet[0], packet[-1]
    return any(not contains(core, lo) or not contains(core, hi) for core in cores)


def in_union(cores: tuple[tuple[int, int], ...], x: int) -> bool:
    return any(contains(core, x) for core in cores)


def union_gap_alternative(packet: tuple[int, ...], cores: tuple[tuple[int, int], ...]) -> bool:
    lo, hi = packet[0], packet[-1]
    if not in_union(cores, lo) or not in_union(cores, hi):
        return True
    return any(lo < x < hi and not in_union(cores, x) for x in packet)


def merged_components(cores: tuple[tuple[int, int], ...]) -> list[tuple[int, int]]:
    merged: list[tuple[int, int]] = []
    for a, b in sorted(cores):
        if not merged or a > merged[-1][1] + 1:
            merged.append((a, b))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
    return merged


def internal_gap_packet_counts(
    packet: tuple[int, ...],
    cores: tuple[tuple[int, int], ...],
) -> list[int]:
    components = merged_components(cores)
    counts: list[int] = []
    for (_, left_end), (right_start, _) in zip(components, components[1:]):
        counts.append(sum(left_end < x < right_start for x in packet))
    return counts


def main() -> None:
    rng = Random(881)
    checked = 0
    union_checked = 0
    gap_count_checked = 0
    for n in range(2, 8):
        all_intervals = intervals(n)
        universe = tuple(range(n))
        for packet_size in range(1, n + 1):
            for packet in combinations(universe, packet_size):
                for core_count in range(1, 5):
                    for cores in combinations(all_intervals, core_count):
                        if packet_missed(packet, cores):
                            assert endpoint_escaped(packet, cores), (n, packet, cores)
                        checked += 1
                        if not all(in_union(cores, x) for x in packet):
                            assert union_gap_alternative(packet, cores), (n, packet, cores)
                        union_checked += 1
                        if in_union(cores, packet[0]) and in_union(cores, packet[-1]):
                            missing = sum(not in_union(cores, x) for x in packet)
                            if missing:
                                counts = internal_gap_packet_counts(packet, cores)
                                assert len(counts) <= core_count - 1, (n, packet, cores, counts)
                                assert sum(counts) == missing, (n, packet, cores, counts)
                                assert max(counts) >= ceil(missing / (core_count - 1)), (
                                    n,
                                    packet,
                                    cores,
                                    counts,
                                )
                            gap_count_checked += 1
    for n in (8, 9, 10):
        all_intervals = intervals(n)
        universe = tuple(range(n))
        for _ in range(5000):
            packet_size = rng.randint(1, n)
            packet = tuple(sorted(rng.sample(universe, packet_size)))
            core_count = rng.randint(1, 5)
            cores = tuple(rng.choice(all_intervals) for _ in range(core_count))
            if packet_missed(packet, cores):
                assert endpoint_escaped(packet, cores), (n, packet, cores)
            checked += 1
            if not all(in_union(cores, x) for x in packet):
                assert union_gap_alternative(packet, cores), (n, packet, cores)
            union_checked += 1
            if in_union(cores, packet[0]) and in_union(cores, packet[-1]):
                missing = sum(not in_union(cores, x) for x in packet)
                if missing:
                    counts = internal_gap_packet_counts(packet, cores)
                    assert len(counts) <= core_count - 1, (n, packet, cores, counts)
                    assert sum(counts) == missing, (n, packet, cores, counts)
                    assert max(counts) >= ceil(missing / (core_count - 1)), (
                        n,
                        packet,
                        cores,
                        counts,
                    )
                gap_count_checked += 1
    print("interval core endpoint check passed")
    print(f"total_checked={checked}")
    print(f"union_gap_checked={union_checked}")
    print(f"gap_count_checked={gap_count_checked}")


if __name__ == "__main__":
    main()
