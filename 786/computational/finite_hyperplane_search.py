#!/usr/bin/env python3
"""Deterministic exact search for dense nonzero additive levels on [1,N].

The search uses an exact elimination that is special to the cutoff y=floor(sqrt(N)).
After weights on primes p <= y are fixed, an integer n <= N either is y-smooth,
or has a unique prime factor p > y, to the first power, and n=pk with k<=N/p.
Thus w_p can be chosen independently to put a modal value of the prefix
{f(k): k<=N/p} onto the target 1.

For each remaining small-prime coordinate, all values at which the objective can
change are rational and explicitly enumerable: a smooth integer can hit level 1,
or two cofactor values can collide.  Each coordinate step is therefore exact,
although coordinate ascent is only a local (not global) optimizer.

Examples:
  python3 786/computational/finite_hyperplane_search.py --N 100,200,500
  python3 786/computational/finite_hyperplane_search.py --N 1000 --sweeps 4
"""

from __future__ import annotations

import argparse
import math
from collections import Counter, defaultdict
from fractions import Fraction
from typing import Dict, Iterable, List, Sequence, Tuple


def sieve_spf(n: int) -> Tuple[List[int], List[int]]:
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(n) + 1):
        if spf[p] != p:
            continue
        for m in range(p * p, n + 1, p):
            if spf[m] == m:
                spf[m] = p
    return spf, [p for p in range(2, n + 1) if spf[p] == p]


def factorizations(n: int, spf: Sequence[int]) -> List[Dict[int, int]]:
    out: List[Dict[int, int]] = [{} for _ in range(n + 1)]
    for m in range(2, n + 1):
        x = m
        fac: Dict[int, int] = {}
        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            fac[p] = e
        out[m] = fac
    return out


def fvalue(fac: Dict[int, int], weights: Dict[int, Fraction]) -> Fraction:
    return sum((e * weights.get(p, Fraction(0)) for p, e in fac.items()), Fraction(0))


def fraction_key(x: Fraction) -> Tuple[int, int, int, int]:
    """A deterministic simplicity ordering, used only to print/tie-break starts."""
    return (abs(x.numerator) + x.denominator, x.denominator, abs(x.numerator), x.numerator)


class FiberSearch:
    def __init__(self, n: int):
        self.n = n
        self.y = math.isqrt(n)
        self.spf, self.primes = sieve_spf(n)
        self.fac = factorizations(n, self.spf)
        self.small_primes = [p for p in self.primes if p <= self.y]
        self.large_primes = [p for p in self.primes if p > self.y]
        self.smooth = [
            m for m in range(1, n + 1)
            if not self.fac[m] or max(self.fac[m]) <= self.y
        ]
        self.large_prefix_multiplicity = Counter(n // p for p in self.large_primes)

    def small_values(self, weights: Dict[int, Fraction]) -> List[Fraction]:
        return [fvalue(self.fac[m], weights) for m in range(self.n + 1)]

    def objective_from_values(self, vals: Sequence[Fraction]) -> int:
        score = sum(vals[m] == 1 for m in self.smooth)
        counts: Counter[Fraction] = Counter()
        mode = 0
        for k in range(1, self.y + 1):
            counts[vals[k]] += 1
            mode = max(mode, counts[vals[k]])
            score += self.large_prefix_multiplicity.get(k, 0) * mode
        return score

    def objective(self, weights: Dict[int, Fraction]) -> int:
        return self.objective_from_values(self.small_values(weights))

    def optimized_large_weights(
        self, weights: Dict[int, Fraction]
    ) -> Dict[int, Fraction]:
        vals = self.small_values(weights)
        prefix_modes: Dict[int, Fraction] = {}
        counts: Counter[Fraction] = Counter()
        current = Fraction(0)
        current_count = 0
        for k in range(1, self.y + 1):
            v = vals[k]
            counts[v] += 1
            if counts[v] > current_count or (
                counts[v] == current_count and fraction_key(v) < fraction_key(current)
            ):
                current = v
                current_count = counts[v]
            prefix_modes[k] = current
        ans = dict(weights)
        for p in self.large_primes:
            ans[p] = 1 - prefix_modes[self.n // p]
        return ans

    def verify_direct(self, weights: Dict[int, Fraction]) -> int:
        full = self.optimized_large_weights(weights)
        direct = sum(fvalue(self.fac[m], full) == 1 for m in range(1, self.n + 1))
        reduced = self.objective(weights)
        assert direct == reduced, (self.n, direct, reduced)
        return direct

    def best_coordinate(
        self, weights: Dict[int, Fraction], q: int
    ) -> Tuple[Fraction, int, int]:
        """Return an exact conditional optimum for w_q and candidate count."""
        current = weights.get(q, Fraction(0))
        vals = self.small_values(weights)
        coeff = [self.fac[m].get(q, 0) for m in range(self.n + 1)]
        base = [vals[m] - coeff[m] * current for m in range(self.n + 1)]

        candidates = {current}
        smooth_hits: Counter[Fraction] = Counter()
        constant_smooth = 0
        for m in self.smooth:
            e = coeff[m]
            if e == 0:
                constant_smooth += base[m] == 1
            else:
                x = (1 - base[m]) / e
                smooth_hits[x] += 1
                candidates.add(x)

        # A prefix mode changes only when two affine values collide.  Pairs
        # with equal q-adic exponent are either always equal or never equal.
        for a in range(1, self.y + 1):
            ea = coeff[a]
            for b in range(a + 1, self.y + 1):
                eb = coeff[b]
                if ea != eb:
                    candidates.add((base[b] - base[a]) / (ea - eb))

        def score(x: Fraction) -> int:
            total = constant_smooth + smooth_hits[x]
            counts: Counter[Fraction] = Counter()
            mode = 0
            for k in range(1, self.y + 1):
                v = base[k] + coeff[k] * x
                counts[v] += 1
                mode = max(mode, counts[v])
                total += self.large_prefix_multiplicity.get(k, 0) * mode
            return total

        current_score = score(current)
        best_x = current
        best_score = current_score
        # Moving on a tie can cycle and is not needed for the local-optimum
        # certificate.  Simpler starts supply alternative tie resolutions.
        for x in sorted(candidates, key=fraction_key):
            sx = score(x)
            if sx > best_score:
                best_x, best_score = x, sx
        return best_x, best_score, len(candidates)

    def coordinate_ascent(
        self, initial: Dict[int, Fraction], sweeps: int
    ) -> Tuple[Dict[int, Fraction], int, int]:
        weights = {p: Fraction(initial.get(p, 0)) for p in self.small_primes}
        tested = 0
        for sweep in range(sweeps):
            changed = False
            order = self.small_primes if sweep % 2 == 0 else list(reversed(self.small_primes))
            for q in order:
                old_score = self.objective(weights)
                x, new_score, ncand = self.best_coordinate(weights, q)
                tested += ncand
                assert new_score >= old_score
                if new_score > old_score:
                    weights[q] = x
                    changed = True
            if not changed:
                break
        score = self.verify_direct(weights)
        # Certify coordinatewise local optimality at termination, even if the
        # sweep budget stopped before a no-change pass.
        local = True
        for q in self.small_primes:
            _, qs, ncand = self.best_coordinate(weights, q)
            tested += ncand
            if qs > score:
                local = False
                break
        return weights, score, tested if local else -tested

    def fixed_threshold_best(self) -> Tuple[int, int]:
        best = -1
        best_cut = 1
        for cut in range(1, self.n + 1):
            full = {p: Fraction(p > cut) for p in self.primes}
            score = sum(fvalue(self.fac[m], full) == 1 for m in range(1, self.n + 1))
            if score > best:
                best, best_cut = score, cut
        return best, best_cut

    def starts(self) -> Iterable[Tuple[str, Dict[int, Fraction]]]:
        yield "zero", {p: Fraction(0) for p in self.small_primes}
        for u100 in (220, 240, 260, 265, 280, 300, 350, 400):
            u = u100 / 100
            cut = self.n ** (1 / u)
            yield f"threshold-u={u:.2f}", {
                p: Fraction(p > cut) for p in self.small_primes
            }
        logn = math.log(self.n)
        for scale in (2, 3, 4, 5, 7, 10):
            yield f"rounded-log-{scale}", {
                p: Fraction(round(scale * math.log(p) / logn), scale)
                for p in self.small_primes
            }


def weight_summary(search: FiberSearch, small: Dict[int, Fraction]) -> str:
    grouped: Dict[Fraction, List[int]] = defaultdict(list)
    for p in search.small_primes:
        grouped[small.get(p, Fraction(0))].append(p)
    pieces = []
    for value in sorted(grouped, key=fraction_key):
        ps = grouped[value]
        pieces.append(f"{value}:" + ",".join(map(str, ps)))
    return " | ".join(pieces)


def large_histogram(search: FiberSearch, small: Dict[int, Fraction]) -> str:
    full = search.optimized_large_weights(small)
    hist = Counter(full[p] for p in search.large_primes)
    return " | ".join(
        f"{value}:{hist[value]}" for value in sorted(hist, key=fraction_key)
    )


def run_one(n: int, sweeps: int) -> None:
    search = FiberSearch(n)
    threshold_score, threshold_cut = search.fixed_threshold_best()
    best_score = -1
    best_name = ""
    best_weights: Dict[int, Fraction] = {}
    best_tested = 0
    for name, initial in search.starts():
        weights, score, tested = search.coordinate_ascent(initial, sweeps)
        if score > best_score:
            best_name, best_score, best_weights, best_tested = name, score, weights, tested
    local = best_tested >= 0
    print(
        f"N={n} y={search.y} primes_small={len(search.small_primes)} "
        f"best={best_score}/{n}={best_score/n:.9f} start={best_name} "
        f"coordinate_local={local} candidates_tested={abs(best_tested)} "
        f"fixed_threshold={threshold_score}/{n} cut={threshold_cut}"
    )
    print("  small", weight_summary(search, best_weights))
    print("  optimized-large histogram", large_histogram(search, best_weights))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", default="100,200,500", help="comma-separated endpoints")
    parser.add_argument("--sweeps", type=int, default=4)
    args = parser.parse_args()
    for n in (int(x) for x in args.N.split(",")):
        if n < 2:
            raise ValueError("N must be at least 2")
        run_one(n, args.sweeps)


if __name__ == "__main__":
    main()
