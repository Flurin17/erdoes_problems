#!/usr/bin/env python3
"""Lift the Erdos 647 residue filter through more primes.

The base filter is the 41-class reduction modulo 11*13*17*19.  A candidate
`n=2520N` that satisfies the problem inequality must also satisfy every
finite forced-divisor obstruction tested here.  This script lifts each
surviving residue `r mod M` to `r + aM mod Mp` and keeps only residues that
survive the same forced-smooth criterion.
"""

from __future__ import annotations

import argparse
from functools import lru_cache


BASE_RESIDUES = (
    0,
    858,
    1287,
    1716,
    2431,
    2574,
    4862,
    5291,
    6149,
    8151,
    9009,
    9867,
    10582,
    12155,
    12584,
    13013,
    13442,
    16302,
    17017,
    17160,
    18733,
    19877,
    20306,
    20735,
    21164,
    24310,
    24453,
    25168,
    27170,
    28028,
    28457,
    29315,
    29601,
    31603,
    32032,
    32461,
    35321,
    36608,
    37752,
    38896,
    44187,
)
BASE_PRIMES = (11, 13, 17, 19)
SMALL_PRIMES = (2, 3, 5, 7)
SMALL_EXPONENT_CAPS = (3, 2, 1, 1)


def parse_primes(text: str) -> list[int]:
    if not text:
        return []
    return [int(part.strip()) for part in text.split(",") if part.strip()]


def max_forced_smooth(exponents: tuple[int, ...], bound: int, primes: tuple[int, ...]) -> int:
    indexes = [index for index, exponent in enumerate(exponents) if exponent]
    if not indexes:
        return 1

    forced = 1
    divisors = 1
    for index, exponent in enumerate(exponents):
        if exponent:
            forced *= primes[index] ** exponent
            divisors *= exponent + 1

    best = 0

    def search(position: int, value: int, tau_value: int) -> None:
        nonlocal best
        if position == len(indexes):
            best = max(best, value)
            return

        index = indexes[position]
        prime = primes[index]
        base_exponent = exponents[index]
        current = value
        exponent = base_exponent
        while True:
            next_tau = tau_value // (base_exponent + 1) * (exponent + 1)
            if next_tau > bound:
                break
            search(position + 1, current, next_tau)
            current *= prime
            exponent += 1

    search(0, forced, divisors)
    return best


def lift_residues(k_limit: int, extra_primes: list[int]) -> tuple[int, list[int]]:
    modulus = 1
    for prime in BASE_PRIMES:
        modulus *= prime
    residues = list(BASE_RESIDUES)
    current_extra: list[int] = list(BASE_PRIMES)

    for prime in extra_primes:
        new_modulus = modulus * prime
        current_extra.append(prime)
        primes = SMALL_PRIMES + tuple(current_extra)
        exponent_caps = SMALL_EXPONENT_CAPS + (1,) * len(current_extra)

        @lru_cache(maxsize=None)
        def cached_max_smooth(exponents: tuple[int, ...], bound: int) -> int:
            return max_forced_smooth(exponents, bound, primes)

        def residue_ok(residue: int) -> bool:
            q_modulus = 2520 * new_modulus
            for k in range(1, k_limit + 1):
                value = (2520 * residue - k) % q_modulus
                if value == 0:
                    value = q_modulus
                forced_tau = 1
                exponents = []
                remaining = value
                for forced_prime, cap in zip(primes, exponent_caps):
                    exponent = 0
                    while exponent < cap and remaining % forced_prime == 0:
                        remaining //= forced_prime
                        exponent += 1
                    exponents.append(exponent)
                    forced_tau *= exponent + 1

                bound = k + 2
                if forced_tau > bound:
                    return False
                if 2 * forced_tau > bound:
                    smooth_limit = cached_max_smooth(tuple(exponents), bound)
                    if value > smooth_limit:
                        return False
            return True

        lifted: list[int] = []
        for residue in residues:
            for digit in range(prime):
                candidate = residue + modulus * digit
                if residue_ok(candidate):
                    lifted.append(candidate)
        modulus = new_modulus
        residues = lifted
        print(
            f"LIFT prime={prime} modulus={modulus} count={len(residues)} "
            f"density={len(residues) / modulus:.12g}"
        )

    return modulus, residues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=200)
    parser.add_argument("--add-primes", default="23")
    parser.add_argument("--format", choices=("lines", "csv"), default="lines")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    modulus, residues = lift_residues(args.k, parse_primes(args.add_primes))
    print(f"RESULT modulus={modulus} count={len(residues)}")
    if args.format == "csv":
        print(",".join(str(residue) for residue in residues))
    else:
        for residue in residues:
            print(residue)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
