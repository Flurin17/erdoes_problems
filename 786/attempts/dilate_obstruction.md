# Dilates and fixed-prime anti-concentration

## 1. Mechanism

Under the repetition-allowed interpretation, product-length rigidity forces
all valuation vectors of the set onto one exact level of a completely
additive rational function.  A prime on which this function is nonzero then
creates a multiplicative chain on which the levels are all different.  One
prime already gives the sharp chain bound

\[
 |A\cap[1,N]|\le N-\lfloor N/p\rfloor.
\]

To aggregate many such primes, use harmonic measure.  Factoring off a finite
set of primes turns their valuations into independent geometric random
variables.  Each geometric variable contains, with probability comparable to
\(1/p\), an independent fair bit.  Sperner's theorem then gives a
Littlewood--Offord anti-concentration estimate for every exact nonzero level.
Combining that estimate with the density of integers having no nonzero-weight
prime gives a universal gap from density one.  In particular, the infinite
question has a **negative answer when repetitions are allowed**.  The argument
does not settle the finite question, because its grading may depend on \(N\)
and its nonzero prime support may escape to infinity.

## 2. Interpretation handled

Throughout Sections 1--8, \(r,s\ge 1\), factors may be repeated, and an
infinite set claimed to have density is assumed to have natural density.  The
argument also applies if only a positive lower natural density is assumed.
It does not apply to the internally-distinct/repetition-free interpretation:
the grading reduction below uses integer coefficients larger than one.

Write

\[
 v(n)=(v_p(n))_p\in \mathbb Q^{(\mathcal P)}.
\]

If \(A\) is product-length rigid, then there is a \(\mathbb Q\)-linear
functional \(L\) on \(\mathbb Q^{(\mathcal P)}\) such that
\(L(v(a))=1\) for every \(a\in A\).  Indeed, first define

\[
 L\left(\sum_{a\in F}q_a v(a)\right)=\sum_{a\in F}q_a
 \tag{2.1}
\]

on the span of \(v(A)\).  This is well-defined: after clearing denominators,
any relation among the \(v(a)\)'s becomes an equality of two products with
repetition, and rigidity says that the two coefficient sums agree.  (Also
\(1\notin A\), since \(1=1\cdot1\).)  Extend \(L\) to the ambient rational
vector space.  Then

\[
 f(n):=L(v(n))=\sum_p f(p)v_p(n)
 \tag{2.2}
\]

is a completely additive rational function, \(f(mn)=f(m)+f(n)\), and

\[
 A\subseteq B_1(f):=\{n\in\mathbb N:f(n)=1\}.
 \tag{2.3}
\]

Thus it suffices to bound a nonzero exact fiber of an arbitrary completely
additive rational function.

## 3. Chain of intermediate lemmas

The route consists of the following precise implications.

1. **Single-prime chain lemma.**  If \(f(p)\ne0\), every chain
   \(\{mp^k:k\ge0\}\), \(p\nmid m\), meets a fiber \(B_t(f)\) at most once.
   Hence
   \[
   |B_t(f)\cap[1,N]|\le N-\lfloor N/p\rfloor.
   \tag{3.1}
   \]

2. **Disjoint-dilate lemma.**  If \(f(d_i)\) are pairwise distinct, then the
   sets \(d_iB_t(f)\) are pairwise disjoint.  If \(B_t(f)\) has natural
   density \(\delta\), this gives
   \[
   \delta\sum_i\frac1{d_i}\le1.
   \tag{3.2}
   \]
   Taking \(d_i=p^i\) recovers \(\delta\le1-1/p\).

3. **Finite-prime harmonic factorization.**  For a finite set \(P\) of
   nonzero-weight primes, the upper logarithmic density of \(B_t(f)\) is at
   most the largest atom of
   \[
   \sum_{p\in P}f(p)V_p,
   \qquad
   \Pr(V_p=k)=(1-1/p)p^{-k}\quad(k\ge0),
   \tag{3.3}
   \]
   where the \(V_p\)'s are independent.

4. **Geometric Littlewood--Offord lemma.**  Put
   \[
   \lambda_P:=\sum_{p\in P}\frac{2(p-1)}{p^2}.
   \tag{3.4}
   \]
   For arbitrary nonzero real coefficients \(c_p\), every atom of
   \(\sum_{p\in P}c_pV_p\) has probability at most
   \[
   e^{-\lambda_P/8}+\sqrt{\frac2{\lambda_P}}.
   \tag{3.5}
   \]
   Since \(2(p-1)/p^2\ge1/p\), the same upper bound holds with
   \(H_P:=\sum_{p\in P}1/p\) in place of \(\lambda_P\).

5. **Support dichotomy.**  If
   \(S=\{p:f(p)\ne0\}\) and \(\sum_{p\in S}1/p=\infty\), (3.5), applied to
   growing finite subsets, makes every exact fiber have logarithmic upper
   density zero.  If the sum is finite and \(t\ne0\), then every member of
   \(B_t(f)\) is divisible by a prime in \(S\), so
   \[
   \overline d(B_t(f))
   \le 1-\prod_{p\in S}(1-1/p).
   \tag{3.6}
   \]

6. **Universal gap.**  Optimizing only very crudely between (3.5) and (3.6)
   gives
   \[
   d(A)\le 1-e^{-16}
   \tag{3.7}
   \]
   for every repetition-allowed product-length-rigid \(A\subset\mathbb N\).

All of these claims are proved in the next section.

## 4. Fully proved obstruction theorem

### Theorem 4.1 (fixed-prime support obstruction)

Let \(f:\mathbb N\to\mathbb Q\) be completely additive, let \(t\ne0\), and
put

\[
 B_t=\{n:f(n)=t\},\qquad
 S=\{p:f(p)\ne0\},\qquad
 H=\sum_{p\in S}\frac1p.
\]

For every finite \(P\subseteq S\), writing
\(H_P=\sum_{p\in P}1/p\),

\[
 \overline\delta_{\log}(B_t)
 \le e^{-H_P/8}+\sqrt{2/H_P}.
 \tag{4.1}
\]

Consequently:

- if \(H=\infty\), then \(B_t\) has logarithmic upper density zero;
- if \(H<\infty\), then
  \[
  \overline d(B_t)
  \le 1-\prod_{p\in S}(1-1/p)
  \le 1-e^{-2H};
  \tag{4.2}
  \]
- every set \(A\subseteq B_t\) having natural density \(\delta\) satisfies
  \[
  \delta\le1-e^{-16}.
  \tag{4.3}
  \]

Here

\[
 \overline\delta_{\log}(E)
 :=\limsup_{X\to\infty}\frac1{\log X}
       \sum_{\substack{n\le X\\n\in E}}\frac1n.
\]

#### Proof: single-prime chains and dilates

For \(p\in S\) and \(p\nmid m\),

\[
 f(mp^k)=f(m)+k f(p).
\]

These values are pairwise distinct as \(k\) varies.  Thus a fixed fiber meets
each \(p\)-chain at most once.  The chains meeting \([1,N]\) are indexed by
their \(p\)-free roots \(m\le N\), of which there are exactly
\(N-\lfloor N/p\rfloor\).  This proves (3.1).

More generally, if the values \(f(d_i)\) are distinct and
\(d_ib=d_jb'\) with \(b,b'\in B_t\), then

\[
 f(d_i)+t=f(d_j)+t,
\]

a contradiction.  Hence the dilates are disjoint.  A dilation \(d_iB_t\)
has density \(\delta/d_i\) whenever \(B_t\) has density \(\delta\), and
finite additivity of density proves (3.2).  Applying this to
\(1,p,p^2,\ldots,p^K\) and letting \(K\to\infty\) gives
\(\delta\le1-1/p\).

#### Proof: an exact Littlewood--Offord bound

We first prove a probabilistic lemma.  Let \(P\) be finite, let
\(c_p\ne0\) be arbitrary real numbers, and let the independent variables
\(V_p\) have the geometric laws in (3.3).  Set

\[
 \alpha_p=\frac{2(p-1)}{p^2},\qquad
 \lambda=\sum_{p\in P}\alpha_p.
\]

The law of \(V_p\) has the following exact mixture representation.  With
probability \(\alpha_p\), let \(V_p=Z_p\), where \(Z_p\) is a fair bit in
\(\{0,1\}\).  With the remaining probability, use a residual variable whose
unnormalized masses are

\[
 (1-1/p)^2\quad\text{at }0,qquad
 0\quad\text{at }1,qquad
 (1-1/p)p^{-k}\quad\text{at }k\ge2.
\]

This is indeed the geometric law: the fair component contributes
\(\alpha_p/2=(1-1/p)/p\) at both 0 and 1.  At 0 the residual plus this
contribution is \(1-1/p\); at 1 it is \((1-1/p)/p\); and the masses for
\(k\ge2\) are unchanged.  The displayed residual masses sum to
\(1-\alpha_p\).

Choose these mixture representations independently.  Condition on the set
\(J\) of primes for which the fair component was chosen and on every residual
variable.  If \(M=|J|\), the remaining random part of the weighted sum is

\[
 \sum_{p\in J}c_pZ_p.
\]

After replacing \(Z_p\) by \(1-Z_p\) whenever \(c_p<0\), all coefficients
may be made positive at the cost of a constant translation.  The subsets of
\(J\) giving one prescribed sum form an antichain: two properly nested
subsets cannot have equal sums when every coefficient is positive.

For completeness, Sperner's bound follows by choosing a uniformly random
maximal chain in the Boolean lattice.  A fixed \(k\)-subset belongs to that
chain with probability \(1/\binom Mk\).  The events corresponding to members
of an antichain are disjoint, so

\[
 \sum_{E\in\mathcal F}\binom M{|E|}^{-1}\le1,
\]

and therefore

\[
 |\mathcal F|\le\binom M{\lfloor M/2\rfloor}.
\]

The central binomial probability obeys

\[
 2^{-M}\binom M{\lfloor M/2\rfloor}\le\frac1{\sqrt{M+1}}.
 \tag{4.4}
\]

Here is a short proof.  For \(M=2k\), put
\(a_k=4^{-k}\binom{2k}k\).  Since \(a_{k+1}/a_k=(2k+1)/(2k+2)\),

\[
 \frac{(2k+3)a_{k+1}^2}{(2k+1)a_k^2}
 =\frac{(2k+1)(2k+3)}{(2k+2)^2}<1.
\]

As \(a_0=1\), this proves \(a_k\le(2k+1)^{-1/2}\).  For \(M=2k+1\), the
central probability is \(a_k(2k+1)/(2k+2)\), whose square is at most
\((2k+2)^{-1}\).  Thus (4.4) holds in both parities.

The variable \(M\) is a sum of independent Bernoulli variables of mean
\(\lambda\).  Exponential Markov gives

\[
 \begin{aligned}
 \Pr(M<\lambda/2)
 &\le e^{\lambda/2}\mathbb E e^{-M}\\
 &\le \exp\bigl((1/2-(1-e^{-1}))\lambda\bigr)\\
 &\le e^{-\lambda/8}.
 \end{aligned}
 \tag{4.5}
\]

The last inequality uses \(e^{-1}<3/8\).  On the complementary event,
(4.4) is at most \(\sqrt{2/\lambda}\).  Averaging over all mixture and
residual choices proves, for every real \(y\),

\[
 \Pr\left(\sum_{p\in P}c_pV_p=y\right)
 \le e^{-\lambda/8}+\sqrt{2/\lambda}.
 \tag{4.6}
\]

Finally,

\[
 \alpha_p=\frac{2(p-1)}{p^2}\ge\frac1p
\]

for every prime \(p\), and the right side of (4.6) decreases with its
argument.  Hence (4.6) remains true with \(H_P\) in place of \(\lambda\).

#### Proof: transfer from geometric concentration to logarithmic density

Fix a finite \(P\subseteq S\), and put

\[
 C_P=\prod_{p\in P}(1-1/p),\qquad
 Z_P=C_P^{-1}.
\]

Every integer has a unique factorization \(n=um\), where all prime factors of
\(u\) lie in \(P\) and \(m\) is coprime to \(\prod_{p\in P}p\).  Consequently,

\[
 \sum_{\substack{n\le X\\f(n)=t}}\frac1n
 =\sum_{\substack{m\le X\\(m,\prod_{p\in P}p)=1}}\frac1m
   \sum_{\substack{u\le X/m\\p\mid u\Rightarrow p\in P\\
                    f(u)=t-f(m)}}\frac1u.
 \tag{4.7}
\]

For any prescribed value \(y\), the unrestricted inner level sum is

\[
 \sum_{\substack{(e_p)\in\mathbb Z_{\ge0}^P\\
                  \sum f(p)e_p=y}}
       \prod_{p\in P}p^{-e_p}
 =Z_P\Pr\left(\sum_{p\in P}f(p)V_p=y\right).
\]

Thus (4.7) is at most

\[
 Z_P Q_P
 \sum_{\substack{m\le X\\(m,\prod_{p\in P}p)=1}}\frac1m,
\]

where \(Q_P\) is the largest atom in (3.3).  Inclusion--exclusion and the
harmonic-sum estimate give

\[
 \sum_{\substack{m\le X\\(m,\prod_{p\in P}p)=1}}\frac1m
 =C_P\log X+O_P(1).
\]

After division by \(\log X\), (4.6) proves (4.1).

If \(H=\infty\), finite subsets \(P\) can have arbitrarily large \(H_P\), so
the right side of (4.1) tends to zero.  This proves the first consequence.

#### Proof: the support alternative and the universal constant

Now suppose \(H<\infty\).  Since \(t\ne0\), every \(n\in B_t\) is divisible
by at least one prime of \(S\).  The union of these sets of multiples has
density

\[
 1-\prod_{p\in S}(1-1/p).
\]

To justify the infinite product directly, use the usual finite
inclusion--exclusion formula and note that the upper density of the union of
the multiples of primes in a tail \(T\subset S\) is at most
\(\sum_{p\in T}1/p\), which tends to zero.  Moreover, for
\(0\le x\le1/2\),

\[
 -\log(1-x)=\sum_{k\ge1}\frac{x^k}{k}
 \le\frac{x}{1-x}\le2x.
\]

It follows that

\[
 \prod_{p\in S}(1-1/p)\ge e^{-2H},
\]

proving (4.2).

Let \(A\subseteq B_t\) have natural density \(\delta\).  Partial summation
shows that its logarithmic density is also \(\delta\): if
\(|A\cap[1,x]|=\delta x+o(x)\), then

\[
 \sum_{\substack{n\le X\\n\in A}}\frac1n
 =\delta\log X+o(\log X).
\]

If \(H\le8\), (4.2) gives

\[
 \delta\le1-e^{-2H}\le1-e^{-16}.
\]

If \(H>8\), choose a finite \(P\subseteq S\) with \(H_P>8\).  Then (4.1)
gives

\[
 \delta\le e^{-1}+\frac12<1-e^{-16}.
\]

The case \(H=\infty\) was already shown to give \(\delta=0\).  This proves
(4.3) and Theorem 4.1.  \(\square\)

### Corollary 4.2 (negative infinite answer with repetition)

Every repetition-allowed product-length-rigid set \(A\subseteq\mathbb N\)
of natural density \(\delta\) satisfies

\[
 \delta\le1-e^{-16}.
\]

Therefore the infinite assertion in the verbatim problem is false under this
interpretation: for any \(0<\epsilon\le e^{-16}\), no such set can have
density greater than \(1-\epsilon\).

#### Proof

Use the grading construction (2.1)--(2.3), and apply Theorem 4.1 with
\(t=1\).  \(\square\)

### Corollary 4.3 (finite fixed-prime necessary condition)

Let \(A\subseteq[1,N]\) be repetition-allowed product-length rigid, and let
\(f\) be any grading with \(f(a)=1\) on \(A\).  If \(f(p)\ne0\), then

\[
 |A|\le N-\lfloor N/p\rfloor.
 \tag{4.8}
\]

Thus, if \(|A|\ge(1-\eta)N\) and
\(\eta<1/p-1/N\), necessarily \(f(p)=0\).  In particular, along any
hypothetical sequence \(|A_N|=(1-o(1))N\), its grading must vanish at every
fixed prime for all sufficiently large \(N\).

#### Proof

This is the single-prime chain count already proved above.  \(\square\)

## 5. Quantitative density calculation

The constants are deliberately crude but completely explicit.

- A single active prime costs at least a \(1/p+O(1/N)\) proportion in a
  finite interval, by (4.8), and at least \(1/p\) in an infinite natural
  density.
- A finite active-prime set with reciprocal mass \(H_P\) forces logarithmic
  concentration at most
  \[
  g(H_P):=e^{-H_P/8}+\sqrt{2/H_P}.
  \]
- Infinite reciprocal mass forces logarithmic density zero.
- Finite reciprocal mass \(H\le8\) leaves an uncovered set of density at
  least \(e^{-2H}\ge e^{-16}\).
- When \(H>8\), anti-concentration already gives the much stronger estimate
  \(e^{-1}+1/2<0.868\).

Thus the universal missing proportion obtained here is

\[
 e^{-16}\approx1.12535\times10^{-7}.
\]

No optimization of the cutoff 8, of the mixture, or of the Chernoff estimate
is needed to refute the quantified infinite claim.

## 6. Weakest unsupported step / exact limitation

There is no unsupported step in the infinite repetition-allowed obstruction:
the grading reduction, anti-concentration estimate, harmonic-density transfer,
and support calculation are all proved above.

The unresolved point on this route is the **finite asymptotically-full
question**.  Corollary 4.3 only forces the nonzero support of a grading
\(f_N\) to move beyond every fixed prime as \(N\to\infty\).  That is compatible
with taking \(f_N(p)=0\) on an expanding initial set of primes.  The harmonic
argument is global across all scales; it cannot simply be applied to a fiber
chosen separately at each \(N\).  In particular, a dense subset of
\([1,N]\) can have very small normalized harmonic mass by omitting a long but
\(o(N)\)-sized initial interval.  Any finite obstruction needs an
interval-local anti-concentration lemma, not an unjustified appeal to the
infinite theorem.

The repetition-free reading is a second exact limitation: (2.1) need not be
well-defined there, so none of the additive-fiber conclusions may be imported
without a new reduction.

## 7. Concrete falsification tests

The route can be attacked at three sharply specified points.

1. Produce a completely additive \(f\) and \(t\ne0\) whose fiber has natural
   density greater than \(1-e^{-16}\).  This would directly falsify Theorem
   4.1; a merely large finite prefix would not.
2. For a finite prime set \(P\), enumerate exponent vectors with geometric
   weights and find an atom of \(\sum c_pV_p\) exceeding (4.6).  Such an
   example would have to invalidate either the exact fair-bit mixture or the
   conditional Sperner bound.
3. For the finite lemma, find \(p\) with \(f(p)\ne0\) and two points of one
   \(p\)-chain in the same fiber.  Complete additivity makes their values
   differ by a nonzero multiple of \(f(p)\), so this test should be
   impossible.

Boundary checks: \(S=\varnothing\) gives no nonzero fiber; \(p=2\) gives
\(\alpha_p=1/p=1/2\); signs and rational dependencies among the \(f(p)\)'s
are allowed by the Sperner proof; and arbitrary prime powers are included by
the geometric variables.

## 8. Next action and repair path

1. Promote Corollary 4.2 to the main ledger as a complete negative resolution
   of the **infinite, repetitions-allowed** reading, then have fresh agents
   audit (2.1), the harmonic factorization (4.7), and the density comparison.
2. For the finite reading, seek a localized replacement for (4.7): on a
   multiplicative window \([x,(1+\theta)x]\), either prove anti-concentration
   from the active primes well below \(x\), or prove that most of the window
   must be supported on primes where \(f_N=0\).  Combine this with (4.8) as a
   density increment across successively larger prime ranges.
3. If such localization fails because support can escape with \(N\), turn the
   failure into a construction: set the grading to zero on an expanding smooth
   core and explicitly analyze the exact level contributed by the remaining
   large primes.  The proof obligation is a cardinality estimate on
   \([1,N]\), not a global harmonic-density estimate.
4. Treat the repetition-free convention independently, since the decisive
   grading necessity is absent there.
