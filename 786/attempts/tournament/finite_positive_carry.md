# Hierarchical carry weights: local carries do not repair rounding

## Status

This note proves three rigorous obstructions for the repetition-allowed
interpretation:

1. a high-density exact additive level has a long **zero spine**;
2. positional carries obey exact congruences and therefore supply no
   context-dependent freedom;
3. the natural top level of the scalar code
   \(p\mapsto\lfloor\log p/h\rfloor\) cannot have density tending to one.

The last result also applies to any mixed-radix implementation of that same
scalar code.  It does **not** rule out signed weights, over-quantizers, an
arbitrarily shifted target level, or a genuinely different multiscale code.
In particular, this is an obstruction, not a solution of the finite problem.

Throughout, \(F\) is completely additive with values in a torsion-free
abelian group (in the applications, \(\mathbb Q\) or \(\mathbb R\)).

## 1. The exact zero spine

Let
\[
 A=\{n\leq N:F(n)=1\},\qquad m=N-|A|.
\]

### Lemma 1 (overlap form)

If \(\lfloor N/d\rfloor>2m\), then \(F(d)=0\).

### Proof

Among the \(\lfloor N/d\rfloor\) integers \(k\leq N/d\), at most \(m\)
fail to lie in \(A\), and at most \(m\) have \(dk\notin A\).  Thus some
\(k\) has both \(k,dk\in A\).  Complete additivity gives
\[
 F(d)=F(dk)-F(k)=1-1=0.
\]
\(\square\)

There is a stronger form which costs no extra work.

### Lemma 2 (chain form)

If \(F(d)\neq0\), then
\[
 m\geq \left\lfloor\frac Nd\right\rfloor.
\]
Consequently \(F(d)=0\) whenever \(\lfloor N/d\rfloor>m\).

### Proof

Partition \([N]\) into the \(d\)-adic chains
\[
 r,rd,rd^2,\ldots ,\qquad d\nmid r.
\]
Along such a chain the values are \(F(r)+jF(d)\), which are pairwise
distinct because the target group is torsion-free and \(F(d)\neq0\).
Hence a chain contains at most one member of the level \(A\).  The number
of chains is the number of \(r\leq N\) not divisible by \(d\), namely
\(N-\lfloor N/d\rfloor\).  Therefore
\[
 |A|\leq N-\left\lfloor\frac Nd\right\rfloor,
\]
which is the claim. \(\square\)

Thus a hypothetical level with \(m=o(N)\) forces \(F(d)=0\) for every
\(d\leq (1-o(1))N/m\).  In a nonnegative positional construction, all
digits of every such prime must vanish individually.

## 2. Exact mixed-radix carry equations

Let \(Q_0=1\) and
\[
 Q_j=b_1b_2\cdots b_j\qquad (b_j\geq2).
\]
Write a nonnegative positional weight as
\[
 w_p=z_p+\sum_{j=1}^J\frac{d_j(p)}{Q_j},
 \qquad z_p\in\mathbb Z_{\geq0},\quad 0\leq d_j(p)<b_j.
\]
For \(n\), put
\[
 Z(n)=\sum_pv_p(n)z_p,
 \qquad S_j(n)=\sum_pv_p(n)d_j(p).
\]
Starting with \(c_J=0\), descend from \(j=J\) to \(j=1\) and write
uniquely
\[
 S_j(n)+c_j=r_j+b_jc_{j-1},
 \qquad 0\leq r_j<b_j.
\]

### Lemma 3 (carry identity)

For \(F(n)=\sum_pv_p(n)w_p\),
\[
 F(n)=Z(n)+c_0+\sum_{j=1}^J\frac{r_j}{Q_j}.
\]
In particular, \(F(n)=1\) implies
\[
 r_j=0\quad(1\leq j\leq J),
 \qquad Z(n)+c_0=1.
\]

### Proof

The recurrence replaces \(b_j\) units of size \(1/Q_j\) by one unit of
size \(1/Q_{j-1}\).  Applying it successively from the finest position to
the coarsest gives the displayed identity.  The final assertion follows
from uniqueness of the canonical mixed-radix expansion and
nonnegativity. \(\square\)

Hence every target-level integer must satisfy, at every position,
\[
 S_j(n)+c_j\equiv0\pmod {b_j}.
\]
There is no contextual choice of carry.  For example, if at some position
one knows \(0\leq S_j(n)+c_j<b_j\), then a level point must have
\(S_j(n)+c_j=0\), not merely a small positive load.  Together with Lemma
2, this says that a nonnegative carry construction cannot use small primes
as latent context-dependent triggers: their entire positional weight is
forced to be zero.

## 3. The missing-tail identity

Let \(x_p\geq0\) be prime data extended additively by
\(X(n)=\sum_pv_p(n)x_p\).  For \(h>0\), define
\[
 c_p=\left\lfloor\frac{x_p}{h}\right\rfloor,
 \qquad \theta_p=\left\{\frac{x_p}{h}\right\},
\]
and
\[
 C_h(n)=\sum_pv_p(n)c_p,
 \qquad \Theta_h(n)=\sum_pv_p(n)\theta_p.
\]

### Lemma 4 (missing-tail identity)

For every \(n\),
\[
 C_h(n)
 =\left\lfloor\frac{X(n)}h\right\rfloor
  -\lfloor\Theta_h(n)\rfloor.
\]
Consequently, if \(X(n)\leq X\) and \(K=\lfloor X/h\rfloor\), then
\[
 C_h(n)=K
 \quad\Longleftrightarrow\quad
 \left\lfloor\frac{X(n)}h\right\rfloor=K
 \ \text{and}\ \Theta_h(n)<1.
\]

### Proof

The equality
\[
 \frac{X(n)}h=C_h(n)+\Theta_h(n)
\]
has an integer first term.  Taking floors proves the identity.  Since
\(X(n)\leq X\), its first floor is at most \(K\), and the equivalence
follows. \(\square\)

For \(x_p=\log p\), \(X=\log N\), this becomes the exact description
\[
 \{n\leq N:C_h(n)=K\}
 =\left\{e^{Kh}\leq n\leq N:
   \sum_pv_p(n)\left\{\frac{\log p}{h}\right\}<1\right\}.
\]
Changing the base in which the integers \(c_p\) are stored changes only
the bookkeeping of their carries; it cannot recover the omitted
fractional tail.

There is also a useful under-quantizer version.  If integers \(q_p\) obey
\(0\leq q_p\leq\log p/h\), put
\[
 \rho_p=\frac{\log p}{h}-q_p\geq0,
 \qquad Q(n)=\sum_pv_p(n)q_p.
\]
If \(K=\lfloor\log N/h\rfloor\), then
\[
 Q(n)=K,\ n\leq N
 \quad\Longrightarrow\quad
 0\leq\sum_pv_p(n)\rho_p<1.
\]
Thus, for
\(P_\eta=\{p:\rho_p\geq\eta\}\), a level point has at most
\(\lceil1/\eta\rceil-1\) prime factors from \(P_\eta\), counted with
multiplicity.  Any such set with substantial harmonic mass gives a direct
sieve or moment obstruction.

## 4. A quantitative obstruction for floor-log codes

For \(N\geq2\), \(h>0\), and
\[
 K=\left\lfloor\frac{\log N}{h}\right\rfloor\geq1,
\]
let
\[
 C_h(n)=\sum_pv_p(n)\left\lfloor\frac{\log p}{h}\right\rfloor,
 \qquad L(N,h)=\{n\leq N:C_h(n)=K\}.
\]

### Theorem 5

There is no sequence \(N\to\infty\), with arbitrary accompanying
\(h=h_N\), for which
\[
 \frac{|L(N,h)|}{N}\longrightarrow1.
\]
More precisely:

- if \(h\to\infty\) and \(K\to\infty\), then \(|L(N,h)|/N\to0\);
- if \(h\to\infty\) and \(K=1\), then
  \(|L(N,h)|/N\leq\log2+o(1)\);
- if \(h\to\infty\) and \(K=k\geq2\) is fixed, the complement has a
  positive lower density depending only on \(k\).

### Proof

Suppose first that \(h\) stays bounded along a subsequence, say \(h\leq H\).
Choose a fixed prime \(p>e^H\).  Then \(C_h(p)\neq0\), so Lemma 2 applied
to the level \(C_h(n)=K\) gives a deletion fraction at least
\(1/p-o(1)\).  Therefore a density-one sequence would have to satisfy
\(h\to\infty\).

Assume next that \(K\to\infty\).  Let \(P\) be the union, over integers
\(j\geq0\) satisfying \((j+1)h\leq(\log N)/2\), of the prime intervals
\[
 e^{(j+1/2)h}<p\leq e^{(j+1)h}.
\]
Every \(p\in P\) is at most \(\sqrt N\) and has
\(\{\log p/h\}\geq1/2\).  The prime number theorem and partial summation
give
\[
 H_P:=\sum_{p\in P}\frac1p
 =\sum_{j\leq(1/2+o(1))K}
   \log\frac{j+1}{j+1/2}+o(\log K)
 =\left(\frac12+o(1)\right)\log K.
\]
In particular, \(H_P\to\infty\).

For uniformly chosen \(n\leq N\), put
\[
 Z(n)=\sum_{p\in P}1_{p\mid n}.
\]
Using
\(\lfloor N/p\rfloor=N/p+O(1)\) and
\(\lfloor N/(pq)\rfloor=N/(pq)+O(1)\), one obtains
\[
 \mathbb EZ=H_P+o(1),
 \qquad \operatorname{Var}Z\leq H_P+o(H_P).
\]
Indeed, all distinct products \(pq\) are at most \(N\), and the total
floor error is
\[
 O\left(\frac{\pi(\sqrt N)^2}{N}\right)=O\left(\frac1{\log^2N}\right).
\]
Chebyshev's inequality now gives \(\mathbb P(Z\leq1)=o(1)\).  But Lemma 4
says that a point of \(L(N,h)\) has total tail below one, hence has
\(Z\leq1\).  Thus \(|L(N,h)|/N=o(1)\).

It remains to treat bounded \(K\).  Pass to a subsequence on which
\(K=k\) is fixed.  If \(k\geq2\), take
\[
 P=\{p:e^{h/2}<p\leq e^{3h/4}\}.
\]
Then
\[
 H_P\longrightarrow\log(3/2).
\]
Also every pair product is at most \(N\), and
\[
 \mathbb E\binom Z2\longrightarrow\frac{H_P^2}{2}>0.
\]
Here the accumulated floor error is
\[
 O\left(\frac{|P|^2}{N}\right)
 =O\left(\frac{e^{3h/2}}{h^2e^{kh}}ight)=o(1).
\]
Since each selected prime exceeds \(e^{h/2}\) and
\(N<e^{(k+1)h}\), one always has \(Z\leq2(k+1)\).  Therefore
\[
 \mathbb P(Z\geq2)
 \geq
 \frac{\mathbb E\binom Z2}{\binom{2(k+1)}2}
 \geq c_k>0
\]
for all sufficiently large \(N\).  Every integer counted here has tail at
least one and hence lies outside \(L(N,h)\).

Finally suppose \(k=1\).  A point of the level must be divisible by some
prime \(p\geq e^h\).  Since \(N<e^{2h}\), there cannot be two such prime
factors.  The union bound and Mertens' theorem give
\[
 \frac{|L(N,h)|}{N}
 \leq\sum_{e^h\leq p\leq N}\frac1p+o(1)
 =\log\frac{\log N}{h}+o(1)
 \leq\log2+o(1).
\]
These cases exclude every possible density-one sequence. \(\square\)

## Limitations and next test

Theorem 5 concerns the top target \(K=\lfloor\log N/h\rfloor\).  For a
shifted target \(T\), the tail budget is approximately
\((\log N)/h-T\), so the same two-prime argument alone need not apply.  A
plausible next obstruction is modular anti-concentration: for
\(K\to\infty\), the completely multiplicative function
\[
 (-1)^{C_h(n)}
\]
should have mean \(o(1)\) by a quantitative Halász estimate, because its
prime signs alternate on successive logarithmic bands.  That would bound
every exact level by \(1/2+o(1)\), including shifted targets.  This
Halász step is not proved here and is not used in any result above.

