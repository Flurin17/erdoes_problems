# Route: restricted quotient energy

For a fiber \(B\), let
\[
 Q(B)=\{x/y:x,y\in B,\ x\ne y\}.
\]
In a pair-admissible \(B\), an off-diagonal quotient has multiplicity at most
two.  The multiplicity-two case is exactly an allowed diagonal relation
\(ab=c^2\).  If \(T(B)\) counts those relations, then
\[
 |Q(B)|=|B|(|B|-1)-2T(B).
\]

If disjoint scaled fibers \(\lambda_iB_i\) lie in one admissible \(A\), their
off-diagonal quotient supports are disjoint.  This proves useful packing
bounds.  In particular, if every cofactor is \(1\) or prime, it gives the
correct target-order upper bound after dyadic summation.  Combining this with
the \(C_4\)-free small-semiprime graph proves
\[
 A\subseteq\{1\}\cup\{m:\Omega(m)\le2\}
 \quad\Longrightarrow\quad
 |A|\le\pi(n)+O\!\left(
 n^{3/4}(\log n)^{-3/2}\right).
\]

## Exact obstruction to arbitrary compression

A hoped-for replacement of the cofactor universe \(z\) by \(\pi(z)\) is
false.  For every coprime \(1\le a<b\le z\), take \(B_{a,b}=\{a,b\}\).
Their quotient supports
\[
 \{a/b,b/a\}
\]
are pairwise disjoint, and there are \(\Omega(z^2)\) such fibers.  Hence
\[
 \sum(|B_i|-1)\asymp z^2,
 \qquad
 \pi(z)\sqrt{\#\{i\}}=o(z^2).
\]
Choosing distinct large primes \(\lambda_i\) realizes these as genuine scaled
fibers in a pair-admissible integer set.

For every fixed \(k\), one can moreover greedily pack
\(\Omega_k(z^2)\) pairwise-coprime \(k\)-subsets with disjoint two-shadows.
This defeats even a proposed repair with any fixed additive multiple of the
number of fibers.

Thus quotient packing remains useful only after arithmetic structure or a
baseline charge restricts the allowed fibers.
