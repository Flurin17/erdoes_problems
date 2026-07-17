# Rational and primitive-set route

## Outcome

This route gives a dependency-complete proof for every admissible set contained
in one fixed integral lattice \(c\mathbb N\).  It also gives an exact finite
reduction of the general real problem to a uniform estimate for
\(Q\)-thick primitive integer sets.  It does **not** solve the general problem:

1. a rational-commensurability class need not be contained in any
   (c\mathbb N), even when it is itself an infinite admissible set; and
2. convergence on each of countably many cyclic classes gives no summable
   budget over the classes.

The first unsupported assertion that a classwise proof would need is therefore
not a primitive-set estimate, but a genuinely cross-scale estimate.

## 1. Exact common-lattice theorem

### Theorem 1 (fixed integral lattice)

Let (c>0), let (S\subseteq\mathbb N), and suppose

\[
 A=cS=\{cn:n\in S\}\subset(1,\infty).
\]

The condition in Problem 143 is exactly

\[
 |km-n|\ge h:=\left\lceil\frac1c\right\rceil
 \tag{1}
\]

for all ordered pairs of distinct (m,n\in S) and all integers (k\ge1).
It implies that (S) is primitive (no distinct member divides another).  If
(c\ge1), it is equivalent to primitivity.  If (A) is countably infinite and
admissible, then

\[
 \sum_{x\in A}\frac1{x\log x}<\infty
 \quad\hbox{and}\quad
 \sum_{\substack{x<N\\x\in A}}\frac1x=o(\log N).
 \tag{2}
\]

#### Exact translation, orientations, and endpoints

For (x=cm,y=cn),

\[
 |kx-y|=c|km-n|.
\]

The quantity (|km-n|) is an integer, so (c|km-n|\ge1) is equivalent
to (1).  The universal quantifier over distinct (x,y) supplies both ordered
orientations; no symmetry is being silently added.  If (n=km), the left
side is zero, proving primitivity.  Conversely, if (c\ge1), primitivity
makes (km-n) a nonzero integer, and hence (c|km-n|\ge c\ge1).  Equality
is allowed.  When (c<1), primitivity alone is not sufficient; for example,
(c=0.6) and (S=\{2,3\}) fail at (k=1).

It remains to prove the weighted assertion about primitive integer sets.

### Lemma 2 (primitive weighted estimate)

For every primitive (S\subseteq\{2,3,\ldots\}),

\[
 \sum_{a\in S}\frac1{a\log a}<\infty.
 \tag{3}
\]

In fact, the sum is bounded by an absolute constant.

#### Rough-multiple sets are disjoint

For (a\ge2), write (P(a)) for its largest prime factor and define

\[
 \mathcal M_a=\{au:u\in\mathbb N,
       \text{ every prime factor of }u\text{ is at least }P(a)\}.
\]

We claim that the sets (\mathcal M_a), (a\in S), are pairwise disjoint.
Suppose (N=au=bv) and (P(a)\le P(b)).  If (P(a)<P(b)), then (v) has
no prime factor (q<P(b)), whence

\[
 \nu_q(N)=\nu_q(b)\qquad(q<P(b)).
\]

Every prime factor of (a) is below (P(b)), and
(\nu_q(a)\le\nu_q(N)), so (a\mid b), contrary to primitivity.  If
(P(a)=P(b)=P), neither multiplier has a prime factor below (P).  Hence
(\nu_q(a)=\nu_q(b)) for every (q<P); the two integers can differ only in
their exponent of (P), so one divides the other.  This is again impossible.

#### Density inequality

Let (Q_a=\prod_{p<P(a)}p).  Finite inclusion-exclusion gives

\[
 d(\mathcal M_a)
 =\frac1a\prod_{p<P(a)}\left(1-\frac1p\right).
 \tag{4}
\]

Indeed, the number of (u\le Y) coprime to (Q_a) is

\[
 Y\prod_{p<P(a)}\left(1-\frac1p\right)+O(2^{\pi(P(a))}),
\]

where the error is harmless because (a) is fixed while the density limit is
taken.  For every finite (F\subseteq S), disjointness and (4) imply

\[
 \sum_{a\in F}\frac1a
  \prod_{p<P(a)}\left(1-\frac1p\right)\le1.
 \tag{5}
\]

#### Elementary finite-product estimate

There is an absolute (C) such that for all (z\ge2),

\[
 \prod_{p\le z}\left(1-\frac1p\right)^{-1}\le C\log z.
 \tag{6}
\]

Here is a proof, included so that no external primitive-set theorem or prime
number theorem is being imported.  Put
(\vartheta(t)=\sum_{p\le t}\log p).  For every integer (m\ge1),

\[
 \prod_{m<p\le2m}p\mid {2m\choose m}
 \quad\hbox{and}\quad {2m\choose m}\le4^m,
\]

so

\[
 \vartheta(2m)-\vartheta(m)\le2m\log2.
\]

Summing this estimate over dyadic intervals (rounding their endpoints only
changes the absolute constant) gives

\[
 \vartheta(t)\le C_0t\qquad(t\ge2).
 \tag{7}
\]

Partial summation therefore gives

\[
 \sum_{p\le z}\frac{\log p}{p}
 =\frac{\vartheta(z)}z+\int_2^z\frac{\vartheta(t)}{t^2}\,dt
 \le C_0(1+\log z).
 \tag{8}
\]

Take (\delta=1/\log z) and (s=1+\delta).  Unique factorization and the
integral test yield

\[
 \prod_{p\le z}(1-p^{-s})^{-1}
 \le\sum_{n\ge1}n^{-s}
 \le1+\int_1^\infty t^{-s}\,dt
 =1+\log z.
 \tag{9}
\]

Moreover, using (\log(1+u)\le u), (1-e^{-v}\le v), and
((p-1)^{-1}\le2/p),

\[
\begin{aligned}
 \log\prod_{p\le z}\frac{1-p^{-s}}{1-p^{-1}}
 &\le \sum_{p\le z}\frac{1-p^{-\delta}}{p-1}\\
 &\le 2\delta\sum_{p\le z}\frac{\log p}{p}=O(1)
\end{aligned}
\]

by (8).  Combining this with (9) proves (6), after enlarging the constant for
bounded (z).

Since (P(a)\le a), (6) implies

\[
 \prod_{p<P(a)}\left(1-\frac1p\right)
 \ge\frac1{C\log P(a)}\ge\frac1{C\log a}.
\]

Substitution in (5), followed by exhaustion of (S) by finite subsets, proves
(3).

#### Completion of Theorem 1

If (c\ge1), then (\log(cn)\ge\log n).  If (0<c<1), then for
(n\ge c^{-2}),

\[
 \log(cn)=\log n+\log c\ge\tfrac12\log n.
\]

There are only finitely many smaller (n), and (cn>1) makes every relevant
logarithm positive.  Thus Lemma 2 gives

\[
 \sum_{n\in S}\frac1{cn\log(cn)}<\infty.
\]

Finally, for any locally finite (B\subset(1,\infty)), convergence of this
weighted series implies the harmonic little-oh conclusion.  For fixed (R>1),

\[
 \frac1{\log N}\sum_{\substack{x<N\\x\in B}}\frac1x
 \le
 \frac1{\log N}\sum_{\substack{x<R\\x\in B}}\frac1x
 +\sum_{\substack{R\le x<N\\x\in B}}\frac1{x\log x}.
\]

First let (N\to\infty), then (R\to\infty).  Admissibility supplies local
finiteness because its (k=1) instance makes the set (1)-separated.  This
proves Theorem 1.

## 2. Why rational commensurability does not finish the problem

Define (x\sim y) when (x/y\in\mathbb Q).  A finite subset of one class can
be put into some (c\mathbb N) by clearing denominators.  The same need not be
true of an infinite class, and the failure can occur under the full
admissibility hypothesis.

### Proposition 3 (an admissible noncyclic rational class)

There is a countably infinite admissible (A\subset\mathbb Q\cap(1,\infty))
such that no (c>0) satisfies (A\subset c\mathbb N).

#### Proof

Set \(x_1=8\).  Inductively maintain rational admissible
\(x_1,\ldots,x_r\), with the reduced denominators of
\(x_2,\ldots,x_r\) distinct primes, and

\[
 \sum_{i\le r}\frac1{x_i}<\frac14.
\]

The later points can be required to exceed any prescribed rapidly growing
sequence, so the reciprocal bound can be maintained (for example, allot the
((r+1))-st new point a reciprocal budget (2^{-r-4})).

Choose (T>\max_i x_i+1), (T>12r), and large enough for that reciprocal
budget.  In ([T,2T]), the forbidden intervals coming from (x_i) have total
length at most

\[
 \left|\bigcup_{k\ge1}(kx_i-1,kx_i+1)\cap[T,2T]\right|
 \le2\left(\frac{T}{x_i}+3\right).
\]

Consequently the union over (i\le r) has length at most

\[
 2T\sum_{i\le r}\frac1{x_i}+6r<T.
\]

Only finitely many intervals meet ([T,2T]), so their complement contains a
nondegenerate interval.  Choose inside it a rational (y=m/q) in lowest terms,
where (q) is a new prime.  This is possible by taking a new prime (q) so
large that the (1/q)-grid has at least two points in the complementary
interval and choosing a numerator not divisible by (q).

Then (|kx_i-y|\ge1) for every (i,k).  In the reverse orientation,
(ky-x_i\ge y-x_i>1) for every (k\ge1).  Thus adjoining (y) preserves
admissibility, and iteration constructs (A).  All its elements are rational,
so it is one commensurability class.

If (A\subset c\mathbb N), the relation (8\in c\mathbb N) makes (c=u/v)
rational in lowest terms.  If (m/q\in c\mathbb N), with (q\nmid m), then

\[
 \frac{mv}{qu}\in\mathbb N,
\]

so (q\mid v).  Infinitely many distinct prime denominators cannot all divide
the fixed integer (v), a contradiction.

Thus the instruction “apply the primitive theorem on each rational ray” fails
before any summation is attempted.  Even when all classes are cyclic, merely
knowing a convergent sum on each of countably many classes does not control the
sum of their (unquantified) finite constants.

### Proposition 4 (singleton-ray finite obstruction)

For an integer (N\ge4), set (\alpha=\sqrt2),
(m=\lfloor(N-1)/\alpha\rfloor), and

\[
 F_N=\{N+j\alpha:0\le j\le m\}.
\]

Then (F_N\subset[N,2N-1]) is admissible, no two of its elements are rationally
commensurable, and

\[
 \sum_{x\in F_N}\frac1x\ge\frac{m+1}{2N},
 \qquad
 \sum_{x\in F_N}\frac1{x\log x}
 \ge\frac{m+1}{2N\log(2N)}.
 \tag{10}
\]

For (k=1), distinct points differ by at least (\sqrt2>1).  For (k\ge2)
and any (x,y\in F_N),

\[
 kx-y\ge2N-(2N-1)=1.
\]

If ((N+i\alpha)/(N+j\alpha)=r\in\mathbb Q), linear independence of
(1,\sqrt2) over (\mathbb Q) gives (N=rN) and (i=rj), hence (r=1)
and (i=j).  The bounds (10) are immediate.  In particular, classwise
information can be vacuous on a block having order-one harmonic mass.  What
remains is precisely the interaction between different scales.

## 3. A useful finite reduction for the general real problem

The failure of commensurability-class decomposition does not prevent a finite
common-denominator reduction.

### Lemma 5 (finite rationalization with admissibility preserved)

Every finite real admissible configuration (F\subset(1,\infty)) can be
approximated arbitrarily closely, coordinate by coordinate, by an admissible
configuration of rational numbers having one common denominator.

#### Proof

Write (F=\{x_1,\ldots,x_r\}), (a=\min F), (b=\max F), and fix
(\eta>0).  Choose (s>1) so close to (1) that
((s-1)b<\eta/2).  Dilation creates the uniform margin

\[
 |ksx_i-sx_j|\ge s>1.
\]

Choose an integer (K) with ((K+1)sa-sb>2), and then choose (\rho>0)
so small that

\[
 (K+1)\rho<s-1,
 \quad (K+1)(sa-\rho)-(sb+\rho)>1,
 \quad \rho<\eta/2,
 \quad \rho<sa-1.
\]

Pick rational (q_i) with (|q_i-sx_i|<\rho).  For (1\le k\le K),

\[
 |kq_i-q_j|
 \ge |ksx_i-sx_j|-(k+1)\rho>1.
\]

For (k\ge K+1),

\[
 kq_i-q_j\ge(K+1)(sa-\rho)-(sb+\rho)>1.
\]

Thus (G=\{q_i}) is admissible, each (q_i>1), and

\[
 |q_i-x_i|\le\rho+(s-1)b<\eta.
\]

Clearing denominators gives (q_i=n_i/Q), where (n_i>Q), and the exact
integer condition is

\[
 |kn_i-n_j|\ge Q
 \tag{11}
\]

for distinct indices and all (k\ge1).

### Definition 6 and the open uniform estimate

Call a finite (S\subset\mathbb N) (Q)-admissible if (n>Q) for every
(n\in S) and (11) holds for every ordered pair of distinct elements.

Fix (a>1).  The following estimate, uniform in (Q), would prove the first
conclusion of Problem 143:

\[
 \boxed{
 \sum_{n\in S}\frac{Q}{n\log(n/Q)}\le C_a
 }
 \tag{12}
\]

for every finite (Q)-admissible (S\subset[aQ,\infty)).

To verify the implication, an admissible real (A) has a least element: choose
one (x_0\in A); the nonempty set (A\cap(1,x_0]) is finite because (A) is
(1)-separated, and hence has a minimum (m>1).  Choose (1<a<m).  Apply
Lemma 5 to an arbitrary finite (F\subset A), with approximation small enough
to keep every rationalized point above (a).  Estimate (12), followed by a
limit as the approximation tends to zero and continuity of
(x\mapsto1/(x\log x)), bounds the weight of (F) by (C_a).  Exhausting
(A) by finite subsets proves convergence.

Ordinary Lemma 2 loses a factor (Q) here: it bounds
(\sum 1/(n\log n)), whereas (12) asks for weights of order
(Q/(n\log(n/Q))).  Recovering this factor from the thick gaps in (11) is the
exact bottleneck of this reduction.

### Lemma 7 (a partial thick packing inequality)

If (S) is (Q)-admissible, all numbers

\[
 \{2^j n:n\in S, j\ge0\}
\]

are mutually (Q)-separated.  Indeed, if (n\ne m) and (j\ge\ell), then

\[
 |2^j n-2^\ell m|
 =2^\ell|2^{j-\ell}n-m|\ge2^\ell Q\ge Q.
\]

For the same (n), two distinct powers differ by at least (n>Q).  Hence, if

\[
 N_S(X)=|\{n\in S:n\le QX\}|,
\]

one has

\[
 \sum_{j\ge0}N_S(X/2^j)\le X+1.
 \tag{13}
\]

This is a real multiscale packing fact, but it is insufficient: (13) permits
linear-size concentration in the top half of every scale and therefore does
not by itself yield either desired little-oh or convergence assertion.

### Lemma 8 (naive thickening of rough multiples fails)

The exact rough-multiple sets in Lemma 2 cannot simply be replaced by their
\(Q/2\)-neighborhoods.  Take \(Q=2\) and \(S=\{5,8\}\).  This is
\(2\)-admissible: the only nonautomatic checks are

\[
 |8-5|=3,\qquad |8-2\cdot5|=2.
\]

But \(P(5)=5\), so \(25=5\cdot5\in\mathcal M_5\), while \(P(8)=2\), so
\(24=8\cdot3\in\mathcal M_8\).  Their distance is \(1<Q\), and their open
radius-\(Q/2\) neighborhoods overlap.  Thus any successful thick analogue
needs a new selection rule or a proved bounded-overlap estimate; exact
disjointness does not survive thickening.

## 4. Dependency graph and route status

The closed common-lattice branch is

\[
 \text{exact lattice translation}
 \Longrightarrow \text{primitive indices}
 \Longrightarrow \text{disjoint rough multiples}
 \Longrightarrow \text{density inequality (5)}
 \Longrightarrow \text{product estimate (6)}
 \Longrightarrow \text{weighted convergence}
 \Longrightarrow \text{harmonic little-oh}.
\]

Every node in this branch is proved above.

The general branch is

\[
 \text{finite rationalization (proved)}
 \Longrightarrow \text{(Q)-admissible skeleton (proved)}
 \Longrightarrow \boxed{\text{uniform thick estimate (12) (open)}}
 \Longrightarrow \text{weighted convergence}
 \Longrightarrow \text{harmonic little-oh}.
\]

The literal class-decomposition branch is dead: Proposition 3 refutes its
cyclic premise, and Proposition 4 shows that even singleton classes can carry
maximal one-scale mass.

## 5. Falsification tests and next action

1. **Cyclic premise.**  Before writing a class as (cS), check that the
   denominators relative to one anchor have bounded least common multiple.
   Proposition 3 fails this test.
2. **Scale-local decay.**  Any asserted (o(N)) occupancy or vanishing harmonic
   mass in ([N,2N]) is refuted by (F_N).
3. **Uniform thick estimate.**  For fixed (Q,a,X), form the finite graph on
   (n\in[\lceil aQ\rceil,\lfloor XQ\rfloor]), joining (n,m) exactly when
   (|kn-m|<Q) in either orientation for some relevant (k).  Maximize the
   independent-set weight (Q/(n\log(n/Q))).  Growth with (Q) or (X)
   falsifies (12), although not by itself the original infinite assertion.
4. **Block concatenation.**  Every proposed construction must check, for each
   earlier (x), all integers (k) with (kx) in the new block.  Verifying
   only within-block admissibility is invalid.

The next mathematical action is to seek a selected bounded-overlap family
derived from rough multiples with density comparable to
\(Q/(n\log(n/Q))\).  Lemma 8 shows that taking all thickened rough multiples
does not work.  Controlling or pruning those overlaps without losing the
factor \(Q\) is the unresolved repair lemma.  Equivalently, in dyadic notation

\[
 h_j=\sum_{x\in A\cap[2^j,2^{j+1})}\frac1x,
\]

one needs a cross-scale budget.  For example, the stronger estimate

\[
 \sum_{j=2^r}^{2^{r+1}-1}h_j
 \ll\frac{2^r}{r^{1+\delta}}
\]

for some (\delta>0) would suffice for weighted convergence.  No raywise
primitive estimate proved here supplies such a budget.
