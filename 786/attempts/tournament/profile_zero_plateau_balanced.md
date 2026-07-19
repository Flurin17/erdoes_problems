# A zero-modal plateau forces a linear zero fibre

## Outcome

This note closes the zero-modal plateau under a **uniform** dyadic-prefix
hypothesis.  Let \(f:\mathbb N\to\mathbb Q\) be completely additive (the
argument only uses that its zero-valued primes generate zero-valued
integers).  Put

\[
 D_0(x)=|\{n\le x:f(n)\ne0\}|.
\]

Let \(Y=\sqrt N\), let \(X=2^J\) be the largest power of two not exceeding
\(Y\), and set

\[
 \delta=\max_{0\le j\le J}\frac{D_0(2^j)}{2^j}.
 \tag{1}
\]

If \(\delta\le1/16\), then, as \(N\to\infty\),

\[
 \#\{n\le N:P^+(n)\le Y,\ f(n)=0\}
 \ge (1-\log 2-O(\delta)-o(1))N.
 \tag{2}
\]

In particular, if \(f=0\) on \((1-o(1))\) of **every** dyadic prefix up
to \(\sqrt N\), uniformly over those prefixes, then a positive proportion
(indeed \(1-\log2-o(1)\)) of all integers up to \(N\) are
\(\sqrt N\)-smooth and have value zero.

The proof uses a canonical incidence rather than a canonical balanced
factorization.  An active prime is paired with every zero-valued cofactor.
The first moment of these pairs is controlled from below by (1), while the
second moment of their collision multiplicity is exactly bounded by the
first two powers of the reciprocal mass of active primes.

## 1. The reciprocal mass lemma

Call a prime \(p\) **active** if \(f(p)\ne0\), and put

\[
 \mathcal A=\{p\le X/2:p\text{ is active}\},
 \qquad
 \lambda=\sum_{p\in\mathcal A}\frac1p.
 \tag{3}
\]

### Lemma 1

If \(0\le\delta\le1/16\), then

\[
 \lambda\le 8\delta.
 \tag{4}
\]

#### Proof

For \(p\in\mathcal A\), set \(y_p=\lfloor X/p\rfloor\).  Thus
\(2\le y_p\le X/2\).  Let \(C_p\) be the least power of two at least
\(y_p\).  Then \(C_p\le X\) and \(C_p<2y_p\).  Since deficiency is
monotone in the endpoint, (1) gives

\[
 D_0(y_p)\le D_0(C_p)\le\delta C_p<2\delta y_p.
\]

Consequently

\[
 |\{k\le y_p:f(k)=0\}|\ge(1-2\delta)y_p.
 \tag{5}
\]

Count incidences

\[
 \mathcal I=\{(p,k):p\in\mathcal A, k\le X/p, f(k)=0\},
 \qquad T=|\mathcal I|.
\]

Because \(y_p\ge X/(2p)\), (5) yields

\[
 T\ge \frac{1-2\delta}{2}X\lambda.
 \tag{6}
\]

The product \(n=pk\) attached to an incidence satisfies \(n\le X\) and

\[
 f(n)=f(p)+f(k)=f(p)\ne0.
\]

For \(n\le X\), let

\[
 S(n)=|\{p\in\mathcal A:p\mid n\}|.
\]

The multiplicity of the product map \((p,k)\mapsto pk\) is at most
\(S(n)\).  Hence Cauchy--Schwarz and (1) at \(X\) give

\[
 T^2
 \le \left(\sum_{\substack{n\le X\\f(n)\ne0}}S(n)\right)^2
 \le D_0(X)\sum_{n\le X}S(n)^2
 \le\delta X\sum_{n\le X}S(n)^2.
 \tag{7}
\]

The collision moment has the elementary exact expansion

\[
 \begin{aligned}
 \sum_{n\le X}S(n)^2
 &=\sum_{p\in\mathcal A}\left\lfloor\frac Xp\right\rfloor
   +2\sum_{\substack{p<q\\p,q\in\mathcal A}}
       \left\lfloor\frac X{pq}\right\rfloor\\
 &\le X\lambda+2X\sum_{p<q}\frac1{pq}
 \le X(\lambda+\lambda^2).
 \end{aligned}
 \tag{8}
\]

Combining (6)--(8), and cancelling \(X^2\), gives

\[
 \frac{(1-2\delta)^2}{4}\lambda^2
 \le\delta(\lambda+\lambda^2).
 \tag{9}
\]

If \(\lambda=0\) there is nothing to prove.  Otherwise, for
\(\delta\le1/16\),

\[
 \lambda
 \le
 \frac{\delta}{(1-2\delta)^2/4-\delta}
 \le 8\delta,
\]

which proves (4).  \(\square\)

This is the desired bounded-marginal statement.  It is uniform in the
locations and rational values of the active primes, and permits arbitrary
cancellation among those values.

## 2. From active-prime mass to zero-valued smooth numbers

The primes in the omitted terminal range \((X/2,Y]\) have reciprocal mass

\[
 \sum_{X/2<p\le Y}\frac1p=O\!\left(\frac1{\log X}\right),
 \tag{10}
\]

because \(Y<2X\), and a standard Chebyshev upper bound gives
\(\pi(2X)=O(X/\log X)\).  Lemma 1 therefore implies

\[
 \Lambda_Y:=\sum_{\substack{p\le Y\\f(p)\ne0}}\frac1p
 =O(\delta)+O\!\left(\frac1{\log N}\right).
 \tag{11}
\]

By the union bound, the number of integers \(n\le N\) divisible by at
least one active prime at most \(Y\) is at most

\[
 \sum_{\substack{p\le Y\\f(p)\ne0}}
 \left\lfloor\frac Np\right\rfloor
 \le N\Lambda_Y.
 \tag{12}
\]

If \(P^+(n)\le Y\) and no active prime divides \(n\), complete additivity
gives \(f(n)=0\).  Thus (12) shows that all but
\(O(\delta N)+o(N)\) of the \(Y\)-smooth integers up to \(N\) have value
zero.

For completeness, the prime number theorem and partial summation give

\[
 \sum_{Y<p\le N}\frac1p=\log2+o(1).
 \tag{13}
\]

An integer at most \(N\) has at most one prime divisor greater than
\(Y=\sqrt N\).  Therefore the number of non-\(Y\)-smooth integers is

\[
 \sum_{Y<p\le N}\left\lfloor\frac Np\right\rfloor
 =N\log2+o(N),
 \tag{14}
\]

where the total floor error is \(O(\pi(N))=o(N)\).  Equations
(11)--(14) prove (2).

## 3. Exact scope and remaining interface

The word "every" in the plateau hypothesis must be uniform.  The proof
uses

\[
 \max_{2^j\le X}D_0(2^j)/2^j=o(1),
\]

not merely convergence at each fixed dyadic prefix.  A profile statement
which controls the zero deficiency on only a harmonic majority of moving
scales does not immediately imply this maximum bound.  The remaining
interface in the largest-prime induction is therefore to upgrade its
weighted-average profile control to uniform small deficiency on a long
enough initial dyadic segment, or to run the incidence proof on a suitably
selected collection of scales.

This distinction is necessary.  Let \(X=2^J\asymp\sqrt N\), put

\[
 j_0=\left\lfloor\frac{J}{(\log J)^2}\right\rfloor,
 \qquad Q=2^{j_0},
\]

and define a completely additive function by

\[
 f_N(p)=
 \begin{cases}
 1,&Q<p\le\sqrt N,\\
 0,&\text{otherwise}
 \end{cases}
 \tag{15}
\]

on primes.  Every prefix \(2^j\) with \(j\le j_0\) is identically zero,
and

\[
 \frac{\sum_{j\le j_0}1/j}{\sum_{j\le J}1/j}=1-o(1).
 \tag{16}
\]

Thus a harmonic \(1-o(1)\) proportion of the dyadic scales is perfect.
Nevertheless, among the \(\sqrt N\)-smooth integers, \(f_N(n)=0\) if and
only if \(n\) is \(Q\)-smooth.  There are only \(o(N)\) such integers.
Indeed, Rankin's elementary bound, with
\(\sigma=1-1/(2\log Q)\), gives

\[
 \begin{aligned}
 \Psi(N,Q)
 &\le N^\sigma\prod_{p\le Q}(1-p^{-\sigma})^{-1}\\
 &\le N\exp\!\left(-\frac{\log N}{2\log Q}
                    +O(\log\log Q)\right)=o(N),
 \end{aligned}
 \tag{17}
\]

because \(\log N/\log Q\asymp(\log J)^2\).  In the second line we used
\(p^{1/(2\log Q)}\le e^{1/2}\) and the standard upper bound
\(\sum_{p\le Q}1/p=O(\log\log Q)\).  This example also defeats merely
pointwise control at every fixed dyadic scale.  The moving bad tail may
carry all of the active-prime mass.
