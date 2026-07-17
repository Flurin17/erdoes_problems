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
- very large prime/cofactor ratios;
- far large-prime tail after missing-prime charge.

Open node:

- the critical band with large smooth kernels, small distinguished primes,
  and comparable ratios.

The repair must use full cross-kernel multiplicative Sidonicity and a
two-sided missing-prime charge.  Lifted \(C_4\)-freeness alone is insufficient:
a projective-plane incidence graph on arbitrary composite left vertices has
too many edges by a factor \(\sqrt{\log n}\), even though it need not be a
valid multiplicative-Sidon set.
