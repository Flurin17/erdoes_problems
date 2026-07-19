# Exact-atom concentration versus the zero kernel

This note isolates a standard-theorem route which rules out a density-one
finite level set for *arbitrary* prime weights.  It also records which input
still needs its precise literature-free audit before the route is promoted.

Let
\[
 f(n)=\sum_{p\leq N}v_p(n)w_p,
 \qquad A_t=\{n\leq N:f(n)=t\},
 \qquad S=\{p\leq N:w_p\neq0\},
\]
where the weights take values in any torsion-free abelian group (in the
application they may be taken rational), and put
\(H(S)=\sum_{p\in S}1/p\).

## 1. An exact chain lemma

**Lemma.**  If \(f(d)\neq0\), then
\[
 N-|A_t|\geq \lfloor N/d\rfloor .                 \tag{1}
\]

**Proof.**  Partition \([N]\) into the \(d\)-adic chains
\[
 r,rd,rd^2,\ldots \quad(d\nmid r).
\]
Along a chain the values are \(f(r)+j f(d)\), and hence are distinct.  A
level contains at most one member of each chain.  The number of chains is
the number of integers at most \(N\) not divisible by \(d\), namely
\(N-\lfloor N/d\rfloor\).  This proves (1).  \(\square\)

In particular, if \(m=N-|A_t|\), then
\[
 f(d)=0\qquad\left(d\leq\left\lfloor\frac{N}{m+1}\right\rfloor\right).
                                                        \tag{2}
\]
This is stronger than the two-row pigeonhole version with denominator
\(2m+1\).

## 2. The concentration--sieve dichotomy

The following is the exact-point form of the Halasz concentration theorem
for additive functions.

**Concentration input (statement to audit).**  There is an absolute
constant \(C\) such that, uniformly in \(N\), in the additive function, and
in the target,
\[
 \frac1N\max_t|A_t|
 \leq \frac{C}{\sqrt{1+H(S)}}.                    \tag{3}
\]

Only exact equality is involved here.  In particular there is no lower
cutoff on \(|w_p|\); every nonzero prime increment is counted.  This point is
essential, since interval-concentration theorems have a logarithmic-drift
exception which is irrelevant to (3).

Suppose a sequence of nonzero levels has mass tending to one.  Equation
(3) implies
\[
 H(S)\leq M                                             \tag{4}
\]
for one absolute constant \(M\).  On the other hand every integer having no
prime factor in \(S\) has value zero, hence lies outside a nonzero target
level.  It remains to know that a prime set of bounded reciprocal mass
cannot sift out almost every integer.

Here is a convenient standard lower-mean input.  It is stated in the form
needed below so that its hypotheses can be checked directly.

**Nonnegative multiplicative lower-mean input (statement to audit).**
Let \(g:\mathbb N\to[0,1]\) be multiplicative.  If for some
\(\alpha>0,B<\infty\)
\[
 \sum_{p\leq y}\frac{g(p)\log p}{p}
 \geq \alpha\log y-B\qquad(y\geq2),               \tag{5}
\]
then
\[
 \frac1x\sum_{n\leq x}g(n)
 \geq c(\alpha,B)
 \prod_{p\leq x}\left(1-\frac{1-g(p)}p\right).    \tag{6}
\]
This is a usual Hildebrand/Wirsing lower-mean theorem for nonnegative
multiplicative functions.  The exact attribution and the uniformity in
(5)--(6) must be checked before this note is used as a completed proof.

Apply it to
\[
 g(n)=\mathbf 1_{(\forall p\in S)\ p\nmid n}.
\]
Condition (5) follows uniformly from (4).  Indeed choose
\(\eta=\exp(-(M+3))\).  Mertens' prime reciprocal estimate gives, uniformly
for all sufficiently large \(y\),
\[
 \sum_{y^\eta<p\leq y}\frac1p
 =\log(1/\eta)+o(1)>M+2.
\]
After deleting the primes of \(S\), reciprocal mass at least one remains in
that interval.  Since \(\log p\geq\eta\log y\) there,
\[
 \sum_{p\leq y}\frac{g(p)\log p}{p}
 \geq \eta\log y.
\]
The bounded range of \(y\) is absorbed into \(B=B(M)\).  Moreover
\[
 \prod_{p\leq N}\left(1-\frac{1-g(p)}p\right)
 =\prod_{p\in S}\left(1-\frac1p\right)
 \geq c_0 e^{-C_0M}>0.                              \tag{7}
\]
Thus (6) and (7) give
\[
 \#\{n\leq N:f(n)=0\}\geq c(M)N.                  \tag{8}
\]
Every nonzero level therefore has density at most \(1-c(M)\).  Combining
(3) and (8), and taking the worse of the two cases \(H(S)>M\) and
\(H(S)\leq M\), gives an absolute gap below one.

## 3. Why a variance-only martingale proof does not suffice

For \(S=(\sqrt N,N]\) with all increments equal, every fixed active-free
core has a star fiber: its center has value zero and all \(d\) leaves have
the same nonzero value.  The conditional modal mass is \(d/(d+1)\), which
can be arbitrarily close to one.  Consequently Efron--Stein, independent
geometric prime models, and a spectral gap on one fiber cannot prove the
needed uniform gap.  The lower-mean step above is precisely the required
cross-fiber/cross-scale charge: bounded total active reciprocal mass leaves
a positive-density zero kernel, while unbounded mass is ruled out by exact
anti-concentration.

## Status

The chain lemma and the reduction from (3),(6) to (8) are complete.  The
route becomes a complete finite negative result once the precise uniform
forms (3) and (6) are either supplied as accepted standard theorems or
proved locally.  Until that audit, this is a conditional route, not a
finished proof.
