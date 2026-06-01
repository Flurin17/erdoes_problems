#!/usr/bin/env python3
"""Verify the support-3 separator calibrations from PROOF.md.

The construction is not a graph search.  It checks the signed-indicator
systems in Examples 18B and 18C: support sizes, total imbalance, strict
separation, Fibonacci separator lower bounds, and the exponential
bounded-imbalance packing with graphical compensation.
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


def packing_multiplicities(t: int) -> list[int]:
    """Multiplicities for the exponential bounded-imbalance packing.

    The returned list matches the order in build_vectors(t).
    """
    pos_single = [0] * (t + 1)
    neg_single = [0] * (t + 1)
    pos_triple = [0] * (t + 1)
    neg_triple = [0] * (t + 1)

    pos_triple[t] = 1
    neg_triple[t] = 1
    neg_triple[t - 1] = 1
    for i in range(t - 1, 1, -1):
        pos_triple[i] = neg_triple[i] + neg_triple[i + 1]
        neg_triple[i - 1] = pos_triple[i] + pos_triple[i + 1]

    pos_single[0] = neg_triple[1]
    pos_single[1] = neg_triple[1] + neg_triple[2]
    neg_single[0] = pos_triple[2]

    counts: list[int] = []
    counts.extend(pos_single)
    counts.extend(neg_single)
    counts.extend(pos_triple[i] for i in range(2, t + 1))
    counts.extend(neg_triple[i] for i in range(1, t + 1))
    return counts


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


def is_graphical(sequence: list[int]) -> bool:
    seq = sorted(sequence, reverse=True)
    while seq and seq[0] > 0:
        degree = seq.pop(0)
        if degree < 0 or degree > len(seq):
            return False
        for i in range(degree):
            seq[i] -= 1
            if seq[i] < 0:
                return False
        seq.sort(reverse=True)
    return all(x == 0 for x in seq)


def has_graphical_compensator(total: Vector) -> bool:
    k = len(total) + 1
    for base_degree in range(k):
        sequence = [base_degree - x for x in total] + [base_degree]
        if all(0 <= x < k for x in sequence) and is_graphical(sequence):
            return True
    return False


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

    counts = packing_multiplicities(t)
    packing_total = zero
    for count, vector in zip(counts, vectors):
        packing_total = add(packing_total, tuple(count * x for x in vector))
    packing_dots = [dot(sep, vector) for count, vector in zip(counts, vectors) if count]
    packing_size = sum(counts)
    assert max(abs(x) for x in packing_total) <= 1
    assert min(packing_dots) >= 1
    assert packing_size >= fib[t]
    assert has_graphical_compensator(packing_total)
    return {
        "t": t,
        "d": d,
        "vectors": len(vectors),
        "max_total": max(abs(x) for x in total),
        "min_dot": min(dots),
        "forced_p_t": p_lower[t],
        "fib_t": fib[t],
        "packing_size": packing_size,
        "packing_max_total": max(abs(x) for x in packing_total),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-t", type=int, default=12)
    args = parser.parse_args()
    if args.max_t < 2:
        raise SystemExit("--max-t must be at least 2")

    print("t d vectors max_total min_dot forced_p_t fib_t packing_size packing_max_total")
    for t in range(2, args.max_t + 1):
        row = check(t)
        print(
            (
                "{t} {d} {vectors} {max_total} {min_dot} {forced_p_t} "
                "{fib_t} {packing_size} {packing_max_total}"
            ).format(
                **row
            )
        )


if __name__ == "__main__":
    main()
