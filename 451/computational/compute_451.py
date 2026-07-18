#!/usr/bin/env python3
"""Exact modular-jump computation for Erdős problem 451."""

import argparse
import json
import math
import time
from pathlib import Path


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    if limit:
        sieve[0] = 0
    if limit > 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit - 1) + 1):
        if sieve[p]:
            sieve[p * p : limit : p] = b"\x00" * (
                (limit - 1 - p * p) // p + 1
            )
    return [p for p in range(2, limit) if sieve[p]]


def solve(k: int) -> tuple[int, list[dict[str, int]]]:
    ps = [p for p in primes_below(2 * k) if p > k]
    x = 2 * k + 1
    chain: list[dict[str, int]] = []
    while True:
        best = None
        for p in ps:
            r = x % p
            if 1 <= r <= k:
                q = (x - r) // p
                end = q * p + k
                if best is None or end > best[0] or (end == best[0] and p < best[1]):
                    best = (end, p, q)
        if best is None:
            assert all(x % p == 0 or x % p > k for p in ps)
            return x, chain
        end, p, q = best
        assert q * p + 1 <= x <= q * p + k == end
        chain.append({"start": x, "end": end, "p": p, "q": q})
        x = end + 1


def direct_scan(k: int, stop: int) -> int:
    """Independent candidate-by-candidate residue scan through stop."""
    ps = [p for p in primes_below(2 * k) if p > k]
    for n in range(2 * k + 1, stop + 1):
        if all(n % p == 0 or n % p > k for p in ps):
            return n
    raise AssertionError("no admissible candidate through certified stop")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_k", type=int)
    parser.add_argument("--certificates", type=Path)
    parser.add_argument("--cross-check", type=int, default=50)
    args = parser.parse_args()
    if args.max_k < 1:
        raise SystemExit("max_k must be positive")
    if args.certificates:
        args.certificates.mkdir(parents=True, exist_ok=True)

    started = time.monotonic()
    print("k\tn_k\tjump_blocks")
    for k in range(1, args.max_k + 1):
        n, chain = solve(k)
        if k <= args.cross_check:
            assert direct_scan(k, n) == n
        print(f"{k}\t{n}\t{len(chain)}")
        if args.certificates:
            payload = {"problem": 451, "k": k, "n": n, "chain": chain}
            path = args.certificates / f"k_{k:04d}.json"
            path.write_text(json.dumps(payload, separators=(",", ":")) + "\n")
    print(f"# elapsed_seconds={time.monotonic() - started:.6f}")


if __name__ == "__main__":
    main()
