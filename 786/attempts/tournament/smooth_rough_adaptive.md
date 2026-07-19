# Adaptive smooth--rough weights: exact constraints and obstructions

## Proposed mechanism

A tempting construction is to expose the largest prime factor \(p\), inspect
the smooth cofactor \(m\), and give \(p\) whatever weight is needed to make
\(f(pm)=1\). One can then recurse on the smooth remainder, in the style of a
Buchstab decomposition. The exact-additivity requirement is much more rigid
than this description suggests: the increment made by \(p\) is the single
number \(w_p=f(p)\), independent of the cofactor. Thus a prime column can be
aligned with **one exact atom** of the cofactor grading, but not with a
cofactor-dependent collection of approximate values. The lemmas below make
this obstruction precise. They also show that a putative density-one grading
must vanish on a growing initial segment, so no fixed smooth-prime stage can
be part of such a construction.

Throughout,

\[
 f(n)=\sum_p w_pv_p(n),\qquad
 A=A_f(1;N)=\{n\leq N:f(n)=1\},\qquad
 E=[N]\setminus A,\quad |E|=m.
\]

The weights may be arbitrary real (or rational) numbers and may depend on
\(N\).

## 1. A prime column is exactly one cofactor atom

**Lemma 1 (column identity).** For every prime \(p\), every \(x\leq N/p\),
and every \(t\),

\[
 \#\{k\leq x:f(pk)=t\}
 =\#\{k\leq x:f(k)=t-w_p\}.
\]

**Proof.** Complete additivity gives \(f(pk)=w_p+f(k)\), including when
\(p\mid k\). This is an equivalence term by term. \(\square\)

In particular, suppose that \(p>\sqrt N\). Then \(k\leq N/p<p\), so \(f(k)\)
does not involve \(w_p\), and two different such primes cannot divide the same
integer at most \(N\). If

\[
 D_f(x)=\max_s\#\{k\leq x:f(k)=s\},
\]

then, after the lower-prime weights have been fixed,

\[
 \max_{w_p}\#\{k\leq N/p:f(pk)=1\}=D_f(N/p).       \tag{1}
\]

Moreover the columns for \(p>\sqrt N\) are disjoint. Hence the best possible
"adaptive compensation" on the large-prime part is exactly

\[
 \sum_{\sqrt N<p\leq N}D_f(N/p),                  \tag{2}
\]

not a sum of approximate or smoothness-conditioned concentrations.

**Corollary 1 (cofactor-dependent markers are not additive).** Suppose an
algorithm assigns a contribution \(c(p,k)\) to the newly exposed prime \(p\)
in a factorization \(pk\), and this contribution is claimed to arise from a
completely additive grading. Then

\[
 c(p,k)=f(pk)-f(k)=w_p
\]

is independent of \(k\). If the algorithm wants every \(pk\), \(k\in B_p\),
to have value \(1\), then \(f\) must be constant, with value \(1-w_p\), on all
of \(B_p\).

Thus a Buchstab stopping rule such as "mark \(p\) only when the remaining
cofactor has property \(Q\)" cannot itself be a completely additive marker.
It is legitimate only if the \(Q\)-class used in that column is already a
single exact \(f\)-atom. This is the first obstruction to the proposed
recursive construction.

## 2. Density one forces an exact zero core

The next observation is elementary but quite restrictive.

**Lemma 2 (zero-core lemma).** If

\[
 f(d)\neq0,
\]

then

\[
 m\geq\left\lfloor\frac Nd\right\rfloor.           \tag{3}
\]

Consequently

\[
 f(d)=0\quad\hbox{for every }d\leq
 Y:=\left\lfloor\frac{N}{m+1}\right\rfloor.        \tag{4}
\]

**Proof.** Partition \([N]\) into the \(d\)-adic chains

\[
 r,dr,d^2r,\ldots\qquad(d\nmid r).
\]

Along such a chain the values form
\(f(r),f(r)+f(d),f(r)+2f(d),\ldots\), so if \(f(d)\neq0\) the level \(1\)
occurs at most once. The number of chains is the number of \(r\leq N\) not
divisible by \(d\), namely \(N-\lfloor N/d\rfloor\). Hence
\(|A|\leq N-\lfloor N/d\rfloor\), proving (3). If
\(d\leq N/(m+1)\), then \(\lfloor N/d\rfloor\geq m+1\), contradicting (3);
this proves (4). \(\square\)

Two immediate consequences are

\[
 w_p=0\quad(p\leq Y),                              \tag{5}
\]

and

\[
 m\geq\Psi(N,Y),                                  \tag{6}
\]

where \(\Psi(N,Y)\) counts the \(Y\)-smooth integers at most \(N\). Indeed,
every such integer has \(f\)-value \(0\), not \(1\).

In particular, if \(m=o(N)\), then \(Y\to\infty\). Any construction that
puts a nonzero weight on a fixed prime, or on a fixed smooth-prime stage, is
therefore ruled out. All nonzero weights have to escape beyond the moving
scale \(N/(m+1)\). This also gives a quick falsification test for any claimed
near-full construction: compute its claimed deficit \(m\), and check that
every weight below (3) is exactly zero.

Equation (6) is a genuine smooth--rough obstruction, but by itself it is not
strong enough to decide the finite problem. For example, at the presently
natural scale \(m\asymp N/\log N\), it only says that all primes up to order
\(\log N\) have weight zero; most integers still have a prime factor above
that scale.

## 3. An exact cut-or-collision inequality for rough layers

There is also an exact Buchstab-level refinement. Let

\[
 S_1=\{p>Y:w_p=1\}.
\]

For an integer \(n\), write

\[
 R_Y(n)=\prod_{p>Y}p^{v_p(n)}
\]

for its \(Y\)-rough prime-power part. The complementary factor is
\(Y\)-smooth, and (4) gives \(f(n)=f(R_Y(n))\). Unique factorization therefore
gives the exact disintegration

\[
 m=\sum_{\substack{r\leq N,\ P^-(r)>Y\\f(r)\neq1}}
       \Psi(N/r,Y),                                \tag{6}
\]

where \(r=1\) is included and \(P^-(r)>Y\) means that every prime factor of
\(r\) exceeds \(Y\). Thus the finite problem is exactly a weighted
hyperplane problem on rough kernels under the Buchstab weight
\(\Psi(N/r,Y)\), not merely approximately so.

**Lemma 3 (one-rough cut or two-rough collision).** With \(Y\) as in (3),

\[
\begin{split}
 m\ \geq\ &\Psi(N,Y)
 +\sum_{\substack{p>Y\\p\notin S_1}}\Psi(N/p,Y)\\
 &+\sum_{\substack{Y<p<q\\p,q\in S_1}}\Psi(N/(pq),Y)
 +\sum_{\substack{p>Y\\p\in S_1}}\Psi(N/p^2,Y).
                                                               \tag{7}
\end{split}
\]

**Proof.** The four terms count disjoint classes, classified by their
multiset of prime factors exceeding \(Y\).

* A \(Y\)-smooth integer has value \(0\).
* An integer \(pk\), where \(p>Y\) and \(k\) is \(Y\)-smooth, has value
  \(w_p\), so it is excluded when \(p\notin S_1\).
* An integer \(pqk\), where \(p<q\) belong to \(S_1\) and \(k\) is
  \(Y\)-smooth, has value \(2\).
* The same is true of \(p^2k\) for \(p\in S_1\).

Unique factorization makes the classes, and every summand within a class,
disjoint. Every counted integer therefore belongs to \(E\). \(\square\)

This is a literal smooth--rough tradeoff: deleting a prime from the
weight-\(1\) class costs its entire one-rough column, while retaining two
weight-\(1\) primes costs their two-rough collision column. For a global
threshold it recovers the familiar competition between zero, one, and two
large prime factors. When \(Y=N^{o(1)}\), however, a typical integer may have
many factors above \(Y\); then the first three roughness layers in (7) have
vanishing total density. Closing the general finite problem requires
iterating this collision accounting through all roughness layers without
losing control of multiplicities.

## 4. What an ideal Buchstab profile would have to be

Write \(x=\log p/\log N\). A scale-profile construction takes
\(w_p\approx W(x)\). Ignoring the \(O(1/\log N)\) deficit in
\(\log n/\log N\), a typical factorization gives a partition
\(x_1+\cdots+x_r\approx1\). The following deterministic rigidity lemma
explains why all successful numerical profiles drift toward logarithmic
weights.

**Lemma 4 (partition rigidity).** Let \(W:(0,1]\to\mathbb R\) be measurable.
Suppose that for every finite partition \(x_1+\cdots+x_r=1\) with \(x_i>0\),

\[
 W(x_1)+\cdots+W(x_r)=1.                           \tag{8}
\]

Then \(W(x)=x\) for all \(x\in(0,1]\).

**Proof.** Comparing the partitions
\((x,y,1-x-y)\) and \((x+y,1-x-y)\) gives

\[
 W(x)+W(y)=W(x+y)\qquad(x,y>0,\ x+y<1).
\]

Thus \(W\) is measurable and locally additive, hence \(W(x)=cx\). The
one-part partition gives \(W(1)=1\), so \(c=1\). \(\square\)

This does not prove a density theorem: (8) is stronger than holding with high
probability under the Buchstab factorization law. It does isolate the exact
problem left by the smooth--rough heuristic. The unique ideal profile is
\(W(x)=x\), but its exact realization

\[
 w_p=\frac{\log p}{\log N}
 \quad\Longrightarrow\quad
 f(n)=\frac{\log n}{\log N}
\]

has \(f(n)=1\) only for \(n=N\). Smooth--rough concentration supplies an
*approximate* constant, while the problem requires one exact atom. Rounding
the logarithmic weights introduces a carry (the sum of the prime-by-prime
rounding errors), and that carry is not determined by the product size. A
quantitative anti-concentration theorem for this carry is the missing lemma
for turning the heuristic obstruction into a general negative result.

## 5. The monotone one-marker subclass collapses to a global cutoff

There is one useful class for which the preceding obstruction is complete.
Suppose the construction literally assigns each prime a marker value
\(a_p\in\{0,1\}\), wants

\[
 f(n)=\sum_p a_pv_p(n)=1,
\]

and its marker decision is monotone in prime size. Corollary 1 says that an
apparently cofactor-adaptive decision must in fact be independent of the
cofactor. Monotonicity then forces, up to a boundary prime,

\[
 a_p={\bf1}_{p>y}.                                 \tag{9}
\]

So a monotone exact-one Buchstab marker is just the ordinary global threshold
construction; recursion does not enlarge this class.

For completeness, put \(y=N^{1/u}\). The standard Dickman asymptotic gives,
uniformly for fixed \(1<u\leq3\), the limiting density \(P_1(u)\) of integers
having exactly one prime factor above \(y\), counted with multiplicity. For
\(1<u\leq2\), at most one such factor occurs and

\[
 P_1(u)=\log u.
\]

For \(2<u\leq3\), at most two occur. Since the zero-count probability is
\(\rho(u)\) and the mean count is \(\log u\),

\[
 P_1(u)=2(1-\rho(u))-\log u.                       \tag{10}
\]

Using \(u\rho'(u)=-\rho(u-1)\) and
\(\rho(v)=1-\log v\) for \(1\leq v\leq2\), (10) is maximized in this range at

\[
 u=1+\sqrt e,
\]

where it equals

\[
 2-2\rho(1+\sqrt e)-\log(1+\sqrt e)
 =0.8284995068\ldots .                             \tag{11}
\]

This calculation is not claimed as an upper bound for arbitrary weights. It
does show rigorously that cofactor-adaptive monotone **marker** language cannot
improve on the already known threshold family in the relevant \(2<u<3\)
regime: exact additivity removes the adaptation before the Dickman
optimization even begins.

## 6. Dependency chain and remaining bottleneck

The adaptive route would need the following chain.

1. Decompose by largest prime factor (exact Buchstab columns).
2. In each column choose \(w_p\) to align the target with an exact cofactor
   atom; Lemma 1 proves this step and shows it is optimal.
3. Prove that the same lower-prime grading has a \(1-o(1)\) atom on almost all
   cofactor prefixes while also covering almost all of the smooth remainder.
4. Iterate over descending roughness scales.

The weakest unsupported step is 3. Lemma 2 says that the common atom starts
as the exact zero atom on a growing initial interval. Lemma 4 says that at a
continuum level any profile capable of surviving all factorization patterns
must become logarithmic. What is still missing is a finite, exact statement
showing that the transition from the zero core to a logarithmic profile incurs
a non-negligible sum of modal deficits (or, in the opposite direction, an
explicit grading whose carry is exactly constant off \(o(N)\) integers).

## 7. Concrete falsification tests and next action

For any proposed adaptive profile:

* let \(m\) be its claimed number of exceptions and check (3)--(4);
* for every \(p>\sqrt N\), tabulate the exact cofactor values on
  \([1,N/p]\); the covered part of that column cannot exceed (1);
* compare the weighted sum of those exact modal deficits with the claimed
  global deficit;
* if the profile is described as a stopping/marker rule, test the same prime
  with two different cofactors--different proposed increments immediately
  violate complete additivity;
* for a rounded logarithmic profile, record the integer carry distribution,
  not merely the distance of \(f(n)\) from \(1\).

The next useful lemma is therefore an exact anti-concentration/charging
statement for the carry of an approximately logarithmic grading across the
nested cofactor prefixes in (2). Proving only ordinary concentration around
\(1\) cannot close the finite problem.
