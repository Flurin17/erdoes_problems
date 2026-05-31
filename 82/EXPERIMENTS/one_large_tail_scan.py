#!/usr/bin/env python3
"""Check full-bin covers for vectors with one distinguished largest class.

The scan enumerates vectors `(x, tail)` with `sum(tail) <= factor*q`,
`x >= max(tail)`, and total at most `q^2`, then calls the exact full-bin
checker.  This is intended to test possible extensions of the one-large-class
repair lemma.
"""

from __future__ import annotations

import argparse

from full_bin_cover import find_cover
from rectangle_cover import integer_partitions


def scan(q: int, factor: int) -> tuple[int, tuple[int, int, tuple[int, ...]] | None]:
    checked = 0
    for tail_total in range(factor * q + 1):
        for tail in integer_partitions(tail_total):
            min_x = tail[0] if tail else 0
            for x in range(min_x, q * q - tail_total + 1):
                checked += 1
                if find_cover((x,) + tail, q, q) is None:
                    return checked, (tail_total, x, tail)
    return checked, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-min", type=int, default=3)
    parser.add_argument("--q-max", type=int, required=True)
    parser.add_argument("--factor", type=int, default=3)
    args = parser.parse_args()

    for q in range(args.q_min, args.q_max + 1):
        checked, bad = scan(q, args.factor)
        print(f"q={q}")
        print(f"factor={args.factor}")
        print(f"checked={checked}")
        if bad is None:
            print("counterexample=none")
        else:
            tail_total, x, tail = bad
            print(f"tail_total={tail_total}")
            print(f"x={x}")
            print("tail=" + ",".join(map(str, tail)))
            print("counterexample=found")
            return


if __name__ == "__main__":
    main()
