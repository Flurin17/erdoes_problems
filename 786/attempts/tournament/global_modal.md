# Global largest-prime/cofactor modal completion

## Proposed mechanism

Normalize the desired nonzero level to \(1\). Choose all weights below
\(\sqrt N\) *globally*, with an objective that includes both the
\(\sqrt N\)-smooth integers and every future cofactor bucket. Only after
that choice, complete the weighting prime-by-prime above \(\sqrt N\): an
integer containing such a prime has a unique representation \(pm\), with
\(m<\sqrt N\), so \(w_p\) can be chosen to hit the most frequent value of
the lower-prime grading on \([1,N/p]\). This is not the failed ascending
local greedy algorithm: a lower weight is judged by its effect on *all*
larger-prime buckets. The exact reduction below is a finite Bellman
identity for this global optimization.

The reduction is promising only if one can find a lower-prime grading
which simultaneously has very large (not necessarily equally located)
modal atoms on many initial intervals and has level \(1\) on almost all
\(\sqrt N\)-smooth integers up to \(N\). The last two sections give both a
test for this requirement and a rigorous barrier for the first natural
one-threshold implementation.

Throughout, \(P^+(1)=1\), and all weights and modal values are rational.

## 1. Exact global modal-completion identity

Let \(z\geq\sqrt N\), and let \(g\) be a completely additive rational
function on the \(z\)-smooth integers (equivalently, choose \(g(q)\) for
the primes \(q\leq z\)). Put

\[
 C_g(x;c)=\#\{m\leq x:g(m)=c\},\qquad
 M_g(x)=\max_{c\in\mathbb Q}C_g(x;c),
\]
and
\[
 R_g(N,z)=\#\{n\leq N:P^+(n)\leq z,\ g(n)=1\}.
\]

### Lemma 1 (exact modal completion)

Among all extensions \(f\) of \(g\) obtained by choosing the weights
\(f(p)\) for \(z<p\leq N\), the largest possible size of the level
\(f(n)=1\) in \([1,N]\) is exactly

\[
 \boxed{
 R_g(N,z)+\sum_{z<p\leq N}M_g(\lfloor N/p\rfloor). }
 \tag{1}
\]

Consequently, if \(F(N)\) is the largest size of a nonzero level of any
rational completely additive function on \([1,N]\), then

\[
 F(N)=\max_g\left(
 R_g(N,\sqrt N)+
 \sum_{\sqrt N<p\leq N}M_g(\lfloor N/p\rfloor)
 \right).
 \tag{2}
\]

Here changing \(\sqrt N\) to its integer part has no effect on the
statement.

#### Proof

An integer \(n\leq N\) which is not \(z\)-smooth has exactly one prime
factor \(p>z\), and that factor occurs to exponent one: two such factors,
or \(p^2\), would exceed \(N\). Thus it has a unique form
\(n=pm\), where \(m\leq N/p<\sqrt N\leq z\). The bucket belonging to \(p\)
contains

\[
 \#\{m\leq N/p:g(m)+f(p)=1\}
 =C_g(N/p;1-f(p))
\]

level elements. Different primes \(p>z\) own disjoint buckets and their
weights occur in no other bucket. Hence each \(p\) can, independently,
choose a modal value \(c_p\) and take \(f(p)=1-c_p\), giving (1). The
\(z\)-smooth part is already fixed and contributes \(R_g(N,z)\). Every
global weighting restricts to some \(g\), while every \(g\) has the modal
extension just constructed, proving (2). \(\square\)

This proof also gives an exact defect identity. Write

\[
 E_g(x)=\lfloor x\rfloor-M_g(\lfloor x\rfloor),
 \qquad
 S(N,z)=\#\{n\leq N:P^+(n)\leq z\}.
\]

For the optimal extension of a fixed \(g\), the number of omitted integers
is

\[
 \boxed{
 N-|\{n\leq N:f(n)=1\}|=
 S(N,z)-R_g(N,z)+\sum_{z<p\leq N}E_g(N/p). }
 \tag{3}
\]

Thus a density-\(1-o(1)\) construction at \(z=\sqrt N\) must satisfy both

\[
 S(N,\sqrt N)-R_g(N,\sqrt N)=o(N)                         \tag{4}
\]

and

\[
 \sum_{\sqrt N<p\leq N}
 \left(\lfloor N/p\rfloor-M_g(\lfloor N/p\rfloor)\right)=o(N).
 \tag{5}
\]

Condition (4) asks for level \(1\) on almost every \(\sqrt N\)-smooth
integer. Condition (5) asks for near-total modal concentration, in the
prime-weighted average, on the entire family of cofactor prefixes. This
is the precise compatibility problem hidden by a merely local modal rule.

## 2. The continuum recurrence for threshold cofactors

For \(u>0\), let \(H_k(u)\) denote the limiting proportion of integers
\(m\leq X\) having exactly \(k\) prime factors, counted with multiplicity,
larger than \(X^{1/u}\). Put \(H_0(u)=1\), \(H_k(u)=0\) for \(k\geq1\)
when \(0<u\leq1\). The standard fixed-\(u\) Dickman asymptotic gives

\[
 H_0(u)=\rho(u).
\]

Marking one of the large prime factors gives the useful recurrence

\[
 \boxed{
 H_k(u)=\frac1k\int_0^{u-1}\frac{H_{k-1}(v)}{u-v}\,dv
 \quad(k\geq1). }
 \tag{6}
\]

Indeed, apart from \(o(X)\) integers containing the square of a prime
larger than \(X^{1/u}\), every integer counted by \(H_k\) is counted \(k\)
times after marking one such prime \(p=X^s\). The remaining cofactor has
relative parameter \(v=u(1-s)\). Prime summation changes \(ds/s\) into
\(dv/(u-v)\), proving (6). In particular, for \(1\leq u\leq2\),

\[
 H_0(u)=1-\log u,\qquad H_1(u)=\log u,                    \tag{7}
\]

and all other \(H_k(u)\) vanish. Hence the modal count in this range
switches from \(k=0\) to \(k=1\) exactly at \(u=\sqrt e\).

Here is the first nonlocal family to which (1) applies. Fix
\(0<\alpha<1/2\), set \(y=N^\alpha\), and initially take

\[
 g(q)=
 \begin{cases}
 0,&q\leq y,\\
 1,&y<q\leq\sqrt N.
 \end{cases}                                             \tag{8}
\]

For each \(p>\sqrt N\), choose \(w_p=1-k_p\), where \(k_p\) is an exact
mode of the number of prime factors in \((y,\sqrt N]\) among
\(m\leq N/p\). Unlike the ordinary threshold construction, the top-prime
weight is allowed to be \(0,-1,-2,\ldots\), as dictated by its whole
cofactor bucket.

Let \(M(u)=\max_kH_k(u)\). Prime summation and (6) give the asymptotic
density

\[
 \boxed{
 D(\alpha)=B(\alpha)+T(\alpha), }
 \tag{9}
\]

where

\[
 B(\alpha)=
 \int_\alpha^{1/2}\rho\!\left(\frac{1-s}{\alpha}\right)\frac{ds}{s}
                                                               \tag{10}
\]

is the contribution with no prime above \(\sqrt N\) and exactly one prime
in \((N^\alpha,\sqrt N]\), while

\[
 T(\alpha)=
 \int_0^{1/2}\frac{M(t/\alpha)}{1-t}\,dt                  \tag{11}
\]

is the optimally completed top-prime contribution. For \(t<\alpha\), the
convention in (11) is \(M(t/\alpha)=1\). Formula (9), rather than a
numerical experiment, is a proved asymptotic lower bound furnished by an
explicit rational grading for every fixed \(\alpha\).

To justify (10), mark the unique prime \(q=N^s\in(y,\sqrt N]\); its
cofactor must be \(y\)-smooth. Formula (11) follows by writing
\(p=N^{1-t}\), so that the prime-sum measure for the bucket of size
\(N^t\) is \(dt/(1-t)\). The endpoint ranges can first be truncated and
then restored, so only the usual fixed-parameter Dickman and prime number
theorems are being used.

## 3. A barrier: one threshold plus globally optimal top modes

The modal completion is genuinely more flexible than assigning weight
\(1\) to every prime above \(N^\alpha\). Nevertheless, it cannot improve
the current constant when the base cutoff is at least \(N^{1/4}\).

### Proposition 2

For every fixed \(1/4\leq\alpha<1/2\), the construction (8) with the
globally optimal completion above \(\sqrt N\) has

\[
 D(\alpha)\leq c_*=0.828499\ldots.
 \tag{12}
\]

Equality is attained at the old threshold value

\[
 \alpha_*=(1+\sqrt e)^{-1}.
\]

#### Proof

Write \(r=\sqrt e\), \(R=\rho(2)=1-\log2\), and
\(\alpha_0=1/(2r)\).

First suppose \(\alpha\geq\alpha_0\). Then every top cofactor has
\(u=t/\alpha\leq r<2\). By (7), its zero-factor atom is at least its
one-factor atom. Thus every optimal top weight is \(1\) (with an
irrelevant tie at the endpoint), and the allegedly more general
construction collapses to the ordinary level

\[
 \#\{n\leq N:\Omega_{>N^\alpha}(n)=1\}.
\]

Its limiting density is \(H_1(1/\alpha)\). On \(2\leq u\leq3\), direct
differentiation of the Dickman formula gives

\[
 H_1'(u)=\frac{1-2\log(u-1)}u,                             \tag{13}
\]

whose maximum is at \(u=1+r\). For completeness, on
\(3\leq u\leq2r\), recurrence (6) and integration by parts give

\[
 H_1'(u)=\frac1u-
 \int_1^{u-1}\frac{\rho(v-1)}{v(u-v)}\,dv
 \leq\frac1u\left(1-
 \log\frac{2(u-1)}{u-2}\right)<0.                         \tag{14}
\]

In the inequality only \(1\leq v\leq2\), where \(\rho(v-1)=1\), was
retained. The last logarithm exceeds \(1\) throughout this short range.
Thus \(H_1(u)\leq H_1(1+r)=c_*\).

It remains to treat \(1/4\leq\alpha\leq\alpha_0\). Now
\(t/\alpha\leq2\), so (7) determines the top modes exactly:

\[
 M(t/\alpha)=
 \begin{cases}
 1,&0\leq t\leq\alpha,\\
 1-\log(t/\alpha),&\alpha\leq t\leq r\alpha,\\
 \log(t/\alpha),&r\alpha\leq t\leq1/2.
 \end{cases}                                              \tag{15}
\]

For the bottom term, put \(s_0=1-2\alpha\). On
\([\alpha,s_0]\), the Dickman argument in (10) is at least \(2\), and on
\([s_0,1/2]\) it is at least \(r\). Monotonicity of \(\rho\) therefore
gives

\[
 B(\alpha)\leq
 R\log\frac{1-2\alpha}{\alpha}
 +\frac12\log\frac{1}{2(1-2\alpha)}
 =:\overline B(\alpha).                                  \tag{16}
\]

The total mass of \(dt/(1-t)\) on \([0,1/2]\) is \(\log2\). Subtracting
the modal deficit in (15), and using
\((1-t)^{-1}\geq(1-\alpha)^{-1}\) when \(t\geq\alpha\), gives

\[
 T(\alpha)\leq\log2-
 \frac{\alpha}{1-\alpha}
 \left(
 \int_1^r\log u\,du+
 \int_r^{1/(2\alpha)}(1-\log u)\,du
 \right)
 =:\overline T(\alpha).                                  \tag{17}
\]

Set

\[
 Q(\alpha)=\alpha(1-2r)+1+\tfrac12\log(2\alpha).
\]

Then

\[
 \overline T(\alpha)=\log2-\frac{Q(\alpha)}{1-\alpha}.
\]

The sum \(U=\overline B+\overline T\) is convex on
\([1/4,\alpha_0]\). One quick verification is to put

\[
 H=Q'(\alpha)(1-\alpha)+Q(\alpha)
 =\frac32-2r+\frac1{2\alpha}+\frac12\log(2\alpha).
\]

Here \(H<0\) on the interval (it is already negative at \(1/4\) and is
decreasing), and direct differentiation gives

\[
 U''(\alpha)=
 \frac1{2\alpha^2(1-\alpha)}-
 \frac{2H}{(1-\alpha)^3}+
 \frac{2(2\log2-1)}{(1-2\alpha)^2}+
 \frac{1-\log2}{\alpha^2}>0.                             \tag{18}
\]

It is consequently enough to check the two endpoints. Direct
substitution gives

\[
\begin{aligned}
 U(1/4)
 &=\frac83\log2-(\log2)^2-\frac53+\frac23\sqrt e,\\
 U(1/(2\sqrt e))
 &=\log2-\frac{2-\sqrt e}{2(2\sqrt e-1)}
 +(1-\log2)\log(2(\sqrt e-1))
 +\frac12\log\frac{\sqrt e}{2(\sqrt e-1)}.
\end{aligned}
\]

Elementary power-series interval bounds for \(\log\) and \(e^{1/2}\)
then give the rigorous inequalities

\[
 U(1/4)<0.801,\qquad
 U(1/(2\sqrt e))<0.817.                                  \tag{19}
\]

For an entirely separated lower comparison, use the ordinary threshold
at \(u=8/3\). Since
\(\log(1+x)\leq x-x^2/2+x^3/3\) for \(0\leq x\leq2/3\),

\[
\begin{aligned}
 c_*\geq H_1(8/3)
 &=\log(8/3)-2\int_0^{2/3}\frac{\log(1+x)}{2+x}\,dx\\
 &\geq
 \log(8/3)-\frac{970}{243}+\frac{40}{3}\log(4/3)
 >0.824.
\end{aligned}                                             \tag{20}
\]

The last strict inequality, as well as the two bounds in (19), follows
for example by truncating
\(\log x=2\sum_{j\geq0}z^{2j+1}/(2j+1)\), where
\(z=(x-1)/(x+1)\), with its positive geometric tail bounded explicitly;
for (20), four terms for \(x=8/3\) and two for \(x=4/3\) already give
\(0.82427\). Thus both endpoints in (19) are strictly below \(c_*\).
Equations (16)--(20) finish this range, and hence the proof. \(\square\)

The significance of Proposition 2 is not that modal completion is useless.
It says that the most immediate attempt to make it useful is exhausted:
one must either put the first active cutoff below \(N^{1/4}\), where a top
cofactor can contain at least two active primes, or abandon the single
equal-weight base band altogether.

## 4. Dependency chain and present bottleneck

The positive route would close through the following explicit chain.

1. **Exact split (proved):** Lemma 1 reduces the full finite problem to a
   lower-prime grading \(g\) and the objective (2).
2. **Cofactor recurrence (proved for threshold statistics):** equation
   (6) computes every modal cofactor law of a one-threshold base.
3. **First-family barrier (proved):** Proposition 2 shows that a single
   base band beginning at \(N^\alpha\), \(\alpha\geq1/4\), cannot improve
   \(c_*\), even with exact global modes above \(\sqrt N\).
4. **Needed lower-prime lemma (open):** construct \(g=g_N\) for which the
   two nonnegative defects in (3) have sum \(o(N)\); equivalently, prove
   (4) and (5) simultaneously.

The weakest unsupported step is item 4. Large prefix modes alone are not
enough: their modal centers may differ with \(x\), while (4) insists on the
specific center \(1\) on a different, smooth-number-weighted population.
Conversely, optimizing the smooth part locally may destroy all the prefix
modes. No compatibility lemma currently bridges these objectives.

There are two sharply defined surviving possibilities.

- **Positive:** use at least two lower bands with different rational
  weights, or recurse below \(N^{1/4}\), so that several cofactor count
  vectors can lie on the same affine level. The correct state is the full
  prefix histogram of \(g\), not just its level-\(1\) density.
- **Negative/stability:** prove that (5) forces \(g\), outside a negligible
  prime-harmonic set, to be essentially a one-threshold/equal-weight
  grading. Proposition 2 would then conflict with (4).

## 5. Concrete falsification test and next action

For any proposed finite lower weighting \(g\), compute, exactly,

\[
 \Delta_{\rm sm}=S(N,\sqrt N)-R_g(N,\sqrt N),\qquad
 \Delta_{\rm top}=
 \sum_{\sqrt N<p\leq N}E_g(N/p).                         \tag{21}
\]

Lemma 1 says that the best possible completion has exactly
\(N-\Delta_{\rm sm}-\Delta_{\rm top}\) elements. Thus (21) is a decisive
falsification test: no choice of the top-prime weights can repair a base
grading for which either defect is large. It also checks a claimed modal
algorithm without any search over the top weights.

The next mathematical action should be a two-band version of (6). For
cutoffs \(N^\beta<N^\alpha<\sqrt N\), define the joint limiting masses

\[
 H_{j,k}(u)=\Pr\bigl(
 \Omega_{(N^\alpha,\sqrt N]}=j,
 \Omega_{(N^\beta,N^\alpha]}=k
 \bigr)
\]

at each cofactor scale, derive the marked-prime integral recurrences, and
maximize the mass on affine lines \(aj+bk=c\). A surviving positive
candidate must beat \(c_*\) in the exact objective (9)/(21), not merely in
an unweighted cofactor model. If no two-band affine line improves the
constant, the same recurrence should be repurposed as the first stability
step toward the negative alternative.
