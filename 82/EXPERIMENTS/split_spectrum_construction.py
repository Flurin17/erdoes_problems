#!/usr/bin/env python3
"""Verify the split-graph spectrum separation construction."""

from __future__ import annotations

import argparse
def split_spectrum(clique_size: int, independent_size: int) -> set[tuple[int, int]]:
    spectrum = {(order, 0) for order in range(1, independent_size + 2)}
    for order in range(2, clique_size + 1):
        spectrum.add((order, order - 1))
    return spectrum


def max_same_degree_total(
    spectrum1: set[tuple[int, int]],
    spectrum2: set[tuple[int, int]],
) -> int:
    best1: dict[int, int] = {}
    best2: dict[int, int] = {}
    for order, degree in spectrum1:
        best1[degree] = max(best1.get(degree, 0), order)
    for order, degree in spectrum2:
        best2[degree] = max(best2.get(degree, 0), order)
    return max((best1[d] + best2[d] for d in best1.keys() & best2.keys()), default=0)


def parameters(h: int) -> tuple[int, int, int, int, int]:
    r = (h - 1) // 2
    a1 = r
    a2 = h - 1
    m = (h - 3 + a1 + a2) // 2
    b1 = m - a1
    b2 = m - a2
    if b1 < 0 or b2 < 0:
        raise ValueError(f"negative independent side for h={h}")
    return m, a1, b1, a2, b2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-h", type=int, default=5)
    parser.add_argument("--max-h", type=int, default=40)
    args = parser.parse_args()

    print("h M a1 b1 a2 b2 obstruction max_same_degree_total")
    for h in range(args.min_h, args.max_h + 1):
        m, a1, b1, a2, b2 = parameters(h)
        assert a1 + b1 == m and a2 + b2 == m
        spectrum1 = split_spectrum(a1, b1)
        spectrum2 = split_spectrum(a2, b2)
        value = max_same_degree_total(spectrum1, spectrum2)
        obstruction = value < h and max(order for order, _degree in spectrum1 | spectrum2) < h
        print(h, m, a1, b1, a2, b2, obstruction, value)
        if not obstruction:
            raise AssertionError((h, m, a1, b1, a2, b2, value))


if __name__ == "__main__":
    main()
