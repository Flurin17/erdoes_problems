#!/usr/bin/env python3
"""Evaluate the bridge-cover Sidon pressure from Corollary 16.28."""

from __future__ import annotations

import argparse
from fractions import Fraction


def pressure_lhs(interval_length: int, translate_size: int) -> Fraction:
    R = interval_length
    H = translate_size
    return Fraction(3 * R * R, 8 * H * H) - Fraction(R, 4 * H)


def pressure_report(R: int, H: int, delta: int) -> dict[str, object]:
    lhs = pressure_lhs(R, H)
    rhs = 2 * delta + 1
    return {
        "interval_length": R,
        "translate_size": H,
        "diameter_bound": delta,
        "lhs": f"{lhs.numerator}/{lhs.denominator}",
        "lhs_float": float(lhs),
        "rhs": rhs,
        "half_packet_impossible": lhs > rhs,
    }


def interval_marker_report(L: int, x: int) -> dict[str, object]:
    # D_L=[2,3L] union {4L}, so |D_L|=3L.  A bridge block inside
    # [x,2x-2] has diameter at most x-2, and J=[x+3L+1,2x].
    return {
        "model": "interval_marker",
        "L": L,
        "x": x,
        **pressure_report(R=x - 3 * L, H=3 * L, delta=x - 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--L", type=int, default=4)
    parser.add_argument(
        "--x",
        type=int,
        nargs="*",
        default=None,
        help="Smallest new marker values to test.",
    )
    args = parser.parse_args()

    xs = args.x or [4 * args.L + 3, 50, 100 * args.L * args.L]
    for x in xs:
        print(interval_marker_report(args.L, x))


if __name__ == "__main__":
    main()
