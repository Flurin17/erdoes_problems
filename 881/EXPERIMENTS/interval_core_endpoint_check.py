#!/usr/bin/env python3
"""Finite check for the single-core endpoint normal form.

For a finite packet P and interval cores C_i, if the common intersection of
the C_i misses P, then some C_i misses min(P) or max(P).  The script
exhausts small universes and core families.
"""

from __future__ import annotations

from itertools import combinations


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


def main() -> None:
    checked = 0
    union_checked = 0
    for n in range(2, 9):
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
    print("interval core endpoint check passed")
    print(f"total_checked={checked}")
    print(f"union_gap_checked={union_checked}")


if __name__ == "__main__":
    main()
