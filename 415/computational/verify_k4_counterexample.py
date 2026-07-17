#!/usr/bin/env python3
"""Independent finite certificate that the decreasing 4-pattern is not last."""

from __future__ import annotations

import math


def phi_by_trial_division(n: int) -> int:
    result = n
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            result -= result // p
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        result -= result // remaining
    return result


def phi_by_gcd_count(n: int) -> int:
    return sum(math.gcd(a, n) == 1 for a in range(1, n + 1))


def pattern(values: tuple[int, ...]) -> tuple[int, ...] | None:
    if len(values) != len(set(values)):
        return None
    return tuple(sorted(range(1, len(values) + 1), key=lambda i: values[i - 1]))


def first_endpoint(target: tuple[int, ...], endpoint_limit: int) -> tuple[int, tuple[int, ...]] | None:
    k = len(target)
    for endpoint in range(k, endpoint_limit + 1):
        values = tuple(phi_by_trial_division(n) for n in range(endpoint - k + 1, endpoint + 1))
        if pattern(values) == target:
            return endpoint, values
    return None


def main() -> None:
    for n in range(1, 828):
        assert phi_by_trial_division(n) == phi_by_gcd_count(n)

    decreasing = (4, 3, 2, 1)
    later = (3, 2, 1, 4)
    first_decreasing = first_endpoint(decreasing, 827)
    first_later = first_endpoint(later, 827)
    assert first_decreasing == (826, (822, 408, 400, 348))
    assert first_later == (827, (408, 400, 348, 826))

    print("independent method: trial-division phi; cross-check: gcd counting for n<=827")
    print(f"M({decreasing}) = {first_decreasing[0]}, phi(823..826) = {first_decreasing[1]}")
    print(f"M({later}) = {first_later[0]}, phi(824..827) = {first_later[1]}")
    print("therefore the decreasing 4-pattern is not the last 4-pattern to appear")


if __name__ == "__main__":
    main()
