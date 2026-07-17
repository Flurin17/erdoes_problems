# Resonance depletion: inverse overlap, prime thinning, and the global bottleneck

## Status and scope

This route tries to turn the forbidden unit neighborhoods of multiples into a
summable loss of available logarithmic measure.  It does not yet solve Problem
143.  It does prove an exact inverse theorem for pairwise overlap, a sharp
prime-thinned local depletion estimate, and the exact-rational part of the
resonance problem.  It also gives two rigorous divisor-cube obstructions to the
naive variance argument.  The remaining global lemma is stated precisely in
Section 9.

Throughout, (A\subset(1,\infty)) is admissible.  The quantifier on pairs is
ordered, so for distinct (x,y\in A) both orientations are available.  As
proved in `NOTES.md`, this is equivalent to checking multiples of the smaller
point, and (A) is (1)-separated and locally finite.

## 1. Half-width trains and the exact variance identity

For (x>1) and (T>0), put
\[
  \mathcal H_{x,T}
  =\bigcup_{1\le k\le \lfloor T/x\rfloor}
    (kx-\tfrac12,kx+\tfrac12),
  \qquad m_x=\lfloor T/x\rfloor .
\]
The intervals in one train are disjoint.  For distinct (x,y\in A), put
\[
 O_T(x,y)=|\mathcal H_{x,T}\cap\mathcal H_{y,T}|.
\]

### Lemma 1.1 (exact overlap and forced resonance)

One has
\[
 O_T(x,y)=
 \sum_{\substack{k\le T/x\\l\le T/y}}
       (1-|kx-ly|)_+ .                                      \tag{1.1}
\]
More generally, for a finite (X\subset A), weights (w_x\ge0), and
\[
 S=\sum_{x\in X}w_xm_x,\quad
 D=\sum_{x\in X}w_x^2m_x,\quad
 C=\sum_{\substack{x,y\in X\\x<y}}w_xw_yO_T(x,y),
\]
one has
\[
 S^2\le T(D+2C),
 \qquad
 C\ge\frac12\left(\frac{S^2}{T}-D\right).                 \tag{1.2}
\]

**Proof.**  Two open unit intervals with centers (u,v) have intersection
length ((1-|u-v|)_+), proving (1.1).  If
(F=\sum_xw_x1_{\mathcal H_{x,T}}), then
\(\int F=S\) and \(\int F^2=D+2C\).  Its support lies in an interval of
length (T), namely ((1/2,T+1/2)).  Cauchy--Schwarz gives (1.2).  Notice
that a center distance exactly (1) contributes zero, as required by the
non-strict hypothesis of the problem. \(\square\)

Thus large harmonic train mass really does force pairwise resonance.  The
problem is not detecting resonance but charging it without losing the desired
factor (1/\log x).

## 2. Determinant rigidity and an inverse-overlap theorem

### Lemma 2.1 (determinant/Farey rigidity)

Suppose
\[
 |kx-ly|<1,\qquad |k'x-l'y|<1                         \tag{2.1}
\]
for positive integers (k,l,k',l').  If
(\Delta=kl'-k'l\ne0), then
\[
 x|\Delta|<l+l',\qquad y|\Delta|<k+k'.                \tag{2.2}
\]
Consequently:

1. in a box (k,k'\le K, l,l'\le L), all incidences have one rational
   slope if (x\ge2L) or (y\ge2K);
2. if all four centers are at most (T\) and (T\le xy/2), all incidences
   have one rational slope.  Equality in (T\le xy/2) is allowed.

**Proof.**  The two determinant eliminations give
\[
 l'(kx-ly)-l(k'x-l'y)=x(kl'-k'l),
\]
and the analogous identity with (k,k'), whose right side is
(y(kl'-k'l)) up to sign.  The strict inequalities in (2.1) give (2.2).
If the integer determinant is nonzero, its absolute value is at least (1),
contradicting either stated size condition.  In the center-truncated case,
(l,l'\le T/y\le x/2) and (k,k'\le T/x\le y/2); strictness in (2.2)
again supplies the contradiction even at equality. \(\square\)

This is an inverse theorem: repeated overlaps below the product scale cannot
come from several unrelated approximating fractions.

### Lemma 2.2 (exact inverse description below the product scale)

Assume (T\le xy/2) and (O_T(x,y)>0).  There are unique coprime positive
integers (a,b) such that every contributing incidence is
\((k,l)=m(a,b)\).  Put
\[
 \delta=|ax-by|,
 \qquad
 M=\min\!\left(\left\lfloor\frac{T}{ax}\right\rfloor,
                \left\lfloor\frac{T}{by}\right\rfloor\right).
\]
Then (a,b\ge2), and exactly
\[
 O_T(x,y)=\sum_{m=1}^{M}(1-m\delta)_+.                    \tag{2.3}
\]
If (N_T(x,y)), the number of positive terms in (2.3), is at least (R),
then
\[
 a\le\frac{T}{Rx},\qquad b\le\frac{T}{Ry},\qquad
 \delta<\frac1R.                                         \tag{2.4}
\]
If instead (O_T(x,y)\ge R>0), the same two bounds hold and either
\(\delta=0\) or
\[
 \delta\le\frac1{2R}.                                    \tag{2.5}
\]
For \(\delta>0\), the exact closed form is
\[
 q-\delta\frac{q(q+1)}2,
 \quad q=\min(M,\lceil1/\delta\rceil-1).                 \tag{2.6}
\]

**Proof.**  Lemma 2.1 says all incidence vectors are proportional.  Reducing
one gives ((a,b)), and every integral vector on that ray is (m(a,b)).
Admissibility rules out (a=1), since then \(|x-by|<1\), and rules out
(b=1) in the other ordered orientation.  Formula (2.3) follows from (1.1).
If at least (R) terms occur, (M\ge R) and (R\delta<1), giving (2.4).
If the sum is at least (R), it still has at least (R) terms.  Moreover,
for \(\delta>0\), monotonicity gives
\[
 \sum_{m\ge1}(1-m\delta)_+
 \le\int_0^\infty(1-\delta t)_+\,dt=\frac1{2\delta},
\]
which gives (2.5); direct summation gives (2.6). \(\square\)

### Lemma 2.3 (Farey count in a denominator shell)

Fix (x,y>1).  Among incidences \(|kx-ly|<1\) with (L\le l<2L), the
number of distinct reduced slopes (k/l) is at most
\[
 1+\frac{8L}{x}.                                         \tag{2.7}
\]

**Proof.**  Every slope lies within (1/(Lx)) of (y/x).  Two distinct
reduced fractions whose denominators are less than (2L) are separated by
more than (1/(4L^2)), since their cross determinant is a nonzero integer.
Packing such points in an interval of length (2/(Lx)) gives (2.7).
\(\square\)

## 3. Exact rational rays

### Lemma 3.1 (LCM formula)

Let (x=\lambda m, y=\lambda n), where (m,n\) are positive integers and
\(\lambda\ge1\).  Put (L=\operatorname{lcm}(m,n)) and
(R=\lfloor T/(\lambda L)\rfloor).  Then distinct train intervals overlap
only at the common centers (\lambda L,2\lambda L,\ldots,R\lambda L), and
\[
 O_T(x,y)=R.                                               \tag{3.1}
\]
Their exact logarithmic measure is
\[
 \sum_{r=1}^{R}
 \log\frac{\lambda Lr+1/2}{\lambda Lr-1/2}
 =\frac{H_R}{\lambda L}+E,
 \qquad
 0\le E\le\frac{\zeta(3)}{9(\lambda L)^3}.               \tag{3.2}
\]

**Proof.**  A nonzero center difference is
\(\lambda|km-ln|\ge\lambda\ge1\), so positive overlap occurs exactly at
common multiples.  This proves (3.1).  Expanding
\(2\operatorname{arctanh}(1/(2\lambda Lr))\) gives its leading term
(1/(\lambda Lr)); bounding the positive tail by a geometric series gives
at most (1/(9(\lambda Lr)^3)).  Sum over (r). \(\square\)

A family \(\{\lambda m:m\in B\}\) with \(\lambda\ge1\) is admissible when
(B\) is an integer divisibility antichain.  Thus rational rays are not a
negligible exceptional case; they contain the entire primitive-set model.

### Lemma 3.2 (the exact-ray sieve, with the sharp logarithm)

Fix (x\in A), and let (y_i\in A\) be distinct old points whose ratios are
exactly rational:
\[
 \frac{y_i}{x}=\frac{a_i}{b_i}\quad ((a_i,b_i)=1).
\]
Then (a_i\ge2).  The multiples (nx) which coincide with a multiple of
(y_i) are exactly those with (a_i\mid n).  For any choice of a prime
(q_i\mid a_i), the natural density of integers avoiding every exact old ray
is at least
\[
 \prod_{q\in Q}\left(1-\frac1q\right)
 \ge \frac{c}{\log(2r)},                                  \tag{3.3}
\]
where (Q\) is the set of distinct selected primes and (r) is the number of
old rays.  The last inequality is the standard elementary
Mertens--Chebyshev lower bound for a product of at most (r) distinct primes.

**Proof.**  If (a_i=1), then (b_i y_i=x), contrary to admissibility.
The equality (m y_i=nx) is (ma_i=nb_i), and coprimality makes it
equivalent to (a_i\mid n).  Integers coprime to \(\prod_{q\in Q}q\) avoid
all these divisibilities and have the product density in (3.3).  For a fixed
number of distinct prime factors the product is minimized by choosing the
smallest primes; the standard Mertens--Chebyshev bound gives the last claim.
\(\square\)

The logarithm cannot be removed.  Let (p\le P) range over primes, choose
(X\ge(2P+1)^2), and put
\[
 y_p=\frac{pX}{2p+1}.
Then \(\{X\}\cup\{y_p:p\le P\}\) is admissible: for (p<q),
\[
 y_q-y_p=\frac{X(q-p)}{(2q+1)(2p+1)}\ge1,
\]
all the (y_p)'s lie in a factor-(5/4) interval so multipliers at least (2)
are harmless, and the only close multiple against (X) is
\(|2y_p-X|=X/(2p+1)\ge1\).  Finally
\((2p+1)y_p=pX\), so the exact old rays cover precisely the (nX) with some
(p\mid n).  Their surviving density is
\(\prod_{p\le P}(1-1/p)\asymp1/\log P\), by the standard Mertens theorem.

## 4. Prime-thinned local depletion

The determinant lemma becomes especially effective after restricting the
multiplier set to primes.

### Lemma 4.1 (prime-thinned (L^2) estimate)

Let (X\subset A\cap[R,2R]), (N=|X|), and let \(\mathcal P\) be the primes
in ([Q,2Q]), where (Q\ge2) and (4Q\le R).  Define
\[
 F(t)=\sum_{x\in X}\sum_{p\in\mathcal P}
       1_{(px-1/2,px+1/2)}(t),
 \qquad M=N|\mathcal P|.
\]
Then
\[
 \int F=M,
 \qquad
 \int F^2\le M+N(N-1),                                   \tag{4.1}
\]
and hence
\[
 |\operatorname{supp}F|
 \ge\frac{M^2}{M+N(N-1)}.                                \tag{4.2}
\]

**Proof.**  Intervals from the same source and different primes have center
gap at least (R).  Intervals from different sources and the same prime have
center gap at least (p\), because (A) is (1)-separated.  For a fixed
ordered source pair (x\ne y), suppose two ordered prime pairs ((p,q)) and
\((p',q')\) produce positive overlaps.  Lemma 2.1 and
\(p,p',q,q'\le2Q\) force (pq'=p'q).  A nonunit ratio of two primes has a
unique representation.  Ratio (1) cannot collide because
\(|p(x-y)|\ge p\).  Thus there is at most one off-diagonal intersection for
each ordered source pair, and its length is at most (1).  This proves
(4.1); Cauchy--Schwarz proves (4.2). \(\square\)

### Corollary 4.2 (a rigorous depletion at the squared scale)

There are absolute (c>0,R_0) such that the following holds.  Let
(R\ge R_0), (X\subset A\cap[R,2R]), (N=|X|), and \(\rho=N/R\).  In the
physical window comparable to ([R^2/16,R^2/2]), the prime-multiple intervals
from (X) occupy logarithmic measure at least
\[
 c\,\frac{\rho}{\log R\,(1+\rho\log R)}.                 \tag{4.3}
\]
This occupied set is disjoint from every half-width interval centered at a
point of (A).

**Proof.**  Take (Q=R/16) (with an immaterial integer adjustment).  The
standard Chebyshev prime estimate gives
\(|\mathcal P\cap[Q,2Q]|\ge c_0Q/\log Q\).  Formula (4.2) then gives physical
measure at least (M^2/(M+N^2)), all lying between (QR-1/2) and
(4QR+1/2).  On this window (dt/t\ge dt/(4QR+1)).  Substitution of
(M\gg NR/\log R\) and (Q\asymp R\) gives (4.3).  If (a\in A), then
\(|px-a|\ge1\) for (a\ne x), while (p\ge2) also separates (px) from
(x); hence the two half-width intervals are disjoint. \(\square\)

For sparse blocks, \(\rho\log R\lesssim1\), this is a loss of order
\(\rho/\log R\), exactly the scale needed by the target series.  For dense
blocks it loses another factor of order \(\rho\log R\).  More importantly,
different source blocks can cover the same forbidden set, so (4.3) alone does
not telescope.

## 5. Why raw second moments necessarily lose a logarithm

Let (B_N=\{N,N+1,\ldots,2N-1\}), an admissible integer block.  For
(K\ge2), the number of exact collisions
\[
 \#\{(a,b,k,l):a,b\in B_N, 1\le k,l\le K, ka=lb\}
 \gg NK\log\min(N,K).                                    \tag{5.1}
\]
Indeed, in each dyadic (Q\lesssim\min(N,K)), take coprime
(q\asymp Q), (5q/4\le p\le4q/3).  There are \(\gg Q^2\) such pairs
(by the elementary coprime-pair count).  Each permits \(\gg N/Q\) choices
((a,b)=(pt,qt)\in B_N^2) and \(\gg K/Q\) choices
((k,l)=(qs,ps)).  Thus each dyadic denominator shell contributes
\(\gg NK\), proving (5.1).

Equivalently, on an integer ray the limiting pair kernel is
\[
 \frac1{\operatorname{lcm}(m,n)}=\frac{\gcd(m,n)}{mn}.
\]
The familiar average-gcd logarithm is therefore a real resonance effect, not
an artifact of a loose estimate.  Prime thinning removes repeated copies of
one rational slope, which is exactly why Lemma 4.1 avoids this loss locally.

## 6. LCM stars and unbounded pointwise multiplicity

Let (L=\operatorname{lcm}(N,N+1,\ldots,2N-1)) and
\[
 B=\{L/j:N\le j<2N\}.
\]
This is an admissible integer set: (L/i\mid L/j) would imply (j\mid i),
impossible for two distinct integers in one strict factor-(2) block.  Yet
\[
 j(L/j)=L
\]
for all (j), so (N) different train intervals have the same center.
Their pair energy is (N^2), and their (s)-th moment contribution is
(N^s).  Thus bounded multiplicity, pointwise independence, and any argument
which discards high-multiplicity centers are all false even for admissible
integer sets.

## 7. The normalized squarefree divisor-cube obstruction

The previous star is concentrated at one center.  The following normalized
cube shows that aggregate rational resonance itself can exceed
\(m\,\operatorname{polylog}m\).

For distinct odd primes (p_1,\ldots,p_r), let
\[
 d_S=\prod_{i\in S}p_i,qquad
 j_S=\lfloor\log_2d_S\rfloor,qquad
 u_S=d_S/2^{j_S}\in[1,2),qquad m=2^r.
\]
The (u_S) are distinct and no ratio of two distinct (u_S)'s is an
integer.  Since this is a finite set, one may choose (T) so large that
\[
 B_r=\{Tu_S:S\subseteq[r]\}\subset[T,2T)
\]
is admissible: multipliers (k\ge3) are automatic in this block, while the
finitely many nonzero gaps \(|ku_S-u_{S'}|\), (k=1,2), become at least (1)
after scaling.

For an ordered pair (S,S'), write
\[
 g=(d_S,d_{S'}),\quad U=d_S/g,\quad V=d_{S'}/g,
 \quad h=j_S-j_{S'}.
\]
If (q_*(S,S')) is the reduced denominator of (u_{S'}/u_S), then
\[
 q_*=U\,2^{\max(0,-h)}.                                  \tag{7.1}
\]
The quantity (1/q_*) is the relative density, among multiples of
(u_{S'}), of centers which coincide with a multiple of (u_S).  Since
(h\log2) differs from \(\log(U/V)\) by less than \(\log2\),
\[
 \frac1{q_*}\ge
 \frac1{2\sqrt{UV}}
 \exp\!\left(-\frac12|\log(U/V)|\right).                 \tag{7.2}
\]

Define
\[
 P_r=\prod_{i=1}^r(1+p_i^{-1/2}),\qquad
 \sigma_r^2=
 \sum_{i=1}^r
 \frac{p_i^{-1/2}(\log p_i)^2}{1+p_i^{-1/2}}.
\]
Then the ordered off-diagonal resonance satisfies
\[
 \sum_{S\ne S'}\frac1{q_*(S,S')}
 \ge \frac m2\left(P_r e^{-\sigma_r/2}-1\right).         \tag{7.3}
\]

**Proof.**  Formula (7.1) follows by reducing
\((V/U)2^h\), using that (U,V) are odd.  The floor error in (h) gives
(7.2).  If the exponential factor in (7.2) is temporarily omitted, summing
\((UV)^{-1/2}\) over the Boolean cube factors prime by prime and gives
\[
 2^r\prod_i(1+p_i^{-1/2})=mP_r.
\]
Under the resulting normalized product measure, the random variable
\(L=\log(U/V)\) is a sum of independent symmetric variables and has variance
\(\sigma_r^2\).  Hence
\(\mathbb E|L|\le\sigma_r\), and convexity gives
\(\mathbb E e^{-|L|/2}\ge e^{-\sigma_r/2}\).  Apply (7.2) and subtract the
(m) diagonal terms, each contributing (1) before the factor (1/2), to
obtain (7.3). \(\square\)

If (p_i) are the first (r) odd primes, the standard prime number theorem
estimates give
\[
 \log P_r=(2+o(1))\sqrt{r/\log r},
 \qquad
 \sigma_r=o(\sqrt{r/\log r}).
\]
Thus the right side of (7.3) is
\[
 m\exp((2+o(1))\sqrt{r/\log r}),                          \tag{7.4}
\]
larger than (m) times every fixed power of \(\log m\).  This does **not**
give a counterexample to Problem 143: the scaling (T) needed for
admissibility may be enormous, and the target weight contains the missing
factor (1/\log T).  It does rigorously refute any proposed aggregate
resonance bound depending only on cardinality by (m\operatorname{polylog}m).

There is also a spectral version.  Choose prime pairs ((p_i,q_i)) and the
integer antichain (n_\varepsilon=\prod_i(p_i\text{ or }q_i)).  For the
normalized Gram kernel
\[
 K(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}},
\]
the cube matrix is
\(
 \bigotimes_i\begin{pmatrix}1&a_i\\a_i&1\end{pmatrix}
\)
with (a_i=(p_iq_i)^{-1/2}).  Its extreme eigenvalues are
\(\prod_i(1+a_i)\) and \(\prod_i(1-a_i)\).  Suitable prime pairings make the
first unbounded and the second tend to zero.  Therefore no uniform upper or
lower frame bound follows from admissibility alone.

## 8. Two sufficient global summation mechanisms

Put
\[
 h_j=\sum_{\substack{x\in A\\e^j\le x<e^{j+1}}}\frac1x.
\]

### Lemma 8.1 (uniform logarithmic-window bound suffices)

If
\[
 \sup_{m\ge m_0}\sum_{j=m}^{2m}h_j<\infty,                \tag{8.1}
\]
then both conclusions of Problem 143 hold.

**Proof.**  On (2^r\le j<2^{r+1}), (8.1) gives
\(\sum h_j/j\ll2^{-r}\).  Summing over (r) proves
\(\sum h_j/j<\infty\), which is equivalent to the first target up to finitely
many initial shells.  The cumulative sum through (J) is (O(\log J)=o(J)),
which is the second target. \(\square\)

The more flexible mechanism is a novelty telescope.  For a finite prefix of
shells define
\[
 U_{\le m,T}=\bigcup_{\substack{x\in A\\x<e^{m+1}}}
                  \mathcal H_{x,T},
 \qquad
 U_{<m,T}=\bigcup_{\substack{x\in A\\x<e^m}}
                  \mathcal H_{x,T}.
\]

### Lemma 8.2 (the novelty inequality would solve the problem)

Suppose there is an absolute (c>0) such that for every sufficiently large
(m),
\[
 \liminf_{T\to\infty}
 \frac{|U_{\le m,T}\setminus U_{<m,T}|}{T}
 \ge c\frac{h_m}{m}.                                     \tag{8.2}
\]
Then \(\sum_jh_j/j<\infty\), and hence both requested conclusions hold.

**Proof.**  For each fixed (J), the increments in (8.2) are disjoint and
their union lies in an interval of length (T).  Sum through (J), use
\(\liminf\sum\ge\sum\liminf\) for this finite sum, and obtain
\(c\sum_{m\le J}h_m/m\le1\).  Let (J\to\infty\), then use the shell
equivalence and Proposition 3.1 of `NOTES.md`. \(\square\)

The factor (1/m\) in (8.2) is the right one.  Lemma 3.2 shows that exact
prime rays alone can reduce novelty by a logarithmic factor.  The normalized
divisor cube shows that a much stronger recurrence based only on unweighted
cumulative harmonic mass is false: high central layers of the squarefree
divisor lattice can have large \(\sum1/d\) while leaving a positive fraction
of integers outside all corresponding divisibility events.  The scale
normalization (1/\log d), not a power of total mass, is essential.

## 9. Dependency graph and precise bottleneck

Here is the exact dependency graph for this route.

1. **Train representation and harmonic mass -- proved.**  Lemma 1.1 and the
   thickened-comb identities in `NOTES.md` identify harmonic mass with
   logarithmic occupancy.
2. **Pairwise inverse theorem -- proved.**  Lemmas 2.1--2.3 turn every strong
   overlap below the product scale into one primitive label ((a,b)), with an
   explicit approximation error and denominator bounds.
3. **Exact rational labels -- proved.**  Lemmas 3.1--3.2 reduce them to a
   divisibility sieve and prove the sharp (1/\log r) survivor bound.
4. **Locally nonresonant labels -- proved after prime thinning.**  Lemma 4.1
   and Corollary 4.2 give the desired (h/\log R) local loss in the sparse
   regime.
5. **Aggregate near-rational label charging -- OPEN.**  Prove (8.2), or the
   weaker window estimate (8.1), by combining primitive labels across source
   shells.  The lemma must retain denominator/scale information and survive
   the gcd logarithm, LCM stars, and the normalized divisor cube in Sections
   5--7.
6. **Global summation -- proved conditional on node 5.**  Lemmas 8.1 and 8.2
   close the first target; Proposition 3.1 in `NOTES.md` then closes the
   second.

The first invalid inference in the naive proof is
\[
 \text{large first moment of trains}
 \quad\Longrightarrow\quad
 \text{comparable new union measure}.
\]
It fails quantitatively by (5.1), pointwise by the LCM star, and even after
cardinality normalization by (7.3).  Pairwise determinant rigidity does not
repair this by itself, because many pairs may carry compatible but different
primitive labels.

### Current bottleneck (minimal repair lemma)

Establish the novelty estimate (8.2) after decomposing overlaps by the
primitive labels supplied by Lemma 2.2.  Equivalently, prove a
denominator-and-scale weighted sieve/large-sieve inequality saying that the
union contributed by shell (m), after deleting all older trains, is at least
(c/m) times its raw density.  Exact labels satisfy the required logarithmic
sieve bound (Lemma 3.2); what remains is to control nonexact rational residues
and irrational near-rays on that sieve survivor.  A valid proof must exploit
pairwise admissibility when labels are composed along paths or cycles; a
bound depending only on the number of labels is impossible by Section 7.

Suggested next attack: label every strong-overlap edge by its reduced
\((a,b)\) and error \(ax-by\), compose labels along paths, and show that a
cycle whose reduced product becomes an integer either violates admissibility
or pays total approximation error at least (1).  The needed output is a
weighted path/cycle packing theorem strong enough to imply (8.2), not another
unweighted pair-energy estimate.
