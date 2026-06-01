#!/usr/bin/env python3
"""Compare the trace Ramsey bounds from Lemmas 14B and 14B.1.

The script uses the Erdos-Szekeres estimate

    R(a,b) <= binom(a+b-2, a-1)

as a common upper-bound proxy, and reports base-2 logarithms of the resulting
trace-class sums.
"""

from __future__ import annotations

import argparse
import math


def log2_binom(n: int, k: int) -> float:
    if k < 0 or k > n:
        return float("-inf")
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)) / math.log(2)


def log2_add(values: list[float]) -> float:
    finite = [value for value in values if value != float("-inf")]
    if not finite:
        return float("-inf")
    m = max(finite)
    return m + math.log2(sum(2 ** (value - m) for value in finite))


def ramsey_proxy_log2(a: int, b: int) -> float:
    return log2_binom(a + b - 2, a - 1)


def old_tau(k: int, h: int, j: int) -> int:
    return k - h + j


def new_tau(k: int, h: int, j: int) -> int:
    half = (k + 1) // 2
    if j >= half:
        return half
    return k - h + j


def trace_sum_log2(k: int, h: int, sharpened: bool) -> tuple[float, int, float]:
    terms: list[float] = []
    max_j = 0
    max_term = float("-inf")
    for j in range(1, h + 1):
        tau = new_tau(k, h, j) if sharpened else old_tau(k, h, j)
        term = log2_binom(h, j) + ramsey_proxy_log2(k - 1, tau)
        terms.append(term)
        if term > max_term:
            max_term = term
            max_j = j
    return log2_add(terms), max_j, max_term


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("k", type=int)
    parser.add_argument("h", type=int)
    args = parser.parse_args()
    if not (2 <= args.h < args.k):
        parser.error("need 2 <= h < k")

    old_total, old_j, old_max = trace_sum_log2(args.k, args.h, sharpened=False)
    new_total, new_j, new_max = trace_sum_log2(args.k, args.h, sharpened=True)

    print(f"k={args.k}")
    print(f"h={args.h}")
    print(f"old_log2_sum_bound={old_total:.6f}")
    print(f"old_max_term_j={old_j}")
    print(f"old_max_term_log2={old_max:.6f}")
    print(f"new_log2_sum_bound={new_total:.6f}")
    print(f"new_max_term_j={new_j}")
    print(f"new_max_term_log2={new_max:.6f}")
    print(f"improvement_bits={old_total - new_total:.6f}")
    print(f"old_per_k={old_total / args.k:.6f}")
    print(f"new_per_k={new_total / args.k:.6f}")


if __name__ == "__main__":
    main()
