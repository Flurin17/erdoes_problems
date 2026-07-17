#!/usr/bin/env python3
"""Deterministic exact search for multiband additive gradings (Problem 786).

A rational piecewise-constant prime weighting may be multiplied by a common
denominator and then divided by the gcd of its entries.  Thus, up to an
irrelevant nonzero scalar, it is represented uniquely here by a primitive
integer vector whose first nonzero entry is positive.

Prime-band endpoints are rational exponents: a cut k/D means
    p <= N**(k/D),
tested without floating point by p**D <= N**k.  For every grading we count
all exact nonzero fibers and retain the largest.  The program also computes
the best unrestricted integer prime cutoff y for the one-threshold grading
Omega_{p>y}, so a reported improvement is an exact same-N comparison.

Only Python's standard library is used.  A typical full run is

  python3 786/computational/multiband_search.py \
      --N 100000 --config 3:31:5 --config 4:31:3:11 \
      --binary-window 31:5:17 --ternary-window 31:7:15 \
      --top 12 --rank-n 450

The optional fourth config field requires that exponent cut to occur.  It is
useful for making a higher-band search contain the exact best one-threshold
cut without paying for every choice of all the other cuts.

The search is exhaustive over the displayed finite grids, not over all
rational band systems.
"""

from __future__ import annotations

import argparse
import bisect
import heapq
import itertools
import math
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, List, Sequence, Tuple


@dataclass(frozen=True)
class Candidate:
    count: int
    denominator: int
    cuts: Tuple[int, ...]
    weights: Tuple[int, ...]
    level: int

    def identity(self) -> Tuple[int, Tuple[int, ...], Tuple[int, ...], int]:
        return (self.denominator, self.cuts, self.weights, self.level)


def sieve_spf(n: int) -> Tuple[List[int], List[int]]:
    """Return smallest-prime-factor table and the primes through n."""
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(n) + 1):
        if spf[p] == p:
            start = p * p
            for m in range(start, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    primes = [p for p in range(2, n + 1) if spf[p] == p]
    return spf, primes


def primitive_weights(bands: int, bound: int) -> List[Tuple[int, ...]]:
    """All primitive projective rational weights with sup norm <= bound."""
    ans = set()
    values = range(-bound, bound + 1)
    for raw in itertools.product(values, repeat=bands):
        if not any(raw):
            continue
        g = 0
        for x in raw:
            g = math.gcd(g, abs(x))
        w = tuple(x // g for x in raw)
        first = next(x for x in w if x)
        if first < 0:
            w = tuple(-x for x in w)
        if max(map(abs, w)) <= bound:
            ans.add(w)
    return sorted(ans)


def atom_bins(primes: Sequence[int], n: int, denominator: int) -> Dict[int, int]:
    """Map p to j when N^(j/D) < p <= N^((j+1)/D), exactly."""
    powers = [1]
    for _ in range(denominator):
        powers.append(powers[-1] * n)
    out: Dict[int, int] = {}
    for p in primes:
        target = p**denominator
        k = bisect.bisect_left(powers, target, lo=1)
        assert 1 <= k <= denominator
        out[p] = k - 1
        assert p**denominator <= n ** (k)
        if k > 1:
            assert p**denominator > n ** (k - 1)
    return out


def atomic_signature_counts(
    n: int, spf: Sequence[int], pbin: Dict[int, int], denominator: int
) -> Tuple[List[Tuple[Tuple[int, ...], int]], int]:
    """Count exact atomic Omega-vectors using an integer DP encoding."""
    max_omega = n.bit_length() - 1
    bits = max(1, (max_omega + 1).bit_length())
    codes = [0] * (n + 1)
    counts: Counter[int] = Counter()
    counts[0] = 1  # n=1
    for m in range(2, n + 1):
        p = spf[m]
        codes[m] = codes[m // p] + (1 << (bits * pbin[p]))
        counts[codes[m]] += 1

    mask = (1 << bits) - 1
    decoded: List[Tuple[Tuple[int, ...], int]] = []
    for code, multiplicity in counts.items():
        x = code
        digits = []
        for _ in range(denominator):
            digits.append(x & mask)
            x >>= bits
        assert x == 0
        decoded.append((tuple(digits), multiplicity))
    decoded.sort()
    assert sum(c for _, c in decoded) == n
    return decoded, len(counts)


def coarsen_signatures(
    atomic: Sequence[Tuple[Tuple[int, ...], int]], cuts: Tuple[int, ...]
) -> List[Tuple[Tuple[int, ...], int]]:
    """Aggregate atomic exponent bins into the bands determined by cuts."""
    endpoints = (0,) + cuts
    denominator = len(atomic[0][0])
    stops = cuts + (denominator,)
    counter: Counter[Tuple[int, ...]] = Counter()
    for digits, multiplicity in atomic:
        prefix = [0]
        for x in digits:
            prefix.append(prefix[-1] + x)
        sig = tuple(prefix[b] - prefix[a] for a, b in zip(endpoints, stops))
        counter[sig] += multiplicity
    return sorted(counter.items())


def modal_nonzero_fiber(
    signatures: Sequence[Tuple[Tuple[int, ...], int]], weights: Tuple[int, ...]
) -> Tuple[int, int]:
    levels: Counter[int] = Counter()
    for signature, multiplicity in signatures:
        level = sum(x * w for x, w in zip(signature, weights))
        if level != 0:
            levels[level] += multiplicity
    if not levels:
        return (0, 0)
    # Deterministic tie-break: count, then smaller |level|, then smaller level.
    level, count = min(levels.items(), key=lambda kv: (-kv[1], abs(kv[0]), kv[0]))
    return count, level


def candidate_sort_key(c: Candidate) -> Tuple:
    return (-c.count, c.denominator, c.cuts, c.weights, abs(c.level), c.level)


def effective_atomic_weights(
    cuts: Tuple[int, ...], weights: Tuple[int, ...], occupied_bins: Sequence[int]
) -> Tuple[int, ...]:
    """Weight on each occupied atomic bin (empty exponent intervals omitted)."""
    return tuple(weights[bisect.bisect_right(cuts, j)] for j in occupied_bins)


def projective_fiber_key(values: Sequence[int], level: int) -> Tuple[Tuple[int, ...], int]:
    """Canonicalize (prime weights, level) under a common nonzero scaling."""
    g = abs(level)
    for x in values:
        g = math.gcd(g, abs(x))
    assert g > 0
    normalized = tuple(x // g for x in values)
    normalized_level = level // g
    first = next((x for x in normalized if x), normalized_level)
    if first < 0:
        normalized = tuple(-x for x in normalized)
        normalized_level = -normalized_level
    return normalized, normalized_level


def compressed_values(values: Sequence[int]) -> Tuple[int, ...]:
    ans: List[int] = []
    for x in values:
        if not ans or ans[-1] != x:
            ans.append(x)
    return tuple(ans)


def is_upper_step(values: Sequence[int]) -> bool:
    """Whether the prime weighting is 0 below one cutoff and constant above."""
    c = compressed_values(values)
    return (len(c) == 1 and c[0] != 0) or (
        len(c) == 2 and c[0] == 0 and c[1] != 0
    )


def search_config(
    n: int,
    spf: Sequence[int],
    primes: Sequence[int],
    bands: int,
    denominator: int,
    weight_bound: int,
    required_cut: int | None,
    top: int,
) -> Tuple[List[Candidate], Candidate, Candidate, int, int, int, int]:
    """Exhaust one (bands, exponent denominator, weight bound) grid."""
    if not (2 <= bands <= denominator):
        raise ValueError("need 2 <= bands <= denominator")
    pbin = atom_bins(primes, n, denominator)
    occupied_bins = sorted(set(pbin.values()))
    atomic, atomic_types = atomic_signature_counts(n, spf, pbin, denominator)
    weights = primitive_weights(bands, weight_bound)
    heap: List[Tuple[Tuple, Candidate]] = []
    seen = set()
    best_nonstep: Candidate | None = None
    best_multisegment: Candidate | None = None
    cut_count = 0
    for cuts in itertools.combinations(range(1, denominator), bands - 1):
        if required_cut is not None and required_cut not in cuts:
            continue
        cut_count += 1
        signatures = coarsen_signatures(atomic, cuts)
        for w in weights:
            count, level = modal_nonzero_fiber(signatures, w)
            if level == 0:
                # All nonzero entries of w lie in empty prime bands.
                continue
            c = Candidate(count, denominator, cuts, w, level)
            effective = effective_atomic_weights(cuts, w, occupied_bins)
            ident = projective_fiber_key(effective, level)
            if ident in seen:
                continue
            seen.add(ident)
            if not is_upper_step(effective):
                if best_nonstep is None or candidate_sort_key(c) < candidate_sort_key(best_nonstep):
                    best_nonstep = c
            if len(compressed_values(effective)) >= 3:
                if best_multisegment is None or candidate_sort_key(c) < candidate_sort_key(best_multisegment):
                    best_multisegment = c
            # heap key is ordered so the worst retained item is smallest.
            goodness = (c.count, tuple(-x for x in cuts), tuple(-x for x in w), -abs(level), -level)
            item = (goodness, c)
            if len(heap) < top:
                heapq.heappush(heap, item)
            elif goodness > heap[0][0]:
                heapq.heapreplace(heap, item)
    winners = sorted((c for _, c in heap), key=candidate_sort_key)
    assert best_nonstep is not None and best_multisegment is not None
    return (
        winners,
        best_nonstep,
        best_multisegment,
        atomic_types,
        cut_count,
        len(weights),
        len(seen),
    )


def search_binary_window(
    n: int,
    spf: Sequence[int],
    primes: Sequence[int],
    denominator: int,
    lo: int,
    hi: int,
    top: int,
) -> Tuple[List[Candidate], Candidate, Candidate, int, int]:
    """Exhaust binary weights on atomic bins [lo,hi), with 0 below and 1 above."""
    if not (0 <= lo < hi <= denominator):
        raise ValueError("binary window must satisfy 0 <= lo < hi <= denominator")
    width = hi - lo
    if width > 20:
        raise ValueError("binary window width above 20 is intentionally refused")
    pbin = atom_bins(primes, n, denominator)
    occupied_bins = sorted(set(pbin.values()))
    atomic, atomic_types = atomic_signature_counts(n, spf, pbin, denominator)
    mask_count = 1 << width

    # Accumulate every mask in one pass.  The recurrence removes the extra
    # factor width that a separate dot product per (signature,mask) would use.
    histograms: List[Counter[int]] = [Counter() for _ in range(mask_count)]
    for digits, multiplicity in atomic:
        base = sum(digits[hi:])
        scores = [0] * mask_count
        scores[0] = base
        if base:
            histograms[0][base] += multiplicity
        for mask in range(1, mask_count):
            least = mask & -mask
            j = least.bit_length() - 1
            score = scores[mask ^ least] + digits[lo + j]
            scores[mask] = score
            if score:
                histograms[mask][score] += multiplicity

    cuts = tuple(range(1, denominator))
    candidates: List[Candidate] = []
    seen = set()
    for mask, levels in enumerate(histograms):
        if not levels:
            continue
        level, count = min(
            levels.items(), key=lambda kv: (-kv[1], abs(kv[0]), kv[0])
        )
        weights = [0] * denominator
        for j in range(lo, hi):
            weights[j] = (mask >> (j - lo)) & 1
        for j in range(hi, denominator):
            weights[j] = 1
        w = tuple(weights)
        effective = tuple(w[j] for j in occupied_bins)
        key = projective_fiber_key(effective, level)
        if key in seen:
            continue
        seen.add(key)
        candidates.append(Candidate(count, denominator, cuts, w, level))

    candidates.sort(key=candidate_sort_key)
    nonstep = next(
        c
        for c in candidates
        if not is_upper_step(tuple(c.weights[j] for j in occupied_bins))
    )
    multisegment = next(
        c
        for c in candidates
        if len(compressed_values(tuple(c.weights[j] for j in occupied_bins))) >= 3
    )
    return candidates[:top], nonstep, multisegment, atomic_types, len(seen)


def search_ternary_window(
    n: int,
    spf: Sequence[int],
    primes: Sequence[int],
    denominator: int,
    lo: int,
    hi: int,
    top: int,
) -> Tuple[List[Candidate], Candidate, Candidate, int, int]:
    """Exhaust weights {-1,0,1} on [lo,hi), with 0 below and 1 above."""
    if not (0 <= lo < hi <= denominator):
        raise ValueError("ternary window must satisfy 0 <= lo < hi <= denominator")
    width = hi - lo
    if width > 12:
        raise ValueError("ternary window width above 12 is intentionally refused")
    pbin = atom_bins(primes, n, denominator)
    occupied_bins = sorted(set(pbin.values()))
    atomic, atomic_types = atomic_signature_counts(n, spf, pbin, denominator)
    state_count = 3**width

    # State trits encode 0, +1, -1.  Removing the least significant nonzero
    # trit produces a smaller state, giving one-addition score recurrence.
    parent = [0] * state_count
    position = [0] * state_count
    coefficient = [0] * state_count
    powers = [3**j for j in range(width)]
    for state in range(1, state_count):
        for j, power in enumerate(powers):
            digit = (state // power) % 3
            if digit:
                parent[state] = state - digit * power
                position[state] = j
                coefficient[state] = 1 if digit == 1 else -1
                break

    histograms: List[Counter[int]] = [Counter() for _ in range(state_count)]
    for digits, multiplicity in atomic:
        base_score = sum(digits[hi:])
        scores = [0] * state_count
        scores[0] = base_score
        if base_score:
            histograms[0][base_score] += multiplicity
        for state in range(1, state_count):
            score = (
                scores[parent[state]]
                + coefficient[state] * digits[lo + position[state]]
            )
            scores[state] = score
            if score:
                histograms[state][score] += multiplicity

    cuts = tuple(range(1, denominator))
    candidates: List[Candidate] = []
    seen = set()
    value = (0, 1, -1)
    for state, levels in enumerate(histograms):
        if not levels:
            continue
        level, count = min(
            levels.items(), key=lambda kv: (-kv[1], abs(kv[0]), kv[0])
        )
        weights = [0] * denominator
        x = state
        for j in range(lo, hi):
            weights[j] = value[x % 3]
            x //= 3
        for j in range(hi, denominator):
            weights[j] = 1
        w = tuple(weights)
        effective = tuple(w[j] for j in occupied_bins)
        key = projective_fiber_key(effective, level)
        if key in seen:
            continue
        seen.add(key)
        candidates.append(Candidate(count, denominator, cuts, w, level))

    candidates.sort(key=candidate_sort_key)
    nonstep = next(
        c
        for c in candidates
        if not is_upper_step(tuple(c.weights[j] for j in occupied_bins))
    )
    multisegment = next(
        c
        for c in candidates
        if len(compressed_values(tuple(c.weights[j] for j in occupied_bins))) >= 3
    )
    return candidates[:top], nonstep, multisegment, atomic_types, len(seen)


def top_two_prime_factors(m: int, spf: Sequence[int]) -> Tuple[int, int]:
    """Largest and second largest prime factors, with multiplicity; 1 if absent."""
    largest = second = 1
    while m > 1:
        p = spf[m]
        if p >= largest:
            second, largest = largest, p
        elif p > second:
            second = p
        m //= p
    return largest, second


def best_threshold(n: int, spf: Sequence[int]) -> Tuple[int, int]:
    """Best exact count of {m<=N: Omega_{p>y}(m)=1}, over integer y."""
    diff = [0] * (n + 2)
    for m in range(2, n + 1):
        largest, second = top_two_prime_factors(m, spf)
        # Exactly one prime factor (with multiplicity) exceeds y iff
        # second <= y < largest.
        diff[second] += 1
        diff[largest] -= 1
    running = 0
    best_count = -1
    best_y = 1
    for y in range(1, n + 1):
        running += diff[y]
        if running > best_count:
            best_count, best_y = running, y
    # Independent direct recount of the winning cutoff.
    direct = 0
    for m in range(2, n + 1):
        x = m
        omega = 0
        while x > 1:
            p = spf[x]
            if p > best_y:
                omega += 1
            x //= p
        direct += omega == 1
    assert direct == best_count
    return best_count, best_y


def band_of_prime(p: int, n: int, denominator: int, cuts: Tuple[int, ...]) -> int:
    pd = p**denominator
    for j, k in enumerate(cuts):
        if pd <= n**k:
            return j
    return len(cuts)


def score_integer(
    m: int,
    spf: Sequence[int],
    n: int,
    denominator: int,
    cuts: Tuple[int, ...],
    weights: Tuple[int, ...],
) -> int:
    score = 0
    while m > 1:
        p = spf[m]
        score += weights[band_of_prime(p, n, denominator, cuts)]
        m //= p
    return score


def candidate_members(n: int, spf: Sequence[int], c: Candidate) -> List[int]:
    members = [
        m
        for m in range(1, n + 1)
        if score_integer(m, spf, n, c.denominator, c.cuts, c.weights) == c.level
    ]
    assert len(members) == c.count
    assert c.level != 0
    return members


def factor_row(m: int, spf: Sequence[int], prime_index: Dict[int, int]) -> Dict[int, Fraction]:
    row: Dict[int, Fraction] = {}
    while m > 1:
        p = spf[m]
        j = prime_index[p]
        row[j] = row.get(j, Fraction(0)) + 1
        m //= p
    return row


def exact_sparse_rank(rows: Iterable[Dict[int, Fraction]]) -> int:
    """Exact row rank over Q by deterministic sparse Gauss-Jordan reduction."""
    basis: Dict[int, Dict[int, Fraction]] = {}
    for source in rows:
        row = {j: Fraction(x) for j, x in source.items() if x}
        while row:
            pivot = min(row)
            if pivot not in basis:
                scale = row[pivot]
                row = {j: x / scale for j, x in row.items()}
                basis[pivot] = row
                break
            q = row[pivot]
            old = basis[pivot]
            for j, x in old.items():
                new = row.get(j, Fraction(0)) - q * x
                if new:
                    row[j] = new
                elif j in row:
                    del row[j]
    return len(basis)


def exact_rank_check(
    members: Sequence[int], spf: Sequence[int], primes: Sequence[int], limit: int
) -> Tuple[int, int, int]:
    """Compute rank(V) and rank([V|1]) exactly on members <= limit."""
    small = [m for m in members if m <= limit]
    relevant_primes = [p for p in primes if p <= limit]
    pindex = {p: j for j, p in enumerate(relevant_primes)}
    rows = [factor_row(m, spf, pindex) for m in small]
    rank_v = exact_sparse_rank(rows)
    augmented = []
    last = len(relevant_primes)
    for row in rows:
        r = dict(row)
        r[last] = Fraction(1)
        augmented.append(r)
    rank_aug = exact_sparse_rank(augmented)
    assert rank_v == rank_aug
    return len(small), rank_v, rank_aug


def format_fraction_cuts(c: Candidate) -> str:
    if len(c.cuts) > 8 and c.cuts == tuple(range(1, c.denominator)):
        return f"all_atomic_cuts/denominator={c.denominator}"
    return "[" + ",".join(f"{k}/{c.denominator}" for k in c.cuts) + "]"


def format_weight_description(c: Candidate) -> str:
    if len(c.weights) <= 8:
        return f"weights={list(c.weights)}"
    runs = [(0, c.weights[0])]
    for j in range(1, len(c.weights)):
        if c.weights[j] != c.weights[j - 1]:
            runs.append((j, c.weights[j]))
    return "weight_runs=" + str(runs) + f"/denominator={c.denominator}"


def parse_config(text: str) -> Tuple[int, int, int, int | None]:
    try:
        fields = tuple(int(x) for x in text.split(":"))
        if len(fields) == 3:
            bands, denominator, bound = fields
            required = None
        elif len(fields) == 4:
            bands, denominator, bound, required = fields
        else:
            raise ValueError
    except Exception as exc:  # pragma: no cover - command-line guard
        raise argparse.ArgumentTypeError(
            "config must be BANDS:DENOMINATOR:WEIGHT_BOUND[:REQUIRED_CUT]"
        ) from exc
    if bands < 2 or denominator < bands or bound < 1:
        raise argparse.ArgumentTypeError("need bands>=2, denominator>=bands, weight bound>=1")
    if required is not None and not (1 <= required < denominator):
        raise argparse.ArgumentTypeError("required cut must lie strictly between 0 and denominator")
    return bands, denominator, bound, required


def parse_binary_window(text: str) -> Tuple[int, int, int]:
    try:
        denominator, lo, hi = (int(x) for x in text.split(":"))
    except Exception as exc:  # pragma: no cover - command-line guard
        raise argparse.ArgumentTypeError("binary window must be DENOMINATOR:LO:HI") from exc
    if denominator < 2 or not (0 <= lo < hi <= denominator) or hi - lo > 20:
        raise argparse.ArgumentTypeError(
            "need denominator>=2, 0<=lo<hi<=denominator, and width<=20"
        )
    return denominator, lo, hi


def parse_ternary_window(text: str) -> Tuple[int, int, int]:
    try:
        denominator, lo, hi = (int(x) for x in text.split(":"))
    except Exception as exc:  # pragma: no cover - command-line guard
        raise argparse.ArgumentTypeError("ternary window must be DENOMINATOR:LO:HI") from exc
    if denominator < 2 or not (0 <= lo < hi <= denominator) or hi - lo > 12:
        raise argparse.ArgumentTypeError(
            "need denominator>=2, 0<=lo<hi<=denominator, and width<=12"
        )
    return denominator, lo, hi


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--N", type=int, default=100_000)
    parser.add_argument(
        "--config",
        action="append",
        type=parse_config,
        help="BANDS:DENOMINATOR:WEIGHT_BOUND[:REQUIRED_CUT]; repeatable",
    )
    parser.add_argument("--top", type=int, default=12)
    parser.add_argument(
        "--binary-window",
        action="append",
        type=parse_binary_window,
        help="DENOMINATOR:LO:HI; binary weights free on [LO,HI), 0 below, 1 above",
    )
    parser.add_argument(
        "--ternary-window",
        action="append",
        type=parse_ternary_window,
        help="DENOMINATOR:LO:HI; weights -1,0,1 free on [LO,HI), 0 below, 1 above",
    )
    parser.add_argument(
        "--rank-n",
        type=int,
        default=450,
        help="exact-Q rank check on the winning fiber restricted to this initial segment",
    )
    args = parser.parse_args()
    if args.N < 2 or args.top < 1 or args.rank_n < 2:
        parser.error("N, top, and rank-n must be positive and nontrivial")
    configs = (
        args.config
        if args.config is not None
        else (
            []
            if args.binary_window or args.ternary_window
            else [(3, 31, 5, None), (4, 31, 3, 11)]
        )
    )
    binary_windows = args.binary_window or []
    ternary_windows = args.ternary_window or []

    started = time.perf_counter()
    spf, primes = sieve_spf(args.N)
    threshold_count, threshold_y = best_threshold(args.N, spf)
    print(f"N={args.N} primes={len(primes)}")
    print(
        "THRESHOLD "
        f"cutoff_y={threshold_y} count={threshold_count} "
        f"density={threshold_count / args.N:.9f}"
    )
    print("ASYMPTOTIC_THRESHOLD_REFERENCE c_star=0.828499...")

    all_winners: List[Candidate] = []
    all_multisegment: List[Candidate] = []
    for bands, denominator, bound, required_cut in configs:
        t0 = time.perf_counter()
        (
            winners,
            best_nonstep,
            best_multisegment,
            atom_types,
            cut_count,
            weight_count,
            distinct_fibers,
        ) = search_config(
            args.N, spf, primes, bands, denominator, bound, required_cut, args.top
        )
        all_winners.extend(winners)
        all_multisegment.append(best_multisegment)
        best = winners[0]
        print(
            "CONFIG "
            f"bands={bands} denominator={denominator} weight_bound={bound} "
            f"required_cut={required_cut} "
            f"cuts_tested={cut_count} weights_tested={weight_count} "
            f"candidates={cut_count * weight_count} atomic_types={atom_types} "
            f"distinct_projective_fibers={distinct_fibers} "
            f"seconds={time.perf_counter() - t0:.3f}"
        )
        print(
            "CONFIG_BEST "
            f"count={best.count} density={best.count / args.N:.9f} "
            f"delta_vs_threshold={best.count - threshold_count} "
            f"cuts={format_fraction_cuts(best)} {format_weight_description(best)} "
            f"level={best.level}"
        )
        print(
            "BEST_NON_UPPER_STEP "
            f"count={best_nonstep.count} density={best_nonstep.count / args.N:.9f} "
            f"delta_vs_threshold={best_nonstep.count - threshold_count} "
            f"cuts={format_fraction_cuts(best_nonstep)} "
            f"{format_weight_description(best_nonstep)} level={best_nonstep.level}"
        )
        print(
            "BEST_AT_LEAST_THREE_SEGMENTS "
            f"count={best_multisegment.count} "
            f"density={best_multisegment.count / args.N:.9f} "
            f"delta_vs_threshold={best_multisegment.count - threshold_count} "
            f"cuts={format_fraction_cuts(best_multisegment)} "
            f"{format_weight_description(best_multisegment)} level={best_multisegment.level}"
        )

    for denominator, lo, hi in binary_windows:
        t0 = time.perf_counter()
        winners, best_nonstep, best_multisegment, atom_types, distinct_fibers = (
            search_binary_window(
                args.N, spf, primes, denominator, lo, hi, args.top
            )
        )
        all_winners.extend(winners)
        all_multisegment.append(best_multisegment)
        best = winners[0]
        print(
            "BINARY_WINDOW "
            f"denominator={denominator} lo={lo} hi={hi} "
            f"masks_tested={1 << (hi - lo)} atomic_types={atom_types} "
            f"distinct_projective_fibers={distinct_fibers} "
            f"seconds={time.perf_counter() - t0:.3f}"
        )
        print(
            "BINARY_WINDOW_BEST "
            f"count={best.count} density={best.count / args.N:.9f} "
            f"delta_vs_threshold={best.count - threshold_count} "
            f"{format_weight_description(best)} level={best.level}"
        )
        print(
            "BINARY_WINDOW_BEST_MULTISEGMENT "
            f"count={best_multisegment.count} "
            f"density={best_multisegment.count / args.N:.9f} "
            f"delta_vs_threshold={best_multisegment.count - threshold_count} "
            f"{format_weight_description(best_multisegment)} "
            f"level={best_multisegment.level}"
        )

    for denominator, lo, hi in ternary_windows:
        t0 = time.perf_counter()
        winners, best_nonstep, best_multisegment, atom_types, distinct_fibers = (
            search_ternary_window(
                args.N, spf, primes, denominator, lo, hi, args.top
            )
        )
        all_winners.extend(winners)
        all_multisegment.append(best_multisegment)
        best = winners[0]
        print(
            "TERNARY_WINDOW "
            f"denominator={denominator} lo={lo} hi={hi} "
            f"states_tested={3 ** (hi - lo)} atomic_types={atom_types} "
            f"distinct_projective_fibers={distinct_fibers} "
            f"seconds={time.perf_counter() - t0:.3f}"
        )
        print(
            "TERNARY_WINDOW_BEST "
            f"count={best.count} density={best.count / args.N:.9f} "
            f"delta_vs_threshold={best.count - threshold_count} "
            f"{format_weight_description(best)} level={best.level}"
        )
        print(
            "TERNARY_WINDOW_BEST_MULTISEGMENT "
            f"count={best_multisegment.count} "
            f"density={best_multisegment.count / args.N:.9f} "
            f"delta_vs_threshold={best_multisegment.count - threshold_count} "
            f"{format_weight_description(best_multisegment)} "
            f"level={best_multisegment.level}"
        )

    ranked = sorted(all_winners, key=candidate_sort_key)
    # Eliminate exact duplicates that can arise only if a config was repeated.
    unique: List[Candidate] = []
    used = set()
    for c in ranked:
        if c.identity() not in used:
            used.add(c.identity())
            unique.append(c)
        if len(unique) == args.top:
            break
    print(f"RANKING top={len(unique)}")
    for j, c in enumerate(unique, 1):
        print(
            f"{j:02d} count={c.count} density={c.count / args.N:.9f} "
            f"delta={c.count - threshold_count:+d} cuts={format_fraction_cuts(c)} "
            f"{format_weight_description(c)} level={c.level}"
        )

    winner = unique[0]
    members = candidate_members(args.N, spf, winner)
    # This is an exact consistency/rank-equality certificate on the full set:
    # V_A * (w_p / level) = 1.  Re-evaluation above is deliberately separate
    # from the signature aggregation used by the search.
    cert_ok = all(
        score_integer(m, spf, args.N, winner.denominator, winner.cuts, winner.weights)
        == winner.level
        for m in members
    )
    assert cert_ok
    rank_limit = min(args.N, args.rank_n)
    rank_rows, rank_v, rank_aug = exact_rank_check(members, spf, primes, rank_limit)
    print(
        "CERTIFICATE exact_full_rank_equality=PASS "
        f"equation=V*(weights/level)=1 members={len(members)}"
    )
    print(
        "EXACT_Q_RANK_CHECK "
        f"restriction_max_n={rank_limit} rows={rank_rows} "
        f"rank_V={rank_v} rank_augmented={rank_aug} result=PASS"
    )

    genuine = min(all_multisegment, key=candidate_sort_key)
    genuine_members = candidate_members(args.N, spf, genuine)
    genuine_cert_ok = all(
        score_integer(
            m,
            spf,
            args.N,
            genuine.denominator,
            genuine.cuts,
            genuine.weights,
        )
        == genuine.level
        for m in genuine_members
    )
    assert genuine_cert_ok
    g_rows, g_rank_v, g_rank_aug = exact_rank_check(
        genuine_members, spf, primes, rank_limit
    )
    print(
        "MULTIBAND_CERTIFICATE exact_full_rank_equality=PASS "
        f"count={genuine.count} cuts={format_fraction_cuts(genuine)} "
        f"{format_weight_description(genuine)} level={genuine.level} "
        "equation=V*(weights/level)=1"
    )
    print(
        "MULTIBAND_EXACT_Q_RANK_CHECK "
        f"restriction_max_n={rank_limit} rows={g_rows} "
        f"rank_V={g_rank_v} rank_augmented={g_rank_aug} result=PASS"
    )
    print(f"TOTAL_SECONDS {time.perf_counter() - started:.3f}")


if __name__ == "__main__":
    main()
