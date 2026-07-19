# Uniform finite-to-PD transfer: what is valid and what is not

## Purpose

This note audits the proposed passage from additive functions on
`[1,N]` to a Poisson--Dirichlet partition.  The conclusion is mixed.

* There is a clean uniform transfer theorem for a bounded number of
  logarithmic prime bands bounded away from `0`.  The band weights may
  be arbitrary and may depend on `N`; compactness of the weights is not
  needed.
* There is no such transfer uniformly over arbitrary `N`-dependent
  rational step profiles.  Microscopic steps can be aligned with the
  finitely many prime locations.  An explicit construction below makes
  the finite statistic injective while its PD analogue is zero with
  probability tending to one.
* Consequently a constant-gap theorem for continuum step profiles, by
  itself, does **not** imply a constant gap for all completely additive
  functions on `[1,N]`.  One needs an additional arithmetic regularity
  lemma which replaces arbitrary prime weights by macroscopic band
  weights with *exact* agreement outside a set of vanishing harmonic
  mass.

The obstruction is about exact atoms.  Uniformly close real-valued
profiles are not an adequate substitute for exactly equal weights.

## 1. Point-process notation and the background limit theorem

Let `U_N` be uniform on `[1,N]` and put

\[
  \Xi_N=\sum_{p\le N}v_p(U_N)\,
          \delta_{\log p/\log N}.
\]

Let `(V_i)_{i\ge1}` have the `PD(1)` distribution and put

\[
  \Xi=\sum_{i\ge1}\delta_{V_i}.
\]

We use the following standard form of the Billingsley prime-factor
limit theorem.

> **PD input.**  For every fixed `eta>0`, the restriction of `Xi_N` to
> `[eta,1]` converges in distribution, as a finite point measure, to the
> restriction of `Xi` to `[eta,1]`.

Equivalently, counts in finitely many intervals whose deterministic
endpoints have zero `Xi`-mass converge jointly.  The exact named
formulation of this standard theorem should be checked if it is cited
in a final proof; only the displayed fixed-`eta` consequence is used
here.

Two elementary facts give the uniformity needed below.  First,

\[
 \sum_i V_i=1\quad\hbox{a.s.},
 \qquad
 \mathbb E\Xi(dx)=\frac{dx}{x}.
 \tag{1}
\]

Second, for a fixed `eta>0` and `eta <= a < b <= 1`,

\[
\begin{split}
 \mathbb E\Xi_N((a,b])
 &=\sum_{N^a<p\le N^b}\mathbb E v_p(U_N)\\
 &\le \sum_{N^a<p\le N^b}\frac1{p-1}
  =\log(b/a)+o_{\eta}(1).
\end{split}
\tag{2}
\]

The last equality is the standard Mertens estimate, uniformly on
`[eta,1]`; replacing `1/(p-1)` by `1/p` costs `o_eta(1)`.  In
particular, an interval of normalized-log length `h` contained in
`[eta,1]` is hit with probability at most

\[
  O_\eta(h)+o_\eta(1).
\tag{3}
\]

The same bound for `Xi` follows from (1).

## 2. A valid uniform transfer theorem

Fix `eta>0` and an integer `K`.  For

\[
 \theta=(a_0,\ldots,a_K),\qquad
 \eta=a_0\le a_1\le\cdots\le a_K=1,
\]

write `I_j(theta)=(a_{j-1},a_j]` and define the count vectors

\[
 C_N(\theta)=(\Xi_N(I_1),\ldots,\Xi_N(I_K)),\qquad
 C(\theta)=(\Xi(I_1),\ldots,\Xi(I_K)).
\]

Degenerate intervals are allowed.

> **Theorem 2.1 (uniform bounded-band transfer).**  For fixed `eta` and
> `K`,
> \[
>  \sup_\theta
>  d_{\rm TV}\bigl({\cal L}(C_N(\theta)),
>                       {\cal L}(C(\theta))\bigr)\longrightarrow0.
>  \tag{4}
> \]
> Consequently, uniformly over `theta`, arbitrary rational (indeed
> arbitrary real) band weights `q_1,...,q_K`, and arbitrary targets
> `t`,
> \[
> \left|
>  \mathbb P\left(\sum_jq_j C_{N,j}(\theta)=t\right)
>  -
>  \mathbb P\left(\sum_jq_j C_j(\theta)=t\right)
> \right|=o_{\eta,K}(1).
> \tag{5}
> \]
> The weights and target in (5) may depend on `N`.

### Proof

Every point counted by either vector has size at least `eta`, while
the total mass is at most one.  Hence both count vectors take values in
the fixed finite set

\[
 {cal S}_{\eta,K}
 =\{c\in\mathbb Z_{\ge0}^K:\ \sum_jc_j\le\lfloor1/\eta\rfloor\}.
 \tag{6}
\]

For each fixed `theta`, the PD input and the fact that a PD part has a
continuous marginal distribution imply convergence in distribution of
the count vector.  Since the state space (6) is finite, this is total
variation convergence.

It remains to make the convergence uniform in the endpoints.  Couple
the count vectors belonging to two parameter points `theta,theta'`
using the same point measure.  If
`max_j |a_j-a'_j| <= h`, the two vectors can differ only if a point lies
within distance `h` of one of the `K-1` moving endpoints.  Equations
(1)--(3) therefore give

\[
 \mathbb P(C_N(\theta)\ne C_N(\theta'))
 +\mathbb P(C(\theta)\ne C(\theta'))
 \le O_{\eta,K}(h)+o_\eta(1).
 \tag{7}
\]

Choose a finite `h`-net of the compact endpoint simplex.  Pointwise
total-variation convergence on the net, followed by (7), proves (4)
after first sending `N` to infinity and then `h` to zero.

For fixed `theta` and weights, the statistic in (5) is the pushforward
of the count vector under the map
`c -> sum_j q_j c_j`.  Total variation cannot increase under a
pushforward.  This proves (5), with no compactness or boundedness
assumption on the weights.  `square`

### Equality-pattern compactness

There is an equivalent useful interpretation of the last paragraph.
On the finite set (6), a weight vector induces an equivalence relation

\[
 c\sim_q c'\quad\Longleftrightarrow\quad q\cdot c=q\cdot c'.
\]

Only finitely many equivalence relations on (6) exist.  Thus every
sequence of rational weight vectors has a subsequence on which the
entire pattern of exact equalities is constant.  This is the right
compactness for exact atoms; numerical convergence of the weights is
neither needed nor sufficient.

### Conditional consequence

Suppose a continuum argument proves, for some `delta>0`,

\[
 \sup_{\theta,q}\sup_{t\ne0}
 \mathbb P\left(\sum_jq_jC_j(\theta)=t\right)\le1-\delta
 \tag{8}
\]

for the fixed class `(eta,K)`.  Theorem 2.1 then gives the same bound,
up to `o(1)`, for finite completely additive functions which vanish on
primes below `N^eta` and are constant on those `K` macroscopic bands.
This is a genuine finite consequence of a PD atom bound.

It does not cover `eta -> 0`, `K -> infinity`, or arbitrary variation
among primes in the same logarithmic band.

## 3. Exact-safe approximation of arbitrary prime weights

Let `w=(w_p)` and `w'=(w'_p)` be two systems of prime weights, and set

\[
 F_w(n)=\sum_pv_p(n)w_p,
 \qquad
 D=\{p\le N:w_p\ne w'_p\}.
\]

> **Lemma 3.1 (harmonic mismatch coupling).**
> \[
> d_{\rm TV}({\cal L}(F_w(U_N)),{cal L}(F_{w'}(U_N)))
> \le \mathbb P(\exists p\in D:p\mid U_N)
> \le \sum_{p\in D}\frac1p.
> \tag{9}
> \]

**Proof.**  On the event that no prime in `D` divides `U_N`, the two
statistics agree exactly.  Couple them using the same `U_N` and apply
the union bound
`P(p|U_N)=floor(N/p)/N <= 1/p`.  `square`

Thus an exact-atom-preserving band approximation would follow from a
partition into bands and values `q_j` satisfying

\[
 \sum_j\sum_{\substack{p\text{ in band }j\\w_p\ne q_j}}\frac1p=o(1).
 \tag{10}

Condition (10) asks for *exact equality* of the original and band
weights outside a set of vanishing prime harmonic mass.  An estimate
such as `|w_p-q_j| <= o(1)` is useless for exact atoms: changing every
weight by a distinct tiny rational perturbation can split every old
atom.

There is no unconditional approximation theorem of the form (10).
For example, color the primes in every macroscopic band alternately
with weights `0` and `1`.  Any one-valued approximation to that band
disagrees with a positive proportion of its harmonic mass.  More
strongly, take all prime weights distinct.  A high-concentration
hypothesis might force modal regularity such as (10), but that is a new
arithmetic lemma, not a consequence of PD convergence or compactness.

## 4. Counterexample to arbitrary-profile uniform transfer

The failure can be made maximal even when the profiles are rational
step functions.

> **Proposition 4.1 (microscopic arithmetic alignment).**  There are
> rational step functions `phi_N:(0,1] -> Q` such that
> \[
>  S_N(n):=\int\phi_N\,d\Xi_N(n)
> \]
> is injective on `[1,N]`, whereas for the PD statistic
> \[
>  S_N^{PD}:=\int\phi_N\,d\Xi
> \]
> one has
> \[
>  \mathbb P(S_N^{PD}=0)\longrightarrow1.
> \tag{11}
> \]
> In particular the total-variation distance between the finite and PD
> laws tends to one, and no uniform transfer theorem over arbitrary
> `N`-dependent rational step profiles is possible.

### Proof

List the primes up to `N` as `p_1<...<p_m` and set

\[
 x_i=\frac{\log p_i}{\log N},
 \qquad B=1+\lfloor\log_2N\rfloor.
\]

Choose pairwise disjoint open intervals `J_i` around the finitely many
points `x_i`, so small that

\[
 \sum_{i=1}^m\int_{J_i}\frac{dx}{x}\le N^{-2}.
 \tag{12}
\]

This is possible because the set of points is finite and every `x_i`
is positive.  Define the rational step function

\[
 \phi_N(x)=B^{i-1}\quad(x\in J_i),
 \qquad
 \phi_N(x)=0\quad(x\notin\cup_iJ_i).
 \tag{13}
\]

All prime-factor atoms of `Xi_N` occur at the points `x_i`, so

\[
 S_N(n)=\sum_{i=1}^m v_{p_i}(n)B^{i-1}.
 \tag{14}
\]

Every digit `v_{p_i}(n)` is at most `floor(log_2N)<B`.  Hence (14) is
the base-`B` encoding of the prime-exponent vector and is injective by
unique factorization.  In particular every finite atom has probability
exactly `1/N`.

For PD(1), (1), (12), and Markov's inequality give

\[
 \mathbb P\left(\Xi(\cup_iJ_i)>0\right)
 \le\mathbb E\Xi(\cup_iJ_i)
 =\sum_i\int_{J_i}\frac{dx}{x}
 \le N^{-2}.
\]

Outside this event the statistic (13) is zero, which proves (11).
`square`

This example also shows why allowing the number of bands to grow
destroys the finite-state compactness in Theorem 2.1.  A step profile
can resolve the discrete prime support much more finely than the PD
limit can see.

## 5. A second obstruction: the linear null direction

Even benign numerical approximation is insufficient for exact atoms.
For a PD partition, the profile `phi(x)=x` satisfies

\[
  \sum_i\phi(V_i)=\sum_iV_i=1\quad\text{a.s.}
  \tag{15}
\]

Let

\[
  \phi_K(x)=\frac{\lfloor Kx\rfloor}{K}.
\]

Then `phi_K -> phi` uniformly.  Moreover

\[
  \sum_i\phi_K(V_i)<1\quad\text{a.s. for every fixed }K,
  \qquad
  \sum_i\phi_K(V_i)\longrightarrow1\quad\text{a.s.}
  \tag{16}

Indeed, PD has positive total mass in parts smaller than `1/K`, all of
which are rounded to zero, giving the strict inequality.  For the
convergence, the rounding loss from parts at least `1/K` is at most
`K^{-1}` times their number, while the total mass of parts smaller than
`1/K` tends to zero; the former also tends to zero almost surely
because the number of parts above `1/K` is `o(K)` (or directly from
summability of the partition).

Thus the limiting functional has an atom of mass one at `1`, although
none of the approximating functionals has an atom at `1`.  Portmanteau
only yields an upper bound by the mass-one limiting atom and hence gives
no anti-concentration.  Any continuum proof must either handle this
linear direction quantitatively or use exact equality-pattern
information before taking a limit.

## 6. Behavior near zero and the exact remaining lemma

Restriction to `[eta,1]` is essential.  The number of PD parts near
zero is infinite, and the number of small prime factors of a uniform
integer is not uniformly bounded.  Therefore arbitrary additive
functionals of the small factors are not tight.  A numerical condition
such as

\[
 \mathbb E\sum_{p\le N^\eta}v_p(U_N)|w_p|=o(1)
\]

would control convergence in probability but still would not preserve
exact atoms.  The exact-safe condition is instead that the contribution
from the discarded primes be identically zero with probability
`1-o(1)`, for example

\[
 \sum_{\substack{p\le N^\eta\\w_p\ne0}}\frac1p=o(1).
 \tag{17}

\]

For the finite product-length problem no estimate like (17) is known
for an arbitrary putative high-density grading.

The precise missing bridge for the PD route can be stated as follows.

> **Macroscopic exact-profile lemma (needed, not proved).**  If a
> completely additive `F_N` has
> `P(F_N(U_N)=1) -> 1`, then, after deleting primes of total harmonic
> mass `o(1)`, its weights are constant on `O(1)` (or on a uniformly
> controllable number of) logarithmic bands bounded away from zero, and
> the remaining small-prime contribution can be removed without
> changing `F_N(U_N)` with probability `1-o(1)`.

The overlap/rectangle methods elsewhere in this directory give local
equalities between prime weights when many common cofactors survive.
They do not currently yield this global harmonic-mass statement across
all scales.  Proposition 4.1 shows that compactness and the PD limit
cannot supply it for free.

## 7. Verdict for the continuum route

Theorem 2.1 validates the finite-to-continuum step for every fixed
macroscopic bounded-complexity profile, uniformly even over
`N`-dependent rational weights.  This is the maximal conclusion
available from ordinary PD convergence without additional regularity.

A universal finite constant gap **does not follow** from a continuum
constant-gap theorem over arbitrary step profiles: the required uniform
transfer is false by Proposition 4.1, and numerical step approximation
is invalid for exact atoms by (16).  To revive the route, one must prove
the macroscopic exact-profile lemma (or an alternative quantitative
stability theorem which directly treats the linear null direction and
microscopic arithmetic alignment).

