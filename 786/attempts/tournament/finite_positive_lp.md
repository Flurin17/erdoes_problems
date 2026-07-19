# Finite affine-hyperplane and circuit-LP route

This route asks whether the valuation vectors
\(v(n)=(v_p(n))_{p\leq N}\) have a nonzero affine hyperplane containing
\(N-o(N)\) of the points. It did not produce such a hyperplane or a
constant-density obstruction. It did, however, identify a rigorous and
fairly strong limitation of the most natural circuit-packing argument.

Throughout, a **bad relation** on a finite set \(S\subseteq[2,N]\) means a
nonzero rational vector \((c_n)_{n\in S}\) such that
\[
 \sum_{n\in S}c_n v(n)=0,
 \qquad
 \sum_{n\in S}c_n\ne0.                                      \tag{1}
\]
After clearing denominators this is an unequal-length product relation.
Let \(\mathcal H_N\) be the hypergraph whose edges are the inclusion-minimal
supports of bad relations. A deletion set meets every edge of
\(\mathcal H_N\) if and only if its complement lies on a level \(f=1\) of
some rational completely additive function. Thus the integral transversal
problem for \(\mathcal H_N\) is exactly the finite repetition-allowed
problem.

## An explicit sublinear fractional cover

### Theorem

Let \(\tau^*(\mathcal H_N)\) denote the usual fractional transversal number,
with one variable per integer and one constraint per *support* (not per
occurrence) of a minimal bad relation. Then
\[
 \tau^*(\mathcal H_N)
 =O\!\left(\frac{N\log\log\log N}{\log\log N}\right)=o(N).    \tag{2}
\]
Consequently every fractional packing of distinct bad-circuit supports with
vertex capacity one has total weight \(o(N)\).

### Proof

Put
\[
 L=\log N,\qquad \ell=\log L,\qquad
 Q=\lfloor\ell\rfloor,\qquad
 K=\left\lfloor\frac{\ell}{4\log\ell}\right\rfloor,
 \qquad M=K!Q^K                                             \tag{3}
\]
for sufficiently large \(N\). Define
\[
 z_n=\frac{\log(N/n)}{L},\qquad
 E=\{n\leq N:v_p(n)\geq Q\text{ for some prime }p\},        \tag{4}
\]
and give vertex \(n\) the fractional weight
\[
 y_n=\frac1K+Mz_n+\mathbf 1_E(n).                           \tag{5}
\]

First note a structural fact about a minimal edge \(S\), say \(|S|=k\).
The space of linear relations among \(\{v(n):n\in S\}\) is one-dimensional.
Indeed, take a relation \(c\) satisfying (1). If the relation space had
dimension at least two, it would contain a nonzero relation \(b\) with
\(\sum b_n=0\). Choosing an index where \(b_n\ne0\), a suitable rational
linear combination of \(c\) and \(b\) kills that coordinate while retaining
the nonzero coefficient sum of \(c\), contrary to support minimality.
Thus the valuation matrix on \(S\) has rank \(k-1\). Its primitive integral
kernel vector \(c\) is, up to a common gcd, the signed vector of maximal
minors of a full-rank \((k-1)\)-row submatrix.

We now verify the cover constraint. If \(k\geq K\), then
\(\sum_{n\in S}1/K\geq1\). Suppose \(k<K\), orient the primitive relation
so that
\[
 d:=\sum_{n\in S}c_n\geq1.
\]
Taking logarithms in (1) and using \(\log n=L(1-z_n)\) gives
\[
 \sum_{c_n>0}c_nz_n-
 \sum_{c_n<0}(-c_n)z_n=d.                                  \tag{6}
\]
In particular, \(\sum_{c_n>0}c_nz_n\geq1\). If
\(\max_n|c_n|\leq M\), it follows that
\[
 M\sum_{n\in S}z_n\geq1.                                  \tag{7}
\]

It remains to handle \(\max|c_n|>M\). If \(S\cap E=\varnothing\), every
entry of the full-rank minor matrix is at most \(Q-1\). Expansion of a
determinant gives
\[
 |\det|\leq(k-1)!(Q-1)^{k-1}<K!Q^K=M.                       \tag{8}
\]
But some signed maximal minor has magnitude at least
\(\max|c_n|>M\), because the minors are a positive integer multiple of the
primitive kernel vector. This contradiction shows that \(S\cap E\ne
\varnothing\). Equations (5), (7), and (8) prove
\(\sum_{n\in S}y_n\geq1\) for every edge.

Finally,
\[
 \sum_{n\leq N}z_n
 =\frac{N\log N-\log N!}{\log N}
 \leq\frac N{\log N},                                      \tag{9}
\]
where the last inequality follows by integrating \(\log x\). Also
\[
 |E|\leq N\sum_p p^{-Q}=O(N2^{-Q})=o(N).                    \tag{10}
\]
The choices in (3) give
\[
 \log M\leq K\log K+K\log Q\leq\frac12\ell
\]
for all large \(N\), hence \(M\leq\sqrt L\). Summing (5) and using
(9)--(10) yields
\[
 \sum_{n\leq N}y_n
 \leq \frac NK+\frac{MN}{L}+O(N2^{-Q})
 =O\!\left(\frac{N\log\ell}{\ell}\right),
\]
which is (2). Weak (or finite-dimensional strong) LP duality gives the
packing assertion. \(\square\)

This theorem does **not** construct a dense PLR set. Rather, it proves that
a linear deletion bound cannot be certified by the unweighted
support-incidence LP for bad circuits. Any constant-gap proof along this
route must exploit a genuinely integral/structural phenomenon, with an
unbounded integrality gap.

## A density-one set with no small-support bad circuit

The same proof gives a useful explicit near-construction. With the
parameters above, delete
\[
 D_N=E\cup
 \left\{n\leq N:z_n\geq\frac1{MK}\right\}.                \tag{11}
\]
Both parts have size \(o(N)\): the second is the initial interval ending at
\[
 N\exp\!\left(-\frac{L}{MK}\right)=o(N),                   \tag{12}
\]
because \(L/(MK)\to\infty\). If a bad circuit in
\([N]\setminus D_N\) had support size \(k<K\), the determinant argument
would give \(\max|c_n|\leq M\), while (6) would give
\(M\sum z_n\geq1\). On the other hand, (11) gives
\[
 M\sum_{n\in S}z_n<\frac{k}{K}<1,
\]
a contradiction. Therefore
\[
 |[N]\setminus D_N|=N-o(N)                                \tag{13}
\]
and this set contains no bad circuit supported on fewer than
\[
 K=(1+o(1))\frac{\log\log N}{4\log\log\log N}              \tag{14}
\]
distinct integers.

Thus every obstruction to turning (13) into a genuine density-one
hyperplane must use a growing number of distinct valuation vectors. This is
stronger than merely excluding bounded product lengths, because coefficient
multiplicities are unrestricted.

For comparison, a simpler size argument says that if
\[
 a_1\cdots a_r=b_1\cdots b_s,\qquad r>s,
 \qquad a_i,b_j\leq N,
\]
then some longer-side factor satisfies
\[
 a_i\leq N^{s/r}.                                          \tag{15}
\]
Otherwise the left side exceeds \(N^s\), while the right side is at most
\(N^s\). Hence \((N^{1-1/K},N]\) has no unequal-length relation with
longer length at most \(K\). Relation support alone is subtler: consecutive
powers can give a two-vertex bad circuit with coefficients of order
\(\log N\). The exceptional prime-power set \(E\) in (11) is what removes
that loophole for small supports.

## Exact rough-core reduction

The hyperplane equations also give a precise description of the only
remaining positive-construction regime. Let
\[
 A=\{n\leq N:f(n)=1\},\qquad m=N-|A|,
 \qquad y=\left\lfloor\frac{N}{m+1}\right\rfloor.           \tag{16}
\]
For every integer \(d\) with \(f(d)\ne0\), the chains
\(r,rd,rd^2,\ldots\), with \(d\nmid r\), meet \(A\) in at most one point.
Consequently
\[
 m\geq\left\lfloor\frac Nd\right\rfloor,
 \qquad\text{and hence}\qquad f(d)=0\quad(d\leq y).         \tag{17}
\]

Write uniquely
\[
 n=sr,qquad P^+(s)\leq y,qquad P^-(r)>y.
\]
Then \(f(n)=f(r)\), so the deficit has the exact fibre expansion
\[
 m=
 \sum_{\substack{r\leq N,\ P^-(r)>y\\ f(r)\ne1}}
 \Psi(N/r,y).                                               \tag{18}
\]
In particular \(m\geq\Psi(N,y)\). If
\[
 G=\{p>y:f(p)=1\},
\]
the mutually disjoint rough-core fibres \(r=1\), \(r=p\), and \(r=pq\)
give the two-layer ledger
\[
\begin{aligned}
 m\geq{}&\Psi(N,y)
 +\sum_{\substack{p>y\\p\notin G}}\Psi(N/p,y)\\
 &+\sum_{\substack{y<p\leq q,\ pq\leq N\\p,q\in G}}
       \Psi(N/(pq),y).                                      \tag{19}
\end{aligned}
\]
Thus making the singleton rough cores good automatically makes every
good--good pair core bad. When \(y\geq\sqrt N\), all nontrivial rough cores
are single primes, and (18) completely solves that range:
\[
 |A|\leq N-\Psi(N,y),                                      \tag{20}
\]
with equality obtained by giving every prime above \(y\) weight one. For
\(y=N^\alpha\), \(1/2\leq\alpha<1\), the limiting optimum is
\(-\log\alpha\), in particular \(\log2\) at \(\alpha=1/2\).

Any hypothetical density-one construction must therefore have
\(y=N^{o(1)}\) and solve the many-layer weighted rough-core problem left
open by (19).

## A cross-prime divisor-shadow inequality

Let \(S=\{p:f(p)\ne0\}\), and let \(Q_S(x)\) count squarefree integers at
most \(x\) all of whose prime factors lie in \(S\). For \(a\in A\), put
\(r(a)=\omega_S(a)\). Removing one copy of every prime in a subset
\(J\subseteq S\cap\operatorname{supp}(a)\) produces
\[
 a_J=\frac a{\prod_{p\in J}p},
 \qquad
 f(a_J)=1-\sum_{p\in J}f(p).                                \tag{21}
\]
Pair the subsets \(J\) by toggling any fixed active prime divisor of \(a\).
The two subset sums differ by a nonzero number, so at most one member of
each pair can have sum zero. At least \(2^{r(a)-1}\) of the distinct
descendants (21) consequently lie outside \(A\). Double counting the
pairs \((a,J)\) gives
\[
 \boxed{
 \sum_{a\in A}2^{\omega_S(a)-1}
 \leq
 \sum_{b\notin A}Q_S(N/b).}                                \tag{22}
\]

This is a genuine cross-prime constraint, unlike a sum of independent
\(p\)-chain bounds. Its present obstruction is again concentration on
small anchors: a small omitted \(b\) can support very many squarefree active
multipliers. A weighted expansion theorem that prevents this concentration
would be a plausible repair lemma.

## Outcome and bottleneck

The affine formulation leaves two logically possible outcomes:

1. construct a rational hyperplane whose exact nonzero atom solves the
   many-layer rough-core recursion in (18); or
2. prove an integral expansion/anti-concentration theorem that upgrades
   (19) or (22) to \(m\gg N\).

The new LP theorem rules out a broad shortcut to the second outcome:
bounded-congestion packings of bad-circuit supports have total \(o(N)\), and
there is an explicit density-one set avoiding every bad circuit of support
up to (14). The first unresolved obstructions are necessarily long,
cross-prime, and cannot be detected by fixed multiplication grids,
semiprime rectangles, or bounded-support affine dependence.
