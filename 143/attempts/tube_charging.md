# Tube charging and multiplicative-filter route

This route is partial.  It gives exact finite-measure and fractional-packing
formulations, proves a divisibility-filter packing estimate, and identifies a
single global union/energy inequality which would imply both requested
conclusions.  That global inequality is not proved here.

Throughout, (B\subset[2,\infty)) is a finite admissible set.  The restriction
to ([2,\infty)) loses nothing for the infinite problem, as proved in
`NOTES.md`.  Put
\[
 I(x,k)=(kx-\tfrac12,kx+\tfrac12),\qquad k\in\mathbb Z_{\ge1}.
\]

## 1. Exact tube equivalence on a finite-measure window

### Lemma 1 (tube form of admissibility)

The set (B) is admissible if and only if
\[
 I(x,k)\cap I(y,1)=\varnothing
 \quad(x,y\in B, x\ne y, k\ge1).
 \tag{1}
\]
Equivalently, because (x\ge2), it is harmless in (1) to permit (x=y)
when (k\ge2).

**Proof.** Two open intervals of radius (1/2), centred at (kx) and
(y), are disjoint exactly when (|kx-y|\ge1).  If (x=y) and (k\ge2),
then (|kx-x|=(k-1)x\ge2).  The use of open intervals correctly retains
the allowed endpoint (|kx-y|=1).  \(\square\)

For a bounded measurable window (Omega\subset\mathbb R), define the
finite-measure truncated tube set
\[
 T_x(\Omega)=\Omega\cap\bigcup_{k\ge1}I(x,k).
 \tag{2}
\]
Only finitely many intervals in (2) meet a bounded (Omega).  Thus all
subsequent union measures and allocation problems are genuinely finite.

### Lemma 2 (exact fractional Hall/LP equivalence)

Let (T_x\subset\Omega) be finite unions of intervals in a bounded window,
and let (d_x\ge0), for (x\in B).  The following are equivalent.

1. There are measurable (f_x\ge0), supported on (T_x), such that
   \[
   \sum_{x\in B}f_x(t)\le1\quad\text{a.e.},
   \qquad \int_\Omega f_x\ge d_x.
   \tag{3}
   \]
2. For every (S\subset B),
   \[
   \left|\bigcup_{x\in S}T_x\right|\ge\sum_{x\in S}d_x.
   \tag{4}
   \]
3. For every vector (u=(u_x)_{x\in B}\) with (u_x\ge0),
   \[
   \int_\Omega\max_{x:\,t\in T_x}u_x\,dt
      \ge\sum_{x\in B}d_xu_x,
   \tag{5}
   \]
   where the maximum of the empty set is (0).

**Proof.** From (3),
\[
 \sum_xd_xu_x\le\int\sum_xu_xf_x
 \le\int\max_{x:t\in T_x}u_x,
\]
so (3) implies (5).  Taking (u=1_S) in (5) gives (4).

For (4) implies (3), partition (Omega), up to a null set, into the
finitely many atoms cut out by all interval endpoints.  Make a finite flow
network: the source has an edge of capacity equal to the measure of each
atom; an atom connects with infinite capacity to every (x) whose (T_x)
contains it; and (x) connects to the sink with capacity (d_x).  Every
finite source-sink cut corresponds to some (S\subset B), and (4) says its
capacity is at least (sum_xd_x).  Finite max-flow/min-cut therefore gives
a flow of that value.  Spread the atom-to-(x) flow uniformly over the atom
to obtain (3).  \(\square\)

This is the promised finite-measure tube equivalence: a charging argument
is neither heuristic nor dependent on a choice of ordering.  It is exactly
a family of tube-union inequalities.

## 2. Divisibility and prime-filter overlap

### Lemma 3 (primitive labels at every target)

For fixed (t\in\mathbb R), let
\[
 K_t=\{k\ge1:t\in I(x,k)\text{ for some }x\in B\}.
\]
Each label (k) occurs for at most one (x), and (K_t) is primitive:
no two distinct members divide one another.

**Proof.** If (t\in I(x,k)\cap I(y,k)), then
(k|x-y|<1), contrary to (1)-separation unless (x=y).  Now suppose
(k=q\ell), (q\ge2), and
(t\in I(x,k)\cap I(y,\ell)).  Then
\[
 |qx-y|=\frac{|kx-\ell y|}{\ell}<\frac1\ell\le1.
\]
For (x\ne y) this contradicts admissibility.  For (x=y), it contradicts
((q-1)x\ge2).  \(\square\)

The following is the useful prime-filter form.  Write
\[
 U_m=\bigcup_{x\in B}I(x,m).
\]
For every prime (p) (indeed every integer (q\ge2)) and every (m\ge1),
\[
 U_m\cap U_{pm}=\varnothing.
 \tag{6}
\]
More generally, if (K\) is a divisibility chain, then all intervals
\({I(x,k):x\in B,k\in K}\) are pairwise disjoint.  This is a genuine
overlap theorem, but only along chains; tubes with incomparable prime labels
can overlap arbitrarily often (Section 5).

### Proposition 4 (prime-power packing)

Let
\[
 N(X)=\#(B\cap[2,X]),\qquad
 H(X)=\sum_{\substack{x\in B\\x\le X}}\frac1x.
\]
For every integer (p\ge2) and (X\ge2),
\[
 \sum_{r\ge0}N(X/p^r)\le X,
 \tag{7}
\]
and
\[
 H(X)\le(1-p^{-1})\bigl(1+\log(X/2)\bigr)+\frac{N(X)}X.
 \tag{8}
\]
In particular, taking (p=2),
\[
 H(X)\le\tfrac12\log X+O(1).
 \tag{9}
\]

**Proof.** By Lemma 3, all unit intervals (I(x,p^r)) with
(p^rx\le X) are disjoint.  They lie in ((0,X+1/2)), and their leftmost
possible endpoint is at least (3/2), so their number is at most (X).
This proves (7) (with the non-strict real upper bound sufficient here).

Put (C(t)=\sum_{r\ge0}N(t/p^r)\).  Integrating (7) gives
\[
 \int_2^X\frac{C(t)}{t^2}\,dt\le\log(X/2).
 \tag{10}
\]
For (x\le X), set (m_x=\lfloor\log_p(X/x)\rfloor).  Reversing the
finite sum in the left side of (10) gives
\[
 \int_2^X\frac{C(t)}{t^2}\,dt
 =\sum_{x\le X}\left(
   \frac{1-p^{-(m_x+1)}}{(1-p^{-1})x}-\frac{m_x+1}{X}
 \right).
\]
Since (p^{m_x+1}x>X), the omitted geometric tail is less than
(1/((1-p^{-1})X)).  Also
(sum_x(m_x+1)=C(X)\le X).  Hence the last display is at least
\[
 \frac{H(X)}{1-p^{-1}}
 -\frac{N(X)}{(1-p^{-1})X}-1.
\]
Together with (10), this proves (8), and (9) follows from (N(X)\le X).
\(\square\)

This does not give (o(\log X)).  Binary powers are already optimal among
single-chain versions of this argument, since for any chain
(1=k_0\mid k_1\mid\cdots), one has (k_i\ge2^i) and hence
(sum_i1/k_i\le2).

## 3. A sufficient fractional charging lemma

For (R>1), let (Omega_R=(0,R)) and use (T_x(R)=T_x(\Omega_R)).
The following is deliberately stated as a sufficient lemma, not as a proved
property of admissible sets.

### Fractional tube-charging lemma (open bottleneck)

There is an absolute (c>0) such that for every finite admissible
(B\subset[2,\infty)), one can choose (R>2\max B) and functions (f_x)
supported on (T_x(R)), satisfying
\[
 \sum_{x\in B}f_x\le1,
 \qquad
 \int_0^R f_x(t)\,dt\ge
       \frac{cR}{x\log(2x)}quad(x\in B).
 \tag{FTCL}
\]

If **FTCL** holds, then both conclusions in Problem 143 hold.

**Proof of sufficiency.** Summing the demands in FTCL and using the capacity
bound gives
\[
 \sum_{x\in B}\frac1{x\log(2x)}\le c^{-1}.
\]
This is uniform over finite subsets (B) of an infinite admissible (A).
Taking an increasing exhaustion, and using
(log(2x)\asymp\log x) for (x\ge2), proves
(sum_{x\in A}1/(x\log x)<\infty).  Proposition 3.1 of `NOTES.md` then
gives (H_A(n)=o(\log n)).  \(\square\)

By Lemma 2, FTCL is equivalent to either of the following uniform
statements (with the same (R) and demands):
\[
 \left|\bigcup_{x\in S}T_x(R)\right|
 \ge cR\sum_{x\in S}\frac1{x\log(2x)}
 \quad\text{for every }S\subset B,
 \tag{11}
\]
or
\[
 \int_0^R\max_{x:t\in T_x(R)}u_x\,dt
 \ge cR\sum_{x\in B}\frac{u_x}{x\log(2x)}
 \quad(u_x\ge0).
 \tag{12}
\]
Thus the bottleneck is an explicit lower bound for the measure of a union,
not a pointwise multiplicity assertion.

## 4. A second sufficient route: multiscale depletion

Set
\[
 \delta_j=2^{-j}\#(A\cap[2^j,2^{j+1})),
 \qquad D_j=\sum_{i\le j}\delta_i.
\]

### Lemma 5 (depletion recursion closes the first conclusion)

If for some constants (C>0,alpha>0) and all sufficiently large (j),
\[
 \delta_j\le\frac{C}{(1+D_{j-1})^\alpha},
 \tag{13}
\]
then
\[
 \sum_j\frac{\delta_j}{j}<\infty.
 \tag{14}
\]
Consequently (sum_{x\in A}1/(x\log x)<\infty), and hence also
(H_A(n)=o(\log n)).

**Proof.** If (D_j) is bounded, then (\sum_j\delta_j<\infty), so (14)
is immediate.  Otherwise, let (\tau_m) be the first (j) with (D_j\ge m).
While (D\in[m-1,m]), each increment is (O(m^{-\alpha})); apart from a
bounded initial range, crossing a unit level therefore requires
(\gg m^\alpha) indices.  Summing these crossing times gives
(\tau_m\gg m^{\alpha+1}).  The total increment while
(D\in[m,m+1]) is at most (1+O(m^{-\alpha})=O(1)), and all its indices
are at least (\tau_m).  Its contribution to (14) is therefore
(O(m^{-\alpha-1})), summable in (m).

For (x\in[2^j,2^{j+1})), the shell contribution to
(\sum1/(x\log x)) is comparable, with absolute constants, to
(\delta_j/j).  This proves the last assertion.  \(\square\)

A tube sieve giving (13), even with arbitrarily small (alpha>0), would
therefore be enough.  This is weaker-looking and more explicitly
multiscale than FTCL, but it too requires a global resonance estimate.

The recurrence (13) is only a sufficient closure device and cannot hold as a
function of (D_{j-1}) alone.  Finite primitive integer prefixes can have
arbitrarily large harmonic mass and still be followed, at one selected scale,
by a positive-density admissible residue block.  Any valid depletion input
must therefore average over scales or retain carrier/residue structure.

## 5. Exact obstructions to naive charging

### Dense safe blocks

If (I=[M,M+L]) with (M-L\ge1), every (1)-separated subset of (I) is
admissible.  Indeed, for (x<y) in (I), the (k=1) condition is the
separation, while for (k\ge2),
\[
 kx-y\ge2M-(M+L)=M-L\ge1.
\]
Thus the sharp occupancy is (lfloor L\rfloor+1).  In particular, for
integers (N,q\ge2),
\[
 B_{N,q}=\{N+1/q+j:0\le j<N\}
\]
is admissible, has identical fractional parts, and has harmonic mass tending
to (log2).  No within-shell density saving or fractional-part dispersion
is available.

### Common-denominator characterization and unbounded resonance

For (A=\{a/q:a\in S\subset\mathbb Z, a>q\}), write (b=ma+r),
(0\le r<a), for (a<b).  The pair (a/q,b/q) is admissible exactly when
\[
 q\le r\le a-q.
 \tag{15}
\]
Indeed the least numerator distance is
(min_{k\ge1}|ka-b|=\min(r,a-r)); the reverse ordered orientation is
automatic after separation.  If (L=\operatorname{lcm}(a:a/q\in A)), then
all tubes
\[
 I(a/q,L/a)
\]
have the common centre (L/q).  Hence admissible sets can have arbitrarily
large tube multiplicity at a point and on a full interval around that point.

Even restricting multipliers to primes does not repair pointwise overlap.
For a finite prime set (P), the primitive integer set
\[
 \{T/p:p\in P\},\qquad T=\prod_{p\in P}p,
\]
is admissible and all prime-labelled tubes have centre (T).  Taking
disjoint prime blocks produces one infinite admissible integer set with
unbounded exact prime-tube multiplicity.  By choosing blocks with large
(sum_{p\in P}1/p) (using the elementary divergence of the prime reciprocal
sum), even (1/p)-weighted pointwise overlap is unbounded.

Therefore neither a bounded-overlap estimate nor an inequality of the form
(\(\int m^2\ll\int m\)) can establish FTCL.  A successful proof must use a
global Hall/union estimate, optimized sieve weights, or explicitly retain
the gcd/lcm collision energy.

## 6. Dependency graph and current bottleneck

\[
\begin{array}{c}
\text{admissibility}\quad\text{(given)}\\
\downarrow\\
\text{tube equivalence (Lemma 1)}
\quad+\quad
\text{primitive-label / prime-filter separation (Lemma 3)}\\
\downarrow\hspace{4.5cm}\downarrow\\
\text{fractional Hall equivalence (Lemma 2)}
\qquad\text{prime-power bound (Proposition 4)}\\
\downarrow\hspace{4.8cm}\searrow\\
\boxed{\text{FTCL / global tube-union estimate: OPEN}}
\quad\text{or}\quad
\boxed{\text{depletion recursion (13): OPEN}}\\
\downarrow\\
\sum_{x\in A}\frac1{x\log x}<\infty\\
\downarrow\\
H_A(n)=o(\log n).
\end{array}
\]

The first open edge is the precise bottleneck.  Lemmas 1--3 say exactly
what combinatorial information admissibility supplies, while Section 5
shows why local multiplicity, single-scale occupancy, and unoptimized
second moments cannot cross it.  A plausible next target is first to prove
(11) for rational rays (A=\alpha P), where (P) is a finite primitive
integer set, by a divisor-chain/weighted covering argument; the genuinely
real case then asks for a stable extension beyond exact common lattices.
