# Notes: Erdős #796

All logarithms are natural.  Throughout, (n) is a positive integer and
([n]=\{1,\ldots,n\}).

## 1. Exact normalization

For (A\subseteq[n]), define
\[
r_A(m)=\#\{\{a,b\}\subseteq A:a<b,\ ab=m\}
       =\sum_{\substack{d\mid m\\d<m/d}}
          1_A(d)1_A(m/d).
\]
Then
\[
g_3(n)=\max\{|A|:A\subseteq[n],\ r_A(m)\leq2\text{ for every }m\geq1\}.
\]
It is enough to quantify over (2\leq m\leq n(n-1)).  Products outside this
range have no distinct factor pair in ([n]).  The asymptotic question is
equivalent to convergence of
\[
\frac{\log n}{n}g_3(n)-\log\log n
\]
to a finite real number (c), which would necessarily be unique.

The phrase “every (m)” is naturally read as every positive integer.  Reading
it as only (m\leq n) would materially change the problem.  The source does
not specify a logarithm base; natural logarithms are the standard
analytic-number-theory convention and are fixed here.

For (n=1), (g_k(1)=1); for (n=2), (g_k(2)=2) for every (k\geq2).

## 2. Collision and overlap lemma

**Lemma 2.1 (equal-product pairs are disjoint).**  If two distinct two-element
sets (P,Q\subset\mathbb N) have the same element-product, then
(P\cap Q=\varnothing).

**Proof.**  If (z\in P\cap Q), write (P=\{z,u\}) and (Q=\{z,v\}).
Cancellation in (zu=zv) gives (u=v), contrary to (P\ne Q).  ∎

**Corollary 2.2 (exact forbidden pattern).**  A set (A) violates the
(k=3) condition if and only if it contains six elements
\[
x_1<x_2<x_3<y_3<y_2<y_1
\]
such that
\[
x_1y_1=x_2y_2=x_3y_3.
\]

**Proof.**  Three distinct representations are pairwise disjoint by Lemma
2.1.  In a representation (ab=m) with (a<b), one has
(a<\sqrt m<b).  Order the three smaller factors increasingly; their
partners (m/a) then occur in reverse order.  The converse is immediate. ∎

Thus no violation can live on three, four, or five elements.  A square (m)
may have non-diagonal representations, but the diagonal pair
(\{\sqrt m,\sqrt m\}) is never counted.

## 3. Equivalent formulations

For each (m), let (F_m) be the graph on ([n]) whose edges are the
two-element factor pairs of (m).  Lemma 2.1 says that every (F_m) is a
matching, and
\[
r_A(m)=e(F_m[A]).
\]
Equivalently, color every edge (\{a,b\}) of (K_n) by (ab).  This is a
proper edge-coloring, and admissibility says that no color occurs on three
edges of (K_n[A]).

Let (\mathcal H_n) be the 6-uniform hypergraph on ([n]) whose hyperedges
are unions of three distinct edges of one (F_m).  Then
\[
g_3(n)=\alpha(\mathcal H_n),\qquad
e(\mathcal H_n[A])=\sum_m\binom{r_A(m)}3.
\]
The common product attached to a hyperedge is unique: the product of its six
vertices is (m^3).  Its three factor pairs are then also unique, since the
partner of (a) is (m/a).

In prime-valuation vectors, with
(\nu(a)=(v_p(a))_p), the problem asks for a restricted unordered
(B_2[2]) set in
\[
\Lambda_n=\{x\in\bigoplus_p\mathbb N_0:
                 \sum_p x_p\log p\leq\log n\}:
\]
every vector sum (x+y) with (x\ne y) has at most two unordered
representations.  If (V=\nu(A)), (s\) is a valuation vector, and
(\epsilon_s=1_{\{s/2\in V\}}), then exactly
\[
2r_V^\wedge(s)=|V\cap(s-V)|-\epsilon_s.
\]

For Dirichlet convolution (f=1_A), put
(\delta_A(m)=1_{\{m=t^2, t\in A\}}).  Then
\[
(f*f)(m)=2r_A(m)+\delta_A(m),
\]
so the exact convolution constraint is
\[
(f*f)(m)-\delta_A(m)\leq4.
\]
Omitting the diagonal correction would incorrectly rule out a square having
two legal non-diagonal representations.

If (R=\binom{|A|}{2}), (d=|\{m:r_A(m)=2\}|), and
(P^\wedge(A)=\{ab:a<b,\ a,b\in A\}), admissibility gives the exact identities
\[
|P^\wedge(A)|=R-d,
\qquad
E_2^\wedge(A):=\sum_m r_A(m)^2=R+2d=3R-2|P^\wedge(A)|\leq2R.
\]
These second-moment identities are necessary bookkeeping but are not
equivalent to admissibility; the exact obstruction is the third factorial
energy (\sum_m\binom{r_A(m)}3).

## 4. Restricted prime--semiprime model

Let (S) be the selected primes and let (E) be the graph on primes whose
edge (pq) denotes selection of the squarefree semiprime (pq).  Inside the
universe of primes and squarefree semiprimes, admissibility is exactly:

1. (E) is (K_4)-free; and
2. the induced graph (E[S]) is triangle-free.

Indeed, three semiprime--semiprime representations of a squarefree product of
four primes are its three perfect matchings and require all six edges of a
(K_4).  Three prime--semiprime representations of a squarefree product of
three primes require selection of all three vertices and all three opposite
edges.  Repeated prime factors only merge possible representations and create
no additional forbidden type.  Adding a dummy vertex joined to the primes in
(S) turns both conditions into (K_4)-freeness in the augmented graph.

A particularly useful admissible family is
\[
A_0(n)=\{p\leq n:p\text{ prime}\}
 \cup\{pq\leq n:p,q\text{ distinct primes},\ p\leq\sqrt n<q\}.
\]
The two magnitude classes form a bipartite prime graph.  A product of two
selected semiprimes has at most the two cross perfect matchings, while a
product of a selected prime and semiprime has at most two complementary
cross edges.  Therefore (r_{A_0}(m)\leq2).

Let
\[
B_1=\lim_{x\to\infty}
   \left(\sum_{p\leq x}\frac1p-\log\log x\right)
\]
be the prime Mertens constant.  Standard PNT with a uniform error for
(x\geq\sqrt n), followed by partial summation of the prime harmonic sum,
gives
\[
|A_0(n)|=\frac n{\log n}
  \left(\log\log n+1+B_1+o(1)\right).
\]
The apparent (-\log2) in
(\sum_{p\leq\sqrt n}1/p) is canceled by
\[
\int_0^{1/2}\frac{du}{1-u}=\log2
\]
when the denominator (\log(n/p)) in (\pi(n/p)) is retained.  Semiprimes
with both prime factors at most (\sqrt n) number only
(O(n/\log^2 n)=o(n/\log n)).

This proves only the baseline lower constant (1+B_1); it is not the best
construction found in this run.

## 5. Strong multiplicative-Sidon lifting

Call (D\subseteq\mathbb N) **strongly multiplicative Sidon** if the map
\[
\{d,e\}\longmapsto de
\]
is injective on unordered pairs from (D), with diagonal pairs allowed.
Let (y=\sqrt n), (D_y=D\cap[1,y]), and define
\[
L_n(D)=D_y\ \cup\
 \{dq:d\in D_y,\ q>y\text{ prime},\ dq\leq n\}.
\]

**Lemma 5.1 (large-prime lift).**  If (D) is strongly multiplicative Sidon,
then (L_n(D)) is admissible for Problem #796.

**Proof.**  A lifted element has a unique prime factor (q>y); its cofactor
is at most (y).  Hence all displayed elements are distinct.  In the product
of two elements of (L_n(D)), unique factorization intrinsically determines
the multiset of prime factors larger than (y), of size zero, one, or two.
It also determines the product (de) of the two (D)-cofactors.  Strong
Sidonicity determines the unordered cofactor pair (\{d,e\}).  With no large
prime there is at most one representation.  With one large prime, there are
at most two choices for which cofactor receives it.  With two distinct large
primes there are at most the two assignments of those primes to (d,e); with
two equal large primes there is at most one.  Requiring the two final elements
to be distinct can only delete cases. ∎

There is also the exact count
\[
|L_n(D)|=|D_y|+
 \sum_{\substack{d\in D\\d\leq y}}
       \bigl(\pi(n/d)-\pi(y)\bigr).
\]
The baseline (D=\{1\}\cup\{p:p\text{ prime}\}) recovers (A_0(n)), up to
the negligible inclusion of the small coefficients themselves.

**Lemma 5.2 (uniform count of a fixed lift).**  Suppose a fixed set $D$
satisfies
\[
H_D(x):=\sum_{\substack{d\leq x\\d\in D}}\frac1d
       =\log\log x+K+o(1).
\]
Then, using the standard quantitative PNT
$\pi(t)=t/\log t+O(t/\log^2t)$,
\[
|L_n(D)|=\frac n{\log n}
 \bigl(\log\log n+K+o(1)\bigr).
\]

**Proof.**  Write $L=\log n$, $y=\sqrt n$, and
$N_D(x)=|D\cap[1,x]|$.  The harmonic hypothesis implies $N_D(x)=o(x)$:
for fixed $0<\lambda<1$,
\[
N_D(x)-N_D(\lambda x)
 \leq x\bigl(H_D(x)-H_D(\lambda x)\bigr)=o(x),
\]
and then let $\lambda\downarrow0$.  Consequently both $N_D(y)$ and
$N_D(y)\pi(y)$ are $o(n/L)$.  Uniform PNT for $n/d\geq y$ reduces the
exact count to
\[
nS_L+o(n/L),\qquad
S_L=\sum_{\substack{d\leq y\\d\in D}}
       \frac1{d(L-\log d)}.
\]
Now
\[
LS_L=H_D(y)+Q_L,\qquad
Q_L=\sum_{\substack{d\leq y\\d\in D}}
 \frac1d\frac{\log d}{L-\log d}.
\]
Put $F(u)=H_D(e^u)=\log u+K+o(1)$.  Stieltjes partial summation gives
\[
Q_L=\int_{[0,L/2]}\frac{u}{L-u}\,dF(u)
   =\int^{L/2}\frac{du}{L-u}+o(1)
   =\log2+o(1).
\]
The bounded initial interval contributes $o(1)$, and integration by parts
bounds the tail error by twice the supremum of the $o(1)$ remainder.  Finally
$H_D(y)=\log L-\log2+K+o(1)$, so the two $\log2$ terms cancel. ∎

If (E\subseteq\mathbb N_0) is an additive Sidon set for unordered sums with
repetition and (0\in E), then
\[
D_E=\{1\}\cup\{p^e:p\text{ prime},\ e\in E\setminus\{0\}\}
\]
is strongly multiplicative Sidon.  This follows immediately by comparing
prime supports and then exponent sums.  For example,
\[
E_*=\{2^j-1:j\geq0\}=\{0,1,3,7,15,\ldots\}
\]
is additive Sidon: after adding $2$, an equality between two exponent sums
is an equality between sums of two powers of $2$, whose unordered summands
are unique.  Hence, with $P(s)=\sum_p p^{-s}$, Lemmas 5.1--5.2 prove
\[
g_3(n)\geq\frac n{\log n}\left(
 \log\log n+1+B_1+\sum_{j\geq2}P(2^j-1)+o(1)\right).       \tag{5.1}
\]
The series converges absolutely, so the baseline coefficient $1+B_1$ is
rigorously not extremal.

For a fixed strong $D$ containing $1$ and every prime, if its composite
reciprocal mass
\[
C(D)=\sum_{\substack{d\in D\\d\text{ composite}}}\frac1d
\]
converges, Lemma 5.2 gives
\[
|L_n(D)|=\frac n{\log n}
  \left(\log\log n+1+B_1+C(D)+o(1)\right).
\]

## 6. Exact large-prime fibers

For an arbitrary admissible (A\), let (y=\sqrt n) and, for every prime
(p>y), define
\[
B_p=\{d\leq n/p:pd\in A\}.
\]
If (p\ne q) are primes greater than (y), then unique factorization gives
the exact identity
\[
r_A(pqt)=
 \#\{(d,e)\in B_p\times B_q:de=t\}.
\]
Thus every two distinct fibers obey the ordered cross-convolution constraint
\[
\#\{(d,e)\in B_p\times B_q:de=t\}\leq2
\quad\text{for every }t.
\]
For completeness, a coefficient $d<n/p<\sqrt n$ is coprime to $p$, and
similarly for $q$.  If $t$ contains $p,q$, or a third prime exceeding
$\sqrt n$, both sides of the preceding identity are zero: a product of two
integers at most $n$ can contain at most two such large prime factors,
counted with multiplicity.
When two full dilates (pD,qD\) occur, this forces (D) to be strongly
multiplicative Sidon: an off-diagonal cofactor factorization already produces
its two orientations, leaving no room for a second factorization or a
diagonal one.

## 7. Closed structural decomposition

The two former upper-bound bottlenecks are now closed.

**Smooth lemma.**  Every admissible \(A\subseteq[1,n]\) satisfies
\[
|\{a\in A:P^+(a)\leq\sqrt n\}|
\ll \frac{n(\log\log n)^2}{\log^2n}
=o(n/\log n).
\]
The proof factors all but an explicitly counted exceptional set into three
large factors.  A \(2\times2\times2\) box of chosen factorizations gives four
equal-product pairs, and a link-intersection \(C_4\) bound controls the
resulting cube-free 3-graph.

**Fiber-repair lemma.**  For pairwise cross-compatible fibers
\(B_i\subseteq[1,N]\), all fibers can be made self-compatible by at most
\(O(N^2\log N)\) total deletions.  Equal-product witnesses cannot occur in
two fibers, and the ambient number of witnesses is bounded by the number of
solutions to \(ab=cd\) in \([N]\), which is \(O(N^2\log N)\).  Applying this
dyadically and using the standard weak multiplication-table theorem in the
last \(O(\log\log n)\) capacity blocks costs \(o(n/\log n)\).

After repair, choose the largest fiber in each stratum
\(k=\lfloor n/p\rfloor\).  This reduces every admissible set, with
\(o(n/\log n)\) loss, to pairwise and self-compatible profiles
\(D_k\subseteq[1,k]\).

## 8. Exact constant

For
\[
\mu_{U,V}(t)=|\{(u,v)\in U\times V:uv=t\}|,
\]
write \(U\sim V\) if \(\mu_{U,V}(t)\leq2\) for every \(t\), and define
\[
M_K=\max_{\substack{D_k\subseteq[1,k]\\D_i\sim D_j\ \forall i,j}}
\sum_{k\leq K}\frac{|D_k|}{k(k+1)},\qquad
P_K=\sum_{k\leq K}\frac{\pi(k)}{k(k+1)}.
\]
A self-compatible \(D\subseteq[1,N]\) obeys
\[
|D|\leq\pi(N)+N^{5/6}+\tfrac32N^{2/3}.
\]
This makes the excess \(M_K-P_K\) Cauchy.  Put
\[
C_*=\lim_{K\to\infty}(M_K-P_K).
\]
The exact large-prime stratum optimum is
\[
\frac n{\log n}\bigl(\log\log n+B_1+C_*+o(1)\bigr).
\]
The smooth lemma and fiber repair give the matching upper bound, while
lifting any compatible profile gives the matching lower bound.  Therefore
\[
\boxed{c=B_1+C_*}.
\]
An explicit three-profile construction proves \(C_*\geq79/60\).

## 9. Proof-dependency graph

- Collision normalization and strict-pair conventions: proved in Sections
  1--3 above.
- Smooth exceptional estimate: proved locally in PROOF.md, Lemma 1.
- Large-prime fiber identity: proved locally in PROOF.md, Lemma 2.
- Witness repair and homogenization: proved locally in PROOF.md, Lemma 3
  and Corollary 4.
- Strong multiplicative-Sidon bound and convergence of \(C_*\): proved
  locally in PROOF.md, Lemma 5 and Section 4.
- Prime-stratum count and uniform tails: quantitative PNT, prime Mertens,
  and locally proved partial-summation/dyadic reductions.
- Large-capacity repair envelope: the explicitly stated standard weak
  multiplication-table theorem.
- Explicit profile compatibility and finite values: independently checked by
  computational/profile_search.py; computation is not used for the general
  asymptotic.
