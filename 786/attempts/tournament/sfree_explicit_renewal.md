# An explicit renewal bound for prime avoidance

This note isolates the quantitative part of the squarefree/prime-avoidance
compactness argument. The compactness lemma is recorded as an input; the
renewal estimate and the deduction of the uniform constant are proved here.

For a set of primes \(S\), put
\[
A_S(N):=\#\{n\le N:p\nmid n\text{ for every }p\in S\}.
\]
Only primes at most \(N\) affect this quantity.

## Compactness input

We use the following factorial-moment compactness statement.

**Prime-avoidance compactness lemma.** Fix \(M\ge0\). Given any sequence
\(N_j\to\infty\) and sets of primes \(S_j\) satisfying
\[
\sum_{p\in S_j}\frac1p\le M,
\]
there is a subsequence on which
\[
\frac{A_{S_j}(N_j)}{N_j}\longrightarrow V_*e^{-h}q_a(1). \tag{C}
\]
Here
\[
V_*:=\prod_{p\in S_*}\left(1-\frac1p\right),
\]
where \(S_*\) is the stable set of fixed primes, \(h\ge0\), and
\(a:[0,1]\to[0,1]\) is measurable. These data obey the budget
\[
\sum_{p\in S_*}\frac1p+h+\int_0^1\frac{a(u)}u\,du\le M. \tag{B}
\]
The function \(q_a\) is nonnegative and continuous on \([0,1]\), satisfies
\(q_a(0)=1\), and, for \(0<r\le1\),
\[
r q_a(r)=\int_0^r(1-a(u))q_a(r-u)\,du. \tag{R}
\]

This lemma is the qualitative compactness part of the argument and is not
reproved here. Its factorial-moment proof uses Mertens' estimate for
reciprocal prime sums and the standard fixed-\(k\) almost-prime estimate
\[
B_k(x)/x=o(1)\qquad(k\text{ fixed}),
\]
where one may take \(B_k(x)\) to count squarefree integers with exactly \(k\)
prime factors (the corresponding estimate with \(\Omega(n)=k\) is equally
sufficient). These inputs justify passage from every fixed factorial moment
to (C). The subsequence/diagonal argument supplies no uniform modulus of
convergence.

## Quantitative renewal lemma

**Lemma.** Let \(M\ge0\), let \(0\le a\le1\) be measurable, and suppose
\[
\int_0^1\frac{a(u)}u\,du\le M. \tag{1}
\]
If a nonnegative continuous function \(q\), with \(q(0)=1\), satisfies (R),
then
\[
q(1)\ge
\exp\!\left(-\frac{4M}{e^{-2M}(1-e^{-M}/2)}\right)
\ge \exp(-8Me^{2M}). \tag{2}
\]

**Proof.** Write
\[
A(r)=\int_0^r a(u)\,du,
\qquad B(r)=\int_0^r(1-a(u))\,du,
\qquad \alpha=e^{-M}.
\]
We first prove the bathtub bound
\[
B(r)\ge \alpha r\qquad(0<r\le1). \tag{3}
\]
Fix \(r\), and abbreviate \(B=B(r)\). If \(B=0\), then \(a=1\) almost
everywhere on \((0,r)\), contradicting the finiteness in (1). The two masses
\[
\int_0^B a(u)\,du
\quad\text{and}\quad
\int_B^r(1-a(u))\,du
\]
are equal. Since \(1/u\) is decreasing,
\[
\begin{aligned}
\int_0^r\frac{a(u)}u\,du-\int_B^r\frac{du}{u}
&=\int_0^B\frac{a(u)}u\,du
  -\int_B^r\frac{1-a(u)}u\,du\\
&\ge0.
\end{aligned}
\]
Consequently
\[
M\ge\int_0^r\frac{a(u)}u\,du\ge\log\frac rB,
\]
which is (3).

Put
\[
\beta=1-\frac\alpha2,
\qquad m(R)=\min_{0\le s\le R}q(s),
\qquad \eta(R)=\frac{A(R)}R.
\]
We claim that for every \(0<R\le1\),
\[
m(R)\ge
\exp\!\left(-\frac{2\eta(R)}{\alpha\beta}\right)m(\beta R). \tag{4}
\]
Choose \(t\in[0,R]\) with \(q(t)=m(R)\). If \(t\le\beta R\), then
\(m(R)=m(\beta R)\), so (4) is immediate. Suppose instead that
\(t>\beta R\). Set
\[
h_0=\frac{\alpha t}{2},
\quad D=\int_0^{h_0}(1-a(u))\,du,
\quad C=\int_{h_0}^t(1-a(u))\,du.
\]
By (3) and \(D\le h_0\),
\[
C=B(t)-D\ge\alpha t-\frac{\alpha t}{2}
=\frac{\alpha t}{2}. \tag{5}
\]
For \(u\ge h_0\),
\[
0\le t-u\le t-h_0=\beta t\le\beta R.
\]
Splitting (R) at \(h_0\) and using the definitions of the two minima gives
\[
t m(R)\ge Dm(R)+Cm(\beta R).
\]
Since \(t-D=C+A(t)\), we obtain, without needing to divide by either
minimum,
\[
\begin{aligned}
m(R)
&\ge \frac{C}{C+A(t)}m(\beta R)\\
&\ge \exp\!\left(-\frac{A(t)}C\right)m(\beta R)\\
&\ge \exp\!\left(-\frac{2\eta(R)}{\alpha\beta}\right)m(\beta R).
\end{aligned}
\]
For the last line we used \(A(t)\le A(R)=R\eta(R)\), (5), and
\(t>\beta R\). This proves (4), including the case in which a minimum might
initially be zero.

Iterate (4) with \(R=\beta^j\). Continuity and \(q(0)=1\) imply
\(m(\beta^n)\to1\). If \(u\in(\beta^{k+1},\beta^k]\), then
\[
\sum_{j:\,u\le\beta^j}\beta^{-j}
=\sum_{j=0}^k\beta^{-j}
\le\frac{\beta^{-k}}{1-\beta}
\le\frac{1}{(1-\beta)u}.
\]
Tonelli's theorem and (1) therefore give
\[
\begin{aligned}
\sum_{j\ge0}\eta(\beta^j)
&=\int_0^1 a(u)
  \sum_{j:\,u\le\beta^j}\beta^{-j}\,du\\
&\le\frac{1}{1-\beta}\int_0^1\frac{a(u)}u\,du
\le\frac{2M}{\alpha}. \tag{6}
\end{aligned}
\]
Letting the number of iterations tend to infinity in (4), and then using
(6), yields
\[
m(1)\ge \exp\!\left(-\frac{4M}{\alpha^2\beta}\right).
\]
As \(q(1)\ge m(1)\), \(\alpha=e^{-M}\), and \(\beta\ge1/2\), this is
(2). \(\square\)

## Uniform consequence

Define
\[
C(M):=\exp(-3M-8Me^{2M}),
\qquad c(M):=\frac12C(M). \tag{7}
\]
In the compactness decomposition (C), the budget (B) gives
\[
e^{-h}\ge e^{-M}
\quad\text{and}\quad
q_a(1)\ge e^{-8Me^{2M}}.
\]
Moreover, for \(0\le x\le1/2\), \(\log(1-x)\ge-2x\). Hence
\[
V_*\ge\exp\!\left(-2\sum_{p\in S_*}\frac1p\right)\ge e^{-2M}.
\]
Every subsequential limit in (C) is consequently at least \(C(M)\).

It follows by contradiction and compactness that
\[
\liminf_{N\to\infty}
\inf_{S:\,\sum_{p\in S}1/p\le M}
\frac{A_S(N)}N
\ge C(M). \tag{8}
\]
Indeed, a sequence violating (8) would have a compactness subsequence whose
limit is smaller than \(C(M)\), contrary to the preceding paragraph.
Therefore there is an \(N_0(M)\) such that, for every \(N\ge N_0(M)\) and
every such \(S\),
\[
\frac{A_S(N)}N\ge
c(M)=\frac12\exp(-3M-8Me^{2M}). \tag{9}
\]

The constant in (9) is explicit, but the threshold \(N_0(M)\) obtained in
this way is **not effective**: the factorial-moment compactness lemma uses
subsequence extraction and a diagonal limiting argument and supplies no
quantitative rate. No effective value of \(N_0(M)\) is claimed here.
