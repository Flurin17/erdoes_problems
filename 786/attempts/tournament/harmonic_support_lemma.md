# Harmonic support lemma for a nearly-zero additive function

Let \(f:\mathbb N\to\mathbb Q\) be completely additive and, for a fixed
\(x\), put
\[
B(t)=\#\{n\le t:f(n)\ne0\},\qquad m=B(x),\qquad \delta=m/x,
\]
and
\[
\mathcal P=\{p\le x:p\text{ prime and }f(p)\ne0\},\qquad
H=\sum_{p\in\mathcal P}\frac1p.
\]

This note records what can be obtained without analytic
anti-concentration.

## 1. The first active prime is large

**Lemma 1.** Every \(p\in\mathcal P\) satisfies
\[
 \left\lfloor\frac{x}{p}\right\rfloor\le 2m,
 \qquad\text{and hence}\qquad p>\frac{x}{2m+1}.
\]

**Proof.** Among the integers \(n\le x/p\), at least
\(\lfloor x/p\rfloor-m\) have \(f(n)=0\). For each such integer,
\(f(pn)=f(p)\ne0\). The map \(n\mapsto pn\) injects these integers into
the exceptional set in \([1,x]\), which has size \(m\). Thus
\(\lfloor x/p\rfloor-m\le m\). The second assertion follows. \(\square\)

In particular \(\#\mathcal P\le m\), since every active prime is itself
exceptional.

## 2. A support-only lower bound

If \(n\le x\) has exactly one active prime factor counted with
multiplicity, then \(f(n)\ne0\). Indeed, writing \(n=pk\) with
\(p\in\mathcal P\) and with \(k\) divisible by no prime in
\(\mathcal P\), one has \(f(k)=0\), hence \(f(n)=f(p)\ne0\).
Consequently
\[
 m\ge \#\left\{n\le x:\sum_{p\in\mathcal P}v_p(n)=1\right\}.            \tag{1}
\]
This statement is independent of all additive relations among the
nonzero values \(f(p)\).

## 3. A quantitative small-\(H\) dichotomy

Define
\[
 X(n)=\sum_{p\in\mathcal P}v_p(n)
\]
on the uniform probability space \(1\le n\le x\). For every
nonnegative integer \(k\),
\[
 {\bf 1}_{k=1}\ge k-k(k-1).
\]
Therefore (1) gives
\[
 \delta\ge\mathbb P(X=1)
 \ge\mathbb EX-\mathbb E X(X-1).                                      \tag{2}
\]
For the first moment,
\[
\begin{aligned}
\mathbb EX
 &=\frac1x\sum_{p\in\mathcal P}\sum_{\substack{j\ge1\\p^j\le x}}
       \left\lfloor\frac{x}{p^j}\right\rfloor\\
 &\ge H-\frac{\#\mathcal P}{x}\ge H-\delta.                            \tag{3}
\end{aligned}
\]

Put \(y=x/(2m+1)\). Lemma 1 gives \(p>y\) for every active prime.
Write
\[
 A_p=\sum_{j\ge1}p^{-j}=\frac1{p-1},\qquad
 S=\sum_{p\in\mathcal P}A_p.
\]
For \(p\ne q\), the contribution to the ordered second factorial
moment from prime-power indicators belonging to \(p\) and \(q\) is at
most \(A_pA_q\). For a fixed \(p\), the contribution from ordered pairs
of distinct powers is at most
\[
 \sum_{j\ne k}p^{-\max(j,k)}
 =2\sum_{k\ge2}(k-1)p^{-k}=\frac{2}{(p-1)^2}.
\]
Here floor errors only decrease the upper bound. Hence
\[
 \mathbb E X(X-1)
 \le S^2+\sum_{p\in\mathcal P}\frac1{(p-1)^2}.                          \tag{4}
\]

Provided \(y>2\), comparison with the full integer tail gives
\[
\begin{aligned}
0\le S-H
 &=\sum_{p\in\mathcal P}\frac1{p(p-1)}
 \le 2\sum_{n>y}\frac1{n^2}\le\frac{2}{y-1},\\
\sum_{p\in\mathcal P}\frac1{(p-1)^2}
 &\le4\sum_{n>y}\frac1{n^2}\le\frac4{y-1}.                             \tag{5}
\end{aligned}
\]
Combining (2)--(5) gives the explicit inequality
\[
 \delta\ge H-\delta-
 \left(H+\frac2{y-1}\right)^2-\frac4{y-1}.                             \tag{6}
\]

Thus, along a sequence with \(x\to\infty\) and \(\delta\to0\), (6)
implies
\[
 H-H^2\le o(1).
\]
In particular, if \(H\le1-\eta\) for a fixed \(\eta>0\), then
\[
 H=O_\eta(\delta+1/x).
\]
So a triangular counterexample to
\[
 B_f(x)=o(x)\quad\Longrightarrow\quad
 \sum_{\substack{p\le x\\f(p)\ne0}}\frac1p=o(1)
\]
must, after passage to a subsequence, have \(\liminf H\ge1\). A
one-level “exactly one active factor” sieve cannot deal with that
regime: its natural independent-model lower bound is \(H e^{-H}\),
which also vanishes when \(H\to\infty\).

## 4. Exact collision descent

There is additional algebraic rigidity in the maps from zero
cofactors. Suppose
\[
 pk=q\ell\le x,\qquad f(k)=f(\ell)=0,
\]
where \(p,q\in\mathcal P\) are distinct. Applying \(f\) first gives
\(f(p)=f(q)\). Unique factorization then gives
\[
 k=qr,\qquad \ell=pr
\]
for an integer \(r\), and hence
\[
 f(r)=-f(p)\ne0,\qquad r\le\frac{x}{pq}.                               \tag{7}
\]
So images belonging to different prime-value classes never collide,
and every collision inside one class consumes a strictly smaller
exceptional residual. Any completely elementary closure of the
large-\(H\) case must exploit (7) iteratively; a first-moment union
bound does not suffice.

## Status

The lemmas above are unconditional. They do **not** prove the full
implication in the large-harmonic-mass regime, nor do they provide a
counterexample. That remaining regime is precisely where a
Kubilius/compound-Poisson concentration estimate, or an iterative use
of the collision descent (7), is needed.
