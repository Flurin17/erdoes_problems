#!/usr/bin/env python3
"""Type-count verifier for the parity-cross pair construction."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Counts:
    x0: int
    x1: int
    xe: int
    xo: int
    ye: int
    yo: int
    z: int

    @property
    def a_total(self) -> int:
        return self.x0 + self.x1 + self.xe + self.xo

    @property
    def b_total(self) -> int:
        return self.ye + self.yo + self.z

    @property
    def total(self) -> int:
        return self.a_total + self.b_total


def capacities(h: int) -> tuple[int, int, int, int]:
    """Return capacities for A-even-isolates, A-odd-isolates, B-even-core, B-odd-core."""
    a_even_iso = len([i for i in range(2, h) if i % 2 == 0])
    a_odd_iso = len([i for i in range(2, h) if i % 2 == 1])
    b_even_core = len([j for j in range(0, h - 1) if j % 2 == 0])
    b_odd_core = len([j for j in range(0, h - 1) if j % 2 == 1])
    return a_even_iso, a_odd_iso, b_even_core, b_odd_core


def degrees(h: int, c: Counts) -> list[tuple[str, int]]:
    z_even = (h - 1) % 2 == 0
    z_odd = not z_even
    a_even = c.x0 + c.xe
    a_odd = c.x1 + c.xo
    b_core = c.ye + c.yo
    out: list[tuple[str, int]] = []
    if c.x0:
        out.append(("x0", c.x1 + c.ye + (c.z if z_even else 0)))
    if c.x1:
        out.append(("x1", c.x0 + c.yo + (c.z if z_odd else 0)))
    if c.xe:
        out.append(("xe", c.ye + (c.z if z_even else 0)))
    if c.xo:
        out.append(("xo", c.yo + (c.z if z_odd else 0)))
    if c.ye:
        out.append(("ye", b_core - 1 + a_even))
    if c.yo:
        out.append(("yo", b_core - 1 + a_odd))
    if c.z:
        out.append(("z", a_even if z_even else a_odd))
    return out


def is_regular_with_degree(h: int, c: Counts, target: int | None = None) -> bool:
    values = degrees(h, c)
    if not values:
        return False
    degree_set = {value for _name, value in values}
    if len(degree_set) != 1:
        return False
    if target is not None and next(iter(degree_set)) != target:
        return False
    return True


def all_counts(h: int):
    ae_cap, ao_cap, be_cap, bo_cap = capacities(h)
    for x0 in (0, 1):
        for x1 in (0, 1):
            for xe in range(ae_cap + 1):
                for xo in range(ao_cap + 1):
                    for ye in range(be_cap + 1):
                        for yo in range(bo_cap + 1):
                            for z in (0, 1):
                                yield Counts(x0, x1, xe, xo, ye, yo, z)


def find_large_regular(h: int) -> Counts | None:
    for c in all_counts(h):
        if c.total >= h and is_regular_with_degree(h, c):
            return c
    return None


def find_balanced_plus(h: int) -> Counts | None:
    r = (h - 1) // 2
    for c in all_counts(h):
        if c.a_total == r and c.b_total == r and is_regular_with_degree(h, c, r):
            return c
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-h", type=int, default=30)
    parser.add_argument("--min-h", type=int, default=3)
    args = parser.parse_args()

    print("h large_regular balanced_plus obstruction large_counts balanced_counts")
    for h in range(args.min_h, args.max_h + 1):
        large = find_large_regular(h)
        balanced = find_balanced_plus(h)
        print(
            h,
            large is not None,
            balanced is not None,
            large is None and balanced is None,
            large if large is not None else "-",
            balanced if balanced is not None else "-",
        )


if __name__ == "__main__":
    main()
