#!/usr/bin/env python3
"""Exact search for the largest nonzero additive level in [1,N].

For rational prime weights w_p, put f(n)=sum_p v_p(n)w_p.  Scaling a
nonzero level lets us take the target to be f(n)=1.  If B=floor(sqrt(N)),
then every p>B occurs to exponent one and every integer divisible by p is
uniquely p*m with 1<=m<=N/p<B.  Once the small-prime weights are fixed,
w_p can therefore be chosen independently to retain a modal value of f(m).

The remaining objective changes only on the following rational hyperplanes:

  * f(n)=1 for B-smooth n<=N; and
  * f(a)=f(b) for 1<=a<b<=max_{p>B} floor(N/p).

The recursive search eliminates one small-prime weight at a time.  At a
node, either no hyperplane involving that weight is met (the generic branch),
or at least one is met and determines that weight as an exact affine
function of the remaining weights (one branch per distinct candidate).
This is exhaustive.  All arithmetic in the search is integral/rational.

The reported level set is independently checked by exact rational ranks:
rank(V_A)=rank([V_A|1]).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple


Form = Tuple[int, ...]
Mask = int


def primes_up_to(n: int) -> List[int]:
    """Return the primes <= n by a deterministic sieve."""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (
                (n - p * p) // p + 1
            )
    return [p for p in range(2, n + 1) if sieve[p]]


def valuation_vector(n: int, primes: Sequence[int]) -> Tuple[int, ...]:
    """Prime valuations of n at the supplied primes (which may be partial)."""
    out: List[int] = []
    x = n
    for p in primes:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        out.append(e)
        if x == 1:
            out.extend([0] * (len(primes) - len(out)))
            break
    return tuple(out)


def smooth(n: int, bound: int) -> bool:
    """Whether every prime divisor of n is at most bound."""
    x = n
    for p in primes_up_to(math.isqrt(x)):
        while x % p == 0:
            x //= p
    return x == 1 or x <= bound


def gcd_many(values: Iterable[int]) -> int:
    g = 0
    for value in values:
        g = math.gcd(g, abs(value))
    return g


def lcm(a: int, b: int) -> int:
    return abs(a // math.gcd(a, b) * b) if a and b else 0


def normalize_form(values: Sequence[Fraction | int]) -> Form:
    """Canonical primitive integral representative of an affine equation."""
    den = 1
    fractions = [Fraction(v) for v in values]
    for value in fractions:
        den = lcm(den, value.denominator)
    ints = [value.numerator * (den // value.denominator) for value in fractions]
    g = gcd_many(ints)
    if g:
        ints = [value // g for value in ints]
        first = next(value for value in ints if value)
        if first < 0:
            ints = [-value for value in ints]
    return tuple(ints)


def form_value(form: Form, assignment: Mapping[int, Fraction]) -> Fraction:
    value = Fraction(form[-1])
    for i, coefficient in enumerate(form[:-1]):
        if coefficient:
            value += coefficient * assignment[i]
    return value


def substitute(form: Form, pivot: int, candidate: Form) -> Form:
    """Substitute candidate=0, solving candidate for the pivot variable."""
    a = candidate[pivot]
    assert a
    c = form[pivot]
    if not c:
        return form
    # h - (h_p/g_p)g has zero pivot coefficient.
    ratio = Fraction(c, a)
    result = [Fraction(x) - ratio * y for x, y in zip(form, candidate)]
    assert result[pivot] == 0
    return normalize_form(result)


def combine_forms(entries: Iterable[Tuple[Form, Mask]]) -> Tuple[Mask, Tuple[Tuple[Form, Mask], ...]]:
    """Combine proportional equations and separate true/false constants."""
    true_mask = 0
    groups: MutableMapping[Form, int] = defaultdict(int)
    for form, mask in entries:
        canonical = normalize_form(form)
        if not any(canonical[:-1]):
            if canonical[-1] == 0:
                true_mask |= mask
            # A nonzero constant equation is false and can be discarded.
        else:
            groups[canonical] |= mask
    return true_mask, tuple(sorted(groups.items()))


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


@dataclass(frozen=True)
class CandidateStep:
    pivot: int
    equation: Form


@dataclass(frozen=True)
class GenericStep:
    pivot: int
    forbidden: Tuple[Form, ...]


Step = CandidateStep | GenericStep


@dataclass
class SearchStats:
    nodes: int = 0
    candidate_branches: int = 0
    generic_branches: int = 0
    bound_prunes: int = 0
    duplicate_prunes: int = 0
    incumbent_updates: int = 0


class ModalSearch:
    """Branch-and-bound instance for a fixed N."""

    def __init__(self, n_max: int) -> None:
        if n_max < 2:
            raise ValueError("N must be at least 2")
        self.N = n_max
        self.B = math.isqrt(n_max)
        self.all_primes = primes_up_to(n_max)
        self.small_primes = [p for p in self.all_primes if p <= self.B]
        self.large_primes = [p for p in self.all_primes if p > self.B]
        self.k = len(self.small_primes)
        self.small_valuations = {
            n: valuation_vector(n, self.small_primes) for n in range(1, n_max + 1)
        }

        self.smooth_numbers = [
            n
            for n in range(2, n_max + 1)
            if self._is_small_smooth_from_vector(n)
        ]
        self.target_count = len(self.smooth_numbers)
        self.target_mask = (1 << self.target_count) - 1

        quotient_counts = Counter(n_max // p for p in self.large_primes)
        self.quotient_counts = tuple(sorted(quotient_counts.items()))
        self.max_cofactor = max(quotient_counts, default=0)
        self.pairs = [
            (a, b)
            for a in range(1, self.max_cofactor + 1)
            for b in range(a + 1, self.max_cofactor + 1)
        ]

        entries: List[Tuple[Form, Mask]] = []
        event = 0
        for n in self.smooth_numbers:
            # f(n)-1=0.
            form = tuple(self.small_valuations[n]) + (-1,)
            entries.append((normalize_form(form), 1 << event))
            event += 1
        self.pair_event_offset = event
        for a, b in self.pairs:
            va = self.small_valuations[a]
            vb = self.small_valuations[b]
            # f(a)-f(b)=0.
            form = tuple(x - y for x, y in zip(va, vb)) + (0,)
            entries.append((normalize_form(form), 1 << event))
            event += 1
        self.event_count = event
        initial_true, self.initial_forms = combine_forms(entries)
        assert initial_true == 0

        self.stats = SearchStats()
        self.best_score = -1
        self.best_small_weights: Tuple[Fraction, ...] | None = None
        self.best_A: Tuple[int, ...] = ()
        self.visited: set[Tuple[Tuple[int, ...], Mask, Tuple[Tuple[Form, Mask], ...]]] = set()

    def _is_small_smooth_from_vector(self, n: int) -> bool:
        product = 1
        for p, e in zip(self.small_primes, self.small_valuations[n]):
            product *= p**e
        return product == n

    @lru_cache(maxsize=None)
    def score_mask(self, true_mask: Mask) -> int:
        """Objective if precisely the recorded target/collision events hold."""
        score = (true_mask & self.target_mask).bit_count()
        pair_mask = true_mask >> self.pair_event_offset
        for maximum, multiplicity in self.quotient_counts:
            uf = UnionFind(maximum)
            bits = pair_mask
            pair_index = 0
            while bits:
                low = bits & -bits
                offset = low.bit_length() - 1
                pair_index += offset
                a, b = self.pairs[pair_index]
                if b <= maximum:
                    uf.union(a - 1, b - 1)
                bits >>= offset + 1
                pair_index += 1
            largest = max(uf.size[uf.find(i)] for i in range(maximum))
            score += multiplicity * largest
        return score

    def additive_value(self, n: int, small_weights: Sequence[Fraction]) -> Fraction:
        return sum(
            (Fraction(e) * weight for e, weight in zip(self.small_valuations[n], small_weights)),
            Fraction(0),
        )

    def complete_weights(
        self, small_weights: Sequence[Fraction]
    ) -> Tuple[Tuple[Fraction, ...], Tuple[int, ...]]:
        """Optimize every large prime modally and return all weights and A."""
        weights: Dict[int, Fraction] = dict(zip(self.small_primes, small_weights))
        modal_value: Dict[int, Fraction] = {}
        for maximum, _multiplicity in self.quotient_counts:
            counts = Counter(
                self.additive_value(m, small_weights) for m in range(1, maximum + 1)
            )
            best_count = max(counts.values())
            modal_value[maximum] = min(
                value for value, count in counts.items() if count == best_count
            )
        for p in self.large_primes:
            weights[p] = Fraction(1) - modal_value[self.N // p]
        ordered = tuple(weights[p] for p in self.all_primes)

        level: List[int] = []
        for n in range(2, self.N + 1):
            vector = valuation_vector(n, self.all_primes)
            value = sum(
                (Fraction(e) * weight for e, weight in zip(vector, ordered)),
                Fraction(0),
            )
            if value == 1:
                level.append(n)
        return ordered, tuple(level)

    def objective(self, small_weights: Sequence[Fraction]) -> int:
        return len(self.complete_weights(small_weights)[1])

    @staticmethod
    def _integer_sequence() -> Iterable[int]:
        yield 0
        for magnitude in range(1, 10**9):
            yield magnitude
            yield -magnitude

    def generic_assignment(
        self, forms: Tuple[Tuple[Form, Mask], ...], remaining: Tuple[int, ...]
    ) -> Dict[int, Fraction]:
        """A rational point avoiding every current proper hyperplane."""
        if not remaining:
            assert not forms
            return {}
        # A moment-curve specialization makes each form a nonzero polynomial
        # in t, so only finitely many t are forbidden.
        for t in self._integer_sequence():
            assignment = {
                variable: Fraction(t ** (position + 1))
                for position, variable in enumerate(remaining)
            }
            if all(form_value(form, assignment) != 0 for form, _ in forms):
                return assignment
        raise AssertionError("unreachable: finite union covered the moment curve")

    def lift_assignment(
        self, assignment: Dict[int, Fraction], history: Sequence[Step]
    ) -> Tuple[Fraction, ...]:
        """Reconstruct eliminated weights, from the newest step backwards."""
        values = dict(assignment)
        for step in reversed(history):
            if isinstance(step, CandidateStep):
                form = step.equation
                coefficient = form[step.pivot]
                rest = Fraction(form[-1])
                for i, value in values.items():
                    if i != step.pivot and form[i]:
                        rest += form[i] * value
                values[step.pivot] = -rest / coefficient
            else:
                for candidate in self._integer_sequence():
                    values[step.pivot] = Fraction(candidate)
                    if all(form_value(form, values) != 0 for form in step.forbidden):
                        break
                else:
                    raise AssertionError("unreachable generic reconstruction")
        assert len(values) == self.k
        return tuple(values[i] for i in range(self.k))

    def update_incumbent(
        self,
        forms: Tuple[Tuple[Form, Mask], ...],
        true_mask: Mask,
        remaining: Tuple[int, ...],
        history: Sequence[Step],
    ) -> None:
        assignment = self.generic_assignment(forms, remaining)
        small_weights = self.lift_assignment(assignment, history)
        all_weights, level = self.complete_weights(small_weights)
        score = len(level)
        expected = self.score_mask(true_mask)
        assert score == expected, (score, expected, small_weights, true_mask)
        small_key = tuple((x.numerator, x.denominator) for x in small_weights)
        best_key = (
            tuple((x.numerator, x.denominator) for x in self.best_small_weights)
            if self.best_small_weights is not None
            else None
        )
        if score > self.best_score or (
            score == self.best_score and (best_key is None or small_key < best_key)
        ):
            self.best_score = score
            self.best_small_weights = small_weights
            self.best_A = level
            self.stats.incumbent_updates += 1
            # all_weights is deliberately recomputed in result(), where it is
            # also checked; evaluating it here catches reconstruction errors.
            assert len(all_weights) == len(self.all_primes)

    def choose_pivot(
        self, forms: Tuple[Tuple[Form, Mask], ...], remaining: Tuple[int, ...]
    ) -> int:
        candidates = []
        for variable in remaining:
            affected = [(form, mask) for form, mask in forms if form[variable]]
            if affected:
                event_mass = sum(mask.bit_count() for _, mask in affected)
                candidates.append((len(affected), -event_mass, -self.small_primes[variable], variable))
        assert candidates
        return min(candidates)[-1]

    def child_from_candidate(
        self,
        forms: Tuple[Tuple[Form, Mask], ...],
        true_mask: Mask,
        pivot: int,
        candidate: Form,
    ) -> Tuple[Tuple[Tuple[Form, Mask], ...], Mask]:
        gained, child_forms = combine_forms(
            (substitute(form, pivot, candidate), mask) for form, mask in forms
        )
        return child_forms, true_mask | gained

    def dfs(
        self,
        forms: Tuple[Tuple[Form, Mask], ...],
        true_mask: Mask,
        remaining: Tuple[int, ...],
        history: Tuple[Step, ...],
    ) -> None:
        self.stats.nodes += 1
        key = (remaining, true_mask, forms)
        if key in self.visited:
            self.stats.duplicate_prunes += 1
            return
        self.visited.add(key)

        undecided_mask = 0
        for _form, mask in forms:
            undecided_mask |= mask
        upper = self.score_mask(true_mask | undecided_mask)
        if upper <= self.best_score:
            self.stats.bound_prunes += 1
            return

        self.update_incumbent(forms, true_mask, remaining, history)
        if not forms or not remaining:
            return

        pivot = self.choose_pivot(forms, remaining)
        child_remaining = tuple(i for i in remaining if i != pivot)
        dependent = tuple((form, mask) for form, mask in forms if form[pivot])
        independent = tuple((form, mask) for form, mask in forms if not form[pivot])

        children: List[
            Tuple[int, int, Tuple[Tuple[Form, Mask], ...], Mask, Step]
        ] = []
        # Every distinct dependent form supplies one exact candidate value.
        for candidate, _mask in dependent:
            child_forms, child_true = self.child_from_candidate(
                forms, true_mask, pivot, candidate
            )
            child_undecided = 0
            for _form, mask in child_forms:
                child_undecided |= mask
            child_upper = self.score_mask(child_true | child_undecided)
            immediate = self.score_mask(child_true)
            children.append(
                (
                    -child_upper,
                    -immediate,
                    child_forms,
                    child_true,
                    CandidateStep(pivot, candidate),
                )
            )

        # Generic value: every dependent equation is false.  Remaining
        # independent equations retain exactly their current forms.
        generic_undecided = 0
        for _form, mask in independent:
            generic_undecided |= mask
        generic_upper = self.score_mask(true_mask | generic_undecided)
        children.append(
            (
                -generic_upper,
                -self.score_mask(true_mask),
                independent,
                true_mask,
                GenericStep(pivot, tuple(form for form, _ in dependent)),
            )
        )

        # High-upper-bound candidates first give the bound an incumbent early.
        children.sort(key=lambda item: (item[0], item[1], repr(item[4])))
        for _negative_upper, _negative_immediate, child_forms, child_true, step in children:
            if isinstance(step, CandidateStep):
                self.stats.candidate_branches += 1
            else:
                self.stats.generic_branches += 1
            self.dfs(
                child_forms,
                child_true,
                child_remaining,
                history + (step,),
            )

    def seed_incumbent(self) -> None:
        """Several deterministic legal points, solely to strengthen pruning."""
        seeds = [
            tuple(Fraction(0) for _ in range(self.k)),
            tuple(Fraction(1) for _ in range(self.k)),
        ]
        for index in range(self.k):
            seed = [Fraction(0) for _ in range(self.k)]
            seed[index] = Fraction(1)
            seeds.append(tuple(seed))
        for small_weights in seeds:
            _all_weights, level = self.complete_weights(small_weights)
            score = len(level)
            key = tuple((x.numerator, x.denominator) for x in small_weights)
            best_key = (
                tuple((x.numerator, x.denominator) for x in self.best_small_weights)
                if self.best_small_weights is not None
                else None
            )
            if score > self.best_score or (
                score == self.best_score and (best_key is None or key < best_key)
            ):
                self.best_score = score
                self.best_small_weights = small_weights
                self.best_A = level
                self.stats.incumbent_updates += 1

    def run(self) -> Dict[str, object]:
        started = time.perf_counter()
        self.seed_incumbent()
        self.dfs(
            self.initial_forms,
            0,
            tuple(range(self.k)),
            (),
        )
        elapsed = time.perf_counter() - started
        assert self.best_small_weights is not None
        all_weights, level = self.complete_weights(self.best_small_weights)
        assert level == self.best_A
        rank = validate_rank(self.N, self.all_primes, level)
        assert rank[0] == rank[1]
        return {
            "N": self.N,
            "maximum": self.best_score,
            "density_over_N": self.best_score / self.N,
            "small_prime_bound": self.B,
            "small_primes": self.small_primes,
            "small_weights": [fraction_string(x) for x in self.best_small_weights],
            "weights": {
                str(p): fraction_string(w) for p, w in zip(self.all_primes, all_weights)
            },
            "level_set": list(level),
            "rank_V": rank[0],
            "rank_augmented": rank[1],
            "events": self.event_count,
            "distinct_root_forms": len(self.initial_forms),
            "nodes": self.stats.nodes,
            "candidate_branches": self.stats.candidate_branches,
            "generic_branches": self.stats.generic_branches,
            "bound_prunes": self.stats.bound_prunes,
            "duplicate_prunes": self.stats.duplicate_prunes,
            "incumbent_updates": self.stats.incumbent_updates,
            "elapsed_seconds": elapsed,
        }


def fraction_string(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def rational_rank(matrix: Sequence[Sequence[int]]) -> int:
    """Exact Gaussian rank over Q (independent of the search algebra)."""
    if not matrix:
        return 0
    rows = [[Fraction(value) for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(row_count):
            if row != pivot_row and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    value - factor * pivot_entry
                    for value, pivot_entry in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def validate_rank(
    n_max: int, primes: Sequence[int], level_set: Sequence[int]
) -> Tuple[int, int]:
    """Return the two exact ranks in the finite grading criterion."""
    assert all(2 <= n <= n_max for n in level_set)
    rows = [list(valuation_vector(n, primes)) for n in level_set]
    augmented = [row + [1] for row in rows]
    return rational_rank(rows), rational_rank(augmented)


def brute_force_rank_maximum(n_max: int) -> Tuple[int, Tuple[int, ...]]:
    """Independent 2^(N-1) subset/rank oracle, intended only for small N."""
    primes = primes_up_to(n_max)
    numbers = tuple(range(2, n_max + 1))
    best: Tuple[int, ...] = ()
    for mask in range(1 << len(numbers)):
        size = mask.bit_count()
        if size <= len(best):
            continue
        candidate = tuple(
            number for index, number in enumerate(numbers) if (mask >> index) & 1
        )
        rank_v, rank_augmented = validate_rank(n_max, primes, candidate)
        if rank_v == rank_augmented:
            best = candidate
    return len(best), best


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--N", type=int, nargs="+", help="one or more N values")
    group.add_argument(
        "--range",
        type=int,
        nargs=2,
        metavar=("START", "END"),
        help="inclusive range of N values",
    )
    group.add_argument(
        "--self-check-through",
        type=int,
        metavar="END",
        help="compare the search with exhaustive subset/rank search for 2<=N<=END",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit one full JSON record per N instead of a compact table",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_check_through is not None:
        if args.self_check_through < 2:
            raise SystemExit("self-check endpoint must be at least 2")
        print("N recursive_maximum brute_rank_maximum witness")
        for value in range(2, args.self_check_through + 1):
            recursive = ModalSearch(value).run()["maximum"]
            brute, witness = brute_force_rank_maximum(value)
            print(value, recursive, brute, list(witness))
            assert recursive == brute
        return 0
    if args.N is not None:
        values = args.N
    else:
        start, end = args.range
        if start > end:
            raise SystemExit("range START must be <= END")
        values = list(range(start, end + 1))
    if any(value < 2 for value in values):
        raise SystemExit("all N must be at least 2")

    if not args.json:
        print("N maximum rank nodes bound_prunes duplicate_prunes seconds")
    for value in values:
        result = ModalSearch(value).run()
        if args.json:
            print(json.dumps(result, sort_keys=True))
        else:
            print(
                result["N"],
                result["maximum"],
                result["rank_V"],
                result["nodes"],
                result["bound_prunes"],
                result["duplicate_prunes"],
                f'{result["elapsed_seconds"]:.6f}',
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
