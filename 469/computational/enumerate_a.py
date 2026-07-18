#!/usr/bin/env python3
"""Exact deterministic enumeration for Erdős Problem 469.

This is experimental evidence, not an asymptotic proof.  The optimized pass
is independently checked on a requested initial range by divisor scanning,
meet-in-the-middle subset sums, and direct testing of every proper divisor.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from collections import Counter, defaultdict


def spf_sieve(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, int(limit**0.5) + 1):
        if spf[p] == p:
            for multiple in range(p * p, limit + 1, p):
                if spf[multiple] == multiple:
                    spf[multiple] = p
    return spf


def factor(n: int, spf: list[int]) -> list[tuple[int, int]]:
    original = n
    out: list[tuple[int, int]] = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    product = 1
    for p, e in out:
        product *= p**e
    assert product == original
    return out


def all_divisors(factors: list[tuple[int, int]]) -> list[int]:
    divisors = [1]
    for p, e in factors:
        old = divisors
        divisors = []
        power = 1
        for _ in range(e + 1):
            divisors.extend(d * power for d in old)
            power *= p
    return sorted(divisors)


def sigma_from_factors(factors: list[tuple[int, int]]) -> int:
    value = 1
    for p, e in factors:
        value *= (p ** (e + 1) - 1) // (p - 1)
    return value


def bitset_hits(values: list[int], target: int) -> bool:
    reachable = 1
    mask = (1 << (target + 1)) - 1
    for value in values:
        if value <= target:
            reachable |= reachable << value
            reachable &= mask
    return bool((reachable >> target) & 1)


def semiperfect_fast(n: int, factors: list[tuple[int, int]]) -> bool:
    divisors = all_divisors(factors)
    assert divisors[-1] == n
    proper = divisors[:-1]
    sigma = sigma_from_factors(factors)
    assert sum(proper) + n == sigma
    excess = sigma - 2 * n
    if excess < 0:
        return False
    # Complementation makes both targets exact; choose the smaller one.
    target = min(n, excess)
    return bitset_hits(proper, target)


def scan_divisors(n: int) -> list[int]:
    return [d for d in range(1, n) if n % d == 0]


def mitm_hits(values: list[int], target: int) -> bool:
    mid = len(values) // 2

    def sums(part: list[int]) -> set[int]:
        result = {0}
        for value in part:
            result |= {s + value for s in tuple(result) if s + value <= target}
        return result

    left = sums(values[:mid])
    right = sums(values[mid:])
    return any(target - x in right for x in left)


def semiperfect_independent(n: int) -> bool:
    proper = scan_divisors(n)
    return mitm_hits(proper, n)


def enumerate_a(limit: int, cross_check: int) -> tuple[list[int], dict]:
    spf = spf_sieve(limit)
    covered = bytearray(limit + 1)
    members: list[int] = []
    semiperfect = bytearray(limit + 1)
    factor_rows: list[tuple[int, list[tuple[int, int]], int]] = []

    for n in range(1, limit + 1):
        factors = factor(n, spf)
        if covered[n]:
            semiperfect[n] = 1
            continue
        if semiperfect_fast(n, factors):
            semiperfect[n] = 1
            members.append(n)
            factor_rows.append((n, factors, sigma_from_factors(factors) - 2 * n))
            for multiple in range(2 * n, limit + 1, n):
                covered[multiple] = 1

    cc = min(cross_check, limit)
    member_set = set(members)
    for n in range(1, cc + 1):
        direct = semiperfect_independent(n)
        assert direct == bool(semiperfect[n]), (n, direct, semiperfect[n])
        direct_minimal = direct and all(
            not semiperfect_independent(d) for d in scan_divisors(n)
        )
        assert direct_minimal == (n in member_set), (n, direct_minimal)

    for n in members:
        assert all(d not in member_set for d in scan_divisors(n))
    recovered = bytearray(limit + 1)
    for a in members:
        for multiple in range(a, limit + 1, a):
            recovered[multiple] = 1
    assert recovered == semiperfect

    fixtures_in = {6, 20, 28, 88, 104, 350, 945}
    fixtures_out = {1, 2, 4, 12, 24, 40, 56, 70}
    assert all(x > limit or x in member_set for x in fixtures_in)
    assert all(x > limit or x not in member_set for x in fixtures_out)

    omega_counts = Counter(len(factors) for _, factors, _ in factor_rows)
    squarefree_count = sum(all(e == 1 for _, e in factors) for _, factors, _ in factor_rows)
    parent_types = Counter()
    for n, factors, _ in factor_rows:
        for p, _ in factors:
            parent = n // p
            pf = factor(parent, spf)
            sig = sigma_from_factors(pf)
            if sig < 2 * parent:
                parent_types["deficient"] += 1
            elif sig == 2 * parent:
                parent_types["perfect"] += 1
            else:
                assert not semiperfect[parent]
                parent_types["abundant_nonsemiperfect"] += 1

    dyadic: dict[int, dict[str, float | int]] = defaultdict(
        lambda: {"count": 0, "reciprocal_mass": 0.0}
    )
    for n in members:
        j = n.bit_length() - 1
        dyadic[j]["count"] += 1
        dyadic[j]["reciprocal_mass"] += 1.0 / n

    digest = hashlib.sha256(
        (",".join(map(str, members)) + "\n").encode("ascii")
    ).hexdigest()
    summary = {
        "limit": limit,
        "cross_checked_through": cc,
        "count": len(members),
        "last_member": members[-1] if members else None,
        "sha256_members_csv_line": digest,
        "omega_counts": dict(sorted(omega_counts.items())),
        "squarefree_count": squarefree_count,
        "parent_cover_types": dict(parent_types),
        "dyadic": {str(k): v for k, v in sorted(dyadic.items())},
        "first_members": members[:25],
        "last_members": members[-25:],
    }
    return members, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--cross-check", type=int, default=1_000)
    parser.add_argument("--include-members", action="store_true")
    args = parser.parse_args()
    start = time.perf_counter()
    members, summary = enumerate_a(args.limit, args.cross_check)
    if args.include_members:
        summary["members"] = members
    summary["runtime_seconds"] = round(time.perf_counter() - start, 6)
    print(json.dumps(summary, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
