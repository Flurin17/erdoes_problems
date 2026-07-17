# Partial proof: Erdős Problem #143

## Status

The general problem remains open locally. This document proves the stronger
weighted conclusion for every admissible set contained in a fixed lattice
$c\mathbb N$, and reduces the general real problem to one explicit uniform
finite estimate for thick primitive integer sets. The boxed estimate below is
not proved and is the current bottleneck.

## Normalization

Call $A\subset(1,\infty)$ admissible when
\[
|kx-y|\ge1
\quad(x,y\in A, x\ne y, k\in\mathbb Z_{\ge1}).
\]
For $x<y$, it suffices to check $|kx-y|\ge1$: the reversed orientation has
$ky-x\ge y-x\ge1$, using the $k=1$ condition. In particular, admissible sets
are $1$-separated and locally finite. If $A$ is infinite, then $A\subset
[2,\infty)$, since for $1<x<2$ every larger $y$ is within $x/2<1$ of a
positive integer multiple of $x$.

## The fixed-lattice theorem

### Theorem

Let $c>0$, let $S\subset\mathbb N$, and suppose $A=cS\subset(1,\infty)$ is
admissible. Then
\[
\sum_{x\in A}\frac1{x\log x}<\infty,
\qquad
\sum_{\substack{x<N\\x\in A}}\frac1x=o(\log N).
\]

### Proof

For distinct $m,n\in S$,
\[
|k(cm)-cn|=c|km-n|.
\]
Thus admissibility forbids $n=km$: $S$ is primitive, meaning that no
distinct member divides another.

We prove from scratch the needed weighted theorem for primitive integers.
For $a\ge2$, let $P(a)$ be its largest prime factor and define
\[
\mathcal M_a=\{au:u\ge1,\text{ every prime factor of }u\text{ is at least }
P(a)\}.
\]
If $a,b$ belong to a primitive set, then $\mathcal M_a$ and $\mathcal M_b$
are disjoint. Indeed, suppose $au=bv$ and $P(a)\le P(b)$. If
$P(a)<P(b)$, then $v$ has no prime factor below $P(b)$, so the exponent in
$a$ of every prime is at most its exponent in $b$; hence $a\mid b$. If
$P(a)=P(b)=p$, the exponents of every prime below $p$ agree in $a$ and $b$,
and only their exponents of $p$ can differ, so again one divides the other.
Both alternatives contradict primitivity.

Finite inclusion-exclusion gives the natural density
\[
d(\mathcal M_a)=\frac1a\prod_{p<P(a)}\left(1-\frac1p\right).
\]
Consequently, for every finite subset $F$ of a primitive set,
\[
\sum_{a\in F}\frac1a\prod_{p<P(a)}\left(1-\frac1p\right)\le1. \tag{1}
\]

We also need the elementary product estimate
\[
\prod_{p\le z}\left(1-\frac1p\right)^{-1}\le C\log z
\qquad(z\ge2). \tag{2}
\]
To prove it, write $\vartheta(t)=\sum_{p\le t}\log p$. Every prime in
$(m,2m]$ divides $\binom{2m}{m}\le4^m$, so dyadic summation gives
$\vartheta(t)\le C_0t$. Partial summation then yields
\[
\sum_{p\le z}\frac{\log p}{p}\le C_1(1+\log z). \tag{3}
\]
Put $\delta=1/\log z$ and $s=1+\delta$. Unique factorization and the
integral test give
\[
\prod_{p\le z}(1-p^{-s})^{-1}\le\zeta(s)\le1+\log z.
\]
Moreover,
\[
\log\prod_{p\le z}\frac{1-p^{-s}}{1-p^{-1}}
\le2\delta\sum_{p\le z}\frac{\log p}{p}=O(1)
\]
by (3), proving (2).

Since $P(a)\le a$, equations (1) and (2) imply, uniformly over finite $F$,
\[
\sum_{a\in F}\frac1{a\log a}\le C.
\]
Exhausting the primitive set gives
\[
\sum_{a\in S}\frac1{a\log a}<\infty. \tag{4}
\]
If $c\ge1$, then $\log(ca)\ge\log a$. If $0<c<1$, then
$\log(ca)\ge\tfrac12\log a$ once $a\ge c^{-2}$, with only finitely many
exceptions. Thus (4) proves
\[
\sum_{a\in S}\frac1{ca\log(ca)}<\infty.
\]

Finally, for fixed $R$ and $N>R$,
\[
\frac1{\log N}\sum_{\substack{x<N\\x\in A}}\frac1x
\le
\frac1{\log N}\sum_{\substack{x\le R\\x\in A}}\frac1x
+\sum_{\substack{R<x<N\\x\in A}}\frac1{x\log x}.
\]
Let $N\to\infty$ and then $R\to\infty$. This proves the theorem. $\square$

## Finite rationalization of the real problem

### Lemma

Every finite admissible real set $F=\{x_1,\ldots,x_r\}$ can be approximated
arbitrarily closely, coordinate by coordinate, by an admissible set of
rational numbers with one common denominator.

### Proof

Put $a=\min F$, $b=\max F$, and fix $\eta>0$. Choose $s>1$ with
$(s-1)b<\eta/2$. The dilated configuration has strict uniform margin
\[
|ksx_i-sx_j|\ge s.
\]
Choose $K$ so that $(K+1)sa-sb>2$, and then choose $\rho>0$ such that
\[
(K+1)\rho<s-1,qquad
(K+1)(sa-\rho)-(sb+\rho)>1,qquad
\rho<\min(\eta/2,sa-1).
\]
Choose rationals $q_i$ with $|q_i-sx_i|<\rho$. For $1\le k\le K$,
\[
|kq_i-q_j|\ge s-(K+1)\rho>1,
\]
while for $k\ge K+1$,
\[
kq_i-q_j\ge(K+1)(sa-\rho)-(sb+\rho)>1.
\]
Thus the $q_i$ are admissible, exceed $1$, and satisfy
$|q_i-x_i|<\eta$. Clearing denominators writes $q_i=n_i/Q$ with
\[
|kn_i-n_j|\ge Q \tag{5}
\]
for every distinct pair and every $k\ge1$. $\square$

## Exact remaining finite estimate

Call a finite $S\subset\mathbb N$ $Q$-admissible if $n>Q$ for $n\in S$
and (5) holds. Fix $a>1$. The following uniform estimate would settle the
general problem:
\[
\boxed{
\sum_{n\in S}\frac{Q}{n\log(n/Q)}\le C_a
\quad\text{for every finite $Q$-admissible }S\subset[aQ,\infty),
} \tag{6}
\]
where $C_a$ is independent of $Q$ and $S$.

Indeed, an infinite admissible real set has a minimum $m>1$. Choose
$1<a<m$, apply the rationalization lemma to every finite subset with the
approximation kept above $a$, apply (6), and let the approximation tend to
zero. Continuity of $1/(x\log x)$ bounds every finite partial sum by $C_a$;
monotone convergence proves the weighted conclusion, and the theorem's final
tail argument proves the harmonic little-$o$ conclusion.

Estimate (6) remains open. Ordinary primitive-set theory loses the required
factor $Q$, while naive radius-$Q/2$ thickening of the disjoint rough-multiple
sets is false (already $Q=2$, $S=\{5,8\}$ gives rough multiples $25$ and
$24$ whose thickened intervals overlap). Thus this reduction is rigorous but
conditional, and no complete solution is claimed.
