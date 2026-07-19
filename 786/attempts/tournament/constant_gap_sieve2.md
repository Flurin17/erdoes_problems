# Small-prime sieve dichotomy: rigorous marginal result and missing row lemma

## Verdict

Put

$$
y=N^{1/u},\qquad
S_y(n)=\sum_{p\le y}w_pv_p(n),\qquad
\Lambda_y=\sum_{\substack{p\le y\\w_p\ne0}}\frac1p .
$$

For a sufficiently large fixed $u$ there is a rigorous **marginal**
dichotomy:

1. if $\Lambda_y$ exceeds a fixed threshold $\delta_u>0$, every atom of
   the small-prime score $S_y(U_N)$ is bounded away from $1$; or
2. if $\Lambda_y<\delta_u$, the zero-weight primes generate a
   positive-density set of $y$-smooth integers $z$ with $f(z)=0$.

This proves a constant gap for nonzero levels when $f(p)=0$ for every
$p>y$.  It does not prove a constant gap for an arbitrary completely
additive $f$: the large-prime remainder is dependent on the small-prime
part, so marginal anti-concentration cannot be convolved into a bound for
the full score.

Fixed and growing $u$ have opposite defects.  For fixed $u$, the
independent-geometric model has a nonzero limiting total-variation error,
although this error becomes extremely small when the chosen fixed constant
$u$ is large.  For $u\to\infty$ slowly the modeling error tends to zero,
but the density of the smooth zero certificate tends to zero as well.

## 1. Exact law and a fixed-$u$ counterexample

Let

$$
D_y(n)=\prod_{p\le y}p^{v_p(n)},\quad
V(y)=\prod_{p\le y}\left(1-\frac1p\right),\quad
\Phi(x,y)=\#\{m\le x:P^-(m)>y\}.
$$

For every $y$-smooth $d\le N$, unique factorization gives

$$
\Pr(D_y(U_N)=d)=\frac{\Phi(N/d,y)}N.                 \tag{1}
$$

Let $G_p$ be independent with
$\Pr(G_p=k)=(1-p^{-1})p^{-k}$, and set
$D_y^*=\prod_{p\le y}p^{G_p}$.  Then

$$
\Pr(D_y^*=d)=\frac{V(y)}d                            \tag{2}
$$

for every $y$-smooth $d\ge1$.

Now fix $u>1$, write $N=y^u$, and choose $a\in(0,1)$.  In the product
model,

$$
K_y=\sum_{y^a<p\le y}\mathbf1_{G_p>0}
$$

converges to a Poisson variable of mean $\log(1/a)$, since

$$
\sum_{y^a<p\le y}\frac1p\to\log(1/a),
\qquad
\sum_{y^a<p\le y}\frac1{p^2}\to0.
$$

Choose an integer $k$ with $ak>u$.  On $K_y\ge k$ one has
$D_y^*>y^{ak}>N$.  Hence

$$
\liminf_{N\to\infty}\Pr(D_y^*>N)
\ge \Pr(\operatorname{Pois}(\log(1/a))\ge k)>0.      \tag{3}
$$

The actual $D_y(U_N)$ is always at most $N$, so the two valuation vectors
have total-variation distance bounded below by the positive constant in
(3).  Thus an $o(1)$ product-model approximation at a fixed $u$ is false.
The same obstruction is visible through the additive score
$w_p=\log p/\log y$: its actual value is at most $u$, while its
product-model value exceeds $u$ with positive probability.

## 2. A small constant error for a large fixed $u$

The standard uniform rough-number form of the one-dimensional fundamental
sieve lemma says that for $x\ge y^s$,

$$
\frac{\Phi(x,y)}{xV(y)}
=1+O\!\left(e^{-c s\log(s+1)}\right)+o_y(1),         \tag{4}
$$

where the $o_y(1)$ is uniform in $x\ge y^s$ when $s$ is fixed.  This
uniform version, not merely pointwise fixed-$s$ asymptotics, is the
external input in this section.  We use iterated limits: first
$N\to\infty$ at fixed $u$, then choose $u$ large.

Take $s=u/2$.  Equations (1), (2), and (4) compare the two laws relatively
on $d\le N/y^s$.  The independent boundary mass satisfies

$$
\Pr(D_y^*>y^{u/2})\le e^{-c_1u\log(u+1)}.            \tag{5}
$$

Indeed, Markov's inequality with
$\theta=(\log u)/(4\log y)$ gives

$$
\mathbb E(D_y^*)^\theta
=\prod_{p\le y}\frac{1-p^{-1}}{1-p^{-1+\theta}},
$$

whose logarithm is $O(u^{1/4})$ by expanding logarithms and applying the
prime Mertens estimate.  The resulting exponent is
$-u\log u/8+O(u^{1/4})$.

Summing the relative error on the interior and controlling the remaining
mass by (5) yields

$$
d_{\rm TV}\!\left(
\mathcal L((v_p(U_N))_{p\le y}),
\bigotimes_{p\le y}\mathcal L(G_p)\right)
\le \varepsilon(u)+o_{N\to\infty}(1),               \tag{6}
$$

where

$$
\varepsilon(u)\le C e^{-c_2u\log(u+1)}.              \tag{7}
$$

For clarity, if the $L^1$ discrepancy on the interior is at most $\eta$
and the product-model boundary mass is $b$, then the actual boundary mass
is at most $b+\eta$, and total variation is at most $b+\eta$.

Equations (3) and (6) are compatible: the error is positive for every fixed
$u$, but its upper bound tends rapidly to zero as the chosen constant $u$
tends to infinity.

There also exists a sufficiently slowly growing diagonal $u=u(N)\to
\infty$ for which (6) is $o(1)$.  This follows by applying (6) successively
at the fixed values $u=3,4,\ldots$ and choosing the transition thresholds
large enough; no unrecorded explicit uniform range is needed.

## 3. Independent-model anti-concentration

**Lemma.**  Let

$$
T=\sum_{p\in P}w_pG_p,\qquad w_p\ne0,\qquad
\Lambda=\sum_{p\in P}\frac1p.
$$

If $0<\delta\le1/8$ and $\Lambda\ge\delta$, then

$$
\sup_t\Pr(T=t)\le1-\frac\delta2.                     \tag{8}
$$

**Proof.**  If some $1/p\ge\delta$, the largest atom of $w_pG_p$ is
$1-1/p\le1-\delta$, and convolution cannot increase a largest atom.
Otherwise choose greedily $B\subseteq P$ with

$$
\delta\le\lambda_B:=\sum_{p\in B}\frac1p<2\delta.
$$

Let $K=\#\{p\in B:G_p>0\}$.  Then

$$
\Pr(K=0)\le e^{-\lambda_B},\qquad
\Pr(K\ge2)\le\frac{\lambda_B^2}{2}.
$$

If $K=1$, the weighted sum is nonzero.  Thus its zero atom is at most

$$
e^{-\lambda_B}+\frac{\lambda_B^2}{2}
\le1-\frac{\lambda_B}{2},
$$

while each nonzero atom is at most
$\Pr(K\ge1)\le\lambda_B<1/4$.  This proves (8) for the partial sum over
$B$, and convolution with the remaining independent summands completes
the proof.  \(\square\)

By data processing and (6), whenever $\Lambda_y\ge\delta$,

$$
\sup_t\Pr(S_y(U_N)=t)
\le1-\frac\delta2+\varepsilon(u)+o(1).               \tag{9}
$$

This conclusion concerns $S_y$, not the full $f$.

## 4. Zero-weight smooth integers

Fix $u>2$, and let $\rho$ be the Dickman function.  Define

$$
\delta_u=\frac{\rho(u)}{4\rho(u-1)}.                 \tag{10}
$$

Let $Z$ be the set of $y$-smooth $z\le N$ all of whose prime divisors
satisfy $w_p=0$.  Every $z\in Z$ has $f(z)=0$, irrespective of the weights
above $y$.

The fixed-$u$ Dickman theorem, uniformly for the parameter in
$[u-1,u]$, gives

$$
\Psi(N,y)=\rho(u)N+o(N)
$$

and, uniformly for $p\le y$,

$$
\Psi(N/p,y)
\le(\rho(u-1)+o(1))\frac Np.                         \tag{11}
$$

Every excluded $y$-smooth integer is divisible by an active prime.  Hence

$$
\begin{aligned}
|Z|
&\ge \Psi(N,y)
 -\sum_{\substack{p\le y\\w_p\ne0}}\Psi(N/p,y)\\
&\ge
\left(\rho(u)-\rho(u-1)\Lambda_y
-o(1)(1+\Lambda_y)\right)N.                         \tag{12}
\end{aligned}
$$

In the low branch $\Lambda_y<\delta_u$, the error is summable and

$$
|Z|\ge\left(\frac34\rho(u)-o(1)\right)N.             \tag{13}
$$

The standard Dickman ratio estimate is

$$
\frac{\rho(u-1)}{\rho(u)}
=u(\log u+\log\log u+O(1)).
$$

Thus $\delta_u$ is only polynomially small in $u$, whereas
$\varepsilon(u)$ is exponentially small in $u\log u$.  A sufficiently
large fixed $u$ therefore has $\varepsilon(u)<\delta_u/4$.  With
$\delta=\delta_u$, (9) and (13) prove the marginal dichotomy stated at the
start.

If all $w_p$ above $y$ vanish, then $f=S_y$, and every nonzero level omits
a fixed positive proportion of $[1,N]$: use (9) in the high branch and the
zero set (13) in the low branch.

## 5. The first invalid inference for an arbitrary score

Write uniquely $n=dm$, where $d$ is $y$-smooth and $m$ is $y$-rough.  The
exact full-level count is

$$
\#\{n\le N:f(n)=t\}
=\sum_{\substack{m\le N\\P^-(m)>y}}
  \#\{d\le N/m:P^+(d)\le y,\ f(d)=t-f(m)\}.          \tag{14}
$$

Both the target $t-f(m)$ and the cap $N/m$ vary with $m$.  Formula (6)
controls only the mixture marginal of $f(d)=S_y(n)$.  It does not control
the sum of rowwise maxima in (14).  Equivalently, $S_y(U_N)$ and the
large-prime remainder $R_y(U_N)$ are dependent, so the independent
convolution inequality used in Section 3 is unavailable.

A sufficient repair lemma is: for some fixed large $u$, prove from
$\Lambda_y\ge\delta_u$ that

$$
\sum_{\substack{m\le N\\P^-(m)>y}}
\max_a\#\{d\le N/m:P^+(d)\le y,\ f(d)=a\}
\le(1-c_u)N.                                        \tag{15}
$$

This is a genuinely conditional, multiscale statement.  Active primes near
$y$ disappear from every row with $N/m<y$, and many short rows are
individually completely concentrated.  Another application of the
marginal approximation (6) cannot prove (15).

## 6. Why growing $u$ does not close the low branch

Although a diagonal $u(N)\to\infty$ makes (6) an $o(1)$ approximation, even
the full set of $y$-smooth integers has density $o(1)$.  This needs no
uniform Dickman asymptotic: for every fixed $K$, eventually $u(N)\ge K$,
so

$$
\Psi(N,N^{1/u(N)})\le\Psi(N,N^{1/K})
=(\rho(K)+o_K(1))N.
$$

Taking first $N\to\infty$ and then $K\to\infty$ proves
$\Psi(N,N^{1/u(N)})=o(N)$.  Also $\delta_u\to0$.  Thus both elementary
gaps vanish in the growing-$u$ regime.

## Route assessment

- Fixed modest $u$: an $o(1)$ product-model approximation is false by
  (3).
- Fixed sufficiently large $u$: a small constant modeling error and the
  marginal active/zero dichotomy are rigorous.
- Growing $u$: the modeling error can be $o(1)$, but the certified gaps
  vanish.
- Arbitrary full score: (15), or an equivalent conditional expansion
  theorem, remains the missing node.

An independent audit confirmed the exact law, fixed-$u$ obstruction,
anti-atom lemma, and fixed-$u$ Dickman union bound.  It identified the need
for the uniform form of (4) and agreed that (15) is the first unresolved
inference.
