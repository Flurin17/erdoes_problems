# Dyadic prime--cofactor rectangles

This note gives an elementary bounded-overlap inequality for a level of a
completely additive function.  Its main point is that the cofactor rows can
be chosen disjoint across dyadic prime scales while all products land in one
upper annulus.  Thus the loss is charged only to exceptional *products*, not
also to exceptional cofactors.

## Setup

Let (G) be an abelian group, let

\[
 f:\mathbb N\longrightarrow G,
 \qquad f(mn)=f(m)+f(n),
\]

and fix a target value (a\in G).  For an integer (X\geq 1), write

\[
 A=\{n\leq X:f(n)=a\},\qquad E=[1,X]\setminus A,
\]

and let

\[
 E^{\rm top}=E\cap(X/4,X],\qquad m_{\rm top}=|E^{\rm top}|.
\]

No ordering, torsion-freeness, or rationality assumption on (G) is needed
for the arguments below.

## One prime band

Fix a real (P>1), and put

\[
 \mathcal P(P)=\{p\text{ prime}:P<p\leq 2P\},
 \qquad
 I(P)=\mathbb N\cap\left(\frac{X}{4P},\frac{X}{2P}\right].
\]

For (c\in G), define

\[
 H_c(P)=\sum_{\substack{p\in\mathcal P(P)\\ f(p)=c}}\frac1p,
 \qquad
 H(P)=\sum_{p\in\mathcal P(P)}\frac1p,
 \qquad
 M(P)=\max_{c\in G}H_c(P).
\]

The maximum exists because only finitely many values occur on the band.

**Lemma 1 (one-band rectangle inequality).**  If

\[
 D(P,X)=\left\lfloor\frac{\log X}{\log P}\right\rfloor,
\]

then

\[
 |I(P)|\bigl(H(P)-M(P)\bigr)
 \leq \frac{D(P,X)}{P}\,m_{\rm top}.                 \tag{1}
\]

In particular, if (P\leq X/8), then

\[
 H(P)-M(P)\leq 8D(P,X)\frac{m_{\rm top}}X.          \tag{2}
\]

**Proof.**  Consider the rectangle of pairs

\[
 (p,n),\qquad p\in\mathcal P(P),\quad n\in I(P),
\]

and give the pair ((p,n)) weight (1/p).  For a fixed row (n), a
product (pn) belongs to (A) only if

\[
 f(p)=a-f(n).
\]

Consequently the total weight of the good entries in that row is at most
(M(P)), so the bad entries have total weight at least (H(P)-M(P)).
Summing over the rows gives bad-pair weight at least the left side of (1).

Every product in the rectangle lies in the common annulus:

\[
 p>P,\ n>X/(4P)\quad\Longrightarrow\quad pn>X/4,
\]

and

\[
 p\leq2P,\ n\leq X/(2P)\quad\Longrightarrow\quad pn\leq X.
\]

Thus every bad pair maps to (E^{\rm top}).  For a fixed (y\leq X),
its preimages correspond to primes (p\in\mathcal P(P)) dividing (y).
There are at most (D(P,X)) of these: if there are (d), their product
divides (y), whereas their product is (>P^d).  The total preimage
weight at (y) is therefore at most (D(P,X)/P).  This proves (1).

Finally,

\[
 |I(P)|=
 \left\lfloor\frac{X}{2P}\right\rfloor-
 \left\lfloor\frac{X}{4P}\right\rfloor
 \geq \frac{X}{4P}-1.
\]

When (P\leq X/8), the last expression is at least (X/(8P)), and
(2) follows.  \(\square\)

The same proof has a useful zero/nonzero formulation.  Put

\[
 H_0(P)=\sum_{\substack{p\in\mathcal P(P)\\f(p)=0}}\frac1p,
 \qquad H_*(P)=H(P)-H_0(P).
\]

Since in every row either all zero-weight prime columns are bad or all
nonzero-weight prime columns are bad,

\[
 |I(P)|\min\{H_0(P),H_*(P)\}
 \leq \frac{D(P,X)}P m_{\rm top}.                    \tag{3}
\]

This also follows from (1), because
(H(P)-M(P)\geq\min\{H_0(P),H_*(P)\}).

## Simultaneous dyadic bands

The preceding estimate can be summed without paying once per scale.  Fix
(P_0>1), set (P_j=2^jP_0), and let (J) be any finite set of
nonnegative integers for which (P_j\leq X/8).  Put

\[
 I_j=I(P_j),\quad H_j=H(P_j),\quad M_j=M(P_j),
 \qquad
 D_0=\left\lfloor\frac{\log X}{\log P_0}\right\rfloor.
\]

The half-open intervals (I_j) are pairwise disjoint.  The prime bands
((P_j,2P_j]) are also pairwise disjoint.

**Theorem 2 (multiscale bounded-overlap inequality).**  With the notation
above,

\[
 \boxed{
 \sum_{j\in J}P_j|I_j|\bigl(H_j-M_j\bigr)
 \leq D_0m_{\rm top}.}                              \tag{4}
\]

Consequently,

\[
 \boxed{
 \sum_{j\in J}(H_j-M_j)
 \leq 8D_0\frac{m_{\rm top}}X.}                     \tag{5}
\]

**Proof.**  In scale (j), give a pair ((p,n)) weight (P_j/p).
The same row argument as in Lemma 1 shows that the bad-pair weight at that
scale is at least

\[
 P_j|I_j|(H_j-M_j).
\]

All bad products from all scales still lie in (E^{\rm top}).  For fixed
(y\in E^{\rm top}), a preimage pair determines a distinct prime divisor
(p>P_0) of (y), and its weight is (P_j/p<1).  An integer (y\leq X)
has at most (D_0) distinct prime divisors exceeding (P_0), because the
product of (d) such divisors is (>P_0^d) and divides (y).  Hence the
total weight mapping to (y) is at most (D_0).  Summation over
(E^{\rm top}) proves (4).

For every (j\in J), the floor estimate in Lemma 1 gives
(P_j|I_j|\geq X/8).  Substitution in (4) proves (5).  \(\square\)

The zero/nonzero consequence is

\[
 \sum_{j\in J}\min\{H_{j,0},H_{j,*}\}
 \leq 8D_0\frac{m_{\rm top}}X.                      \tag{6}
\]

If the zero prime-value class is harmonic-modal in every selected band,
then (M_j=H_{j,0}), and (5) becomes the direct active-prime estimate

\[
 \sum_{j\in J}\sum_{\substack{P_j<p\leq2P_j\\f(p)\ne0}}\frac1p
 \leq 8D_0\frac{m_{\rm top}}X.                      \tag{7}
\]

For (P_0=X^\alpha) with fixed (\alpha>0), one may replace (D_0) by
(\lfloor1/\alpha\rfloor).  Thus an (o(X)) exceptional set forces
the total nonmodal harmonic mass throughout any fixed-power collection of
these bands to be (o(1)).

## Weighted abstract form

The collision argument is not tied to the weights above.  For arbitrary
nonnegative coefficients (u_j), give ((p,n)) weight (u_j/p).  If

\[
 \Delta(u)=
 \max_{y\leq X}
 \sum_{j\in J}\ \sum_{\substack{P_j<p\leq2P_j\\p\mid y}}
 \frac{u_j}{p},
\]

then exactly the same proof gives

\[
 \sum_{j\in J}u_j|I_j|(H_j-M_j)
 \leq m_{\rm top}\Delta(u).                         \tag{8}
\]

A completely explicit bound is

\[
 \Delta(u)
 \leq (\log X)\max_{j\in J}\frac{u_j}{P_j\log P_j}. \tag{9}
\]

Indeed, if (d_j) selected-band primes divide (y), then
(\sum_jd_j\log P_j<\log X), while their contribution to
(\Delta(u)) is at most (sum_jd_ju_j/P_j).  Taking (u_j=P_j)
recovers the bound (D_0) in (4), up to the harmless floor improvement.

## What this does and does not prove

The theorem is unconditional and has no probabilistic or prime-distribution
input.  It proves scale-by-scale harmonic monochromaticity whenever the
target level occupies (1-o(1)) of the upper annulus.  It also gives the
active-prime estimate (7) as soon as zero is known to be the modal prime
value on the relevant scales.

It does not force the modal values at different scales to agree.  For
example, a threshold assignment of prime weights is exactly monochromatic
away from the threshold band, so every term (H_j-M_j) there is zero.
Closing a global concentration argument therefore still requires a
cross-scale additive relation or another mechanism that identifies the
different band modes.
