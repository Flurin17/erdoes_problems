# Route: exact covering frontier and prime-gap lower bounds

## Status and mechanism

This route is rigorous as a **lower-bound route**, but it does not determine the
sharp scale of \(n_k\).  Its mechanism is to express all forbidden integers as
integer intervals
\[
  C_{p,q}:=[qp+1,qp+k]\cap\mathbb Z
  \qquad(k<p<2k,\ q\geq1),
\]
and then prove that many such intervals stitch into one initial covered
frontier.  The dilation by \(q\) of gaps between consecutive primes is the
quantity that limits this method.

Throughout, \(k\) is a positive integer and
\[
 \mathcal P_k=\{p:p\text{ is prime},\ k<p<2k\}.
\]
For \(k\geq2\), Bertrand's postulate gives \(\mathcal P_k\ne\varnothing\).
For \(k=1\), the set is empty and directly \(n_1=3\).

## 1. Exact covering and quotient formulations

### Lemma 1 (covering intervals)

An integer \(n>2k\) is forbidden if and only if
\[
 n\in\bigcup_{p\in\mathcal P_k}\bigcup_{q\geq1}C_{p,q}.
\]
Equivalently, it is forbidden if and only if there is an integer \(q\geq1\)
such that the **closed** real interval
\[
  \left[\frac{n-k}{q},\frac{n-1}{q}\right]
\]
contains a prime in \((k,2k)\).

#### Proof

The prime \(p\) divides one of \(n-k,\ldots,n-1\) precisely when
\(n-k\leq qp\leq n-1\) for some positive integer \(q\).  Rearranging gives
\(qp+1\leq n\leq qp+k\), and division by \(q\) gives the quotient version.
The lower endpoint in the quotient interval is closed: equality
\(qp=n-k\) is forbidden. \(\square\)

Writing \(n=2k+m\), the same assertion becomes
\[
 m\in B_{p,q}:=[qp-2k+1,qp-k]\cap\mathbb Z_{>0}.
\]
Thus \(n_k-2k\) is exactly the first positive integer outside the union of
the interval streams \(B_{p,q}\).

## 2. Exact first block \((2k,3k]\)

Write each \(p\in\mathcal P_k\) as \(p=k+r\), and put
\[
 r_{\min}=\min_{p\in\mathcal P_k}(p-k),\qquad
 r_{\max}=\max_{p\in\mathcal P_k}(p-k).
\]

### Lemma 2 (exact initial dichotomy)

For \(1\leq m\leq k\), the prime \(p=k+r\) is avoided by
\([k+m,2k+m-1]\) if and only if
\[
 r+1\leq m\leq2r.
\]
Consequently,
\[
 r_{\max}+1\leq2r_{\min}
 \quad\Longrightarrow\quad
 n_k=2k+r_{\max}+1,
\]
whereas if this inequality fails then \(n_k>3k\).

#### Proof

For \(1\leq m\leq k\), the only possible positive multiples of
\(p\in(k,2k)\) in \([k+m,2k+m-1]\) are \(p\) and \(2p\).  The first occurs
exactly when \(m\leq r\), and the second occurs exactly when
\(m\geq2r+1\).  Hence \(p\) is avoided exactly on
\([r+1,2r]\cap\mathbb Z\).  All primes are avoided simultaneously exactly
when
\[
 m\in[r_{\max}+1,2r_{\min}]\cap\mathbb Z.
\]
If this interval is nonempty, its first member gives the displayed exact
value; if it is empty, every \(1\leq m\leq k\) is forbidden. \(\square\)

This lemma is also an endpoint check on any more general covering argument.

## 3. Exact layer-stitching theorem

List
\[
 k<p_1<\cdots<p_s<2k
\]
and, when \(s\geq2\), define
\[
 G=\max_{1\leq i<s}(p_{i+1}-p_i),\quad
 a=p_1-k,\quad b=2k-p_s,\quad W=p_s-p_1=k-a-b.
\]

### Lemma 3 (one layer)

For a fixed \(q\geq1\), if \(qG\leq k\), then
\[
 \bigcup_{i=1}^s C_{p_i,q}=[qp_1+1,qp_s+k]\cap\mathbb Z.
\]

#### Proof

The right endpoint of \(C_{p_i,q}\) is \(qp_i+k\), while the next left
endpoint is \(qp_{i+1}+1\).  There is no missing integer between them exactly
when
\[
 qp_{i+1}+1\leq qp_i+k+1,
\]
which is equivalent to \(q(p_{i+1}-p_i)\leq k\).  Notice that equality gives
adjacent integer intervals; actual real overlap is not needed. \(\square\)

### Lemma 4 (successive layers)

Assume the conclusion of Lemma 3 for layers \(q\) and \(q+1\).  These layers
have no missing integer between them exactly when
\[
 a\leq qW.
\]

#### Proof

The condition is
\[
 (q+1)p_1+1\leq qp_s+k+1,
\]
which rearranges to \(p_1-k\leq q(p_s-p_1)\). \(\square\)

### Theorem 5 (exact covered frontier)

Suppose \(s\geq2\), \(a\leq W\), and put \(Q=\lfloor k/G\rfloor\).  Then
\[
 \bigcup_{q=1}^{Q}\bigcup_{i=1}^s C_{p_i,q}
   =[p_1+1,Qp_s+k]\cap\mathbb Z,
\]
and in particular
\[
 \boxed{\ n_k\geq Qp_s+k+1.\ }
\]

#### Proof

For every \(q\leq Q\), \(qG\leq k\), so Lemma 3 makes the \(q\)-th layer
an interval.  Since \(a\leq W\leq qW\), Lemma 4 stitches every pair of
successive layers.  The union is therefore the stated interval.  Its left
endpoint is below \(2k+1\), so every candidate \(2k<n\leq Qp_s+k\) is
forbidden. \(\square\)

The hypotheses are close to minimal for this precise argument: internal
continuity requires \(QG\leq k\), while stitching at the first transition
requires \(a\leq W\), equivalently \(2a+b\leq k\).

Define the augmented maximum gap
\[
 \Delta_k=\max\{a,b,G\}.
\]
If \(3\Delta_k\leq k\), then
\(W=k-a-b\geq k-2\Delta_k\geq\Delta_k\geq a\), so Theorem 5 applies.  In
particular, whenever \(\Delta_k=o(k)\),
\[
 n_k\geq(2+o(1))\frac{k^2}{G},
\]
because \(p_s=(2-o(1))k\) and \(\lfloor k/G\rfloor=(1+o(1))k/G\).

## 4. PNT consequences

### Precisely stated imported theorem

We use the following standard effective prime number theorem as an imported
dependency: there are absolute constants \(A,c>0\) and \(x_0\) such that,
for all real \(x\geq x_0\),
\[
 \left|\vartheta(x)-x\right|
 \leq A x\exp(-c\sqrt{\log x}),
 \qquad \vartheta(x)=\sum_{p\leq x}\log p.
\]
No numerical values of \(A,c,x_0\) are asserted here.

### Lemma 6 (effective short interval consequence)

For all sufficiently large \(k\), put
\[
 H(k)=8Ak\exp(-c\sqrt{\log k}).
\]
Every \(x\in[k,2k]\) for which \(x+H(k)\leq2k\) has a prime in
\((x,x+H(k)]\), and \(\Delta_k\leq H(k)\).

#### Proof

Let \(E(x)=\exp(-c\sqrt{\log x})\) and
\(h=4AxE(x)\).  For sufficiently large \(x\), \(h\leq x\).  Since \(E\)
is decreasing,
\[
\begin{aligned}
 \vartheta(x+h)-\vartheta(x)
 &\geq h-A(x+h)E(x+h)-AxE(x)\\
 &\geq 4AxE(x)-2AxE(x)-AxE(x)>0.
\end{aligned}
\]
Thus \((x,x+h]\) contains a prime.  For \(k\leq x\leq2k\),
\(h\leq8AkE(k)=H(k)\), proving the first assertion.

Taking \(x=k\) bounds \(p_1-k\).  Taking \(x=p_i\) bounds every next-prime
gap that ends before \(2k\).  Finally, if \(2k-p_s>H(k)\), taking
\(x=2k-H(k)\) supplies a prime strictly larger than \(p_s\) and at most
\(2k\); equality with \(2k\) is impossible for \(k>1\).  This contradiction
bounds the terminal gap.  Hence \(\Delta_k\leq H(k)\). \(\square\)

### Corollary 7 (strongest unconditional claim on this route)

For some absolute \(c>0\),
\[
 \boxed{\ n_k\gg k\exp(c\sqrt{\log k})\ }.
\]
More explicitly, with the constants in the imported theorem, for all
sufficiently large \(k\),
\[
 n_k\geq
 \left\lfloor\frac{k}{H(k)}\right\rfloor(2k-H(k))+k+1,
\]
and therefore, after increasing the threshold if necessary,
\[
 n_k\geq \frac1{5A}k\exp(c\sqrt{\log k}).
\]

#### Proof

Lemma 6 gives \(G\leq H(k)\), \(p_s\geq2k-H(k)\), and, since
\(H(k)=o(k)\), the stitching hypothesis \(a\leq W\) for all sufficiently
large \(k\).  Apply Theorem 5 and use
\(\lfloor k/G\rfloor\geq\lfloor k/H(k)\rfloor\).  The final displayed bound
follows from the definition of \(H(k)\) and the fact that its leading
coefficient tends to \(1/(4A)\). \(\square\)

In particular \(n_k/k\to\infty\).  Bare PNT also proves
\(\Delta_k=o(k)\), by partitioning \([k,2k]\) into finitely many fixed
relative-length intervals and applying PNT in each, but it gives neither
\(G=O(\log k)\) nor a sharp scale.

## 5. Independent quotient-gap cross-check

The following weaker formulation is useful for falsifying endpoint mistakes.
If every open subinterval of \((k,2k)\) of length greater than \(\Delta_k\)
contains a prime, let \(Q=\lceil k/\Delta_k\rceil\).  Provided
\(\Delta_k<(k+1)/3\), Lemma 2 gives \(n_k>3k\).  For
\(n=qk+s\), \(3\leq q\leq Q\), \(0\leq s<k\), choose \(j=q-1\).  Then
\[
 \left(\frac{n-k}{j},\frac n j\right)
 =\left(k+\frac{s}{j},k+\frac{s}{j}+\frac{k}{j}\right)
 \subset(k,2k)
\]
(with open left endpoint \(k\) when \(s=0\)), and its length
\(k/j>\Delta_k\).  A prime in this interval has
\(jp\in[n-k,n-1]\), so \(n\) is forbidden.  Thus
\[
 n_k\geq(Q+1)k.
\]
This proves the same qualitative superlinearity without layer stitching,
though with a weaker constant under the effective PNT input.

## 6. Exact computational frontier

The shifted intervals \(B_{p,q}\) form one increasing stream for every
prime \(p\in\mathcal P_k\).  An exact deterministic heap sweep is:

1. Sieve the primes in \((k,2k)\).
2. For each prime, place its first interval
   \((L,R,q)=(p-2k+1,p-k,1)\), truncated to positive integers, in a heap
   ordered by \(L\).
3. Maintain a frontier \(F\) such that processed intervals cover every
   integer in \([1,F]\).
4. Pop the least \(L\).  If \(L>F+1\), return \(n_k=2k+F+1\).  Otherwise set
   \(F=\max(F,R)\) and push the next interval in that prime's stream.

The invariant is that the heap contains the least unprocessed interval of
each stream and all processed intervals cover \([1,F]\).  At termination,
\(F+1\) is absent from every stream, while all smaller positive shifts are
covered.  Termination follows, for example, because a positive multiple of
\(\prod_{p\in\mathcal P_k}p\) is admissible.  Retaining only intervals that
extend \(F\) gives a compact exact lower-frontier certificate.  An independent
verifier should check both the returned admissible residues and coverage of
every earlier shift; no numerical table is claimed in this route file without
such a recorded run.

## 7. Objections, repairs, and falsification tests

1. **Average gap substituted for maximum gap.**  The average prime gap is
   irrelevant to Lemma 3; a single gap \(d\) dilates to \(qd\).  Repair:
   retain the actual maximum \(G\), or state a genuine uniform gap theorem.
2. **Internal continuity confused with global coverage.**  Even if each layer
   is an interval, consecutive layers may not meet.  For \(k=8\), primes are
   \(11,13\); the first layers are \([12,21]\) and \([23,34]\), leaving
   \(22\) admissible.  Repair: require \(a\leq W\).
3. **Ceiling used in the layer count.**  The correct safe count is
   \(Q=\lfloor k/G\rfloor\).  For \(k=10\), the gap \(13\to17\) dilates to
   \(12>10\) at \(q=3\), so replacing the floor by a ceiling creates holes.
4. **Real overlap demanded at equality.**  When \(qG=k\), the integer
   intervals are adjacent and there is no missing integer.  Lemma 3 therefore
   correctly uses \(\leq\), not \(<\).
5. **Wrong quotient length.**  The closed quotient interval in Lemma 1 has
   length \((k-1)/q\), not \(k/q\).  Section 5 deliberately uses the smaller
   open interval \(((n-k)/q,n/q)\), whose length is \(k/q\), and finds a prime
   strictly below \(n/q\).
6. **Overclaim from PNT.**  PNT yields \(G=o(k)\), not
   \(G=O(\log k)\).  The effective bound above is only
   \(G\ll k\exp(-c\sqrt{\log k})\).

Concrete automated falsification tests should:

- enumerate all primes in \((k,2k)\), compare Lemma 2 with direct divisibility
  for every \(1\leq m\leq k\), and check both sides of its dichotomy;
- for every layer \(q\leq\lfloor k/G\rfloor\), compare the predicted interval
  with the literal union of \(C_{p,q}\);
- verify that the layer transition has no hole exactly when \(a\leq qW\);
- compare the heap frontier against brute-force residue testing for small
  \(k\).

## 8. Dependency graph and open bottleneck

The proved chain is
\[
\text{product condition}
\Rightarrow\text{covering intervals (Lemma 1)}
\Rightarrow\text{layer continuity and stitching (Lemmas 3--4)}
\Rightarrow\text{exact frontier (Theorem 5)}
\Rightarrow\text{effective-PNT gap bound (Lemma 6)}
\Rightarrow n_k\gg k e^{c\sqrt{\log k}}.
\]
All arrows except the stated effective PNT are proved in this file.

The exact density of admissible residue classes over a full CRT period is
\[
 \rho_k=\prod_{k<p<2k}\left(1-\frac{k}{p}\right),
\]
and PNT partial summation heuristically gives
\[
 \log\rho_k\sim-2\log2\,\frac{k}{\log k}.
\]
Thus the reciprocal-density heuristic scale is
\(\exp((2\log2+o(1))k/\log k)\), far beyond the prime-gap lower bound.
This heuristic is not a localization theorem.

**Open bottleneck.**  Prime-gap covering gives no matching upper bound and
cannot by itself locate the first admissible residue box.  The next required
lemma is an anchored localization result showing that some admissible residue
occurs in a controlled initial interval (or, alternatively, a new covering
mechanism that produces an exponential-scale lower frontier).  Positive
density over the full CRT period does not supply either conclusion.
