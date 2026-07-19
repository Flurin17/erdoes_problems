# Complementary semiprime profiles and coproduct charges

## Objective and outcome

Let (f) be a rational completely additive function and put

\[
 B=\{n\leq N:f(n)=1\},\qquad E=[1,N]\setminus B,\qquad m=|E|.
\]

This note rigorously closes the bounded-overlap bookkeeping for prime-band
color transitions.  The main proved inequality is (12): every dyadic band
whose complementary semiprime rectangle has large error, and every change
between two reliable adjacent modal prime colors, costs

\[
 \gg \frac{N}{\log N}\frac1i
\]

distinct exceptional semiprimes at logarithmic scale (i).  Consequently a
profile which changes on harmonic mass (gg\log\log N) already gives

\[
 m\gg \frac{N\log\log N}{\log N}.
\]

The argument is unconditional.  It also identifies exactly why semiprimes
alone do not prove the desired improvement: a threshold profile has no such
transition errors.  Arbitrary-order coproducts, not another semiprime
count, are needed to charge a long constant plateau.  An exact coproduct
ledger and two model closure lemmas are given below.  The remaining robust
plateau lemma is stated precisely in the final section; it is not claimed
proved.

## 1. A robust color-rectangle lemma

Let (X,Y) be finite nonempty sets, give every element (z\in X\cup Y) a
color (w(z)\in\mathbb Q), and call ((x,y)) bad when
(w(x)+w(y)\ne1).  If there are (D) bad pairs, then there is an
(\alpha\in\mathbb Q) such that

\[
 |\{x\in X:w(x)\ne\alpha\}|\leq \frac D{|Y|}.                 \tag{1}
\]

If (D\leq |X||Y|/2), the same (\alpha) also satisfies

\[
 |\{y\in Y:w(y)\ne1-\alpha\}|
 \leq \frac{2D}{|X|}.                                       \tag{2}
\]

Indeed, choose (y_0\in Y) incident with at most (D/|Y|) bad pairs and
put (\alpha=1-w(y_0)).  This proves (1).  If (X_0) is the set on which
the color is (\alpha), then every (y) of color different from
(1-\alpha) makes all (|X_0|) pairs bad.  Since
(|X_0|\geq |X|/2), (2) follows.

No probability or approximate equality of rational colors is being used:
different colors give bad pairs exactly.

## 2. Dyadic complementary rectangles

Write

\[
 L=\lfloor\log_2N\rfloor,\qquad D=L-4,
 \qquad
 \mathcal P_i=\{p\text{ prime}:2^i<p\leq2^{i+1}\},
 \quad R_i=|\mathcal P_i|.
\]

Fix an absolute (i_0) large enough for the dyadic prime-number-theorem
lower bound

\[
 R_i\geq c_0\frac{2^i}{i}\qquad(i\geq i_0).                  \tag{3}
\]

Only indices

\[
 I=\{i_0,i_0+1,\ldots,\lfloor D/3\rfloor\}                  \tag{4}
\]

will be used.  For (i\in I), let

\[
 C_i=
 |\{(p,q)\in\mathcal P_i\times\mathcal P_{D-i}:
             f(p)+f(q)\ne1\}|,
 \qquad
 \delta_i=\frac{C_i}{R_iR_{D-i}}.                           \tag{5}
\]

Every product counted by (C_i) is at most
(2^{i+1}2^{D-i+1}=2^{L-2}\leq N), has grading different from
one, and is therefore in (E).  Unique factorization and the restriction
(i<D-i) show that these semiprime sets are disjoint as (i) varies.  In
particular,

\[
 \sum_{i\in I}C_i\leq m.                                    \tag{6}
\]

For every (i\in I) with (\delta_i\leq1/4), apply the rectangle
lemma and choose a modal color (\alpha_i) such that

\[
 \begin{aligned}
 |\{p\in\mathcal P_i:f(p)=\alpha_i\}|&\geq(1-\delta_i)R_i,\\
 |\{q\in\mathcal P_{D-i}:f(q)=1-\alpha_i\}|&\geq(1-2\delta_i)R_{D-i}.
 \end{aligned}                                               \tag{7}
\]

The value (\alpha_i) is unique whenever the first displayed proportion is
greater than (1/2).

## 3. Every reliable modal-color transition has a disjoint charge

Suppose (i,i+1\in I), (\delta_i,\delta_{i+1}\leq1/4), and
(\alpha_i\ne\alpha_{i+1}).  Consider the under-complementary rectangle

\[
 \mathcal U_i=\mathcal P_i\times\mathcal P_{D-i-1}.          \tag{8}
\]

The first factor has color (\alpha_i) on at least
((1-\delta_i)R_i) primes.  Applying (7) at (i+1), the second factor has
color (1-\alpha_{i+1}) on at least
((1-2\delta_{i+1})R_{D-i-1}) primes.  Every product of one prime from
each of these two sets has color

\[
 \alpha_i+(1-\alpha_{i+1})\ne1.
\]

Thus at least

\[
 \frac38 R_iR_{D-i-1}                                      \tag{9}
\]

entries of (\mathcal U_i) lie in (E).  Products in distinct
(\mathcal U_i)'s are distinct, since the two prime-factor band indices
determine (i).  They are also disjoint from all products counted in (5),
because their band-index sum is (D-1), rather than (D).  All these
products are at most (2^{D+1}<N).

Let

\[
 H=\{i\in I:\delta_i>1/4\}
\]

and let

\[
 T=\{i:i,i+1\in I\setminus H,\ \alpha_i\ne\alpha_{i+1}\}.
\]

By (3), uniformly for (i\in I),

\[
 R_iR_{D-i}\gg\frac{2^D}{i(D-i)}\gg\frac{N}{iD},
 \qquad
 R_iR_{D-i-1}\gg\frac{N}{iD}.                              \tag{10}
\]

For (i\in H), (5) directly gives

\[
 C_i\geq\frac14R_iR_{D-i}\gg\frac{N}{iD}.                  \tag{11}
\]

Summing the pairwise disjoint charges (9) and (11) proves the promised
unconditional profile inequality

\[
 \boxed{
 m\ \geq\ c\frac ND
 \left(\sum_{i\in H}\frac1i+\sum_{i\in T}\frac1i\right)
 }                                                           \tag{12}
\]

for an absolute (c>0) and all sufficiently large (N).

In particular, if the unreliable bands and genuine modal transitions have
combined harmonic mass (gg\log D), then

\[
 m\gg\frac{N\log D}{D}
 \asymp\frac{N\log\log N}{\log N}.                          \tag{13}
\]

This summation has overlap exactly one, not merely bounded average overlap.
It is therefore safe to combine with other exceptional families that have
a different number of prime factors.

## 4. Exact coproduct ledger

The plateau case must use products of more than two primes.  Here is a
convenient bookkeeping statement that loses no multiplicity.

For a nondecreasing tuple of band indices
(\mathbf i=(i_1,\ldots,i_r)), let (\mathcal C_{\mathbf i}) be the set
of squarefree integers

\[
 n=p_1\cdots p_r,
 \qquad p_j\in\mathcal P_{i_j},
\]

where primes chosen from a repeated band are distinct.  If

\[
 \sum_{j=1}^r(i_j+1)\leq L,                                 \tag{14}
\]

then every member of (\mathcal C_{\mathbf i}) is at most (N).  Distinct
nondecreasing tuples give disjoint sets, by unique factorization.  Hence for
every collection (\mathscr I) of tuples satisfying (14),

\[
 m\geq
 \sum_{\mathbf i\in\mathscr I}
 |\{p_1\cdots p_r\in\mathcal C_{\mathbf i}:
                  f(p_1)+\cdots+f(p_r)\ne1\}|.              \tag{15}
\]

Repeated ordering of the same factorization never occurs in (15).  This is
the required bounded-overlap coproduct ledger.  Under exact monochromaticity
of the participating bands, every summand is either zero or the full
coproduct box.

For fixed (r), the PNT gives the rough box size

\[
 |\mathcal C_{\mathbf i}|\asymp_r
 \frac{2^{i_1+\cdots+i_r}}{i_1\cdots i_r}                   \tag{16}
\]

when the indices tend to infinity and repeated-band diagonal choices are
accounted for by the corresponding fixed factorial.  Thus complementary
tuples with index sum (L-r+O(1)) have total scale (N) times a harmonic
composition sum.  Formula (15), rather than a sum over ordered
factorizations, is the correct way to exploit those boxes.

## 5. Two exact model closures

The next two lemmas explain the two sides of the transition/plateau
dichotomy.  They are not assumptions in (12).

### 5.1 Cauchy profile forces all transitions

Assume, as an exact model, that every band
(\mathcal P_1,\ldots,\mathcal P_{D-1}) is monochromatic, of colors
(a_1,\ldots,a_{D-1}), and that all complementary semiprime and triple
boxes are good:

\[
 a_i+a_{D-i}=1,                                             \tag{17}
\]

and

\[
 a_i+a_j+a_k=1\qquad(i+j+k=D).                              \tag{18}
\]

Comparing (18) for ((1,i-1,D-i)) with (17) for
((i,D-i)) gives

\[
 a_i=a_1+a_{i-1}\qquad(2\leq i\leq D-1).
\]

Therefore (a_i=ia_1).  Equation (17) then gives (Da_1=1), so

\[
 a_i=\frac iD.                                              \tag{19}
\]

Every under-complementary semiprime box has color

\[
 a_i+a_{D-i-1}=\frac{D-1}{D}\ne1.
\]

Summing these disjoint boxes for (i_0\leq i\leq D/3) gives

\[
 m\gg\sum_{i=i_0}^{D/3}\frac{N}{iD}
 \gg\frac{N\log D}{D}.                                    \tag{20}
\]

Thus an exactly additive scale profile pays the desired
(N\log\log N/\log N) through a transition at every scale.

### 5.2 A genuinely constant initial plateau has linear coproduct cost

Assume instead that, for some (\alpha\in\mathbb Q),

\[
 f(p)=\alpha\qquad\text{for every prime }p\leq N^{1/3}.     \tag{21}
\]

Every (N^{1/3})-smooth (n\leq N) then has

\[
 f(n)=\alpha\Omega(n),                                     \tag{22}
\]

with multiplicity in (\Omega).  The standard fixed-(u) Dickman theorem
gives

\[
 \Psi(N,N^{1/3})=(\rho(3)+o(1))N.                           \tag{23}
\]

If (\alpha=0), or if (1/\alpha) is not a positive integer, all these
smooth integers are exceptional.  Otherwise the only possibly good smooth
integers have (Omega(n)=1/\alpha).  The standard uniform
Hardy--Ramanujan/Sathe--Selberg concentration estimate

\[
 \sup_{k\geq0}|\{n\leq N:\Omega(n)=k\}|
 \ll \frac{N}{\sqrt{\log\log N}}                           \tag{24}
\]

(used here as a named standard dependency) and (23) imply

\[
 m\geq(\rho(3)-o(1))N.                                     \tag{25}
\]

Thus the exact long-plateau model costs linearly many arbitrary-order
coproducts, even though its complementary semiprime transition charge is
zero.

## 6. Exact remaining bottleneck

The threshold grading

\[
 f(p)=0\ (p\leq\sqrt N),\qquad f(p)=1\ (p>\sqrt N)
\]

shows that (12) cannot by itself be strengthened: throughout the range
(i\leq D/3), its reliable modal color is constantly zero, and both the
diagonal and under-diagonal semiprime boxes are good.  Its linear exceptional
set consists instead of smooth coproducts.  This is a genuine obstruction
to any proof that only adds more complementary semiprime rectangles.

Combining (12) and (15) would yield the unconditional
(N\log\log N/\log N) bound once the following robust plateau statement is
proved.

> **Robust coproduct-profile lemma (open in this note).**  Suppose the
> complementary rectangles (5) yield reliable modal colors outside a set
> of harmonic weight (o(\log D)), and the reliable modal transition set
> also has harmonic weight (o(\log D)).  Then the disjoint coproduct sum
> in (15), over tuples supported on the resulting constant plateaux, has at
> least (cN\log D/D) entries of color different from one.

The required lemma must be robust to two effects that the exact models avoid:

1. exceptional primes in a band may have total reciprocal mass tending to
   infinity even when it is (o(\log\log N)); and
2. a modal profile can make a small number of jumps at growing scale indices,
   so no single plateau need contain every prime below a fixed power of (N).

The weakest plausible repair is a weighted smooth-number estimate for a
set of zero-colored prime bands after deleting prime exceptions of total
reciprocal mass (h): one needs a lower bound of size
(N\exp(-O(h))/ (\log N)^{O(1)}), uniform over the locations of the deleted
bands, together with the analogous local concentration bound when the
plateau color is nonzero.  Neither estimate follows from a union bound, and
asserting it without a sieve proof would be the first unjustified step.

In summary: the semiprime transition summation and all overlap issues are
closed by (12); the exact Cauchy and exact plateau endpoints are closed by
(20) and (25); the only missing step in this route is robust arbitrary-order
coproduct concentration across several approximate plateaux.
