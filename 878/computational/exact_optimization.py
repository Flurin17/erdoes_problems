#!/usr/bin/env python3
"""Deterministic exact experiments for Erdos problem 878.

Only integer arithmetic is used for f, M, and F.  The small-n oracle scans
all integers a <= n independently of the support-partition formulation.
"""

from __future__ import annotations

import argparse
import math
import time
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, List, Sequence, Tuple


def prime_factors(n: int) -> Tuple[int, ...]:
    """Return the distinct prime factors of positive n in increasing order."""
    if n < 1:
        raise ValueError("n must be positive")
    factors: List[int] = []
    d = 2
    remainder = n
    while d * d <= remainder:
        if remainder % d == 0:
            factors.append(d)
            while remainder % d == 0:
                remainder //= d
        d = 3 if d == 2 else d + 2
    if remainder > 1:
        factors.append(remainder)
    return tuple(factors)


def primes_below(x: int) -> List[int]:
    """Return all primes p < x by a deterministic sieve."""
    if x <= 2:
        return []
    sieve = bytearray(b"\x01") * x
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(x - 1) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:x:p] = b"\x00" * (((x - 1 - start) // p) + 1)
    return [p for p in range(2, x) if sieve[p]]


def largest_power_leq(p: int, n: int) -> int:
    """Return p**floor(log_p(n)), without floating point logarithms."""
    if p < 2 or n < 1:
        raise ValueError("require p >= 2 and n >= 1")
    value = 1
    while value <= n // p:
        value *= p
    return value


def f_exact(n: int) -> int:
    """Compute f(n), with f(1)=0."""
    return sum(largest_power_leq(p, n) for p in prime_factors(n))


def mask_primes(primes: Sequence[int], mask: int) -> Tuple[int, ...]:
    return tuple(p for i, p in enumerate(primes) if mask & (1 << i))


def exact_support_max(n: int, block: Sequence[int]) -> int:
    """Compute M_n(block) by exhaustive exponent-vector enumeration."""
    block = tuple(block)
    if n < 1 or not block:
        raise ValueError("require n >= 1 and a nonempty block")
    radical = 1
    for p in block:
        radical *= p
    if radical > n:
        raise ValueError("the requested exact support is infeasible")

    best = 0

    def visit(index: int, product: int) -> None:
        nonlocal best
        if index == len(block):
            best = max(best, product)
            return
        p = block[index]
        product *= p
        while product <= n:
            visit(index + 1, product)
            if product > n // p:
                break
            product *= p

    visit(0, 1)
    assert radical <= best <= n
    return best


@dataclass(frozen=True)
class FResult:
    primes: Tuple[int, ...]
    nonunit: int
    unit: int
    partition_masks: Tuple[int, ...]
    partition_values: Tuple[int, ...]
    block_maxima: Tuple[int, ...]


def f_partition_dp(n: int) -> FResult:
    """Compute F using the exact-support block values and subset DP."""
    if n < 1:
        raise ValueError("n must be positive")
    primes = prime_factors(n)
    size = 1 << len(primes)
    if n == 1:
        return FResult((), 0, 1, (), (), (0,))

    maxima = [0] * size
    for mask in range(1, size):
        maxima[mask] = exact_support_max(n, mask_primes(primes, mask))

    dp = [-1] * size
    choice = [0] * size
    dp[0] = 0
    for mask in range(1, size):
        low_bit = mask & -mask
        submask = mask
        while submask:
            if submask & low_bit:
                candidate = maxima[submask] + dp[mask ^ submask]
                if candidate > dp[mask]:
                    dp[mask] = candidate
                    choice[mask] = submask
            submask = (submask - 1) & mask

    full = size - 1
    parts: List[int] = []
    remaining = full
    while remaining:
        part = choice[remaining]
        assert part and part & remaining == part
        parts.append(part)
        remaining ^= part

    result = FResult(
        primes=primes,
        nonunit=dp[full],
        unit=dp[full] + 1,
        partition_masks=tuple(parts),
        partition_values=tuple(maxima[part] for part in parts),
        block_maxima=tuple(maxima),
    )
    assert sum(result.partition_values) == result.nonunit
    assert result.nonunit >= max(n, f_exact(n))
    return result


def support_mask_if_admissible(a: int, primes: Sequence[int]) -> int | None:
    """Return the exact support mask if all prime factors of a are in primes."""
    remainder = a
    mask = 0
    for i, p in enumerate(primes):
        if remainder % p == 0:
            mask |= 1 << i
            while remainder % p == 0:
                remainder //= p
    return mask if remainder == 1 and mask else None


def brute_force_family(n: int) -> Tuple[int, Tuple[int, ...], Dict[int, int]]:
    """Independent oracle: scan admissible a and maximize disjoint supports."""
    primes = prime_factors(n)
    best: Dict[int, Tuple[int, Tuple[int, ...]]] = {0: (0, ())}
    maxima: Dict[int, int] = {}
    for a in range(2, n + 1):
        mask = support_mask_if_admissible(a, primes)
        if mask is None:
            continue
        maxima[mask] = a
        updated = dict(best)
        for used, (value, family) in best.items():
            if used & mask:
                continue
            new_state = used | mask
            candidate = (value + a, family + (a,))
            if new_state not in updated or candidate[0] > updated[new_state][0]:
                updated[new_state] = candidate
        best = updated
    optimum, family = max(best.values(), key=lambda item: item[0])
    return optimum, family, maxima


def equality_criterion(n: int, result: FResult | None = None) -> bool:
    """Test all exact-support subset inequalities characterizing F=f."""
    result = result or f_partition_dp(n)
    if n == 1:
        return True
    singleton = [largest_power_leq(p, n) for p in result.primes]
    for mask in range(1, 1 << len(result.primes)):
        bound = sum(singleton[i] for i in range(len(singleton)) if mask & (1 << i))
        if result.block_maxima[mask] > bound:
            return False
    return True


def harmonic_numbers(limit: int) -> List[Fraction]:
    values = [Fraction(0)]
    for m in range(1, limit + 1):
        values.append(values[-1] + Fraction(1, m))
    return values


def h_direct(x: int) -> Fraction:
    """Directly compute H(x)=sum_{1 <= n < x} f(n)/n."""
    if x < 1:
        raise ValueError("x must be a positive integer")
    return sum((Fraction(f_exact(n), n) for n in range(1, x)), Fraction(0))


def h_prime_block_identity(x: int) -> Fraction:
    """Compute H(x) using the finite prime/block identity in NOTES.md."""
    if x < 1:
        raise ValueError("x must be a positive integer")
    harmonics = harmonic_numbers(max(0, (x - 1) // 2))
    total = Fraction(0)
    for p in primes_below(x):
        upper = (x - 1) // p  # ceil(x/p)-1 for integral x
        power = 1
        while power <= upper:
            right = min(power * p - 1, upper)
            total += power * (harmonics[right] - harmonics[power - 1])
            power *= p
    return total


def format_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def format_partition(result: FResult) -> str:
    blocks = []
    for mask, value in zip(result.partition_masks, result.partition_values):
        block = "*".join(map(str, mask_primes(result.primes, mask)))
        blocks.append(f"[{block}]:{value}")
    return " ".join(blocks) if blocks else "(empty)"


def verify(limit: int, h_x: int) -> None:
    if limit < 1 or h_x < 1:
        raise ValueError("limits must be positive")
    started = time.perf_counter()
    one_prime = two_prime = equality_count = 0
    for n in range(1, limit + 1):
        factors = prime_factors(n)
        result = f_partition_dp(n)
        brute, family, brute_maxima = brute_force_family(n)
        f_value = f_exact(n)

        assert result.nonunit == brute, (n, result.nonunit, brute, family)
        assert result.unit == result.nonunit + 1
        assert len(family) == len(set(family))
        for i, a in enumerate(family):
            assert 2 <= a <= n and support_mask_if_admissible(a, factors) is not None
            for b in family[i + 1 :]:
                # Euclid, kept local so the oracle does not depend on math.gcd.
                u, v = a, b
                while v:
                    u, v = v, u % v
                assert u == 1
        if n > 1:
            full = (1 << len(factors)) - 1
            assert result.block_maxima[full] == n
            for mask in range(1, full + 1):
                assert result.block_maxima[mask] == brute_maxima[mask], (n, mask)
            for i, p in enumerate(factors):
                assert result.block_maxima[1 << i] == largest_power_leq(p, n)
        else:
            assert result.nonunit == f_value == 0

        criterion = equality_criterion(n, result)
        assert criterion == (result.nonunit == f_value), (n, criterion)
        equality_count += int(criterion)
        if len(factors) == 1:
            one_prime += 1
            assert result.nonunit == f_value == n
        if len(factors) == 2:
            two_prime += 1
            assert result.nonunit == max(n, f_value)

    direct = h_direct(h_x)
    blocked = h_prime_block_identity(h_x)
    assert direct == blocked, (h_x, direct, blocked)
    elapsed = time.perf_counter() - started
    print(f"verified n=1..{limit}; H at integer x={h_x}")
    print(f"one-prime cases={one_prime}; two-prime cases={two_prime}; F_nonunit=f cases={equality_count}")
    print(f"H({h_x})={format_fraction(direct)} (~{float(direct):.12g})")
    print("invariants: exact integer powers; every block M agrees with the integer-scan oracle;")
    print("  partition DP agrees with admissible-family DP; witnesses are distinct/coprime/in range;")
    print("  M(full)=n; singleton/one-prime/two-prime formulas; all-subset equality criterion;")
    print("  F_unit=F_nonunit+1; direct H equals the finite prime/block identity")
    print(f"runtime_seconds={elapsed:.6f}")


def print_single(n: int) -> None:
    result = f_partition_dp(n)
    f_value = f_exact(n)
    print(f"n={n} support={result.primes}")
    print(f"f={f_value} F_nonunit={result.nonunit} F_unit={result.unit}")
    print(f"F_nonunit=f: {result.nonunit == f_value}; criterion: {equality_criterion(n, result)}")
    print(f"optimal partition: {format_partition(result)}")
    if n > 1:
        for mask in range(1, 1 << len(result.primes)):
            print(f"M({mask_primes(result.primes, mask)})={result.block_maxima[mask]}")


def print_tables(limit: int) -> None:
    if limit < 1:
        raise ValueError("limit must be positive")
    started = time.perf_counter()
    equality_nonunit: List[int] = []
    equality_unit: List[int] = []
    max_f = max_fn = max_fu = -1
    print("running-record table (a row appears when f, F_nonunit, or F_unit sets a record)")
    print("n support f F_nonunit F_unit record_f record_F_nonunit record_F_unit")
    for n in range(1, limit + 1):
        result = f_partition_dp(n)
        f_value = f_exact(n)
        if f_value == result.nonunit:
            equality_nonunit.append(n)
        if f_value == result.unit:
            equality_unit.append(n)
        flags = (f_value > max_f, result.nonunit > max_fn, result.unit > max_fu)
        if any(flags):
            print(n, ",".join(map(str, result.primes)) or "-", f_value, result.nonunit,
                  result.unit, *("*" if flag else "." for flag in flags))
        max_f = max(max_f, f_value)
        max_fn = max(max_fn, result.nonunit)
        max_fu = max(max_fu, result.unit)
    print(f"equality table, nonunit convention ({len(equality_nonunit)}): {equality_nonunit}")
    print(f"equality table, unit convention ({len(equality_unit)}): {equality_unit}")
    print(f"terminal maxima: max_f={max_f} max_F_nonunit={max_fn} max_F_unit={max_fu}")
    print(f"runtime_seconds={time.perf_counter() - started:.6f}")


def print_h(x: int) -> None:
    direct = h_direct(x)
    blocked = h_prime_block_identity(x)
    print(f"H({x}) direct={format_fraction(direct)} (~{float(direct):.12g})")
    print(f"H({x}) prime_block={format_fraction(blocked)}")
    print(f"exact_match={direct == blocked}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    single = commands.add_parser("single", help="show exact data for one n")
    single.add_argument("n", type=int)
    check = commands.add_parser("verify", help="run independent finite cross-checks")
    check.add_argument("--limit", type=int, default=500)
    check.add_argument("--h-x", type=int, default=501)
    tables = commands.add_parser("tables", help="print equality and running-maxima tables")
    tables.add_argument("--limit", type=int, default=100)
    h_command = commands.add_parser("h", help="compare the two exact formulas for H(x)")
    h_command.add_argument("x", type=int)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "single":
        print_single(args.n)
    elif args.command == "verify":
        verify(args.limit, args.h_x)
    elif args.command == "tables":
        print_tables(args.limit)
    elif args.command == "h":
        print_h(args.x)
    else:  # pragma: no cover - argparse enforces this
        raise AssertionError(args.command)


if __name__ == "__main__":
    main()
