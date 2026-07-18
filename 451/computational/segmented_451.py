#!/usr/bin/env python3
"""Independent segmented forbidden-block solver for Erdős problem 451."""

import argparse

from compute_451 import primes_below


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def solve(k: int, block_size: int = 65536) -> int:
    ps = [p for p in primes_below(2 * k) if p > k]
    low = 2 * k + 1
    while True:
        high = low + block_size - 1
        marked = bytearray(block_size)
        for p in ps:
            first_q = max(1, ceil_div(low - k, p))
            last_q = (high - 1) // p
            for q in range(first_q, last_q + 1):
                start = max(low, q * p + 1)
                end = min(high, q * p + k)
                if start <= end:
                    marked[start - low : end - low + 1] = b"\x01" * (end - start + 1)
        try:
            return low + marked.index(0)
        except ValueError:
            low = high + 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_k", type=int)
    parser.add_argument("--block-size", type=int, default=65536)
    args = parser.parse_args()
    if args.max_k < 1 or args.block_size < 1:
        raise SystemExit("arguments must be positive")
    print("k\tn_k")
    for k in range(1, args.max_k + 1):
        print(f"{k}\t{solve(k, args.block_size)}")


if __name__ == "__main__":
    main()
