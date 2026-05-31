#!/usr/bin/env python3
"""Report small n covered by currently recorded positive/negative facts.

This script deliberately avoids guessing. It marks only:

- elementary positive families from PROOF.md;
- recorded sufficient Beeson `3alpha+2beta=pi` constructions;
- Zhang's sufficiently-large 2pi/3 family for primitive triples found in range;
- Beeson negatives 7 and 11.
- workspace composite obstructions 14, 15, 21, 22, 30, 33, 35, 38, 39, 42,
  46, 51, 55, 57, and 62;
- workspace prime obstructions from the source-reduction dashboard: primes
  `3 mod 4` are negative unless they survive Beeson's isosceles
  `gamma=2pi/3` prime filter; the surviving isosceles candidates are then
  removed by the boundary-transition obstruction.

Everything else is reported as unresolved by this experiment.
"""

from __future__ import annotations

from math import ceil, gcd, isqrt

from beeson_3alpha2beta_sufficient import constructions as beeson_3alpha2beta_constructions


def is_square(n: int) -> bool:
    r = isqrt(n)
    return r * r == n


def is_sum_two_squares(n: int) -> bool:
    for a in range(1, isqrt(n) + 1):
        b2 = n - a * a
        b = isqrt(b2)
        if b > 0 and b * b == b2:
            return True
    return False


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def survives_isosceles_gamma_prime_filter(p: int) -> bool:
    for t in range(1, isqrt((p - 1) // 2) + 1):
        b = t * t
        a = p - 2 * b
        if a <= 0 or gcd(a, b) != 1:
            continue
        c2 = a * a + a * b + b * b
        c = isqrt(c2)
        if c * c == c2:
            return True
    return False


def primitive_zhang_counts(limit_n: int, limit_side: int) -> dict[int, str]:
    out: dict[int, str] = {}
    for a in range(1, limit_side + 1):
        for b in range(1, a + 1):
            if gcd(a, b) != 1:
                continue
            c2 = a * a + a * b + b * b
            c = isqrt(c2)
            if c * c != c2:
                continue
            threshold = 3 * ceil((c2 - a - b) / (a * b))
            m = threshold
            while m * m * a * b <= limit_n:
                n = m * m * a * b
                out.setdefault(n, f"Zhang 2pi/3: ({a},{b},{c}), m={m}")
                m += 1
    return out


def classify(n: int, zhang: dict[int, str], beeson_sufficient: dict[int, str]) -> str:
    if n in beeson_sufficient:
        return f"positive: {beeson_sufficient[n]}"
    if n == 7:
        return "negative: Beeson"
    if n == 11:
        return "negative: Beeson"
    if n in {14, 15, 21, 30, 33, 35, 38, 39, 42, 46, 51, 55, 57, 62}:
        return "negative: workspace composite benchmark"
    if n == 22:
        return "negative: workspace N=22 composite benchmark"
    if is_prime(n) and n % 4 == 3 and n != 3:
        if survives_isosceles_gamma_prime_filter(n):
            return "negative: prime source reductions + isosceles gamma boundary transition"
        return "negative: prime source reductions + isosceles gamma filter"
    if is_square(n):
        return "positive: square"
    if n % 2 == 0 and is_square(n // 2):
        return "positive: 2m^2"
    if n % 3 == 0 and is_square(n // 3):
        return "positive: 3m^2"
    if n % 6 == 0 and is_square(n // 6):
        return "positive: 6m^2"
    if is_sum_two_squares(n):
        return "positive: a^2+b^2"
    if n in zhang:
        return f"positive: {zhang[n]}"
    return "unresolved by current certificates"


def main() -> None:
    limit_n = 250
    zhang = primitive_zhang_counts(limit_n, 80)
    beeson_sufficient = {
        n: f"{rows[0].source}: {rows[0].details}"
        for n, rows in beeson_3alpha2beta_constructions(limit_n).items()
    }
    for n in range(1, limit_n + 1):
        print(f"{n:3d}: {classify(n, zhang, beeson_sufficient)}")


if __name__ == "__main__":
    main()
