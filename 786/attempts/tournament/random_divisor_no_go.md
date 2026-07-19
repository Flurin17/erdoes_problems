# Independent random-divisor models: a no-go lemma

This note isolates the exact obstruction to replacing the uniform measure on
\([1,N]\) by an unconditioned independent-prime random divisor.  It also
quantifies the cost of recovering the uniform measure by conditioning.

## 1. Unconditioned product laws have too little support

**Lemma 1 (Cartesian-support obstruction).**  Let
\[
X=\prod_p p^{V_p},
\]
where the nonnegative integer-valued random variables \(V_p\) are independent.
If \(X\le N\) almost surely, then
\[
|\operatorname{supp}X|\le 2\sqrt N.
\]
Consequently an unconditioned independent-prime law supported on \([1,N]\)
cannot satisfy
\[
\max_{n\le N}\Pr(X=n)\le \frac K N
\]
for a fixed \(K\) once \(N>4K^2\).

**Proof.**  Only finitely many coordinates can be nonconstant: otherwise one
can choose finitely many primes having a positive probability of a positive
exponent and whose product exceeds \(N\); independence then gives positive
probability to \(X>N\).  For every active prime let
\(a_p=\max\operatorname{supp}V_p\).  Independence implies that the simultaneous
choice \(V_p=a_p\) has positive probability, so
\[
M:=\prod_p p^{a_p}\le N.
\]
Every value in the support of \(X\) divides \(M\).  Hence
\[
|\operatorname{supp}X|\le \tau(M)\le 2\sqrt M\le 2\sqrt N,
\]
where the middle inequality follows by pairing each divisor below \(\sqrt M\)
with its complementary divisor.  If every point mass were at most \(K/N\),
their total mass would be at most \(2K/\sqrt N<1\), a contradiction. \(\square\)

The same proof shows that a mixture of \(R\) such bounded product/divisor laws
with point masses at most \(K/N\) must have
\[
R\ge \frac{\sqrt N}{2K}.
\]
Thus a bounded-complexity mixture does not repair the obstruction.

## 2. Conditioning a product proposal is necessarily extremely rare

**Lemma 2 (acceptance bound).**  Let the \(V_p\) again be independent, without
assuming \(X\le N\), and put \(E=\{X\le N\}\).  Suppose the conditional law
\(\mu(n)=\Pr(X=n\mid E)\) is two-sided \(K\)-comparable with uniform measure:
\[
\frac1{KN}\le \mu(n)\le \frac K N\qquad(1\le n\le N).
\]
Then
\[
\Pr(E)\le KN\left(1+K^{-2}\right)^{-\pi(N)}.
\]

**Proof.**  Write \(q_{p,j}=\Pr(V_p=j)\).  For each prime \(p\le N\),
independence and cancellation of all other coordinates give
\[
\frac{q_{p,1}}{q_{p,0}}
=\frac{\Pr(X=p)}{\Pr(X=1)}
=\frac{\mu(p)}{\mu(1)}
\ge K^{-2}.
\]
Therefore \(q_{p,0}\le(1+K^{-2})^{-1}\).  Independence yields
\[
\Pr(X=1)\le(1+K^{-2})^{-\pi(N)}.
\]
Finally \(\mu(1)=\Pr(X=1)/\Pr(E)\ge1/(KN)\), which rearranges to the claimed
bound. \(\square\)

For fixed \(K\), the acceptance probability is exponentially small in
\(\pi(N)\).  Thus an unconditional atom estimate for the independent proposal
cannot be transferred through the elementary inequality
\(\Pr(F\mid E)\le\Pr(F)/\Pr(E)\) with a uniform loss.

## 3. Exact model showing that the hard conditioning is the whole problem

Let
\[
L_N=\operatorname{lcm}(1,2,\ldots,N),\qquad
a_p=\lfloor\log_pN\rfloor,
\]
and take the \(V_p\) independently and uniformly on
\(\{0,1,\ldots,a_p\}\).  Then \(X=\prod p^{V_p}\) is a uniformly random divisor
of \(L_N\), and
\[
\mathcal L(X\mid X\le N)=\operatorname{Unif}\{1,\ldots,N\}.
\]
Moreover, for every completely additive \(f\) that is nonzero on at least one
prime \(p\le N\), the unconditioned sum
\(f(X)=\sum_p f(p)V_p\) has every atom at most \(1/2\): condition on all
coordinates except one with \(f(p)\ne0\), and note that its exponent is uniform
on at least two values.  Nevertheless
\[
\Pr(X\le N)=\frac{N}{\tau(L_N)}\le N2^{-\pi(N)}.
\]
So this construction simultaneously has perfect independent-prime
anti-concentration before conditioning and the exact desired uniform measure
after conditioning.  Any bound on the conditioned atom is precisely a bound on
an additive slice of the knapsack down-set \(\{\prod p^{v_p}\le N\}\), i.e. the
original finite problem; independence alone supplies no shortcut.

## Route verdict

An **unconditioned** independent random-divisor measure cannot even have the
one-sided point-mass comparison needed to turn a probability gap into a
positive-density gap.  A **conditioned** product proposal can reproduce uniform
measure exactly, but two-sided comparability forces exponentially rare
conditioning.  Therefore a successful probabilistic proof must exploit the
geometry of the product cutoff (or use a genuinely dependent hierarchical
law), rather than transfer a free-product atom bound.
