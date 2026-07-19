# Ascending-largest-prime greedy assignment

## Model

Fix \(N\), a torsion-free additive target group (in particular \(\mathbb Q\)
or \(\mathbb R\)), and target value \(1\).  Process primes in increasing
order.  When the prime \(p\) is reached, the weights \(w_q\) for \(q<p\)
have already been chosen.  The integers whose membership is now determined
are
\[
 B_p(N)=\{n\leq N:P^+(n)=p\}.
\]
Writing such an integer uniquely as \(n=p^a m\), where \(a\geq1\) and
\(P^+(m)<p\), the local largest-factor greedy rule chooses \(w_p\) to
maximize
\[
 H_p(w)=\sum_{a\geq1}
 \#\{m\leq N/p^a:P^+(m)<p, f_{<p}(m)=1-aw\}.
 \tag{1}
\]
Here \(f_{<p}(m)=\sum_{q<p}v_q(m)w_q\).  At the end one takes
\(A_N=\{n\leq N:f(n)=1\}\), or any subset of this level set.

The blocks \(B_p(N)\) partition \([2,N]\), and later choices cannot alter a
value on \(B_p(N)\).  Thus (1) is the exact one-step recurrence: if \(S_p\)
is the number of successes in blocks through \(p\), then
\[
 S_p=S_{p^-}+\max_w H_p(w).
 \tag{2}
\]
The earlier choices affect later functions \(H_q\), so (2) is a greedy
recurrence, not a dynamic-programming optimum.

For \(p>\sqrt N\), put \(M=\lfloor N/p\rfloor\).  Only \(a=1\) occurs and
every \(m\leq M\) has \(P^+(m)<p\), so (1) simplifies to
\[
 \max_w H_p(w)=\max_t\#\{m\leq M:f(m)=t\}.
 \tag{3}
\]
Thus the large-prime step is exactly a modal-value recurrence.

## The first greedy decision is fatal

**Lemma 1 (the greedy rule activates 2).**  If \(N\geq2\), every locally
greedy choice at the first step has \(w_2\ne0\).

**Proof.**  Let \(L=\lfloor\log_2N\rfloor\).  The block \(B_2(N)\) is
\(\{2,2^2,\ldots,2^L\}\), and
\[
 H_2(w)=\#\{1\leq a\leq L:aw=1\}.
\]
The value is zero at \(w=0\), at most one for every \(w\), and exactly one
at each \(w=1/a_0\), \(1\leq a_0\leq L\).  Hence the greedy maximum is one
and every maximizer is nonzero. \(\square\)

**Lemma 2 (least-active-prime obstruction).**  Let \(f\) be completely
additive with values in a torsion-free group, and suppose \(w_q=f(q)\ne0\)
for a prime \(q\).  For any target \(t\),
\[
 \#\{n\leq N:f(n)=t\}\leq N-\lfloor N/q\rfloor.
 \tag{4}
\]
In particular, if \(w_2\ne0\), every level has size at most
\(\lceil N/2\rceil\).

**Proof.**  Partition \([N]\) into its \(q\)-adic chains
\[
 C_r=\{q^a r\leq N:a\geq0\},\qquad q\nmid r.
\]
On a fixed chain,
\(f(q^ar)=f(r)+aw_q\).  Torsion-freeness and \(w_q\ne0\) make these values
pairwise distinct, so a target level contains at most one member of each
chain.  The number of chains is the number of \(q\)-free positive integers
at most \(N\), namely \(N-\lfloor N/q\rfloor\). \(\square\)

**Corollary 3 (failure of ascending-prime local greedy).**  Under the model
above, for every \(N\geq2\),
\[
 |A_N|\leq\lceil N/2\rceil.
\]
Consequently this greedy algorithm cannot produce density \(1-o(1)\),
regardless of all tie-breaking choices after or at the first step.

**Proof.**  Combine Lemmas 1 and 2. \(\square\)

The conclusion remains true if the final construction discards some points
from the level set.  It also remains true for vector weights in any
torsion-free abelian group.

## What a successful adaptive rule would have to change

If \(q_N\) is the least prime with \(w_{q_N}\ne0\), (4) gives
\[
 1-|A_N|/N\geq 1/q_N+O(1/N).
\]
Hence density \(1-o(1)\) forces \(q_N\to\infty\).  In particular, a viable
recursive construction must deliberately assign weight zero to every fixed
small prime once \(N\) is large.  This necessarily sacrifices all locally
available successes in the first several largest-factor blocks; it cannot
be implemented by the myopic recurrence (2).

For comparison, after \(w_2\ne0\), Lemma 2 applied on every initial segment
in (3) gives
\[
 \max_w H_p(w)\leq\lceil\lfloor N/p\rfloor/2\rceil
 \qquad(p>\sqrt N),
\]
so even the modal recurrence explicitly records the same loss.  The global
chain argument is stronger and avoids any prime-distribution estimate.

## Prefix-defect accounting

For a fixed completely additive \(f\), write
\[
 D_t(x)=\#\{n\leq x:f(n)=t\},\qquad
 E(x)=x-\max_tD_t(x)
 \tag{5}
\]
for integral \(x\geq1\).  Thus \(E(x)\) is the number missed by the most
populous level on the prefix \([x]\).

**Lemma 4 (large-prime blocks charge prefix defect).**  Let
\(A\subseteq\{n\leq N:f(n)=1\}\), and put \(m=N-|A|\).  Then, with the
following sum taken over primes,
\[
 m\geq\sum_{\sqrt N<p\leq N}E(\lfloor N/p\rfloor).
 \tag{6}
\]

**Proof.**  For a prime \(p>\sqrt N\), every member of \(B_p(N)\) is
uniquely \(pn\) with \(1\leq n\leq M_p:=\lfloor N/p\rfloor\).  Since
\[
 f(pn)=w_p+f(n),
\]
at most
\(D_{1-w_p}(M_p)\leq\max_tD_t(M_p)=M_p-E(M_p)\) members of this block can
belong to \(A\).  The block therefore contains at least \(E(M_p)\) missing
integers.  The blocks for distinct largest prime factors are disjoint, so
summing their missing integers proves (6). \(\square\)

**Lemma 5 (a modal change costs a whole half-scale).**  Choose modal values
\[
 u\in\mathop{\rm argmax}_tD_t(x),\qquad
 v\in\mathop{\rm argmax}_tD_t(2x).
\]
If \(u\ne v\), then
\[
 E(x)+E(2x)\geq x.
 \tag{7}
\]

**Proof.**  The \(u\)-level in \([x]\) and the \(v\)-level in \([2x]\)
are disjoint subsets of \([2x]\).  Hence
\[
 (x-E(x))+(2x-E(2x))=D_u(x)+D_v(2x)\leq2x,
\]
which rearranges to (7). \(\square\)

This lemma is tie-safe: it applies to any two selected modal values that
are unequal.  Thus a route seeking small \(E(x)\) on adjacent dyadic scales
must keep a common modal value across those scales.

Finally, there is no freedom in a normalized scale-homogeneous boundary
profile.  Precisely, if a partition profile \(\phi\) is normalized by
\(\phi(1)=1\) and scale homogeneity means
\[
 \phi(\lambda x)=\lambda\phi(x)
 \tag{8}
\]
whenever the displayed arguments lie in its domain, then setting \(x=1\)
in (8) gives
\[
 \phi(\lambda)=\lambda.
 \tag{9}
\]
Thus every normalized scale-homogeneous partition profile is the identity
\(\phi(x)=x\); a nonlinear proposed profile necessarily introduces a scale
dependence and is not homogeneous in the sense of (8).

## Falsification test

Any claimed implementation of this exact local greedy rule should be tested
at its \(p=2\) update.  If it selects \(w_2=0\), it is not maximizing
\(H_2\); if it selects \(w_2\ne0\), enumerate integers by odd part and check
that no target level contains two members of one \(2\)-adic chain.  Either
branch prevents the claimed density-one conclusion under the stated rule.
