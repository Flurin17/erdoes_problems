# Independent pattern-and-transfer audit of the finite constant-gap candidate

## Verdict

I independently checked `finite_constant_gap_ratio_grid.md`, with emphasis on
the globally disjoint factorization patterns and on the final reduction to
small primes.  I found no substantive error.  Conditional on the four
standard analytic inputs stated in Section 1 of that draft, the argument
proves an absolute density gap for every nonzero exact level of every
rational completely additive function on `[1,N]`.

There is one harmless notation error: in (27), the selected semiprime
`d=pq` lies in the numerical dyadic band indexed by `t`, not in the set
`\mathcal P_t` of primes.  None of the subsequent arguments treats `d` as a
prime; its two-prime signature is used correctly.

## 1. Why bounded local circuits cannot prove this result

Fix `0<eta<1` and an integer `K`.  If

\[
 a_1\cdots a_r=b_1\cdots b_s,\qquad r<s\leq K,
\]

and every factor belongs to `[eta N,N]`, then

\[
 (\eta N)^s\leq N^r,
 \qquad\text{so}\qquad
 N^{s-r}\leq\eta^{-s}\leq\eta^{-K}.
\]

Consequently, for `N>eta^{-K}` no unequal-length relation having at most
`K` factors on either side is contained in a fixed macroscopic slab.
Equivalently, any such relation in the slab has total multiplicity
`Omega_eta(log N)`.  A slightly different formulation is that
`[N^{1-1/(K+1)},N]` contains no unequal-length relation with both lengths at
most `K`, although that interval has density `1-o(1)`.

This explains why the candidate's `Theta((log N)^2)` family of dyadic
prime--semiprime comparisons is necessary: a fixed collection of bounded
circuits cannot give a constant deficit.

The familiar long power pattern also does not suffice by itself.  If
`q^h\leq N`, then

\[
 (qx)^h=q^h x^h
\]

shows that a level-one set cannot contain all three of `x,qx,q^h`.
Conditional on the anchor `q^h`, disjoint pairs `(x,qx)` can force a linear
deficit, but all perfect-power anchors up to `N` form an `o(N)` set and may
be deleted.  The ratio-grid construction avoids this anchor bottleneck.

## 2. Same-band modalization is globally disjoint

For a matched unequal-weight prime pair `(p,q)` in one dyadic band and a
`y`-smooth cofactor `k`, the endpoints `pk,qk` have different additive
values.  Each endpoint has exactly one prime factor greater than `y`; that
prime recovers the matched pair and division recovers `k`.  Since each prime
is used in at most one base matching, all lifted edges in Section 2 are
vertex-disjoint, including across bands.

For the full range of indices used there,

\[
 \frac{\log(N/2^{i+1})}{\log y}
\]

stays in a compact positive interval depending only on fixed `alpha`.
Thus the stated Dickman lower bound is uniform.  The disjoint matching then
really gives `sum_i r_i=o(log N)`, so all but `o(log N)` bands possess a
`1-o(1)` modal prime class.

## 3. Prime--semiprime allocation has no hidden multiplicity

The low and high fixed subbands produce, respectively, semiprimes in the
two adjacent numerical product bands.  For a fixed target band there are
only `O(log N)` source triples, each requesting
`O(2^t/(log N)^2)` primes, while a good target band contains
`Omega(2^t/log N)` modal primes.  A sufficiently small fixed allocation
constant therefore makes every assigned target prime distinct.

After multiplying by a `y`-smooth cofactor, a prime endpoint has exactly
one prime factor above `y`, whereas a semiprime endpoint has exactly two,
counted with multiplicity; squares were excluded in the equal-band case.
The complete large-prime signature recovers the assigned base and then the
cofactor.  Hence the lifted ratio-grid edges are globally vertex-disjoint.
Each failed shifted or unshifted profile equation consequently costs
`Omega_alpha(N/(log N)^2)` distinct missing vertices.

## 4. Shifted Cauchy stability

The proof of the stability lemma is valid.  Comparing

\[
 F(x+h)+F(z)=G(x+h+z),\qquad
 F(x)+F(z+h)=G(x+z+h)
\]

shows that almost every increment of each admissible length has one modal
value.  The three-increment identity makes those modal increments additive,
so they are `hu`.  An averaging anchor then gives `F(x)=ux+v` off `o(n)`
points, and triangular representation counts give
`G(s)=us+2v` off `o(n)` points.  The shifted equation forces `u=0`; the
macroscopic overlap of the input and output intervals forces `v=0`.

At the extreme pair `(n-1,n-1)`, the shifted output is the unused endpoint
`2n-1`.  Omitting that single pair, as the draft does, removes the only
endpoint nuisance and changes no asymptotic estimate.

It follows correctly that the nonzero-weight primes between `N^alpha` and
`N^{1-4alpha+o(1)}` have reciprocal mass `o(1)`.

## 5. The small-prime transfer is uniform enough

For a `y`-smooth exponent vector with associated integer `d`, the exact
uniform and independent-geometric masses are

\[
 \frac{\Phi(N/d,y)}N,
 \qquad
 \frac{V(y)}d.
\]

This proves the total-variation identity (64).  On the interior
`d\leq N/y^{u/2}`, the standard rough-number fundamental lemma applies
uniformly.  In the independent model,

\[
 \mathbb E\log d
 =\sum_{p\leq y}\frac{\log p}{p-1}
 =(1+o(1))\log y,
\]

so Markov gives boundary mass `O(1/u)`.  Normalization and the relative
interior comparison give the same bound for the actual boundary mass.
Thus the claimed `epsilon(u)+o(1)` total-variation estimate, with
`epsilon(u)\to0`, follows in the stated order of quantifiers.

The independent-geometric atom lemma is also correct.  Sparse active
reciprocal mass makes a nonzero atom sparse; one active prime with
`1/p\geq1/8` caps every convolution atom at `7/8`; otherwise a greedy
subcollection of reciprocal mass in `[1/8,1/4)` has zero atom at most

\[
 e^{-1/8}+\frac1{32}<0.915
\]

and every nonzero atom below `1/4`.  Convolution cannot increase a maximum
atom.

The high-prime union bound loses only
`-log(1-4alpha)+o(1)`.  Choosing one sufficiently small fixed `alpha` makes
this loss and the transfer error smaller than the fixed geometric atom gap,
contradicting a level of density `1-o(1)`.

## Conclusion

The candidate is dependency-complete once the stated standard
rough-number estimate is accepted.  It proves the finite
repetition-allowed assertion is negative.  This audit does not address the
internally distinct-factor convention.
