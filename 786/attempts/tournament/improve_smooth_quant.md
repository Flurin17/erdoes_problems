# Optimizing the smooth-number self-consistency bound

This note separates three issues which should not be conflated:

1. the exact finite implication of the active-prime-chain argument;
2. the best consequence of the one-scale prime-product construction in the
   current draft;
3. the stronger consequence obtained from a genuinely uniform smooth-number
   theorem (fixed-\(u\) Dickman asymptotics do not suffice).

Throughout, put
\[
 X=\log N,\qquad R=\log X,\qquad S=\log R.
\]
Write \(\Psi(x,y)\) for the number of positive integers at most \(x\) all
of whose prime divisors are at most \(y\), with \(1\) included.

## 1. Exact finite self-consistency

Let \(m=N-|A|\), and first suppose \(m<N\).  Define
\[
 y=\left\lfloor\frac{N}{m+1}\right\rfloor\geq 1.
\]
If \(f(p)\ne0\), a level of the completely additive grading meets each
\(p\)-adic chain at most once.  Since the number of such chains in
\([1,N]\) is \(N-\lfloor N/p\rfloor\),
\[
 m\geq \left\lfloor\frac Np\right\rfloor.                 \tag{1}
\]
For every prime \(p\leq y\), however,
\(p\leq N/(m+1)\), and hence \(\lfloor N/p\rfloor\geq m+1\).
Thus (1) forces \(f(p)=0\) for every \(p\leq y\).  Complete additivity
then gives \(f(n)=0\) for every \(y\)-smooth \(n\), whereas members of
\(A\) have grading \(1\).  Consequently
\[
 m\geq\Psi(N,y).                                          \tag{2}
\]
The floor defining \(y\) also gives
\[
 m+1\leq\frac Ny.
\]
Combining this with (2) gives the stronger and exact scalar condition
\[
 \boxed{\quad y\bigl(\Psi(N,y)+1\bigr)\leq N.\quad}        \tag{3}
\]
Thus the natural finite fixed point is
\[
 Y_N:=\max\{t\in\mathbb Z_{\geq1}:t(\Psi(N,t)+1)\leq N\}. \tag{4}
\]
Every admissible configuration with \(m<N\) has \(y\leq Y_N\), and the
other half of the floor relation gives the exact consequence
\[
 m\geq\left\lfloor\frac{N}{Y_N+1}\right\rfloor.           \tag{5}
\]
The case \(m=N\) is already stronger than every asymptotic lower bound
below.  Notice that (3), rather than merely (2), is the clean object to
estimate.

## 2. Optimizing the elementary one-scale construction

Let \(L=\log y\), \(u=X/L\), and
\[
 k=\lceil u\rceil,\qquad z=e^{X/k}\leq y,\qquad Q=\pi(z).
\]
Products of exactly \(k\) primes at most \(z\), now allowing repeated
primes, are all \(y\)-smooth and at most \(N\).  Unique factorization
shows that they give exactly
\[
 \binom{Q+k-1}{k}                                          \tag{6}
\]
different integers.  This is marginally stronger than taking distinct
primes in \((z/2,z]\).

In the asymptotically relevant range \(L>2R\), one has \(Q/k\to\infty\).
The prime number theorem and Stirling's formula give
\[
 \begin{aligned}
 \log\binom{Q+k-1}{k}
 &=k\log Q-\log(k!)+o(k)\\
 &=k(\log z-\log\log z)-k\log k+k+o(k)\\
 &=X-k(R-1+o(1)),                                         \tag{7}
 \end{aligned}
\]
because \(k\log z=X\), and hence
\(\log k+\log\log z=\log X=R\) exactly.  A preliminary version with
\(O(k)\) in place of \(-(1+o(1))k\), together with the trivial range
\(L\leq2R\), first gives \(L=O(\sqrt{XR})\); in particular
\(k\to\infty\), justifying the refined form (7).

From (3), or simply \(\Psi(N,y)\leq N/y\), equations (6)--(7) imply
\[
 L\leq k(R-1+o(1)).                                       \tag{8}
\]
Since \(k=X/L+O(1)\) and the preliminary bound makes \(LR=o(X)\),
\[
 \boxed{\quad L^2\leq X(R-1+o(1)).\quad}                  \tag{9}
\]
Therefore this construction yields
\[
 m\geq N\exp\!\left(-(1+o(1))\sqrt{XR}\right).           \tag{10}
\]

The constant \(1\) in (10) is optimal **within this one-scale
construction**.  More generally, choose \(r\) prime factors from primes
at most \(e^t\), where
\[
 t\leq L,\qquad rt\leq X.
\]
When \(\pi(e^t)\gg r\), its logarithmic count is
\[
 r\{t-\log t-\log r+1+o(1)\}.                            \tag{11}
\]
For fixed \(r\), (11) increases with \(t\), so
\(t=\min(L,X/r)\).  If \(r\geq u\), then (11) becomes
\[
 X-r(R-1+o(1)),
\]
which is maximized at \(r=\lceil u\rceil\).  If \(r<u\), the missing
main term \((u-r)L\) swamps any saving in the factorial or prime-density
terms unless \(u-r=O(1)\); rounding/mixing the two adjacent values only
affects lower-order terms.  Thus changing the common prime cutoff,
using an interval, allowing multiplicity, or varying the number of
factors cannot improve the leading constant of this particular scheme.
A genuinely multiscale count of smooth numbers is required.

For (10) with leading constant only, the full prime number theorem is
unnecessary: a Chebyshev lower bound \(\pi(t)\gg t/\log t\), plus the
elementary binomial estimate, suffices.  The \(-1\) in (9) uses the
sharper inputs
\[
 \pi(t)=(1+o(1))\frac{t}{\log t},\qquad
 \log(r!)=r\log r-r+o(r).                                 \tag{12}
\]

## 3. Uniform smooth numbers improve the constant to \(1/\sqrt2\)

The exact standard input sufficient for the leading improvement is the
following logarithmic estimate in the displayed range:

> **Uniform smooth-number input.**  If \(x\to\infty\),
> \(v=\log x/\log w\to\infty\), and
> \(\log w\asymp\sqrt{\log x\,\log\log x}\), then
> \[
> \log\Psi(x,w)=\log x-(1+o(1))v\log v.                  \tag{13}
> \]

One precise standard theorem implying (13) is Hildebrand's uniform
Dickman estimate: for every fixed \(\varepsilon>0\), uniformly in
\[
 \exp\{(\log\log x)^{5/3+\varepsilon}\}\leq w\leq x,
\]
\[
 \Psi(x,w)=x\rho(v)
 \left(1+O_\varepsilon\!\left(\frac{\log(v+1)}{\log w}\right)\right),
 \qquad v=\frac{\log x}{\log w}.                          \tag{14}
\]
Together with de Bruijn's large-\(v\) estimate
\[
 \log\rho(v)=-(1+o(1))v\log v,                           \tag{15}
\]
this gives (13).  The range needed here lies very comfortably inside
(14), since \(\sqrt{XR}\gg R^{5/3+\varepsilon}\).  In particular, the
fixed-\(v\) Dickman asymptotic cited in the earlier draft is not enough:
here \(v\asymp\sqrt{X/R}\to\infty\).

We now apply (13).  The elementary result (9) already gives
\(L=O(\sqrt{XR})\).  If \(L=o(\sqrt{XR})\), the desired improvement is
automatic.  Otherwise \(L\asymp\sqrt{XR}\), so (13), with \(x=N,w=y\),
and (3) give
\[
 X-L\geq\log\Psi(N,y)
 =X-(1+o(1))\frac XL\log\frac XL.
\]
Consequently
\[
 L^2\leq(1+o(1))X\log\frac XL.                           \tag{16}
\]
Since (9) gives
\[
 \log(X/L)=\tfrac12R+O(S),
\]
(16) becomes
\[
 \boxed{\quad L\leq
 \left(\frac1{\sqrt2}+o(1)\right)\sqrt{XR}.\quad}        \tag{17}
\]
Finally, from \(N/(m+1)<y+1\),
\(\log(N/(m+1))\leq L+o(1)\).  Thus, without needing an a priori
assumption \(m=o(N)\),
\[
 \boxed{\quad
 m\geq N\exp\!\left[-\left(\frac1{\sqrt2}+o(1)\right)
 \sqrt{\log N\,\log\log N}\right].\quad}                \tag{18}
\]
Indeed, any sequence on which (18) were nontrivial and failed would
itself have \(m=o(N)\), placing it in the range used above.

## 4. A second-order fixed-point location

If a second-order statement is wanted, use the standard de Bruijn
expansion
\[
 -\log\rho(v)=vF(v),                                      \tag{19}
\]
where
\[
 F(v)=\log v+\log\log v-1
 +\frac{\log\log v-1}{\log v}
 +O\!\left(\frac{(\log\log v)^2}{(\log v)^2}\right).     \tag{20}
\]
The relative error in (14) has logarithm \(o(1)\) in our range.  Hence
(3), (14), and (19) imply, for \(q=L^2/X\),
\[
 q\leq F\!\left(\sqrt{X/q}\right)+o(1).                  \tag{21}
\]
The leading estimate first gives \(q\leq(1/2+o(1))R\).  At the unique
asymptotic crossing in (21),
\[
 \log v=\frac{R-\log q}{2}
 =\frac R2-\frac S2+\frac{\log2}{2}+o(1).
\]
Substitution in (20) yields
\[
 \boxed{\quad
 \frac{L^2}{X}\leq
 \frac R2+\frac S2-1-\frac{\log2}{2}+o(1).
 \quad}                                                   \tag{22}
\]
Equivalently,
\[
 L\leq\frac1{\sqrt2}\sqrt{XR}
 \left(1+\frac{S-2-\log2}{2R}
 +o\!\left(\frac1R\right)\right).                       \tag{23}
\]
Together with the floor relation, (23) gives the corresponding
second-order lower bound on \(m\) by replacing \(L\) in
\(m\geq N\exp(-L+o(1))\).

The constant \(1/\sqrt2\) is sharp for the scalar condition (3) itself.
Indeed, if \(L=c\sqrt{XR}\), then (13) gives
\[
 \log\frac{y\Psi(N,y)}N
 =\left(c-\frac1{2c}+o(1)\right)\sqrt{XR}.                \tag{24}
\]
Thus (3) holds at the exponential scale for every fixed
\(c<1/\sqrt2\) and fails for every fixed \(c>1/\sqrt2\).  Formula (22)
locates the transition more precisely.  Therefore any improvement of
the leading constant below \(1/\sqrt2\) must use additional structure of
the PLR set, not only smooth-number deletion and the active-prime-chain
inequality.

## 5. Dependency and falsification ledger

Locally proved here:

- the exact condition (3) and the finite fixed-point formulation (4)--(5);
- the optimized one-scale construction (6)--(11);
- the deductions (17)--(18) from the stated uniform input;
- the second-order algebra (21)--(24).

External standard inputs, in increasing strength:

- Chebyshev's lower bound for primes gives the leading constant \(1\);
- PNT plus Stirling gives the refinement (9);
- Hildebrand's uniform estimate (14) plus (15) gives \(1/\sqrt2\);
- the full expansion (20) gives (22)--(23).

The weakest nonlocal step for (18) is precisely (13), not the chain
argument.  A direct falsification test for every asserted constant is to
insert \(L=c\sqrt{XR}\) into
\(L\leq (X/L)\log(X/L)\): it gives \(c^2\leq1/2\).  For the refined
constant, insert the right-hand side of (22) into (20); the terms of
orders \(R,S,1\) respectively match
\(R/2,S/2,-1-(\log2)/2\).
