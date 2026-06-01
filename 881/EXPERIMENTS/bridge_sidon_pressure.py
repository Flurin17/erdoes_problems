#!/usr/bin/env python3
"""Evaluate the bridge-cover Sidon pressure from Corollary 16.28."""

from __future__ import annotations

import argparse
from fractions import Fraction


def pressure_lhs(interval_length: int, translate_size: int) -> Fraction:
    R = interval_length
    H = translate_size
    return Fraction(3 * R * R, 8 * H * H) - Fraction(R, 4 * H)


def staggered_lhs(
    interval_length: int,
    translate_size: int,
    windows: int,
    beta: Fraction,
) -> Fraction:
    R = interval_length
    H = translate_size
    gamma = beta / windows
    coefficient = gamma - gamma * gamma / 2
    return coefficient * R * R / (H * H) - Fraction(R, 2 * H)


def pressure_report(
    R: int,
    H: int,
    delta: int,
    windows: tuple[int, ...],
    beta: Fraction,
) -> dict[str, object]:
    lhs = pressure_lhs(R, H)
    rhs = 2 * delta + 1
    staggered = {}
    for count in windows:
        gamma = beta / count
        coefficient = gamma - gamma * gamma / 2
        monotone_threshold = Fraction(1, 4) / coefficient
        staggered_value = staggered_lhs(R, H, count, beta)
        condition_met = Fraction(R, H) >= monotone_threshold
        staggered[count] = {
            "beta": f"{beta.numerator}/{beta.denominator}",
            "gamma": f"{gamma.numerator}/{gamma.denominator}",
            "monotone_threshold": (
                f"{monotone_threshold.numerator}/{monotone_threshold.denominator}"
            ),
            "condition_met": condition_met,
            "lhs": f"{staggered_value.numerator}/{staggered_value.denominator}",
            "lhs_float": float(staggered_value),
            "impossible_if_applicable": condition_met and staggered_value > rhs,
        }
    return {
        "interval_length": R,
        "translate_size": H,
        "diameter_bound": delta,
        "lhs": f"{lhs.numerator}/{lhs.denominator}",
        "lhs_float": float(lhs),
        "rhs": rhs,
        "half_packet_impossible": lhs > rhs,
        "bounded_staggered": staggered,
    }


def interval_marker_report(
    L: int,
    x: int,
    windows: tuple[int, ...],
    beta: Fraction,
) -> dict[str, object]:
    # D_L=[2,3L] union {4L}, so |D_L|=3L.  A bridge block inside
    # [x,2x-2] has diameter at most x-2, and J=[x+3L+1,2x].
    return {
        "model": "interval_marker",
        "L": L,
        "x": x,
        **pressure_report(R=x - 3 * L, H=3 * L, delta=x - 2, windows=windows, beta=beta),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--L", type=int, default=4)
    parser.add_argument("--windows", type=int, nargs="*", default=[1, 2, 4])
    parser.add_argument("--beta-num", type=int, default=1)
    parser.add_argument("--beta-den", type=int, default=1)
    parser.add_argument(
        "--x",
        type=int,
        nargs="*",
        default=None,
        help="Smallest new marker values to test.",
    )
    args = parser.parse_args()

    beta = Fraction(args.beta_num, args.beta_den)
    windows = tuple(args.windows)
    xs = args.x or [4 * args.L + 3, 50, 100 * args.L * args.L]
    for x in xs:
        print(interval_marker_report(args.L, x, windows=windows, beta=beta))


if __name__ == "__main__":
    main()
