# Route: logarithmic combs, finite-rank supports, and torus obstructions

## Status

This route proves several self-contained special cases and an exact
fixed-prefix torus inequality.  It does **not** solve the full problem.  Its
main negative conclusion is that neither finite abstract multiplicative rank
nor qualitative equidistribution supplies the uniform multiscale estimate
needed in the general case.

Throughout, (A\subset(1,\infty)) is admissible in the sense of
`PROBLEM.md`.  For (x<y), both ordered orientations in the original
hypothesis are available.  In fact the pair condition is exactly
\[
 x\,\operatorname {dist}(y/x,\mathbb Z)\geq 1.                 \tag{1}
\]
Indeed the nearest integer to (y/x>1) is positive, while in the reversed
orientation (ky-x\geq y-x\geq1) for every (k\geq1).  Equality in (1) is
allowed.

## 1. Proper finite-dimensional logarithmic supports

The useful finite-rank hypothesis is properness of log-height, not abstract
rank by itself.

### Lemma 1 (polynomial log-counting)

Let (B\subset(1,\infty)), and suppose that for constants (C,d<\infty),
\[
 \#\{x\in B:x\leq e^T\}\leq C(1+T)^d\qquad(T\geq0).           \tag{2}
\]
Then
\[
 \sum_{x\in B}\frac1x<\infty.
\]
Consequently both conclusions in the problem hold for (B), and in fact
(H_B(t)=O(1)).

**Proof.**  The contribution of the shell
([e^j,e^{j+1})) is at most
(C(j+2)^d e^{-j}), whose sum over (j\geq0) converges.  Condition (2) also
makes (B\cap(1,e)) finite.  Thus its finitely many weighted terms are
finite, and for (x\geq e),
(1/(x\log x)\leq1/x).  Finally (H_B(t)\leq\sum_B1/x=O(1)), so
(H_B(t)/\log t\to0).  The strict cutoff (x<t) is immaterial.  \(□\)

The following formulation includes positive multiplicative monoids and
low-dimensional logarithmic combs.

### Theorem 2 (coercive log-lattice special case)

Let (L\subset\mathbb R^r) be a lattice, let (S\subset L), and let
(\ell:\mathbb R^r\to\mathbb R) be linear.  Suppose
\[
 \ell(v)\geq a\lVert v\rVert-B\qquad(v\in S)                 \tag{3}
\]
for some (a>0) and (B<\infty).  For fixed real shifts
(b_1,\ldots,b_J), every subset
\[
 A\subset
 \bigcup_{j=1}^J\{\exp(b_j+\ell(v)):v\in S\}\cap(1,\infty) \tag{4}
\]
satisfies
\[
 \sum_{x\in A}\frac1x<\infty,
 \qquad
 \sum_{x\in A}\frac1{x\log x}<\infty,
 \qquad
 H_A(t)=O(1)=o(\log t).
\]
Admissibility is not needed for this theorem.

**Proof.**  If (0<b_j+\ell(v)\leq T), (3) gives
(\lVert v\rVert\leq (T-b_j+B)/a).  A fixed (r)-dimensional lattice has
(O((1+T)^r)) points in such a ball (cover a containing box by finitely many
translates of a bounded fundamental cell).  Taking the union over the
finitely many shifts proves (2); apply Lemma 1.  \(□\)

Here are three concrete corollaries.

1. If (q_i>1), (c_j>0), and
   \[
   A\subset\bigcup_{j=1}^J
       \left\{c_j\prod_{i=1}^r q_i^{n_i}:n_i\in\mathbb Z_{\geq0}\right\},
   \]
   then, even more directly,
   \[
   \sum_{x\in A}\frac1x
   \leq\sum_{j=1}^Jc_j^{-1}\prod_{i=1}^r(1-q_i^{-1})^{-1}<\infty. \tag{5}
   \]
   Collisions between exponent vectors only decrease the left side.

2. A finite union of geometric rays
   (\{c_jq_j^n:n\in\mathbb Z, c_jq_j^n>1\}), or more generally a finite
   union of chains with a uniform ratio (a_{n+1}/a_n\geq q>1), has
   convergent total reciprocal sum.

3. Every nonzero topologically discrete additive subgroup of
   (\mathbb R) is (\delta\mathbb Z).  To see this, discreteness gives a
   neighborhood of zero containing no nonzero group element.  A sequence of
   positive elements tending to their infimum is therefore eventually
   constant, so a least positive element (\delta) exists.  Euclidean
   division by (\delta) then shows that every group element is an integer
   multiple of it.  Thus if
   (\log A\subset b+\Lambda) for a genuine discrete lattice
   (\Lambda\leq\mathbb R), then (A) lies on one geometric ray and both
   conclusions follow.

The word *discrete* is essential in item 3.  An abstract finite-rank subgroup
such as (\mathbb Z\log2+\mathbb Z\log3) is dense in (\mathbb R), not a
lattice in the topological sense.

### Proposition 3 (integer-generator refinement)

Suppose all (q_i\geq2) in (5) are integers.  An admissible (A) contained
in the displayed finite union is finite.

**Proof.**  If (A) were infinite, one seed (c_j) would contain infinitely
many assigned points.  Choose one exponent vector in
(\mathbb Z_{\geq0}^r) for each such point.  Dickson's lemma says that two
distinct vectors satisfy (n\leq m) coordinatewise.  For completeness,
Dickson's lemma follows by induction on (r): in an infinite sequence of
vectors, either some first coordinate occurs infinitely often, when apply
induction to that subsequence, or there is a subsequence with strictly
increasing first coordinate, from which induction on the remaining
coordinates selects a comparable pair.  The associated distinct points then
satisfy
\[
 y/x=\prod_iq_i^{m_i-n_i}\in\mathbb Z_{\geq2},
\]
contradicting (1).  \(□\)

### Proposition 4 (exact single-ray test)

For (q>1,c>0) and (E\subset\mathbb Z), put
(A_E=\{cq^n:n\in E, cq^n>1\}).  The pair corresponding to (n<m), with
(s=m-n), is admissible exactly when
\[
 cq^n\,\operatorname {dist}(q^s,\mathbb Z)\geq1.             \tag{6}
\]
In particular:

- if (q^s) is an integer for some (s\geq1), each residue class of
  exponents modulo (s) contains at most one member of (E), so
  ​(\#E\leq s);
- a full tail (E=\{n\geq N\}) is admissible exactly when
  \[
  \delta(q):=\inf_{s\geq1}\operatorname {dist}(q^s,\mathbb Z)>0
  \quad\hbox{and}\quad cq^N\delta(q)\geq1.                  \tag{7}
  \]

This is only a characterization; it does not assert that a familiar
nonintegral (q) has (\delta(q)>0).

## 2. Why abstract finite rank is insufficient locally

### Proposition 5 (rank-two groups contain thick admissible finite blocks)

Let
\[
 G=\{2^a3^b:a,b\in\mathbb Z\}.
\]
For every fixed (0<\varepsilon<1/10) and all sufficiently large (T), (G)
contains an admissible set (B_T\subset[T,2T-1]) of cardinality at least
(c_\varepsilon T).

**Proof.**  The additive group
(\mathbb Z\log2+\mathbb Z\log3) is dense in (\mathbb R): the usual
pigeonhole argument makes nonzero integer combinations arbitrarily close to
zero because (\log2/\log3\notin\mathbb Q), and their integer translates
approximate every real number.  The irrationality follows from unique
factorization.  Exponentiating shows that (G) is dense in
((0,\infty)).

Choose centers
\[
 z_i=T+2\varepsilon+i(1+3\varepsilon)
\]
as long as (z_i\leq2T-1-2\varepsilon), and choose distinct
(g_i\in G) with ​(|g_i-z_i|<\varepsilon).  Consecutive selected points
are separated by more than (1+\varepsilon), and all lie in
([T+\varepsilon,2T-1-\varepsilon]).  If (x<y) are selected, then (k=1)
is safe, while for (k\geq2),
\[
 kx-y\geq2(T+\varepsilon)-(2T-1-\varepsilon)=1+3\varepsilon.
\]
The reverse orientation is automatic.  Thus the set is admissible and has
linear cardinality.  \(□\)

The same cancellation already occurs in the semigroup
(\{2^a3^{-b}:a,b\geq0\}).  Hence a fixed number of generators, without the
coercivity (3), cannot imply a polylogarithmic one-shell occupancy bound.
Proposition 5 is finite and therefore does not refute either global
conclusion; it shows that cross-scale depletion is indispensable.

## 3. The exact fixed-prefix torus bound

The half-unit thickening turns harmonic mass into logarithmic measure.  Put
\[
 I_a=(a-½,a+½),\qquad E=\bigcup_{a\in A}I_a.
\]
The intervals (I_a) are disjoint.  Since an infinite admissible set lies in
([2,\infty)),
\[
 \int_{I_a}\frac{dt}{t}
 =\log\frac{a+1/2}{a-1/2}=\frac1a+O(a^{-3}).                 \tag{8}
\]
The sum of the errors converges because the increasing enumeration satisfies
(a_j\geq a_1+j-1).  At a cutoff only (O(1)) intervals meet the boundary.
Consequently, uniformly for (T\geq2),
\[
 \int_{E\cap[3/2,T]}\frac{dt}{t}=H_A(T)+O(1).                \tag{9}
\]

Fix an initial prefix (B=\{x_1,\ldots,x_m\}) of (A), and define
\[
 \alpha=(1/x_1,\ldots,1/x_m),\qquad
 \mathbb H_B=\overline{\{t\alpha\pmod{\mathbb Z^m}:t\in\mathbb R\}},
\]
\[
 R_B=\left\{\theta\in\mathbb H_B:
       \lVert\theta_i\rVert_{\mathbb R/\mathbb Z}\geq\frac1{2x_i}
       \ (1\leq i\leq m)\right\},
 \qquad p(B)=\mu_{\mathbb H_B}(R_B),                         \tag{10}
\]
where ​(\mu_{\mathbb H_B}) is normalized Haar measure.

### Theorem 6 (fixed-prefix torus inequality)

For every fixed finite initial prefix (B\subset A),
\[
 \limsup_{T\to\infty}\frac{H_A(T)}{\log T}\leq p(B).        \tag{11}
\]

**Proof.**  If (t\in I_a) and (a>x_m), then for every (i) and positive
integer (k), admissibility and the open definition of (I_a) give
\[
 |t-kx_i|\geq|a-kx_i|-|t-a|>1/2.
\]
Nonpositive multiples are farther away.  Hence the tail of (E) is
contained in
\[
 F_B=\{t:t\alpha\pmod1\in R_B\}.                            \tag{12}
\]

The boundary of (R_B) has Haar measure zero.  Indeed, it is contained in
finitely many fibers ​(\theta_i=\pm1/(2x_i)); the (i)-th coordinate
projection of ​(\mathbb H_B) is all of the circle (the real parameter
(t/x_i) already traverses it), so projected Haar measure is uniform and a
point fiber has measure zero.

For a nontrivial character ​(\chi_n) of ​(\mathbb H_B), one has
(n\cdot\alpha\ne0); otherwise the character is one on the dense defining
orbit and hence trivial.  Direct integration gives
\[
 \frac1U\int_0^U\chi_n(t\alpha)\,dt\longrightarrow0.
\]
Approximation by characters, followed by upper and lower continuous
approximations to the boundary-null indicator of (R_B), gives
\[
 M(U):=\int_0^U1_{F_B}(t)\,dt=p(B)U+o(U).                   \tag{13}
\]
Partial summation now yields
\[
 \int_1^T\frac{1_{F_B}(t)}t\,dt=p(B)\log T+o(\log T).       \tag{14}
\]
Explicitly, write (M(t)=p(B)t+r(t)), (r(t)=o(t)), and integrate
(dM(t)/t); after any fixed threshold the error integral is bounded by
(\varepsilon\log T).  Equations (9), (12), and (14) prove (11).  \(□\)

If (1/x_1,\ldots,1/x_m) are linearly independent over (\mathbb Q), then
​(\mathbb H_B=\mathbb T^m), and
\[
 p(B)=\prod_{i=1}^m(1-1/x_i).                               \tag{15}
\]
It follows rigorously that if the entire reciprocal family
​(\{1/x:x\in A\}) is (\mathbb Q)-linearly independent, then the second
conclusion of the problem holds.  If ​(\sum_A1/x<\infty), this is immediate.
Otherwise the products in (15) tend to zero; apply (11) for each fixed
prefix and then let the prefix grow.  This argument does **not** prove
​(\sum_A1/(x\log x)<\infty) in the divergent-harmonic branch.

More generally, if
(r=\dim_{\mathbb Q}\operatorname {span}\{1/x_i:1\leq i\leq m\}), choose a
​(\mathbb Q)-basis and clear denominators.  Then for suitable
​(q_i\in\mathbb Z^r),
\[
 p(B)=\operatorname {Leb}_{\mathbb T^r}
 \left\{\theta:\lVert q_i\cdot\theta\rVert
       \geq\frac1{2x_i}\quad(1\leq i\leq m)\right\}.        \tag{16}
\]
Dependent coordinates are character strips on the correct orbit torus, not
independent coordinates on (\mathbb T^m).

### Exact rank-one resonance calculation

Let (x_i=cn_i), where (c\geq1), (n_i\in\mathbb Z_{>0}), and
(D=\operatorname {lcm}(n_1,\ldots,n_m)).  Parameterizing the orbit by
(u=t/(cD)\pmod1), the (i)-th forbidden condition pulls back to arcs of
radius (1/(2cD)) about the grid points (j n_i/D).  These arcs are
disjoint, apart from harmless endpoint contact when (c=1).  Therefore
\[
 p(B)=1-\frac{N}{cD},\qquad
 N=\#\left(\bigcup_i n_i\mathbb Z\pmod D\right).             \tag{17}
\]
For example, (n_1=6,n_2=10) gives (D=30,N=7), so
\[
 p(B)=1-\frac7{30c},
\]
not the independent product
((1-1/(6c))(1-1/(10c))).

For distinct primes (n_i), inclusion-exclusion gives
\[
 p(B)=1-\frac1c+\frac1c\prod_i(1-1/n_i).                   \tag{18}
\]
The infinite set ​(\{cp:p\text{ prime}\}) is admissible for (c\geq1):
for (p<q), every nonzero integer (kp-q) has absolute value at least one,
and equality is allowed after multiplication by (c).  By Euler's standard
theorem ​(\sum_p1/p=\infty), the products in (18) tend to zero.  Thus for
(c>1), the harmonic sum of these prefixes diverges while their ambient safe
volume tends only to (1-1/c>0).  The unfilled fraction consists of
carrier/lattice gaps.  This is an exact obstruction to deducing depletion
from ​(\sum1/x_i) without accounting for resonances.

## 4. Growing dimension and logarithmic-coordinate failures

### Proposition 7 (no dimension-uniform equilibration)

For arbitrarily large (T), there is an admissible set
(B_T=\{x_1,\ldots,x_m\}\subset[T,3T/2]), with (m\asymp T), whose
reciprocals are ​(\mathbb Q)-linearly independent, such that every point of
\[
 W_T=[3T/2+1,2T-1]
\]
is safe from all half-unit multiple combs belonging to (B_T), although the
full-torus equilibrium safe volume is at most a fixed constant less than one.

**Proof.**  Take (m=\lfloor T/4\rfloor) tiny pairwise disjoint intervals
around (T+2j), with their last center below (3T/2-2).  Inductively select
(x_j) in the (j)-th interval so that (1/x_j) avoids the countable
​(\mathbb Q)-span of the previous reciprocals.  Choose the intervals small
enough that gaps exceed one.  The set lies in ​([T,2T-1]), so it is
admissible by the same-block calculation: for (x<y), (k=1) is safe and
(kx-y\geq2x-y\geq1) for (k\geq2).

For (z\in W_T), both (z-x_j\geq1) and (2x_j-z\geq1); all other integer
multiples are farther away.  Thus the actual safe fraction on (W_T) is one.
On the other hand, by (15),
\[
 p(B_T)=\prod_j(1-1/x_j)
 \leq\exp\left(-\sum_j1/x_j\right)\leq e^{-1/7}
\]
for all sufficiently large (T).  \(□\)

The first invalid step in a naive torus proof is therefore replacing the
one-parameter orbit by Haar measure on the full torus.  Even when reciprocal
frequencies are independent and the full torus is correct for each fixed
prefix, qualitative equidistribution has no uniformity as the number and
size of frequencies change with the shell.  Proposition 7 gives a constant
finite-horizon discrepancy when (m\asymp T).

Passing instead to logarithms does not remove resonance.  For (u=\log x),
the exact intervals forbidden to (v=\log y) are
\[
 \bigl(\log(kx-1),\log(kx+1)\bigr),
\]
with asymmetric radii and width asymptotic to (2/(kx)).  Combs from (x)
and (y) overlap when (kx\approx \ell y).  Admissibility excludes only
(y\approx k'x), not general common-multiple relations with
(k,\ell\geq2).  Moreover the additive rank of
​(\{\log k:k\leq K\}) is the number of primes at most (K): composites
factor into prime logs, and prime-log independence follows from unique
factorization.  The relevant log-translate dimension therefore grows.

## 5. Dependency graph, limitations, and falsification tests

The proved dependencies are
\[
 \text{coercive log support}
 \Longrightarrow \text{polynomial log count}
 \Longrightarrow \sum1/x<\infty
 \Longrightarrow \begin{cases}
   \sum1/(x\log x)<\infty,\\
   H_A(t)=o(\log t),
 \end{cases}
\]
and independently
\[
 \text{half-unit thickening}+
 \text{fixed-prefix orbit closure}
 \Longrightarrow \limsup H_A(t)/\log t\leq p(B).
\]
For a general proof by the latter route, the remaining nodes would be:

1. prove a carrier-sensitive estimate forcing effective depletion inside
   resonant safe channels (the ambient statement is false by (17)--(18));
2. choose prefixes on successive shells with discrepancy errors summable
   after weighting by (1/j);
3. obtain ​(\sum_j[p_j+\Delta_j]/j<\infty) for the first target.

Qualitative unique ergodicity proves none of these three nodes.  Even a proof
that (p_j\to0) would yield only (H_A(t)=o(\log t)), with no integrable rate
for the weighted series.

Concrete falsification tests for any extension are:

- replacing (n_i\geq0) by signed exponents for (2,3) must invalidate the
  properness step, as Proposition 5 demonstrates;
- an integer (q) in Proposition 4 must permit at most one exponent, and
  (q^s\in\mathbb Z) must permit at most (s);
- the prefix (\{6c,10c\}) must give (17), not an independence product;
- a proposed finite-rank local occupancy bound must survive the dense
  rank-two blocks of Proposition 5;
- a proposed dimension-uniform discrepancy estimate must survive
  Proposition 7;
- every thickening argument must retain the open forbidden intervals,
  equality cases, both original orientations, and the fact that the relevant
  multiplier depends on the pair.

The present precise bottleneck is a multiscale, carrier-conditioned comb
coverage inequality.  One-shell density, abstract relation rank, and
unquantified torus equidistribution are each rigorously insufficient.
