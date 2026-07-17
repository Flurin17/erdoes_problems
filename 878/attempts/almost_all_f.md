# Route: a first moment for the almost-all upper bound on `f`

## Result and conventions

All logarithms below are natural.  Put `log_2 x=log log x` and
`log_3 x=log log log x` when these are defined.  The argument proves the
uniform estimate

`H(x) << x(1+log_3 x)`                                             (1)

for all sufficiently large real `x`; enlarging the absolute implied constant
handles every real `x>=2` if the right side is interpreted with a harmless
positive truncation of `log_3`.  Consequently

`f(n)=o(n log log n)` for almost all positive integers `n`,              (2)

where “almost all” means outside one set of natural density zero.  This does
not prove the conjectured estimate `H(x)<<x log_4 x`.

The convention at `n=1` is `f(1)=0`, so it makes no contribution.  Every
inequality below respects the strict cutoff `n<x` in the definition of
`H(x)`.

## Analytic inputs

Only the following standard upper-bound forms are used.

1. **Mertens upper bound.**  There is an absolute `C` such that, for `z>=3`,

   `sum_{p<=z} 1/p <= log log z+C`.                                  (M)

2. **Brun--Titchmarsh, interval form.**  If `A>=0` and `D>=2`, then

   `pi(A+D)-pi(A) <= 2D/log D`.                                      (BT)

Only intervals for which `D` tends to infinity are used, so changes to the
usual inessential small-`D` formulation are absorbed in an absolute
constant.  No prime number theorem, short-interval asymptotic, or unproved
equidistribution assertion is used.

## 1. Exact finite identity

For `n>1` and `p|n`, write `n=pm`.  For an integer `k>=1`,

`p^(k-1) <= m < p^k`

is equivalent to `p^k <= n < p^(k+1)`.  Hence the `p`-summand of
`f(n)/n` is `p^k/(pm)=p^(k-1)/m`.  Finite reindexing therefore gives the
exact identity

`H(x) = sum_p sum_{k>=1} p^(k-1)
              sum_{p^(k-1)<=m<p^k, pm<x} 1/m`.                       (3)

Every sum here is finite: a nonempty inner sum implies `p^k<x`.  Thus (3)
does not interchange conditionally convergent or infinite sums.

We repeatedly use the elementary estimate, valid for every integer `a>=1`
and real `b>a`,

`sum_{a<=m<b} 1/m <= 1/a+log(b/a)`.                                  (4)

Indeed, separate the term `1/a` and bound the remaining terms by an
integral.

## 2. Completed prime-power blocks contribute `O(x)`

For each `p`, reserve the name *boundary block* for the unique exponent `K`
in (6) below, and call all blocks `k<K` *bulk completed blocks*.  Such a block
has `p^(k+1)<=p^K<x`, so every integer `m<p^k` satisfies `pm<x`.  By (4), a
bulk completed block is at most

`p^(k-1) log p+1`.                                                    (5)

For a fixed `p`, if `K` is the terminal exponent characterized by

`p^K<x<=p^(K+1)`,                                                     (6)

then all bulk completed blocks have `1<=k<K`.  Therefore

`sum_{1<=k<K} p^(k-1) < p^(K-1)/(p-1) < x/(p(p-1))`.

The logarithmic terms in (5), summed over all primes, are consequently at
most

`x sum_p log p/(p(p-1)) = O(x)`,                                     (7)

because the displayed series converges by comparison with
`sum_{r>=2}log r/r^2`.  The number of bulk completed pairs is at most

`sum_{1<=k<=(log x)/(log 2)} x^(1/(k+1))
 <= sqrt(x)(log x)/(log 2) = O(x)`.                                  (8)

Thus all bulk completed blocks together contribute `O(x)`.  The exact
arithmetic criterion for a full block is slightly broader
(`p^(k+1)-p<x`).  In particular, at an exact prime-power cutoff the boundary
block can itself be full.  Classifying it with the boundary blocks in the next
section only enlarges the upper bound and avoids any endpoint gap.

## 3. Terminal blocks

For each prime `p<x`, (6) defines one and only one `K=k>=1`.  Blocks below it
are bulk completed and blocks above it are empty, so the remaining block is
the only boundary block (whether partial or accidentally full).  Set

`L=log x`, `delta=L-k log p=log(x/p^k)`.

By (6), `0<delta<=log p`.  Applying (4) with `a=p^(k-1)` and `b=x/p` gives

`T(p) <= 1+p^(k-1) delta
       = 1+(x/p) phi(delta)`,                                        (9)

where `phi(u)=u exp(-u)`.  The equality in (9) uses
`x/p=p^(k-1)exp(delta)`.  Since there are fewer than `x` terminal primes,
the additive ones in (9) total `O(x)`.  It remains to estimate

`S(x)=sum_{p<x} phi(delta_p)/p`,                                     (10)

where each `delta_p` uses its unique exponent in (6).

### Small terminal primes

Let `Z=e L^2`.  Since `phi(u)<=1/e` for `u>=0`, (M) gives

`sum_{p<=Z} phi(delta_p)/p
 <= (1/e) sum_{p<=Z}1/p
 << 1+log log Z
 << 1+log_3 x`.                                                      (11)

This is the only source of the third iterated logarithm.

### Large terminal primes

Suppose `p>Z`.  From `p^k<x` in (6),

`1<=k<L/log Z`.                                                      (12)

Also `x<=p^(k+1)` implies

`delta=L-k log p <= L/(k+1)`.                                       (13)

Fix `k` and put `j=floor(delta)`.  The condition `j<=delta<j+1` places `p`
in the root cell

`A=exp((L-j-1)/k) < p <= B=exp((L-j)/k)`,                            (14)

whose length is

`D=B-A=A(exp(1/k)-1)`.

We apply (BT) only to cells containing an actual terminal prime `p>Z`.
For such a cell, (14) gives `A>=p/e>Z/e=L^2`.  Moreover (12) gives `k<L`,
so

`D>=A/k`,  `log D>=log A-log k >= (1/2)log A`,                       (15)

once `x` is sufficiently large.  In particular `D>=2`.  Since
`exp(1/k)-1 <= (e-1)/k`, Brun--Titchmarsh and (15) yield

`sum_{A<p<=B}1/p
 <= [pi(B)-pi(A)]/A
 <= 2D/(A log D)
 << 1/(k log A)
 = 1/(L-j-1)`.                                                       (16)

By (13), `j<=L/(k+1)`, and hence, uniformly for every `k>=1`,

`L-j-1 >= L-L/(k+1)-1 >= L/3`                                      (17)

for all sufficiently large `L`.  On the cell (14),

`phi(delta)<= (j+1)e^(-j)`.

Combining this with (16)--(17) and summing over all `j>=0`, we obtain, for
each fixed `k`,

`sum_{p>Z, p terminal with exponent k} phi(delta_p)/p
 << (1/L) sum_{j>=0}(j+1)e^(-j)
 << 1/L`.                                                           (18)

There are fewer than `L/log Z` possible exponents by (12), so all large
terminal primes contribute

`<< (L/log Z)(1/L) = O(1/log Z)=O(1)`.                              (19)

The enlargement from the terminal primes to the full cells in (16) is an
upper bound, not an assertion that every prime in a cell has terminal
exponent `k`.

Equations (7)--(11) and (19), inserted into (9), prove (1).

## 4. Markov deduction of the almost-all statement

Fix `epsilon>0`, and let `E_epsilon(X)` count integers `n<X` satisfying

`f(n) >= epsilon n log log n`.

Integers `n<sqrt(X)` contribute only `O(sqrt(X))`.  For
`sqrt(X)<=n<X`, every exceptional integer contributes at least
`epsilon log log(sqrt(X))` to `H(X)`.  Therefore (1) gives

`E_epsilon(X)
 <= sqrt(X)+H(X)/(epsilon log log(sqrt(X)))
 << sqrt(X)+(X/epsilon)(1+log_3 X)/log_2 X
 = o(X)`.                                                           (20)

Thus `f(n)/(n log log n)` converges to zero in natural density.  To obtain
the literal formulation “outside one density-zero set”, apply the standard
diagonal argument to the density-zero sets

`E_r={n: f(n)/(n log log n)>1/r}` (`r=1,2,...`):

choose increasing cutoffs so far enough out the density of `E_r` is as small
as desired, and on the `r`-th successive interval remove only `E_r`.  The
union removed has density zero (choose the density tolerances tending to
zero), while off that union the ratio is at most `1/r` on the `r`-th interval
and hence tends to zero.  This proves (2).

## Mechanism, falsification tests, and remaining bottleneck

The mechanism is that all completed logarithmic blocks have a convergent
prime weight, while a terminal block has the exact phase weight
`phi(log(x/p^k))/p`.  Small primes are paid for by Mertens; large primes are
localized into logarithmic root cells and paid for by Brun--Titchmarsh.

Endpoint-sensitive falsification checks for this proof are:

- verify (3) directly at real cutoffs immediately below, equal to, and
  immediately above prime powers;
- verify that (6) assigns exactly one terminal exponent when `x` is itself a
  prime power;
- check the root-cell implications (12)--(17), especially the cells meeting
  the artificial cutoff `p=Z`;
- check that every use of (BT) has `D>=2` (guaranteed by (15), not assumed).

The weakest step relative to the source's stronger `H` question is (11).
Paying trivially for every prime up to `e(log x)^2` costs `log_3 x`.
Replacing the cutoff by one whose Mertens mass is `O(log_4 x)` makes the
root-cell lengths too short for the above direct Brun--Titchmarsh argument
near the cutoff.  A proof of `H(x)<<x log_4 x` therefore needs additional
uniform cancellation or finer phase information for these medium primes;
neither follows from (M) and (BT) as used here.  No claim about `log_4 x` is
made.
