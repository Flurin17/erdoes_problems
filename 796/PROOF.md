# Erdős Problem #796: a compatible-profile formula for the constant

## Theorem

Let
\[
r_A(m)=\#\{\{a,b\}\subseteq A:a<b,\ ab=m\}.
\]
There is a finite real constant \(c\) such that
\[
g_3(n)=\frac{n\log\log n}{\log n}
       +(c+o(1))\frac n{\log n}.
\]
More precisely, let
\[
\mu_{U,V}(t)=\#\{(u,v)\in U\times V:uv=t\}
\]
for finite sets of positive integers.  Say \(U\sim V\) if
\(\mu_{U,V}(t)\leq2\) for every \(t\).  For \(K\geq1\), define
\[
M_K=\max\left\{
 \sum_{k=1}^K\frac{|D_k|}{k(k+1)}:
 D_k\subseteq[1,k],\ D_i\sim D_j\ (1\leq i,j\leq K)
\right\}
\]
and
\[
P_K=\sum_{k=1}^K\frac{\pi(k)}{k(k+1)}.
\]
Then the finite limit
\[
C_*=\lim_{K\to\infty}(M_K-P_K)
\]
exists, and
\[
\boxed{c=B_1+C_*},
\]
where
\[
B_1=\lim_{x\to\infty}
\left(\sum_{p\leq x}\frac1p-\log\log x\right)
\]
is the prime Mertens constant.

This is an exact variational identification of the constant by finite
combinatorial problems.  An explicit compatible profile below gives
\[
C_*\geq\frac{79}{60}.
\]

## Standard analytic inputs

We use the following standard results.

1. The quantitative prime number theorem, in particular
   \[
   \pi(x)=\operatorname{Li}(x)+O(xe^{-c\sqrt{\log x}})
   \]
   for some \(c>0\), together with prime Mertens and Chebyshev's upper
   bound \(\pi(x)\ll x/\log x\).
2. The weak form of the multiplication-table theorem: there is an absolute
   \(\eta>0\) such that
   \[
   \mathcal M(x):=\#\{ab:1\leq a,b\leq x\}
       \ll \frac{x^2}{(\log x)^\eta}.                 \tag{MT}
   \]
   Only this logarithmic saving is used; no sharp multiplication-table
   asymptotic is needed.

Everything else is proved below.

## 1. The smooth part is negligible

Write \(P^+(a)\) for the largest prime factor of \(a\), with \(P^+(1)=1\).

**Lemma 1.**  If \(A\subseteq[1,n]\) and \(r_A(m)\leq2\) for every \(m\),
then
\[
\#\{a\in A:P^+(a)\leq\sqrt n\}
 \ll \frac{n(\log\log n)^2}{\log^2n}
 =o(n/\log n).                                        \tag{1.1}
\]

**Proof.**  Put \(y=\sqrt n\), \(L=\log n\), and \(T=L^{24}\); bounded
\(n\) may be absorbed into the constant.  We first prove a factorization
trichotomy.  Every integer \(a\) is in at least one of the following classes:

\[
\begin{array}{ll}
\mathrm{G}:&a=xyz\quad\text{with }x,y,z\geq T,\\
\mathrm{E}_0:&a<T^5,\\
\mathrm{E}_1:&a=ps,\quad p\text{ prime},\ s<T^3,\\
\mathrm{E}_2:&a=pqs,\quad p,q\text{ prime (possibly equal)},\ s<T.
\end{array}                                             \tag{1.2}
\]

To see this, list the prime factors of \(a\), with multiplicity, as
\(p_1\geq p_2\geq\cdots\).  If \(p_2\geq T\), then either
\(a/(p_1p_2)\geq T\), giving G, or \(a\) is in \(\mathrm E_2\).
If \(p_1\geq T>p_2\), put \(R=a/p_1\).  If \(R<T^3\), use
\(\mathrm E_1\).  Otherwise greedily multiply the remaining prime factors
until their product \(u\) first reaches \(T\).  Then \(u<T^2\) and
\(R/u>T\), giving G.  Finally, if \(p_1<T\) and \(a\geq T^5\), greedily
form two products in \([T,T^2)\); their complementary factor exceeds \(T\).
The remaining case is \(\mathrm E_0\).

We count the exceptional \(y\)-smooth integers.  Classes \(\mathrm E_0\)
and \(\mathrm E_1\) contribute at most
\[
T^5+T^3\pi(y)=o(n/L).
\]
For fixed \(s<T\), the number of ordered pairs of primes \(p,q\leq y\)
with \(spq\leq n\) is
\[
\begin{aligned}
Q(s)
&\leq \pi(y/s)\pi(y)
 +\sum_{y/s<p\leq y}\pi(n/(sp))\\
&\ll \frac{n}{sL^2}
 +\frac{n}{sL}\sum_{y/s<p\leq y}\frac1p\\
&\ll \frac{n(1+\log s)}{sL^2}.                           \tag{1.3}
\end{aligned}
\]
The last estimate follows either from prime Mertens or by splitting the
interval into \(O(1+\log s)\) dyadic intervals and applying Chebyshev.
Summing (1.3) over \(s<T\) gives
\[
\#\mathrm E_2\ll n(\log T)^2/L^2
 \ll n(\log\log n)^2/L^2.                               \tag{1.4}
\]

It remains to count the good elements of \(A\).  Choose one ordered
factorization \(a=x(a)y(a)z(a)\), with all three factors at least \(T\),
for every good \(a\).  Make a 3-partite 3-uniform hypergraph whose edge
is the chosen triple.  The product map on its edges is injective, because
one triple was chosen for each element of the set \(A\).

This hypergraph is \(K_{2,2,2}^{(3)}\)-free.  Indeed, the eight corners of
a \(2\times2\times2\) box give eight distinct elements of \(A\).  Its four
antipodal pairs all have product
\[
x_1x_2y_1y_2z_1z_2,
\]
contrary to \(r_A\leq2\).

We use the following elementary extremal estimate.  If a
\(K_{2,2,2}^{(3)}\)-free 3-partite hypergraph has part sizes \(u,v,w\) and
\(e\) edges, then
\[
e\ll uv+wuv^{3/4}+wu^{1/2}v.                             \tag{1.5}
\]
For each vertex \(z\) in the third part, let \(G_z\) be its bipartite
link on the first two parts.  For \(z\ne z'\), the intersection
\(G_z\cap G_{z'}\) is \(C_4\)-free, so it has at most \(u\sqrt v+v\)
edges.  If \(d_{xy}\) is the number of links containing \(xy\), then
\[
\sum_{xy}\binom{d_{xy}}2
\leq\binom w2(u\sqrt v+v),
\]
whereas Cauchy gives
\[
\sum_{xy}\binom{d_{xy}}2\geq \frac{e^2}{2uv}-\frac e2.
\]
Solving this quadratic proves (1.5).

Place \(x,y,z\) in dyadic intervals with lower endpoints \(X,Y,Z\).
For a nonempty box, \(XYZ\leq n\) and \(X,Y,Z\geq T/2\).  Estimate (1.5)
gives
\[
e_{\rm box}\ll
XY+ZXY^{3/4}+ZX^{1/2}Y
\ll \frac nT+\frac n{T^{1/4}}+\frac n{T^{1/2}}
\ll \frac n{T^{1/4}}.
\]
There are \(O(L^3)\) boxes, so the good elements number
\[
O(nL^3/T^{1/4})=O(n/L^3).
\]
Together with (1.3)--(1.4), this proves (1.1). ∎

## 2. Large-prime fibers

Put \(y=\sqrt n\) and
\[
A_0=\{a\in A:P^+(a)\leq y\}.
\]
Every \(a\in A\setminus A_0\) has a unique prime divisor \(p>y\), since
the product of two such primes exceeds \(n\).  Define
\[
B_p=\{d:pd\in A\},\qquad y<p\leq n.
\]
Then \(B_p\subseteq[1,\lfloor n/p\rfloor]\), and
\[
|A|=|A_0|+\sum_{p>y}|B_p|.                               \tag{2.1}
\]

**Lemma 2.**  If \(p\ne q\) are primes exceeding \(y\), then
\[
\mu_{B_p,B_q}(t)=r_A(pqt)\leq2                            \tag{2.2}
\]
for every \(t\).

**Proof.**  A coefficient in \(B_p\) is smaller than \(y\), so it has no
prime divisor exceeding \(y\).  The large-prime multiset of a product of
two elements of \([1,n]\) therefore determines the two fiber labels.
For labels \(p,q\), assigning the coefficient \(d\) to \(p\) and \(e\)
to \(q\) is ordered, and gives the pair \(\{pd,qe\}\).  This
correspondence is injective.  If \(t\) contains either \(p\) or \(q\), or a third prime
larger than \(y\), both sides are zero because a product of two integers
at most \(n\) cannot contain three such large prime factors, counted with
multiplicity. ∎

## 3. Repairing all fibers at negligible cost

Call a **witness** in a finite set \(B\) two distinct unordered multisets
\(\{a,b\}\ne\{c,d\}\), with entries in \(B\), such that \(ab=cd\).
Diagonal multisets are allowed.  A set has no witness exactly when
\(\mu_{B,B}(t)\leq2\) for every \(t\).

**Lemma 3 (witness hitting).**  Suppose \(B_i\subseteq[1,N]\) and
\(B_i\sim B_j\) whenever \(i\ne j\).  There are \(C_i\subseteq B_i\)
such that \(C_i\sim C_i\) for every \(i\), all cross compatibilities remain
valid, and
\[
\sum_i|B_i\setminus C_i|\leq
N^2\left(1+2\sum_{m\leq N}\frac1m\right)
\ll N^2\log N.                                          \tag{3.1}
\]

**Proof.**  One witness cannot occur in two different \(B_i,B_j\).  If
both factorizations are off diagonal, it contributes four ordered pairs
to \(\mu_{B_i,B_j}\); if one is diagonal, it contributes three.  Two
distinct diagonal factorizations of a positive integer are impossible.
Thus the witness families of the \(B_i\) are disjoint.

For every witness in \(B_i\), select one of its entries and delete the
union of all selected entries.  Every witness is destroyed, and the
number of deletions is at most the number of witnesses.  It remains to
bound the number of ambient witnesses, which is at most the number of
ordered solutions of \(ab=cd\) with \(a,b,c,d\leq N\).

Write \(a=gr,c=gs\), where \((r,s)=1\).  Then \(b=sh,d=rh\), and
\[
g,h\leq \frac N{\max(r,s)}.
\]
Consequently the number of ordered solutions is at most
\[
\sum_{\substack{r,s\leq N\\(r,s)=1}}
\left\lfloor\frac N{\max(r,s)}\right\rfloor^2
\leq N^2\left(1+2\sum_{m\leq N}\frac1m\right).
\]
Deleting elements preserves every cross inequality. ∎

We apply Lemma 3 dyadically to the fibers \(B_p\).  Put
\[
k_p=\lfloor n/p\rfloor
\]
and group the primes for which \(K\leq k_p<2K\), with \(K\) dyadic.
Since every such fiber lies in \([1,2K]\), Lemma 3 repairs the whole block
at cost \(O(K^2(1+\log K))\).

For large \(K\) it is cheaper to delete the whole block.  Each \(B_p\) is
itself admissible in \([1,2K]\): three strict coefficient pairs of one
product would lift to three strict pairs in \(A\).  Hence
\[
\binom{|B_p|}{2}\leq2\mathcal M(2K),
\]
and (MT) gives, with \(a=\eta/2>0\),
\[
|B_p|\ll \frac K{(\log K)^a}.                             \tag{3.2}
\]
Chebyshev gives
\[
\#\{p:K\leq k_p<2K\}\ll\frac n{KL},
\]
so the whole block has size
\[
\ll\frac n{L(\log K)^a}.                                 \tag{3.3}
\]

Choose \(K_0=y/L^2\).  The total repair cost over dyadic \(K\leq K_0\)
is
\[
\ll K_0^2\log K_0\ll n/L^3.
\]
There are only \(O(\log L)\) dyadic blocks between \(K_0\) and \(y\);
there \(\log K\asymp L\), so (3.3) shows that deleting all of them costs
\[
O\left(\frac{n\log L}{L^{1+a}}\right)=o(n/L).
\]
We have proved:

**Corollary 4.**  By deleting \(o(n/\log n)\) elements in total from the
fibers \(B_p\), one obtains \(C_p\subseteq B_p\) such that
\[
C_p\sim C_q\quad\text{for all }p,q>y,                    \tag{3.4}
\]
including \(p=q\).

For each integer \(k\geq1\), let
\[
h_k(n)=\#\{y<p\leq n:p\text{ prime},\ \lfloor n/p\rfloor=k\}.
\]
Among the repaired fibers with capacity \(k\), choose one of maximum size
and call it \(D_k\); if \(h_k=0\), choose \(D_k=\varnothing\).  Then
\[
D_k\subseteq[1,k],\qquad D_i\sim D_j\quad\text{for all }i,j,
\]
and
\[
\sum_{p>y}|B_p|
\leq \sum_k h_k(n)|D_k|+o(n/L).                          \tag{3.5}
\]
Indeed, the chosen \(D_k\)'s are original repaired fibers, so distinct
ones are cross compatible; copying one within its stratum is valid because
it is self compatible.

## 4. The profile constant exists

We first need a uniform bound on a self-compatible set.

**Lemma 5.**  If \(D\subseteq[1,N]\) and \(D\sim D\), then
\[
|D|\leq\pi(N)+N^{5/6}+\frac32N^{2/3}.                    \tag{4.1}
\]

**Proof.**  The condition \(D\sim D\) says that the product map on
unordered two-multisets from \(D\) is injective.

We use the elementary graph fact that a \(C_4\)-free bipartite graph with
parts of sizes \(x,y\) has at most
\[
y+x\sqrt y                                                  \tag{4.2}
\]
edges.  Indeed, counting pairs of neighbors on the \(x\)-side gives
\(\sum_{v\in Y}\binom{d(v)}2\leq\binom x2\), and Cauchy solves the
resulting quadratic.

Let \(D_>\) consist of elements having a prime divisor \(p>N^{2/3}\).
It is unique, and each such element is \(mp\) with \(m\leq N^{1/3}\).
The bipartite graph of selected pairs \((m,p)\) is \(C_4\)-free, since a
rectangle would give
\[
(m_1p_1)(m_2p_2)=(m_1p_2)(m_2p_1).
\]
If \(d(p)\) is its degree, then
\[
\sum_p\binom{d(p)}2\leq\binom{\lfloor N^{1/3}\rfloor}2.
\]
Since \(d\leq1+\binom d2\) for \(d\geq1\),
\[
|D_>|\leq\pi(N)+\tfrac12N^{2/3}.                         \tag{4.3}
\]

For every remaining \(a\), choose a factorization \(a=uv\) with
\[
u\leq N^{1/2},\qquad v\leq N^{2/3}.                      \tag{4.4}
\]
If \(a\leq N^{2/3}\), use \(1\cdot a\).  Otherwise put
\(T=a/N^{2/3}\), multiply prime factors until the product \(s\) first
reaches \(T\), and let \(q\) be the last prime used.  If
\(s\leq N^{2/3}\), both \(s\) and \(a/s\) are at most \(N^{2/3}\).
If \(s>N^{2/3}\), then
\[
q>N^{2/3}/T=N^{4/3}/a\geq a/N^{2/3}=T,
\]
so \(q,a/q\leq N^{2/3}\).  Orient the two factors increasingly to obtain
(4.4).

Choose one pair per element.  The resulting bipartite graph on parts of
sizes \(N^{1/2}\) and \(N^{2/3}\) is \(C_4\)-free for the same rectangle
reason.  By (4.2), it has at most \(N^{2/3}+N^{5/6}\) edges.  Combine
this with (4.3). ∎

We now prove convergence of the constant in the theorem.  Put
\[
R_K=M_K-P_K.
\]
For \(J>K\), restrict an optimal \(J\)-profile to its first \(K\)
coordinates.  Lemma 5 bounds every tail coordinate, so
\[
R_J\leq R_K+E_K,\qquad
E_K:=\sum_{j>K}
\frac{j^{5/6}+\frac32j^{2/3}}{j(j+1)}
\leq6K^{-1/6}+\frac92K^{-1/3}.                           \tag{4.5}
\]

Conversely, extend any optimal \(K\)-profile by
\[
E_j=\{1\}\cup\{p:K<p\leq j,\ p\text{ prime}\},\qquad j>K.
\]
The new coordinates are mutually compatible.  They are also compatible
with every old coordinate: an equality between an old factor at most \(K\)
and two distinct new primes would force a prime greater than \(K\) to
divide the old factor.  Therefore
\[
R_J\geq R_K+(1-\pi(K))
\left(\frac1{K+1}-\frac1{J+1}\right).                    \tag{4.6}
\]
Equations (4.5)--(4.6), together with
\(\pi(K)/K\to0\), show that \(R_K\) is Cauchy.  Thus \(C_*=\lim R_K\)
exists and is finite.

Finally,
\[
\begin{aligned}
P_K
&=\sum_{p\leq K}\sum_{j=p}^K\frac1{j(j+1)}\\
&=\sum_{p\leq K}\frac1p-\frac{\pi(K)}{K+1}
 =\log\log K+B_1+o(1).                                  \tag{4.7}
\end{aligned}
\]
Hence
\[
M_K=\log\log K+B_1+C_*+o(1).                            \tag{4.8}
\]

## 5. The actual prime-stratum optimum

Let
\[
G(n)=\max\left\{
\sum_kh_k(n)|D_k|:
D_k\subseteq[1,k],\ D_i\sim D_j\text{ for all }i,j
\right\}.
\]
We prove
\[
G(n)=\frac nL\bigl(\log L+B_1+C_*+o(1)\bigr).            \tag{5.1}
\]

First consider the prime-only profile:
\[
\mathcal B(n)=\sum_kh_k(n)\pi(k).
\]
Double counting pairs of primes on opposite sides of \(y\) gives
\[
\mathcal B(n)
=\sum_{q\leq y,\ q\ {\rm prime}}\pi(n/q)-\pi(y)^2.       \tag{5.2}
\]
Uniform quantitative PNT and prime partial summation give
\[
\sum_{q\leq y}\pi(n/q)
=\frac nL\bigl(\log L+B_1+o(1)\bigr).                    \tag{5.3}
\]
Explicitly, \(\sum_{q\leq y}1/q=\log L-\log2+B_1+o(1)\),
while retaining the denominator \(\log(n/q)\) contributes
\[
\int_2^y\frac{dt}{t(L-\log t)}=\log2+o(1).
\]
Since \(\pi(y)^2=O(n/L^2)\), (5.2)--(5.3) yield
\[
\mathcal B(n)=\frac nL(\log L+B_1+o(1)).                 \tag{5.4}
\]

For \(0<\alpha<1\), Chebyshev and a dyadic decomposition give the uniform
tail estimate
\[
\sum_{\substack{p>y\\n/p>K}}(n/p)^\alpha
\ll_\alpha \frac nL K^{\alpha-1}.                        \tag{5.5}
\]
Indeed, when \(Q<n/p\leq2Q\), there are \(O(n/(QL))\) possible primes,
and summing \((n/L)Q^{\alpha-1}\) over dyadic \(Q\geq K\) is geometric.

Fix \(K\).  For \(k\leq K\),
\[
h_k(n)=\left(\frac1{k(k+1)}+o_K(1)\right)\frac nL.       \tag{5.6}
\]
The prefix of any profile is feasible for \(M_K\).  In the tail, Lemma 5
and (5.5) with \(\alpha=5/6,2/3\) give the one-sided bound
\[
\sum_{k>K}h_k(n)(|D_k|-\pi(k))
\leq C\frac nL(K^{-1/6}+K^{-1/3})                        \tag{5.7}
\]
for an absolute constant \(C\).
It follows that
\[
\limsup_{n\to\infty}\frac Ln\bigl(G(n)-\mathcal B(n)\bigr)
\leq R_K+O(K^{-1/6}+K^{-1/3}).
\]
Letting \(K\to\infty\) gives the upper bound \(C_*\).

For the lower bound, take an optimal \(K\)-profile and extend it by the
sets \(E_j\) used in (4.6).  Its prefix excess over the prime profile is
\((R_K+o_K(1))n/L\).  Its tail excess is \(1-\pi(K)\) per occupied
large-prime stratum, and
\[
\sum_{k>K}h_k(n)
=\pi(n/(K+1))-\pi(y)+O(1)
=\left(\frac1{K+1}+o_K(1)\right)\frac nL.
\]
Thus
\[
\liminf_{n\to\infty}\frac Ln\bigl(G(n)-\mathcal B(n)\bigr)
\geq R_K+\frac{1-\pi(K)}{K+1}.
\]
Let \(K\to\infty\).  This proves (5.1).

## 6. Completion of the upper and lower bounds

For the lower bound, choose a profile attaining \(G(n)\) and set
\[
A_{\mathcal D}(n)=
\{pd:p>\sqrt n\text{ prime},\ d\in D_{\lfloor n/p\rfloor}\}.
\]
Every element has a unique large-prime label.  Equal products preserve
the multiset of the two labels, and the relevant coefficient
multiplicity is at most two because every two profile coordinates are
compatible.  Thus \(A_{\mathcal D}(n)\) is admissible and
\[
g_3(n)\geq G(n).                                         \tag{6.1}
\]

For the upper bound, start with any admissible \(A\).  Lemma 1, (2.1),
Corollary 4, and (3.5) give
\[
|A|\leq G(n)+o(n/L).                                     \tag{6.2}
\]
Combine (5.1), (6.1), and (6.2):
\[
g_3(n)=\frac n{\log n}
\bigl(\log\log n+B_1+C_*+o(1)\bigr).
\]
This proves the theorem with \(c=B_1+C_*\).

## 7. An explicit lower bracket for \(C_*\)

The following three infinite coefficient sets are pairwise compatible,
including self-pairs:
\[
\begin{aligned}
C_0&=\{1\}\cup\mathbb P,\\
C_1&=\{1,3,4,5,6\}\cup\{p\geq7:p\text{ prime}\},\\
C_2&=\{1,2,5,7,8,9,11,12,13,15\}
      \cup\{p\geq17:p\text{ prime}\}.
\end{aligned}
\]
This reduces to a finite product check below \(17\): a prime at least \(17\)
in an equality must occur identically on both sides.  The nontrivial finite
coincidences have multiplicity two, never three; they are listed in
attempts/large_prime_profiles.md and checked by
computational/profile_search.py.

Use
\[
D_k=
\begin{cases}
C_0\cap[1,k],&k\leq5,\\
C_1\cap[1,k],&6\leq k\leq11,\\
C_2\cap[1,k],&k\geq12.
\end{cases}
\]
Relative to \(C_0\), the cardinality gains are \(1\) for \(6\leq k\leq11\),
\(2\) for \(12\leq k\leq14\), and \(3\) for \(k\geq15\).  Since the
prime-only profile differs from \(C_0\) by the element \(1\) in every
coordinate,
\[
\begin{aligned}
C_*
&\geq1+
\sum_{k=6}^{11}\frac1{k(k+1)}
+2\sum_{k=12}^{14}\frac1{k(k+1)}
+3\sum_{k=15}^{\infty}\frac1{k(k+1)}\\
&=1+\left(\frac16-\frac1{12}\right)
  +2\left(\frac1{12}-\frac1{15}\right)+\frac3{15}\\
&=\frac{79}{60}.
\end{aligned}
\]
Lemma 5 also gives the finite crude upper bound
\[
C_*\leq\sum_{j\geq1}
\frac{j^{5/6}+\frac32j^{2/3}}{j(j+1)}
\leq\zeta(7/6)+\frac32\zeta(4/3).
\]
