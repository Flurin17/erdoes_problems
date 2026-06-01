#!/usr/bin/env python3
"""Verify the support-3 separator calibration from PROOF.md.

The construction is not a graph search.  It checks the signed-indicator
system in Example 18B: support sizes, total imbalance, a strict separator, and
the Fibonacci lower-bound recurrence forced on every integer separator.
"""

from __future__ import annotations

import argparse


Vector = tuple[int, ...]


def fibonacci(count: int) -> list[int]:
    out = [1, 1]
    while len(out) <= count:
        out.append(out[-1] + out[-2])
    return out[: count + 1]


def add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))


def dot(a: Vector, b: Vector) -> int:
    return sum(x * y for x, y in zip(a, b))


def unit(index: int, d: int, sign: int = 1) -> Vector:
    return tuple(sign if i == index else 0 for i in range(d))


def support(v: Vector) -> int:
    return sum(1 for x in v if x)


def build_vectors(t: int) -> list[Vector]:
    d = 2 * t + 2
    p = list(range(t + 1))
    n = list(range(t + 1, d))
    vectors: list[Vector] = []

    for i in range(t + 1):
        vectors.append(unit(p[i], d, 1))
    for i in range(t + 1):
        vectors.append(unit(n[i], d, -1))
    for i in range(2, t + 1):
        v = [0] * d
        v[p[i]] = 1
        v[n[i - 1]] = 1
        v[n[i - 2]] = 1
        vectors.append(tuple(v))
    for i in range(1, t + 1):
        v = [0] * d
        v[n[i]] = -1
        v[p[i]] = -1
        v[p[i - 1]] = -1
        vectors.append(tuple(v))
    return vectors


def explicit_separator(t: int) -> Vector:
    p = [0] * (t + 1)
    q = [0] * (t + 1)
    p[0] = p[1] = q[0] = 1
    q[1] = p[1] + p[0] + 1
    for i in range(2, t + 1):
        p[i] = q[i - 1] + q[i - 2] + 1
        q[i] = p[i] + p[i - 1] + 1
    return tuple(p + [-x for x in q])


def forced_lower_bounds(t: int) -> tuple[list[int], list[int]]:
    p = [1] * (t + 1)
    q = [1] * (t + 1)
    q[1] = p[1] + p[0] + 1
    for i in range(2, t + 1):
        p[i] = q[i - 1] + q[i - 2] + 1
        q[i] = p[i] + p[i - 1] + 1
    return p, q


def check(t: int) -> dict[str, int]:
    vectors = build_vectors(t)
    d = 2 * t + 2
    zero = tuple(0 for _ in range(d))
    total = zero
    for v in vectors:
        total = add(total, v)

    sep = explicit_separator(t)
    dots = [dot(sep, v) for v in vectors]
    p_lower, q_lower = forced_lower_bounds(t)
    fib = fibonacci(t)

    assert len(vectors) == 4 * t + 1
    assert max(support(v) for v in vectors) <= 3
    assert max(abs(x) for x in total) <= 2
    assert min(dots) >= 1
    assert p_lower[t] >= fib[t]
    for i in range(3, t + 1):
        assert p_lower[i] >= p_lower[i - 1] + p_lower[i - 2]
    for i in range(1, t + 1):
        assert q_lower[i] >= p_lower[i] + p_lower[i - 1] + 1
    return {
        "t": t,
        "d": d,
        "vectors": len(vectors),
        "max_total": max(abs(x) for x in total),
        "min_dot": min(dots),
        "forced_p_t": p_lower[t],
        "fib_t": fib[t],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-t", type=int, default=12)
    args = parser.parse_args()
    if args.max_t < 2:
        raise SystemExit("--max-t must be at least 2")

    print("t d vectors max_total min_dot forced_p_t fib_t")
    for t in range(2, args.max_t + 1):
        row = check(t)
        print(
            "{t} {d} {vectors} {max_total} {min_dot} {forced_p_t} {fib_t}".format(
                **row
            )
        )


if __name__ == "__main__":
    main()
