# Protected prime markers and coprime block scales

## 1. Proposed mechanism

Let (I) be finite or countable, choose distinct primes (q_i) and integers
(c_i\geq 1), and call an integer (Q)-free if none of the primes
(Q=\{q_i:i\in I\}) divides it.  For arbitrary sets of (Q)-free cores
(B_i), put

\[
A_i=q_i^{c_i}B_i,
\qquad
A=\bigcup_{i\in I}A_i. \tag{1}
\]

The prime (q_i) occurs to the fixed positive exponent (c_i) on every
element of block (A_i), and occurs on no other block.  Thus its valuation
counts, exactly, how many factors in a product came from block (i).  This
is the strongest and cleanest version of patching finite constructions by a
protected prime or a pairwise coprime scale.  The maximal completion of (1)
is obtained by taking every (Q)-free core:

\[
U(Q,\mathbf c)
=\bigcup_{q\in Q}
 \{n:v_q(n)=c_q, v_{q'}(n)=0\text{ for every }q'\in Q\setminus\{q\}\}.
\tag{2}
\]

This gives an explicit infinite PLR construction.  Unfortunately, the
density calculation below proves a sharp ceiling (1/e) for this entire
strict protected-marker mechanism.  Restricting the cores to local finite
constructions or to magnitude blocks can only lower its density.

## 2. Interpretation handled

Everything below uses the strongest reading of the problem: (r,s\geq1)
are arbitrary, repetitions are allowed, and density means natural density.
The construction therefore also works under the internally
repetition-free reading.  The argument is not a bounded-length or modular
certificate.  The element (1) is absent automatically.

For a magnitude-block patch one may additionally require
(q_i^{c_i}B_i\subset (X_{i-1},X_i]).  No part of the rigidity proof uses
this extra restriction.  A coprime-scale patch (M_iB_i), in which the
scales (M_i>1) are pairwise coprime and every core avoids every prime in
the scales, is a special case after choosing one (q_i\mid M_i) and fixing
its exponent in (M_iB_i).

## 3. Precise lemma chain

1. **Protected-marker lemma.**  Fixed, exclusive marker valuations force
   equality of the number of factors from every block separately.
2. **Maximal-completion reduction.**  Every construction of the form (1),
   including every further finite-block restriction, is a subset of
   (U(Q,\mathbf c)).
3. **Finite-(Q) density formula.**  If (Q) is finite, then
   \[
   d(U(Q,\mathbf c))
   =\prod_{q\in Q}\left(1-\frac1q\right)
     \sum_{q\in Q}\frac1{q^{c_q}}. \tag{3}
   \]
4. **Infinite-(Q) dichotomy.**  If \(\sum_{q\in Q}1/q<\infty\), formula
   (3), with the convergent product and sum, remains valid.  If
   \(\sum_{q\in Q}1/q=\infty\), then (U(Q,\mathbf c)) has natural density
   (0).
5. **Sharp ceiling.**  Every strict protected-marker construction has
   density at most (1/e).  The supremum (1/e) is approached by taking
   (c_q=1) and a finite collection of individually large primes whose
   reciprocal sum tends to (1).
6. **Block dilution.**  In an interval (J) of length (H), a block with
   marker (q_i^{c_i}) contains at most (H/q_i^{c_i}+1) integers.  Thus a
   genuinely fresh sequence of marker primes has vanishing within-block
   density even before the global (1/e) ceiling is applied.

## 4. A complete cross-block rigidity lemma

**Lemma (exclusive fixed markers).**  Let ((A_i)_{i\in I}) be sets of
positive integers.  Suppose that for every (i\in I) there are a prime
(q_i) and an integer (c_i\geq1) such that the (q_i) are distinct and

\[
v_{q_i}(a)=c_i\quad(a\in A_i),
\qquad
v_{q_i}(a)=0\quad(a\in A_j, j\ne i). \tag{4}
\]

Then (A=\bigcup_i A_i) is product-length rigid, with repetitions allowed.
No internal rigidity assumption on the individual (A_i) is needed.

**Proof.**  The conditions imply that the (A_i) are pairwise disjoint.
Consider an equality

\[
\prod_{u=1}^r a_u=\prod_{v=1}^s b_v,
\qquad a_u,b_v\in A.
\]

For each (i), let \(\ell_i\) and \(m_i\) be the numbers of factors on the
left and right, respectively, which belong to (A_i).  Only finitely many
of these numbers are nonzero.  Taking (q_i)-adic valuations and using (4)
gives

\[
c_i\ell_i=c_i m_i.
\]

Since (c_i>0), \(\ell_i=m_i\) for every (i).  Summing over (i) yields
(r=\sum_i\ell_i=\sum_i m_i=s).  This works for arbitrary product lengths
and arbitrary repetitions. \(\square\)

Equivalently, (1) has the explicit global grading

\[
f(n)=\sum_{i\in I}\frac{v_{q_i}(n)}{c_i};
\]

the sum is finite for each integer, and (f(a)=1) for every (a\in A).

## 5. Quantitative density and loss calculation

First suppose that (Q) is finite and write

\[
P_Q=\prod_{q\in Q}\left(1-\frac1q\right).
\]

For a fixed owner (q\), the conditions (v_q(n)=c_q) and
(v_{q'}(n)=0) for (q'\ne q) are independent periodic divisibility
conditions (by the Chinese remainder theorem).  Their density is

\[
\frac{1-1/q}{q^{c_q}}
\prod_{q'\ne q}\left(1-\frac1{q'}\right)
=\frac{P_Q}{q^{c_q}}.
\]

The owner classes are disjoint, proving (3).  Put
(S_Q=\sum_{q\in Q}1/q).  Since (c_q\geq1) and
(1-x\leq e^{-x}),

\[
d(U(Q,\mathbf c))
\leq P_QS_Q
\leq e^{-S_Q}S_Q
\leq \frac1e. \tag{5}
\]

Thus even the maximal strict-marker completion deletes at least

\[
1-\frac1e=0.632120\ldots \tag{6}
\]

of all integers.  For example, with (Q=\{2,3\}) and both exponents equal
to (1), the construction is
(\{n:v_2(n)+v_3(n)=1\}) and has density

\[
\frac12\frac23\left(\frac12+\frac13\right)=\frac5{18}.
\]

It occupies exactly (10) residue classes modulo (36).

For completeness, the same ceiling holds for infinite (Q).  If
(S=\sum_{q\in Q}1/q<\infty), finite truncation gives

\[
d(U(Q,\mathbf c))
=P_Q\sum_{q\in Q}q^{-c_q}.
\tag{7}
\]

Indeed, after imposing the conditions for a finite subset (R\subset Q),
the integers affected by any omitted prime have upper density at most
(\sum_{q\in Q\setminus R}1/q), which tends to zero.  The same union bound
controls owner classes in the tail.  Hence (7) follows from the finite
formula, and (5) applies.

If instead (S=\infty), fix a finite (R\subset Q).  Every member of
(U(Q,\mathbf c)) is divisible by at most one distinct prime of (R).
The set of integers with this weaker property has density

\[
P_R\left(1+\sum_{q\in R}\frac1{q-1}\right)
\leq e^{-S_R}(1+2S_R),
\qquad S_R=\sum_{q\in R}\frac1q.
\]

Taking finite (R) with (S_R\to\infty) proves that (U(Q,\mathbf c))
has upper density, hence natural density, (0).

The bound (1/e) is the sharp supremum for this mechanism.  Using the
standard Euler theorem \(\sum_p1/p=\infty\), choose finite sets (Q_k) of
primes all tending to infinity such that
(S_{Q_k}\to1).  With (c_q=1),

\[
\log P_{Q_k}
=-S_{Q_k}+O\!\left(\sum_{q\in Q_k}\frac1{q^2}\right)
=-1+o(1),
\]

so (P_{Q_k}S_{Q_k}\to1/e).  This sharpness statement is not needed for
the obstruction, only for locating exactly how much density strict
protection can retain.

For fixed finite (Q\) and \(\mathbf c\), the set is periodic modulo
(M=\prod_{q\in Q}q^{c_q+1}), so

\[
|U(Q,\mathbf c)\cap[1,N]|
=d(U(Q,\mathbf c))N+O_{Q,\mathbf c}(1). \tag{8}
\]

Also, if a magnitude block (A_i\) lies in an interval of length (H_i),
then (A_i\subset q_i^{c_i}\mathbb N) gives

\[
|A_i|\leq \frac{H_i}{q_i^{c_i}}+1. \tag{9}
\]

Equations (5), (8), and (9) show that neither taking all allowable cores nor
cutting them into rapidly growing intervals repairs the density loss.

## 6. Weakest unsupported step and exact bottleneck

There is no gap in the strict-marker construction: it is PLR, and its
density ceiling is proved.  The exact bottleneck is that **exclusive**
markers diagonalize the cross-block valuation equations only by forcing
every admitted integer to realize one positive, rare divisibility event and
to avoid every competing marker.  The maximal union of those events already
has density at most (1/e).

Consequently a high-density patch must allow markers to be shared across
blocks.  The weakest plausible repair is an *overlapping-marker profile
lemma*: find marker valuation profiles (c(a)=(v_q(a))_{q\in Q}) occupying
(1-o(1)) of every late block, together with rational weights
((\lambda_q)), such that

\[
\sum_{q\in Q}\lambda_qv_q(a)=1
\]

on every retained profile.  This would still give exact arbitrary-length
rigidity, but a single (q)-valuation would no longer isolate a block.
Reconciling the shared-marker equations with the local finite gradings is
the unsupported step.  In the language of the structural notes, it is
precisely the problem of producing a high-mass nonzero exact atom of a
completely additive function; private coprime coordinates do not make that
step easier.

This argument does **not** rule out an (N)-dependent protected-marker trick
that exploits boundary effects before a full marker period is visible.  It
does rule out using a fixed global family of exclusive markers to transfer
such finite sets to an infinite set of density (>1-\epsilon).

## 7. Concrete falsification tests

1. **Variable owner exponent.**  If a proposed direct counting proof allows
   both (2) and (4) in one block marked only by (2), then
   (2\cdot2=4) is already a length-(2) versus length-(1) failure.
   A fixed positive marker exponent (or some replacement grading) is
   essential.
2. **Cross-contamination.**  Let one nominal (2)-block contain
   \(\{2,6\}\) and a nominal (3)-block contain \(\{3\}\).  The element
   (6) carries the other block's marker, and
   (2\cdot3=6) shows exactly how the exclusive-marker proof can fail.
3. **Density check.**  For (Q=\{2,3\}), (c_2=c_3=1), direct enumeration
   modulo (36) must find (10) accepted residue classes, agreeing with
   density (5/18).  Any implementation or claimed density formula that
   disagrees has mishandled exact valuations versus mere divisibility.
4. **Ceiling check.**  Any claimed strict-marker construction of density
   greater than (1/e) must fail at least one defining condition: some
   block has variable owner valuation, some marker occurs in another block,
   or some admitted element has no protected positive marker.  Formula (5)
   is otherwise decisive.

## 8. Next action if the route is retained

Replace diagonal/private marker profiles by a fixed **shared** block-profile
matrix.  First prove the following generalized certificate: if every element
of block (j) has one fixed marker profile (c_j), and all profiles satisfy
(\lambda\cdot c_j=1) for one rational vector (\lambda), then their union
is PLR.  Then investigate whether many profiles lying on such a nonzero
affine hyperplane can jointly occupy (1-o(1)) of long integer intervals.
Triangular profile matrices are the first concrete subclass to test, because
they retain an inductive block interpretation while permitting controlled
marker reuse.  If their density also has a uniform ceiling below (1), that
would rigorously eliminate the next broader finite-to-infinite patching
class; if not, the resulting common rational weights would supply the
needed global grading.
