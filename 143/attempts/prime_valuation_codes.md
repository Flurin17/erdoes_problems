# Prime-valuation code route

> **Route-status correction.**  The apparent “colored-rank inequality” gap
> described below is already closed by the common-ray primitive theorem: the
> union over pairwise disjoint prime alphabets is itself primitive, regardless
> of the varying ranks, so its full $\sum 1/(n\log n)$ series converges.  Thus
> Sections 4–6 are retained as a record of the exploratory route, but they do
> not state a live bottleneck.  A valuation-code counterexample must leave a
> single common integer ray, not merely use infinitely many colors or ranks.

## 1. Mechanism

For a positive integer `n`, write `v(n)=(v_p(n))_p` and
`Omega(n)=sum_p v_p(n)`.  Divisibility is coordinatewise comparison of
valuation vectors.  Thus any antichain of valuation vectors gives an
admissible integer set.  The simplest codes are rank levels
`Omega(n)=r`; a more flexible exact construction assigns pairwise disjoint
prime alphabets `P_j` and takes one rank `r_j` inside each alphabet.  Two
words from different alphabets have disjoint nonempty supports, hence are
incomparable.

This route is useful both constructively and diagnostically.  It produces
large, rigorously admissible families, but the lemma below shows that one
fixed rank (and hence every finite union of fixed ranks) cannot disprove
either requested conclusion.  A negative valuation-code construction
would have to use infinitely many ranks/alphabet components and overcome a
global weighted summability constraint.

## 2. Precise lemma chain

1. An integer set is admissible for Problem 143 if and only if it is
   primitive (no distinct member divides another).
2. Every fixed `Omega` level is primitive.  More generally, if the prime
   alphabets `P_j` are pairwise disjoint and `r_j >= 1`, then the union of
   the rank-`r_j` words supported on `P_j` is primitive.
3. For `s>1`, if
   `F_r(s)=sum_{Omega(n)=r} n^(-s)` and
   `P(s)=sum_p p^(-s)`, then `F_r(s) <= P(s)^r`.
4. The Euler product and the integral bound for the zeta series give
   `P(s) <= log zeta(s) <= log(s/(s-1))`.
5. Since `1/(n log n)=int_1^infty n^(-s) ds`, Steps 3--4 imply convergence
   of the target series on every fixed rank.
6. Taking `s=1+1/log X` also gives the explicit harmonic estimate
   `sum_{n<X, Omega(n)=r} 1/n <= e[log(1+log X)]^r`, hence `o(log X)` for
   fixed `r`.
7. These levels are not merely geometric sparse sets: their harmonic mass
   is unbounded.  If `L(Y)=sum_(p<=Y)1/p`, then a rank-`r` squarefree
   subfamily below `Y^r` has harmonic mass at least
   `(L(Y)/r-O_r(1))^r`.

## 3. Completely proved lemma

**Lemma (fixed valuation rank, including common scaling).**  Fix an integer
`r>=1`, let `B` be any subset of `{n>=2: Omega(n)=r}`, and let `c>=1`.
Then `cB={cn:n in B}` satisfies the full ordered-pair condition of Problem
143, and

```
sum_(n in B) 1/(cn log(cn)) < infinity,
sum_(cn<X, n in B) 1/(cn) = O_(c,r)((log log X)^r)=o(log X).
```

The same admissibility assertion holds for the union of possibly varying
ranks on pairwise disjoint prime alphabets.

*Proof.*  If distinct integers `m,n` have `Omega(m)=Omega(n)=r` and
`m=kn` for an integer `k>=1`, then
`r=Omega(m)=Omega(k)+Omega(n)` forces `Omega(k)=0`, hence `k=1` and `m=n`,
a contradiction.  Thus `B` is primitive.  For distinct `m,n in B` and
integer `k>=1`, `kn-m` is a nonzero integer, so
`|kcn-cm|=c|kn-m|>=c>=1`.  Notice that this verifies every `k`, not merely
the potential quotient nearest `m/n`.

For the estimates, put

```
F_r(s)=sum_(Omega(n)=r) n^(-s),    P(s)=sum_(p prime) p^(-s).
```

In the expansion of `P(s)^r`, each integer with `Omega(n)=r` occurs at
least once (in fact with the number of orderings of its prime-factor
multiset).  Hence `F_r(s)<=P(s)^r`.  Absolute convergence of the Euler
product for `s>1` gives

```
P(s) <= sum_p sum_(a>=1) p^(-as)/a = log zeta(s).
```

Also `zeta(s)<=1+int_1^infty t^(-s)dt=s/(s-1)`.  Therefore, on `1<s<=2`,

```
F_r(s) <= [log(2/(s-1))]^r,
```

whose integral is finite because
`int_0^1 (log(2/u))^r du<infinity`.  On `s>=2`,
`P(s)<=sum_(n>=2)n^(-s)<=3*2^(-s)`, so the integral is again finite.
Tonelli and

```
int_1^infty n^(-s)ds = 1/(n log n)
```

now prove `sum_(Omega(n)=r)1/(n log n)<infinity`.  Common scaling can only
decrease this by the estimate
`1/(cn log(cn))<=c^(-1)/(n log n)`.

Finally, for `X>1` take `s=1+1/log X`.  If `n<X`, then
`n^(-1)<=e n^(-s)`, whence

```
sum_(n<X, Omega(n)=r) 1/n
 <= e F_r(s)
 <= e[log(1+log X)]^r.
```

For fixed `r` this is `o(log X)`; division by `c` and replacement of `X`
by `X/c` handle `cB`.

For the alphabet assertion, a word supported on `P_i` cannot divide a
word supported on a disjoint `P_j`, because the former has a prime factor
absent from the latter.  Within one alphabet, equality of `Omega` rules out
proper divisibility as above.  This completes the proof.

For completeness, the claimed lower mass in Step 7 is elementary apart
from Euler's standard theorem `sum_p 1/p=infinity`.  Greedily distribute
the primes at most `Y` among `r` boxes, always placing the next reciprocal
prime weight in a currently lightest box.  The box sums differ by at most
`1/2`, so each is at least `L(Y)/r-O(1)`.  Products formed by taking one
prime from each box are distinct, squarefree, have `Omega=r`, and are at
most `Y^r`; the sum of their reciprocals is exactly the product of the box
sums.  Thus fixed rank can have polylogarithmically growing harmonic mass
(using the remembered standard estimate `L(Y)=log log Y+O(1)` would give
the familiar order), but the proved upper bound still makes it
`o(log X)`.

## 4. Weakest unsupported step

Let `P_j` be pairwise disjoint prime alphabets and choose arbitrary ranks
`r_j>=1`.  The exact candidate

```
A = union_j {n : supp(v(n)) subset P_j, Omega(n)=r_j}
```

is admissible.  Each component separately has both desired sparsity
properties, but that does **not** justify summing over infinitely many
components.  The missing colored-rank inequality is

```
sum_j sum_(supp(n) subset P_j, Omega(n)=r_j) 1/(n log n) < infinity.
```

Either a proof of this inequality (preferably with a uniform constant) or
an explicit partition/rank choice violating it would decisively settle the
valuation-code route.  The fixed-rank Dirichlet bound above has constants
depending strongly on `r` and therefore does not close this step.

## 5. Concrete falsification test

The dangerous finite models use prime blocks rather than initial primes.
Partition a long interval on the `u=log p` axis into disjoint colored
blocks, and in each block choose `r` near its reciprocal-prime mass

```
L = sum_(p in block) 1/p.
```

Compute exactly (using elementary-symmetric or complete-homogeneous
recurrences) the coefficient

```
int_1^infty [z^r] product_(p in block)(1-z p^(-s))^(-1) ds.
```

Any proposed uniform colored-rank bound must survive ranks near `L`, where
the coefficient is largest.  Conversely, a numerical excess is only a
target for a rigorous interval construction, not a counterexample by
itself.

A useful analytic stress test comes from ordering a squarefree product by
its largest prime.  For the squarefree rank-`r` subfamily on one alphabet
one obtains the rigorous upper bound

```
sum_(n squarefree, Omega(n)=r, supp(n) subset P) 1/(n log n)
 <= 1/(r-1)! sum_(p in P)
       (sum_(q in P, q<=p)1/q)^(r-1)/(p log p).
```

Indeed, charge a squarefree product to its largest prime and dominate the
elementary symmetric sum of the other `r-1` reciprocal primes by the
corresponding power divided by `(r-1)!`.  The right side exposes precisely
the regime `r` comparable with accumulated reciprocal-prime mass.  For
prime powers one instead uses complete-homogeneous sums; the displayed
factorial bound must not be applied unchanged.

## 6. Next action if the route survives

Prove the colored-rank inequality by treating the disjoint prime alphabets
as colors in the cumulative reciprocal-prime measure.  In the continuous
model, if color masses have fixed proportions `delta_j` with
`sum delta_j=1`, the integral becomes
`sum_j delta_j^(r_j)<=1`; this strongly predicts convergence.  The needed
discrete proof must allow proportions that change with scale.  A viable
approach is largest-prime charging plus integration by parts in the
cumulative color masses, retaining the exponential discount from the
`1/log p` factor.  If that fails, search explicitly for scale-varying color
blocks and ranks that make the displayed largest-prime sum diverge.

## Perturbation warning

Common dilation by `c>=1` is safe, but additive perturbation is not a
formal consequence of valuation incomparability: the integer slack may be
exactly one and the perturbation term is `k epsilon_n-epsilon_m`, with
unbounded `k`.  Even a common translation of the prime level can fail:
for `A={p+theta:p prime}`, the pair `2+theta,5+theta` with `k=2` gives
`|-1+theta|<1` for `0<theta<2`.  Thus a perturbed valuation construction
must verify a new quantitative gap for every pair and every relevant `k`;
there is no generic small-perturbation lemma.
