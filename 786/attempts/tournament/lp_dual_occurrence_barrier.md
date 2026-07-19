# Fractional circuit-packing barriers

Fix \(N\), and orient every unequal-length product identity as
\[
   a_1\cdots a_r=b_1\cdots b_s,\qquad r>s.
\]
Repetitions are allowed.  Define its long-side occurrence vector by
\[
   m_C^+(n)=\#\{i:a_i=n\}.
\]

## Proposition (universal fractional-cover barrier)

Suppose nonnegative circuit weights \(\lambda_C\) obey
\[
   \sum_C m_C^+(n)\lambda_C\le 1
   \qquad (1\le n\le N).
\]
Then
\[
   \sum_C\lambda_C
   \le {N\log N-\log(N!)\over\log N}
   ={N\over\log N}+O(1).
\]
In particular, no occurrence-capacity fractional packing has total
weight \(\Omega(N)\).

### Proof

Put
\[
   z_n={\log(N/n)\over\log N}\ge0.
\]
The product equality gives
\[
 \sum_{i=1}^r z_{a_i}-\sum_{j=1}^s z_{b_j}
 =r-s.
\]
Consequently \(\sum_i z_{a_i}\ge r-s\ge1\).  Therefore
\[
\begin{aligned}
 \sum_C\lambda_C
 &\le \sum_C\lambda_C\sum_i z_{a_i}\\
 &=\sum_{n\le N}z_n\sum_Cm_C^+(n)\lambda_C\\
 &\le\sum_{n\le N}z_n
 ={N\log N-\log(N!)\over\log N}.
\end{aligned}
\]
Stirling's formula gives the stated asymptotic.  \(\square\)

The same proof applies to ordinary binary vertex incidence whenever the
factors on the long side are internally distinct.  It therefore also
rules out a linear bounded-congestion packing for the distinct-factor
reading of the problem.

## Elementary length-splitting version

If long-side factors are distinct (or capacity counts their
occurrences), split circuits at a parameter \(R\).  For a circuit with
\(r\le R\), one long-side factor is at most
\[
   N^{s/r}\le N^{1-1/r}\le N^{1-1/R}.
\]
Thus the total weight of these circuits is at most
\(N^{1-1/R}\).  Circuits with \(r>R\) consume more than \(R\)
long-side slots, so their total weight is at most \(N/R\).  Hence
\[
   T\le N^{1-1/R}+{N\over R}=o(N)
\]
for any \(R\to\infty\) with \(R=o(\log N)\), for example
\(R=\sqrt{\log N}\).

## Deduplicated support: a determinant repair

For repetition-allowed identities, a hitting-set LP would normally
deduplicate repeated occurrences of one integer.  The preceding
\(z_n\) alone is not a cover for that stronger support hypergraph.  For
example, take \(N=2^r\).  The identity
\[
   (2^{r-1})^r=(2^r)^{r-1}
\]
has unequal lengths but support \(\{2^{r-1},2^r\}\), whose total
log-deficiency weight is only \(1/r\).

Coefficient-heavy relations can, however, be covered by the sparse set of
integers having a high prime-power divisor.  This gives a universal
\(o(N)\)-weight cover even for binary support incidence.

### Theorem (support-incidence fractional cover)

Let \(\mathcal H_N\) be the hypergraph on \([1,N]\) whose edges are the
distinct supports of unequal-length product identities, with arbitrary
repetitions allowed.  Then
\[
   \tau^*(\mathcal H_N)=o(N).
\]
Consequently every fractional packing satisfying
\[
   \sum_{C\ni n}\lambda_C\le C_0
\]
for every integer \(n\), where \(C_0=O(1)\), has total weight \(o(N)\).

### Proof

Write \(v(n)=(v_p(n))_p\).  For all sufficiently large \(N\), set
\[
 K=\left\lfloor\sqrt{\log\log N}\right\rfloor,
 \qquad M=\sqrt{\log N},
 \qquad
 Q=\left\lfloor\left({M\over K!}\right)^{1/K}\right\rfloor.
\]
Here \(K\ge2\), and
\[
 \log Q={1\over2}\sqrt{\log\log N}
         -{1\over2}\log\log\log N+O(1),
\]
so \(Q\to\infty\).  Let
\[
 E_Q=\{n\le N:v_p(n)\ge Q\text{ for some prime }p\}
\]
and define
\[
 y_n={1\over K}+M{\log(N/n)\over\log N}+\mathbf1_{E_Q}(n).
 \tag{1}
\]
We prove that \(y\) covers every edge.

It is enough to cover support-minimal bad relations.  Indeed, starting
from any integer vector \(c\), supported on an edge, with
\[
  \sum_n c_n v(n)=0,
  \qquad d:=\sum_n c_n\ne0,
  \tag{2}
\]
one may choose a relation of minimal support inside it.  Let that support
be \(S\), put \(k=|S|\), and take \(c\) primitive.

The kernel of the valuation matrix \(V_S\) is one-dimensional.  To see
this, if it had dimension at least two, it would contain a nonzero
vector \(b\) with \(\sum b_n=0\).  Choosing \(i\) with \(b_i\ne0\), the
vector
\[
  c-{c_i\over b_i}b
\]
would still satisfy (2), with the same nonzero coordinate sum, but would
have smaller support.  After clearing denominators this contradicts
minimality.  Hence \(\operatorname{rank}V_S=k-1\).

There are three cases.

1. If \(k\ge K\), the first term of (1) gives
   \(\sum_{n\in S}y_n\ge k/K\ge1\).

2. Suppose \(k<K\) and \(H:=\max_n|c_n|\le M\).  With
   \(z_n=\log(N/n)/\log N\), (2) gives
   \[
      \sum_{n\in S}c_nz_n=d.
   \]
   Since \(d\) is a nonzero integer and \(z_n\ge0\),
   \[
      1\le |d|
      \le H\sum_{n\in S}z_n
      \le M\sum_{n\in S}z_n.
   \]
   Thus the middle term of (1) covers \(S\).

3. Suppose \(k<K\) and \(H>M\).  Choose \(k-1\) independent rows of
   \(V_S\), obtaining an integer \((k-1)\)-by-\(k\) matrix \(B\).
   Its signed maximal minors form a kernel vector, so the primitive
   vector \(c\) is that cofactor vector divided by the gcd of its
   coordinates.  In particular, some maximal minor has absolute value
   greater than \(M\).  If \(S\cap E_Q\) were empty, every entry of
   \(B\) would be at most \(Q-1\), and every such minor would instead
   be bounded by
   \[
      (k-1)!(Q-1)^{k-1}
      \le K!Q^K\le M,
   \]
   a contradiction.  Hence \(S\) contains an element of \(E_Q\), and
   the last term of (1) covers it.

Finally, the total weight in (1) is small.  Stirling's formula gives
\[
 \sum_{n\le N}z_n={N\over\log N}+O(1),
\]
while the union bound gives
\[
 |E_Q|
 \le N\sum_p p^{-Q}
 \le N\sum_{m=2}^{\infty}m^{-Q}
 =o(N).
\]
Therefore
\[
 \sum_{n\le N}y_n
 \le {N\over K}+{MN\over\log N}+O(M)+o(N)
 =o(N).
\]
This proves the fractional-cover statement, and LP weak duality proves
the packing statement.  \(\square\)

This theorem is only a barrier to a particular lower-bound method.  A
fractional cover need not round to an integral cover at comparable cost;
indeed that integrality gap is precisely where the finite PLR problem can
still live.
