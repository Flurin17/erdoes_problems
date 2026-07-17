# Real prime layers and irrational common scales

> **Proof-dependency note.**  The self-contained elementary proof of the
> finite Euler-product lower bound used here is supplied in
> `rational_primitive.md`.  Until that file is complete, the displayed Mertens
> estimate below is a precisely stated standard input rather than an imported
> primitive-set theorem.

## 1. Proposed mechanism

A natural real construction is a common irrational ray
\[
  A=\alpha B,\qquad \alpha>0,
\]
where $B$ is an integer antichain under divisibility.  Examples are the primes,
the layer $\{n:\Omega(n)=r\}$ for fixed $r$, and products of a fixed number of
primes from prescribed prime pools.  The hope would be that irrationality of
$\alpha$ removes integer resonances while a thick prime layer supplies enough
harmonic mass.  In fact this mechanism cannot produce a counterexample:
irrationality cancels out of every comparison, and an elementary prime-prefix
packing inequality gives convergence of the stronger requested series for
every admissible such ray.  For $\alpha\ge1$, primitivity of $B$ is also a
sufficient condition for admissibility; for $0<\alpha<1$ a stronger integral
gap condition is needed, but this only shrinks the available families.

The only possible continuation of this constructive route is therefore to use
different scales $\alpha_j$ in different finite layers.  That creates genuine
Diophantine freedom, but also cross-layer forbidden intervals; no lemma is
currently known that leaves enough parameter space while the accumulated
harmonic mass diverges.

## 2. Precise intermediate lemmas

1. **Common-ray equivalence.**  If $B\subset\mathbb N_{\ge2}$ and $\alpha\ge1$,
   then $\alpha B$ is admissible exactly when $B$ is primitive (no two distinct
   members divide one another).
2. **Prime-prefix cylinders.**  If $P^+(b)$ is the largest prime factor of $b$,
   put
   \[
     L_b=\{bm:m\ge1,\ p\mid m\Longrightarrow p\ge P^+(b)\}.
   \]
   If $B$ is primitive, the sets $L_b$, $b\in B$, are pairwise disjoint.
3. **Density packing.**  Each cylinder has natural density
   \[
     d(L_b)=\frac1b\prod_{p<P^+(b)}\left(1-\frac1p\right),
   \]
   and consequently
   \[
     \sum_{b\in B}\frac1b
       \prod_{p<P^+(b)}\left(1-\frac1p\right)\le1.
   \]
4. **Weighted primitive bound.**  The standard Mertens product lower bound
   $\prod_{p<t}(1-1/p)\ge c/\log(2t)$ and $P^+(b)\le b$ imply
   \[
     \sum_{b\in B}\frac1{b\log b}<\infty.
   \]
5. **Return to the real ray.**  For fixed $\alpha\ge1$,
   \[
     \sum_{x\in\alpha B}\frac1{x\log x}
       =\frac1\alpha\sum_{b\in B}
          \frac1{b\log(\alpha b)}<\infty.
   \]
   The general implication already proved in `NOTES.md` then gives
   $H_{\alpha B}(n)=o(\log n)$.
   If $0<\alpha<1$ and $\alpha B$ is admissible, $B$ is still primitive and,
   after discarding the finite set $b<\alpha^{-2}$,
   $\log(\alpha b)\ge\tfrac12\log b$.  The same convergence follows.

Thus every fixed-$\Omega$ prime layer, and indeed every union of prime-product
families that remains primitive, satisfies both desired conclusions after any
common irrational scaling.

The same argument also eliminates a finite union of rays.  If
$A\subset\bigcup_{i=1}^r\alpha_i\mathbb N$, then admissibility makes each
$B_i=\{b:\alpha_i b\in A\}$ primitive.  Applying the lemma ray by ray and
summing the resulting $r$ convergent series proves both conclusions for $A$.
Consequently a ray-based counterexample would require infinitely many genuinely
different scales, with no reduction to finitely many commensurability classes.

## 3. Completely proved lemma

### Lemma (common rays are harmless)

Let $B\subset\mathbb N_{\ge2}$ and $\alpha>0$, with $A=\alpha B\subset(1,\infty)$.
If $A$ is admissible, then
\[
  \sum_{x\in A}\frac1{x\log x}<\infty.
\]
When $\alpha\ge1$, $A$ is admissible if and only if $B$ is primitive.

**Proof.**  For distinct $b,c\in B$ and $k\ge1$,
\[
  |k(\alpha b)-\alpha c|=\alpha|kb-c|.
\]
If $b\mid c$, choosing $k=c/b$ gives zero, so admissibility implies
primitivity for every $\alpha>0$.  Conversely, if $\alpha\ge1$ and $B$ is
primitive, $kb-c$ is a nonzero integer
for every ordered distinct pair and every $k\ge1$.  Its absolute value is at
least $1$, and multiplication by $\alpha\ge1$ proves admissibility.

It remains to prove convergence.  List the prime factors of each integer in
nondecreasing order, with multiplicity.  Membership $N\in L_b$ says exactly
that the prime-factor list of $b$ is an initial segment of the prime-factor
list of $N$ (ties at the final prime do not change the product of that initial
segment).  Hence if $N\in L_b\cap L_c$, the two initial segments are nested,
so either $b\mid c$ or $c\mid b$.  Primitivity makes the cylinders $L_b$
pairwise disjoint.

The multiplier in $L_b$ is forbidden only from divisibility by the finitely
many primes below $P^+(b)$.  Inclusion-exclusion therefore gives
\[
  d(L_b)=\frac1b\prod_{p<P^+(b)}\left(1-\frac1p\right).
\]
For every finite $F\subset B$, disjointness and finite additivity of natural
density yield
\[
  \sum_{b\in F}\frac1b
       \prod_{p<P^+(b)}\left(1-\frac1p\right)\le1.
\]
Letting $F$ increase to $B$ proves the same inequality for the full
nonnegative sum.  By the standard Mertens product estimate, for an absolute
$c>0$,
\[
 \prod_{p<P^+(b)}\left(1-\frac1p\right)
   \ge \frac{c}{\log(2P^+(b))}
   \ge \frac{c}{\log(2b)}
   \ge \frac{c/2}{\log b}\qquad(b\ge2).
\]
Therefore $\sum_{b\in B}1/(b\log b)\le2/c$.  If $\alpha\ge1$, finally
\[
 \frac1{\alpha b\log(\alpha b)}
 \le\frac1\alpha\frac1{b\log b},
\]
which proves the assertion.  If $0<\alpha<1$, there are only finitely many
$b<\alpha^{-2}$, while for every remaining $b$,
$\log(\alpha b)\ge\tfrac12\log b$.  Thus the tail of the real-ray series is at
most $(2/\alpha)\sum_b1/(b\log b)$, proving the assertion in this case too.
$\square$

The use of Mertens here is only the standard two-sided order of the finite
Euler product, not a primitive-sequence theorem imported from the literature.

## 4. Weakest unsupported step

To obtain a counterexample by real prime layers one must abandon a common
scale and choose finite layers $A_j=\alpha_jB_j$.  Given the previous points
$E$ and a new integer $c\in B_j$, the exact restrictions on the new parameter
are
\[
  \alpha_j\notin
  \bigcup_{x\in E}\ \bigcup_{k\ge1}
  \left(\frac{kx-1}{c},\frac{kx+1}{c}\right),
\]
with only finitely many relevant $k$ in a bounded parameter interval.  The
missing lemma would have to find one common $\alpha_j$ outside these unions
for every $c\in B_j$, while the new layer has harmonic mass bounded below and
the layer locations grow slowly enough that $\sum_j h_j/\log X_j$ diverges.
The crude union bound costs a constant multiple of the accumulated harmonic
mass of $E$ and becomes useless precisely in the counterexample regime.  This
is the first unsupported step, not verification of within-layer pairs.

A common affine shift also does not cheaply fix this.  If
$A=\{\alpha(n+\delta):n\ge n_0\}$ with irrational $\delta$, then for
$k=q+1$ Dirichlet approximation supplies arbitrarily large $q$ with
$\|q\delta\|<1/\alpha$.  Taking
$c=kb+\operatorname{nint}(q\delta)$ gives, for large $b$,
\[
 |k\alpha(b+\delta)-\alpha(c+\delta)|
   =\alpha\,\|q\delta\|<1.
\]
Thus a dense translated integer lattice fails; sparsifying the integer base is
essential.

## 5. Concrete falsification tests

For any proposed finite new layer $\alpha B$ above an already constructed
finite set $E$:

1. Check that $B$ is primitive; otherwise an internal exact multiple kills
   the layer for every $\alpha$.
2. For every $x\in E$, $c\in B$, intersect the candidate parameter interval
   with the finitely many open intervals
   $((kx-1)/c,(kx+1)/c)$.  If their union covers the candidate interval, that
   layer cannot be appended.  Endpoints must be retained because equality is
   allowed.
3. After choosing $\alpha$, check each cross pair using only
   $k=\lfloor\alpha c/x\rfloor$ and $k+1$ (positive values only), equivalently
   verify $\operatorname{dist}(\alpha c/x,\mathbb Z)\ge1/x$.
4. For a fixed common scale, simply test divisibility in $B$ and then apply the
   prime-prefix density inequality above; numerical size cannot overturn that
   proof.

The affine-lattice formula above is also a direct analytic falsification test:
the near-integer multiples $q\delta$ explicitly produce violating pairs.

## 6. Next action if the route survives

The useful remaining experiment is not another common-scale prime layer.  It
is a deterministic interval-union computation for layer-dependent scales:
choose several candidate bases $B_j$ (short dyadic blocks, fixed-$\Omega$
blocks, and marker-prime products), compute the exact surviving set of
$\alpha_j$ after all cross constraints, and measure survival against prior
harmonic mass.  If survival repeatedly collapses, extract a rigorous covering
lemma.  If a structured resonance leaves intervals, identify its invariant
and attempt an infinite induction.  The common irrational-ray route itself is
rigorously eliminated as a source of either counterexample.
