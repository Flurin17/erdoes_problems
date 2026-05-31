# Erdos Problem 647 Notes

## Problem

Find an integer `n > 24` such that

```text
max_{m < n} (m + tau(m)) <= n + 2,
```

where `tau(m)` is the number of positive divisors of `m`.

Equivalently, every `m < n` satisfies

```text
tau(m) <= n + 2 - m.
```

This is only restrictive for `m` close to `n`.

## Known Remarks To Reconstruct

- `n = 24` works.
- The `n + 2` threshold is best possible.
- Erdos suspected examples `n > 24` may be rare.
- Related problems 413 and 679 may be relevant.

## Source Summary

Direct page `/647`:

- Problem: let `tau(n)` count positive divisors. Is there an `n > 24`
  such that `max_{m < n} (m + tau(m)) <= n + 2`?
- Status on the site: open and "verifiable"; prize listed as `$44`.
- The page attributes the problem to Erdos and Selfridge.
- The page states that `n = 24` works.
- The page states that `n + 2` is best possible, because
  `max(tau(n-1)+n-1, tau(n-2)+n-2) >= n+2`.
- The page quotes Erdos [Er79] as saying it is "extremely doubtful" that
  infinitely many such `n` exist, and suggests
  `lim_{n -> infinity} max_{m<n}(tau(m)+m-n) = infinity`.
- The page quotes Erdos [Er79d] as saying it "seems certain" that for each
  fixed `k` there are infinitely many `n` such that
  `max_{n-k < m < n}(m + tau(m)) <= n+2`, but that this is out of reach
  by present methods and follows from Schinzel's Hypothesis H.
- The page says Erdos offered 25 pounds in [Er92e] for an example
  `n > 24`.
- Tao's linked comment says the problem is similar to, but slightly weaker
  than, the first part of problem 679 because `tau(m)` behaves somewhat like
  `2^omega(m)`, and is much stronger than problems 413 or 248.
- Related external data: formal statement link, OEIS A062249 for `n+tau(n)`,
  and OEIS A087280 for equality cases `max_{m<n}(m+tau(m)) = n+2`.
  A087280 lists `5, 8, 10, 12, 24` and says no more terms are known below
  `10^10`.

Bibliography hooks on `/647`:

- [Er79] Paul Erdos, "Some unconventional problems in number theory",
  Math. Mag. (1979), 67-70, MR 527408.
- [Er79d] P. Erdos, "Some unconventional problems in number theory",
  Acta Math. Acad. Sci. Hungar. (1979), 71-80, MR 515121.
- [Er80] Paul Erdos, "A survey of problems in combinatorial number theory",
  Ann. Discrete Math. (1980), 89-115, problem page cites p. 107,
  MR 593525.
- [Er92e] Pal Erdos, "Some Unsolved problems in Geometry, Number Theory
  and Combinatorics", Eureka (1992), 44-48.
- [Er95c] Paul Erdos, "Some problems in number theory",
  Octogon Math. Mag. (1995), 3-5, MR 1374981.

Forum comments on `/forum/discuss/647`:

- Terence Tao, 2025-10-02: notes the analogy with `2^omega(m)` and links
  the problem to 679, 413, and 248.
- Sayan Dutta, 2026-01-18: proves elementary necessary conditions:
  for sufficiently large candidates, `2,4,6,5,7,8,9` divide `n`, so any
  candidate `n > 84` must be `n = 2520 N`. Also derives small-shift
  constraints for `k = 1,2,3,4,6,8,12,24`, with a later correction about
  coprimality for `k = 8,24`.
- Boris Alexeev, 2026-01-19: checks the coprimality issue for `k=8,24`,
  reports OEIS A087280 has no examples below `10^10`, and says the same
  style of search suggests no examples up to `10^16` or more, assuming no
  implementation errors. Gives a near miss
  `n = 604517614941240`, `N = 239887942437`, where the small shifts
  `1 <= k <= 13` and `k=24` pass.
- Sayan Dutta, 2026-01-19: agrees about the `k=8,24` coprimality issue and
  refines those constraints using 2-adic valuation.
- Jamal Agbanwa, 2026-01-28: claims the only solutions are
  `{1,2,3,4,5,6,8,10,12,24}`.
- Terence Tao, 2026-01-28: replies that the claimed asymptotic part is not
  justified and the Lean formalization treats it as an axiom; this is not
  an unconditional certificate.
- Scott Hughes, 2026-05-27: records two reductions. First, every candidate
  `n > 84` satisfies `n = 2520 N` with `N` in 41 explicit residue classes
  modulo `11*13*17*19 = 46189`. Second, every candidate `n > 24` lies in
  one of two prime-chain families:
  `n = 8s+8` with `s, 2s+1, 4s+3, 8s+7` prime, or
  `n = 16s+8` with `s, 4s+1, 8s+3, 16s+7` prime. This gives a
  density-zero upper bound `O(x/(log x)^4)` for candidate count, not a
  solution.
- Kenta Kitamura, 2026-05-29: under the reduction, any candidate `n > 84`
  also satisfies `(n-3)/3` prime.
- Scott Hughes, 2026-05-29: strengthens the prime-chain reduction to two
  admissible prime 7-tuples. With `n = 2520N`, the branches can be written
  as:
  - `n = 8s+8`, `s = 3u+2`:
    `2u+1, 3u+2, 4u+3, 6u+5, 8u+7, 12u+11, 24u+23` prime.
  - `n = 16s+8`, `s = 3u+1`:
    `3u+1, 4u+1, 8u+3, 12u+5, 16u+7, 24u+11, 48u+23` prime.
  This improves the density-zero upper bound to `O(x/(log x)^7)`.

Related pages:

- Problem 413 asks for barriers for `omega(n)`, the count of distinct prime
  divisors, with inequalities of the form `m + omega(m) <= n`.
- Problem 679 asks for `n` such that `omega(n-k)` remains below about
  `log k / log log k` for all sufficiently large `k`.
- Problem 248 asks for infinitely many `n` such that `omega(n+k) << k`.
  The page says Tao and Teravainen resolved a related upper-bound form, and
  Lau improved it to logarithmic in `k`.

## Search Strategy

- Compute `tau(m)` over long intervals using divisor-sieve and segmented methods.
- Track records of `f(m) = m + tau(m)`.
- Candidate `n` must satisfy `R(n - 1) <= n + 2`, where
  `R(x) = max_{m <= x} f(m)`.
- Verify any candidate with at least two independent implementations.

## Derived Small-Shift Conditions

Writing `k = n - m`, the target condition is

```text
tau(n-k) <= k+2    for every 1 <= k < n.
```

For any candidate `n > 84`, the comment reductions give

```text
n = 2520 N.
```

The strengthened prime-chain reduction gives two branches.

Branch A:

```text
N even, and
210N-1, 315N-1, 420N-1, 630N-1, 840N-1, 1260N-1, 2520N-1
are prime.
```

In Branch A, `k=24` gives one more prime condition. Since `N` is even,
`105N-1` is odd and

```text
n-24 = 24(105N-1),        tau(n-24) <= 26,
```

so `tau(105N-1) <= 3`; also `105N-1 == 2 mod 3`, so it is not a square.
Therefore `105N-1` is prime in Branch A.

Branch B:

```text
N odd, and
(315N-1)/2, 210N-1, 420N-1, 630N-1, 840N-1, 1260N-1, 2520N-1
are prime.
```

Additional constraints from shifts `k=5,9,10`:

```text
k=5:  n-5  = 5(504N-1).
      If 5 does not divide 504N-1, then 504N-1 must be prime.
      If 504N-1 is divisible by 5, then the allowed composite case is
      504N-1 = 5p with p prime.

k=9:  n-9  = 9(280N-1).
      If 3 does not divide 280N-1, then 280N-1 must be prime.
      If 3 divides it, allowed composite cases include 280N-1 = 3p
      or 9p with p prime.

k=10: n-10 = 10(252N-1).
      Since 252N-1 is odd, if 5 does not divide 252N-1 then it must
      be prime. If 5 divides it, the allowed composite case is
      252N-1 = 5p with p prime.
```

The current C++ search can enforce a restrictive prime-only subsearch for
these three forms with:

```text
--extra-prime-coeffs 504,280,252
```

This is useful for finding very prime-rich near misses, but it is not a
complete candidate search. A complete search must use the 7-tuple branch
conditions and then verify all shifts directly.

The next obstructions in direct verification are often at `k=14,15,16`:

```text
k=14: n-14 = 14(180N-1), so tau(180N-1) <= 4.
k=15: n-15 = 15(168N-1), so tau(168N-1) <= 4.
```

These allow semiprime cofactors, so they are handled by direct `tau`
factorization rather than by prime-form sieving.

For shifts `14 <= k <= 40`, no new global prime-form conditions are
currently known. The fixed factor in `2520N-k` can share primes with the
remaining linear form, so tempting forms such as `180N-1`, `168N-1`,
`140N-1`, `126N-1`, and `105N-1` are not globally forced prime.

## Search Results So Far

- `record_sieve 1000` returns exactly
  `1,2,3,4,5,6,8,10,12,24`.
- Independent verifier confirms `n=24` passes the shift check.
- The published near miss
  `n = 604517614941240 = 2520 * 239887942437`
  passes `k <= 13` but fails at `k=14`, where
  `tau(n-14) = 192 > 16`.
- The complete branch search over `N < 10^9` found 622 prime tuples and
  no candidate passing `k <= 500`.
- The complete branch search over `10^9 < N <= 11*10^9` found 2883 prime
  tuples and no candidate passing `k <= 500`.
- The complete branch search over `11*10^9 < N <= 21*10^9` found 2096 prime
  tuples and no candidate passing `k <= 500`.
- The complete branch search over `21*10^9 < N <= 31*10^9` found 1892 prime
  tuples and no candidate passing `k <= 500`.
- With the restrictive prime-only filters
  `504N-1,280N-1,252N-1`, the search over `N < 10^9` found only two
  matching prime tuples and neither survived past `k=13`. This is a
  heuristic subsearch, not an exclusion of all candidates in that range.

## Proof Notes

For a proposed candidate `n`, compute

```text
B = max_{m < n} tau(m)
```

by enumerating exponent vectors

```text
2^a1 3^a2 5^a3 ...
```

with nonincreasing exponents. This gives the exact maximum possible divisor
count below `n` without sieving up to `n`.

It is enough to verify `tau(n-k) <= k+2` for `1 <= k <= B-1`. For
`k >= B`, one has

```text
n-k + tau(n-k) <= n-k+B <= n.
```

The final certificate should list `B`, a witness attaining `B`, every
factorization of `n-k` for `1 <= k <= B-1`, the resulting tau values, and
the maximum value(s) of `m + tau(m)`.
