#!/usr/bin/env python3
"""Standalone window verifier for Erdos problem 647.

Checks whether tau(n-k) <= k+2 over a finite window.  With no explicit
--shift-limit, the script computes B = max_{m < n} tau(m) by enumerating
highly-composite exponent vectors, then checks the sufficient window
1 <= k <= B-2.
"""

from __future__ import annotations

import argparse
import math
import random
import sys
from collections import Counter
from pathlib import Path


MILLER_RABIN_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
SMALL_PRIMES = (
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
)


def is_prime(n: int) -> bool:
    """Return True if n passes deterministic Miller-Rabin for this range."""
    if n < 2:
        return False
    for p in SMALL_PRIMES:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    for a in MILLER_RABIN_BASES:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n: int) -> int:
    """Find a nontrivial factor of odd composite n."""
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    rng = random.Random(n ^ 0x647647647)
    while True:
        c = rng.randrange(1, n - 1)
        x = rng.randrange(2, n - 1)
        y = x
        d = 1
        for _ in range(100_000):
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
            if d != 1:
                break
        if 1 < d < n:
            return d


def factor_into(n: int, out: list[int]) -> None:
    if n == 1:
        return
    if is_prime(n):
        out.append(n)
        return
    d = pollard_rho(n)
    factor_into(d, out)
    factor_into(n // d, out)


def factor_counts(n: int) -> Counter[int]:
    if n < 1:
        raise ValueError(f"cannot factor nonpositive integer {n}")

    counts: Counter[int] = Counter()
    for p in SMALL_PRIMES:
        if p * p > n:
            break
        while n % p == 0:
            counts[p] += 1
            n //= p

    if n > 1:
        parts: list[int] = []
        factor_into(n, parts)
        counts.update(parts)
    return counts


def tau(n: int) -> int:
    result = 1
    for exponent in factor_counts(n).values():
        result *= exponent + 1
    return result


def next_prime_after(n: int, known_primes: list[int]) -> int:
    candidate = n + 1
    while True:
        for p in known_primes:
            if p * p > candidate:
                return candidate
            if candidate % p == 0:
                break
        else:
            return candidate
        candidate += 1


def highly_composite_primes(limit: int) -> list[int]:
    """Enough consecutive primes for exact max-tau enumeration up to limit."""
    primes: list[int] = []
    product = 1
    candidate = 1
    while True:
        candidate = next_prime_after(candidate, primes)
        if product * candidate > limit:
            return primes
        primes.append(candidate)
        product *= candidate


def max_tau_leq(limit: int) -> tuple[int, int]:
    if limit < 1:
        return 0, 0

    primes = highly_composite_primes(limit)
    best_tau = 1
    best_arg = 1

    def search(index: int, max_exp: int, value: int, divisors: int) -> None:
        nonlocal best_tau, best_arg
        if divisors > best_tau or (divisors == best_tau and value < best_arg):
            best_tau = divisors
            best_arg = value
        if index == len(primes):
            return

        p = primes[index]
        x = value
        for exp in range(1, max_exp + 1):
            if x > limit // p:
                break
            x *= p
            search(index + 1, exp, x, divisors * (exp + 1))

    search(0, limit.bit_length(), 1, 1)
    return best_tau, best_arg


def checked_limit_for(n: int, requested_shift_limit: int | None) -> tuple[int, str]:
    if n < 2:
        raise ValueError("n must be at least 2")
    if requested_shift_limit is not None:
        if requested_shift_limit < 0:
            raise ValueError("--shift-limit must be nonnegative")
        return min(requested_shift_limit, n - 1), "explicit"

    max_tau, arg = max_tau_leq(n - 1)
    checked = min(n - 1, max(0, max_tau - 2))
    print(f"BOUND n={n} max_tau={max_tau} arg={arg} checked_limit={checked}")
    return checked, "full"


def verify_one(n: int, requested_shift_limit: int | None) -> bool:
    checked_limit, _ = checked_limit_for(n, requested_shift_limit)

    max_seen_tau = 0
    max_seen_k = 0
    max_seen_m = 0
    for k in range(1, checked_limit + 1):
        m = n - k
        t = tau(m)
        if t > max_seen_tau:
            max_seen_tau = t
            max_seen_k = k
            max_seen_m = m
        bound = k + 2
        if t > bound:
            print(f"FAIL n={n} k={k} tau={t} bound={bound} m={m}")
            return False

    print(
        f"PASS n={n} checked_limit={checked_limit} "
        f"max_seen_tau={max_seen_tau} at_k={max_seen_k} m={max_seen_m}"
    )
    return True


def read_input_file(path: Path) -> list[int]:
    values: list[int] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, 1):
            line = raw_line.split("#", 1)[0].strip()
            if not line:
                continue
            try:
                values.append(int(line))
            except ValueError as exc:
                raise ValueError(f"{path}:{line_number}: expected one integer") from exc
    return values


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify tau(n-k) <= k+2 for one n or a file of n values."
    )
    parser.add_argument("n", nargs="?", type=int, help="single n to verify")
    parser.add_argument(
        "--input-file",
        type=Path,
        help="file containing one integer n per line",
    )
    parser.add_argument(
        "--shift-limit",
        type=int,
        help="maximum k to check; default computes the full highly-composite bound",
    )
    args = parser.parse_args()

    if (args.n is None) == (args.input_file is None):
        parser.error("provide exactly one of positional n or --input-file")
    return args


def main() -> int:
    args = parse_args()
    try:
        values = [args.n] if args.n is not None else read_input_file(args.input_file)
        all_ok = True
        for n in values:
            all_ok = verify_one(n, args.shift_limit) and all_ok
        return 0 if all_ok else 1
    except (OSError, ValueError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
