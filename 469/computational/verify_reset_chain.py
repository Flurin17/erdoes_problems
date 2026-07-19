#!/usr/bin/env python3
"""Exact certificate for the gap reset 70 -> 70*149 -> 70*149*4051.

The final node 70*149*4051*4177 is checked to be semiperfect and every
prime cover is checked to be nonsemiperfect.  No randomized choices occur.
"""

from bisect import bisect_left
from math import isqrt, prod
from time import perf_counter


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return False
    return True


def subset_sums(values: set[int]) -> set[int]:
    sums = {0}
    for value in sorted(values):
        sums |= {old + value for old in sums}
    return sums


def positive_gaps(target: int, sums: set[int]) -> set[int]:
    return {target - value for value in sums if value < target}


def failed_child_gap(gaps: set[int], totals: set[int], prime: int) -> int:
    """Return min(prime*r-s>0), after asserting there is no equality."""
    assert not any(prime * gap in totals for gap in gaps)
    ordered = sorted(totals)
    answer = None
    for gap in gaps:
        index = bisect_left(ordered, prime * gap) - 1
        if index >= 0:
            candidate = prime * gap - ordered[index]
            answer = candidate if answer is None else min(answer, candidate)
    assert answer is not None
    return answer


def assert_divisor_witness(target: int, witness: set[int]) -> None:
    assert len(witness) > 1
    assert all(0 < value < target and target % value == 0 for value in witness)
    assert sum(witness) == target


def squarefree_sigma(primes: list[int]) -> int:
    return prod(p + 1 for p in primes)


def main() -> None:
    started = perf_counter()
    p1, p2, p3 = 149, 4051, 4177
    assert all(is_prime(p) for p in (p1, p2, p3))

    divisors70 = {1, 2, 5, 7, 10, 14, 35, 70}
    proper70 = divisors70 - {70}
    proper_sums70 = subset_sums(proper70)
    totals70 = subset_sums(divisors70)
    assert proper_sums70 == set(range(0, 4)) | set(range(5, 70)) | {71, 72, 73, 74}
    assert totals70 == set(range(0, 4)) | set(range(5, 140)) | {141, 142, 143, 144}

    gaps70 = positive_gaps(70, proper_sums70)
    assert gaps70 == set(range(1, 66)) | {67, 68, 69, 70}
    assert min(gaps70) == 1

    m1 = 70 * p1
    totals1 = {left + p1 * right for left in totals70 for right in totals70}
    gaps1 = {p1 * gap - total for gap in gaps70 for total in totals70 if p1 * gap > total}
    assert max(totals1) == 21_600
    assert len(gaps1) == len(gaps70) * len(totals70)
    assert min(gaps1) == 5

    # The only capacity-eligible gap is 5, and both proposed next primes miss.
    assert [gap for gap in gaps1 if p2 * gap <= max(totals1)] == [5]
    assert [gap for gap in gaps1 if p3 * gap <= max(totals1)] == [5]
    assert 5 * p2 == p1 * 135 + 140 and 140 not in totals70
    assert 5 * p2 not in totals1
    assert 5 * p3 == p1 * 140 + 25 and 140 not in totals70
    assert 5 * p3 not in totals1

    m2 = m1 * p2
    assert failed_child_gap(gaps1, totals1, p2) == 1
    assert 5 * p2 - 1 == p1 * 135 + 139
    assert 135 in totals70 and 139 in totals70
    assert 5 * p2 - 1 in totals1
    assert all(value in totals1 for value in range(20_120, 20_255))

    # Build an explicit subset of proper divisors of m2 summing to m2-1.
    u1 = divisors70 | {p1 * value for value in {1, 2, 7, 10, 14, 35}}
    v1 = (divisors70 - {5}) | {p1 * value for value in divisors70 - {2, 7}}
    assert sum(u1) == m1 - 5
    assert sum(v1) == 5 * p2 - 1
    u2 = {p2 * value for value in u1} | v1
    assert len(u2) == len(u1) + len(v1)
    assert all(m2 % value == 0 and value < m2 for value in u2)
    assert sum(u2) == m2 - 1

    # A genuine failed new-largest prime below half the scalar threshold.
    half_prime = 42_253_417
    sigma2 = 87_523_200
    delta2 = sigma2 - 2 * m2
    excess = half_prime - m2
    assert is_prime(half_prime)
    assert p2 < half_prime < sigma2 // 2

    def in_totals2(value: int) -> bool:
        return any(value - p2 * right in totals1 for right in totals1)

    forced_holes = {
        excess,
        delta2 - excess,
        delta2 - 2 * excess,
        delta2 - (excess - 1),
        delta2 - 2 * excess + 1,
    }
    assert all(not in_totals2(value) for value in forced_holes)
    assert all(value not in totals1 for value in range(592, 745))
    assert not in_totals2(half_prime)
    assert not in_totals2(2 * half_prime)
    assert in_totals2(half_prime - 2)
    assert not in_totals2(half_prime - 1)
    assert not in_totals2(2 * half_prime - 1)
    assert 2 * half_prime <= sigma2 < 3 * half_prime

    boundary = {p2, 70, 35, 14, 7}
    assert sum(boundary) == p3
    terminal = m2 * p3
    witness = {p3 * value for value in u2} | boundary
    assert len(witness) == len(u2) + len(boundary)
    assert_divisor_witness(terminal, witness)

    # Check the six prime covers.  Removing p3 leaves failed node m2;
    # removing p2 leaves the independently verified failed extension m1*p3.
    assert 5 * p2 not in totals1
    assert 5 * p3 not in totals1

    # Removing p1 fails even the boundary-capacity condition over core 70.
    assert p2 * p3 > 144 * (p2 + p3 + 1)

    # Removing a core prime leaves a deficient squarefree number.
    terminal_primes = [2, 5, 7, p1, p2, p3]
    for removed in (2, 5, 7):
        cover_primes = [p for p in terminal_primes if p != removed]
        cover = prod(cover_primes)
        assert squarefree_sigma(cover_primes) < 2 * cover

    print(f"verified_terminal={terminal}")
    print(f"witness_terms={len(witness)}")
    print("gap_chain=1,5,1")
    print("reset_child_initial_gap_interval=1..135")
    print(f"half_threshold_failed_prime={half_prime}")
    print("half_threshold_child_gap=2")
    print("cover_checks=6")
    print(f"runtime_seconds={perf_counter() - started:.6f}")


if __name__ == "__main__":
    main()
