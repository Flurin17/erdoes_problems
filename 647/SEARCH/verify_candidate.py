#!/usr/bin/env python3
"""Independent verifier for a proposed Erdos #647 candidate.

This deliberately does not call the C++ search code. It uses Python integer
arithmetic, deterministic Miller-Rabin for 64-bit integers, Pollard-Rho
factorization, and a recursive highly-composite search for max tau below n.
"""

from __future__ import annotations

import argparse
import math
import random
from collections import Counter


MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
HC_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in MR_BASES:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in MR_BASES:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard(n: int) -> int:
    if n % 2 == 0:
        return 2
    rng = random.Random(n ^ 0x647647)
    while True:
        c = rng.randrange(1, n)
        x = rng.randrange(0, n)
        y = x
        d = 1
        for _ in range(50_000):
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
            if d != 1:
                break
        if 1 < d < n:
            return d


def factor(n: int, out: list[int]) -> None:
    if n == 1:
        return
    if is_prime(n):
        out.append(n)
        return
    d = pollard(n)
    factor(d, out)
    factor(n // d, out)


def tau(n: int) -> int:
    ans = 1
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
        if p * p > n:
            break
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            ans *= e + 1
    if n > 1:
        parts: list[int] = []
        factor(n, parts)
        for e in Counter(parts).values():
            ans *= e + 1
    return ans


def max_tau_leq(limit: int) -> tuple[int, int]:
    best_tau = 1
    best_arg = 1

    def dfs(idx: int, max_exp: int, cur: int, divs: int) -> None:
        nonlocal best_tau, best_arg
        if divs > best_tau or (divs == best_tau and cur < best_arg):
            best_tau = divs
            best_arg = cur
        if idx >= len(HC_PRIMES):
            return
        p = HC_PRIMES[idx]
        x = cur
        for e in range(1, max_exp + 1):
            x *= p
            if x > limit:
                break
            dfs(idx + 1, e, x, divs * (e + 1))

    dfs(0, 64, 1, 1)
    return best_tau, best_arg


def verify(n: int, shift_limit: int | None) -> bool:
    if shift_limit is None:
        mt, arg = max_tau_leq(n - 1)
        shift_limit = mt - 2
        print(f"max_tau_leq({n - 1}) = {mt} at {arg}; checking k <= {shift_limit}")
    best = (0, None, None)
    for k in range(1, shift_limit + 1):
        t = tau(n - k)
        if t > best[0]:
            best = (t, k, n - k)
        if t > k + 2:
            print(f"FAIL n={n} k={k} m={n-k} tau={t} bound={k+2}")
            return False
    print(f"PASS n={n} checked_k={shift_limit} max_seen_tau={best[0]} at k={best[1]} m={best[2]}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("--shift-limit", type=int)
    args = ap.parse_args()
    return 0 if verify(args.n, args.shift_limit) else 1


if __name__ == "__main__":
    raise SystemExit(main())
