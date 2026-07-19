# Independent probabilistic prime weights: a rigorous obstruction

## Question tested

Can one choose rational prime weights independently (possibly by randomized
rounding or an LLL argument) so that the completely additive function

\[
 F_w(n)=\sum_{p\leq N}v_p(n)w_p
\]

has an exact nonzero level containing \((1-o(1))N\) integers up to \(N\)?
The answer is negative for the standard independent product measures.  In
fact, a nondegenerate product measure normally forces anti-concentration, and
large random ranges normally make all the values distinct.  This does not
rule out a highly correlated construction, but it shows that independence or
a direct variable-LLL is not supplying the missing mechanism.

## 1. Product-measure anti-concentration

### Proposition 1 (bounded-grid independent weights)

Fix \(0<\alpha<1\).  For every prime \(p\leq N\), let \(W_p\) be independent,
and suppose

\[
 \sup_x \Pr(W_p=x)\leq\alpha.                                      \tag{1}
\]

Suppose also that all \(W_p\) lie on one rational grid
\(D_N^{-1}\mathbb Z\), and that \(|D_NW_p|\leq H_N\) surely, where
\(H_N=N^{O(1)}\).  Put

\[
 X_t(W)=\#\{n\leq N:F_W(n)=t\}.
\]

Then, in probability,

\[
 \max_t X_t(W)\leq (\alpha+o(1))N.                                \tag{2}
\]

The same proof permits \(\log H_N=N^{o(1)}\), equivalently
\(\log H_N=o(N^c)\) for every fixed \(c>0\), rather than the displayed
polynomial hypothesis.

### Proof

Fix an integer \(u\geq2\), put \(y=N^{1/u}\), and write
\(S=\Psi(N,y)\) for the number of \(y\)-smooth integers up to \(N\).
Condition on all \(W_p\) with \(p\leq y\).  If \(n\) is not \(y\)-smooth,
choose one prime \(q(n)>y\) dividing it.  After conditioning on all weights
except \(W_{q(n)}\), the equation \(F_W(n)=t\) determines at most one value
of \(W_{q(n)}\): its coefficient is the nonzero integer
\(v_{q(n)}(n)\).  Hence (1) gives

\[
 \mathbb E(X_t\mid (W_p)_{p\leq y})
 \leq S+\alpha(N-S)
 \leq \alpha N+(1-\alpha)S.                                      \tag{3}
\]

Changing one coordinate \(W_p\), for \(p>y\), can change \(X_t\) only on
multiples of \(p\), and therefore has bounded difference at most \(N/p\).
Consequently

\[
 \sum_{p>y}(N/p)^2
 \leq N^2\sum_{m>y}m^{-2}
 \leq N^2/y.                                                       \tag{4}
\]

McDiarmid's inequality, still conditional on the small-prime weights, now
implies, for every fixed \(\varepsilon>0\),

\[
 \Pr\left(X_t>\alpha N+(1-\alpha)S+\varepsilon N
       \mid (W_p)_{p\leq y}\right)
 \leq \exp(-2\varepsilon^2y).                                    \tag{5}
\]

There are at most

\[
 2H_N\lfloor\log_2N\rfloor+1                                   \tag{6}
\]

possible values of \(D_NF_W(n)\), because
\(\Omega(n)\leq\log_2N\).  Thus (5) and a union bound show, with probability
\(1-o(1)\),

\[
 \max_tX_t\leq \alpha N+(1-\alpha)\Psi(N,N^{1/u})+\varepsilon N. \tag{7}
\]

For fixed \(u\), the standard smooth-number asymptotic gives
\(\Psi(N,N^{1/u})/N\to\rho(u)\). Since \(\rho(u)\to0\), given
\(\delta>0\), choose a fixed \(u\) with
\((1-\alpha)\rho(u)<\delta/2\), then choose
\(\varepsilon<\delta/2\), and finally let \(N\to\infty\). This proves (2).
Only the much weaker standard Rankin bound
\(\lim_{u\to\infty}\limsup_N\Psi(N,N^{1/u})/N=0\) is actually needed. \(\square\)

### Consequences

* Independent fair binary or sign weights have, with high probability, no
  level larger than \((1/2+o(1))N\).
* Uniform \(q\)-ary weights have no level larger than
  \((1/q+o(1))N\).
* The proof is unchanged for non-identically distributed weights as long as
  the uniform point-mass cap (1) holds.
* If the cap is \(1-\eta_N\) with \(\eta_N\to0\), the proof gives only an
  upper bound \((1-\eta_N+o(1))N\), with no assertion that the error is
  \(o(\eta_N)\). Such a law is an almost deterministic perturbation, so the
  deterministic modal structure has to be supplied before the randomness is
  introduced.

This also explains the failure of independent randomized rounding of a
logarithmic profile whenever, for a suitable \(y=N^{1/u}\), all but \(o(N)\)
integers have a prime divisor \(p>y\) whose rounding bit is uniformly
nondegenerate: exact equality is then anti-concentrated rather than
concentrated.

## 2. A large random range is maximally bad

### Proposition 2 (generic integer weights are injective)

Let the \(W_p\) be independent and uniform on \(\{1,\ldots,Q\}\).  Then

\[
 \Pr\bigl(F_W(m)=F_W(n)\text{ for some }1\leq m<n\leq N\bigr)
 \leq \frac{N(N-1)}{2Q}.                                         \tag{8}
\]

In particular, if \(Q/N^2\to\infty\), every exact level on \([1,N]\) is a
singleton with probability \(1-o(1)\).

### Proof

For a fixed pair \(m\ne n\), choose a prime \(p\) for which
\(v_p(m)-v_p(n)\ne0\).  Conditional on all other weights, equality is a
nontrivial linear equation in \(W_p\), and therefore permits at most one of
its \(Q\) possible values.  Thus the collision probability is at most
\(1/Q\).  Sum over the fewer than \(N^2/2\) pairs. \(\square\)

Thus a continuous or high-entropy random-hyperplane heuristic points in the
opposite direction from the desired construction: generic hyperplanes meet
the valuation vectors sparsely.

## 3. Why the direct variable-LLL certificate fails

Fix a proposed target \(t\) and a predetermined retained set \(A\).  In the
usual variable formulation one declares

\[
 B_n=\{F_W(n)\ne t\},\qquad n\in A,
\]

to be the bad events.  If \(n\) contains a random coordinate satisfying
(1), convolution cannot increase its largest point mass, so

\[
 \Pr(B_n)\geq1-\alpha=:\eta.                                     \tag{9}
\]

Events whose integers are divisible by the same random prime form a clique
in the standard variable-dependency graph.  There is an elementary exact
obstruction to the asymmetric LLL on such a clique.

### Lemma 3 (clique obstruction)

Let \(p_i=\Pr(B_i)\) (or let \(p_i\) be chosen upper bounds for these
probabilities). If the asymmetric LLL inequalities

\[
 p_i\leq x_i\prod_{j\in\Gamma(i)}(1-x_j),\qquad 0<x_i<1,           \tag{10}
\]

hold, then for every dependency clique \(K\),

\[
 \sum_{i\in K}p_i<1.                                             \tag{11}
\]

### Proof

Put \(P=\prod_{j\in K}(1-x_j)\).  Discarding neighbors outside \(K\) from
the product in (10) only enlarges its right side, so

\[
 \sum_{i\in K}p_i
 \leq P\sum_{i\in K}\frac{x_i}{1-x_i}.
\]

Writing \(z_i=x_i/(1-x_i)>0\), the right side is
\((\sum_i z_i)/\prod_i(1+z_i)<1\). \(\square\)

By (9), a clique of \(\lceil1/\eta\rceil\) retained multiples of one random
prime already makes (10) impossible. If one of the corresponding bad events
is identically true, (10) already fails; otherwise the shared prime variable
is in each event's natural variable support, so these events really do form
a clique in the ordinary variable-intersection graph. Moreover, if the
random prime coordinates collectively occur in almost every member of a set
\(|A|=(1-o(1))N\), then

\[
 \sum_{p\ \mathrm{random}}\#\{n\in A:p\mid n\}\geq(1-o(1))N.    \tag{12}
\]

Since there are only \(\pi(N)=o(N)\) prime coordinates, (12) forces a clique
of size at least \((1-o(1))N/\pi(N)\), which tends to infinity. For the fixed
\(\eta=1-\alpha>0\) in Proposition 1, the asymmetric criterion (10) therefore
cannot hold for these per-integer events on the natural variable-intersection
graph.

This is an obstruction to this *proof architecture*, not a proof that a rare
correlated assignment cannot exist. It also does not exclude a genuinely
lopsided sparser dependency graph, a different aggregate event family, or a
stronger criterion tailored to special event structure. Aggregate events or
correlated rounding would require a new structural input. Merely observing
that every deterministic assignment has positive probability in a finite
product space does not help: proving that a favorable assignment is in the
support is then exactly the original hyperplane problem.

## 4. Surviving correlated possibility

The only probabilistic-looking mechanism not covered above is a correlated
integer rounding of the ideal logarithmic profile

\[
 w_p\approx D\frac{\log p}{\log N},
\]

with \(D=o(\log N)\).  Since a uniform random integer \(n\leq N\) satisfies
\(\log n=\log N-O_{\mathbb P}(1)\), the unrounded sum is concentrated in an
interval of width \(o(1)\).  If one could round the prime coordinates so
that the additive rounding error vanished on \(1-o(1)\) of the valuation
rows, integrality would turn that interval concentration into one exact
level.  Independent rounding does not do this (Proposition 1); its errors
instead have an anti-concentrated lattice distribution.  Producing the
needed correlations is precisely a high-density discrepancy/affine-
hyperplane lemma, not an application of the ordinary LLL.

## Verdict and falsification tests

1. **Independent bounded rational weights:** rigorously eliminated by
   Proposition 1.
2. **Generic high-range rational weights:** rigorously eliminated, much more
   sharply, by Proposition 2.
3. **Direct per-integer variable-LLL:** its ordinary asymmetric criterion on
   the natural variable-intersection graph is rigorously blocked by Lemma 3
   and the incidence count (12).
4. **Correlated rounding:** remains logically possible, but its required
   lemma is exactly: find integer prime weights whose row sums take one value
   on \(N-o(N)\) valuation vectors.  No probabilistic gain has yet been
   identified.

A concrete computational falsification test for any proposed independent
law is to sample the weights and record the largest level.  Proposition 1
predicts a limiting fraction at most its largest single-coordinate atom.  A
claimed experiment substantially above that bound must be exploiting either
strong coordinate correlations or a range/support hypothesis outside the
proposition.
