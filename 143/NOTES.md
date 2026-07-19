# Notes: Erdős #143

This file records distilled definitions, equivalent formulations, calculations, and proved lemmas. Raw agent transcripts are not retained.

## 1. Definitions and conventions

A set $A\subset(1,\infty)$ is **admissible** if
\[
(\forall x,y\in A)(x\ne y)(\forall k\in\mathbb Z_{\ge1})\quad |kx-y|\ge1.
\]
For such a set put
\[
H_A(t)=\sum_{\substack{x\in A\\x<t}}\frac1x,
\qquad
H_A^{\le}(t)=\sum_{\substack{x\in A\\x\le t}}\frac1x,
\qquad
S_A=\sum_{x\in A}\frac1{x\log x}.
\]
Natural logarithms are used. Replacing $x<t$ by $x\le t$ changes $H_A$ by at most $1/t$.

## 2. Exact normalization

### Lemma 2.1 (ordered pairs reduce to the smaller-first orientation)

The hypothesis is equivalent to
\[
(\forall a,b\in A)(a<b)(\forall k\ge1)\quad |ka-b|\ge1.
\]

**Proof.** Necessity is immediate. Conversely, the displayed condition at $k=1$ gives $b-a\ge1$. For the reversed ordered pair, $k=1$ is the same condition, while for $k\ge2$,
\[
kb-a=(k-1)b+(b-a)>1.
\]
Thus only multiples of the smaller member need checking. The relevant $k$ may depend on the pair. $\square$

### Lemma 2.2 (separation, local finiteness, and enumeration)

Every admissible set is $1$-separated. Hence
\[
\#(A\cap[u,v])\le\lfloor v-u\rfloor+1,
\]
and $A$ is countable and locally finite. If $A$ is infinite it is unbounded, has a least element, and has a unique increasing enumeration $a_1<a_2<\cdots$ with $a_j\ge a_1+j-1$.

**Proof.** Take $k=1$. Ordering any finite set in $[u,v]$ shows consecutive gaps are at least $1$. Every half-open unit interval contains at most one point, proving countability. Given $a\in A$, the finite nonempty set $A\cap(1,a]$ has a least element. An infinite locally finite set is unbounded. $\square$

### Lemma 2.3 (the lower endpoint is actually $2$)

Every infinite admissible set is contained in $[2,\infty)$.

**Proof.** If $1<a<2$ and $b>a$, choose a nearest positive integer $k$ to $b/a$. Then $|ka-b|\le a/2<1$, a contradiction. Every member of an infinite locally finite $A$ has a larger member. $\square$

Thus the apparent singularity of $(x\log x)^{-1}$ at $1$ never occurs in the infinite problem.

### Lemma 2.4 (safe-gap, ratio, and nearest-integer forms)

For $a<b$ the pair is admissible exactly when any, hence all, of the following hold:
\[
b\notin\bigcup_{k\ge1}(ka-1,ka+1),
\]
\[
\operatorname{dist}(b/a,\mathbb Z)\ge1/a,
\]
\[
\{b/a\}\in[1/a,1-1/a],
\]
and, writing $m=\lfloor b/a\rfloor$,
\[
1\le b-ma\le a-1.
\]
Equivalently the allowed values above $a$ form
\[
\bigcup_{m\ge1}[ma+1,(m+1)a-1].
\]
The forbidden intervals are open because equality $|ka-b|=1$ is allowed.

**Proof.** Divide $|ka-b|\ge1$ by $a$. Since $b/a>1$, nonpositive integers are farther than $1>1/a$ and may be included in the nearest-integer formulation. The fractional-part and safe-gap forms are algebraic rearrangements. $\square$

For a fixed pair with $a\ge2$, the interval $((b-1)/a,(b+1)/a)$ has length at most $1$, so at most one integer $k$ can violate the condition (with the harmless possibility of two endpoint integers when its length is exactly $1$, neither lying in the open interval).

### Lemma 2.5 (exact logarithmic form)

Let $u=\log a$, $v=\log b$, $d=v-u>0$, and $\delta=e^{-u}=1/a$. Then the condition is
\[
\operatorname{dist}(e^d,\mathbb Z)\ge\delta,
\]
or equivalently
\[
d\notin\bigcup_{k\ge1}\bigl(\log(k-\delta),\log(k+\delta)\bigr).
\]
Around $\log k$ the left and right forbidden radii are respectively
\[
-\log(1-\delta/k),\qquad \log(1+\delta/k),
\]
so the forbidden neighborhood is not exactly symmetric or uniform.

### Lemma 2.6 (same dyadic block)

If $a<b<2a$, the pair condition is exactly
\[
a+1\le b\le2a-1.
\]
All $k\ge3$ are automatic. More generally, multiplicative interaction inside a single nearly dyadic block can be as weak as additive separation: every finite set in $[T,2T-1]$ with pairwise gaps at least $1$ is admissible. In particular
\[
\max\#(A\cap[T,2T-1])=\lfloor T\rfloor,
\]
attained by consecutive unit-spaced points starting at $T$.

## 3. The two requested conclusions

### Proposition 3.1 (the first conclusion implies the second)

For every cutoff-locally-finite $A\subset(1,\infty)$,
\[
S_A<\infty\quad\Longrightarrow\quad H_A(t)=o(\log t).
\]

**Proof.** Fix $M>1$. For $t>M$,
\[
\frac{H_A(t)}{\log t}
\le \frac{H_A^{\le}(M)}{\log t}
 +\sum_{\substack{x\in A\\M<x<t}}\frac1{x\log x},
\]
because $\log x\le\log t$. First let $t\to\infty$ and then $M\to\infty$. $\square$

### Proposition 3.2 (exact integral criterion)

As an identity in $[0,\infty]$,
\[
S_A=\int_1^\infty\frac{H_A^{\le}(t)}{t(\log t)^2}\,dt.
\]
For finite $X$,
\[
\sum_{\substack{x\in A\\x\le X}}\frac1{x\log x}
=\frac{H_A^{\le}(X)}{\log X}
 +\int_1^X\frac{H_A^{\le}(t)}{t(\log t)^2}\,dt.
\]

**Proof.** Use
\[
\frac1{\log x}=\int_x^\infty\frac{dt}{t(\log t)^2}
\]
and Tonelli for the first identity. The finite identity is Stieltjes integration by parts. The integral is harmless near $1$ because an admissible infinite set is contained in $[2,\infty)$. $\square$

Thus $H_A(t)=o(\log t)$ alone supplies no integrable rate. Indeed, for general $1$-separated locally finite sets the converse to Proposition 3.1 fails: for sufficiently large $m$, $x_m=m\log\log m$ has gaps greater than $1$, satisfies $H(n)=o(\log n)$, but
\[
\sum_m\frac1{x_m\log x_m}\gg
\sum_m\frac1{m\log m\log\log m}=\infty.
\]
This example is not asserted to satisfy the $k\ge2$ exclusions.

### Shell form

Put
\[
h_j=\sum_{\substack{x\in A\\e^j\le x<e^{j+1}}}\frac1x.
\]
Then, up to finitely many initial shells,
\[
S_A<\infty\quad\Longleftrightarrow\quad\sum_j\frac{h_j}{j}<\infty,
\]
whereas
\[
H_A(t)=o(\log t)\quad\Longleftrightarrow\quad
\sum_{j<J}h_j=o(J).
\]

## 4. Boundary and model cases

1. If $2\in A$, Lemma 2.4 forces every larger member to be an odd integer. For integer sets the condition is exactly that no distinct member divides another, since $|kx-y|$ is integral and can be less than $1$ only when it is zero.
2. If $m=\min A$, every later point lies in one of the closed cells $[km+1,(k+1)m-1]$. At $m=2$ these cells collapse to odd integers.
3. If eventually every geometric shell $[q^j,q^{j+1})$ contains at most $C$ points, $q>1$, then $S_A<\infty$ and even $\sum_{x\in A}1/x<\infty$.
4. Integer-ratio geometric progressions are inadmissible. The Fermat numbers $F_j=2^{2^j}+1$ form an admissible scale-sparse integer example because $\prod_{i<j}F_i=F_j-2$, so no one divides another.
5. Identical ordinary fractional parts do not force failure. For every fixed $\theta\in[0,1)$ there is an infinite admissible $A\subset\mathbb Z+\theta$ with successive elements more than doubling. To extend a finite such set $F$ with $\sum_{x\in F}1/x<1/4$, use candidates on the lattice in a long remote interval. For each $x\in F$, its forbidden intervals contain at most two lattice points per relevant multiple, hence delete at most $2|I|/x+O(1)$ candidates. The union deletes fewer than half the candidates for long enough $I$, leaving an arbitrarily remote admissible extension.

## 5. Exact thickened-comb identities

For $a\in A$ let $I_a=(a-1/2,a+1/2)$ and
\[
C_x=\bigcup_{k\ge2}(kx-1/2,kx+1/2).
\]
The intervals $I_a$ are disjoint and $E:=\bigcup_{a\in A}I_a$ is disjoint from every $C_x$. Uniformly for $Z\ge Y\ge2$,
\[
\left|\log(E)\cap[\log Y,\log Z]\right|
=\sum_{a\in A\cap[Y,Z]}\frac1a+O(1/Y),
\]
where boundary intervals may be interpreted in the evident truncated sense. For fixed $x$ and $Z\ge Y\ge4x$,
\[
\left|\log(C_x)\cap[\log Y,\log Z]\right|
=\frac1x\log(Z/Y)+O(1/Y).
\]
These follow from
\[
\log\frac{v+1/2}{v-1/2}=\frac1v+O(v^{-2})
\]
and $1$-separation. They make harmonic mass literally logarithmic occupancy and isolate overlap/resonance among the combs as the central issue.

## 6. Proved structural advances from the search

### Fixed integral lattices

If $A\subset c\mathbb N$ for one fixed $c>0$, then both requested
conclusions hold. Admissibility makes the integer index set primitive. A
self-contained rough-multiple density argument proves
\[
\sum_{n\in P}\frac1{n\log n}<\infty
\]
for every primitive integer set $P$; scaling by $c$ changes only finitely many
initial terms and a constant factor. The complete proof is in `PROOF.md` and
`attempts/rational_primitive.md`.

This does not cover an arbitrary rational commensurability class: there are
infinite admissible rational sets whose reduced denominators contain
infinitely many distinct primes, so no global representation $A\subset
c\mathbb N$ exists.

### Finite rationalization and the thick-integer reduction

Every finite admissible real configuration can be approximated arbitrarily
closely by an admissible configuration $\{n_i/Q\}$ satisfying
\[
|kn_i-n_j|\ge Q
\quad(i\ne j, k\ge1).
\]
The proof first dilates by $1+\varepsilon$ to create strict margin, then makes
a sufficiently small rational perturbation; only finitely many multipliers
need direct control. Consequently the uniform estimate
\[
\sum_{n\in S}\frac{Q}{n\log(n/Q)}\le C_a
\quad(S\subset[aQ,\infty))
\]
for all finite $Q$-admissible $S$ would prove the first conclusion for every
real admissible set. This sufficient estimate is open and may be stronger
than the original infinite assertion.

On a fixed grid, for $m<n$ and $r=n\bmod m$, compatibility is exactly
\[
Q\le r\le m-Q.
\]
This is the exact graph used by `computational/discrete_skeleton_exact.py`.

### Fixed-prefix torus theorem

For a finite prefix $B=\{x_1,\ldots,x_m\}$, let $\mathbb H_B$ be the orbit
closure of $t(1/x_1,\ldots,1/x_m)$ in $\mathbb T^m$, and let $p(B)$ be the
Haar measure of the box where every coordinate has distance at least
$1/(2x_i)$ from an integer. Half-unit thickening and fixed-prefix
equidistribution give
\[
\limsup_{T\to\infty}\frac{H_A(T)}{\log T}\le p(B).
\]
In particular, if the reciprocals are $\mathbb Q$-linearly independent and
their reciprocal mass diverges, then $p(B)=\prod_{x\in B}(1-1/x)\to0$ and
the second requested conclusion holds. The missing ingredient for the full
problem is a carrier-conditioned estimate when rational relations persist,
plus scale-uniform discrepancy for the stronger series.

### Exact reciprocal blocks and the concatenation obstruction

For integers $M\ge2$ and $T\ge(2M-2)(2M-1)$,
\[
B(T,M)=\{T/j:M\le j<2M\}
\]
is admissible. At $T=4M^2$ it has harmonic mass $3/8+O(1/M)$ and weighted
mass $\asymp1/\log M$. Thus single-scale density is genuinely maximal.
However, such full blocks cannot simply be concatenated: even one fixed old
anchor forces dilution, and the exact cross condition is
\[
|kTq-Sp|\ge pq
\]
for an old $T/p$ and a later $S/q$. The surviving counterexample question is
whether suitably thinned positive-density reciprocal blocks can be appended
at geometrically controlled scales.

### Resonance facts

At a fixed target, multiplier labels of overlapping half-unit tubes form a
primitive integer set, but their cardinality and even prime-reciprocal
weighted multiplicity can be arbitrarily large. Common-center constructions
$\{T/p\}$ show that bounded multiplicity, naive variance, and unconditional
prime-filter disjointness are false. Below the product scale, a determinant
identity does force repeated pairwise overlaps onto one rational slope; the
open step is to charge these primitive slope labels across many source
scales. See `attempts/resonance_depletion.md` and
`attempts/tube_charging.md`.

## 7. Focused second wave on the $Q$-thick reduction

The uniform $Q$-thick estimate remains neither proved nor refuted. The
following refinements are now established.

1. For the actual weight $f(x)=1/(x\log x)$, the prime set is the unique
   maximizer among all finite real admissible $A\subset[2,10]$. This is a
   continuum theorem, hence simultaneous over every rational grid. Its proof
   uses the exact safe bands of the least point and is recorded in
   `attempts/qthick_bottleneck.md`.
2. Crystallization is false for a general decreasing objective. The
   $2$-grid set $\{7/2,5,6,8,9\}$ beats every primitive integer subset of
   $[2,9]$ for $g(x)=1/(x+5)$, by the exact gap $1/7956$. It does not beat
   the prime set for either target in Problem 143.
3. Far-side floor/ceiling rounding plus logarithmic interval sampling extracts
   a primitive rounded subset carrying an $\Omega(1/\log X)$ fraction of the
   target weight below $X$. Fixed endpoint rounding can be globally
   inconsistent, so removing this logarithmic loss requires a mass-sensitive
   treatment of implication cycles.
4. A local tube family indexed by multipliers $F$ has exact admissible
   capacity equal to the divisibility width of $F$; common-center reciprocal
   blocks attain it. Consequently a static one-target incidence estimate
   cannot improve on divisibility width.
5. For every fixed $R$, a primitive integer set can carry at least
   $3/(256R)$ harmonic mass in each of $R$ arbitrarily widely separated
   narrow shells. This rules out a fixed-arity support-only obstruction, but
   not every quantitative inequality involving finitely many shells.
6. For every integer $a\ge5$, the admissible three-point set
   \[
   \{a+1/2,\ a^2-1/2,\ (a^2-1)^2-1/2\}
   \]
   has no primitive floor/ceiling labeling. Its cheapest deletion has weight
   $\asymp1/(a^4\log a)$, so this gadget does not refute bounded-weight
   deletion; it shows that any proof must charge whole implication cycles.

Exact computations for $Q\in\{1,2,3,4\}$ at cutoffs $10,14$ and for
$Q\in\{2,4,6,8\}$ at cutoff $18$ found that the harmonic and dyadic-log
optima, including a separately optimized forced-off-lattice comparison,
remain strictly crystallized on $Q\mathbb N$. This is finite evidence only
and does not evaluate the transcendental target weight.

## 8. Third focused wave: cumulative packet and cycle excess

### Quotient-rough fiber packets

For a $Q$-admissible numerator $n=Qb+r$, put $\theta=r/Q$ and
\[
U_b=\{u:p\mid u\Rightarrow p\ge b\},\qquad C_b=bU_b,
\]
\[
K_n=[(\theta+1/2)/b,(\theta+1)/b).
\]
The product packets $C_b\times K_n$ are pairwise disjoint. Carrier
intersection forces quotient bins to be comparable, say $c=kb$, while
$Q$-admissibility gives $kr-s\ge Q$ and separates the corresponding fibers.
Their carrier density is
\[
\delta_b=\frac1b\prod_{p<b}(1-1/p)\gg\frac1{b\log b},
\]
the exact order of the target weight. This proves a pointwise fiber-packing
bound, but its logarithmic integral has unbounded depth.

The remaining explicit Hall target uses periodic physical packets
\[
R_n=\{nu+j:u\in U_b,\ 0\le j<Q\}.
\]
A uniform aggregate inequality
\[
d\left(\bigcup_{n\in T}R_n\right)
\gg_a\sum_{n\in T}d(R_n)
\]
for every $T$ in a $Q$-admissible set would prove the required uniform
$Q$-estimate. Pairwise disjointness is false; the aggregate inequality is
open. See `attempts/qthick_fiber_packets.md`.

### Weighted endpoint-clause excess

Injective rounding is unnecessary. By $1$-separation, at most two points can
receive one adjacent integer label, and their total target weight is at most
four times that label's weight. Hence a primitive set of distinct image
labels still transfers the primitive integer theorem with a constant loss.

For the strict-divisibility endpoint $2$-CNF, retain one multigraph edge per
clause and define
\[
\Xi_f(G)=\int_0^\infty
\sum_{C\in\operatorname{comp}(G_t)}(|E(C)|-|V(C)|)_+\,dt,
\]
where $G_t$ is induced by vertices of weight at least $t$ and the sum is over
components. A maximum-weight pseudoforest argument proves that deleting
variables of total weight at most $\Xi_f(G)$ makes the formula satisfiable.
Therefore
\[
\sum_{x\in F}f(x)\le\Xi_f(G_F)+4C_{\rm prim}.
\]
A uniform bound for $\Xi_f$ would solve the problem. Parallel clauses are
essential. See `attempts/weighted_clause_excess.md`.

### Sharp shell obstruction

Neither endpoint route admits a summable shell-by-shell estimate. There are
admissible mixed integer/half-integer sets in $[N,3N]$ whose least deletion
weight permitting primitive adjacent rounding is $\Theta(1/\log N)$. There
are also fixed seven-point, strict-divisibility contradictory cores in
$[t,7t]$, and linearly many disjoint copies fit in one shell. Thus
contradictory cycles need not cause quadratic scale growth, and their total
repair cost can saturate the natural shell order. The unresolved issue is
whether critical shells can recur cross-admissibly with divergent total
weight. See `attempts/rounding_shell_obstructions.md`.
