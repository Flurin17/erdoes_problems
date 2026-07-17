# Reciprocal blocks, self-thinning, and the concatenation bottleneck

## 1. Status of this route

This route seeks a counterexample assembled from finite blocks having harmonic
mass bounded below.  Such blocks exist in isolation, but merely putting them
far apart does not preserve admissibility.  The exact obstruction is now
isolated below as a controlled-scale concatenation problem.  No counterexample
is claimed.

For distinct `a<b`, the ordered quantifiers reduce to

\[
  |ka-b|\geq 1\qquad(k\in\mathbb Z_{\geq1}).                 \tag{1}
\]

Indeed, the reverse orientation at `k=1` is the same inequality and, for
`k>=2`, `kb-a=(k-1)b+(b-a)>1`.  Every cross-block statement below either
assumes that all new points exceed all old points by at least one, or checks
both orientations explicitly.

## 2. Dense reciprocal blocks

For a finite set of positive integers `P`, put

\[
  B(T,P)=\{T/p:p\in P\}.
\]

### Lemma 2.1 (exact internal criterion)

For `i>j` in `P`, define

\[
 \rho_j(i)=\min_{k\geq1}|i-kj|.
\]

Then

\[
 B(T,P)\text{ is admissible}
 \quad\Longleftrightarrow\quad
 T\rho_j(i)\geq ij\quad(i>j\text{ in }P).                 \tag{2}
\]

**Proof.**  The smaller of `T/i,T/j` is `T/i`.  Substitution in (1) gives

\[
 \min_{k\geq1}\left|k\frac Ti-\frac Tj\right|
   =\frac{T}{ij}\min_{k\geq1}|kj-i|.
\]

This is at least one exactly when (2) holds.  Notice that equality is
permitted.  \(\square\)

In particular, if `P` is a divisibility antichain and

\[
 T\geq\max_{p\ne q\in P}pq,                               \tag{3}
\]

then `B(T,P)` is admissible: the integer `kq-p` never vanishes and hence has
absolute value at least one.  For the full interval

\[
 P_M=\{M,M+1,\ldots,2M-1\},
\]

the sharp threshold in (2) is

\[
 T_M=(2M-2)(2M-1).                                        \tag{4}
\]

The upper bound follows from `rho>=1` and `ij<=T_M`; equality is forced by
the adjacent pair `i=2M-1,j=2M-2`.  Thus a reciprocal block can be as dense
as the elementary additive block, at a comparable scale.  Its weights are

\[
 \sum_{x\in B(T,P_M)}\frac1x
   =\frac{M(3M-1)}{2T},                                   \tag{5}
\]

and

\[
 \frac{H(B)}{\log(T/M)}
 \leq \sum_{x\in B(T,P_M)}\frac1{x\log x}
 \leq \frac{H(B)}{\log(T/(2M-1))}.                        \tag{6}
\]

At `T=4M^2`, (5) tends to `3/8` and (6) is of order
`1/log M`.  Consequently, blocks at geometrically growing scales would
disprove both requested conclusions if they could be concatenated with a
uniform positive denominator density.

## 3. Cross-block determinants

Let `x=T/p` be old and `y=S/q` be new, and assume `y>=x+1`.  Their exact
compatibility condition is

\[
  |kTq-Sp|\geq pq\qquad(k\geq1).                           \tag{7}
\]

Without the ordering assumption one must additionally check
`|kSp-Tq|>=pq`.  Formula (7), rather than scale separation, is the
concatenation constraint.

For example, the internally admissible and well-separated blocks

\[
 B(16,\{3,4\})=\{16/3,4\},\qquad
 B(400,\{11,\ldots,20\})
\]

do not concatenate, since

\[
 \left|6\cdot4-\frac{400}{17}\right|=\frac8{17}<1.
\]

If `S=LT`, (7) becomes

\[
 T\,\operatorname{dist}(Lp,q\mathbb Z_{\geq1})\geq pq.   \tag{8}
\]

Thus avoiding exact resonance is not enough unless `T` already dominates
`pq`.  This is the quantitative margin lost in informal divisibility
constructions.

There is one exact but ultimately harmless bounded-denominator construction.
Fix `Q` and `T_0>=Q^2`; let `M_i` be distinct primes greater than `Q`, and let
`P_i subset {1,...,Q}` be divisibility antichains.  Then

\[
 \bigcup_i\{T_0M_i/p:p\in P_i\}                           \tag{9}
\]

is admissible.  Internally this follows from (3).  Across two blocks, an
equality `kM_iq=M_jp` would force `M_i` to divide `M_jp`, which is impossible,
and every nonzero integer determinant, multiplied by `T_0/(pq)`, has size at
least one.  However, (9) has a fixed common rational lattice: after multiplying
by `lcm(1,...,Q)/T_0`, it is an integer primitive set.  The common-ray theorem
therefore proves convergence of its `1/(x log x)` series.  Unbounded
denominators, where (8) no longer follows from nonvanishing, are essential.

## 4. Generic insertion and why the elementary estimate stops

Let `F` be a finite admissible old set and let `I` be an interval of possible
numerators `S` of length `L`.  For fixed `a in F` and denominator `q`, the bad
set is

\[
 \{S\in I:\ |ka-S/q|<1\text{ for some }k\geq1\}
 =I\cap\bigcup_{k\geq1}(kaq-q,kaq+q).                    \tag{10}
\]

At most `L/(aq)+2` intervals on the right meet `I`, whence

\[
 \mu(\text{bad}(a,q))\leq \frac{2L}{a}+4q.               \tag{11}
\]

There are two importantly different uses of (11).

* A union bound seeking one `S` for which *every* `q in P` is safe has main
  term `2L |P| H(F)`.  Its positivity condition is approximately
  `2|P|H(F)<1`, so it cannot append a full growing block.
* If `S` is selected first and unsafe denominators are then discarded, let
  `N_bad(S)` count them.  Integration of (11) gives some `S in I` for which

  \[
  N_{\rm bad}(S)
   \leq 2|P|H(F)+\frac{4|F|}{L}\sum_{q\in P}q.             \tag{12}
  \]

  Hence a positive fraction is retained when `H(F)<1/2` and `L` is large.

After thinning, internal admissibility remains true.  But (12) spends a finite
harmonic budget and says nothing once `H(F)>=1/2`.  Random choice, generic
perturbation, and first-moment deletion therefore do not by themselves give
an infinite divergent construction.  A successful random construction would
need a lower bound for the *overlap* of the combs in (10), valid after the
old harmonic mass becomes arbitrarily large.

Perturbation also has no automatic safety margin: the sharp block (4) has
pairs at distance exactly one from a multiple.  A perturbation term is
`k epsilon_i-epsilon_j`, with `k` depending on the pair.  Finite strict-slack
blocks have an open neighborhood of admissible perturbations after finitely
many relevant multipliers are bounded, but that observation supplies no
uniform radius as the block grows.

## 5. A rigorous one-anchor packing obstruction

For `a>2` set

\[
 E_a=\{y>a:|ka-y|\geq1\text{ for all }k\geq1\}.
\]

Its safe components are the closed intervals

\[
 [ka+1,(k+1)a-1],                                        \tag{13}
\]

each of length `a-2`.  Put `r=floor(a-1)`.  A `1`-separated subset has at
most `r` points in each component, and an interval of length `L` meets at
most `L/a+2` components.  Therefore

\[
 \#(C\cap E_a)\leq r(L/a+2)                               \tag{14}
\]

for every `1`-separated `C` contained in an interval of length `L`.

The full reciprocal block `B(S,{m+1,...,2m})` has `m` points and span

\[
 L_S=S\left(\frac1{m+1}-\frac1{2m}\right)
     =\frac{S(m-1)}{2m(m+1)}.
\]

If it is compatible with `a`, (14) forces

\[
 S\geq \frac{2am(m+1)}{m-1}\left(\frac mr-2\right).     \tag{15}
\]

For `2<a<3`, `r=1`; in particular `S=4m^2` fails for all sufficiently large
`m` (the exact inequality is `(a-2)m(m-1)>2a`).  Even one early anchor can
force dilution of the naive block.

At `a=2`, (13) degenerates to the odd integers.  If every `S/q`,
`m<q<=2m`, were safe, all would be odd integers.  Then `S` is an integer and
`v_2(S)=v_2(q)` for every such `q`, impossible because the denominator interval
contains different `2`-adic valuations.  Thus a full consecutive reciprocal
block cannot follow the anchor `2`; thinning is unavoidable.

A similar obstruction kills repeated full additive grids.  If
`G={t,t+1,...,t+N-1}` and the interval
`[t+1/2,t+N-3/2]` has length at least `a`, it contains a multiple of `a`.
The nearest point of `G` is then within `1/2`, contradicting compatibility.
Thus the locally sharp additive block also cannot simply be repeated across
scales.

## 6. Divisor cubes and exact resonance

Let `N=prod_{i=1}^{2r}p_i` for distinct primes, and take `P` to be the
middle layer of its divisor cube.  Then `N/q`, `q in P`, are integers forming
a divisibility antichain, so the block is admissible without the crude
condition (3).  This is exact resonance in its most favorable form, but it
returns to a common integer ray and cannot furnish a counterexample.

Moreover, exponential cardinality is misleading for the weighted objectives.
The reciprocal mass of the complementary middle layer is

\[
 e_r(1/p_1,\ldots,1/p_{2r})
 \leq \frac1{r!}\left(\sum_{i=1}^{2r}\frac1{p_i}\right)^r
 \leq \left(\frac{e\log(2r+1)}r\right)^r.                 \tag{16}
\]

Here the first inequality follows by expanding the power and the second from
`p_i>=i+1` and `r!>=(r/e)^r`.  Since every middle-layer integer is at least
`2^r`, its logarithm is at least `r log 2`; (16) also bounds the target
weighted mass after division by `r log 2`.  It tends rapidly to zero.  Nested
divisor cubes can additionally create cross-level divisibilities, while
disjoint prime alphabets again give a single primitive integer set.  Thus
divisor-cube resonance explains large comb overlap, but does not presently
give the required real, varying-scale construction.

## 7. The exact missing concatenation lemma

For a finite admissible prefix `F`, constants `C>=4`, and `m` large enough
that every point of `B(S,Q)` below is at least `max(F)+1`, define

\[
 \sigma_F(m,C)=
 \sup_{4m^2\leq S\leq Cm^2}\frac1m
 \max\{|Q|:Q\subset\{m+1,\ldots,2m\},\ B(S,Q)
             \text{ is cross-compatible with }F\}.       \tag{17}
\]

Internal compatibility is automatic.  If `rho=|Q|/m`, then

\[
 \frac{\rho}{C}
 \leq\sum_{q\in Q}\frac qS
 \leq\frac{\rho}{2}.                                     \tag{18}
\]

The weakest clean lemma that would make this route a counterexample is:

> There are constants `C,delta>0` and `R>1` and an infinite induction with
> `sigma_{F_j}(m_{j+1},C)>=delta`, full scale separation, and
> `m_{j+1}<=R m_j`.

Indeed, (18) gives a fixed positive harmonic contribution per block, while
`log m_j=O(j)`.  The partial harmonic sums are then not `o(log n)`, and (6)
gives a divergent comparison with the harmonic series for
`sum 1/(x log x)`.  The upper scale bound is indispensable: the existence of
positive-density blocks at arbitrarily enormous scales would not imply either
failure.

The elementary estimate (12) proves this statement only while
`H(F_j)<1/2`; the one-anchor estimate (15) shows that even full blocks already
fail.  The unresolved mathematical question is whether structured overlap of
the old forbidden combs keeps (17) uniformly positive for a suitably thinned
sequence, or whether `sigma_{F_j}` must decay.  This is the first unsupported
step of the block-counterexample route.

## 8. Exact finite falsification model

For a rational prefix `F` and fixed `m,C`, every change in the safe-denominator
set occurs at a rational breakpoint

\[
 S=q(ka\pm1),\qquad a\in F,\quad m<q\leq2m,             \tag{19}
\]

inside `[4m^2,Cm^2]`; only finitely many `k` meet that interval.  An exact
sweep should sort (19), evaluate every open cell **and every breakpoint**
(endpoints are safe because equality is allowed), and maximize the surviving
denominator weight.  Direct verification of a rational pair `u<v` needs only

\[
 1\leq k\leq\left\lfloor\frac{v+1}{u}\right\rfloor.
\]

For more general finite denominator pools, fix `T` and form the incompatibility
graph with edge `{i,j}` exactly when `T rho_j(i)<ij`; after deleting vertices
that conflict with `F`, maximum harmonic or logarithmic block weight is a
maximum-weight independent-set problem with vertex weights respectively
`i/T` and `i/[T log(T/i)]`.  This computation can falsify proposed uniform
bounds and expose gcd/residue patterns, but a finite positive result is not an
infinite concatenation proof.

## 9. Dependency graph and next action

The isolated-block lemma, determinant criterion, self-thinning estimate,
one-anchor obstruction, and weight conversion are proved above.  A negative
solution through this route has exactly two remaining dependencies:

1. prove a controlled-scale positive lower bound of the form (17), using
   overlap rather than a union bound; and
2. iterate it while maintaining the hypotheses and full cross-compatibility.

Conversely, a quantitative upper bound forcing `sigma_{F_j}(m,C)` to decay
along every growing admissible prefix would eliminate repeated positive-mass
blocks and feed directly into a multiscale positive proof.  The next useful
experiment is therefore the exact sweep (19) on prefixes generated by the
optimizer itself, grouped by gcd and residue signature, followed by a proof of
whichever overlap law persists.
