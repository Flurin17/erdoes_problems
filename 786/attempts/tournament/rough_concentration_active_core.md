# Bounded active mass leaves a linear zero core

## Outcome

Let \(f:\mathbb N\to\mathbb Q\) be completely additive and call a prime
\(p\) *active* when \(f(p)\ne0\).  This note proves the following uniform
boundary-sensitive statement.

**Theorem 1 (linear zero core).**  For every fixed \(K<\infty\) there is
\(c_K>0\) such that, for all sufficiently large \(N\), if

\[
 \sum_{\substack{p\leq \sqrt N\\ f(p)\ne0}}\frac1p\leq K,       \tag{1}
\]

then

\[
 \#\{n\in(N/2,N]:f(n)=0,\ P^+(n)<N^{1/4}\}\geq c_KN.          \tag{2}
\]

Thus every nonzero level of \(f\) omits a fixed positive proportion of
\([1,N]\), with the proportion allowed to depend on the reciprocal active
mass bound.  The proof is elementary apart from the prime number theorem
in fixed polynomial intervals.

This closes the bounded-reciprocal-mass prime-avoidance bottleneck denoted
`(PA)` in `finite_uniform.md`.  It also upgrades the prime-tuple lemma in
`profile_lpf_charge.md`: there the small factor was required to be one
zero-coloured prime, giving harmonic mass \(\asymp\log\log N\).  It can be
any integer composed of zero-coloured primes; a short tilted-Dirichlet
argument gives harmonic mass \(\gg_K\log N\), and hence a linear rather
than \(N\log\log N/\log N\) family.

## 1. Harmonic mass of the zero core

We first record the input that supplies the missing factor
\(\log N/\log\log N\).

**Lemma 2 (harmonic prime avoidance).**  Let \(X\geq2\) be an integer and
let \({\cal S}\) be any set of primes at most \(X\) satisfying

\[
 \sum_{p\in{\cal S}}\frac1p\leq K.                              \tag{3}
\]

Put

\[
 {\cal B}(X,{\cal S})=
 \{b\leq X:p\mid b\Longrightarrow p\notin{\cal S}\}.
\]

There is an explicit \(d_K>0\), independent of \(X\) and of
\({\cal S}\), such that

\[
 \sum_{b\in{\cal B}(X,{\cal S})}\frac1b\geq d_K\log X          \tag{4}
\]

for all sufficiently large \(X\).

### Proof

Treat every prime greater than \(X\) as allowed and set

\[
 A=2K+\log2,
 \qquad \sigma=1+\frac A{\log X}.
\]

The Dirichlet series of the multiplicative semigroup avoiding
\({\cal S}\) is

\[
 F(\sigma)=\zeta(\sigma)\prod_{p\in{\cal S}}(1-p^{-\sigma}).    \tag{5}
\]

For \(0\leq u\leq1/2\), \(\log(1-u)\geq-2u\).  Hence (3) gives

\[
 \prod_{p\in{\cal S}}(1-p^{-\sigma})
 \geq \exp\!\left(-2\sum_{p\in{\cal S}}p^{-\sigma}\right)
 \geq e^{-2K}.                                                   \tag{6}
\]

Also \(\zeta(\sigma)\geq1/(\sigma-1)=\log X/A\).  The entire tail,
even without the prime-avoidance restriction, satisfies

\[
 \sum_{b>X}b^{-\sigma}
 \leq\int_X^\infty t^{-\sigma}\,dt
 =\frac{e^{-A}\log X}{A}
 =\frac{e^{-2K}\log X}{2A}.                                    \tag{7}
\]

Subtracting (7) from (5)--(6) yields

\[
 \sum_{b\in{\cal B}(X,{\cal S})}b^{-\sigma}
 \geq\frac{e^{-2K}}{2A}\log X.                                 \tag{8}
\]

Since \(b^{-\sigma}\leq b^{-1}\), (4) follows with
\(d_K=e^{-2K}/(2(2K+\log2))\).  \(\square\)

The point of Lemma 2 is that it is a harmonic assertion.  Turning (8)
directly into a cardinality bound gives only a polynomial-size set.  The
next step uses a fixed tuple of medium zero-coloured primes to transport
every small zero-core integer into \((N/2,N]\), where the reciprocal
weights become cardinality.

## 2. A clean medium-prime band

Write \(L=\log N\).  For integers \(i\geq i_0\), put

\[
 a_i=2^{-i-1},\qquad I_i=(N^{a_i},N^{2a_i}].                    \tag{9}
\]

Choose \(i_0\) as a sufficiently large absolute constant.  By the prime
number theorem and partial summation,

\[
 \sum_{p\in I_i}\frac1p=\log2+o(1)                              \tag{10}
\]

for each fixed \(i\).

Fix a sufficiently small absolute \(\varepsilon_0>0\), chosen in the
local convolution estimate below, and inspect

\[
 H=\lfloor K/\varepsilon_0\rfloor+2
\]

consecutive intervals (9).  At least one of them, say
\(I=(N^a,N^{2a}]\), satisfies

\[
 \sum_{\substack{p\in I\\f(p)\ne0}}\frac1p\leq\varepsilon_0.  \tag{11}
\]

Indeed, otherwise their disjoint union would violate (1).  The possible
values of \(a\) form a finite set depending only on \(K\).  Increasing
\(i_0\), we may and do arrange

\[
 2a<1/4                                                        \tag{12}
\]

and the harmless interior condition used below.

Define measures on logarithmic exponent space by

\[
 \begin{aligned}
 \mu&=\sum_{p\in I}\frac1p\,\delta_{\log p/L},\\
 \nu&=\sum_{\substack{p\in I\\f(p)\ne0}}
             \frac1p\,\delta_{\log p/L},\\
 \mu_0&=\mu-\nu.
 \end{aligned}                                                \tag{13}
\]

Thus \(\mu_0\) is supported on zero-coloured primes and
\(\|\nu\|\leq\varepsilon_0\).

Let \(W\) be any interval of length between fixed positive multiples of
\(1/L\), contained in

\[
 [(3-1/10)a,(3+1/10)a].
\]

The PNT in fixed multiplicative intervals gives absolute constants
\(c,C>0\) such that

\[
 (\mu*\mu)(W)\geq c\frac{|W|}{a},
 \qquad
 \sup_x\mu(W-x)\leq C\frac{|W|}{a}.                            \tag{14}
\]

For clarity, the limiting convolution density at \(s\) is

\[
 \int_{[a,2a]\cap[s-2a,s-a]}\frac{dt}{t(s-t)},                 \tag{15}
\]

which is \(\asymp1/a\) uniformly on the displayed central interval.
The finite-\(N\) form (14) follows by one prime summation and the PNT in
intervals whose endpoint ratio is bounded away from one.  Moreover,

\[
 \mu^{*2}-\mu_0^{*2}=\nu*\mu+\mu_0*\nu\leq2\nu*\mu.
\]

Taking \(\varepsilon_0<c/(4C)\), equations (11) and (14) give

\[
 \mu_0^{*2}(W)\geq c'\frac{|W|}{a}.                             \tag{16}
\]

## 3. Fixed zero-prime tuples near every required product size

Put

\[
 J=[(3-1/20)a,(3+1/20)a].                                      \tag{17}
\]

By making \(i_0\) larger, there is an integer \(k=k(a)\) for which
\(1\) lies in the interior of \(kJ\).  Since only finitely many values of
\(a\) occur for a fixed \(K\), there is a \(\delta=\delta_K>0\) such
that

\[
 [1-2\delta,1]\subset\operatorname{int}(kJ)                    \tag{18}
\]

for the selected \(a\).  Set \(r=2k\).

Convolving (16) \(k\) times gives, uniformly for
\(s\in[1-\delta,1]\),

\[
 \mu_0^{*r}([s-\log2/L,s])\geq\frac{c_a}{L}.                   \tag{19}
\]

Here is a fully discrete justification of the \(1/L\) scale.  Put
\(h=\log2/L\).  Choose a constant \(\theta_a>0\) so small that
\(k\theta_a<(\log2)/4\), and partition a slightly shrunken copy
\(J'\Subset J\) into cells of length

\[
 \ell=\theta_a/L.                                             \tag{19a}
\]

Because the target interval lies a fixed positive distance inside \(kJ\),
the polytope

\[
 \{(x_1,\ldots,x_{k-1})\in(J')^{k-1}:
       s-x_1-\cdots-x_{k-1}\in J'\}
\]

has volume bounded below uniformly for \(s\in[1-\delta,1]\), after
shrinking \(\delta\) if necessary.  It therefore contains
\(\gg_a L^{k-1}\) grid boxes.  For each such choice of the first
\(k-1\) cells, choose the forced last cell so that the Minkowski sum of
all \(k\) cells lies in \([s-h,s]\); the total width
\(k\ell<h/4\) leaves the required endpoint slack.  Every cell has
\(\mu_0^{*2}\)-mass \(\gg_a1/L\) by (16).  The resulting boxes in
\(J^k\) are disjoint, so multiplying their masses and summing gives
\(\gg_a L^{k-1}L^{-k}=c_a/L\).  For fixed \(K\), the possible
\((a,k)\)'s form a finite set, so \(\theta_a\), all margins, and all PNT
thresholds can be made uniform over that set.

Tuples in (19) with a repeated prime have total reciprocal mass

\[
 O_r\!\left(
     \sum_{q>N^a}\frac1{q^2}
     \left(\sum_{p\in I}\frac1p\right)^{r-2}
 \right)=O_r(N^{-a})=o(1/L).                                  \tag{20}
\]

After reducing \(c_a\), (19) therefore counts only ordered tuples of
\(r\) distinct zero-coloured primes.

## 4. Harmonic-to-cardinality transport and injectivity

Choose

\[
 0<\delta_0<\min(\delta,a/2),\qquad
 X=\lfloor N^{\delta_0}\rfloor.                               \tag{21}
\]

Let

\[
 {\cal B}=\{b\leq X:p\mid b\Longrightarrow f(p)=0\}.           \tag{22}
\]

For \(b\in{\cal B}\), take

\[
 s_b=1-\frac{\log b}{L}\in[1-\delta_0,1].
\]

Equations (19)--(20), with a harmless endpoint convention, say that

\[
 \sum_{\substack{(q_1,\ldots,q_r)\in(I\cap\mathbb P)^r\\
                   q_i\ {\rm distinct},\ f(q_i)=0\\
                   N/(2b)<q_1\cdots q_r\leq N/b}}
 \frac1{q_1\cdots q_r}
 \geq\frac{c_a}{L}.                                            \tag{23}
\]

Every product \(Q=q_1\cdots q_r\) in (23) exceeds \(N/(2b)\), so
\(1/Q<2b/N\).  Consequently the number of ordered tuples in (23) is at
least

\[
 \frac{c_aN}{2bL}.                                             \tag{24}
\]

After forgetting the ordering, the loss is exactly at most \(r!\).

The map

\[
 (b,\{q_1,\ldots,q_r\})\longmapsto bq_1\cdots q_r             \tag{25}
\]

is injective.  Indeed, every prime factor of \(b\) is at most
\(b\leq N^{\delta_0}<N^a\), whereas every \(q_i>N^a\).  Unique
factorization therefore recovers \(b\) as the complete part supported
below \(N^a\), and recovers the unordered \(q_i\)'s as the factors above
\(N^a\).  Notice that \(b\) need not be prime or squarefree; this is the
point that supplies the improvement.

Every integer in (25) lies in \((N/2,N]\), has grading zero, and by
(12) has largest prime factor below \(N^{1/4}\).  Summing (24) over
\(b\in{\cal B}\), dividing by \(r!\), and applying Lemma 2 to the active
primes at most \(X\), gives

\[
 \begin{aligned}
 \#\{n\in(N/2,N]:f(n)=0,\ P^+(n)<N^{1/4}\}
 &\geq \frac{c_aN}{2r!L}\sum_{b\in{\cal B}}\frac1b\\
 &\geq \frac{c_a d_K\delta_0}{2r!}\,N.
 \end{aligned}                                                \tag{26}
\]

This proves Theorem 1.  All constants may deteriorate very rapidly with
\(K\), but they are positive and independent of \(N\) and of the moving
set of active primes.

## 5. Closing the finite problem with exact-value concentration

We use the following standard dependency.

**Halász--Ruzsa interval concentration theorem.**  If \(F\) is a real
additive function, \(x\geq3\), and \(h>0\), put

\[
 E_h(F;x)=\inf_{\tau\in\mathbb R}\left[
 \left(\frac{\tau}{h}\right)^2+
 \sum_{p\leq x}\frac1p
 \min\left\{1,
 \left(\frac{F(p)-\tau\log p}{h}\right)^2\right\}\right].       \tag{27}
\]

Then, with an absolute implied constant,

\[
 \sup_u\frac1x
 \#\{n\leq x:u<F(n)\leq u+h\}
 \ll(1+E_h(F;x))^{-1/2}.                                      \tag{28}
\]

The archimedean term \((\tau/h)^2\) in (27) is essential.  Omitting it
would make (28) false for functions close to \(c\log n\).

Here is the exact-point corollary needed below.  Suppose \(F(p)\in\mathbb Z\)
for all \(p\leq x\), and write

\[
 H(F;x)=\sum_{\substack{p\leq x\\F(p)\ne0}}\frac1p.
\]

Choose

\[
 0<h<\min\left\{\frac14,\frac1{4\sqrt{1+H(F;x)}\log x}\right\}. \tag{29}
\]

For each \(\tau\), either
\(|\tau|/h\geq\sqrt{H(F;x)}\), in which case the first term of
(27) is at least \(H(F;x)\), or

\[
 |\tau|\log x<h\sqrt{H(F;x)}\log x\leq\frac14.
\]

In the latter case, every active prime satisfies

\[
 |F(p)-\tau\log p|\geq\frac34>h,
\]

so the prime sum in (27) is at least \(H(F;x)\).  Consequently
\(E_h(F;x)\geq H(F;x)\).  An exact atom fits in an interval of length
\(h\), and (28) gives

\[
 \boxed{\quad
 \sup_t\frac1x\#\{n\leq x:F(n)=t\}
 \ll(1+H(F;x))^{-1/2}.
 \quad}                                                       \tag{30}
\]

The constant in (30) is uniform when \(F\), its integer scale, and \(h\)
depend on \(x\).  For a rational completely additive \(f\), multiply the
finitely many weights \(f(p)\), \(p\leq x\), by a common denominator and
set all later prime weights to zero.  This produces an integer-valued
completely additive \(F\) agreeing with a scalar multiple of \(f\) on
\([1,x]\), so (30) applies without changing either the fibers or the
active primes up to \(x\).

**Corollary 3 (absolute finite gap).**  There is an absolute
\(\eta>0\) such that, for all sufficiently large \(N\), every rational
completely additive \(f\) and every \(t\ne0\) satisfy

\[
 \#\{n\leq N:f(n)=t\}\leq(1-\eta)N.                            \tag{31}
\]

Indeed, let \(C\) be an absolute constant in (30), and take
\(K=4C^2\).  If \(H(f;N)\geq K\), equation (30), with an inessential
enlargement of \(K\), bounds the fiber by at most \(N/2\).  If
\(H(f;N)<K\), Theorem 1 supplies at least \(c_KN\) integers with value
zero.  They are disjoint from the nonzero \(t\)-fiber, which therefore has
size at most \((1-c_K)N\).  Taking
\(\eta=\min(1/2,c_K)\), with constants adjusted for the finite initial
range, proves (31).

Thus the finite question in the verbatim statement has a negative answer
under the repetition-allowed reading: not only is density \(1-o(1)\)
impossible, every such PLR set misses a fixed positive proportion.  The
square-root escaping-support example passes the proof's stress test: its
active mass is bounded, and Theorem 1 supplies a genuine zero-core gap
without replacing the finite valuation law by independent geometrics.

## 6. Falsification checklist

The vulnerable points, all explicit above, are:

1. the tail in Lemma 2 is subtracted from the *full* Dirichlet series,
   while terms at most \(X\) cannot involve a prime greater than \(X\);
2. the local prime window in (14) has exponent width \(\asymp1/L\), hence
   a fixed multiplicative endpoint ratio, so ordinary PNT is sufficient;
3. repeated \(q_i\)'s are removed before dividing by \(r!\);
4. \(b<N^a<q_i\) makes (25) genuinely injective even when \(b\) is
   composite and has prime powers;
5. the harmonic sum in (26) is over *all* zero-core integers, not merely
   zero primes.

Any counterexample to Theorem 1 must break one of these five exact steps.
