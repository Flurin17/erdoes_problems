#!/usr/bin/env python3
"""Anchored Fourier/discrepancy diagnostics for Erdos Problem 451.

Only the standard library is used.  For every prime k < p < 2k, put

    g_p(r) = 1 if r is not in {1,...,k} (mod p), and 0 otherwise.

Then f(n)=prod_p g_p(n mod p) is the indicator in Problem 451.  The
program compares direct counts of f on [2k+1,2k+H] with its CRT density,
decomposes the discrepancy by interaction order, and explicitly sums all
one-prime Fourier modes (including their anchored phases).
"""

from __future__ import annotations

import argparse
import cmath
import math
from dataclasses import dataclass
from typing import Iterable


TAU = 2.0 * math.pi


def primes_below(n: int) -> list[int]:
    if n <= 2:
        return []
    sieve = bytearray(b"\x01") * n
    sieve[0:2] = b"\x00\x00"
    for q in range(2, math.isqrt(n - 1) + 1):
        if sieve[q]:
            sieve[q * q : n : q] = b"\x00" * (((n - 1 - q * q) // q) + 1)
    return [q for q in range(2, n) if sieve[q]]


def interval_primes(k: int) -> list[int]:
    return [p for p in primes_below(2 * k) if p > k]


def admissible_residue(n: int, k: int, ps: Iterable[int]) -> bool:
    return all(not (1 <= n % p <= k) for p in ps)


def verify_residue_equivalence(k: int, ps: Iterable[int]) -> None:
    """Exhaust every residue mod every p against the literal k factors."""
    for p in ps:
        for r in range(p):
            residue_test = not (1 <= r <= k)
            literal_test = all((r - i) % p for i in range(1, k + 1))
            if residue_test != literal_test:
                raise AssertionError(f"equivalence failed at k={k}, p={p}, r={r}")


def parse_ks(spec: str) -> list[int]:
    out: list[int] = []
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if ":" in item:
            fields = [int(x) for x in item.split(":")]
            if len(fields) == 2:
                lo, hi = fields
                step = 1
            elif len(fields) == 3:
                lo, hi, step = fields
            else:
                raise ValueError(f"bad range {item!r}")
            if step <= 0:
                raise ValueError("range step must be positive")
            out.extend(range(lo, hi + 1, step))
        else:
            out.append(int(item))
    if not out or min(out) < 1:
        raise ValueError("all k must be positive")
    return sorted(set(out))


def local_b(k: int, p: int, a: int) -> complex:
    """Normalized nonconstant coefficient hat(g_p)(a)/hat(g_p)(0)."""
    assert 1 <= a < p
    z = cmath.exp(-1j * TAU * a / p)
    forbidden_sum = z * (1.0 - z**k) / (1.0 - z)
    return -forbidden_sum / (p - k)


def exponential_interval(a: int, p: int, start: int, length: int) -> complex:
    """sum_{0<=t<length} exp(2 pi i a(start+t)/p)."""
    w = cmath.exp(1j * TAU * a / p)
    return w**start * (1.0 - w**length) / (1.0 - w)


@dataclass(frozen=True)
class Mode:
    p: int
    a: int
    b_abs: float
    b_arg: float
    anchor_arg: float
    kernel_abs: float
    real: float
    imag: float
    absolute: float


def local_inversion_error(k: int, ps: list[int]) -> float:
    err = 0.0
    for p in ps:
        alpha = (p - k) / p
        bs = [0j] + [local_b(k, p, a) for a in range(1, p)]
        for r in range(p):
            reconstructed = alpha * (
                1.0
                + sum(bs[a] * cmath.exp(1j * TAU * a * r / p) for a in range(1, p))
            )
            target = float(not (1 <= r <= k))
            err = max(err, abs(reconstructed - target))
    return err


def find_first(k: int, ps: list[int], limit: int) -> int | None:
    for n in range(2 * k + 1, 2 * k + 1 + limit):
        if admissible_residue(n, k, ps):
            return n
    return None


def one_k(k: int, h: int, order: int, search_limit: int) -> dict:
    ps = interval_primes(k)
    alpha = [(p - k) / p for p in ps]
    density = math.prod(alpha)
    start = 2 * k + 1
    verify_residue_equivalence(k, ps)

    # C[j]/density is sum_n e_j(u_p(n)), where u_p=g_p/alpha_p-1.
    interaction = [0.0] * (order + 1)
    actual = 0
    for n in range(start, start + h):
        good = admissible_residue(n, k, ps)
        actual += int(good)
        elementary = [0.0] * (order + 1)
        elementary[0] = 1.0
        used = 0
        for p, ap in zip(ps, alpha):
            u = (1.0 / ap - 1.0) if not (1 <= n % p <= k) else -1.0
            used += 1
            for j in range(min(order, used), 0, -1):
                elementary[j] += u * elementary[j - 1]
        for j in range(1, order + 1):
            interaction[j] += density * elementary[j]

    # Sum every singleton Fourier mode with the actual phase at start=2k+1.
    singleton = 0j
    singleton_l1 = 0.0
    modes: list[Mode] = []
    local_l1_factors: list[float] = []
    for p in ps:
        local_sum = 0.0
        for a in range(1, p):
            b = local_b(k, p, a)
            kernel = exponential_interval(a, p, start, h)
            term = density * b * kernel
            singleton += term
            singleton_l1 += abs(term)
            local_sum += abs(b)
            modes.append(
                Mode(
                    p=p,
                    a=a,
                    b_abs=abs(b),
                    b_arg=cmath.phase(b),
                    anchor_arg=(TAU * a * start / p) % TAU,
                    kernel_abs=abs(kernel),
                    real=term.real,
                    imag=term.imag,
                    absolute=abs(term),
                )
            )
        local_l1_factors.append(1.0 + local_sum)

    inv_err = local_inversion_error(k, ps)
    c1_err = abs(singleton.real - interaction[1]) if order >= 1 else math.nan
    imag_err = abs(singleton.imag)
    if inv_err > 2e-11 or c1_err > 2e-7 or imag_err > 2e-7:
        raise AssertionError(
            f"Fourier invariant failed: inv={inv_err}, c1={c1_err}, imag={imag_err}"
        )

    expected = h * density
    discrepancy = actual - expected
    partial = sum(interaction[1:])
    first = find_first(k, ps, search_limit)
    # The full Fourier coefficient l1 norm is density*prod(1+sum |b_p|).
    log10_full_l1 = (
        math.log10(density) + sum(math.log10(x) for x in local_l1_factors)
        if density > 0
        else -math.inf
    )
    return {
        "k": k,
        "m": len(ps),
        "h": h,
        "density": density,
        "expected": expected,
        "actual": actual,
        "discrepancy": discrepancy,
        "first": first,
        "gap": None if first is None else first - 2 * k,
        "interaction": interaction,
        "residual": discrepancy - partial,
        "singleton_l1": singleton_l1,
        "cancel_ratio": abs(interaction[1]) / singleton_l1 if singleton_l1 else 0.0,
        "inv_err": inv_err,
        "c1_err": c1_err,
        "log10_full_l1": log10_full_l1,
        "modes": sorted(modes, key=lambda x: (-x.absolute, x.p, x.a)),
    }


def fmt(x: float | int | None) -> str:
    if x is None:
        return "NA"
    if isinstance(x, int):
        return str(x)
    return f"{x:.8g}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ks", default="5,10,20,40,80,160,320")
    parser.add_argument("--H", type=int, default=100_000)
    parser.add_argument("--order", type=int, default=6)
    parser.add_argument("--search-limit", type=int, default=1_000_000)
    parser.add_argument("--detail-k", type=int, default=160)
    parser.add_argument("--top-modes", type=int, default=20)
    args = parser.parse_args()
    if args.H < 1 or args.order < 1 or args.search_limit < 1 or args.top_modes < 0:
        parser.error("H, order, and search-limit must be positive; top-modes nonnegative")

    results = [one_k(k, args.H, args.order, args.search_limit) for k in parse_ks(args.ks)]
    print("# Anchored Fourier/discrepancy experiment")
    print(
        f"# ks={args.ks} H={args.H} order={args.order} "
        f"search_limit={args.search_limit} detail_k={args.detail_k}"
    )
    headers = [
        "k", "m", "H", "density", "expected", "actual", "discrepancy",
        "first_n", "gap", "C1", "singleton_L1", "cancel_ratio",
    ] + [f"C{j}" for j in range(2, args.order + 1)] + [
        f"residual_after_C{args.order}", "log10_full_Fourier_L1", "max_inv_err",
    ]
    print("\t".join(headers))
    for r in results:
        row = [
            r["k"], r["m"], r["h"], r["density"], r["expected"], r["actual"],
            r["discrepancy"], r["first"], r["gap"], r["interaction"][1],
            r["singleton_l1"], r["cancel_ratio"],
        ] + [r["interaction"][j] for j in range(2, args.order + 1)] + [
            r["residual"], r["log10_full_l1"], r["inv_err"],
        ]
        print("\t".join(fmt(x) for x in row))

    details = [r for r in results if r["k"] == args.detail_k]
    if details and args.top_modes:
        r = details[0]
        print(f"# top {args.top_modes} singleton modes for k={args.detail_k}")
        print("p\ta\t|b|\targ_b\tanchor_phase\t|D_H|\tterm_real\tterm_imag\t|term|")
        for q in r["modes"][: args.top_modes]:
            print(
                "\t".join(
                    fmt(x)
                    for x in (
                        q.p, q.a, q.b_abs, q.b_arg, q.anchor_arg, q.kernel_abs,
                        q.real, q.imag, q.absolute,
                    )
                )
            )


if __name__ == "__main__":
    main()
