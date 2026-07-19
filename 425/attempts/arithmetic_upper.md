# Route: arithmetic upper reduction

## Proved structural lemmas

### Canonical roughness

If \(a=xy\), where \(x\) is the largest divisor of \(a\) not exceeding
\(\sqrt a\), and \(R=y/x\), then
\[
 P^-(y)\ge R.
\]
For if a prime \(\ell\mid y\) satisfies \(\ell\le\sqrt R\), then
\(x\ell\in(x,\sqrt a]\); if \(\sqrt R<\ell<R\), then
\(y/\ell\in(x,\sqrt a)\).  Both contradict the maximality of \(x\).

If \(k=\Omega(y)\), it follows that
\[
 x\ge R^{k-1},\qquad a\ge R^{2k-1}.
\]
Thus a composite \(y\) forces \(R\le n^{1/3}\), and larger ratios force very
small \(\Omega(y)\).

### Kernel-absorbing colored rectangles

Let canonical triples \((d,p,q)\) inject into \(A\) through \(dpq\).
The bipartite graph
\[
 (d,p)\sim q
\]
is \(C_4\)-free: a rectangle would give the four distinct elements
\(dpq,dps,erq,ers\) and the collision
\[
 (dpq)(ers)=(dps)(erq).
\]
Consequently, with \(M\) active left vertices, \(R\) active right vertices,
and \(E\) triples,
\[
 E^2/M-E\le R(R-1),\qquad E\le M+R\sqrt M.
\]
This couples all smooth-kernel colors before applying the square-root bound.

For dyadic
\[
 D\le d<2D,\quad X\le p<2X,\quad p\le q\le2p,
\]
with \(p,q\ge n^\delta\), this gives
\[
 E_{D,X}\ll_\delta
 \frac{DX}{\log n}
 +\frac{D^{1/2}X^{3/2}}{(\log n)^{3/2}}.
\]
Summing \(X\), then \(D\le\sqrt n/\log n\), bounds this entire
comparable-prime, small-kernel sector by the target scale.

### Two-flattening theorem for the whole comparable two-prime sector

The small-kernel restriction above is unnecessary when the complementary
canonical factor has exactly two prime factors.

**Theorem.** Fix \(K\ge1\). Suppose that every member of a family
\(\mathcal T\) is a distinct element of a pair-product-Sidon set
\(A\subseteq[n]\), and is assigned one (and only one) triple
\[
 a=dpq,\qquad p\le q\le Kp,
\]
where \(p,q\) are prime, \(d\le pq\), and \(dpq\le n\). Then
\[
 |\mathcal T|\ll_K \frac{n^{3/4}}{(\log n)^{3/2}}.
\]

For a dyadic \(P\le p<2P\), put \(\ell_P=\log(2P)\) and choose
\[
 D=C_K\min(P^2,n/P^2)
\]
large enough to bound every possible \(d\).
The graph with tagged parts \(d\) and \(pq\) is \(C_4\)-free: a rectangle
would give four distinct selected elements \(d_i(p_jq_j)\) and the forbidden
collision
\[
 [d_1(p_1q_1)][d_2(p_2q_2)]
   =[d_1(p_2q_2)][d_2(p_1q_1)].
\]
Its parts have sizes at most \(D\) and
\(O_K(P^2/\ell_P^2)\), respectively, so
\[
 E_P\ll_K D+\frac{P^2\sqrt D}{\ell_P^2}.                 \tag{1}
\]
The second graph, with tagged parts \((d,p)\) and \(q\), is also
\(C_4\)-free and gives
\[
 E_P\ll_K \frac{DP}{\ell_P}
       +\frac{\sqrt D\,P^{3/2}}{\ell_P^{3/2}}.           \tag{2}
\]
Both assertions use the elementary bound
\(\pi(CP)\ll_C P/\log(2P)\) and the oriented \(C_4\) estimate
\(e\le m+r\sqrt m\).

Let \(L=\log n\), \(X=n^{1/4}\), and
\(P_0=XL^{1/2}\). Use (1) up to \(P_0\) and (2) afterwards.
For \(P\le X\), their dyadic sum is
\[
 O_K(n^{1/2}+n^{3/4}L^{-2}).
\]
For \(X<P\le P_0\), (1) sums to
\[
 O_K\!\left(n^{1/2}+\sqrt n\,P_0L^{-2}\right)
 =O_K(n^{3/4}L^{-3/2}).
\]
Finally, for \(P_0<P\le\sqrt n\), (2) is
\[
 O_K\!\left(\frac n{PL}
       +\frac{\sqrt{nP}}{L^{3/2}}\right),
\]
whose decreasing and increasing dyadic sums are both endpoint-dominated by
the target. Subpolynomial \(P\) causes no loss because one retains
\(\ell_P=\log(2P)\) there.

For the canonical decomposition, \(d\) is the largest divisor not exceeding
\(\sqrt a\), while \(a/d=pq\); hence the assignment is unique and \(d\le pq\).
Thus this theorem closes the formerly open comparable \(\Omega(a/d)=2\)
critical band, with no smoothness assumption on \(d\).

The one-triple-per-element condition is essential. If all admissible
factorizations are retained, distinct formal vertices \((d_1,p_1)\) and
\((d_2,p_2)\) can satisfy \(d_1p_1=d_2p_2\), creating a formal \(K_{2,2}\)
whose four edges represent only two integers. Canonical selection excludes
this degeneracy.

### Negligibility of a prime in the kernel larger than both complementary primes

There is a stronger estimate for the most nonsmooth part of this sector.
Suppose, in addition, that
\[
 r=P^+(d)>q,\qquad d=hr.
\]
Then \(h<p\), because \(hr=d\le pq\) and \(r>q\). For dyadic
\(H\le h<2H\) and \(Q\le p<2Q\), graph the selected element
\[
 a=(hpq)r
\]
as an edge \(hpq--r\). The representation is injective: \(r\) is the unique
largest prime factor, since every prime factor of \(hpq\) is smaller than
\(r\). The graph is \(C_4\)-free by the usual multiplicative-rectangle
argument.

Writing \(\ell_Q=\log(2Q)\), its part sizes satisfy
\[
 M\ll_K\frac{HQ^2}{\ell_Q^2},\qquad
 R\ll_K\frac{\min(Q^2/H,n/(HQ^2))}{\ell_Q}.
\]
Consequently
\[
 E_{H,Q}\ll_K
 \frac{HQ^2}{\ell_Q^2}
 \frac{\min(Q^3,n/Q)}{\sqrt H\,\ell_Q^2}.
\]
Nonemptiness forces
\[
 H\ll_K\min(Q,n/Q^3).
\]
The dyadic \(H\)-sum is therefore
\[
 \ll_K \frac{\min(Q^3,n/Q)}{\ell_Q^2}.
\]
For \(Q\le n^{1/8}\) this sums to \(O(n^{3/8})\). Above that point
\(\ell_Q\asymp\log n\), and the sum is geometrically dominated at
\(Q=n^{1/4}\). Thus the whole bad-kernel sector is
\[
 O_K\!\left(\frac{n^{3/4}}{(\log n)^2}\right)=o\!\left(
 \frac{n^{3/4}}{(\log n)^{3/2}}\right).
\]

This also repairs a tempting but false smoothness assertion. Canonical
\(d\) need not satisfy \(P^+(d)=O(p)\): choose primes
\(p<q<2p\) and \(pq/2<r<pq\), and take \(a=pqr\). Then \(d=r\) is the
largest divisor at most \(\sqrt a\), while \(P^+(d)\asymp p^2\). The estimate
above, rather than pointwise smoothness, removes this family at leading
order.

### Prime-deficit tail

For chosen composites \(uq\in A\) with prime \(q\) and \(u\le U\), subtract
the incident missing \(q\)'s.  The graph \(u-q\) is \(C_4\)-free, while each
\(u\) has at most one neighbor \(q\in A\), because
\[
 (uq)r=(ur)q.
\]
It follows that the net excess is at most
\[
 U+\binom U2.
\]
More generally, for \(y>\sqrt n\),
\[
 \#\{qk\in A:q>y\text{ prime},\,k\ge2\}
 -\#\{q>y:q\notin A\}=O((n/y)^2).
\]
At \(y=n^{5/8}(\log n)^{3/4}\), this is at the target scale.

## Dependency graph

Closed nodes:

- exact prime ledger: excess equals composites minus missing primes;
- canonical roughness and its \(\Omega\)-spectrum;
- colored-kernel \(C_4\) coupling;
- small-kernel/comparable distinguished primes;
- the entire canonical comparable two-prime sector, by the two flattenings;
- very large prime/cofactor ratios;
- far large-prime tail after missing-prime charge.

Open node:

- synthesize the remaining \(\Omega(a/d)=1\) and \(\Omega(a/d)\ge3\) canonical
  sectors with the prime-deficit ledger at the same precision, and then
  strengthen the order bound enough to identify an exact leading constant.

The first of these is a proof-synthesis obligation rather than the former
critical-band bottleneck. Exact-constant work still needs full cross-kernel
multiplicative Sidonicity and a two-sided missing-prime charge. A single
lifted \(C_4\) bound remains insufficient for that sharper task.
