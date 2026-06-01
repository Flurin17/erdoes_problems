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

Direct page `/647`, read from the site on 2026-05-31:

- Problem: let `tau(n)` count positive divisors. Is there an `n > 24`
  such that `max_{m < n} (m + tau(m)) <= n + 2`?
- Status on the site: open and "verifiable"; prize listed as `$44`.
- The page was last edited 2026-04-07 and showed 9 comments.
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

Additional necessary prime constraints from shifts `k=5,9,10`:

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

For `N > 24`, the exceptional pure-power cases allowed by the divisor budget
would force the displayed cofactor to be one of finitely many tiny powers
(`5^a` for `k=5,10`, or `3^a` for `k=9`), which is impossible in the searched
ranges. Thus the relevant divided cofactor is prime. The current C++ search
enforces the complete conditional version with:

```text
--extra-prime-shift-forms 5,9,10
```

This is not the same as the older restrictive `--extra-prime-coeffs
504,280,252`: that older option incorrectly throws away the valid divided
prime cases `(504N-1)/5`, `(280N-1)/3`, `(280N-1)/9`, and `(252N-1)/5`.
The shift-form option conditionally root-sieves those divided forms according
to the current `N` congruence, then still verifies all shifts directly.

The next obstructions in direct verification are often at `k=14,15,16`:

```text
k=14: n-14 = 14(180N-1).
k=15: n-15 = 15(168N-1).
```

These formulas are only globally true away from shared factors:
`7 | 180N-1` can occur for `k=14`, and `5 | 168N-1` can occur for
`k=15`. The safe conditions are:

```text
k=14: with 180N-1 = 7^r C and 7 not dividing C,
      2(r+2) tau(C) <= 16.

k=15: with 168N-1 = 5^r C and 5 not dividing C,
      2(r+2) tau(C) <= 17.
```

Thus if the shared prime does not divide the cofactor one gets
`tau(180N-1) <= 4` or `tau(168N-1) <= 4`; if `r=1,2`, the remaining
cofactor must be prime. The search handles these by direct `tau`
factorization rather than by prime-form sieving.

For shifts `14 <= k <= 120`, no additional global prime-only conditions are
currently known. The fixed factor in `2520N-k` can share primes with the
remaining linear form, so tempting forms such as `180N-1`, `168N-1`,
`140N-1`, `126N-1`, and `105N-1` are not globally forced prime. The useful
exact filter is instead to remove any shared prime powers from the remaining
linear form and compare the residual divisor budget.

Additional safe small-shift constraints, useful for hand-checking near
misses and for avoiding unnecessary full factorizations:

```text
k=7:  L=360N-1,  (r+2) tau(C) <= 9   for L=7^r C.
k=18: L=140N-1,  2(r+3) tau(C) <= 20 for L=3^r C.
k=20: L=126N-1,  3(r+2) tau(C) <= 22 for L=5^r C.
k=21: L=120N-1,  2(r+2) tau(C) <= 23 for L=7^r C.
k=24: L=105N-1,  2(r+4) tau(C) <= 26 for L=2^r C.
k=28: L=90N-1,   3(r+2) tau(C) <= 30 for L=7^r C.
k=30: L=84N-1,   4(r+2) tau(C) <= 32 for L=5^r C.
k=36: L=70N-1,   3(r+3) tau(C) <= 38 for L=3^r C.
k=40: L=63N-1,   (a+4)(b+2) tau(C) <= 42 for L=2^a 5^b C.
k=42: L=60N-1,   4(r+2) tau(C) <= 44 for L=7^r C.
k=45: L=56N-1,   (a+3)(b+2) tau(C) <= 47 for L=3^a 5^b C.
k=48: L=105N-2,  2(r+4) tau(C) <= 50 for L=2^r C.
k=56: L=45N-1,   (a+4)(b+2) tau(C) <= 58 for L=2^a 7^b C.
k=60: L=42N-1,   6(r+2) tau(C) <= 62 for L=5^r C.
k=72: L=35N-1,   (a+4)(b+3) tau(C) <= 74 for L=2^a 3^b C.
k=84: L=30N-1,   6(r+2) tau(C) <= 86 for L=7^r C.
k=90: L=28N-1,   2(a+3)(b+2) tau(C) <= 92 for L=3^a 5^b C.
k=120: L=21N-1,  2(a+4)(b+2) tau(C) <= 122 for L=2^a 5^b C.
```

Here `r`, or `a,b`, denotes valuation at the displayed shared prime(s), and
`C` is the remaining cofactor.

The C++ tuple search now handles these exact low-budget shared-prime cases
for `k=7,14,15,16,18,20,21,24,27,28,30,32,35,36,40,42,45,48,56,60,72,84,90,120`
without full factorization when possible. The helper `tau_leq_small(C,T)` is
exact for `T <= 5`: it permits `C=1`, primes, prime squares, prime cubes,
fourth powers of primes, and semiprimes as allowed by the divisor budget, so
it does not make the invalid "prime-only" simplification. For residual
budgets above 5 it falls back to the exact factorization routine.

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
- The 41 residue classes modulo `46189` from Scott Hughes's comment were
  independently reconstructed with `residue_classes 50`:

```text
0, 858, 1287, 1716, 2431, 2574, 4862, 5291, 6149, 8151,
9009, 9867, 10582, 12155, 12584, 13013, 13442, 16302,
17017, 17160, 18733, 19877, 20306, 20735, 21164, 24310,
24453, 25168, 27170, 28028, 28457, 29315, 29601, 31603,
32032, 32461, 35321, 36608, 37752, 38896, 44187
```

  The key refinement beyond the original `tau(gcd)` filter is: if the
  forced divisor contribution `T` at shift `k` satisfies `2T > k+2`, then
  there can be no prime factor outside the forced set. The number
  `2520N-k` would have to be composed only of the forced primes, and if the
  smallest positive representative in the residue class is already larger
  than every such forced-smooth number with at most `k+2` divisors, the
  class is impossible.
- A complete scan of those 41 classes for `N < 10^15` found 331,487 branch
  prime tuples and no value passing direct checks through `k <= 5000`.
  Aggregated first failures were:

```text
5:288159 7:26766 9:14390 10:1880 11:190 13:61 14:32 15:6 16:3
```

  The deepest near misses failed at `k=16`; the best recorded one is
  `N = 832414790665601`, `n = 2097685272477314520`,
  `tau(n-16) = 32`.
- The follow-up scan over `10^15 <= N < 3*10^15` found 485,824 branch
  prime tuples and no value passing direct checks through `k <= 5000`.
  Aggregated first failures were:

```text
5:425531 7:37720 9:19745 10:2480 11:231 13:81 14:27 15:9
```

  No tuple in this range survived past `k=15`.
- The final unsigned-64-bit scan over
  `3*10^15 <= N < 7320136537186331` found 886,846 branch prime tuples and
  no value passing direct checks through `k <= 5000`. Aggregated first
  failures were:

```text
5:779139 7:68367 9:34486 10:4284 11:360 13:139 14:48 15:16 16:4 18:2 20:1
```

  The deepest near miss failed at `k=20`:
  `N = 3602115923026621`, `n = 9077332126027084920`,
  `tau(n-20) = 72`.
- The first 128-bit scan over
  `7320136537186331 <= N < 10^16` found 501,242 branch prime tuples and
  no value passing direct checks through `k <= 5000`. Aggregated first
  failures were:

```text
5:440986 7:38229 9:19525 10:2200 11:198 13:69 14:28 15:7
```

  No tuple in this range survived past `k=15`.
- A lifted scan through prime `23` used 352 residue classes modulo
  `1062347`. Over `10^16 <= N < 2*10^16`, it found 917,450 branch prime
  tuples and no value passing direct checks through `k <= 5000`.
  Aggregated first failures were:

```text
5:801083 7:74718 9:36482 10:4519 11:438 13:142 14:50 15:14 16:3 22:1
```

  The deepest near miss failed at `k=22`:
  `N = 10182590254890053`, `n = 25660127442322933560`,
  `tau(n-22) = 32`.
- Lifting the same forced-smooth residue filter through primes `23,29` with
  `k <= 1000` gives 4,374 residue classes modulo `30808063`, density
  approximately `1.41975819772e-4`. This scan was stopped early in the range
  `2*10^16 <= N < 4*10^16` once the stricter `23,29,31` lift was available.
- Lifting through primes `23,29,31` with `k <= 1000` gives 59,128 residue
  classes modulo `955049953`, density approximately `6.1911e-5`. This cuts
  the tested progression density by about `2.29x` compared with the
  `23,29` lift, but it requires the batched job mode in `prime_tuple_search128`
  and `run_residue_scan.py` to avoid one process per residue class.
- A compiled lifter independently reproduced the `23,29,31` CSV byte-for-byte.
  Extending the same forced-smooth filter through prime `37` with `k <= 1000`
  gives 1,122,290 residue classes modulo `35336848261`, density approximately
  `3.17598e-5`. A dry run for `8*10^16 <= N < 1.6*10^17` gives 274 batched
  jobs with `--batch-size 4096` and total `X` count `2540781207701`.
- Extending that same `37` lift to the scan's full quick-check range
  `k <= 5000` removes only one more residue: 1,122,289 residue classes, dry-run
  total `X` count `2540778943775` over `8*10^16 <= N < 1.6*10^17`.
- The complete `23,29,31` lifted scan over
  `2*10^16 <= N < 4*10^16` found 532,062 branch prime tuples and no value
  passing direct checks through `k <= 5000`. Aggregated first failures were:

```text
5:459759 7:46776 9:22007 10:3035 11:325 13:114 14:38 15:5 16:3
```

  The deepest near misses failed at `k=16`; the best by failing shift and
  then smaller failing divisor count was
  `N = 27483420334150209`, `n = 69258219242058526680`,
  `tau(n-16) = 32`.
- The complete `23,29,31` lifted scan over
  `4*10^16 <= N < 8*10^16` found 950,660 branch prime tuples and no value
  passing direct checks through `k <= 5000`. Aggregated first failures were:

```text
5:823271 7:82828 9:38459 10:5283 11:537 13:184 14:72 15:18 16:5 17:1 18:1 21:1
```

  The deepest near miss failed at `k=21`:
  `N = 59845588255683945`, `n = 150810882404323541400`,
  `tau(n-21) = 32`. Both independent Python verifiers reject it at `k=21`.
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

It is enough to verify `tau(n-k) <= k+2` for every positive `k` with
`k+2 < B`; the scripts check the slightly larger range `1 <= k <= B-2`.
For `k+2 >= B`, one has

```text
tau(n-k) <= B <= k+2.
```

The final certificate should list `B`, a witness attaining `B`, every
factorization of `n-k` for `1 <= k <= B-1`, the resulting tau values, and
the maximum value(s) of `m + tau(m)`.
