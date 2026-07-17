# Route: the fixed-\(r\) problem

Let \(P_r(A)\) mean injectivity of the product map on \(\binom Ar\).

## Exact semiprime graph lemma

Let \(R,U,V\) be disjoint prime sets, let \(G\subseteq U\times V\), and put
\[
 A=R\cup\{uv:(u,v)\in E(G)\}.
\]
If \(|R|\ge r-2\), then \(A\) has \(P_r\) if and only if \(G\) has no
\[
 C_4,C_6,\dots,C_{2r}.
\]

For a collision, the total \(\Omega\) value gives equal semiprime counts and
the \(R\)-valuations force identical retained primes.  Cancel common edges,
color the two residual edge sets red and blue, and orient red \(U\to V\) and
blue \(V\to U\).  Equal valuations make the directed graph balanced, so it
contains an alternating directed cycle of length at most \(2r\).  Conversely,
the two alternating matchings of \(C_{2k}\) have equal products and can be
padded by \(r-k\) common retained primes.

This gives
\[
 F_r(n)\ge\pi(n)-2M+h_r(M),
 \qquad M=\lfloor\pi(\sqrt n)/2\rfloor,
\]
where \(h_r(M)\) is the maximum edge count in a balanced bipartite graph of
girth greater than \(2r\).

## Prime/semiprime upper theorem

Set \(\alpha=(r+1)/(2r)\).  Subject to the standard asymmetric even-girth
estimate recalled from memory,
\[
 e(B)\ll_r (mn)^\alpha+m+n
\]
for a bipartite \(B\) with no \(C_4,\ldots,C_{2r}\), one obtains:
\[
 A\text{ consists of primes and semiprimes and has }P_r
 \quad\Longrightarrow\quad
 |A|\le\pi(n)+O_r(n^\alpha).
\]

Encode primes as edges from a root of weight \(1\), and semiprimes as edges
between prime vertices.  Peel to the \(2\)-core, so tree edges are paid for by
the \(\pi(n)+1\) vertex baseline.  The small-prime core has
\(O_r(n^\alpha)\) edges.  Dyadic large-prime bands have product \(mn\ll n\);
the asymmetric girth estimate and geometric summation give \(O_r(n^\alpha)\).

The exact hypotheses of the quoted asymmetric girth theorem should be checked
before this special-case theorem is promoted from conditional to
dependency-complete.

## Arbitrary integers: proved reduction

With \(s=\lfloor r/2\rfloor\), put
\[
 \gamma=1+1/s,\qquad
 \theta=1-\frac{(r+1)/(2r)}{\gamma}.
\]
Largest-prime fiber compression and the ordinary even-cycle bound prove
\[
 \#\{a\in A:P^+(a)\ge n^\theta\}
 \le\pi(n)+O_r(n^{(r+1)/(2r)}).
\]
Thus the remaining explicit bottleneck is
\[
 P^+(a)<n^\theta\ \forall a\in A
 \quad\Longrightarrow\quad
 |A|=O_r(n^{(r+1)/(2r)}).
\]

Pure incidence girth cannot solve this smooth core.  The family \(uv^2\)
has a forest as its largest-prime incidence graph, while rectangular choices
satisfy
\[
 (u_1v_1^2)(u_2v_2^2)=(u_1v_2^2)(u_2v_1^2).
\]
The missing lemma must retain higher quotient-product spectra, not treat
composite cofactors as atomic vertices.
