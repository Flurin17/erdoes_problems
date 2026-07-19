# Zero-extension from one scale to the next: exact variants

Let \(G\) be an abelian group and let \(f:\mathbb N\to G\) be completely
additive.  For a real parameter \(X\geq 2\), put

\[
 E_X=\{n\leq X:f(n)\ne0\},\qquad B(X)=|E_X|=m.
\]

This note separates three superficially similar assertions about extending a
large zero set from \([1,X]\) to the \(X\)-smooth integers below \(X^2\).

## 1. Pointwise extension is false

Choose a prime \(p_X\) with \(X/2<p_X\leq X\), set

\[
 f(p_X)=1\in\mathbb Q,
 \qquad f(q)=0\quad(q\ne p_X\text{ prime}),
\]

and extend completely additively.  Then the only nonzero integer at most
\(X\) is \(p_X\), so \(B(X)=1=o(X)\).  Nevertheless, for every integer
\(1\leq k\leq X\),

\[
 p_Xk\leq X^2,qquad P^+(p_Xk)\leq X,qquad
 f(p_Xk)=1+v_{p_X}(k)\ne0.
\]

Thus there are at least \(X\) nonzero \(X\)-smooth integers below \(X^2\).
Consequently the hypotheses do **not** imply that all such integers vanish,
nor even that all but \(o(X)\) vanish.  This also rules out any general
extension estimate \(o(XB(X))\).  It does not refute an all-but-\(o(X^2)\)
assertion.

The example amplifies without introducing collisions.  Choose any \(b\)
distinct primes \(P\subset(X/2,X]\), give every prime in \(P\) weight one,
and give every other prime weight zero.  Then \(B(X)=b\).  The products

\[
 pk,\qquad p\in P,\quad 1\leq k\leq\lfloor X/2\rfloor,
\]

are pairwise distinct: if \(pk=q\ell\) with distinct \(p,q\in P\), then
Euclid's lemma gives \(p\mid\ell\), impossible because
\(\ell<X/2<p\).  They are all nonzero and \(X\)-smooth.  Hence

\[
 |T_X|\geq b\lfloor X/2\rfloor .
 \tag{A}
\]

Thus the obstruction has order \(XB(X)\), even with \(B(X)\to\infty\)
whenever enough primes are selected from the interval.

The prime can be supplied by Bertrand's postulate (with harmless rounding of
\(X\)); alternatively one may restrict to integer parameters for which such
a prime has already been chosen.

## 2. A sharp elementary range for density extension

The preceding construction is essentially the obstruction detected by the
most direct injection.

**Lemma.**  Let

\[
 S_X=\{p\leq X:p\text{ is prime and }f(p)\ne0\}.
\]

If \(m=B(X)\), then every \(p\in S_X\) satisfies

\[
 \left\lfloor\frac Xp\right\rfloor\leq 2m,
 \qquad	ext{and hence}\qquad
 p>\frac{X}{2m+1}.
 \tag{1}
\]

Moreover, if

\[
 T_X=\{n\leq X^2:P^+(n)\leq X,\ f(n)\ne0\},
\]

then

\[
 |T_X|\leq (2m+1)mX.
 \tag{2}
\]

**Proof.**  Fix \(p\in S_X\).  Every \(a\leq X/p\) with \(f(a)=0\)
gives a distinct element \(pa\in E_X\), because
\(f(pa)=f(p)\ne0\).  Therefore

\[
 \left\lfloor\frac Xp\right\rfloor-B(X/p)\leq B(X)=m.
\]

As \(B(X/p)\leq m\), this proves the first inequality in (1), and the
second follows from \(\lfloor X/p\rfloor\leq2m\).

The set \(S_X\) is contained in \(E_X\), so \(|S_X|\leq m\).  If an
\(X\)-smooth integer \(n\) has \(f(n)\ne0\), at least one of its prime
divisors belongs to \(S_X\).  The union bound and (1) now give

\[
 |T_X|
 \leq\sum_{p\in S_X}\left\lfloor\frac{X^2}{p}\right\rfloor
 <\sum_{p\in S_X}(2m+1)X
 \leq(2m+1)mX.
\]

This argument uses only the group law; torsion-freeness is unnecessary. \(\square\)

In particular, \(B(X)=o(\sqrt X)\) implies \(|T_X|=o(X^2)\).  The
one-prime example has \(m=1\) and \(|T_X|\geq X\), so the factor \(X\) in
this elementary estimate cannot be removed.  For the substantially weaker
hypothesis \(m=o(X)\), (2) gives no density conclusion.  Any use of such a
conclusion therefore needs an additional multiscale argument; it is not a
formal consequence of complete additivity and the one-scale count.

## 3. A fixed function is a different, trivial variant

Suppose now that \(f\) is one fixed completely additive function and

\[
 B_f(X)=o(X)\qquad(X\to\infty).
\]

Then \(f\) is identically zero.  Indeed, if a fixed prime \(p\) had
\(f(p)\ne0\), the same injection would give

\[
 B_f(X)\geq \left\lfloor\frac Xp\right\rfloor-B_f(X/p)
 =\frac Xp-o(X),
\]

contradicting \(B_f(X)=o(X)\).  Hence every prime has weight zero.  The same
proof works if the little-oh estimate is known only along an unbounded
sequence \(X_j\), since \(B_f(X_j/p)\leq B_f(X_j)=o(X_j)\).

Thus the only genuinely difficult formulation is the triangular/local one
in which the grading itself may depend on \(X\), and “almost all” is measured
on the \(X^2\) scale.  The pointwise statement is false, the fixed-function
statement is trivial, and the local density statement beyond
\(B(X)=o(\sqrt X)\) remains a separate multiscale lemma.
