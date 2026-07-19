# Martingale/influence analysis for a moving additive grading

Let
\[
 f(n)=\sum_{p\leq N}w_pv_p(n),\qquad
 P=\{p\leq N:w_p\neq 0\},
\]
where the weights are arbitrary nonzero real numbers on `P`.  The level of
interest for product-length rigidity is a **nonzero** level (normalized to
`1`).  This qualification matters: by putting a nonzero weight on one prime
near `N`, the zero atom has density tending to one, so no upper bound below
one for the unrestricted maximal atom can hold.

This note records the exact conditional model, two rigorous consequences,
and the obstruction to a generic martingale or Efron--Stein proof of a
constant gap.

## 1. Exact active-prime fibers

For `n <= N`, remove all active-prime powers and write
\[
 n=r(n)\prod_{p\in P}p^{a_p(n)},\qquad (r(n),\prod_{p\in P}p)=1.
\]
For a fixed possible core `r`, put
\[
 D_r=\left\{a\in\mathbb Z_{\geq0}^{P}:
 r\prod_{p\in P}p^{a_p}\leq N\right\}.
\]
Conditioned on `r(n)=r`, the exponent vector is exactly uniform on `D_r`:
each vector represents one integer.  Moreover `f(r)=0`, so
\[
 \Pr(f(n)=t\mid r(n)=r)
 =\frac{\#\{a\in D_r:\sum_pw_pa_p=t\}}{|D_r|}.                 \tag{1}
\]
Thus the appropriate martingale is not a product-coordinate martingale.  It
is a mixture of uniform measures on logarithmic knapsack down-sets `D_r`.
The product constraint can make the coordinates maximally negatively
dependent.

## 2. One-coordinate conditioning: the exact chain bound

**Lemma 1 (prime-chain bound).**  If `w_q != 0`, then for every real `t`,
\[
 \#\{n\leq N:f(n)=t\}\leq N-\lfloor N/q\rfloor.              \tag{2}
\]
Equivalently, every such level deletes at least `floor(N/q)` integers.

**Proof.**  Partition `[1,N]` into the disjoint `q`-adic chains
\[
 C_m=\{m,mq,\ldots,mq^{L_m}\},\qquad q\nmid m.
\]
Along a chain the values are `f(m)+j w_q`, hence are distinct, so a level
uses at most one point of each chain.  The number of chains is the number of
integers at most `N` not divisible by `q`, namely
`N-floor(N/q)`.  This proves (2).  \(\square\)

There is also an exact conditional-probability interpretation.  Given the
`q`-free part `m=n/q^{v_q(n)}`, the exponent is uniform on
`{0,...,L_m}`.  A level has conditional probability at most
`1/(L_m+1)`.  Averaging, with
`Pr(m)=(L_m+1)/N`, gives exactly the number-of-chains bound.

For a nonzero target this immediately combines with smooth-number support.
If `q_0` is the smallest active prime and `E={n<=N:f(n)!=t}`, then
\[
 |E|\geq \max\left(\lfloor N/q_0\rfloor,\Psi(N,q_0^- )\right),             \tag{3}
\]
where `Psi(N,q_0^-)` counts integers at most `N` all of whose prime factors
are smaller than `q_0`.  Indeed all those integers have value zero.  This is
the elementary martingale form of the previously found smooth/chain
dichotomy; optimizing it is subconstant and therefore cannot settle the
finite density-one question.

## 3. Full Boolean subfibers: a Littlewood--Offord deletion lemma

Martingale coordinates do give more when several active primes can be
toggled simultaneously.

**Lemma 2 (multiplicative-cube bound).**  Let `q_1,...,q_k` be distinct
active primes, put `Q=product_i q_i`, and let
`B_k=binom(k,floor(k/2))`.  Every level set `A={n<=N:f(n)=t}` satisfies
\[
 N-|A|\geq (2^k-B_k)
 \left(\frac NQ\prod_{i=1}^k(1-1/q_i)-2^k\right).             \tag{4}
\]
The right side may of course be replaced by zero when the displayed
parenthesis is negative.

**Proof.**  For every `b<=N/Q` coprime to `Q`, the `2^k` integers
\[
 \mathcal C_b=\left\{b\prod_{i\in S}q_i:S\subseteq[k]\right\}
\]
lie in `[1,N]`, and these cubes are pairwise disjoint.  On this cube the
grading is
\[
 f(b)+\sum_{i\in S}w_{q_i}.
\]
Replace the membership bit of coordinate `i` by its complement whenever
`w_{q_i}<0`.  Up to an additive constant this becomes a subset sum with all
coefficients `|w_{q_i}|>0`.  Subsets having one fixed sum form an antichain,
so Sperner's theorem bounds their number by `B_k`.  Hence every cube has at
least `2^k-B_k` deleted vertices.

Finally, inclusion--exclusion gives
\[
 \#\{b\leq N/Q:(b,Q)=1\}
 =\sum_{d\mid Q}\mu(d)\lfloor N/(Qd)\rfloor
 \geq \frac NQ\frac{\varphi(Q)}Q-2^k.
\]
Multiplying the two estimates proves (4).  \(\square\)

This is a genuine multi-coordinate anticoncentration statement, valid for
arbitrary signs and magnitudes.  Its limitation is structural: the cost of
a full cube is the product `Q`.  If all active primes move to infinity, (4)
does not supply a constant-density deletion bound.

## 4. The sharp star-fiber obstruction

Take
\[
 P_N=\{p:\sqrt N<p\leq N\},\qquad w_p=1\ (p\in P_N),
\]
and zero weights elsewhere.  An integer at most `N` has at most one active
prime divisor, and that divisor occurs to the first power.  Consequently
\[
 A_N=\{n\leq N:f(n)=1\}
\]
is the disjoint union of the multiples of the primes in `P_N`, and
\[
 |A_N|=\sum_{\sqrt N<p\leq N}\lfloor N/p\rfloor,
 \qquad \frac{|A_N|}{N}\longrightarrow \log 2.               \tag{5}
\]
Here the last assertion follows from the usual prime harmonic-sum estimate;
the total floor error is `O(pi(N))=o(N)`.

More revealingly, fix an active-prime-free core `r`.  Its exact fiber is
\[
 D_r=\{0\}\cup\{e_p:\sqrt N<p\leq N/r\}.                     \tag{6}
\]
If there are `d_r` available primes, the conditional mass of the level one
is
\[
 \frac{d_r}{d_r+1},                                           \tag{7}
\]
which can be arbitrarily close to one.  Every coordinate is nonconstant,
but the feasibility constraint makes the coordinates mutually exclusive.
This is precisely the configuration in which coordinate-influence
arguments lose their force: all leaf-to-level transitions are charged to
the one off-level center.

For comparison, replacing these divisibility indicators by independent
Bernoulli variables gives total parameter
`sum_{sqrt(N)<p<=N}1/p -> log 2` and probability of exactly one active prime
tending to `(log 2)/2`, only half of the true value in (5).  Thus a product
model or independent-coordinate Efron--Stein inequality is not even
asymptotically accurate in this boundary regime.

One can see the same issue spectrally.  On the uniform star
`{0,e_1,...,e_d}`, random-scan single-coordinate heat-bath dynamics moves
between the center and a specified leaf with probability `1/(2d)` in each
direction.  Leaf-difference eigenfunctions have eigenvalue
`1-1/(2d)`, so the spectral gap is `1/(2d)`.  There is no dimension-free
Poincare constant for the conditional fibers (1).

Finally, the Doob identity
\[
 \operatorname{Var}(1_A)=\sum_j
 \mathbb E\bigl[(M_j-M_{j-1})^2\bigr]
\]
does not distinguish an atom of mass `epsilon` from one of mass
`1-epsilon`: both have variance `epsilon(1-epsilon)`.  In the star, the
near-one conditional atom (7) simply has correspondingly tiny variance.
Therefore a variance-only or influence-only argument cannot prove the
needed upper bound away from one without an additional geometric statement
that rules out or globally charges star-like boundary fibers.

## 5. What a successful martingale route would still need

The exact missing ingredient is a cross-fiber charging lemma.  It would have
to show that if many fibers `D_r` have a near-full affine slice, then their
off-level centers (or higher codimension faces) occur at enough different
integer scales to have positive total uniform density.  Lemmas 1 and 2 only
charge within one chain or within full cubes; example (6) shows why no
statement about an isolated fiber can suffice.

Thus the useful rigorous output of this route is (2)--(4), while the first
invalid inference in a naive Efron--Stein proof is treating the active prime
valuations as independent, or assuming their conditional measures have a
uniform spectral gap.  Both claims are falsified exactly by (6).
