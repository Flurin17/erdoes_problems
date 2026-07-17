# Strongest proved results for Erdős #878

The global problem remains partly open locally.  This file records the
dependency-complete elementary reductions already proved.  Throughout the
substantive interpretation of `F` is the nonunit convention `a_i>1`; the
literal unit-admissible reading is handled separately below.

## Exact theorem for `F(n)`

Let `P(n)` be the prime support of `n`, and for each nonempty `B subset P(n)`
put

`M_n(B)=max{prod_{p in B}p^{e_p}<=n : every e_p is a positive integer}`.

Then

`F(n)=max_{Pi partition of P(n)} sum_{B in Pi}M_n(B)`.      (1)

In particular `F(n)>=max(n,f(n))`, and

`F(n)=f(n)` iff
`M_n(B)<=sum_{p in B}p^{floor(log_p n)}` for every `B`.     (2)

Proof.  Every admissible nonunit has a nonempty prime support.  Pairwise
coprimality makes these supports disjoint.  An optimum cannot omit a prime
`p|n`, since adjoining `p` would preserve admissibility and increase the sum;
thus its supports partition `P(n)`.  On any fixed block, the largest possible
term is exactly `M_n(B)`, proving the upper bound in (1), and choosing these
block maxima proves attainability.  The singleton partition has value `f(n)`;
the full block has value `n`.  Finally, if all inequalities (2) hold, summing
them over an arbitrary partition bounds (1) by `f(n)`.  If the inequality for
one block fails, that block together with all outside singleton blocks gives a
partition worth more than `f(n)`.  This proves (2).

For one-prime support, (1) gives `F(n)=f(n)=n`.  For two-prime support it gives
`F(n)=max(n,f(n))`.

## Literal convention allowing `1`

If `1` is admissible because its set of prime factors is empty, it occurs in
every optimum and may occur only once.  Hence

`F_unit(n)=F_{>1}(n)+1` for all `n>=1`,

with `F_{>1}(1)=0`.  Therefore `f(n)=F_unit(n)` has no solutions, its counting
function is identically zero, and the two running maxima cannot be equal for
any real cutoff `x>=1`.  The nontrivial equality questions in the source thus
require the nonunit convention.

## Exact finite starting point for `H(x)`

With `U_p(x)=ceil(x/p)-1` and harmonic numbers `h_r`, finite reindexing yields

`H(x)=sum_{p<x} sum_{p^j<=U_p(x)}
 p^j*(h_{min(p^{j+1}-1,U_p(x))}-h_{p^j-1})`,

where `j>=0`.  This follows from writing `n=pm` and observing that the
`p`-contribution to `f(pm)/(pm)` is
`p^{floor(log_p m)}/m`.  No infinite sums are interchanged.

## The two almost-all questions

The following two results are proved relative only to the standard inputs
stated explicitly below.  Each proof was checked independently by two fresh
adversarial referees, who found no substantive objection.

### Theorem 1

For almost all positive integers `n`,

`f(n)=o(n log log n)`.

Proof.  Put `L=log x`, `Z=eL^2`, and write `n=pm` in the exact identity above.
For a fixed prime, all completed `p`-power blocks contribute in total
`O(x log p/(p(p-1)))`; their sum over `p` is `O(x)`.  If `p^k<x<=p^{k+1}`,
the remaining boundary block is at most

`1+(x/p) phi(delta)`, `delta=log(x/p^k)`, `phi(u)=ue^{-u}`.      (3)

The additive ones total `O(x)`.  For `p<=Z`, Mertens' bound gives

`sum_{p<=Z}phi(delta_p)/p << 1+log_3 x`.                         (4)

For `p>Z`, group first by `k`, then by `j<=delta<j+1`.  The primes in one
cell lie in

`(exp((L-j-1)/k), exp((L-j)/k)]`.

Its length `D` satisfies `D>=A/k`, `log D>=(1/2)log A`, because an occupied
cell has `A>=p/e>L^2` and `k<L/log Z`.  Interval Brun--Titchmarsh therefore
gives reciprocal prime mass `O(1/(L-j-1))`.  Terminality gives
`delta<=L/(k+1)`, so this is `O(1/L)`.  Weighting by
`phi(delta)<=(j+1)e^{-j}`, summing `j`, then the fewer than `L/log Z`
possible `k`, gives `O(1)` for all large primes.  Thus

`H(x)<<x(1+log_3 x)`.                                           (5)

Markov on `sqrt(x)<=n<x` shows, for each fixed `epsilon>0`, that the set
`f(n)>epsilon n log_2 n` has density zero.  A standard block diagonalization
over `epsilon=1/r` produces one density-zero exceptional set outside which
the ratio tends to zero.  This proves the theorem.

Inputs: `sum_{p<=z}1/p<=log log z+O(1)` and the interval form
`pi(A+D)-pi(A)<<D/log D` for `D>=2`.  Exact endpoint details and the complete
cell calculation appear in `attempts/almost_all_f.md`.

### Theorem 2

There is an absolute `c>0` such that, for almost all positive integers `n`,

`F(n)>=c n log log n`.

Proof.  Work on `X<=n<2X`, put `L=log X`, `ell=log L`, and take primes in
the two logarithmic bands

`A: L^(1/8)<=log p<=L^(1/4)`,
`B: L^(1/3)<=log q<=L^(1/2)`.

Mertens gives reciprocal masses `(1/8+o(1))ell` and
`(1/6+o(1))ell`.  Call `(p,q)` good if some positive `a,b` satisfy
`X/e<=p^a q^b<=X`.

The following shrinking-target lemma is elementary Fourier analysis: for
`N>=2`, `0<lambda<=1/2`, uniformly in `t`,

`meas{theta: no 1<=b<=N has {t-btheta} in [0,lambda]}
 << log(2N)/(Nlambda)`.                                         (6)

It follows by expanding the interval indicator; the covariance for indices
`b=dr,c=ds` is
`O((lambda/s)(1+log(s/r)))`, whose total is `O(Nlambda log N)`.

Apply (6) with `theta=log q/log p`, `lambda=1/log p`, and
`N=floor(L/(3L^(1/2)))`.  A hit gives positive `a,b` and a good pair.
Transferring the exceptional logarithmic intervals to primes with the uniform
interval upper-bound sieve gives

`sum_{(p,q) bad}1/(pq)=o(ell^2)`.                               (7)

The transference is legitimate because the exceptional set has polynomial
interval complexity and its log-coordinate begins at `L^(1/3)`; subdividing
into pieces of log-length at least `exp(-L^(1/3)/2)` makes every corresponding
ordinary interval long enough for the sieve.

Exact first and second moments of divisibility show that almost every `n` in
the dyadic interval has at least `ell/10` prime divisors in each band.  The
expected number of bad divisor pairs is `o(ell^2)`, so it is below
`ell^2/200` for almost every `n`.  In the bipartite graph of good divisor
pairs, a matching smaller than `ell/40` would, by Konig's theorem, leave more
than `3ell/40` uncovered vertices on both sides and hence more than
`ell^2/200` bad cross pairs, a contradiction.  Each matching edge supplies a
number in `[X/e,X]`; disjoint edges give distinct pairwise-coprime numbers
whose primes divide `n`.  Therefore

`F(n)>=n ell/(80e)`                                              (8)

outside `o(X)` integers of `[X,2X)`.  Dyadic summation gives one density-one
set and proves the theorem.  The unit-admissible convention only increases
`F`.

Inputs: prime Mertens, the uniform interval upper-bound sieve
`pi(z+h)-pi(z)<<h/log h` for `h>=2`, and Konig's finite bipartite matching
theorem.  The full Fourier and transference proof is in
`attempts/almost_all_F.md`.

## A pointwise counterexample for the running maxima

Under the nonunit convention,

`max_{m<=210}f(m)=383`, while `F(210)>=128+125+189=442`.         (9)

The three displayed terms are supported on `{2}`, `{5}`, and `{3,7}` and are
pairwise coprime.  For the first equality: five support primes are impossible;
four force `m=210`.  If three support primes are `p<q<r`, the cases
`(p,q)=(2,3),(2,5),(2,7),(3,5)` give respective upper bounds
`378,374` (with `{2,5,13}` checked separately at `266`), `346`, and `375`;
all other pairs force `pqr>210`.  With two primes, the bound is `297` when
the larger is at most `13`; when it is at least `17`, splitting on the smaller
prime gives bounds at most `231`.  One-prime support contributes at most
`210`.  The exact optimizer independently checks these finite cases.  Hence
equality of the two running maxima is false “for all `x`”.  Eventual equality
remains open.

## An asymptotic formula for `H(x)`

For `p^2<=x`, define `ell_p=floor(log_p x)`,
`theta_p={log_p x}`, and

`M(x)=sum_{p^2<=x}log p*((p^{ell_p-1}-p)/(p-1)
                         +p^{ell_p-1}theta_p)`.                 (10)

Then, for every fixed integer `N>=1`,

`H(x)=M(x)+x sum_{r=0}^{N-1}C_r/(log x)^{r+1}
       +O_N(x/(log x)^{N+1})`,                                 (11)

where

`C_r=r! sum_{s=0}^r(-1)^s zeta^{(s)}(2)/s!`.

In particular,

`H(x)=M(x)+zeta(2)x/log x+O(x/log^2 x)`.                        (12)

Proof.  In the exact finite identity, separate the block with
`floor(log_p m)=0`.  It equals

`A_0=sum_{m^2<x}(pi_<(x/m)-pi(m))/m
    =sum_{m<sqrt(x)}pi(x/m)/m+O(sqrt(x))`.                      (13)

For `j>=1`, the block `p^j<=m<p^{j+1}` is nonempty precisely when
`p^{j+1}<x`; harmonic summation gives

`p^j sum_{p^j<=m<min(p^{j+1},x/p)}1/m
 =p^j min(log p,log(x/p^{j+1}))+O(1)`.                         (14)

The sum of the errors is `O(sqrt(x)/log x)`.  Geometric summation of the
main terms in (14) is exactly (10), with the correct strict endpoint when
`theta_p=0`.  Finally use, uniformly for `y>=sqrt(x)`, the standard fixed-
order PNT expansion

`pi(y)=y sum_{k<N}k!/(log y)^{k+1}+O_N(y/(log y)^{N+1})`.

Taylor-expand `(log x-log m)^{-k-1}` in (13).  Since
`sum_m(log m)^s/m^2=(-1)^s zeta^{(s)}(2)`, the coefficient of
`(log x)^{-r-1}` is exactly `C_r`; all truncated tails and Taylor errors are
`O_N(x/(log x)^{N+1})`.  This proves (11).  Two fresh referees independently
checked the endpoints, constants, and uniform remainder.

The oscillatory main term cannot be replaced by a constant multiple of `x`:
simultaneous Dirichlet approximation, applied to `1/log p` for `p<=P`, gives
arbitrarily large `x` at which all corresponding terminal phases lie near
one.  Hence `H(x)>>x log log P>>x log_4 x` along an unbounded sequence.
Thus the proposed `H(x)<<x log_4 x`, if true, is order-sharp.  Its uniform
upper bound remains open.

## Honest global status

The two almost-all assertions, the exact optimization, the literal-unit
equality count, the asymptotic formula (11), and the counterexample to
running-max equality for all `x` are proved.  The full maximal-order limit,
eventual running-max equality, the nonunit equality-counting asymptotic, and
the proposed `H(x)<<x log_4 x` remain open locally.
`attempts/extremal_f.md` proves the sharp limsup for maximal `f`.
