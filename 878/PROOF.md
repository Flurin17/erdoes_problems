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

The remaining global asymptotics are not claimed here until their analytic
dependencies and endpoint estimates have been audited.
