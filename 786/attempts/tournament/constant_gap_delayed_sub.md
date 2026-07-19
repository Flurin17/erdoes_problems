# A uniform gap for fully active delayed-support profiles

## Outcome

This note closes one natural moving-support subclass.  Let

\[
 f(n)=\sum_{p\leq N}w_pv_p(n)
\]

be completely additive, and suppose that for some cutoff \(y=y(N)\)

\[
 w_p=0\quad(p\leq y),\qquad w_p\ne0\quad(y<p\leq N).       \tag{1}
\]

The nonzero weights above the cutoff may be arbitrary, may have either
sign, and may depend on \(N\).  There is an absolute \(\delta>0\) such
that, for every nonzero target \(c\),

\[
 \bigl|\{n\leq N:f(n)=c\}\bigr|\leq(1-\delta)N             \tag{2}
\]

for all sufficiently large \(N\).  In particular this applies to the
target \(c=1\) relevant to product-length rigidity.  If
\(y=N^{o(1)}\), the proof in fact gives the stronger bound

\[
 \bigl|\{n\leq N:f(n)=c\}\bigr|=o(N).                     \tag{3}
\]

for all sufficiently large \(N\).

The proof uses the standard exact-atom theorem for additive functions.
Thus (2) is a rigorous consequence of a precisely stated background
theorem, but it is not an elementary replacement for that theorem.

## Background input: exact-atom anti-concentration

We use the following uniform form of Halasz's exact-value concentration
theorem.

> **Exact-atom theorem.**  There is an absolute constant \(C\) such that,
> for every real additive function \(g\), every \(X\geq2\), and every real
> \(t\),
> \[
>  \frac1X\bigl|\{n\leq X:g(n)=t\}\bigr|
>  \leq
>  \frac{C}{\sqrt{1+\displaystyle
>        \sum_{p\leq X,\ g(p)\ne0}\frac1p}}.                \tag{H}
> \]

The constant is uniform in the values of \(g(p)\); consequently the
function is allowed to vary with \(X\).  Only exact nonzeroness of the
prime values occurs in (H), not their magnitudes.  This uniformity is
essential here.

We also use the standard fixed-parameter smooth-number asymptotic

\[
 \Psi(X,X^{1/u})=(\rho(u)+o_u(1))X                         \tag{D}
\]

for each fixed \(u>1\).  Here \(\rho(u)>0\) is the Dickman function.

## The dichotomy

Choose once and for all a sufficiently large fixed \(U>1\) that

\[
 \frac{C}{\sqrt{1+\tfrac12\log U}}\leq\frac12.             \tag{4}
\]

For example any fixed \(U\) with \(\log U\geq 8C^2\) is more than
enough after harmless enlargement.  Put

\[
 x=N^{1/U}.
\]

There are two cases.

### Case 1: \(y\geq x\)

Every prime at most \(x\) has weight zero.  Hence every \(x\)-smooth
integer \(n\leq N\) satisfies \(f(n)=0\), and so it is outside every
nonzero fibre.  By (D), for all sufficiently large \(N\),

\[
 \bigl|\{n\leq N:f(n)\ne c\}\bigr|
 \geq \Psi(N,x)
 \geq \frac{\rho(U)}2N.                                   \tag{5}
\]

This part is completely insensitive to the weights above \(y\).

### Case 2: \(y<x\)

By the second half of (1), every prime in \((x,N]\) is active.  Mertens'
prime-reciprocal estimate, with the fixed number \(U\), gives

\[
 \sum_{\substack{p\leq N\\f(p)\ne0}}\frac1p
 \geq\sum_{x<p\leq N}\frac1p
 =\log U+o_U(1)
 \geq\frac12\log U                                      \tag{6}
\]

for all sufficiently large \(N\).  Applying (H), then (4), yields

\[
 \bigl|\{n\leq N:f(n)=c\}\bigr|
 \leq \frac{C}{\sqrt{1+\tfrac12\log U}}N
 \leq\frac12N.                                           \tag{7}
\]

Equations (5) and (7) prove (2), with the explicit choice

\[
 \delta=\min\left\{\frac12,\frac{\rho(U)}2\right\}>0.     \tag{8}
\]

Finally suppose \(y=N^{o(1)}\).  If \(y\to\infty\), Mertens' estimate
at the two moving endpoints gives

\[
 \sum_{y<p\leq N}\frac1p
 =\log\frac{\log N}{\log y}+o(1)\longrightarrow\infty.
\]

If \(y\) stays bounded along a subsequence, the same sum is
\(\log\log N+O(1)\), and again tends to infinity.  All these primes are
active, so (H) proves (3).  Thus the subpolynomial-cutoff conclusion is
not merely a fixed one-half gap: every exact fibre has vanishing density.

## What this does and does not settle

The hypothesis that **every** prime above \(y\) has nonzero weight is the
mechanism that makes (6) automatic.  The argument does not cover a sparse
or multiband active set above a long zero prefix.  In that setting neither
branch need apply: the smooth zero core can have density tending to zero
while the active reciprocal mass stays below the threshold needed in (H).

No independent-geometric approximation is used.  In particular, the
boundary-biased square-root threshold is not replaced by an Euler product.
The only anti-concentration input is the finite, uniform exact-atom theorem
(H), which is designed precisely to tolerate moving prime supports and
arbitrary signed rational weights.

For a fully elementary proof, the exact remaining subtask is a special-case
replacement for (H): prove that for some fixed large \(U\), every completely
additive \(g\) satisfying \(g(p)\ne0\) on
\((N^{1/U},N]\) has every exact fibre of density at most \(1-\eta_U\),
with \(\eta_U>0\) independent of the prime values.  Multiplier-chain
matchings alone cannot establish this: every one-prime edge has its lower
endpoint at most \(N^{1-1/U}=o(N)\).  A valid elementary proof must use
relations between several rough-prime layers, rather than sum those
overlapping one-prime edges.

## Checks against the principal stress tests

1. For the square-root threshold, the proof may fall in the smooth branch;
   it never predicts the false independent-geometric density.
2. For \(y=N^{o(1)}\), the reciprocal mass in (6) is at least the fixed
   \(\log U+o(1)\), irrespective of how slowly \(y\) moves.
3. Arbitrarily small but nonzero rational weights remain active in (H).
4. Signed weights and exact cancellations are allowed by (H).
5. The conclusion concerns a nonzero fibre.  It would be false to use the
   smooth numbers in (5) against the zero fibre.
