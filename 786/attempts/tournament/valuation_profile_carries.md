# Valuation profiles and the carry obstruction

## Proposed mechanism

The most tempting density-one construction is a discretized logarithm.  If one
could make a completely additive integer-valued function satisfy

\[
 F(n)=\left\lfloor D\frac{\log n}{\log N}\right\rfloor,
\]

then its level \(D-1\) would contain every
\(N^{1-1/D}\le n<N\), hence \(N-o(N)\) integers even for fixed
\(D\ge2\).  A multiscale version tries to assign the high digit from the
largest prime and then use successively smaller primes to supply the carries.

The obstruction is that a completely additive function is a *linear* sum of
its prime digits.  A carry is a nonlinear function of the previously
accumulated residue.  Adding more digit levels only replaces the original
prime weight by another single prime weight; it never creates the required
state dependence.  The lemmas below make this precise for three natural
versions of the construction.

## 1. Exact carry triples

**Lemma 1 (a carry must be deleted).**  Put

\[
 L_D(n)=D\frac{\log n}{\log N}.
\]

Let \(F\) be completely additive and integer-valued.  If \(a,b,ab\le N\)
and

\[
 \{L_D(a)\}+\{L_D(b)\}\ge1,
\]

then \(F(m)=\lfloor L_D(m)\rfloor\) cannot hold simultaneously for
\(m=a,b,ab\).

**Proof.**  Complete additivity gives

\[
 F(ab)=F(a)+F(b).
\]

The displayed fractional-part inequality gives

\[
 \lfloor L_D(ab)\rfloor
 =\lfloor L_D(a)\rfloor+\lfloor L_D(b)\rfloor+1,
\]

which is incompatible with the preceding identity.  \(\square\)

Thus a recursive construction which claims to reproduce the rounded-log
profile on several lower scales must hit every carry triple with an
exception.  In particular, a correction of the form
\(F(p)=\lfloor L_D(p)\rfloor+c(p)\) does not implement a carry: it merely
changes the fixed prime error from \(-\{L_D(p)\}\) to
\(c(p)-\{L_D(p)\}\).

## 2. Collision-free positional digits are too rigid

Partition a set of primes into blocks \(P_0,\ldots,P_J\).  Let
\(R_j\ge2\), put \(Q_0=1\), and put
\(Q_{j+1}=R_jQ_j\).  Consider

\[
 F(n)=\sum_{j=0}^J Q_jX_j(n),\qquad
 X_j(n)=\sum_{p\in P_j}v_p(n).
\]

**Lemma 2 (no-carry positional obstruction).**  Suppose

\[
 \max_{n\le N}X_j(n)<R_j\qquad(0\le j\le J).
\]

If \(t=\sum_jQ_jd_j\), with \(0\le d_j<R_j\), then

\[
 F(n)=t\quad\Longleftrightarrow\quad X_j(n)=d_j
 \text{ for every }j.
\]

Consequently, if \(t\ne0\), then for at least one block \(j\),

\[
 \frac1N\#\{n\le N:F(n)=t\}
 \le \sum_{p\in P_j}\frac1p.
\]

In particular, refining the hierarchy into blocks having maximum reciprocal
prime mass \(o(1)\) makes every nonzero exact level have density \(o(1)\),
not density \(1-o(1)\).

**Proof.**  The size assumption means that the displayed expression for
\(F(n)\) is already its unique mixed-radix expansion; no carry is possible.
This proves the equivalence.  If \(t\ne0\), choose \(j\) with \(d_j>0\).
Then every point of the level is divisible by some prime of \(P_j\), and the
union bound gives

\[
 \#\{n\le N:F(n)=t\}
 \le\sum_{p\in P_j}\left\lfloor\frac Np\right\rfloor.
\]

Divide by \(N\).  \(\square\)

This leaves only deliberately colliding digits.  Small fixed bases do allow
arithmetic carries, but equality of the final integer still imposes all the
corresponding congruence conditions; they do not compute the carry of the
real logarithmic sum.

## 3. A general bounded-error log code has vanishing atoms

The following proposition covers arbitrary signed prime-by-prime corrections,
not just floors or nearest-integer rounding.

**Proposition 3 (sublinear-error log-lattice obstruction).**  Let
\(D=D(N)\to\infty\) with \(D=o(\log N)\), and let
\(E=E(N)\ge0\) satisfy \(E=o(D)\).  For every prime \(p\le N\), let
\(a_p\in\mathbb Z\) satisfy

\[
 \left|a_p-D\frac{\log p}{\log N}\right|\le E.
\]

Extend \(F\) completely additively by
\(F(n)=\sum_{p\le N}a_pv_p(n)\).  Then, uniformly in \(t\in\mathbb Z\),

\[
 \#\{n\le N:F(n)=t\}
 \ll \frac{N}{\sqrt{\log(D/(E+1))}}=o(N).
\]

**Dependency.**  This uses the standard quantitative Halasz concentration
theorem for an additive function \(g\):

\[
 \sup_z\frac1x\#\{n\le x:g(n)=z\}
 \ll
 \left(1+\sum_{\substack{p\le x\\g(p)\ne0}}\frac1p\right)^{-1/2}.
 \tag{HC}
\]

The constant in (HC) is absolute and the statement is uniform in an
\(x\)-dependent additive function.  This exact-atom formulation, rather than
an interval-concentration variant, is the only external theorem used here.

**Proof.**  If

\[
 p>N^{(E+1)/D},
\]

then \(D\log p/\log N>E+1\), and hence the approximation assumption forces
\(a_p\ne0\).  Mertens' prime-reciprocal estimate, uniformly because
\((E+1)\log N/D\to\infty\), gives

\[
 \begin{aligned}
 \sum_{\substack{p\le N\\a_p\ne0}}\frac1p
 &\ge \sum_{N^{(E+1)/D}<p\le N}\frac1p\\
 &=\log\!\left(\frac{D}{E+1}\right)+o(1).
 \end{aligned}
\]

Substitution in (HC) proves the claim.  \(\square\)

After multiplying rational weights by a common denominator, Proposition 3
says that *every* fine logarithmic lattice whose primewise carry corrections
are even \(o(D)\), uniformly in the prime, has vanishing maximum atom.  The
obstruction is not merely that the most obvious rounding convention was
chosen badly.

There is also a useful profile-free consequence of the same theorem.  If

\[
 H_N(F)=\sum_{\substack{p\le N\\F(p)\ne0}}\frac1p,
\]

then every exact level of fixed positive density forces \(H_N(F)=O(1)\).
Indeed, (HC) gives

\[
 \frac1N\max_t\#\{n\le N:F(n)=t\}
 \ll (1+H_N(F))^{-1/2}.
\]

Thus a carry hierarchy cannot keep activating logarithmic blocks whose total
reciprocal-prime mass tends to infinity, regardless of the signs, bases, or
congruences assigned to those blocks.  Proposition 3 is the special case in
which logarithmic approximation itself forces
\(H_N(F)\ge\log(D/(E+1))+o(1)\).

## 4. Bounded harmonic support leaves a positive zero core

The missing rough-core statement in fact follows from the standard uniform
lower mean-value theorem of Hildebrand for nonnegative multiplicative
functions.  A precise form sufficient here is the following.

**Uniform lower mean-value theorem (standard dependency).**  For each
\(\eta>0\) there is \(c_\eta>0\) such that, uniformly over multiplicative
\(g:\mathbb N\to[0,1]\) satisfying

\[
 \sum_{p\le x}(1-g(p))\frac{\log p}{p}
 \le (1-\eta)\log x,
 \tag{HM}
\]

one has

\[
 \frac1x\sum_{n\le x}g(n)
 \ge c_\eta
 \prod_{p\le x}\left(1-\frac1p\right)
 \left(\sum_{\nu\ge0}\frac{g(p^\nu)}{p^\nu}\right).
 \tag{HLM}
\]

Only this finite, uniform lower-bound form is needed; an asymptotic mean-value
theorem for a single fixed multiplicative function would not suffice.

**Lemma 4 (uniform rough core).**  For every fixed \(H<\infty\) there is
\(c(H)>0\) such that, for every sufficiently large \(N\) and every set of
primes \(S\subseteq\{p:p\le N\}\) satisfying

\[
 \sum_{p\in S}\frac1p\le H,
\]

one has

\[
 \#\{n\le N:p\nmid n\text{ for every }p\in S\}\ge c(H)N.
 \tag{RC}
\]

**Proof.**  Define the completely multiplicative \(0\)-\(1\) function
\(g\) by \(g(p)=0\) for \(p\in S\) and \(g(p)=1\) otherwise.  Put

\[
 B_S(y)=\sum_{\substack{p\le y\\p\in S}}\frac{\log p}{p}.
\]

The layer-cake identity is

\[
 \frac{B_S(y)}{\log y}
 =\int_0^1
 \sum_{\substack{y^u\le p\le y\\p\in S}}\frac1p\,du.
 \tag{1}
\]

The integrand is at most \(H\), and Mertens' estimate bounds it by
\(\log(1/u)+o_H(1)\), uniformly away from an initial interval of length
\(o_H(1)\).  Hence

\[
 \frac{B_S(y)}{\log y}
 \le \int_0^1\min\{H,\log(1/u)\}\,du+o_H(1)
 =1-e^{-H}+o_H(1).
 \tag{2}
\]

For large \(y\), condition (HM) therefore holds with
\(\eta=e^{-H}/2\).  Applying (HLM) at \(x=N\), its Euler product simplifies
exactly to

\[
 \prod_{p\in S}\left(1-\frac1p\right)
 \ge \exp(-H-C_0),
\]

where \(C_0\) is absolute.  Since the left side of (HLM) is precisely the
proportion of \(S\)-free integers, (RC) follows.  Bounded \(N\) can be
absorbed by decreasing \(c(H)\).  \(\square\)

The dependence on \(H\) must be very poor.  For example, taking all primes
\(p>N^{e^{-H}}\) has reciprocal mass \(H+o(1)\), while its zero core is the
set of \(N^{e^{-H}}\)-smooth integers, of limiting density
\(\rho(e^H)>0\).

## 5. Consequence: an absolute finite density gap

**Theorem 5.**  There is an absolute \(\varepsilon_0>0\) such that every
real completely additive \(F\), every \(N\), and every nonzero \(t\) satisfy

\[
 \#\{n\le N:F(n)=t\}\le(1-\varepsilon_0)N
\]

apart from a harmless adjustment of \(\varepsilon_0\) for bounded \(N\).

**Proof.**  Let

\[
 S=\{p\le N:F(p)\ne0\},\qquad H=\sum_{p\in S}\frac1p,
\]

and write \(Q=N^{-1}\#\{n\le N:F(n)=t\}\).  By (HC), for an absolute
constant \(C\),

\[
 Q\le C(1+H)^{-1/2}.
 \tag{3}
\]

Choose a fixed \(H_0\) so large that the right side of (3) is at most
\(1/2\) whenever \(H>H_0\).  If \(H\le H_0\), Lemma 4 supplies at least
\(c(H_0)N\) integers having no prime divisor in \(S\).  Every such integer
has \(F(n)=0\), and hence is absent from the nonzero level.  Therefore

\[
 Q\le1-c(H_0).
\]

Taking \(\varepsilon_0=\min\{1/2,c(H_0)\}\) proves the claim.  \(\square\)

Combined with the already proved grading characterization, Theorem 5 rules
out the density-\(1-o(1)\) finite construction in the repetition-allowed
reading of Problem 786.  The proof is uniform in \(N\)-dependent weights.
It depends on the exact uniform formulations (HC) and (HLM), so those two
standard-theorem imports should be independently audited before promotion to
the main proof.

## What remains outside the obstruction

These results rule out the two clean implementations of a valuation profile:

1. digits separated enough to avoid collisions (Lemma 2); and
2. a fine lattice which follows normalized logarithmic size with sublinear
   integer error (Proposition 3).

An escaping construction would have to use genuine collisions and corrections
\(a_p-D\log p/\log N\) of order \(D\) on some primes (or abandon uniform
logarithmic approximation altogether).  It would therefore cease to be a
uniformly accurate size code.  It
would also have to arrange those large signed errors to cancel on almost every
factorization, despite (HC).  No such mechanism was found.

The weakest unresolved step toward a universal negative result is an inverse
statement: prove that an exact level of density \(1-o(1)\) forces, after
integer rescaling, a sublinear-error logarithmic profile on enough reciprocal
prime mass to invoke Proposition 3.  Fixed-frequency multiplicative phases
only give an approximate logarithm modulo phase, so they do not by themselves
supply this inverse statement.

Lemma 4 supplies an alternative to this inverse theorem and closes the finite
density-one question.  The inverse problem remains interesting only if one
wants a much sharper numerical gap or a classification of near-extremizers.

## Falsification tests

A claimed hierarchical construction should be checked in this order.

1. Scale all rational weights to integers and record the effective denominator
   \(D\).
2. If its digit bases exceed all possible digit counts, apply Lemma 2.
3. If \(D\to\infty\), compute
   \(E=\max_p|a_p-D\log p/\log N|\).  The condition \(E=o(D)\) invokes
   Proposition 3.
4. Exhibit an explicit carry triple from Lemma 1 for every claimed recursive
   floor-log identity.
5. If the construction survives, its essential new feature must be a family
   of unbounded signed prime errors; test their exact atom numerically rather
   than only their variance or approximate concentration.
