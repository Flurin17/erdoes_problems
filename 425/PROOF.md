# Partial proof: an improved lower bound for Erdős Problem #425

## Status

This is a dependency-complete **partial result**, not a solution of the
constant problem.  It proves
\[
 \liminf_{n\to\infty}
 \frac{F(n)-\pi(n)}
      {n^{3/4}(\log n)^{-3/2}}
 \ge c_0,
 \qquad
 c_0=\frac{2^{11/4}}{3^{3/4}}=2.951151\ldots .
\]
It does not prove a matching upper bound, the existence of the limit, or the
fixed-\(r\) assertion.

All logarithms are natural.

## 1. Two graph lemmas

### Lemma 1 (semiprime replacement)

Let \(X,Y\) be disjoint prime sets, let \(G\subseteq X\times Y\) be
\(C_4\)-free, and suppose \(xy\le n\) for every \(xy\in E(G)\).  Then
\[
 A_G=\bigl(\{p\le n:p\text{ prime}\}\setminus(X\cup Y)\bigr)
       \cup\{xy:(x,y)\in E(G)\}
\]
has distinct products on its unordered pairs of distinct elements.

Proof.  Unique factorization makes the edge labels distinct.  In an equality
between products of two members of \(A_G\), the two sides contain the same
number of semiprime members, because their total numbers of prime factors
counted with multiplicity agree.  Prime-prime equalities are trivial.
A prime-semiprime equality decodes uniquely because the retained prime class
is disjoint from \(X\cup Y\). Finally, compare the multisets of \(X\)- and
\(Y\)-endpoints in two semiprime pairs. If either endpoint multiset is
repeated, those multisets already determine the unordered edge pair uniquely.
If both contain two distinct vertices, the only different pairing is the
other perfect matching, and the four edges form a \(C_4\).  ∎

### Lemma 2 (rectangular \(C_4\)-free graphs)

Suppose \(m=m(N)\le N\), \(m,N\to\infty\), and \(m/N\) is bounded below by a
positive constant.  There is a \(C_4\)-free bipartite graph with part sizes
\(m,N\) and
\[
 e=(1+o(1))m\sqrt N.
\]

Proof.  Choose the least prime \(q\ge\sqrt N\).  The prime number theorem
implies \(q=(1+o(1))\sqrt N\).  The point-line incidence graph of the
projective plane of order \(q\) is \(C_4\)-free, has
\(v=q^2+q+1=(1+o(1))N\) vertices on each side, and is \((q+1)\)-regular.
Choose uniformly an exact \(m\)-subset on one side and an exact \(N\)-subset
on the other.  The expected retained edge count is
\[
 v(q+1)\frac m v\frac N v=(1+o(1))m\sqrt N.
\]
Some restriction attains at least its expectation.  ∎

The only standard inputs are the prime number theorem and the elementary
finite-projective-plane construction over a prime field.

## 2. The interval architecture

Put
\[
 L_n=\frac{\sqrt n}{\log n}.
\]
Choose numbers
\[
 b_{-1}>b_0>b_1>\cdots>0,\qquad b_{-1}b_0=1.
\]
For a fixed integer \(J\ge0\), define disjoint prime intervals
\[
 X_j=\{p:b_{j+1}\sqrt n<p\le b_j\sqrt n\},
\]
\[
 Y_j=\{p:\sqrt n/b_{j-1}<p\le\sqrt n/b_j\}
 \qquad(0\le j\le J).
\]
Every \(x\in X_j\), \(y\in Y_j\) satisfies \(xy\le n\).  For fixed \(J\),
the prime number theorem gives
\[
 |X_j|=(2x_j+o(1))L_n,\qquad
 |Y_j|=(2y_j+o(1))L_n,
\]
where
\[
 x_j=b_j-b_{j+1},\qquad
 y_j=\frac1{b_j}-\frac1{b_{j-1}}.
\]
When \(x_j\le y_j\), Lemma 2 supplies a \(C_4\)-free component with
\[
 e_j=(2\sqrt2\,x_j\sqrt{y_j}+o(1))L_n^{3/2}.
\]
The components have disjoint vertex sets, so their union is \(C_4\)-free.
Lemma 1 then gives
\[
 |A|=\pi(n)+
 \left(2\sqrt2\sum_{j=0}^{J}x_j\sqrt{y_j}+o(1)\right)L_n^{3/2},
\]
because deleting the \(O_J(L_n)\) endpoint primes is lower order.

## 3. Exact optimization

Write
\[
 r_j=\frac{b_j}{b_{j-1}}\quad(j\ge0).
\]
Then
\[
 S:=\sum_{j\ge0}x_j\sqrt{y_j}
 =\sum_{j\ge0}\sqrt{b_j}(1-r_{j+1})\sqrt{1-r_j}.
\]

For \(r,s\in(0,1)\),
\[
 (1-s)\sqrt{1-r}+\sqrt{s(2-s)}\le\sqrt{2-r}.                 \tag{1}
\]
Indeed, with \(a=\sqrt{1-r}\) and \(u=1-s\), the left side is
\[
 au+\sqrt{1-u^2}\le\sqrt{a^2+1}
\]
by Cauchy--Schwarz.  Equality holds exactly when
\[
 1-s=\sqrt{\frac{1-r}{2-r}}.                                \tag{2}
\]

Multiplying (1), with \(r=r_j,s=r_{j+1}\), by \(\sqrt{b_j}\) and
telescoping gives
\[
 S\le\sqrt{b_0}\sqrt{2-r_0}.
\]
Since \(b_{-1}b_0=1\), \(r_0=b_0^2\), and hence
\[
 S^2\le b_0(2-b_0^2).
\]
The right side is maximized at \(b_0=\sqrt{2/3}\), giving
\[
 \sup S=\left(\frac{32}{27}\right)^{1/4}
       =\frac{2^{5/4}}{3^{3/4}}.                             \tag{3}
\]

Equality is achieved by
\[
 b_{-1}=\sqrt{\frac32},\qquad b_0=\sqrt{\frac23},
\]
and, writing \(\delta_j=1-r_j\), recursively taking
\[
 \delta_0=\frac13,\qquad
 \delta_{j+1}=\sqrt{\frac{\delta_j}{1+\delta_j}},\qquad
 b_{j+1}=(1-\delta_{j+1})b_j.                                \tag{4}
\]
The map \(f(t)=\sqrt{t/(1+t)}\) is increasing, and
\(f(t)>t\) exactly for \(0<t<(\sqrt5-1)/2\). Hence the sequence
\(\delta_j\) increases to the unique positive fixed point
\((\sqrt5-1)/2\). Consequently \(r_j\) tends to
\((3-\sqrt5)/2<1\), so \(b_j\to0\) geometrically and the terminal Bellman
potential vanishes.

It remains to check the orientation \(x_j\le y_j\).  Put
\[
 R_j=\frac{\delta_j}{\delta_{j+1}}
    =\sqrt{\delta_j(1+\delta_j)}.
\]
At \(j=0\), \(b_0^2=R_0=2/3\).  Since \(\delta_j\) increases, \(R_j\)
increases, while
\[
 b_{j+1}^2=b_j^2(1-\delta_{j+1})^2<R_j<R_{j+1}.
\]
Induction gives \(b_j^2\le R_j\), and therefore
\[
 \frac{x_j}{y_j}
 =\frac{b_j^2\delta_{j+1}}{\delta_j}\le1.
\]

## 4. Conclusion

For every \(\varepsilon>0\), choose \(J\) so the first \(J+1\) terms of
(3)--(4) are within \(\varepsilon/(2\sqrt2)\) of \(S\).  Keep this \(J\)
fixed and let \(n\to\infty\).  The construction in Section 2 then gives
\[
 F(n)\ge\pi(n)+
 \left(\frac{2^{11/4}}{3^{3/4}}-\varepsilon+o(1)\right)
 \frac{n^{3/4}}{(\log n)^{3/2}}.
\]
Since \(\varepsilon\) is arbitrary, the asserted liminf bound follows.

The architecture is optimized only among these disjoint interval-incidence
components.  A coupled two-level \(C_4\)-free packing could in principle do
better; no matching global upper bound is claimed.
