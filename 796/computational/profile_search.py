#!/usr/bin/env python3
"""Exact finite search for compatible large-prime multiplier profiles.

For a large prime label p and a multiplier profile V, the lifted elements are
    p V = {p*v : v in V}.
If p != q, representations with label multiset {p,q} are counted by the
*ordered* pairs (v,w) in V x W having a fixed product.  If p=q, they are
instead unordered pairs of distinct multipliers in V.  This program searches
for one repeatable profile V_k subset [k] for every 1 <= k <= K.

The asymptotic weight of V_k is 1/(k(k+1)): primes p with floor(n/p)=k
have this density on the n/log(n) scale.  The optional canonical-tail anchor
requires compatibility with {1} union {primes <= K}; this is exactly the
condition needed for compatibility with every canonical tail profile.

Only the Python standard library is used.  All choices and tie breaks are
deterministic.
"""

from __future__ import annotations

import argparse
import itertools
import math
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


def primes_up_to(n: int) -> Tuple[int, ...]:
    """Return the primes at most n by deterministic trial division."""
    out: List[int] = []
    for x in range(2, n + 1):
        if all(x % p for p in out if p * p <= x):
            out.append(x)
    return tuple(out)


def mask_values(mask: int) -> Tuple[int, ...]:
    """Decode bit i as the integer i+1."""
    return tuple(i + 1 for i in range(mask.bit_length()) if mask & (1 << i))


def values_mask(values: Iterable[int]) -> int:
    mask = 0
    for value in values:
        if value < 1:
            raise ValueError("profile values must be positive")
        mask |= 1 << (value - 1)
    return mask


def ordered_product_counts(left: int, right: int) -> Counter[int]:
    """Counts (a,b) in left x right by ab; orientation is retained."""
    return Counter(a * b for a in mask_values(left) for b in mask_values(right))


def same_label_product_counts(profile: int) -> Counter[int]:
    """Counts unordered {a,b} subset V with a != b by ab."""
    return Counter(
        a * b for a, b in itertools.combinations(mask_values(profile), 2)
    )


def independently_ordered_compatible(left: int, right: int) -> bool:
    """Slow, deliberately separate implementation used in validation."""
    products: List[int] = []
    for a in mask_values(left):
        for b in mask_values(right):
            products.append(a * b)
    return all(products.count(product) <= 2 for product in set(products))


class CompatibilityOracle:
    """Memoized exact ordered cross-compatibility oracle."""

    def __init__(self) -> None:
        self.cache: Dict[Tuple[int, int], bool] = {}
        self.calls = 0
        self.misses = 0

    def compatible(self, left: int, right: int) -> bool:
        self.calls += 1
        key = (left, right) if left <= right else (right, left)
        answer = self.cache.get(key)
        if answer is not None:
            return answer
        self.misses += 1
        counts: Dict[int, int] = {}
        for a in mask_values(key[0]):
            for b in mask_values(key[1]):
                product = a * b
                count = counts.get(product, 0) + 1
                if count > 2:
                    self.cache[key] = False
                    return False
                counts[product] = count
        self.cache[key] = True
        return True


def repeatable_profiles(max_k: int, oracle: CompatibilityOracle) -> List[int]:
    """Profiles that can be assigned to two distinct large-prime labels."""
    profiles: List[int] = []
    for mask in range(1 << max_k):
        if oracle.compatible(mask, mask):
            # A same-label representation is weaker but checked independently:
            # C(V,V;t) = 2*S(V;t) + 1_{t=a^2 for some a in V}.
            same = same_label_product_counts(mask)
            if max(same.values(), default=0) > 2:
                raise AssertionError("ordered-repeatable profile failed self check")
            profiles.append(mask)
    return profiles


def canonical_mask(k: int) -> int:
    return values_mask((1, *primes_up_to(k)))


def format_profile(mask: int) -> str:
    return "{" + ",".join(map(str, mask_values(mask))) + "}"


@dataclass(frozen=True)
class SearchResult:
    max_k: int
    tail_anchored: bool
    scale: int
    scaled_score: int
    solution: Mapping[int, int]
    nodes: int
    pruned_by_bound: int
    pruned_empty: int
    elapsed_seconds: float

    @property
    def score(self) -> Fraction:
        return Fraction(self.scaled_score, self.scale)


class ProfileOptimizer:
    """Exact weighted multipartite-clique branch-and-bound search."""

    def __init__(
        self,
        max_k: int,
        oracle: CompatibilityOracle,
        repeatable: Sequence[int],
        tail_anchored: bool,
    ) -> None:
        self.max_k = max_k
        self.oracle = oracle
        self.tail_anchored = tail_anchored
        self.anchor = canonical_mask(max_k)
        self.levels = tuple(range(1, max_k + 1))
        self.scale = math.lcm(*(k * (k + 1) for k in self.levels))
        self.weights = {k: self.scale // (k * (k + 1)) for k in self.levels}

        domains: Dict[int, Tuple[int, ...]] = {}
        for k in self.levels:
            upper = 1 << k
            candidates = [mask for mask in repeatable if mask < upper]
            if tail_anchored:
                candidates = [
                    mask
                    for mask in candidates
                    if self.oracle.compatible(mask, self.anchor)
                ]
            # Larger sets first finds strong incumbents; numeric mask breaks ties.
            candidates.sort(key=lambda mask: (-mask.bit_count(), mask))
            domains[k] = tuple(candidates)
        self.root_domains = domains

        baseline = {k: canonical_mask(k) for k in self.levels}
        self._assert_feasible_solution(baseline)
        self.best_solution: Dict[int, int] = baseline
        self.best_score = self._score(baseline)
        self.nodes = 0
        self.pruned_by_bound = 0
        self.pruned_empty = 0

    def _score(self, solution: Mapping[int, int]) -> int:
        return sum(
            solution[k].bit_count() * self.weights[k] for k in solution
        )

    def _assert_feasible_solution(self, solution: Mapping[int, int]) -> None:
        for k, mask in solution.items():
            if mask >= 1 << k:
                raise AssertionError("profile is not a subset of its level")
            if not self.oracle.compatible(mask, mask):
                raise AssertionError("profile is not repeatable")
            if self.tail_anchored and not self.oracle.compatible(mask, self.anchor):
                raise AssertionError("profile is not compatible with tail anchor")
        for k, ell in itertools.combinations(solution, 2):
            if not self.oracle.compatible(solution[k], solution[ell]):
                raise AssertionError("profiles are not pairwise compatible")

    def _upper_bound(
        self, current_score: int, domains: Mapping[int, Sequence[int]]
    ) -> int:
        return current_score + sum(
            max(mask.bit_count() for mask in domain) * self.weights[k]
            for k, domain in domains.items()
        )

    def _choose_level(self, domains: Mapping[int, Sequence[int]]) -> int:
        # Minimum remaining values, then larger weight, then smaller k.
        return min(domains, key=lambda k: (len(domains[k]), -self.weights[k], k))

    def _dfs(
        self,
        chosen: Dict[int, int],
        domains: Mapping[int, Sequence[int]],
        current_score: int,
    ) -> None:
        self.nodes += 1
        if not domains:
            if current_score > self.best_score:
                self.best_score = current_score
                self.best_solution = dict(chosen)
            return
        if self._upper_bound(current_score, domains) <= self.best_score:
            self.pruned_by_bound += 1
            return

        level = self._choose_level(domains)
        remaining_levels = tuple(k for k in domains if k != level)
        for mask in domains[level]:
            next_score = current_score + mask.bit_count() * self.weights[level]
            next_domains: Dict[int, Tuple[int, ...]] = {}
            impossible = False
            for k in remaining_levels:
                filtered = tuple(
                    other
                    for other in domains[k]
                    if self.oracle.compatible(mask, other)
                )
                if not filtered:
                    impossible = True
                    self.pruned_empty += 1
                    break
                next_domains[k] = filtered
            if impossible:
                continue
            if self._upper_bound(next_score, next_domains) <= self.best_score:
                self.pruned_by_bound += 1
                continue
            chosen[level] = mask
            self._dfs(chosen, next_domains, next_score)
            del chosen[level]

    def run(self) -> SearchResult:
        start = time.perf_counter()
        self._dfs({}, self.root_domains, 0)
        elapsed = time.perf_counter() - start
        self._assert_feasible_solution(self.best_solution)
        return SearchResult(
            max_k=self.max_k,
            tail_anchored=self.tail_anchored,
            scale=self.scale,
            scaled_score=self.best_score,
            solution=dict(sorted(self.best_solution.items())),
            nodes=self.nodes,
            pruned_by_bound=self.pruned_by_bound,
            pruned_empty=self.pruned_empty,
            elapsed_seconds=elapsed,
        )


def baseline_weight(max_k: int) -> Fraction:
    return sum(
        (Fraction(canonical_mask(k).bit_count(), k * (k + 1))
         for k in range(1, max_k + 1)),
        Fraction(),
    )


def exhaustive_small_optimum(max_k: int, tail_anchored: bool) -> Fraction:
    """Independent Cartesian-product enumeration, intended only for K <= 5."""
    if max_k > 5:
        raise ValueError("independent exhaustive check is restricted to K <= 5")
    anchor = canonical_mask(max_k)
    domains: List[List[int]] = []
    for k in range(1, max_k + 1):
        level: List[int] = []
        for mask in range(1 << k):
            if not independently_ordered_compatible(mask, mask):
                continue
            if tail_anchored and not independently_ordered_compatible(mask, anchor):
                continue
            level.append(mask)
        domains.append(level)

    best = Fraction(-1)
    for profiles in itertools.product(*domains):
        if any(
            not independently_ordered_compatible(profiles[i], profiles[j])
            for i in range(max_k)
            for j in range(i + 1, max_k)
        ):
            continue
        score = sum(
            (Fraction(mask.bit_count(), k * (k + 1))
             for k, mask in enumerate(profiles, 1)),
            Fraction(),
        )
        if score > best:
            best = score
    return best


def next_primes_after(bound: int, count: int) -> Tuple[int, ...]:
    primes: List[int] = []
    x = bound + 1
    while len(primes) < count:
        divisor = 2
        prime = x >= 2
        while divisor * divisor <= x and prime:
            if x % divisor == 0:
                prime = False
            divisor += 1
        if prime:
            primes.append(x)
        x += 1
    return tuple(primes)


def direct_lift_validation(solution: Mapping[int, int]) -> Tuple[int, int, int]:
    """Independently enumerate pair products after two prime lifts per level."""
    max_k = max(solution, default=1)
    labels = iter(next_primes_after(max_k, 2 * len(solution)))
    lifted: List[int] = []
    for k in sorted(solution):
        for _ in range(2):
            label = next(labels)
            lifted.extend(label * value for value in mask_values(solution[k]))
    if len(lifted) != len(set(lifted)):
        raise AssertionError("distinct formal lifts unexpectedly coincided")
    counts = Counter(a * b for a, b in itertools.combinations(lifted, 2))
    maximum = max(counts.values(), default=0)
    if maximum > 2:
        bad = next(product for product, count in counts.items() if count > 2)
        raise AssertionError(f"direct lifted validation failed at product {bad}")
    return len(lifted), len(counts), maximum


def explicit_infinite_profile_validation() -> None:
    """Certify the finite core of the C0/C1/C2 profile in PROOF.md.

    Every member at least 17 is a prime occurring as a singleton.  In an
    equality of two cross-products, such a prime is forced to occur on both
    sides in the same way unless both sides consist of two large primes; that
    case has only the two swapped orientations.  It therefore suffices to
    check the displayed elements below 17.
    """
    cores = (
        values_mask((1, 2, 3, 5, 7, 11, 13)),
        values_mask((1, 3, 4, 5, 6, 7, 11, 13)),
        values_mask((1, 2, 5, 7, 8, 9, 11, 12, 13, 15)),
    )
    for i in range(3):
        for j in range(i, 3):
            counts = ordered_product_counts(cores[i], cores[j])
            maximum = max(counts.values(), default=0)
            if maximum > 2:
                bad = next(product for product, count in counts.items() if count > 2)
                raise AssertionError(
                    f"C{i},C{j} finite core fails at product {bad}"
                )
    gain = (
        Fraction(1, 6) - Fraction(1, 12)
        + 2 * (Fraction(1, 12) - Fraction(1, 15))
        + 3 * Fraction(1, 15)
    )
    if gain != Fraction(19, 60):
        raise AssertionError("explicit profile gain arithmetic failed")
    print("explicit_C0_C1_C2_core: max_cross_multiplicity=2 gain=19/60 PASS")


def validate_result(result: SearchResult, oracle: CompatibilityOracle) -> None:
    solution = result.solution
    for k, mask in solution.items():
        if not independently_ordered_compatible(mask, mask):
            raise AssertionError(f"independent repeatability failure at k={k}")
        if max(same_label_product_counts(mask).values(), default=0) > 2:
            raise AssertionError(f"same-label failure at k={k}")
        if result.tail_anchored and not independently_ordered_compatible(
            mask, canonical_mask(result.max_k)
        ):
            raise AssertionError(f"independent tail-anchor failure at k={k}")
    for k, ell in itertools.combinations(solution, 2):
        if not independently_ordered_compatible(solution[k], solution[ell]):
            raise AssertionError(f"independent cross failure at {k},{ell}")
        if not oracle.compatible(solution[k], solution[ell]):
            raise AssertionError("oracle and independent checker disagree")


def print_result(result: SearchResult) -> None:
    base = baseline_weight(result.max_k)
    gain = result.score - base
    mode = "tail-anchored" if result.tail_anchored else "truncated-unanchored"
    print(f"mode={mode} K={result.max_k}")
    print(f"  optimum_weight={result.score} ({float(result.score):.12f})")
    print(f"  canonical_weight={base} ({float(base):.12f})")
    print(f"  gain_over_canonical={gain} ({float(gain):+.12f})")
    print(f"  candidate_constant=1+B_1+({gain})")
    print(
        f"  search_nodes={result.nodes} bound_prunes={result.pruned_by_bound} "
        f"empty_prunes={result.pruned_empty} runtime={result.elapsed_seconds:.6f}s"
    )
    for k, mask in result.solution.items():
        print(
            f"    k={k:2d} weight=1/{k*(k+1):3d} "
            f"size={mask.bit_count():2d} V_k={format_profile(mask)}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-k", type=int, default=10)
    parser.add_argument(
        "--mode",
        choices=("tail", "truncated", "both"),
        default="both",
        help="search with canonical tail anchor, without it, or both",
    )
    parser.add_argument(
        "--bruteforce-k",
        type=int,
        default=5,
        help="independently exhaust all profile tuples up to this K (0 disables)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 1 <= args.max_k <= 20:
        raise SystemExit("--max-k must lie in [1,20]")
    if not 0 <= args.bruteforce_k <= 5:
        raise SystemExit("--bruteforce-k must lie in [0,5]")

    total_start = time.perf_counter()
    explicit_infinite_profile_validation()
    oracle = CompatibilityOracle()
    enum_start = time.perf_counter()
    repeatable = repeatable_profiles(args.max_k, oracle)
    enum_elapsed = time.perf_counter() - enum_start
    by_level = [sum(mask < (1 << k) for mask in repeatable) for k in range(1, args.max_k + 1)]
    print(
        f"enumerated_repeatable_profiles_K={args.max_k}: {len(repeatable)} "
        f"runtime={enum_elapsed:.6f}s"
    )
    print("repeatable_counts_by_level=" + ",".join(map(str, by_level)))

    modes = []
    if args.mode in ("tail", "both"):
        modes.append(True)
    if args.mode in ("truncated", "both"):
        modes.append(False)

    results: List[SearchResult] = []
    for tail_anchored in modes:
        optimizer = ProfileOptimizer(
            args.max_k, oracle, repeatable, tail_anchored=tail_anchored
        )
        result = optimizer.run()
        validate_result(result, oracle)
        lifted_size, distinct_products, max_multiplicity = direct_lift_validation(
            result.solution
        )
        print_result(result)
        print(
            f"  independent_lift: elements={lifted_size} "
            f"distinct_pair_products={distinct_products} "
            f"max_multiplicity={max_multiplicity} PASS"
        )
        results.append(result)

    if args.bruteforce_k:
        check_k = min(args.bruteforce_k, args.max_k)
        for tail_anchored in modes:
            small_oracle = CompatibilityOracle()
            small_repeatable = repeatable_profiles(check_k, small_oracle)
            small_result = ProfileOptimizer(
                check_k,
                small_oracle,
                small_repeatable,
                tail_anchored=tail_anchored,
            ).run()
            exhaustive = exhaustive_small_optimum(check_k, tail_anchored)
            if exhaustive != small_result.score:
                raise AssertionError(
                    f"branch-and-bound {small_result.score} != exhaustive {exhaustive}"
                )
            mode = "tail-anchored" if tail_anchored else "truncated-unanchored"
            print(
                f"independent_exhaustive_K={check_k} mode={mode}: "
                f"optimum={exhaustive} PASS"
            )

    print(
        f"oracle_calls={oracle.calls} oracle_cache_misses={oracle.misses} "
        f"total_runtime={time.perf_counter()-total_start:.6f}s"
    )


if __name__ == "__main__":
    main()
