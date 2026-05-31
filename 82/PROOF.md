# Proof Attempt For Erdos Problem 82

Target theorem:

```text
For every function C(n) -> infinity, eventually every graph on n vertices
contains a regular induced subgraph on at least C(n) log n vertices.
```

Equivalently:

```text
G(k) <= 2^{o(k)}.
```

## Definitions

Let `reg(G)` denote the maximum order of a regular induced subgraph of `G`.
Then

```text
F(n) = min_{|V(G)|=n} reg(G),
G(k) = min { m : F(m) >= k }.
```

## Reconstructed Known Bound: Ramsey Lower Bound

Every clique and every independent set is a regular induced subgraph.  Hence
`reg(G) >= max{omega(G), alpha(G)}`.  By the diagonal Ramsey bound, every
`n`-vertex graph contains a clique or independent set of order at least
`c log n` for an absolute constant `c>0`.  Therefore `F(n) >= c log n`, or
equivalently `G(k) <= 2^{O(k)}`.

## Proposition 0A: Linear Homogeneous Sets Are The Hard Ramsey Regime

For every `epsilon>0` there is a `delta>0` such that, for all sufficiently
large `k`, every graph on at least `2^{epsilon k}` vertices contains either
a clique of order `k`, an independent set of order `k`, or both a clique and
an independent set of order at least `delta k`.

Consequently, to prove `G(k)<=2^{o(k)}` it is enough to rule out
counterexamples in which both ordinary Ramsey parameters are linear in `k`.

Proof.  The Erdos--Szekeres bound gives

```text
R(k,l) <= binom(k+l-2,l-1).
```

If `l=floor(delta k)`, then

```text
log_2 R(k,l) <= (k+l) H_2(l/(k+l)) + O(log k),
```

where `H_2` is the binary entropy function.  As `delta -> 0`, the coefficient
`(1+delta)H_2(delta/(1+delta))` tends to `0`.  Choose `delta` so small that
this coefficient is less than `epsilon`.  Then every graph on
`2^{epsilon k}` vertices with no clique of order `k` has an independent set
of order at least `delta k`.  Applying the same argument to the complement
shows that, unless there is already a clique or independent set of order
`k`, both `alpha(G)` and `omega(G)` are at least `delta k`.  Since cliques
and independent sets are regular, this proves the claimed reduction.  QED.

## Lemma 0B: Split Graphs Give No Non-Ramsey Regularity

Let `G` be a split graph with a vertex partition `V(G)=A union B`, where
`A` is a clique and `B` is an independent set.  Then every regular induced
subgraph of `G` is either a clique or an independent set.

Proof.  Let `S` induce a regular graph, and write

```text
X = S cap A,      Y = S cap B,      x=|X|,      y=|Y|.
```

If `X` or `Y` is empty, then `S` is respectively independent or a clique, so
assume both are nonempty.  Since vertices of `X` already have `x-1` neighbors
inside the clique `X`, a common degree `D` on `S` has the form

```text
D = x-1+p,
```

where every vertex of `X` has exactly `p` neighbors in `Y`.  Every vertex of
`Y` has all its neighbors in `X`, so it has common degree `D<=x`.  Hence
`p<=1`.

If `p=0`, then `D=x-1`.  Counting edges between `X` and `Y` gives

```text
0 = yD = y(x-1),
```

so `x=1`; then `S` is independent.  If `p=1`, then `D=x`, so every vertex of
`Y` is adjacent to all vertices of `X`.  Counting cross edges gives

```text
x = yx,
```

and hence `y=1`; then `S` is a clique.  QED.

Thus Proposition 0A's linear clique and independent set reduction is not by
itself a source of extra regularity: the cross edges between one clique and
one independent set may form a split graph, and in split graphs regular
induced subgraphs are exactly the ordinary homogeneous induced subgraphs.

## Lemma 0C: Split Graphs Satisfy The Terminal-Size Partition Target

Let `G` be a split graph on `n` vertices, and put `q=ceil(sqrt n)`.  Then
`V(G)` can be partitioned into at most `q` regular induced subgraphs, each of
order at most `q+1`.

Proof.  Fix a split partition `V(G)=A union B`, where `A` is a clique and
`B` is independent.  Partition `A` into cliques of size at most `q+1`, and
partition `B` into independent sets of size at most `q+1`.  Every part is
regular.  It remains only to count the number of parts.

Let `c=q+1`, and write `a=|A|`, `b=|B|`.  The number of parts is

```text
ceil(a/c) + ceil(b/c).
```

Since `n<=q^2=(q+1)(q-1)+1=c(q-1)+1`, this sum is at most `q`.  Indeed, write
`a=rc+alpha` and `b=sc+beta` with `0<=alpha,beta<c`.  If both remainders are
positive, then

```text
(r+s)c+2 <= a+b <= c(q-1)+1,
```

so `r+s<=q-2`, and the number of parts is `r+s+2<=q`.  If exactly one
remainder is positive, the same inequality with `+1` gives `r+s<=q-1`, so
the number of parts is `r+s+1<=q`.  If neither is positive, then
`(r+s)c<=c(q-1)+1`, hence `r+s<=q-1<=q`.  QED.

Thus split graphs are a barrier for extracting non-Ramsey regularity from one
fixed clique-independent pair, but not a barrier for the terminal-size modular
partition program.

## Reconstructed Known Bound: Bollobas Upper Bound

The literature records a construction, attributed first to Bollobas and then
strengthened by Alon--Krivelevich--Sudakov and Dyson--McKay, showing that the
guaranteed value cannot be much larger than `sqrt(n)`.  The currently recorded
best form is Dyson--McKay's

```text
F(n) << sqrt(n).
```

Equivalently, for some absolute `c>0`,

```text
G(k) >= c k^2
```

for all sufficiently large `k`; Dyson--McKay give the explicit indexed
constant `c=9/163`.

I have not reconstructed the probabilistic construction proof locally yet; the
logical translation is:

```text
G(k) >= c k^2
iff
there exists an n-vertex graph with reg(G) < k for n = floor(c k^2)
iff
F(n) <= C sqrt(n).
```

This is an upper bound on the guaranteed value `F(n)` and is compatible with
the target `F(n)=omega(log n)`.

## Lemma 1: Hole / Antihole Reduction

Let `k >= 4`.  If `G` has no regular induced subgraph of order at least `k`,
then neither `G` nor its complement contains an induced cycle of length at
least `k`.

Proof.  An induced cycle of length `ell >= k` is `2`-regular.  The complement
of an induced cycle of length `ell` is `(ell-3)`-regular.  Since regularity of
an induced subgraph is preserved under graph complementation, either case
gives a regular induced subgraph on `ell >= k` vertices, a contradiction.  QED.

## Lemma 1A: Perfect Graphs Are Polynomially Easy

If `G` is a perfect graph on `n` vertices, then

```text
reg(G) >= sqrt(n).
```

Consequently, a graph with no regular induced subgraph of order at least `k`
and with `n>=k^2` is not perfect.

Proof.  In a perfect graph, `chi(G)=omega(G)`.  Coloring `G` with
`omega(G)` independent sets gives

```text
n <= alpha(G) omega(G).
```

Therefore `max(alpha(G),omega(G)) >= sqrt(n)`.  A clique or independent set
of this order is a regular induced subgraph.  QED.

Together with Lemma 1 and the strong perfect graph theorem, this says that a
large counterexample must contain odd holes or odd antiholes, but all such
holes and antiholes have length less than `k`.  The obstruction is therefore
not imperfection itself, but controlling graphs whose imperfect witnesses are
present only below the target scale.

## Conditional Proposition 1B: A Long-Hole Chi-Bound Would Suffice

For `k>=4`, let `X(k)` be the least number such that every graph with
`omega(G)<k` and with no induced cycle of length at least `k` has
`chi(G)<=X(k)`.  If

```text
X(k) = 2^{o(k)},
```

then `G(k)<=2^{o(k)}`.

Proof.  Let `G` be a graph with no regular induced subgraph of order at least
`k`.  Then `omega(G)<k` and `alpha(G)<k`, since cliques and independent sets
are regular.  By Lemma 1, `G` has no induced cycle of length at least `k`.
Therefore `chi(G)<=X(k)`.  Coloring `G` into `chi(G)` independent sets gives

```text
|V(G)| <= alpha(G) chi(G) < k X(k).
```

Thus every graph on at least `kX(k)` vertices contains a regular induced
subgraph of order at least `k`, so `G(k)<=kX(k)=2^{o(k)}` under the assumed
bound.  QED.

This route is independent of modular lifting.  Known elementary induced-path
or induced-matching recursions give only `2^{O(k log k)}`-type bounds in this
workspace; to settle the problem through this proposition one would need a
genuinely subexponential chi-bound for bounded-clique graphs with no long
holes.

## Lemma 2: Modular Terminal Criterion

Let `q` be a positive integer and let `S` be a vertex set with
`|S| <= q+1`.  If all degrees in `G[S]` are congruent modulo `q`, then
`G[S]` is regular.

Proof.  If `|S|<=q`, every degree in `G[S]` lies in the interval
`[0, |S|-1]`, whose length is at most `q-1`.  Two integers in this interval
that are congruent modulo `q` are equal, so all induced degrees are equal.

It remains to consider `|S|=q+1`.  Then two distinct degrees in
`[0,q]` can be congruent modulo `q` only if they are `0` and `q`.  These two
degree values cannot both occur in a graph on `q+1` vertices: a vertex of
degree `q` is adjacent to every other vertex, while a vertex of degree `0` is
adjacent to none.  Therefore either all degrees are equal, or the only
possible two-value case is impossible.  Thus `G[S]` is regular.  QED.

## Lemma 2A: Near-Terminal Modular Extraction

Let `q` be a positive integer, and let `H` be a `q`-modular graph on
`m=q+s` vertices with `2<=s<q`.  Then `H` contains a clique or independent
set, and hence a regular induced subgraph, on at least

```text
m/(s+1)
```

vertices.

Proof.  Let the common degree residue be `a mod q`, with `0<=a<q`.  Since
all degrees lie in `[0,q+s-1]`, every degree is either `a` or `a+q`.  If only
one of these values occurs, then `H` itself is regular, so assume both occur.
Let `L` be the vertices of degree `a` and `U` the vertices of degree `a+q`.
The second value can occur only if `a+q<=q+s-1`, so `a<=s-1`.

The induced graph `H[L]` has maximum degree at most `a`, hence by the greedy
independence bound it contains an independent set of size at least
`|L|/(a+1)`.

For a vertex of `U`, the number of nonneighbors in all of `H` is

```text
(q+s-1) - (a+q) = s-1-a.
```

Therefore the complement of `H[U]` has maximum degree at most `s-1-a`, so
`H[U]` contains a clique of size at least `|U|/(s-a)`.  Since

```text
(a+1) + (s-a) = s+1,
```

we have

```text
max( |L|/(a+1), |U|/(s-a) ) >= (|L|+|U|)/(s+1) = m/(s+1).
```

The corresponding independent set or clique is regular.  QED.

The omitted case `s=1` is covered by Lemma 2 and gives regularity of all of
`H`.  Lemma 2A gives useful additional information only when the excess
`s=m-q` is small.  It does not by itself repair a dyadic partition argument
with loss comparable to `q`, because such an argument need not produce a
`q`-modular witness with small excess over `q`.

## Lemma 2B: `q+2` Modular Sets Are One Vertex From Regular

Let `q>=2`, and let `H` be a `q`-modular graph on `m<=q+2` vertices.  Then
`H` contains a regular induced subgraph on at least `m-1` vertices.

More precisely, either `H` is regular, or `m=q+2` and `H` is isomorphic to
one of

```text
K_{1,q+1},          K_{q+1} union K_1.
```

Proof.  If `m<=q+1`, Lemma 2 says that `H` is regular.  Assume then that
`m=q+2`.  The degrees of `H` lie in `[0,q+1]` and are all congruent to some
residue `r mod q`.

If `2<=r<=q-1`, the only possible degree in `[0,q+1]` with residue `r` is
`r`, so `H` is regular.  If `r=0`, the only possible degrees are `0` and `q`.
If both occur, a degree-`q` vertex has exactly one non-neighbor, while a
degree-`0` vertex is nonadjacent to every other vertex.  Hence there can be
only one degree-`0` vertex, and all other vertices have degree `q` and form a
clique.  Thus `H=K_{q+1} union K_1`.  If only one of the two degree values
occurs, `H` is regular.

The residue `r=1` is the complement of the previous case: the possible
degrees are `1` and `q+1`, and if both occur then `H` is the star
`K_{1,q+1}`.  Again, if only one degree value occurs, `H` is regular.

In each nonregular case, deleting the exceptional vertex leaves respectively
`K_{q+1}` or an independent set on `q+1` vertices.  QED.

## Lemma 3: Gallai Parity Witness

Every graph on `n` vertices contains an induced subgraph on at least
`ceil(n/2)` vertices in which all degrees are even.

Proof.  By Gallai's parity partition theorem, `V(G)` can be partitioned into
two sets `A` and `B` such that both `G[A]` and `G[B]` have all degrees even.
The larger of `A` and `B` has size at least `ceil(n/2)`.  QED.

This is a strong source of `2`-modular witnesses.  The unresolved difficulty is
to lift a large `2^i`-modular witness to a large `2^{i+1}`-modular witness
with subexponential total loss.

## Conditional Proposition: Interval Polynomial-Loss Dyadic Lifting Would Suffice

For a power of two `q`, call a vertex set `S` `q`-modular if all degrees in
`G[S]` are congruent modulo `q`.

Assume there are absolute constants `A,C` such that for every graph `G`, every
power of two `q >= 2`, every `q`-modular induced subgraph on `M` vertices,
and every integer `r` satisfying

```text
1 <= r <= floor(M / (A q^C)),
```

there is a `2q`-modular induced subgraph on exactly `r` vertices.

Then

```text
F(n) >= exp(c sqrt(log n))
```

for some constant `c>0`; in particular `F(n)/log n -> infinity`.

Proof.  By Lemma 3, `G` has a `2`-modular induced subgraph on
at least `n/2` vertices.  Put `q_i=2^i`.  For `i<t`, repeatedly apply the
assumption with the largest allowed target size.  After reaching modulus
`q_i`, we can retain a `q_i`-modular induced subgraph of order at least

```text
M_i >= (n/2) A^{-(i-1)} 2^{-C i(i-1)/2}.
```

Choose `t=Theta(sqrt(log n))` so that

```text
M_{t-1} / (A q_{t-1}^C) >= q_t = 2^t.
```

Such a `t` exists with `t >= c sqrt(log n)` for some constant `c>0`, because
the left side in base-`2` logarithms is

```text
log n - O(t^2).
```

At the last step, apply the interval lifting assumption with target
`r=q_t`.  This gives a `q_t`-modular induced subgraph on exactly `q_t`
vertices.  By Lemma 2 it is regular.  Hence
`F(n) >= q_t >= exp(c' sqrt(log n))`, which is `omega(log n)`.  QED.

The interval-size hypothesis is essential.  A lower bound alone on the size of
a modular witness is not enough for the terminal step, because arbitrary
subsets of a `q`-modular set need not remain `q`-modular; a single exact size
per lift can also skip the range where the witness size is at most the
modulus.

The brute-force checks in `EXPERIMENTS/regular_induced.py` show that the
strongest naive lifting hopes already fail at the first dyadic step; any proof
needs trace-control, absorption, or a way to choose modular witnesses with
controlled sizes.

More concretely, `EXPERIMENTS/modular_lift.py` finds parity-modular graphs on
`10` vertices whose largest `4`-modular induced subgraph has order only `4`.
Thus even the tempting first-step statement "every parity-modular graph has a
`4`-modular induced subgraph on at least half its vertices" is false.  The
interval polynomial-loss proposition above is still viable, but a proof of
it must use a subtler loss bound than simple halving at each dyadic step.
Later sampling and local search in `EXPERIMENTS/search_modular_lift.py` found
worst seen values `5,6,6,8` for even parity graphs on `12,14,16,18` vertices,
respectively.  These computations do not disprove a constant-factor first
lift from modulus `2` to modulus `4`; they only rule out the naive factor
`1/2`.

The interval-size hypothesis is also genuinely stronger than the existence of
large modular witnesses.  `EXPERIMENTS/modular_spectrum.py` finds that the
perfect matching on `6` vertices has `3`- and `4`-modular witness spectrum
`{1,2,3,4,6}`, with a gap at `5`, despite the whole graph being regular.
Thus even exact-size modular arguments cannot rely on a general monotonicity
of witness sizes.

There is still a useful modular-partition signal.  The known bad
parity-modular masks that fail a `2`-part lift often admit partitions into a
small number of induced `4`-modular parts, and
`EXPERIMENTS/modular_partition.py --exhaustive-parity` verifies a `3`-part
partition for all even graphs on `8` vertices.

The clean first-lift question

```text
Does every graph whose degrees are all congruent modulo 2 admit a partition
of its vertex set into three parts, each inducing a graph whose degrees are
all congruent modulo 4?
```

is false.  The script found even graphs on `14` and `16` vertices with no such
`3`-part partition.  Both examples do admit `4`-part partitions, and random
checks on even graphs up to `18` vertices have not found a `4`-part
counterexample.  Thus the plausible first-lift partition target, if any, is a
`4`-part theorem, not a `3`-part theorem.  The script also finds
counterexamples to the stronger demand that all parts have internal degrees
congruent to `0` modulo `4` with only four parts.  For example, the even
`n=8` mask `86423135` has a `3`-part unrestricted `4`-modular partition, but
requires `5` parts if every part must have residue `0` modulo `4`.  Thus
allowing different residues for different parts appears essential.

## Lemma 4A: Clique Obstruction To Zero-Residue Lifting

For every positive integer `q`, the clique `K_q` is `q`-modular but every
partition of `V(K_q)` into induced subgraphs whose degrees are all congruent
to `0` modulo `2q` has at least `q` parts.

Proof.  The clique `K_q` is `q`-modular because every vertex has degree
`q-1`.  A part of size `s` induces a clique `K_s`, so every degree inside the
part is `s-1`.  Since `1<=s<=q`, the congruence

```text
s-1 congruent 0 mod 2q
```

forces `s=1`.  Hence every part is a singleton and at least `q` parts are
needed.  QED.

Thus any zero-residue `q -> 2q` partition theorem has loss at least `q`,
which has exponent `1` in `q`.  It cannot feed the sublinear-exponent
partition proposition below.  The dyadic route must allow the lifted residue
to depend on the part.

## Lemma 4A.1: Complete Multipartite Graphs Have A Two-Part Dyadic Lift

Let `q` be a positive integer.  If `G` is a complete multipartite graph whose
degrees are all congruent modulo `q`, then `V(G)` can be partitioned into at
most two induced subgraphs whose degrees are all congruent modulo `2q`.

Proof.  Let the multipartite class sizes be `s_1,...,s_t`, and let
`N=sum_i s_i`.  A vertex in class `i` has degree `N-s_i`.  Since all these
degrees are congruent modulo `q`, all class sizes `s_i` are congruent modulo
`q`.  Hence the class sizes have at most two residues modulo `2q`.

Group whole multipartite classes according to their size residue modulo
`2q`.  Consider one group, and suppose all class sizes in it are congruent to
`r mod 2q`.  If the total size of the group is `M`, then a vertex in any
class of this group has internal degree

```text
M - s_i congruent M-r mod 2q,
```

independent of `i`.  Thus each nonempty group is `2q`-modular, and there are
at most two groups.  QED.

By complementation, the same statement holds for disjoint unions of cliques.
Thus neither complete multipartite graphs nor their complements can force a
large number of parts in a residue-flexible dyadic lift.

In particular, complete multipartite graphs satisfy the coarse dyadic lift
from the later conditional proposition with the best possible constant
retention at the first step.  If `G` has `M` vertices, the larger of the two
parts above has order at least `M/2`; since `q>=2` in the dyadic program, this
is at least `M/q`.  Thus the coarse lift holds for this class with `D=1`.

The factor `1/2` is sharp already for `q=2`.  Let

```text
C = K_4 union K_{1,3}.
```

Every vertex of `C` has odd degree, so `C` is `2`-modular.  Any
`4`-modular induced subgraph of `C` has at most `4` vertices.  Indeed, write a
chosen induced subgraph by coordinates `(a,b,c)`, where `a` is the number of
chosen vertices from `K_4`, `b in {0,1}` records whether the star center is
chosen, and `c` is the number of chosen leaves.  The displayed internal degree
values are

```text
a-1  if a>0,
c    if b=1,
b    if c>0.
```

For `4`-modularity, all displayed values must be congruent modulo `4`.  A
case check over `0<=a<=4`, `b in {0,1}`, and `0<=c<=3` shows that the maximum
of `a+b+c` under these congruences is `4`: examples attaining it are
`(4,0,0)`, `(1,0,3)`, and `(2,1,1)`.  Taking disjoint unions of this graph
shows that a `2 -> 4` coarse lift cannot generally retain more than half of
the vertices.

For the next dyadic step, exact enumeration shows that every `4`-modular graph
on `6` or `7` vertices admits a partition into four induced `8`-modular
parts.  This is tiny evidence, but it is consistent with the uniform
constant-part theorem that would settle the problem by the preceding
conditional proposition.

The first-lift theorem alone would not prove the target, but a uniform
partition theorem for all dyadic moduli would be powerful.  The next
proposition records the exact quantitative form needed by the largest-part
strategy.

## Conditional Proposition: Sublinear-Exponent Dyadic Partitioning Would Suffice

For powers of two `q>=2`, suppose every `q`-modular induced subgraph can be
partitioned into at most `b(q)` induced subgraphs, each of which is
`2q`-modular.  If there is a fixed `alpha<1` such that, for all sufficiently
large powers of two `q`,

```text
b(q) <= q^alpha,
```

then `F(n)/log n -> infinity`.

Proof.  Start with the `2`-modular set of order at least `n/2` from Lemma 3.
At modulus `q_i=2^i`, apply the assumed partition theorem and keep a largest
part.  This produces nested `q_i`-modular sets of sizes `m_i` satisfying

```text
m_1 >= n/2,
m_{i+1} >= m_i / b(q_i).
```

Stop at the first index `t` for which `m_t <= q_t`.  Then Lemma 2 makes the
current set regular.  Since `m_{t-1}>q_{t-1}`, the last retained part has

```text
m_t >= q_{t-1}/b(q_{t-1})
    >= c q_t^{1-alpha}.
```

Here `c>0` absorbs the harmless factor of `2` and finitely many small moduli.
It remains to see that `q_t` tends to infinity faster than any power of
`log n` along this stopping time.  If `q_t <= (log n)^A` for a fixed `A`, then

```text
product_{i<t} b(q_i) <= exp(O(t^2)) = n^{o(1)},
```

while `t=O(log log n)`, so

```text
m_t >= (n/2) / n^{o(1)} > q_t
```

for all sufficiently large `n`, contradicting the definition of `t`.  Hence
`q_t` grows faster than every fixed power of `log n`.  Choosing a fixed
`A>1/(1-alpha)`, this gives `q_t^{1-alpha}/log n -> infinity`, and therefore

```text
m_t >= c q_t^{1-alpha} = omega(log n).
```

The stopped set is regular, so `F(n)/log n -> infinity`.  QED.

Thus a constant-part theorem at every dyadic step would be much stronger than
needed, and any `q^alpha`-part theorem with fixed `alpha<1` would already
settle the problem.  A partition bound of order `q^C` with fixed `C>=1` does
not give this conclusion by the same argument.

## Conditional Proposition: A Polylogarithmic Saving From `q` Would Suffice

For powers of two `q>=2`, suppose every `q`-modular induced subgraph can be
partitioned into at most `b(q)` induced `2q`-modular subgraphs.  If there are
constants `C>2` and `q_0` such that, for all powers of two `q>=q_0`,

```text
b(q) <= q / (log_2 q)^C,
```

then `F(n)/log n -> infinity`.

Proof.  Start with the `2`-modular set of order at least `n/2` from Lemma 3.
Write `q_i=2^i`, and at the `q_i -> q_{i+1}` step keep a largest part.
Finitely many small moduli only change constants, so ignore them in the
asymptotic estimates.  Stop at the first `t` for which the retained
`q_t`-modular set has size `m_t<=q_t`; then it is regular by Lemma 2.

For large `t`,

```text
prod_{i<t} b(q_i)
  <= O(1) prod_{i<t} 2^i / i^C
  = O(1) 2^{t(t-1)/2} / ((t-1)!)^C.
```

Since stopping gives

```text
n / prod_{i<t} b(q_i) <= O(2^t),
```

we have

```text
log_2 n <= t(t-1)/2 + O(t) - C log_2((t-1)!).
```

In particular `t >= (1-o(1)) sqrt(2 log_2 n)`.

The previous retained set had `m_{t-1}>q_{t-1}`.  Therefore the last retained
part satisfies

```text
m_t >= m_{t-1}/b(q_{t-1})
    > q_{t-1} / (q_{t-1}/(t-1)^C)
    = (t-1)^C,
```

again up to harmless constant losses from small moduli.  Hence

```text
m_t >= (log n)^{C/2-o(1)}.
```

Since `C>2`, this is `omega(log n)`.  QED.

Thus the dyadic partition target need not reach `q^alpha` parts for a fixed
`alpha<1`; even a sufficiently strong polylogarithmic saving over the naive
`q`-part scale would settle the problem.

## Conditional Proposition: Coarse Lifts Plus One Terminal-Window Lift Suffice

For powers of two `q>=2`, suppose there is a constant `D` and a function
`s(q)` with

```text
s(q) = o(q / (log_2 q)^2)
```

such that the following two statements hold.

1. Coarse dyadic lift: every `q`-modular induced graph on `M` vertices
   contains a `2q`-modular induced subgraph on at least `M/(Dq)` vertices.
2. Terminal-window lift: every `q`-modular induced graph on at least `q^2`
   vertices contains a `2q`-modular induced subgraph `S` with

```text
2q <= |S| <= 2q+s(q).
```

Then `F(n)/log n -> infinity`.

Proof.  Let `G` be an `n`-vertex graph, put `L=log_2 n`, and set
`t=floor(sqrt L)`.  By Lemma 3, `G` has a `2`-modular induced subgraph
`H_1` of order `m_1>=n/2`.  Write `q_i=2^i`.  Applying the coarse dyadic lift
for `i=1,...,t-1` and retaining the guaranteed subgraph gives a
`q_t`-modular induced subgraph `H_t` of order `m_t` satisfying

```text
m_t >= n / (2 D^{t-1} q_1 q_2 ... q_{t-1})
    = n / (2 D^{t-1} 2^{t(t-1)/2}).
```

Since `t=floor(sqrt L)`, the base-`2` logarithm of the right hand side is

```text
L - t(t-1)/2 - O(t) = (1/2+o(1))L,
```

whereas

```text
log_2(q_t^2)=2t=O(sqrt L).
```

Thus, for all sufficiently large `n`, `m_t>=q_t^2`.  The terminal-window lift
applied to `H_t` gives a `2q_t`-modular induced subgraph `S` with

```text
2q_t <= |S| <= 2q_t+s(q_t).
```

Put `Q=2q_t` and write `|S|=Q+r`, where `0<=r<=s(q_t)`.  If `r<=1`, Lemma 2
makes `S` regular.  If `r>=2`, Lemma 2A, applied with modulus `Q`, gives a
regular induced subgraph of `S` on at least `(Q+r)/(r+1)` vertices.  In all
cases `G` contains a regular induced subgraph of order at least

```text
Q / (s(q_t)+1).
```

Because `s(q)=o(q/(log_2 q)^2)`, this lower bound is

```text
omega((log_2 q_t)^2).
```

Finally `(log_2 q_t)^2=t^2=(1+o(1))log_2 n`, so the regular induced subgraph
has order `omega(log n)`.  This proves `F(n)/log n -> infinity`.  QED.

This route is weaker than the `q+2` one-shot target in two ways.  The early
dyadic steps need only produce one large `2q`-modular witness with the naive
`O(q)` loss, and the size-controlled demand appears only once, inside an
already `q`-modular host of size at least `q^2`.  The price is that the final
window must have excess `o(q/(log q)^2)`, not merely a constant-factor
overshoot.

There is an even weaker terminal demand if the final step searches directly
for regular subgraphs instead of first lifting from `q` to `2q`.

## Conditional Proposition: Coarse Lifts Plus A `q`-Modular Host Theorem Suffice

For powers of two `q>=2`, suppose there is a constant `D` such that every
`q`-modular induced graph on `M` vertices contains a `2q`-modular induced
subgraph on at least `M/(Dq)` vertices.  Suppose also that there is a function
`phi(q)` with

```text
phi(q) = omega((log_2 q)^2)
```

such that every `q`-modular graph on at least `q^2` vertices contains a
regular induced subgraph on at least `phi(q)` vertices.  Then
`F(n)/log n -> infinity`.

Proof.  Repeat the coarse-lift part of the previous conditional proposition.
For `L=log_2 n`, set `t=floor(sqrt L)` and `q_i=2^i`.  Starting from Gallai's
`2`-modular induced subgraph of order at least `n/2`, the coarse lift gives a
`q_t`-modular induced subgraph `H_t` of order

```text
|H_t| >= n / (2 D^{t-1} 2^{t(t-1)/2}).
```

As before, this is larger than `q_t^2` for all sufficiently large `n`.
Applying the `q`-modular host theorem to `H_t` yields a regular induced
subgraph of order at least

```text
phi(q_t) = omega((log_2 q_t)^2)
         = omega(t^2)
         = omega(log n).
```

This proves the desired conclusion.  QED.

This formulation identifies a weaker final target than the terminal-window
lift.  Since a regular `q`-modular host is already solved by taking the whole
host, the hard case is a nonregular `q`-modular graph whose degree levels are
all congruent modulo `q`.  On `q^2` vertices there are only about `q` possible
degree levels, so at least one level has size about `q`; the challenge is to
combine many such repeated-degree levels well enough to beat the ordinary
`Theta(log q)` Ramsey extraction from a single level.

The degree-level structure has an exact trace form.  Let `H` be `q`-modular,
write

```text
deg_H(v)=a+q lambda(v)
```

with integer degree level `lambda(v)`, and for `S subset V(H)` put
`P=V(H)\S` and `tau_P(v)=deg_P(v)`.

**Lemma: Degree-Level Trace Characterization.**  For `S subset V(H)`:

1. `H[S]` is regular if and only if `tau_P(v)-q lambda(v)` is constant on
   `S`.
2. `H[S]` is `q`-modular if and only if `tau_P(v)` is constant modulo `q` on
   `S`.
3. `H[S]` is `2q`-modular if and only if
   `tau_P(v)-q lambda(v)` is constant modulo `2q` on `S`.

Proof.  For every `v in S`,

```text
deg_{H[S]}(v)=deg_H(v)-deg_P(v)=a+q lambda(v)-tau_P(v).
```

Equality of these degrees, congruence modulo `q`, and congruence modulo `2q`
are exactly the three displayed conditions.  QED.

Thus a multi-level regular induced subgraph is precisely a trace-balanced face:
if two vertices lie in levels differing by `j`, their outside traces must
differ by `jq` for regularity, or by `jq` modulo `2q` for a `2q`-modular
witness.  In particular, if `|P|<q`, then a regular `H[S]` cannot meet two
distinct original degree levels, and a `2q`-modular `H[S]` cannot meet both
parities of degree levels.

Repeated degree levels alone are not enough, because a single level may induce
an arbitrary graph.

**Lemma: Leaf Completion Obstruction For Degree-Level Pigeonholes.**  Let
`X` be any graph on vertices `x_1,...,x_s`, let `q>=1`, and choose integers
`ell_i` such that

```text
1+q ell_i >= deg_X(x_i)
```

for every `i`.  There is a graph `H` containing `X` as an induced subgraph on
`{x_1,...,x_s}` such that every vertex of `H` has degree congruent to `1`
modulo `q`, and

```text
deg_H(x_i)=1+q ell_i.
```

Proof.  For each `i`, add

```text
1+q ell_i-deg_X(x_i)
```

new leaves adjacent only to `x_i`.  Then the degree of `x_i` in the resulting
graph is `1+q ell_i`, while every new leaf has degree `1`.  All degrees are
congruent to `1` modulo `q`, and the original vertices still induce `X`.
QED.

Consequently, even a degree level of size `q` can have completely arbitrary
internal structure.  Any proof of the `q`-modular host theorem must use global
trace balance against the rest of the host, not only pigeonhole a large degree
level or apply Ramsey theory inside one level.

There is also a basic density reduction for the `q`-modular host theorem.

**Lemma: Sparse Or Co-Sparse Hosts Are Easy.**  Let `H` be any graph on
`m>=q^2` vertices.  If the average degree of `H` is at most
`q^2/L`, then `H` contains an independent set, hence a regular induced
subgraph, on at least `L` vertices.  The same conclusion holds if the average
degree of the complement of `H` is at most `q^2/L`, with a clique in place of
an independent set.

Proof.  By the Caro--Wei bound,

```text
alpha(H) >= sum_{v in V(H)} 1/(deg(v)+1)
          >= m/(average_degree(H)+1).
```

If `average_degree(H)<=q^2/L` and `m>=q^2`, this is at least `L` up to a
harmless additive constant, which can be absorbed by replacing `L` with
`L/2` in asymptotic applications.  Applying the same argument to the
complement gives the clique statement.  QED.

Thus, for the terminal target with `L=(log q)^2`, the hard `q`-modular hosts
have both edge density and co-density at least `Omega(1/(log q)^2)`.  The
modular degree-level structure must be used only after this ordinary
sparse/co-sparse Ramsey obstruction has been removed.

The coarse-lift hypothesis in the preceding conditional follows from a
flexible `O(q)` partition theorem.

**Lemma: Flexible `O(q)` Partitions Give Coarse Lifts.**  Suppose there is a
constant `D` such that every `q`-modular graph can be partitioned into at most
`Dq` induced `2q`-modular subgraphs.  Then every `q`-modular graph on `M`
vertices contains a `2q`-modular induced subgraph on at least `M/(Dq)`
vertices.

Proof.  In such a partition, one part has size at least the average
`M/(Dq)`.  QED.

This target is weaker than the fixed-slot and self-labelled formulations
refuted later in this file, because the number of parts may be linear in `q`
and each part may choose its own target residue.  Small experiments support
the flexible version: sampled even graphs on `8` and `10` vertices partitioned
into four `4`-modular parts, and sampled `4`-modular graphs on `12` vertices
partitioned into eight `8`-modular parts, with no counterexample seen in the
bounded searches.

The linear bound is more than is needed for the conditional host route.  The
same proof works if the coarse lift loses a fixed polylogarithmic factor at
each dyadic step: for any fixed `C`, replacing the loss `Dq_i` by
`q_i(log_2 q_i)^C` changes the retained size after `t=floor(sqrt(log_2 n))`
steps by the extra factor

```text
prod_{i<t} i^C = exp(O(t log t)) = 2^{o(t^2)} = n^{o(1)}.
```

Thus the final retained `q_t`-modular host still has size
`2^{(1/2-o(1))log_2 n}`, far larger than `q_t^2`.  Therefore a partition
theorem with at most `q(log q)^C` flexible `2q`-modular parts, combined with
the `q`-modular host theorem above, would also prove Problem 82.

The terminal-window lift has a rigid endpoint shape.

**Lemma: Shape Of Near-Terminal Dyadic Witnesses.**  Let `|S|=2q+r` with
`0<=r<q`.  If `G[S]` is `2q`-modular, then either `G[S]` is regular, or there
is an integer `d` with `0<=d<=r-1` such that every vertex of `S` has degree
either

```text
d       or       d+2q.
```

Proof.  All degrees in `G[S]` lie in `[0,2q+r-1]`.  In this interval, two
integers congruent modulo `2q` are either equal or differ by exactly `2q`.
Thus if more than one degree value occurs, the values are `d` and `d+2q` for
some `d`.  The larger value can occur only if
`d+2q<=2q+r-1`, so `d<=r-1`.  QED.

Thus a nonregular terminal-window witness with
`r=o(q/(log q)^2)` is almost split: its low-degree vertices have degree
`o(q/(log q)^2)`, while its high-degree vertices have complement-degree
`r-1-d=o(q/(log q)^2)` inside `S`.

Such a terminal-window witness already contains the regular subgraph size
needed in the weaker host theorem.  If `L` and `U` are the degree-`d` and
degree-`d+2q` classes in `G[S]`, then one of them has size at least `q`.  If
`|L|>=q`, the graph `G[L]` has maximum degree at most `d<=r-1`, so it contains
an independent set of size at least `|L|/(r+1)>=q/(r+1)`.  If `|U|>=q`, then
the complement of `G[U]` has maximum degree at most `r-1-d`, so `G[U]`
contains a clique of size at least `|U|/(r-d)>=q/(r+1)`.  Thus when
`r=o(q/(log q)^2)`, either case gives a regular induced subgraph of order
`omega((log q)^2)`.  This is the same numerical extraction as Lemma 2A, but
viewed through the low/high degree split.

The same terminal-window demand is already strong on regular graphs.  Every
regular graph is `q`-modular for every `q`, so the lift would imply that every
regular graph on at least `q^2` vertices contains an induced subgraph of order
`2q+o(q/(log q)^2)` of the rigid low/high form above, and in particular the
exact `r=0` version asks for a regular induced subgraph on exactly `2q`
vertices.

The exact `r=0` regular-host statement is false at small `q`: for `q=3`, the
2-regular graph `C_4 union C_5` has `q^2=9` vertices and no regular induced
subgraph on exactly `2q=6` vertices.  A regular induced subgraph of a
2-regular graph is `0`-, `1`-, or `2`-regular; in `C_4 union C_5`, the largest
independent set has size `4`, the largest induced matching has `4` vertices,
and a 2-regular induced subgraph is a union of whole cycle components, with
sizes only `4`, `5`, or `9`.  This obstruction does not scale in sparse
regular graphs by the sparse-host lemma below.

There is also a clean weighted hard core obtained from twin blowups.

**Lemma: Regular Twin Blowup Reduction.**  Let `B` be a `D`-regular graph on
vertex set `{1,...,r}`.  Replace every vertex `i` by an independent cluster
`C_i` of size `L`, and join `C_i` completely to `C_j` exactly when
`ij in E(B)`.  The resulting graph `G` is `DL`-regular.  For an induced
subset `S`, put

```text
x_i=|S cap C_i|.
```

Then every selected vertex in cluster `i` has degree

```text
(A_B x)_i = sum_{j~_B i} x_j
```

inside `G[S]`.  Consequently `S` is `2q`-modular if and only if the values
`(A_B x)_i` are congruent modulo `2q` over all active indices `i` with
`x_i>0`.

Proof.  The blowup is regular because every vertex in `C_i` is adjacent to
all `L` vertices in each of the `D` neighboring clusters of `i`.  Inside a
selected set `S`, a selected vertex from `C_i` sees exactly `x_j` selected
vertices in each neighboring cluster `C_j` and none inside its own
independent cluster.  This gives the displayed degree formula, and reducing
it modulo `2q` gives the criterion.  QED.

In particular, an exact terminal witness of size `2q` in such a blowup is
equivalent to an integer vector satisfying

```text
0<=x_i<=L,       sum_i x_i=2q,
(A_B x)_i is constant on supp(x).
```

This removes much of the general graph noise while preserving the terminal
dyadic difficulty.  For example, taking a regular base with about
`q(log q)^3` vertices and cluster size about `q/(log q)^3` gives a regular
`q^2`-vertex host in which any terminal witness must use many base vertices;
ordinary clique or independent-set witnesses in the base do not explain such
a weighted equitable vector.

Finally, a purely deletion-based absorption proof has a strong trace
restriction.

**Lemma: Deletion Absorption Criterion.**  Let `W` be a `2q`-modular vertex
set and let `P subset W`.  Then `W\P` is `2q`-modular if and only if

```text
deg_P(v) mod 2q
```

is constant over all `v in W\P`.  In particular, if `|P|<2q`, this condition
is literal equality of the integers `deg_P(v)`.

Proof.  For `v in W\P`,

```text
deg_{G[W\P]}(v)=deg_{G[W]}(v)-deg_P(v).
```

The degrees `deg_{G[W]}(v)` are already congruent modulo `2q`, so the
remaining degrees are congruent modulo `2q` exactly when the deleted traces
`deg_P(v)` are congruent modulo `2q`.  If `|P|<2q`, then
`0<=deg_P(v)<2q`, so congruence is equality.  QED.

Thus absorption by deleting small neutral blocks would require many subsets
with constant outside trace, which generic regular or twin-free graphs need
not provide.  A terminal-window proof likely needs swaps, weighted
corrections, or a nonlocal linearization of the dyadic degree bit rather than
simple deletion absorption.

There are elementary positive regimes for the regular-host hard core.

**Lemma: Sparse Regular Hosts Give Linear Regular Subgraphs.**  If `G` is
`d`-regular on `q^2` vertices and `d<=Cq`, then `G` contains an induced
`1`-regular subgraph on at least `q/(2C)` vertices, up to harmless rounding.
The complement gives the same conclusion when the complement degree is at
most `Cq`.

Proof.  If `d=0`, any `2q` vertices form an independent set.  Otherwise,
greedily build an induced matching.  When an edge `uv` is chosen, delete every
edge with an endpoint in `N[u] union N[v]`; at most `2d^2` edges are deleted.
Since `G` has `q^2 d/2` edges, the greedy process chooses at least

```text
(q^2 d/2)/(2d^2) = q^2/(4d) >= q/(4C)
```

edges.  Their endpoints induce a `1`-regular subgraph on at least `q/(2C)`
vertices.  Applying the same argument to the complement handles co-sparse
regular hosts.  QED.

In particular, very sparse or very dense regular graphs are not obstructions
to an `Omega(q)` terminal regular-host theorem.  Dense random-like regular
graphs also look poor as obstructions heuristically: a fixed `2q`-set in a
dense random regular graph is regular with probability roughly
`(2q)^{-q+O(q)}`, while there are `binom(q^2,2q)=q^{2q+O(q)}` such sets.
This leaves regular twin blowups and other highly structured medium-density
regular graphs as the most plausible terminal exact-size obstruction class.

## Conditional Proposition: Terminal-Size Modular Partitions Would Suffice

Suppose that every graph on `n` vertices admits, for
`q=ceil(sqrt(n))`, a partition of its vertex set into at most `q` induced
subgraphs, each of which is `q`-modular and has order at most `q+1`.  Then

```text
F(n) >= floor(sqrt(n)).
```

Proof.  Let

```text
V(G)=P_1 union ... union P_t,    t<=q,
```

be such a partition.  By Lemma 2, each nonempty `G[P_i]` is regular, since
`|P_i|<=q+1` and `P_i` is `q`-modular.  One part has size at least

```text
n/t >= n/q >= floor(sqrt(n)).
```

That part is a regular induced subgraph of the required order.  QED.

This is a one-shot alternative to dyadic lifting.  It is much stronger than
an unrestricted theorem saying that `q` modular parts suffice: without the
terminal size bound, the partition may place almost all vertices in one large
`q`-modular part, which is not necessarily regular.  Exact equal-size
versions are false even for small parameters.  The weaker cap `|P_i|<=q+1`
also fails in general, as the next example shows, but the conditional
proposition remains useful as a calibration of what a one-shot route would
need.

## Proposition: The Strict Terminal-Size Target Is False

For every integer `q>=5`, let `G` be the complete multipartite graph
`K_{q^2-q+2,2,1}` with multipartite classes `A,B,C` of sizes

```text
|A|=q^2-q+2,      |B|=2,      |C|=1.
```

Then `n=|V(G)|=q^2-q+5` satisfies `ceil(sqrt n)=q`, but `G` has no partition
into at most `q` induced `q`-modular subgraphs of order at most `q+1`.

Proof.  In a complete multipartite graph, a selected set with class counts
`(x,y,z)` induces a `q`-modular graph if either at most one of `x,y,z` is
positive, or all positive counts are congruent modulo `q`.  Indeed, a vertex
from a positive class with selected count `x_i` has induced degree
`m-x_i`, where `m=x+y+z`; equality of these degrees modulo `q` is equivalent
to equality of the positive selected class counts modulo `q`.

Also, since

```text
(q-1)^2 < q^2-q+5 <= q^2
```

for `q>=5`, we have `ceil(sqrt n)=q`.

Assume that a capped partition exists.  Consider the part containing the
single vertex of `C`.
Since this part has `z=1`, every other positive selected count in the same
part must be congruent to `1` modulo `q`; the cap `x+y+z<=q+1` rules out a
count `q+1` together with the `C` vertex.  Therefore the `C`-part is one of

```text
(0,0,1), (1,0,1), (0,1,1), (1,1,1).
```

It remains to cover the leftover vertices of `A` and `B` with at most `q-1`
parts.  With no `C` vertex left, a capped valid mixed part using both `A` and
`B` has counts either `(1,1,0)` or `(2,2,0)`; otherwise it is contained in one
class, and an `A`-only part covers at most `q+1` vertices of `A`.

If the `C`-part is `(0,0,1)`, the remainder is
`(q^2-q+2,2,0)`.  The two vertices
of `B` can contribute at most two vertices of `A` through one mixed part
`(2,2,0)`; the other `q-2` parts cover at most `(q-2)(q+1)` vertices of
`A`.  Thus at most

```text
2 + (q-2)(q+1) = q^2-q < q^2-q+2
```

vertices of `A` can be covered.

If the `C`-part is `(0,1,1)`, the remainder is
`(q^2-q+2,1,0)`.  The remaining vertex of `B` can contribute at most one
vertex of `A` through a mixed part, and the other `q-2` parts cover at most
`(q-2)(q+1)` vertices of `A`; this covers at most

```text
1 + (q-2)(q+1) = q^2-q-1 < q^2-q+2
```

vertices of `A`.

If the `C`-part is `(1,0,1)`, the remainder is
`(q^2-q+1,2,0)`.  The same bound as in the first case covers at most
`q^2-q < q^2-q+1` vertices of `A`.

Finally, if the `C`-part is `(1,1,1)`, the remainder is
`(q^2-q+1,1,0)`.  The same bound as in the second case covers at most
`q^2-q-1 < q^2-q+1` vertices of `A`.

All possibilities for the part containing `C` are impossible, so no such
partition exists.  QED.

The exact integer model in `EXPERIMENTS/multipartite_modular.py` independently
checks the first case `q=5`, namely `K_{22,2,1}`, with

```text
python3 EXPERIMENTS/multipartite_modular.py --target-modulus 5 --cap 5 --max-bin-size 6 --sizes 1,2,22
```

and returns `min_bins=NA`.

## Proposition: The Terminal Obstruction Has A `q+2` Repair

For every `q>=5`, the graph `K_{q^2-q+2,2,1}` from the previous proposition
can be partitioned into at most `q` induced `q`-modular subgraphs, each of
order at most `q+2`.

Proof.  Use the same multipartite classes `A,B,C`, with
`|A|=q^2-q+2`, `|B|=2`, and `|C|=1`.

First form one part using the vertex of `C` and `q+1` vertices of `A`.  Its
positive class counts are `(q+1,1)`, which are congruent modulo `q`, and its
order is `q+2`.

Second form one part using the two vertices of `B` and two further vertices of
`A`.  Its positive class counts are `(2,2)`, so it is `q`-modular and has
order `4`.

There remain

```text
(q^2-q+2) - (q+1) - 2 = q^2-2q-1
```

vertices of `A`.  Partition these remaining vertices into `A`-only chunks of
size at most `q+2`.  Every such chunk is independent and hence `q`-modular.
The number of these chunks is at most `q-2`, because

```text
q^2-2q-1 <= (q-2)(q+2).
```

Thus the total number of parts is at most `2+(q-2)=q`, and all parts have
order at most `q+2`.  QED.

## Lemma: Unit-Layer Packing

Let `B` and `C` be positive integers.  Let `r_1,...,r_t` be nonnegative
integers such that

```text
r_i <= B        for every i,
sum_i r_i <= B C.
```

Then one can assign, for each `i`, exactly `r_i` distinct bins from
`{1,...,B}` so that no bin is assigned more than `C` indices.

Proof.  Process the indices `i` in any order.  When assigning index `i`,
choose `r_i` currently least-loaded bins and increase their loads by one.
This is possible because `r_i<=B`.

We claim that no load ever exceeds `C`.  Suppose the first violation occurs
while assigning index `i`.  Then some chosen bin had load `C` before this
assignment.  Since the chosen bins were least-loaded, every bin had load at
least `C` before the assignment.  Hence the total previous load was at least
`BC`.  But the final total load is `sum_i r_i<=BC`, and the current index
still has positive demand, a contradiction.  QED.

## Proposition: Bounded Complete Multipartite Classes Satisfy The `q+2` Target

Let `q>=1`, let `B<=q`, and let `H` be a complete multipartite graph with
class sizes `r_1,...,r_t` satisfying

```text
r_i <= B        for every i,
sum_i r_i <= B(q+2).
```

Then `V(H)` can be partitioned into at most `B` induced `q`-modular subgraphs,
each of order at most `q+2`.

Proof.  Apply the unit-layer packing lemma with `C=q+2`.  For each bin, take
one vertex from every multipartite class assigned to that bin.  Since each
class `i` is assigned to exactly `r_i` distinct bins, all vertices are used
exactly once.

In any nonempty bin, the positive intersections with the multipartite classes
all have size `1`, so the induced complete multipartite graph is regular
with degree one less than the bin size.  In particular it is `q`-modular, and
the bin size is at most `q+2` by the load bound.  QED.

In particular, every complete multipartite graph on at most `q^2` vertices
whose multipartite classes all have size at most `q` satisfies the `q+2`
one-shot target, by taking `B=q`.  The remaining complete-multipartite
packing problem is to combine this unit-layer lemma with single-class chunks
from classes that are larger than the number of bins left.

## Remark: Complete Multipartite Packing As Ferrers Rectangles

For a complete multipartite graph with class-size vector `a=(a_1,...,a_t)`,
a `q`-modular bin of size at most `q+2` is, except for the special type
`(q+1,1)`, exactly a rectangle subtraction

```text
a_i -> a_i-r      for i in I,
```

where `r>=1`, `I` is nonempty, and `r|I|<=q+2`.  Thus a rectangle-only proof
of the complete-multipartite `q+2` target would show that every integer
partition of total size at most `q^2` can be decomposed into at most `q`
Ferrers rectangles, each of area at most `q+2`.

The two easiest rectangle strategies are insufficient.

First, truncating all columns at a threshold `M` and paying for the excess by
single-column chunks need not work.  For `q=4`, `q+2=6`, and

```text
(5,4,3,2,1),
```

there is no `M` for which the excess above `M` fits in `q-M` chunks while the
truncation to height `M` fits in `M` unit-layer bins.  Nevertheless the vector
has the rectangle decomposition

```text
(2,2,2,0,0),   (2,2,0,2,0),   (1,0,1,0,1).
```

Thus equal chunks of height larger than `1` are essential.

Second, induction by repeatedly removing a full-area rectangle also fails.  For
`q=5`, `q+2=7`, the vector

```text
(5,4,4,4,4)
```

has total `21=3(q+2)` but no legal rectangle of area `7`: height `7` and
width `1` is too tall, height `1` and width `7` is too wide, and no other
factorization of `7` is available.  It still decomposes into four legal
rectangles:

```text
(1,1,1,1,1),   (0,3,3,0,0),   (0,0,0,3,3),   (4,0,0,0,0).
```

Any proof of the complete-multipartite theorem therefore needs an amortized
rectangle-covering argument, not just threshold truncation or full-bin
induction.

## Conditional Proposition: Rectangle Covering Implies Complete Multipartite `q+2`

Fix `q>=3`.  Suppose every nonnegative integer vector
`a=(a_1,...,a_t)` with

```text
sum_i a_i <= q^2
```

can be written as a sum of at most `q` vectors of the form `r 1_I`, where
`r>=1`, `I subset {1,...,t}` is nonempty, and

```text
r |I| <= q+2.
```

Then every complete multipartite graph on at most `q^2` vertices admits a
partition into at most `q` induced `q`-modular subgraphs, each of order at
most `q+2`.

Proof.  Let the multipartite class sizes be `a_1,...,a_t`, and fix a rectangle
decomposition as in the hypothesis.  For each rectangle `r 1_I`, form one
vertex part by taking exactly `r` unused vertices from each multipartite class
indexed by `I`.  The decomposition uses exactly `a_i` units in coordinate `i`,
so this partitions all vertices.

Each part has order `r|I|<=q+2`.  If `|I|=1`, the part is independent.  If
`|I|>=2`, then every positive class intersection in that part has size `r`,
so the induced complete multipartite graph has all internal degrees equal to
`r(|I|-1)`.  In either case the part is regular, hence `q`-modular.  QED.

Thus the rectangle theorem would prove a strong positive class for the
one-shot `q+2` program: all complete multipartite graphs and, by complement,
all disjoint unions of cliques.  However, the rectangle theorem itself is
false.

## Refutation Of The Rectangle-Only Target

For every `q>=9`, the vector

```text
(q^2-7, 4, 2, 1)
```

has total `q^2` and is not coverable by `q` rectangles of area at most `q+2`.
Let `C=q+2`.  If all `q` rectangles are counted against the first coordinate,
their total first-coordinate capacity is at most `qC=q^2+2q`.  The first
coordinate itself uses `q^2-7`, leaving only `2q+7` unused capacity.

On the other hand, covering the tail `(4,2,1)` forces loss at least

```text
(C-4)+(C-2)+(C-1)=3C-7=3q-1.
```

Indeed, decompose the tail contribution into horizontal slices.  A slice of
height `h` that touches a tail coordinate contributes at most `h` to the first
coordinate, and therefore loses at least `C-h` from the corresponding
first-coordinate capacity.  The cheapest exact slicing of `(4,2,1)` is by
heights `4,2,1`; splitting a slice only increases the sum of losses.  Since
`3q-1>2q+7` for `q>=9`, no such rectangle cover exists.

This does not refute the complete-multipartite `q+2` target, because complete
multipartite modular bins also allow the special type `(q+1,1)`: one bin may
take `q+1` vertices from a large class and one vertex from another class.  For
example, the vector `(q^2-7,4,2,1)` is repaired by four special bins using
`q+1` vertices from the large class with one of the `4` small-class vertices,
two special bins with the class of size `2`, one special bin with the singleton
class, and then single-class bins for the remaining large class.

The finite complete-multipartite target is therefore the following arithmetic
statement, not the rectangle-only theorem.

**Multipartite bin target.**  Let `q>=3`.  Every nonnegative integer vector of
total at most `q^2` can be decomposed into at most `q` bins, each of one of the
following types:

- a rectangle `r 1_I` with `r>=1`, `I` nonempty, and `r|I|<=q+2`;
- a special two-class bin `(q+1)e_i+e_j` with `i != j`.

Such a decomposition is exactly a partition of the corresponding complete
multipartite graph into induced `q`-modular subgraphs of order at most `q+2`.

The special bins handle the sparse-tail obstruction in a clean range.

**Lemma: Special-Plus-Excess Trimming.**  Fix `q>=3` and put `C=q+2`.  Let
`a` be a nonnegative integer vector.  Suppose that after subtracting `s`
legal special bins `(q+1)e_i+e_j`, the residual vector is `b`.  Let
`B,h>=0` satisfy

```text
s+h+B <= q.
```

For each coordinate define the excess above `B` by

```text
E_i = max(b_i-B,0).
```

If

```text
sum_i ceil(E_i/C) <= h
```

and

```text
sum_i min(b_i,B) <= B C,
```

then `a` has a multipartite bin decomposition using at most `q` bins.

Proof.  Use the `s` special bins first.  For each coordinate `i`, cover its
excess `E_i` by single-coordinate rectangle bins of heights at most `C`.  This
uses exactly `ceil(E_i/C)` bins for coordinate `i`, hence at most `h` bins in
total.

After removing all excesses, the remaining vector is

```text
c_i = b_i-E_i = min(b_i,B).
```

Every coordinate of `c` is at most `B`, and the assumed total bound gives
`sum_i c_i<=BC`.  If `B=0`, this residual is empty.  If `B>0`, the unit-layer
packing lemma covers it by at most `B` unit-height rectangle bins, each of
total size at most `C`.  The total number of bins used is at most

```text
s+h+B <= q.
```

All non-special bins used above are rectangles of area at most `C=q+2`, so
all bins are legal.  QED.

The unit-layer packing proposition is the special case `s=h=0`.  The
sparse-tail repair below is the case where the chosen special bins consume
the whole tail and the remaining one-coordinate residual is trimmed by
single-class bins.

**Lemma: Sparse-Tail Multipartite Repair.**  Fix `q>=3`.  Let
`a=(x,a_2,...,a_t)` be a nonnegative integer vector with tail total

```text
A = a_2+...+a_t <= q.
```

If `x>= (q+1)A` and `x+A<=q^2`, then `a` has a multipartite bin decomposition
using at most `q` bins.

Proof.  For each of the `A` tail vertices, use one special bin containing that
tail vertex and `q+1` vertices from the first class.  This is possible because
`x>= (q+1)A`.  These `A` bins cover the whole tail and `(q+1)A` vertices from
the first class.  The remaining first-class size is

```text
x' = x-(q+1)A.
```

Cover it by single-class bins of size at most `q+2`; these are rectangle bins
of width `1`.  The number of additional bins is at most

```text
ceil(x'/(q+2)).
```

Since `x+A<=q^2`, we have

```text
x' <= q^2-(q+2)A,
```

and therefore

```text
A + ceil(x'/(q+2))
    <= A + ceil(q^2/(q+2)-A)
    = ceil(q^2/(q+2))
    = q-1
```

for `q>=3`.  Hence the vector is covered by at most `q-1`, and therefore at
most `q`, legal bins.  QED.

The lower bound `x>=(q+1)A` is unnecessary.

**Lemma: One-Large-Class Repair.**  Fix `q>=3`.  Let
`a=(x,a_2,...,a_t)` be a nonnegative integer vector with

```text
A = a_2+...+a_t <= q,
x+A <= q^2.
```

Then `a` has a multipartite bin decomposition using at most `q` bins.

Proof.  First suppose `A<q`.  Split the `A` tail vertices into `A` singleton
tail bins.  In a
singleton tail bin we may consume from the first class either:

- `0` vertices, leaving a one-class singleton bin;
- `1` vertex, giving a rectangle of type `(1,1)`;
- `q+1` vertices, giving a special bin of type `(q+1,1)`.

Thus the `A` tail bins can be made to consume any number

```text
L = s(q+1)+u
```

of first-class vertices with `s,u>=0` and `s+u<=A`.

The remaining `q-A` bins will be one-class bins from the first class, so they
can cover any remaining first-class size up to `(q-A)(q+2)`.  It is therefore
enough to choose such an `L` with

```text
max(0, x-(q-A)(q+2)) <= L <= x.
```

Put

```text
E = max(0, x-(q-A)(q+2)).
```

If `E=0`, choose `L=0`.  Suppose `E>0`, and write

```text
E = m(q+1)+r,       0 <= r <= q.
```

Since `x+A<=q^2`,

```text
E <= q^2-A-(q-A)(q+2) = A(q+1)-2q < A(q+1),
```

where the final inequality uses `A<q`.  Hence `m+1<=A` whenever we need one
more special bin.

If `r<=A-m`, choose `L=E`, using `m` special tail bins and `r` ordinary
`(1,1)` tail bins.  If `r>A-m`, choose

```text
L=(m+1)(q+1).
```

This uses `m+1<=A` special tail bins.  Its overshoot over `E` is

```text
L-E=q+1-r <= q+1-(A-m+1) = q-A+m <= q-1,
```

because `m<=A-1`.  Since `A<q`, we have

```text
q-1 <= (q-A)(q+2),
```

and therefore `L<=E+(q-A)(q+2)<=x`.  In both cases we have chosen an allowed
`L` in the desired interval.  Cover the remaining `x-L` first-class vertices
by the reserved `q-A` one-class bins.  All bins are legal, and the total
number of bins is exactly `A+(q-A)=q`, with empty one-class bins omitted if
not needed.  This proves the case `A<q`.

It remains to handle the boundary case `A=q`.  Then `x<=q^2-q=q(q-1)`.  Put
`C=q+2`.  For `0<=s<=q`, consider the interval

```text
I_s = [ s(q+1), s(q+1) + floor((q-s)/2) C ].
```

The intervals `I_s` with `0<=s<=q-2` cover every integer from `0` through
`q(q-1)`.  Indeed, for `s<=q-2`,

```text
floor((q-s)/2) C >= C >= q,
```

so the end of `I_s` is at least one less than the start of `I_{s+1}`.  Also
`I_0` starts at `0`, and

```text
end(I_{q-2}) = (q-2)(q+1)+C = q^2 >= q(q-1).
```

Choose `s` with `x in I_s`.  Use `s` special bins, each containing `q+1`
vertices from the first class and one tail vertex.  This is possible because
`x>=s(q+1)` and the tail has `q` vertices.  The remaining tail has size
`q-s`; cover it in `ceil((q-s)/2)` rectangle bins by pairing tail vertices
arbitrarily, with a singleton bin if one vertex is left over.  A pair from
one class is a one-coordinate rectangle of height `2`; a pair from two classes
is a height-`1`, width-`2` rectangle.  Both have area `2<=C`.

The remaining first-class size is `x-s(q+1)`, which is at most
`floor((q-s)/2)C` because `x in I_s`.  Cover these vertices by
`floor((q-s)/2)` one-class bins of size at most `C`.  The total number of bins
is

```text
s + ceil((q-s)/2) + floor((q-s)/2) = q.
```

Thus the boundary case is also covered.  QED.

Consequently, any counterexample to the multipartite bin target must have
largest coordinate greater than `q` and all other coordinates summing at least
`q+1`.

The remaining complete-multipartite arithmetic target would follow from a
bounded-height version of the rectangle theorem.

**Conditional Proposition: Bounded-Height Rectangles Imply The Multipartite
Bin Target.**  Fix `q>=3`.  Suppose that, for every integer `B` with
`0<=B<=q`, every nonnegative integer vector `b` satisfying

```text
sum_i b_i <= (B-2)(q+2)+4
```

and

```text
max_i b_i <= 2q+1
```

can be decomposed into at most `B` rectangle bins `r 1_I` with
`r|I|<=q+2`.  Then every nonnegative integer vector of total at most `q^2`
has a multipartite bin decomposition using at most `q` bins.

Proof.  Let `a=(a_i)` be a nonnegative vector with `sum_i a_i<=q^2`, and put
`C=q+2` and `H=2q+1`.  If `a` has only one positive coordinate, then it is
covered by single-coordinate rectangles because

```text
ceil(q^2/(q+2)) = q-1.
```

If the sum of all coordinates except a largest one is at most `q`, the
one-large-class repair applies.  We may therefore assume that the tail outside
a largest coordinate has size at least `q+1`.

For each coordinate define

```text
d_i = max(0, ceil((a_i-H)/(q+1))).
```

We will use `d_i` special bins with coordinate `i` as the large endpoint.  Let
`S=sum_i d_i`, and let `P={i:d_i>0}`.  If `m=|P|`, then for `i in P`,

```text
d_i <= (a_i-(q+1))/(q+1),
```

because `ceil(y/(q+1)) <= (y+q)/(q+1)` and `H=2q+1`.  Hence

```text
S <= (sum_{i in P} a_i)/(q+1) - m
  <= q^2/(q+1) - m
  < q.
```

Thus `S<=q-1`.

It remains only to justify that the singleton endpoints of these `S` special
bins can be chosen without using the same coordinate as the large endpoint of
that bin.  Consider the bipartite matching problem whose left side has `d_i`
requests of type `i`, and whose right side has `a_j` donor units of coordinate
`j`; a request of type `i` is adjacent to all donor units except those of
coordinate `i`.  Hall's condition is immediate for any set of requests
involving at least two types, because their combined neighborhood is the whole
right side and has size `sum_j a_j>=S`.  For requests of a single type `i`,
the available donor capacity is `sum_j a_j-a_i`.  This is at least `q+1` by
the assumption on the tail outside a largest coordinate, and `d_i<=q-1` by the
same estimate as above.  Hall's condition holds, so the donor units can be
assigned.

Subtract these `S` special bins.  The residual vector `b` has

```text
max_i b_i <= H = 2q+1
```

by the definition of `d_i`, and

```text
sum_i b_i = sum_i a_i - S(q+2)
          <= q^2 - S(q+2)
          = (q-S-2)(q+2)+4.
```

Apply the bounded-height rectangle hypothesis with `B=q-S` to cover `b` by at
most `q-S` rectangle bins.  Together with the `S` special bins, this gives at
most `q` legal multipartite bins for `a`.  QED.

The hypothesis in the preceding conditional proposition is false as stated.
The obstruction is not area, but the number of different coordinate heights
that a small number of rectangles can generate.

**Lemma: Distinct-Height Obstruction For Rectangle Covers.**  If a vector is a
sum of at most `B` rectangle vectors, then it has at most `2^B-1` distinct
positive coordinate values.

Proof.  Write the rectangles as `r_j 1_{I_j}`, `1<=j<=B`, after padding with
zero rectangles if necessary.  Each coordinate of their sum is

```text
sum_{j in J} r_j
```

for some subset `J subset {1,...,B}` depending on which rectangles contain
that coordinate.  Thus the positive coordinate values all lie among the
nonzero subset sums of `r_1,...,r_B`, of which there are at most `2^B-1`.
QED.

**Counterexample To The Bounded-Height Rectangle Hypothesis.**  Take `B=3`,
`q>=30`, `C=q+2`, and

```text
b=(8,7,6,5,4,3,2,1).
```

Then

```text
sum_i b_i=36 <= q+6 = (B-2)(q+2)+4
```

and `max_i b_i=8<=2q+1`, so `b` satisfies the bounded-height hypotheses.
However, by the distinct-height obstruction, three rectangles can produce at
most `2^3-1=7` distinct positive coordinate values, while `b` has eight.
Hence no three-rectangle cover exists, even without the area constraint.  More
generally, for any fixed `B`, the staircase

```text
(2^B,2^B-1,...,2,1)
```

requires at least `B+1` rectangles and satisfies the displayed total and height
inequalities for all sufficiently large `q`.  Therefore the conditional
proposition remains formally valid, but its hypothesis cannot be the final
multipartite arithmetic target.

The preceding counterexample points to the right repair mechanism: keep a
large coordinate as a reservoir and include it in the tail rectangles.  This
simultaneously covers the tail and reduces the number of singleton bins needed
for the reservoir.

**Lemma: Reservoir Lifting Criterion.**  Put `C=q+2`.  Let

```text
a=(x,y_1,...,y_t)
```

be a nonnegative vector, and choose `s` tail units to be the small endpoints of
special bins whose large endpoint is the first coordinate.  Let `y'` be the
residual tail after these `s` deletions.  Suppose that `y'` has a rectangle
decomposition

```text
y' = sum_{j=1}^R r_j 1_{I_j}
```

with the stronger lifted legality condition

```text
r_j(|I_j|+1) <= C
```

for every `j`.  Put `H=sum_j r_j`.  If

```text
s+R <= q,
x >= s(q+1)+H,
x-s(q+1)-H <= (q-s-R)C,
```

then `a` has a multipartite bin decomposition using at most `q` bins.

Proof.  First use the `s` special bins, each taking `q+1` vertices from the
first coordinate and one chosen tail vertex.  Then, for each tail rectangle
`r_j 1_{I_j}`, use one ordinary rectangle bin on the index set
`{0} union I_j`, where `0` denotes the first coordinate.  Its area is
`r_j(|I_j|+1)<=C`, so it is legal; over all such bins it removes exactly
`y'` from the tail and `H` vertices from the first coordinate.  The remaining
first-coordinate mass is `x-s(q+1)-H`, which is nonnegative by the second
display and fits into the remaining `q-s-R` singleton rectangle bins by the
third display.  QED.

It is useful to rewrite the last upper-reservoir condition as a slack
condition depending only on the residual tail representation.

**Lemma: Slack Form Of The Reservoir Certificate.**  Put `C=q+2` and let

```text
a=(x,y_1,...,y_t),       A=sum_i y_i,
delta=q^2-x-A >= 0.
```

Choose a residual tail vector `z` with `0<=z_i<=y_i`; put

```text
s=A-sum_i z_i.
```

Assume that the deleted tail mass can be realized by `s` special bins from the
first coordinate, and that `z` has a lifted-legal rectangle representation

```text
z_i = sum_{j: i in I_j} h_j,       h_j(|I_j|+1)<=C
```

with `R` rectangles.  Define

```text
B=sum_i z_i,       H=sum_j h_j,       Delta=R C-(B+H).
```

If

```text
s+R <= q,
x >= s(q+1)+H,
Delta <= 2q+delta,
```

then `a` has a multipartite bin decomposition using at most `q` bins.

Proof.  Apply the reservoir lifting criterion.  The only condition not
identical to one of the displayed assumptions is

```text
x-s(q+1)-H <= (q-s-R)C.
```

Since `x=q^2-A-delta=q^2-s-B-delta`, this inequality is equivalent to

```text
q^2-s-B-delta-s(q+1)-H <= (q-s-R)(q+2).
```

After cancellation, this is exactly

```text
R(q+2)-(B+H) <= 2q+delta,
```

which is the stated bound on `Delta`.  QED.

**Corollary: Binary Reservoir Certificate.**  In the slack-form lemma, suppose
`z` is represented by its active binary bits.  For each active bit `h`, let
`n_h` be the number of coordinates of `z` whose binary expansion contains
`h`.  If

```text
h(n_h+1) <= q+2
```

for every active bit, and if with

```text
R=#{active bits},       H=sum_{h active} h,       B=sum_i z_i
```

we have

```text
s+R <= q,
x >= s(q+1)+H,
B+H >= (R-2)q+2R-delta,
```

then `a` has a multipartite bin decomposition using at most `q` bins.

Proof.  The active bit `h` supplies one tail rectangle of height `h` on its
support.  The displayed support bound is exactly lifted legality after adding
the reservoir coordinate.  The final displayed inequality is the slack
condition `R(q+2)-(B+H)<=2q+delta`.  QED.

In the common three-bit case, if after deleting `s` tail units the residual
satisfies `0<=z_i<=7`, the active bits are `1,2,4`, and all three lifted bit
supports are legal, then `R=3` and `H=7`; it is enough that

```text
s+3 <= q,
x >= s(q+1)+7,
sum_i z_i >= q-1-delta.
```

The reservoir criterion also gives a small extension past the previously
proved one-large-class boundary.

**Lemma: Wide-Tail One-Large Repair.**  Let `A=sum_i y_i=q+e` with
`0<=e<=q-2`, and suppose the tail has at least `e+3` positive coordinates.  If

```text
x >= (q-3)(q+1)+1,
```

then `a=(x,y)` has a multipartite bin decomposition using at most `q` bins.

Proof.  Retain one tail unit in any `e+3` positive tail coordinates and delete
all other tail units by specials from the first coordinate.  The number of
deleted units is

```text
s=A-(e+3)=q-3.
```

The residual tail is a single rectangle of height `1` and width `e+3`; after
adding the reservoir coordinate, its lifted area is `e+4<=q+2`, so `R=1` and
`H=1`.  The bin count condition is `s+R=q-2<=q`, and the reservoir lower
condition is exactly `x>=s(q+1)+1`.  Finally, the remaining reservoir mass is
at most

```text
q^2-A-s(q+1)-1
= q^2-(q+e)-(q-3)(q+1)-1
= q-e+2,
```

which fits into the remaining two singleton bins because `q-e+2<=2(q+2)`.
QED.

These reservoir certificates have a real limitation.  They depend not only on
the number of residual heights but also on support sizes: for example, when
`4|q`, a residual tail with `q/4` coordinates all equal to `4` has one
distinct positive height, but the lifted height-`4` rectangle has area
`4(q/4+1)=q+4>q+2`.  In addition, for near-terminal vectors with
`delta=o(q)`, a rank-`R` residual certificate must satisfy

```text
B+H >= (R-2)q+O(R).
```

Thus if the residual tail mass is only `q+o(q)` and its maximum height is
`o(q)`, ranks `R>=4` cannot be certified by this method unless most of the
required mass is left in the residual tail.  A successful sparse-special proof
must therefore usually reduce to one, two, or three dense lifted rectangles,
or deliberately keep residual tail mass of order `(R-2)q`.

The reservoir criterion explains how a single special repairs the staircase
obstruction to rectangle-only covering.

**Example: Reservoir Repair Of A Staircase Tail.**  For `q>=30`, put `C=q+2`
and

```text
a=((q-3)C,8,7,6,5,4,3,2,1).
```

Then `sum_i a_i=(q-3)(q+2)+36=q^2-q+30<=q^2`.  This vector has no
`q`-rectangle cover.  Indeed, let `m` be the number of rectangles that meet
the tail.  The tail has eight distinct positive coordinate values, so by the
distinct-height obstruction `m>=4`.  If the heights of the tail-meeting
rectangles sum to `H`, then the first coordinate can receive at most
`(q-m)C+H` mass from the `q` rectangles.  Since it needs `(q-3)C`, we have

```text
H >= (m-3)C.
```

On the other hand every tail-meeting rectangle has height at most `8`, so
`H<=8m`.  For `m>=5` this contradicts `C>=32`; for `m=4`, the inequality
forces `H>=C`, while `H<=32`.  If `q>30` then `C>32`, contradiction.  If
`q=30`, equality would force all four tail-meeting heights to be `8`, which
cannot produce the tail values `1,...,7`.  Thus no `q`-rectangle cover exists.

However, one special bin repairs the vector.  Use one special bin from the
first coordinate to the tail coordinate of size `8`, leaving tail

```text
(7,7,6,5,4,3,2,1).
```

This residual tail is the sum of three binary rectangles of heights `4`, `2`,
and `1`, where in each case the index set consists of the tail coordinates
whose binary expansion contains the corresponding bit.  Each bit occurs in
five tail coordinates, so after adjoining the reservoir coordinate the lifted
areas are `4*6`, `2*6`, and `1*6`, all at most `C`.  The reservoir height used
by these three rectangles is `H=7`, and the remaining first-coordinate mass is

```text
(q-3)C-(q+1)-7 <= (q-4)C.
```

Therefore the reservoir lifting criterion gives a cover with
`1+3+(q-4)=q` bins.

## Conditional Proposition: Small-Excess Modular Partitions Would Suffice

Let `s(n)` be a function with

```text
s(n) = o(sqrt(n)/log n).
```

Suppose that every graph on `n` vertices admits, for `q=ceil(sqrt(n))`, a
partition of its vertex set into at most `q` induced `q`-modular subgraphs,
each of order at most `q+s(n)`.  Then `F(n)/log n -> infinity`.

Proof.  Let

```text
V(G)=P_1 union ... union P_t,    t<=q,
```

be such a partition, and choose a largest part `P`.  Its order `m` satisfies

```text
m >= n/q = (1-o(1)) sqrt(n).
```

If `m<=q+1`, Lemma 2 makes `G[P]` regular, so this part itself has order
`Omega(sqrt(n))`.  Otherwise write `m=q+r` with `2<=r<=s(n)`.  Lemma 2A
applied to `G[P]` gives a clique or independent set, hence a regular induced
subgraph, of order at least

```text
m/(r+1) >= (1-o(1)) sqrt(n)/(s(n)+1).
```

By the hypothesis on `s(n)`, this lower bound is `omega(log n)`.  QED.

Thus the one-shot modular route does not need terminal-sized parts exactly.
It would be enough to partition into `ceil(sqrt n)` modular parts whose sizes
exceed `q` by `o(q/log n)`.  Conversely, partitions with part sizes as large
as `2q` would not feed this argument, because Lemma 2A may then give only a
constant-size homogeneous subset inside the largest modular part.

## Conditional Proposition: `q+2` Modular Partitions Would Suffice

Suppose that every graph on `n` vertices admits, for `q=ceil(sqrt(n))`, a
partition of its vertex set into at most `q` induced `q`-modular subgraphs,
each of order at most `q+2`.  Then

```text
F(n) >= floor(sqrt(n))-1.
```

Proof.  Let `P` be a largest part.  Since there are at most `q` parts,

```text
|P| >= n/q >= floor(sqrt(n)).
```

By Lemma 2B, `G[P]` contains a regular induced subgraph on at least
`|P|-1 >= floor(sqrt(n))-1` vertices.  QED.

Thus the `q+2` capped target would be much stronger than Problem 82: it would
give polynomial growth at essentially the best possible `sqrt(n)` scale.

## Conditional Corollary: Constant Dyadic Partitions Give Polynomial Growth

For powers of two `q>=2`, suppose every `q`-modular induced subgraph can be
partitioned into at most a fixed number `B` of induced `2q`-modular subgraphs.
Then

```text
F(n) >= c_B n^{1/(1+log_2 B)}
```

for an absolute constant `c_B>0` depending only on `B`.  In particular, if
the experimentally suggested four-part dyadic theorem were true for every
power of two `q`, then

```text
F(n) >= c n^{1/3}.
```

Proof.  Start from a `2`-modular induced subgraph of order at least `n/2`.
Let `q_i=2^i` and keep a largest part at each dyadic partition step.  After
reaching modulus `q_i`, the retained set has order

```text
m_i >= (n/2) B^{-(i-1)}.
```

Stop at the first `t` for which `m_t <= q_t=2^t`.  By Lemma 2 the stopped set
is regular.  Since `m_{t-1}>q_{t-1}`, the final retained part satisfies

```text
m_t >= q_{t-1}/B = 2^{t-1}/B.
```

The stopping inequality gives

```text
(n/2) B^{-(t-1)} <= 2^t.
```

Equivalently,

```text
2^t >= c'_B n^{1/(1+log_2 B)}.
```

Combining this with the lower bound on `m_t` proves the claim after adjusting
the constant.  For `B=4`, the exponent is `1/(1+2)=1/3`.  QED.

## Lemma 3A: Complement Invariance Of Modular Partitions

Let `M` be a positive integer and let `S` be a vertex set of size `s`.  If
`G[S]` is `M`-modular with degree residue `r`, then
`complement(G)[S]` is `M`-modular with degree residue

```text
s-1-r mod M.
```

Consequently, if `G` admits a partition into at most `B` induced `M`-modular
parts, then so does its complement.

Proof.  For every `v in S`,

```text
deg_{complement(G)[S]}(v) = s-1-deg_{G[S]}(v).
```

Thus congruent degrees modulo `M` in `G[S]` become congruent degrees modulo
`M` in the complement, with the displayed residue.  Apply this to each part of
the partition.  QED.

## Lemma 3B: Chromatic Certificate For The First Dyadic Lift

Let `G` be any graph.  If `chi(G)<=4` or `chi(complement(G))<=4`, then `V(G)`
can be partitioned into at most four induced subgraphs whose degrees are
constant modulo `4`.

Proof.  If `chi(G)<=4`, take a proper four-coloring of `G`.  Each color class
is independent, hence has all internal degrees equal to `0` modulo `4`.

If `chi(complement(G))<=4`, then `V(G)` is the union of at most four cliques
in `G`.  Every clique is regular, so each clique is `4`-modular.  Equivalently
this follows from the first case and Lemma 3A.  QED.

Therefore any counterexample to the flexible first-lift assertion

```text
every even graph has a partition into at most four 4-modular induced parts
```

must satisfy

```text
chi(G) >= 5
and
chi(complement(G)) >= 5.
```

By the Nordhaus--Gaddum inequality `chi(G)+chi(complement(G)) <= |V(G)|+1`,
such a counterexample has at least `9` vertices.  The first balanced
high-chromatic case is `chi(G)=chi(complement(G))=5`, which is the `n=10`
finite search target recorded in the experiments.  This is only a pruning
lemma for the first dyadic lift; it does not prove the lift.

## Lemma 4: Local Congruence Criterion For Dyadic Partitions

Before using the local criterion, it is useful to dispose of a natural
structured obstruction class.

## Lemma 4C: Complete Multipartite Graphs Have Two-Part Dyadic Lifts

Let `q` be a positive integer and let `H` be a complete multipartite graph
with part sizes `s_1,...,s_t`.  If `H` is `q`-modular, then `V(H)` can be
partitioned into at most two induced subgraphs, each of which is
`2q`-modular.

Proof.  In a complete multipartite graph, every vertex in the `i`th
multipartite class has degree

```text
|V(H)| - s_i.
```

Thus `H` is `q`-modular if and only if all `s_i` are congruent modulo `q`.
Consequently the sizes `s_i` occupy at most two residue classes modulo `2q`.
Group whole multipartite classes according to the residue of their size
modulo `2q`.

Each group induces a complete multipartite graph whose nonempty class sizes
are all congruent modulo `2q`.  Hence its induced degrees, equal to the group
size minus the relevant class size, are all congruent modulo `2q`.  Therefore
each group is `2q`-modular.  QED.

The same argument applies to complete multipartite induced subgraphs selected
by whole original classes.  If one selects partial classes, the exact
condition for a selected set with counts `c_i` is: either at most one `c_i`
is positive, or all positive `c_i` are congruent modulo the target modulus.
`EXPERIMENTS/multipartite_modular.py` encodes this bin-packing model and
confirms on bounded exact searches that no stronger obstruction is hiding in
small complete multipartite examples.

## Example 4D: Two Dyadic Parts Do Not Suffice For Twin Blow-Ups

Let `H` be the disjoint union of `K_4` and `K_{1,3}`.  Then every vertex has
odd degree, so `H` is `2`-modular.  However, `V(H)` cannot be partitioned into
two induced `4`-modular subgraphs.

Proof.  Describe a subset by a triple `(a,b,c)`, where `a` is the number of
chosen vertices from the `K_4`, `b` is `0` or `1` according as the center of
the `K_{1,3}` is chosen, and `c` is the number of chosen leaves.  The induced
degrees appearing in the subset are

```text
a-1   if a>0,
c     if b=1,
b     if c>0.
```

The subset is `4`-modular if and only if all displayed present values are
congruent modulo `4`.  The possible nonempty triples are therefore

```text
(0,0,1), (0,0,2), (0,0,3), (0,1,0), (0,1,1),
(1,0,0), (1,0,1), (1,0,2), (1,0,3), (1,1,0),
(2,0,0), (2,1,1), (3,0,0), (4,0,0).
```

None of these has a complement, relative to `(4,1,3)`, also on the list.
Hence no two-part `4`-modular partition exists.  QED.

The script `EXPERIMENTS/twin_blowup_modular.py` searches this exact weighted
twin-class model.  Bounded labelled searches found no example requiring more
than three parts, but this example shows that the two-part residue grouping
for complete multipartite graphs is a special feature and cannot be extended
to all bounded twin quotients.

## Lemma 4E: Residue-Signature Alignment For Disjoint Unions

Fix a modulus `M`.  For an `M`-modular partition of a graph, call the sorted
multiset of part residues modulo `M` its residue signature.  Let

```text
G = G_1 disjoint union ... disjoint union G_t.
```

Suppose there is a residue multiset `R` of size at most `B` such that, for
each component `G_i`, there is an `M`-modular partition of `G_i` whose
residue signature is a submultiset of `R`.  Then `G` has an `M`-modular
partition into at most `B` parts.

Proof.  Think of the elements of `R` as `B` global slots, each labelled by a
residue modulo `M`.  For every component `G_i`, choose one of the assumed
local partitions and inject its parts into distinct global slots with matching
residues.  For each global slot, take the union of all local parts assigned to
that slot.  Since there are no edges between different components, the
internal degree of a vertex in its global part is exactly its internal degree
inside the corresponding local part.  All local parts assigned to the same
slot have the same residue, so the global slot is `M`-modular with that
residue.  Removing empty slots gives the desired partition.  QED.

This lemma turns a possible disjoint-union obstruction into a finite
signature-intersection problem.  For the first lift, the especially clean
strengthening would be: every even graph has a `4`-modular partition whose
signature is a submultiset of `{0,1,2,3}`.  The checker
`EXPERIMENTS/slot_partition.py` supports this on the current hard masks and
small random samples, while `EXPERIMENTS/disjoint_signature.py` found no
small components whose feasible signatures are incompatible with common
four-slot choices.  This remains experimental, not a proof.

## Lemma 4E.1: Flexible First Lift Equals A Universal Slot

For a residue multiset `R` of size four modulo `4`, say that an even graph
`G` is `R`-slot-partitionable if `V(G)` has a partition into at most four
induced `4`-modular subgraphs whose residue signature is a submultiset of
`R`.

The following statements are equivalent.

1. Every even graph has a partition into at most four induced `4`-modular
   subgraphs.
2. There is a single residue multiset `R` of size four modulo `4` such that
   every even graph is `R`-slot-partitionable.

Proof.  The second statement clearly implies the first.  Conversely, suppose
the first statement holds but no universal `R` exists.  There are only
`binom(4+4-1,4)=35` residue multisets of size four modulo `4`.  For each such
`R`, choose an even graph `G_R` that is not `R`-slot-partitionable.  The
disjoint union

```text
G = disjoint union_R G_R
```

is even, so by the first statement it has a four-part `4`-modular partition.
Pad the residue signature of this partition by arbitrary unused residues to a
four-element residue multiset `R_0`.  Restricting the global partition to the
component `G_{R_0}` gives an `R_0`-slot partition of `G_{R_0}`, contradicting
the choice of `G_{R_0}`.  QED.

Thus to prove the flexible first lift it is enough, and in fact necessary, to
prove one universal four-slot theorem.  The current experimental survivor
list for such a universal `R` is recorded in `NOTES.md`.

## Lemma 4E.2: Universal Slots Within A Fixed Source Residue

Fix positive integers `q`, `M`, and `B` with `q` dividing `M`.  Say that a
graph has source residue `a mod q` if every vertex degree is congruent to
`a` modulo `q`.  Say that a residue multiset `R` of size `B` modulo `M` is
universal for the lift `a mod q -> M` if every graph of source residue
`a mod q` has a partition into at most `B` induced `M`-modular subgraphs
whose residue signature is a submultiset of `R`.

For fixed `q`, `M`, `B`, and `a`, the following are equivalent.

1. Every graph of source residue `a mod q` has a partition into at most `B`
   induced `M`-modular subgraphs.
2. There is a residue multiset `R` of size `B` modulo `M` that is universal
   for `a mod q -> M`.

Proof.  The second statement implies the first.  Conversely, suppose the first
statement holds and no universal `R` exists.  There are finitely many residue
multisets of size `B` modulo `M`.  For each such `R`, choose a graph `G_R`
of source residue `a mod q` with no `R`-slot partition.  The disjoint union

```text
G = disjoint union_R G_R
```

again has source residue `a mod q`, so by the first statement it has a
`B`-part `M`-modular partition.  Pad the residue signature of this partition
to a `B`-element residue multiset `R_0`.  Restricting the global partition to
the component `G_{R_0}` gives an `R_0`-slot partition of `G_{R_0}`, a
contradiction.  QED.

Consequently a flexible `q -> M` theorem for all source residues gives a
finite family of universal slot multisets, one for each residue `a mod q`.
It does not by this argument give a single common `B`-slot multiset that
works simultaneously for all source residues; the class of all `q`-modular
graphs is not closed under disjoint unions of different source residues.

Any universal slot multiset for source residue `a mod q` must pass the clique
tests whose source residue is `a`.  Since the clique `K_m` has degree
`m-1`, it belongs to the source class `a mod q` exactly when
`m congruent a+1 mod q`.  Therefore a universal
`R={r_1,...,r_B}` modulo `M` for `a mod q -> M` must have the property that
every positive integer `m` with `m congruent a+1 mod q` can be written as

```text
m = s_1+...+s_j,  j<=B,
s_i congruent r_i+1 mod M
```

using a submultiset of `R`.  Lemma 4I.8 is the all-cliques version of this
necessary condition.  Thus fixed-slot candidates for higher dyadic lifts are
already heavily constrained by elementary coin-representation conditions, but
the constraint should be applied separately to the relevant source residues.

## Corollary 4E.3: Dyadic Source Clique Test

Let `q` be a positive integer, let `M=2q`, and fix a source residue
`a mod q`.  For a residue `r mod 2q`, write `w(r)` for the least positive
integer congruent to `r+1` modulo `2q`.  A target slot multiset `R` modulo
`2q` passes all clique tests in source class `a mod q` if and only if both

```text
a+1      and      a+1+q
```

are subset sums of the multiset `{w(r): r in R}`.

Proof.  The clique `K_m` belongs to source class `a mod q` exactly when
`m-1 congruent a mod q`, or equivalently `m congruent a+1 mod q`.  In a
target-slot partition of a clique, a part using slot `r` has positive size
congruent to `r+1` modulo `2q`, so its least possible size is `w(r)`.

The positive integers congruent to `a+1` modulo `q` split into two residue
classes modulo `2q`, represented by `a+1` and `a+1+q`.  If these two smallest
representatives are subset sums of the available weights, then every larger
integer in the same modulo-`2q` class is represented by adding a suitable
multiple of `2q` to one already-used clique part.  Conversely, if all clique
sizes in source class `a mod q` are representable, then the two displayed
smallest sizes are representable.  QED.

In particular, the two slots `{a,a+q}` already pass all clique tests for the
source residue `a mod q`.  Thus cliques alone do not obstruct a constant-part
source-residue dyadic lift.

There is also a small common slot family passing all clique tests across all
source residues: choose weights

```text
1,2,4,...,q,2q
```

and use the corresponding target residues

```text
0,1,3,...,q-1,2q-1.
```

Every residue class modulo `2q` has a representative in `[1,2q]`; binary
expansion expresses representatives below `2q` as subset sums of
`1,2,4,...,q`, and the representative `2q` uses the final weight.  This shows
that even a common slot family needs only `O(log q)` slots for cliques.
However, clique tests are far too weak: for `q=4`, the four power-of-two slots
`(0,1,3,7)` pass all clique tests except the size-`8` representative, and the
five-slot corrected family `(0,1,3,7,7)` is still not a useful structural
certificate for multipartite graphs without allowing repeated lower residues.
Already the complete bipartite graph `K_{2,2}` has no `(0,1,3,7)`-slot
partition modulo `8`.  Indeed, a part in a complete multipartite graph is
`8`-modular only when the positive intersections with its two sides have equal
size modulo `8`, or when it uses just one side; the size vector `(2,2)` cannot
be packed into the allowed residues `0,1,3,7` without a residue-`2` part or
repeated lower slots.

## Computational Proposition 4E.4: Three Parts Do Not Suffice For `4 -> 8`

There is a graph whose degrees are all congruent to `2 mod 4` and whose vertex
set cannot be partitioned into three induced `8`-modular subgraphs.

Proof.  Consider the following five `10`-vertex graph masks, in the edge order
used by `EXPERIMENTS/regular_induced.py`:

```text
10576016915819
964524775696
33317578526621
6543506392701
30609183199989
```

The exact checker verifies that every vertex in each mask has degree
`2 mod 4`.  It also verifies that these five masks kill all
`binom(8+3-1,3)=120` three-slot residue multisets modulo `8`: after the
five masks, the numbers of newly killed still-possible triples are

```text
110, 5, 3, 1, 1.
```

This is checked by:

```text
python3 82/EXPERIMENTS/slot_obstruction_certificate.py 10 \
  --source-modulus 4 --source-residue 2 \
  --target-modulus 8 --slot-count 3 \
  --masks "10576016915819,964524775696,33317578526621,6543506392701,30609183199989"
```

Let `H` be the disjoint union of these five graphs.  Since all components have
source residue `2 mod 4`, the graph `H` also has source residue `2 mod 4`.
If `H` had a partition into at most three induced `8`-modular subgraphs, pad
the residue signature to a three-element multiset `R`.  The finite
verification says that one component has no `R`-slot partition.  Restricting
the global partition of `H` to that component would give such an `R`-slot
partition, because there are no edges between components, a contradiction.
QED.

This obstruction is useful calibration: the dyadic route cannot hope for a
three-part theorem even at the second lift.  It does not contradict the
currently plausible four-part source-residue version of `4 -> 8`.

## Lemma 4F: Self-Labelled Modular Colorings

Fix a positive integer `M`.  The following two statements are equivalent for
a graph `G`.

1. `V(G)` has a partition into at most `M` induced `M`-modular subgraphs whose
   residue signature is a submultiset of `{0,1,...,M-1}`.
2. There is a labeling `c:V(G)->Z/MZ` such that, for every vertex `v`,

```text
|N(v) cap c^{-1}(c(v))| congruent c(v) mod M.
```

Proof.  Given a partition with distinct residues, label every vertex by the
residue of its part.  Then the displayed congruence is exactly the assertion
that the part containing `v` has residue `c(v)`.

Conversely, given such a labeling, the fibers `c^{-1}(r)`, after deleting
empty fibers, form an `M`-modular partition; the fiber labelled `r` has
internal degree residue `r`.  QED.

The tempting sharpened first-lift target for even graphs was the special case
`M=4` of this labeling problem.  This target is also false; see the Eulerian
cactus obstruction in Example 4I.5 below.  The unrestricted version, with no
hypothesis on `G`, is already false for every `M>=3`; see Example 4I.  Thus
self-labelled colorings are useful as a source of positive classes and
algebraic structure, but the dyadic partition route must allow repeated
residues among the parts.

## Lemma 4G: The Self-Labelled Coloring Theorem For `M=2`

Every graph `G` has a labeling `x:V(G)->F_2` such that

```text
|N(v) cap x^{-1}(x(v))| congruent x(v) mod 2
```

for every vertex `v`.

Proof.  Let `A` be the adjacency matrix of `G` over `F_2`, let `1` be the
all-one vector, and let

```text
d = A 1
```

be the degree-parity vector.  If `x_v=0`, the parity of the number of
neighbors of `v` in its own class is

```text
d_v + (A x)_v,
```

while if `x_v=1`, it is

```text
(A x)_v.
```

Thus the desired condition is exactly the linear system

```text
A x = d + (d+1) * x,
```

where multiplication by `d+1` is coordinatewise.  Equivalently,

```text
B x = d,
B = A + diag(d+1).
```

It remains to prove that this system is solvable.  Since `B` is symmetric,
`d` lies in the column space of `B` if and only if `y dot d=0` for every
`y in ker B`.  Let `y in ker B`.  First, because

```text
B 1 = A1 + (d+1) = d+d+1 = 1,
```

we have

```text
y dot 1 = y dot B1 = (By) dot 1 = 0.
```

Second,

```text
0 = y dot By = sum_v (d_v+1) y_v,
```

because the off-diagonal edge terms occur twice and vanish in characteristic
`2`.  Combining the last two displayed equations gives

```text
y dot d = sum_v d_v y_v = sum_v (d_v+1)y_v + sum_v y_v = 0.
```

Hence every vector orthogonal to the column space of `B` is orthogonal to
`d`, so `d` is in the column space and the system has a solution.  Any
solution `x` is the required self-labelled `2`-modular coloring.  QED.

This lemma is a strict strengthening of Gallai's parity partition in a
different direction: one part has even internal degrees and the other has odd
internal degrees.  It does not imply the `M=4` self-labelled theorem, because
the next binary digit of an internal degree depends quadratically on the
chosen residue classes rather than linearly.

## Example 4I: Self-Labelled Colorings Fail For `M>=3`

Let `T` be the tree with edges

```text
r x, r y, r z, x x', y y'.
```

Then for every modulus `M>=3`, `T` has no labeling `c:V(T)->Z/MZ` satisfying

```text
|N(v) cap c^{-1}(c(v))| congruent c(v) mod M
```

at every vertex.

Proof.  Since every leaf has degree `1`, a leaf label can only be `0` or `1`.
It is `1` exactly when its neighbor has the same label, and it is `0` exactly
when its neighbor has a different label.

Consider the length-two branch `r-x-x'`.  If `x'` has the same label as `x`,
then both labels are `1`; vertex `x` already has one same-labelled neighbor,
so the root `r` cannot also have label `1`.  If `x'` has a different label
from `x`, then `x'` has label `0`, and the only way for `x` to have the
correct residue is for `x` to have label `1` and for `r` also to have label
`1`.  In either case `x` has label `1`.  The same argument on the branch
`r-y-y'` shows that `y` has label `1`.

If `r` has label `1`, then it has at least the two same-labelled neighbors
`x` and `y`, so its same-labelled degree is at least `2` and is not congruent
to `1` modulo any `M>=3` because this degree is at most `3`.  If `r` has
label `0`, then the leaf `z` cannot be labelled consistently: label `0` would
make it same-labelled with its neighbor, while label `1` would require it to
be same-labelled with its neighbor.  Finally, if `r` has any label other than
`0` or `1`, then `z` must have label `0`, and `r` has no same-labelled
neighbors; this is not congruent to the label of `r`.  All cases contradict
the required condition.  QED.

In the edge ordering used by `EXPERIMENTS/regular_induced.py`, this tree is
the `n=6` mask `659`.  It has degree sequence `(3,2,2,1,1,1)`, so it does not
contradict the restricted even-graph target for the first dyadic lift.
The obstruction is also not preserved by the simplest Eulerian blow-up:
`EXPERIMENTS/twin_self_label.py` checks that replacing every vertex of this
tree by an independent twin pair gives a self-labelled mod-`4` coloring.  In
the notation of the proof, assign both twins of `r,x,y,z` residue `2` and
both twins of `x',y'` residue `0`.  Each used class then has the required
same-residue degree modulo `4`.

## Lemma 4I.1: Independent Two-Blowups Are Self-Labelled Mod-`4`

Let `G` be any graph, and let `G^{(2)}` be the graph obtained by replacing
each vertex `v` by an independent pair `{v_0,v_1}` and each edge `uv` by the
complete bipartite graph between `{u_0,u_1}` and `{v_0,v_1}`.  Then
`G^{(2)}` has a self-labelled mod-`4` coloring.

Proof.  By Lemma 4G, choose a labeling `x:V(G)->F_2` such that the number of
neighbors `u` of `v` with `x_u=x_v` is congruent to `x_v` modulo `2`.  In
`G^{(2)}`, label both twins of `v` by `2x_v`, viewed as an element of
`Z/4Z`.

For a twin `v_i`, its same-labelled neighbors are exactly the two twins of
each neighbor `u` of `v` with `x_u=x_v`.  Hence its same-labelled degree in
`G^{(2)}` is

```text
2 |{u in N_G(v): x_u=x_v}|,
```

which is congruent modulo `4` to `2x_v`, the label of `v_i`.  QED.

This lemma explains why the tree obstruction in Example 4I disappears after
the independent two-blowup.  It is still far from the first-lift target,
because a general even graph need not be a two-blowup or decompose into such
pieces in a way that preserves the same labels.

## Proposition 4I.2: A Cactus Class With Self-Labelled Mod-`4` Colorings

Let `G` be a connected cactus graph whose blocks are cycles.  Suppose no cycle
of `G` contains two adjacent articulation vertices.  Then `G` has a
self-labelled mod-`4` coloring.

Proof.  We first record two colorings of a cycle `C` with a specified set
`R` of marked vertices, assuming no two vertices of `R` are adjacent on `C`.
All marked vertices will have label `2`.

The active coloring labels every vertex of `C` by `2`.  Then each marked
vertex receives contribution `2` from this cycle, and every unmarked vertex
has two same-labelled neighbors, hence is correctly labelled.

The inactive coloring gives every marked vertex contribution `0`.  Between
two consecutive marked vertices on the cycle, the internal path has length at
least one; if there is only one marked vertex, use the single path obtained by
deleting it from the cycle.  Label the internal vertices of each such path by
a word over `{0,1}` formed from
tiles `0` and `11`, with no two `0` tiles adjacent; such a word exists in
every positive length, for instance by using repetitions of `011` and then
appending `0` or `11` according to the length modulo `3`.  In this word,
every `0` has no same-labelled neighbor, and every `1` lies in a block `11`
and has exactly one same-labelled neighbor.
The endpoints of the path are marked vertices of label `2`, so the marked
vertices receive no same-labelled neighbor from inactive segments.  Thus all
unmarked vertices on an inactive cycle are correctly labelled, and every
marked vertex receives contribution `0` from that cycle.

It remains to choose which cycle blocks are active.  Form the block-cut tree
of `G`, with one node for every cycle block and one node for every
articulation vertex.  Since every leaf of this tree is a cycle node, the
incidence matrix over `F_2` from cycle nodes to articulation nodes has full
row rank.  Indeed, remove a leaf cycle node `B` adjacent to an articulation
node `a`; after solving the components left after deleting `a`, choose the
variable of `B` to make the equation at `a` hold.  Induction proves
surjectivity.

Therefore we can choose active/inactive values `x_C in F_2` for the cycle
blocks so that, at every articulation vertex `a`,

```text
sum_{C incident with a} x_C = 1 mod 2.
```

Now color every cycle block actively when `x_C=1` and inactively when
`x_C=0`, using the same label `2` for each articulation vertex in all incident
blocks.  Every non-articulation vertex is correct by the cycle construction.
An articulation vertex `a` has label `2`; each active incident cycle
contributes two same-labelled neighbors and each inactive incident cycle
contributes none.  Since the number of active incident cycles is odd, its
same-labelled degree is congruent to `2` modulo `4`, as required.  QED.

This proposition is narrow, but it gives a nontrivial inductive class of
Eulerian graphs beyond regular graphs and independent two-blowups.  The
remaining difficulty is handling adjacent articulation vertices on a cycle
and, much more generally, overlapping cycle decompositions in arbitrary
Eulerian graphs.

## Proposition 4I.3: Cycle-Block Signature Criterion For Cacti

Let `G` be a cactus graph whose blocks are cycles.  For a cycle block `C`,
let `R(C)` be its set of articulation vertices.  A signature of `C` is a pair
of functions

```text
ell_C: R(C) -> Z/4Z,
s_C: R(C) -> {0,1,2}
```

for which the non-articulation vertices of `C` can be labelled so that every
non-articulation vertex is self-labelled mod `4`, every articulation vertex
`a in R(C)` has label `ell_C(a)`, and `s_C(a)` is the number of neighbors of
`a` inside `C` with label `ell_C(a)`.

If there is a choice of one signature for every cycle block such that

```text
ell_C(a) is independent of C incident with a
```

and, for every articulation vertex `a`,

```text
sum_{C incident with a} s_C(a) congruent ell(a) mod 4,
```

then `G` has a self-labelled mod-`4` coloring.

Proof.  Use the chosen signature on each cycle block.  The first displayed
condition makes the labels agree at articulation vertices, so these local
labellings patch to a global vertex labelling of `G`.  Every
non-articulation vertex lies in a single cycle block and is correct by the
definition of signature.  At an articulation vertex `a`, the same-labelled
degree in the whole cactus is the sum of the same-labelled contributions from
the incident cycle blocks, because distinct blocks share only the vertex
`a`.  The second displayed condition says exactly that this total is
congruent to the label of `a` modulo `4`.  QED.

The script `EXPERIMENTS/cycle_block_signature.py` enumerates these signatures
for small cycle blocks.  For example, adjacent marked vertices on a triangle
already have feasible signatures not used in Proposition 4I.2, explaining why
the nonadjacent-articulation hypothesis is not sharp.

## Lemma 4I.4: Chromatic Certificate For Modular Partitions

If `G` is `r`-colorable, then for every modulus `M`, `V(G)` can be
partitioned into at most `r` induced subgraphs whose degrees are all
congruent to `0` modulo `M`.

Proof.  Take a proper `r`-coloring.  Each color class is an independent set,
so every induced degree inside a color class is `0`.  QED.

In particular, every cactus graph is `3`-colorable, since each block is an
edge or a cycle and the colorings can be extended block by block through the
block-cut tree.  Hence every cactus graph has a `3`-part zero-residue
modular partition for every modulus.  This explains why the Eulerian cactus
that refutes the aligned self-labelled strengthening still has an ordinary
`3`-part `4`-modular partition: the ordinary residue-flexible question is
much weaker on low-chromatic graph classes.

## Example 4I.5: The Self-Labelled Even-Graph Target Is False

Let `G` be the cactus graph with cycle blocks

```text
(0,1,2,3),
(0,4,5),
(5,6,7,8),
(2,9,10,11),
(3,12,13,14).
```

Then `G` is Eulerian but has no self-labelled mod-`4` coloring.

The articulation vertices are `0,2,3,5`.  Applying the exact signature
criterion of Proposition 4I.3, the five cycle blocks have respectively

```text
64, 16, 4, 4, 4
```

possible signatures.  Exhaustive enumeration of the `64*16*4*4*4`
combinations finds no compatible choice.  This is checked by
`EXPERIMENTS/cactus_signature_dp.py` with

```text
--cycles '0,1,2,3;0,4,5;5,6,7,8;2,9,10,11;3,12,13,14'
```

The same graph has `15` vertices and degree sequence

```text
2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,
```

so it is an even graph.  In the edge ordering used by
`EXPERIMENTS/regular_induced.py`, its mask is

```text
25393864177572795278346554458141.
```

This does not refute the ordinary residue-flexible first lift: the same graph
has a `3`-part `4`-modular partition, found by
`EXPERIMENTS/modular_partition.py`, with part residues `(1,0,1)`.
It only rules out the aligned self-labelled strengthening.

There remains an intermediate alignment question: perhaps there is a fixed
multiset `R` of four residues modulo `4` such that every even graph partitions
into `4`-modular parts whose residue signature is a submultiset of `R`.
This would still be strong enough to align disjoint unions via Lemma 4E.
The scripts `EXPERIMENTS/universal_slots.py` and
`EXPERIMENTS/universal_slots_fast.cpp` test this finite question.  The full
labelled even-graph sweep on `8` vertices leaves exactly ten four-slot
multisets:

```text
(0,0,0,1), (0,0,0,2), (0,0,1,1), (0,0,1,2),
(0,0,2,2), (0,0,2,3), (0,1,1,1), (0,1,1,2),
(0,1,2,2), (0,1,2,3).
```

The aligned self-labelled slots `(0,1,2,3)` survive this `n=8` sweep but are
killed by the `15`-vertex cactus above.  Combining all current exact
counterexamples leaves eight residue multisets as plausible universal
first-lift slots:

```text
(0,0,0,1), (0,0,0,2), (0,0,1,1), (0,0,1,2),
(0,0,2,2), (0,0,2,3), (0,1,1,2), (0,1,2,2).
```

The extra elimination beyond the `n=8` sweep is a random even graph on
`14` vertices, mask `1938867942138712527476832246`, which has no
`(0,1,1,1)` slot partition.

Thus the self-labelled obstruction above does not rule out all useful
residue-slot alignment strategies.  Any such theorem would still only be a
first-lift alignment result unless it extends uniformly to higher dyadic
moduli.

The strongest-looking surviving candidate is `R=(0,0,1,2)`, because it has
two zero slots and one slot for each nonzero parity class.  The next lemma
records an equivalent form that replaces the two zero slots by a cut
congruence problem.

## Lemma 4I.6: Cut-Congruence Form For The Slots `(0,0,1,2)`

Let `G` be an even graph.  Then `G` has a `4`-modular partition with residue
signature contained in `(0,0,1,2)` if and only if there are disjoint sets
`C,D subset V(G)` such that:

1. `G[C]` is `1`-modular modulo `4`;
2. `G[D]` is `2`-modular modulo `4`;
3. writing `H=G[V(G)\(C union D)]`, there is a cut `V(H)=A union B` such
   that, for every `v in V(H)`,

```text
deg_H(v, opposite side of the cut) congruent deg_H(v) mod 4.
```

Proof.  Suppose first that `A,B,C,D` is such a partition, with `A` and `B`
the two zero-residue parts.  For `v in A`, the degree of `v` inside `A` is
`0` modulo `4`, so

```text
deg_H(v,B) = deg_H(v)-deg_H(v,A) congruent deg_H(v) mod 4.
```

The same argument applies to vertices of `B`.

Conversely, suppose `C,D` and a cut `A,B` of the residual graph `H` satisfy
the displayed congruence.  Then for `v in A`,

```text
deg_H(v,A)=deg_H(v)-deg_H(v,B) congruent 0 mod 4,
```

and similarly `deg_H(v,B) congruent 0 mod 4` for `v in B`.  Thus `A` and `B`
are zero-residue parts, while `C` and `D` have residues `1` and `2` by
assumption.  QED.

Equivalently, if the cut is encoded by signs `x_v in {+1,-1}` on `V(H)`,
then the residual condition is

```text
x_v sum_{u in N_H(v)} x_u congruent -deg_H(v) mod 8
```

for every vertex `v`.  Indeed,
`x_v sum_{u in N_H(v)} x_u = deg_H(v,same side)-deg_H(v,opposite side)`,
and this is congruent to `-deg_H(v)` modulo `8` exactly when the
opposite-side degree is congruent to `deg_H(v)` modulo `4`.

In particular, every bipartite even graph has a `(0,0,1,2)` partition: take
`C=D=empty` and use a bipartition of `G`, so both zero-residue parts are
independent.  More generally, the task for this slot multiset is to remove
one `1`-modular part and one `2`-modular part so that the residual graph has
the displayed mod-`4` cut-degree prescription.

## Lemma 4I.6A: One-Defect Sufficient Condition

Let `G` be an even graph.  Suppose there is a vertex set `D` such that

```text
deg_{G[D]}(v) congruent 2 mod 4  for every v in D,
deg_G(v,D) congruent deg_G(v) mod 4  for every v notin D.
```

Then `G` has a `4`-modular partition with residue signature contained in
`(0,0,1,2)`.

Proof.  Put `D` in the residue-`2` slot.  For every vertex
`v in V(G)\D`,

```text
deg_{G[V\D]}(v) = deg_G(v) - deg_G(v,D) congruent 0 mod 4.
```

Thus `V(G)\D` is a zero-residue part.  The remaining two slots may be empty.
QED.

This condition is only a sufficient shortcut, not a viable replacement for
Lemma 4I.6.  The script `EXPERIMENTS/defect_set.py` checks the condition, and
the recorded hard masks on `14`, `15`, and `16` vertices already have no such
set `D`, despite having `(0,0,1,2)` partitions.  Random even graphs on
`12` vertices also usually fail the shortcut.  Hence the two zero slots, or
equivalently the residual cut in Lemma 4I.6, are genuinely needed.

## Proposition 4I.7: Complete Multipartite Graphs Are Covered By `(0,0,1,2)`

Let `G` be a complete multipartite even graph with class sizes
`s_1,...,s_t`.  Then `G` has a `4`-modular partition with residue signature
contained in `(0,0,1,2)`.

Proof.  For a union of whole multipartite classes, the induced graph is again
complete multipartite.  If the classes used in this union all have the same
size residue `r` modulo `4`, and there are `m` such classes, then every
internal degree in the union is congruent to

```text
(m-1)r mod 4.
```

First assume every class size is even.  Let `I_0` be the classes with
`s_i congruent 0 mod 4` and `I_2` the classes with
`s_i congruent 2 mod 4`.  The union of the classes in `I_0`, if nonempty,
has residue `0`.  The union of the classes in `I_2` has residue

```text
2(|I_2|-1) mod 4,
```

which is either `0` or `2`.  Thus these two unions fit into the two zero
slots and the residue-`2` slot.

It remains to handle the case where all class sizes are odd.  Since `G` is
even, the number of classes is odd.  Let `a` be the number of classes with
size `1` modulo `4`, and let `b` be the number of classes with size `3`
modulo `4`; thus `a+b` is odd.

For a class of size `3` modulo `4`, fix once and for all a split into two
nonempty pieces of sizes `1` and `2` modulo `4`.  This is possible because
the class size is at least `3`: choose one vertex for the first piece and put
the rest in the second piece.

We now give a construction according to `b mod 4`.

If `b congruent 0 mod 4`, put all `3 mod 4` classes whole into the residue-`1`
slot, since their whole-class union has residue `3(b-1) congruent 1 mod 4`.
Here `a` is odd, so the whole union of all `1 mod 4` classes has residue
`a-1`, which is either `0` or `2`, and fits an available zero or residue-`2`
slot.

If `b congruent 1 mod 4`, first suppose `a congruent 2 mod 4`.  Then put all
`3 mod 4` classes whole into a zero slot and all `1 mod 4` classes whole into
the residue-`1` slot.  If instead `a congruent 0 mod 4`, choose one
`3 mod 4` class.  Put all `1 mod 4` classes together with the `1 mod 4` piece
of the chosen class into one zero slot; put the `2 mod 4` piece of the chosen
class into the other zero slot as an independent set; and put the remaining
`3 mod 4` classes, whose number is divisible by `4`, whole into the
residue-`1` slot.

If `b congruent 2 mod 4`, split every `3 mod 4` class.  If
`a congruent 1 mod 4`, put all `1 mod 4` classes whole into a zero slot, put
all `1 mod 4` pieces of the `3 mod 4` classes into the residue-`1` slot, and
put all `2 mod 4` pieces of those classes into the residue-`2` slot.  If
`a congruent 3 mod 4`, put all `1 mod 4` classes together with all
`1 mod 4` pieces of the `3 mod 4` classes into a zero slot; this uses
`a+b congruent 1 mod 4` positive pieces of residue `1`.  Put all
`2 mod 4` pieces of the `3 mod 4` classes into the residue-`2` slot.

Finally suppose `b congruent 3 mod 4`.  If `a congruent 2 mod 4`, put all
`3 mod 4` classes whole into the residue-`2` slot and all `1 mod 4` classes
whole into the residue-`1` slot.  If `a congruent 0 mod 4`, choose one
`3 mod 4` class.  Put all `1 mod 4` classes together with the `1 mod 4` piece
of the chosen class into one zero slot; put the chosen class's `2 mod 4`
piece alone into the second zero slot; and split the remaining
`3 mod 4` classes.  Their number is `2 mod 4`, so their `1 mod 4` pieces form
a residue-`1` part and their `2 mod 4` pieces form a residue-`2` part.

Each part described above is a union of pieces whose positive intersections
with multipartite classes all have the same residue modulo `4`, so the
residue computation at the start of the proof verifies the claimed part
residue.  The parts cover every vertex exactly once, proving the proposition.
QED.

## Lemma 4I.8: Clique Test For Fixed Slot Multisets

Fix a modulus `M` and a residue multiset `R`.  The clique `K_m` has an
`M`-modular partition whose residue signature is a submultiset of `R` if and
only if there is a submultiset `{r_1,...,r_j}` of `R` and positive integers
`s_1,...,s_j` such that

```text
s_i congruent r_i+1 mod M  for every i,
s_1+...+s_j = m.
```

Proof.  Every part of a partition of a clique is itself a clique.  A part of
size `s` has internal degree `s-1` at every vertex, hence has residue
`s-1 mod M`.  Therefore a partition with residues `r_1,...,r_j` is exactly a
decomposition of `m` into positive part sizes `s_i` satisfying the displayed
congruences.  QED.

This elementary test already shows that the first-lift candidate
`(0,0,1,2)` cannot be iterated unchanged at the next dyadic step: `K_8` is
`4`-modular, but modulo `8` the slots `(0,0,1,2)` allow clique part sizes
congruent to `1,1,2,3`, whose positive representatives have total at most
`7` when all four slots are used.  Thus `K_8` has no such four-slot
`8`-modular partition.  Any uniform dyadic fixed-slot theorem must let the
target slots depend on the current modulus, or use a larger/more flexible
slot family.

The most direct bootstrapping attempt from Lemma 4G to `M=4` is false.  One
might try to choose a self-labelled mod-`2` split, then refine the even side
into residues `{0,2}` modulo `4` and the odd side into residues `{1,3}`
modulo `4`.  The exact checker `EXPERIMENTS/hier_self_label.py` shows that
both recorded hard first-lift masks on `14` and `16` vertices admit no
partition of this form, despite having self-labelled mod-`4` colorings.  Thus
the `M=4` problem requires a simultaneous choice of both residue bits rather
than a sequential mod-`2` construction.

## Lemma 4H: The Lower Bit Of Self-Labelled Mod-`4` Is Always Solvable

Let `G` be a graph and let `b:V(G)->F_2` be any binary labeling.  Then there
is a second binary labeling `a:V(G)->F_2` such that, for every vertex `v`,

```text
|{u in N(v): a_u=a_v and b_u=b_v}| congruent a_v mod 2.
```

Equivalently, after the high bit `b` of a candidate mod-`4` label
`a+2b` is fixed arbitrarily, the low-bit condition

```text
deg_same(v) congruent a_v mod 2
```

can always be satisfied.

Proof.  Let `H` be the spanning subgraph of `G` containing exactly those edges
`uv` for which `b_u=b_v`.  Applying Lemma 4G to `H` gives a labeling
`a:V(H)->F_2` such that the number of neighbors of `v` in `H` with the same
`a`-label is congruent to `a_v` modulo `2`.  But the neighbors of `v` in `H`
with the same `a`-label are exactly the neighbors `u` of `v` satisfying both
`a_u=a_v` and `b_u=b_v`.  QED.

Thus a proof of self-labelled mod-`4` colorings only has to choose the high
bit `b` and a solution `a` to the guaranteed lower-bit system so that the next
binary digit also matches:

```text
floor(deg_same(v)/2) congruent b_v mod 2.
```

The hard part is not the parity shadow but the compatibility of this upper
bit with the lower-bit solution space.

## Lemma 4J: Polynomial Form Of The Self-Labelled Mod-`4` Equations

Let `G` be a graph, and encode a candidate label of vertex `v` modulo `4` as

```text
c_v = a_v + 2 b_v,  with a_v,b_v in F_2.
```

For an edge-neighbor `u` of `v`, put

```text
t_{uv} = (1+a_u+a_v)(1+b_u+b_v) in F_2.
```

This is the indicator, over `F_2`, that `u` and `v` have the same mod-`4`
label.  Then the self-labelled mod-`4` condition is equivalent to the two
equations, for every vertex `v`,

```text
sum_{u in N(v)} t_{uv} = a_v,
sum_{ {u,w} subset N(v), u<w } t_{uv} t_{wv} = b_v
```

over `F_2`.

Proof.  The first equation says that the parity of the same-labelled degree
of `v` is the low bit `a_v`.  For the second equation, if

```text
s_v = |{u in N(v): c_u=c_v}|,
```

then the second binary digit of `s_v` is

```text
floor(s_v/2) mod 2 = binom(s_v,2) mod 2.
```

Since `t_{uv}` is `1` exactly for same-labelled neighbors, this binomial
coefficient is precisely the second displayed sum.  Requiring this upper bit
to be `b_v` is exactly the remaining mod-`4` condition.  QED.

The first equations have degree `2` and the second equations have degree `4`
in the `2|V(G)|` binary variables.  A direct Chevalley--Warning argument
therefore has the wrong degree count: the total degree of the full system is
`6|V(G)|`, far larger than the number of variables.  Any polynomial proof must
use additional structure, not just the standard total-degree criterion.

## Lemma 4: Local Congruence Criterion For Dyadic Partitions

Let `q` be a positive integer, let `H` be a `q`-modular graph, and let
`V(H)=P_1 union ... union P_r` be a partition.  For `v in P_i`, write

```text
tau(v) = deg_H(v) mod 2q,
c_i(v) = deg_H(v, V(H)\P_i) mod 2q.
```

Then `H[P_i]` is `2q`-modular if and only if `tau(v)-c_i(v)` is constant
modulo `2q` over all `v in P_i`.

Proof.  For every `v in P_i`,

```text
deg_{H[P_i]}(v) = deg_H(v) - deg_H(v,V(H)\P_i).
```

Reducing modulo `2q` gives the displayed criterion.  QED.

Since `H` is `q`-modular, the values `tau(v)` take only two residues modulo
`2q`.  Thus a dyadic modular partition is a coloring problem controlled by
the total-degree lift from modulo `q` to modulo `2q` and the cross-degree
residue to the complement of the color class.  Diagnostics from
`EXPERIMENTS/modular_partition.py --diagnostics` show that successful
minimum-color partitions of the recorded `3`-part counterexamples do not have
constant pairwise cross-degrees between color classes; a simple equitable
partition explanation is therefore too strong.

## Lemma 4B: Pairwise Merge Criterion For Modular Parts

Let `M` be a positive integer and let `A,B` be disjoint vertex sets such that
`G[A]` is `M`-modular with residue `r_A` and `G[B]` is `M`-modular with
residue `r_B`.  Then `G[A union B]` is `M`-modular if and only if there is a
residue `rho mod M` such that

```text
r_A + deg(v,B) congruent rho mod M  for every v in A,
r_B + deg(w,A) congruent rho mod M  for every w in B.
```

Equivalently, the cross-degree residues from `A` to `B` are constant on `A`,
the cross-degree residues from `B` to `A` are constant on `B`, and the two
resulting shifted residues agree.

Proof.  For `v in A`,

```text
deg_{G[A union B]}(v) = deg_{G[A]}(v) + deg(v,B),
```

and for `w in B`,

```text
deg_{G[A union B]}(w) = deg_{G[B]}(w) + deg(w,A).
```

Reducing these two identities modulo `M` gives the criterion.  QED.

Consequently, in a partition into the minimum possible number of
`M`-modular parts, no two parts satisfy the displayed criterion.  This is the
obstruction faced by any proof that starts with singleton parts and tries to
compress them by merging.

There is also an intrinsic obstruction to decomposing arbitrary modular sets
by repeated pairwise merges.  A cycle `C_n` is `4`-modular, since every
internal degree is `2`.  For `n>=4`, a proper induced subgraph of `C_n` is
`4`-modular if and only if it is either independent or a matching, because all
proper induced degrees are in `{0,1,2}` and equality modulo `4` is equality.
Therefore the last merge in a merge-decomposition of `C_n` would partition the
cycle into two sets, each inducing either an independent set or a matching.

Such a partition exists exactly when `n` is even or divisible by `3`.  If both
parts are independent, `C_n` is bipartite and `n` is even.  If both parts are
matchings, both part sizes are even and hence `n` is even.  In the remaining
case one part is independent and the other is a matching.  Walking around the
cycle, the matching part must occur in blocks of exactly two consecutive
vertices, and the independent part must occur in singleton blocks; hence the
cyclic pattern is forced to be `MMI MMI ...`, so `3` divides `n`.  Conversely,
the bipartition works for even `n`, and the repeated `MMI` pattern works when
`3` divides `n`.

Thus every cycle `C_n` with `n>=5` odd and not divisible by `3`, for instance
`C_5` or `C_7`, is a `4`-modular set that is not merge-decomposable.  A
merge/absorption proof must allow repartitioning, not only binary
decomposition of a chosen modular part.

The exact script `EXPERIMENTS/decomposable_partition.py` shows a stronger
computational limitation: there are even graphs on `10` vertices with a
`2`-part `4`-modular partition but no `2`-part partition into
merge-decomposable `4`-modular parts.  One mask is `2019815596227`.

## Lemma 5: Four-Color Sign Formula

Let `q` be a positive integer and let `H` be a graph.  A coloring of `V(H)` by
four colors may be represented by two signs `x_v,y_v in {+1,-1}` at each
vertex.  For a sign function `z`, put

```text
S_z(v) = sum_{u in N_H(v)} z_u.
```

Then, for every vertex `v`,

```text
4 deg_{same}(v)
= deg_H(v) + x_v S_x(v) + y_v S_y(v) + x_v y_v S_{xy}(v),
```

where `deg_same(v)` is the degree of `v` inside its own color class.
Consequently, the four color classes are `2q`-modular if and only if the
right-hand side is constant modulo `8q` on each of the four sign-pair classes.

Proof.  The indicator that a neighbor `u` has the same pair of signs as `v` is

```text
((1+x_v x_u)(1+y_v y_u))/4.
```

Summing this identity over all neighbors `u` of `v` gives the displayed
formula.  Since two integers are congruent modulo `2q` exactly when four times
them are congruent modulo `8q`, the final assertion follows.  QED.

This reformulates the conjectural `4`-part first dyadic lift as a problem
about finding two signings whose three signed neighbor sums make the displayed
quantity depend only on the sign pair.  It is exact, but it does not yet give
a construction of the signs.

## Lemma 5A: Binary Parity-Split Equation

Let `H` be a graph in which every degree is even, and let
`x:V(H)->F_2` be a two-coloring.  Write `A` for the adjacency matrix of `H`
over `F_2`.  For every vertex `v`, the parity of the degree of `v` inside its
own color class is

```text
(A x)_v.
```

Consequently, the internal-degree parity is constant on each of the two color
classes if and only if there are `a,b in F_2` such that

```text
A x = a 1 + b x.
```

Proof.  If `x_v=0`, then the neighbors of `v` in its own color class are the
neighbors `u` with `x_u=0`; their number is

```text
deg_H(v) - sum_{u~v} x_u,
```

which is `(A x)_v` modulo `2` because `deg_H(v)` is even.  If `x_v=1`, then
the number of same-color neighbors is exactly `sum_{u~v} x_u`, again
`(A x)_v` modulo `2`.

Thus the parity is constant with value `r_0` on `x=0` and value `r_1` on
`x=1` exactly when

```text
(A x)_v = r_0 + (r_0+r_1)x_v
```

for every `v`.  Put `a=r_0` and `b=r_0+r_1`.  QED.

This is only the lower-bit shadow of the first lift from modulus `2` to
modulus `4`: it controls degrees modulo `2` inside a bipartition of an even
graph, but not the next bit needed to make degrees constant modulo `4`.
The natural hierarchical strengthening "first make such a parity-pattern
split, then split each side into two `4`-modular parts" is false: the
`n=14` mask `2354908367450303302346343845` has a `4`-part `4`-modular
partition but `EXPERIMENTS/hierarchical_lift.py` checks that no partition of
this hierarchical form exists.

## Lemma 5B: Dyadic Bit Polynomial

Let `q=2^s`, and let `z_1,...,z_D in {0,1}`.  In `F_2`,

```text
floor((z_1+...+z_D)/q) mod 2
= sum_{|I|=q} product_{i in I} z_i.
```

Equivalently, the `q`'s binary digit of a sum of bits is the elementary
symmetric polynomial of degree `q` in those bits.

Proof.  If exactly `h` of the variables `z_i` are equal to `1`, the right-hand
side is

```text
binom(h,q) mod 2.
```

By Lucas's theorem, since `q=2^s`, this binomial coefficient is odd exactly
when the `2^s` binary digit of `h` is `1`.  This is precisely
`floor(h/q) mod 2`.  QED.

For a dyadic lift from `q` to `2q`, this lemma identifies the new bit of an
internal degree as a degree-`q` polynomial in the indicators of same-part
neighbors.  In a four-coloring represented by two vertex bits, each same-part
indicator has degree `2`; the resulting equations have degree `2q`.  Thus the
algebraic formulation has enough variables heuristically, but a direct
Chevalley-Warning degree count deteriorates with `q`.

## Lemma 5C: The Dyadic-Bit Degree Barrier Is Real

Let `q=2^s`, let colors be encoded by vectors in `F_2^t`, and consider a
star whose center has fixed color `0`.  If the leaf `i` has color variables

```text
x_i=(x_{i1},...,x_{it}) in F_2^t,
```

put

```text
z_i = 1_{x_i=0} = product_{j=1}^t (1+x_{ij}).
```

For `D>=q`, the Boolean function

```text
floor((z_1+...+z_D)/q) mod 2
```

has multilinear degree exactly `qt` over `F_2`.

Proof.  By Lemma 5B the function is the elementary symmetric polynomial

```text
e_q(z_1,...,z_D).
```

The monomial

```text
prod_{i=1}^q prod_{j=1}^t x_{ij}
```

appears with coefficient `1`, coming from the unique term
`z_1 z_2 ... z_q` in `e_q`.  No other `q`-subset of leaves can produce this
same monomial, because it would omit at least one of the leaf blocks
`{x_{ij}:1<=j<=t}` or include variables from a different block.  Hence the
degree is at least `qt`.  Since each `z_i` has degree `t` and `e_q` is a sum
of products of `q` of the `z_i`, the degree is at most `qt`.  QED.

Consequently, the degree growth in Lemma 5B is not an artifact of the sign
formula.  With `r=q^alpha` colors one has `t=alpha log_2 q+O(1)` color bits,
so the local equations for the new dyadic bit have degree
`Omega(q log q)` even in this star subproblem.  A direct
Chevalley--Warning or Combinatorial Nullstellensatz attack that writes one
such exact local equation per vertex has total degree larger than the number
of coloring variables by a factor of order `q`.  Any algebraic proof of a
sublinear-exponent dyadic partition theorem must therefore use a nonlocal
compression, a hidden linearization, or a structural reduction rather than
the raw vertex-by-vertex top-bit equations.

## Lemma 6: Degree-Class Bridge

Let `H` be an induced subgraph of `G`, and let `A subset V(H)` be a set of
vertices that all have the same degree in `H`.  If all vertices of `A` also
have the same number of neighbors in `V(H)\A`, then `H[A]` is regular.

Proof.  Let the common degree of vertices of `A` in `H` be `d`, and let the
common number of neighbors in `V(H)\A` be `s`.  For every `v in A`,

```text
deg_{H[A]}(v) = d - s.
```

Thus every vertex of `H[A]` has the same degree.  QED.

A stronger sufficient condition is that all vertices of `A` have the same
trace, that is the same neighborhood, in `V(H)\A`.  The important limitation is
that a large repeated-degree class need not satisfy this outside-degree
condition.  Partitioning a repeated-degree class by traces into `V(H)\A` is
not enough, because edges from a trace class to the rest of `A` may still vary.

## Lemma 7: Twin-Quotient Lower Bound

Call two vertices twins if they have the same neighborhood outside the pair.
Twin classes induce either cliques or independent sets, and between two twin
classes the bipartite graph is either complete or empty.  Let `t(G)` be the
number of twin classes of `G`.  Then

```text
reg(G) >= max { n/t(G), c log t(G) }
```

for an absolute constant `c>0`.

Proof.  Some twin class has order at least `n/t(G)`.  Since a twin class
induces either a clique or an independent set, it is regular.

For the second term, form the quotient graph `Q` whose vertices are the twin
classes and whose edges record complete adjacency between classes.  Choose one
representative from each class.  Any clique or independent set in `Q` lifts to
a clique or independent set in `G`, hence to a regular induced subgraph.  By
Ramsey's theorem, `Q` has a clique or independent set of order at least
`c log t(G)`.  QED.

Optimizing the displayed lower bound over `t` gives only `Omega(log n)`.
Thus neighborhood diversity alone cannot prove the target; it must be coupled
with a stronger statement about the quotient or with a way to use class sizes.

## Proposition 8: Ramsey-Core Reduction

For `C>0`, call an `n`-vertex graph `C`-Ramsey if it has no clique and no
independent set of order greater than `C log n`.  Suppose that for every fixed
`C>0`,

```text
min { reg(G) : |V(G)|=n and G is C-Ramsey } / log n -> infinity.
```

Then `F(n)/log n -> infinity`.

Proof.  Fix `A>0`.  Choose `C>A/c`, where `c` is the absolute constant in the
Ramsey lower bound convention used above.  Let `G` be any graph on `n`
vertices.  If `G` is not `C`-Ramsey, then it has a clique or independent set
of order at least `C log n > A log n`, hence a regular induced subgraph of
that order.  If `G` is `C`-Ramsey, the displayed assumption gives
`reg(G)>A log n` for all sufficiently large `n`.  Since `A` was arbitrary,
`F(n)/log n -> infinity`.  QED.

Known results on `C`-Ramsey graphs show strong pseudorandom features, such as
large induced subgraphs with many distinct degrees.  These do not immediately
imply regular induced subgraphs; they identify the hard core where a proof
must exploit more than homogeneous-set Ramsey theory.

## Proposition 8A: Fixed Clique Number Is Not The Hard Case

For every fixed integer `r>=3`, there is a constant `c_r>0` such that every
`K_r`-free graph on `n` vertices contains an independent set of order at least

```text
c_r n^{1/(r-1)}.
```

Consequently, for every fixed `r`, every `n`-vertex graph `G` with
`omega(G)<r` satisfies

```text
reg(G) >= c_r n^{1/(r-1)} = omega(log n).
```

The same conclusion holds when `alpha(G)<r`, by applying the statement to the
complement.

Proof.  The standard Ramsey recurrence gives

```text
R(r,t) <= binom(r+t-2,r-1) <= C_r t^{r-1}
```

for a constant `C_r` depending only on `r`.  If
`n >= C_r t^{r-1}`, then every `n`-vertex graph contains either a clique of
order `r` or an independent set of order `t`.  A `K_r`-free graph therefore
has an independent set of size at least `c_r n^{1/(r-1)}` after adjusting
constants.  An independent set is a `0`-regular induced subgraph, proving the
displayed lower bound for `reg(G)`.  The complement argument is identical,
since cliques in `G` are independent sets in `complement(G)` and regularity is
preserved under complementation.  QED.

Thus a counterexample sequence to the conjecture with
`reg(G_n)=O(log |G_n|)` must satisfy

```text
omega(G_n) -> infinity
and
alpha(G_n) -> infinity.
```

This is much weaker than the `C`-Ramsey reduction: it removes fixed-clique and
fixed-independence-number classes, but it does not control graphs with
`omega(G)` and `alpha(G)` growing slowly.

## Lemma 8B: Fixed-Clique-Free Induced Pieces In Counterexamples

Let `G` be a graph with `reg(G)<k`.  For every `2 <= r <= k`, every induced
`K_r`-free subgraph of `G` has fewer than `R(r,k)` vertices.  Equivalently,
every vertex set `U` with `|U| >= R(r,k)` contains a clique of order `r`.
The complement statement also holds: every induced `K_r`-free subgraph of
`complement(G)` has fewer than `R(r,k)` vertices.

Proof.  Let `H=G[U]` be `K_r`-free.  If `|U| >= R(r,k)`, Ramsey's theorem
gives either a clique of order `r` in `H` or an independent set of order `k`
in `H`.  The clique is excluded, while the independent set is an induced
`0`-regular subgraph of `G` on `k` vertices, contradicting `reg(G)<k`.

For the complement statement, observe that
`reg(complement(G))=reg(G)`, because the complement of a `d`-regular graph on
`m` vertices is `(m-1-d)`-regular.  Apply the first part to the complement.
QED.

Using the fixed-`r` off-diagonal Ramsey estimate

```text
R(r,k) <= C_r k^{r-1}/(log k)^{r-2}
```

for `r>=3`, this says, for example, that a counterexample has no induced
triangle-free or co-triangle-free subgraph on `C k^2/log k` vertices.  This is
consistent with random-like extremal examples and does not by itself imply a
subexponential upper bound for `G(k)`.

## Lemma 9: Hereditary Density Window For Counterexamples

If `G` has no regular induced subgraph of order at least `k`, then for every
nonempty vertex set `U` with `u=|U|`,

```text
average_degree(G[U]) > u/k - 1
and
average_degree(complement(G[U])) > u/k - 1.
```

Equivalently,

```text
u(u-k)/(2k) < e(G[U]) < binom(u,2) - u(u-k)/(2k).
```

Proof.  Since every induced subgraph of `G` also has no regular induced
subgraph of order at least `k`, the graph `G[U]` has no independent set of
order `k`.  By the Caro--Wei bound,

```text
alpha(G[U]) >= u / (average_degree(G[U]) + 1).
```

Thus `u/(average_degree(G[U])+1) < k`, giving the first displayed inequality.
Apply the same argument to the complement of `G[U]`, since a clique in `G[U]`
is also a regular induced subgraph.  The edge-count formulation is just the
translation from average degree to edge density.  QED.

This hereditary lower and upper density window is weak when `k` is large, but
it is useful because it applies to every induced subgraph of a counterexample.
Any density increment or dependent-random-choice route must exploit this
window more efficiently than the direct Ramsey argument.

## Lemma 9A: Density-Only DRC Cannot Beat The Exponential Scale

Let `H` be an `N`-vertex graph and let `Gamma` be either `H` or its
complement with edge density `p`.  A standard dependent-random-choice step
with `t` sampled roots can guarantee, from density information alone, a common
neighborhood of expected size at least

```text
N p^t.
```

This order is tight up to constants for near-regular density-`p` graphs.

Proof.  Choose `t` roots independently and uniformly from `V(Gamma)`, with
replacement, and let `X` be their common neighborhood.  Then

```text
E |X| = sum_{v in V(Gamma)} (deg_Gamma(v)/N)^t.
```

By convexity this is at least

```text
N (average_degree(Gamma)/N)^t = N p^t (1+O(1/N))^t,
```

depending on whether density is normalized by `N^2` or `binom(N,2)`.  In a
regular or near-regular graph of density `p`, the same expression is also at
most a constant multiple of `N p^t`, proving tightness for density-only
information.  QED.

Consequently, using the denser of a graph and its complement gives `p>=1/2`,
so retaining even `k` common neighbors after `t` roots requires

```text
N >= k 2^t.
```

Using only the hereditary density lower bound of Lemma 9 can be much worse:
in sparse induced subgraphs the available density may be only `p=Theta(1/k)`,
forcing `N >= k^{t+1}` to retain `k` leaves.  Thus any DRC proof whose regular
template needs `t=Theta(k)` specified root vertices already has exponential or
worse size cost.  A successful DRC route must carry additional internal
degree control on the leaf set; a large common neighborhood alone simply
returns to Ramsey or to the original `G(k)` problem inside the leaves.

## Lemma 10: Equitable-Partition Cell Certificate

Let `P={V_1,...,V_t}` be an equitable partition of `V(G)`, meaning that for
every pair `i,j` and every two vertices `x,y in V_i`,

```text
|N(x) cap V_j| = |N(y) cap V_j|.
```

Then every cell `V_i` induces a regular subgraph.  In particular,

```text
reg(G) >= max_i |V_i|.
```

Proof.  Apply the defining equality with `j=i`.  Every vertex of `V_i` has the
same number of neighbors in `V_i`, which is exactly its degree in `G[V_i]`.
Thus `G[V_i]` is regular.  QED.

The coarsest equitable partition obtained by color refinement often has large
cells in structured graphs, but random-like graphs typically refine to
singletons.  Thus this is another useful certificate that does not address the
hard `C`-Ramsey core by itself.

## Lemma 11: Repeated Degree Gives Bounded Spread

Let `H` be an induced subgraph of `G`, and let `A subset V(H)` be a set of
vertices with the same degree in `H`.  Put `s=|V(H)\A|`.  Then the degrees in
`G[A]` have spread at most `s`; that is,

```text
Delta(G[A]) - delta(G[A]) <= s.
```

Proof.  Let the common degree of vertices of `A` in `H` be `d`.  For
`v in A`,

```text
deg_{G[A]}(v) = d - deg_H(v, V(H)\A).
```

The second term lies between `0` and `s`, so all degrees in `G[A]` lie in the
interval `[d-s,d]`.  QED.

Thus any theorem forcing large regular induced subgraphs in graphs of small
additive degree spread would combine naturally with repeated-degree results.
For example, if every `r`-vertex graph with degree spread at most `s` had a
regular induced subgraph of order at least `Phi(r,s)`, then any induced
subgraph `H` with an equal-degree class `A` of order `r` and complement size
`s` would contain a regular induced subgraph of order at least `Phi(r,s)`.
The current obstacle is to prove a lower bound for `Phi(r,s)` that beats the
Ramsey bound in the needed parameter range.

Computationally, this route remains plausible in very small cases.  Exhaustive
checks with `EXPERIMENTS/degree_spread.py` show that every labelled graph on
`6` or `7` vertices with degree spread at most `1` has a regular induced
subgraph of order at least `4`; local search on `10` vertices with spread `1`
found examples with maximum regular order `5`, but not smaller.

However, the strongest natural linear guess is false.  The script
`EXPERIMENTS/search_bounded_spread.py` found a spread-`1` graph on `12`
vertices with maximum regular induced order `5`, and a spread-`1` graph on
`14` vertices with maximum regular induced order `6`.  These are verified by

```text
python3 EXPERIMENTS/degree_spread.py 12 --mask 22368837872701959356
python3 EXPERIMENTS/degree_spread.py 14 --mask 146294004578047919044267715
```

Thus it is false that every spread-`1` graph contains a regular induced
subgraph on at least half its vertices.  Any bounded-spread theorem useful for
Problem 82 must have a weaker, but still asymptotically strong, lower bound.

## Lemma 12: Minimal Repeated-Degree Host Obstruction

Let `H` be an induced subgraph of `G` containing a set
`A={a_1,...,a_k}` of vertices with equal degree in `H`.  Suppose `H` is
vertex-minimal with this property, in the sense that no proper induced
subgraph of `H` contains `k` vertices of equal degree.  Put `B=V(H)\A`.

Then for every nonempty set `X subset B`, the numbers

```text
|N_H(a_i) cap X|,  i=1,...,k,
```

are not all equal.

Proof.  Let the common degree of vertices of `A` in `H` be `d`.  If a nonempty
`X subset B` had `|N_H(a_i) cap X|=r` for every `i`, then in the proper
induced subgraph `H-X` every vertex `a_i` would have degree `d-r`.  Thus
`H-X` would still contain `k` vertices of equal degree, contradicting the
minimality of `H`.  QED.

Equivalently, the trace vectors of vertices in `B` on the coordinate set `A`
form a multiset of `0/1` vectors with no nonempty submultiset whose coordinate
sum is a constant vector.  If `B` itself had constant trace-sum on `A`, then
Lemma 5 would make `H[A]` regular.  This frames the repeated-degree route as a
finite discrepancy or zero-sum problem for trace vectors, with the additional
complication that large repeated trace classes must be handled recursively.

## Lemma 13: Exponential Trace-Counting Obstruction

For every `k>=2`, there is a family `F` of `2^{k-1}-1` distinct nonconstant
vectors in `{0,1}^k` such that no nonempty subfamily has coordinate-sum equal
to a constant vector.

Proof.  Let `F` be the set of all nonzero `0/1` vectors whose last coordinate
is `0`.  Then `|F|=2^{k-1}-1`.  In any nonempty subfamily, the last coordinate
sum is `0`, while some other coordinate has positive sum because at least one
chosen vector is nonzero.  Hence the coordinate-sum vector is not constant.
QED.

Consequently, the minimal-host obstruction in Lemma 12 cannot be defeated by
showing merely that many distinct trace types force a balanced deletion:
exponentially many distinct traces may still avoid one.  A successful
trace-based proof must exploit multiplicities, internal structure of trace
classes, or additional restrictions coming from the ambient graph.

## Lemma 14: Trace-Class Recursion In A Counterexample

Let `G` have no regular induced subgraph of order at least `k`.  Fix a vertex
set `A subset V(G)`, and for each trace `T subset A` put

```text
C_T = { v in V(G)\A : N_G(v) cap A = T }.
```

Then `|C_T| < G(k)` for every `T`.

Proof.  If some trace class `C_T` had order at least `G(k)`, then the induced
graph `G[C_T]` would contain a regular induced subgraph on at least `k`
vertices by the definition of `G(k)`.  This subgraph is also induced in `G`,
contradicting the hypothesis.  QED.

This is the only recursion that trace partitioning gives for free.  Together
with Lemma 13 it shows why a direct "partition by traces and pigeonhole" proof
cannot beat the Ramsey scale: a counterexample may have exponentially many
trace classes, and each class is only controlled by the original unknown
quantity `G(k)`.

## Lemma 14A: Homogeneous Trace Amplification Certificate

Let `A` be an independent set in `G`, let `T subset A`, and let

```text
C_T = {v in V(G)\A : N_G(v) cap A = T}.
```

If `C_T` contains an independent set `B` of size `s`, then:

1. if `|T|>=s`, `G` contains an induced `s`-regular subgraph on `2s`
   vertices;
2. if `|A\T|>=s`, `G` contains an induced `0`-regular subgraph on `2s`
   vertices.

Proof.  In the first case choose `A' subset T` with `|A'|=s`.  The set
`A' union B` induces the complete bipartite graph `K_{s,s}`, because `A` and
`B` are independent and every vertex of `B` is adjacent to every vertex of
`T`.  This graph is `s`-regular on `2s` vertices.

In the second case choose `A' subset A\T` with `|A'|=s`.  There are no edges
inside `A'`, no edges inside `B`, and no edges between `A'` and `B`, so the
union is independent on `2s` vertices.  QED.

The lemma is quantitatively limited as a standalone route.  To force a
regular induced subgraph of order at least `k` from a single trace class one
needs `s>=k/2`, hence an independent set `A` of order at least `k/2`.
Ramsey's theorem supplies only `Theta(log n)` vertices in the inverse regime
`n=2^{o(k)}`.  A trace-amplification proof would therefore need to combine
many trace classes, not just one large class.

## Lemma 14A.1: Regular Trace-Class Amplification

Let `A` be an independent set in `G`, let `T subset A`, and let

```text
C_T = {v in V(G)\A : N_G(v) cap A = T}.
```

Suppose `B subset C_T` induces an `r`-regular graph on `b` vertices.  If

```text
b-r <= |T|,
```

then `G` contains a regular induced subgraph on `2b-r` vertices.

Proof.  Choose `X subset T` with `|X|=b-r`.  The set `X` is independent,
because `A` is independent, and every vertex of `B` is adjacent to every
vertex of `X` by the definition of `C_T`.  Therefore every vertex of `B` has
degree

```text
r + |X| = r + b-r = b
```

inside `G[B union X]`, while every vertex of `X` has degree `b`, all of it
going to `B`.  Thus `G[B union X]` is `b`-regular on

```text
b+|X| = 2b-r
```

vertices.  QED.

Lemma 14A is the special case `r=0`, with either `X subset T` giving a
complete bipartite graph or `X subset A\T` giving an independent set.  The
new form shows what extra information a trace recursion would need: a large
regular witness inside a trace class is useful when its internal degree is
not too close to its order.  A high-degree witness only adds a few vertices
from `T`, so this lemma still does not close the trace route without degree
control for the regular witnesses found recursively.

## Lemma 14A.2: Clique-Base Trace-Class Amplification

Let `A` be a clique in `G`, let `T subset A`, and let

```text
C_T = {v in V(G)\A : N_G(v) cap A = T}.
```

Suppose `B subset C_T` induces an `r`-regular graph on `b` vertices.  If

```text
r+1 <= |A\T|,
```

then `G` contains a regular induced subgraph on `b+r+1` vertices.

Proof.  Choose `X subset A\T` with `|X|=r+1`.  Since `A` is a clique, `X`
induces a clique, and every vertex of `X` has degree `r` inside `X`.  There
are no edges between `B` and `X`, because all vertices of `B` have trace `T`
on `A`.  Therefore every vertex of `B` has degree `r` inside
`G[B union X]`, and every vertex of `X` also has degree `r`.  Thus
`G[B union X]` is `r`-regular on `b+r+1` vertices.  QED.

The independent-base and clique-base amplification lemmas pull in opposite
directions.  With an independent base, low internal degree in `B` is useful
because `b-r` vertices from the trace can be added.  With a clique base, high
internal degree in `B` is useful because `r+1` non-neighbors in the base can
be added.  A trace proof that alternates between large independent and clique
bases would need to exploit this complementary degree information.

## Corollary 14A.3: Trace-Class Degree Restrictions In Counterexamples

Let `G` have no regular induced subgraph of order at least `k`.

1. If `A` is independent, `T subset A`, and `B subset C_T` induces an
   `r`-regular graph on `b` vertices, then

```text
b-r > |T|       or       2b-r < k.
```

2. If `A` is a clique, `T subset A`, and `B subset C_T` induces an
   `r`-regular graph on `b` vertices, then

```text
r+1 > |A\T|     or       b+r+1 < k.
```

Proof.  If the first alternative in (1) fails, Lemma 14A.1 gives a regular
induced subgraph on `2b-r` vertices, so this order must be less than `k`.
The proof of (2) is identical using Lemma 14A.2.  QED.

These inequalities are weak for one trace class in isolation, but they give a
checkable degree-window obstruction for any attempt to combine many trace
classes over a large homogeneous set.

## Lemma 14A.4: One-Trace Homogeneous Amplification Is Exhaustive

Let `A` be independent, let `T subset A`, and let `B subset C_T` induce an
`r`-regular graph on `b` vertices.  For any `X subset A`, write

```text
x = |X cap T|,       y = |X \ T|.
```

If `B union X` is regular and `B` and `X` are both nonempty, then either

```text
y=0 and x=b-r,
```

which is exactly Lemma 14A.1, or

```text
x=0 and r=0,
```

in which case `B union X` is independent.

Proof.  Vertices of `B` have degree `r+x` in `G[B union X]`.  Vertices in
`X cap T`, if any, have degree `b`, while vertices in `X\T`, if any, have
degree `0`.  If both `x` and `y` are positive then regularity would force
`b=0`, impossible.  If `y=0`, regularity forces `r+x=b`, i.e. `x=b-r`.  If
`x=0`, regularity forces `r=0`, and then all vertices have degree `0`.  QED.

The clique-base dual is as follows.  Let `A` be a clique, let `T subset A`,
and let `B subset C_T` induce an `r`-regular graph on `b` vertices.  For
`X subset A`, again put `x=|X cap T|` and `y=|X\T|`.  If `B union X` is
regular and `B` and `X` are both nonempty, then either

```text
x=0 and y=r+1,
```

which is exactly Lemma 14A.2, or

```text
y=0 and r=b-1,
```

in which case `B union X` is a clique.

Indeed, vertices of `B` have degree `r+x`; vertices in `X cap T` have degree
`b+x+y-1`; and vertices in `X\T` have degree `x+y-1`.  If both `x` and `y`
are positive, the two types of vertices in `X` differ by `b`, impossible.
If `x=0`, regularity gives `r=y-1`.  If `y=0`, regularity gives `r=b-1`.
QED.

Consequently, a one-trace proof cannot be improved by mixing vertices from
both `T` and its complement inside the same homogeneous base.  Any stronger
trace argument must combine multiple trace classes or use additional
structure inside the trace classes.

## Lemma 14B: Maximal Independent Trace Ramsey Bound

Let `G` be a graph with no regular induced subgraph of order at least `k`,
and let `A` be a maximal independent set of size `h<k`.  For each
nonempty `T subset A`, put

```text
C_T = {v in V(G)\A : N_G(v) cap A = T}.
```

Then

```text
|V(G)| <= h + sum_{nonempty T subset A}
              ( R(k-1, k-h+|T|) - 1 ).
```

Equivalently,

```text
|V(G)| <= h + sum_{j=1}^h binom(h,j)
              ( R(k-1, k-h+j) - 1 ).
```

Proof.  Since `A` is maximal, every vertex outside `A` has at least one
neighbor in `A`, so the nonempty trace classes cover `V(G)\A`.

Fix a nonempty trace `T`.  The graph `G[C_T]` has no clique of order `k-1`:
if `Q subset C_T` were such a clique, then for any `a in T` the set
`Q union {a}` would be a clique of order `k`, hence a regular induced
subgraph.  Also `G[C_T]` has no independent set of order `k-h+|T|`: such an
independent set, together with `A\T`, would be independent of order

```text
(k-h+|T|) + (h-|T|) = k,
```

again a regular induced subgraph.  Hence

```text
|C_T| <= R(k-1,k-h+|T|)-1.
```

Summing over the trace classes gives the first inequality, and grouping by
`j=|T|` gives the second.  QED.

This improves the completely free trace recursion of Lemma 14 by using
maximality of `A`, but by itself it does not break the diagonal Ramsey scale.
When `h` is close to `k`, many large traces have weak independent-set
thresholds, and the displayed sum remains exponentially large under the
standard binomial estimates for ordinary Ramsey numbers.  Thus any trace
route still needs an argument coupling different trace classes, not just a
separate Ramsey bound for each class.

## Lemma 15: Total Trace Imbalance In A Repeated-Degree Host

In the setting of Lemma 12, write

```text
t_i = |N_H(a_i) cap B|,  i=1,...,k.
```

Then

```text
max_i t_i - min_i t_i <= k-1.
```

Equivalently, if the vertices of `B` are encoded by their trace vectors on
`A`, the coordinate sums of all trace vectors have spread at most `k-1`.

Proof.  Let `d` be the common degree of the vertices of `A` in `H`, and let
`e_i = deg_{H[A]}(a_i)`.  Then `t_i=d-e_i`.  Since
`0 <= e_i <= k-1`, the numbers `t_i` lie in an interval of length at most
`k-1`.  QED.

This additional constraint is not present in the exponential construction in
Lemma 13: the family of all nonzero traces with one coordinate fixed to zero
has exponentially large total imbalance.  Thus the trace route should be
studied as a zero-sum-free sequence problem with small total imbalance, not as
an unrestricted trace-counting problem.

The script `EXPERIMENTS/trace_balance_bound.py` checks the distinct-trace
version of this strengthened obstruction.  For `k=2,3,4,5` it still finds
families of sizes `1,3,7,15` with no balanced subfamily and total imbalance at
most `k-1`.  These examples show that even Lemma 15 does not immediately give
a subexponential trace count; a proof would need still more input, such as
multiplicity recursion or constraints from the internal graph on `A`.

## Lemma 16: Graphical Compensation In A Repeated-Degree Host

In the setting of Lemma 12, the trace-sum vector on `A` must be compensated by
the degree sequence of a graph on `A`.  More explicitly, with

```text
t_i = |N_H(a_i) cap B|,
```

there is an integer `D` such that

```text
(D-t_1, ..., D-t_k)
```

is the degree sequence of the graph `H[A]`.

Proof.  Let `D` be the common degree of the vertices `a_i` in `H`.  Then

```text
deg_{H[A]}(a_i) = D - t_i
```

for every `i`, so the displayed sequence is exactly the degree sequence of
`H[A]`.  QED.

This condition is stronger than the spread bound in Lemma 15.  The small
zero-sum-free trace families found by `EXPERIMENTS/trace_balance_bound.py`
for `k=2,3,4,5` without graphical compensation do not satisfy Lemma 16.  With
the `--require-graphical` filter, the maximum distinct admissible sizes are
`0,2,4,9` for `k=2,3,4,5`.

## Lemma 17: Steinitz Bound For Minimal Trace Obstructions

In the setting of Lemma 12,

```text
|B| <= (3k)^{k-1}.
```

Proof.  For every `b in B`, define the difference trace vector

```text
v_b = (1_{ba_1 in E(H)} - 1_{ba_k in E(H)}, ...,
       1_{ba_{k-1} in E(H)} - 1_{ba_k in E(H)})
       in {-1,0,1}^{k-1}.
```

By Lemma 12, no nonempty `X subset B` has constant trace-sum on `A`.  In the
difference-vector notation, this says exactly that no nonempty submultiset of
the vectors `{v_b : b in B}` has sum `0`.

Let

```text
T = sum_{b in B} v_b.
```

By Lemma 15, `||T||_infty <= k-1`.  Put `d=k-1` and `m=|B|`.

If `m<d^2`, then `m <= d^2 <= (3d+3)^d` for every `d>=1`, so assume
`m>=d^2`.

Use the standard Steinitz rearrangement lemma in this form: if vectors in
`R^d` have infinity norm at most `R` and sum `0`, then they can be ordered so
that every partial sum has infinity norm at most `dR`.  Apply it to the
centered vectors

```text
u_b = v_b - T/m.
```

These vectors sum to `0` and have infinity norm at most `1+d/m`.  Hence there
is an ordering for which the centered partial sums `Q_j` satisfy

```text
||Q_j||_infty <= d(1+d/m) <= d+1
```

for every `0<=j<=m`.  For the corresponding original partial sums

```text
P_j = sum_{i<=j} v_i,
```

we have

```text
P_j = Q_j + (j/m) T.
```

In each coordinate, `(j/m)T` lies in an interval of length at most `d`, while
the correction `Q_j` lies in `[-d-1,d+1]`.  Therefore all values of a fixed
coordinate of all `P_j` lie in an interval of length at most `3d+2`, and so
in at most `3d+3` integer values.

If two of these `m+1` partial sums were equal, the consecutive block between
them would be a nonempty submultiset of the `v_b` with sum `0`, contradicting
Lemma 12.  Hence the `m+1` partial sums are distinct lattice points in a box
with at most

```text
(3d+3)^d
```

points.  Thus

```text
m+1 <= (3d+3)^d.
```

Since `3d+3=3k`, the displayed bound follows.  QED.

This is still far too weak to prove `G(k)<=2^{o(k)}` by itself, because it is
`2^{O(k log k)}`.  Its value is structural: any repeated-degree minimal host
has a bounded outside obstruction depending only on the repeated class size,
not on the ambient graph.

## Lemma 18: Separating Functional Bound For Trace Obstructions

In the setting of Lemma 12, use the difference trace vectors `v_b` from
Lemma 17 and put `d=k-1`.  Suppose there is an integer vector
`a in Z^d` such that

```text
a dot v_b >= 1
```

for every `b in B`.  Then

```text
|B| <= d ||a||_1.
```

Proof.  Let `T=sum_{b in B} v_b`.  By Lemma 15, `||T||_infty <= d`.  Since
each vector has positive `a`-weight,

```text
|B| <= sum_{b in B} a dot v_b = a dot T <= ||a||_1 ||T||_infty <= d ||a||_1.
```

QED.

This identifies a concrete way to improve Lemma 17: prove that every minimal
trace obstruction either has a small positive dependence, contradicting
zero-sum-freeness with the available multiplicities, or admits a separating
integer functional with `||a||_1=2^{o(k)}`.  The general determinant bounds for
such separators are only exponential in `k log k`, so this remains an
unproved route.

## Conditional Proposition: Repeated-Degree / Bounded-Spread Bridge

Let `E(r)` be the least integer `N` such that every `N`-vertex graph contains
an induced subgraph with at least `r` vertices of the same degree.  Let
`Phi(r,s)` be the minimum, over all `r`-vertex graphs with degree spread at
most `s`, of the largest order of a regular induced subgraph.  Put

```text
S(r) = (3r)^{r-1}.
```

Then for all `r`,

```text
F(E(r)) >= Phi(r,S(r)).
```

Proof.  Let `G` be any graph on `E(r)` vertices.  By definition of `E(r)`,
there is an induced subgraph `H_0` containing a set `A` of `r` vertices with
equal degree in `H_0`.  Among induced subgraphs of `H_0` that contain `A` and
in which the vertices of `A` still have equal degree, choose one, say `H`,
with the fewest vertices.  Write `B=V(H)\A`.

Lemma 17 gives `|B| <= S(r)`.  By Lemma 11, the graph `G[A]=H[A]` has degree
spread at most `|B|`, and hence at most `S(r)`.  By the definition of
`Phi(r,S(r))`, the induced graph `G[A]` contains a regular induced subgraph on
at least `Phi(r,S(r))` vertices.  This subgraph is also induced in `G`.  Since
`G` was arbitrary, `F(E(r)) >= Phi(r,S(r))`.  QED.

Thus the repeated-degree route has been reduced to two quantitative tasks:
force large repeated-degree classes in induced subgraphs, and prove a
bounded-spread theorem strong enough for the specific spread scale `S(r)`.
With the current Steinitz value of `S(r)`, this bridge is not yet strong enough
to imply the target.

## Conditional Proposition: Exact Dyadic Modular Program

For a power of two `q`, call a vertex set `S` `q`-modular if all degrees in
`G[S]` are congruent modulo `q`.  Let `n` be large.  Suppose there are powers
of two

```text
2 = q_1 < q_2 < ... < q_t
```

and integers

```text
m_1 = floor(n/2), m_2, ..., m_t
```

such that

```text
m_t <= q_t
and
m_t / log n -> infinity,
```

and such that the following lifting statement holds for every graph `G` and
every `i<t`:

```text
every q_i-modular induced subgraph of order at least m_i
contains a q_{i+1}-modular induced subgraph of exactly m_{i+1} vertices.
```

Then `F(n)/log n -> infinity`.

Proof.  Lemma 3 gives a `2`-modular induced subgraph of order at least
`m_1`.  Iterating the assumed exact-size lifts gives a `q_t`-modular induced
subgraph on exactly `m_t` vertices.  Since `m_t <= q_t`, Lemma 2 makes this
induced subgraph regular.  Its order is `m_t=omega(log n)`, proving the
claim.  QED.

The exact-size hypothesis is deliberate.  A lower bound alone on the size of a
modular witness is not enough for the terminal step, because arbitrary subsets
of a `q`-modular set need not remain `q`-modular.

## Lemma 19: Component and Cocomponent Restrictions

If `G` has no regular induced subgraph of order at least `k`, then `G` has
fewer than `k` connected components and fewer than `k` connected components in
its complement.

Proof.  If `G` has at least `k` connected components, choosing one vertex from
each of `k` components gives an independent set of order `k`, hence a
`0`-regular induced subgraph.  Applying the same argument to the complement
gives the cocomponent statement, because a regular induced subgraph in the
complement is regular in `G` after complementing degrees.  QED.

This is a weak but useful sanity check for structural reductions: any
extremal counterexample must be connected and anticonnected up to fewer than
`k` pieces.

## Lemma 20: Induced Path and Copath Exclusion

If `G` has no regular induced subgraph of order at least `k`, then neither
`G` nor its complement contains an induced path on `2k-1` vertices.

Proof.  An induced path on `2k-1` vertices contains an independent set of size
`k`, obtained by taking alternating vertices along the path.  That independent
set is an induced `0`-regular subgraph.  The same argument in the complement
rules out induced complements of such paths.  QED.

This reduction is structurally useful but not sufficient with standard
quantitative tools.  Known chi-bounds for `P_t`-free graphs combined with
`omega(G)<k` and `alpha(G)<k` lead only to exponential or worse bounds in
`k`, not to `2^{o(k)}`.

There is a sharper reason why this structural information alone cannot prove
Problem 82: random graphs satisfy all these restrictions up to the exponential
Ramsey scale.

**Lemma 20B: Random Obstruction To Hole/Antihole Restrictions.**  Fix
`epsilon>0`.  For all sufficiently large `k`, there exists a graph `G` on

```text
n=floor(2^{(1/2-epsilon)k})
```

vertices such that `alpha(G)<k`, `omega(G)<k`, neither `G` nor its complement
has an induced cycle on at least `k` vertices, and neither `G` nor its
complement has an induced path on at least `k` vertices.

Proof.  Take `G` from `G(n,1/2)`.  The expected number of `k`-cliques plus
`k`-independent sets is at most

```text
2 binom(n,k) 2^{-binom(k,2)}
  <= 2 (en/k)^k 2^{-k(k-1)/2}
  = o(1),
```

because `log_2 n=(1/2-epsilon)k+O(1)`.

For induced cycles, the expected number of induced cycles of length `l` is at
most

```text
binom(n,l) (l-1)!/2 * 2^{-binom(l,2)}
  <= n^l 2^{-l(l-1)/2}.
```

Writing `a_l=n^l 2^{-l(l-1)/2}`, for every `l>=k` we have

```text
a_{l+1}/a_l = n 2^{-l}
             <= 2^{(1/2-epsilon)k-k+O(1)}
             = 2^{-(1/2+epsilon)k+O(1)}.
```

Thus the tail over `l>=k` is dominated by its first term, and

```text
sum_{l>=k} a_l <= 2 a_k
               <= 2^{-\epsilon k^2+O(k)}
               = o(1).
```

The same estimate applies to induced cycles in the complement, by symmetry.
For induced paths, the union bound is even simpler: a fixed ordered `l`-tuple
induces a path with probability at most `2^{-binom(l,2)+O(l)}`, so the same
geometric-tail calculation excludes induced paths of order at least `k` in
both `G` and its complement with probability `1-o(1)`.  With positive
probability all desired properties hold.  QED.

Consequently, no proof can use only the consequences `alpha,omega<k` plus no
long holes, antiholes, paths, or copaths.  Those restrictions still allow
`2^{(1/2-o(1))k}` vertices and chromatic number at least `n/k`.  A structural
proof must use additional information genuinely forced by the absence of
large regular induced subgraphs.

## Lemma 20A: Stronger Induced-Path Exclusion Via Induced Matchings

If `G` has no regular induced subgraph of order at least `k`, then neither
`G` nor its complement contains an induced path on

```text
3 ceil(k/2) - 1
```

vertices.

Proof.  Let `r=ceil(k/2)`.  An induced path on `3r-1` vertices contains the
induced matching

```text
v_1v_2, v_4v_5, ..., v_{3r-2}v_{3r-1}.
```

This matching has `r` edges and therefore induces a `1`-regular graph on
`2r>=k` vertices.  Thus such a path cannot occur in `G`.

If the complement of `G` contains such an induced path, then the same selected
vertices induce a matching in the complement.  In `G` they induce the
complement of a matching, which is regular of degree `2r-2` on `2r>=k`
vertices.  This is again forbidden.  QED.

This improves the constant in Lemma 20, but not the known asymptotic
consequence.  Plugging `t=Theta(k)` into standard `P_t`-free structural
bounds still gives only `k^{O(k)}`-scale restrictions.

## Remark 21: Quantitative Failure Of The Path-Free Route

Lemma 20 puts every counterexample inside the class of graphs whose graph and
complement are `P_{2k-1}`-free.  Standard Gyárfás-type chi-bounds for
`P_t`-free graphs imply bounds of the form

```text
chi(G) <= f(t, omega(G))
```

with `f(t,k)` exponential or worse in `k log t`.  Combining such a theorem
with `omega(G)<k` and `alpha(G)<k` gives only

```text
|V(G)| <= alpha(G) chi(G) <= k f(2k-1,k-1),
```

which is weaker than the elementary Ramsey bound for the present problem.
Thus the path-exclusion route needs a genuinely stronger structural input than
the standard chi-boundedness machinery.

## Lemma 22: Induced Matching and Co-Induced Matching Exclusion

If `G` has no regular induced subgraph of order at least `k`, then neither
`G` nor its complement contains an induced matching of size at least
`ceil(k/2)`.

Proof.  An induced matching of size `r` is a `1`-regular induced subgraph on
`2r` vertices.  If `2r>=k`, this is forbidden.  If the complement of `G`
contains an induced matching of size `r`, then `G` induced on the same `2r`
vertices is the complement of a matching, hence is `(2r-2)`-regular.  This is
again forbidden when `2r>=k`.  QED.

This is another necessary condition on extremal counterexamples.  By itself
it only reproduces exponential Ramsey-type bounds: a large ordinary matching
can be colored by the finite cross-edge pattern between pairs of matched
edges, and a monochromatic submatching yields either an induced matching, a
co-induced matching, or a large homogeneous endpoint set.  The resulting
Ramsey bound is still `2^{O(k)}`, not `2^{o(k)}`.

## Proposition 23: Maximal Induced Matching Cover Bound

Let `a,r,w` be positive integers.  Let `G` be a graph with

```text
alpha(G) < a,
omega(G) <= w,
im(G) < r,
```

where `im(G)` is the maximum size of an induced matching in `G`.  Then

```text
|V(G)| <= (a+2r)(2r)^w.
```

Consequently, using Lemma 22 alone in a counterexample gives only a
`k^{O(k)}` bound on `G(k)`.

Proof.  We prove the slightly stronger recursive bound

```text
B(1) = a-1,
B(w) <= a + 2(r-1) + 2(r-1) B(w-1)   for w>=2,
```

for the maximum possible order under the three displayed hypotheses.  The
case `w=1` is immediate because the graph is independent.

For `w>=2`, take a maximal induced matching `M`.  It has at most `r-1` edges;
let `U` be its set of endpoints, so `|U|<=2(r-1)`.  Let

```text
Z = { v in V(G)\U : N_G(v) cap U = emptyset }.
```

The set `Z` is independent.  Indeed, if two vertices of `Z` were adjacent,
their edge could be added to `M`, since it has no edge to any endpoint in
`U`, contradicting maximality.  Hence `|Z|<a`.

Every vertex outside `U union Z` lies in `N(u)` for some `u in U`.  For each
`u`, the induced graph on `N(u)` has clique number at most `w-1`; it also
inherits `alpha<a` and `im<r`.  Thus each such neighborhood has at most
`B(w-1)` vertices.  Therefore

```text
|V(G)| <= |U| + |Z| + sum_{u in U} |N(u)|
        <= 2(r-1) + (a-1) + 2(r-1) B(w-1),
```

which proves the recurrence.  The displayed closed bound follows by induction
after harmlessly absorbing constants into `(a+2r)(2r)^w`.

For a graph with no regular induced subgraph of order `k`, we have
`alpha(G)<k`, `omega(G)<k`, and by Lemma 22, `im(G)<ceil(k/2)`.  The bound
above is therefore at most `k^{O(k)}`, which is weaker than Ramsey and far
from `2^{o(k)}`.  QED.

This proposition explains why induced matching exclusion is not enough by
itself.  It reduces the graph recursively through neighborhoods, but the
branching factor is still linear in `k` for `k` levels.

## Lemma 24: Deletion-Face Characterization

Let `S` be a vertex set with `|S|>=2`.  Then `G[S]` is regular if and only if
the numbers

```text
e(G[S\{v}]),  v in S,
```

are all equal.

Proof.  For each `v in S`,

```text
deg_{G[S]}(v) = e(G[S]) - e(G[S\{v}]).
```

Thus the degrees in `G[S]` are all equal exactly when the one-vertex-deletion
edge counts are all equal.  QED.

Consequently, if the `(k-1)`-subsets of `V(G)` are colored by their induced
edge count and some `k`-set has all of its `(k-1)`-faces in one color, then
that `k`-set induces a regular graph.  This gives a formally correct
hypergraph-Ramsey proof that `G(k)` is finite, but the bound is enormous and
does not approach `2^{o(k)}`.

The most direct density pigeonhole variant is also too weak.  A family `F` of
`(k-1)`-sets that contains no full boundary of a `k`-set has complement `C`
that covers every `k`-set.  Since each `(k-1)`-set lies in exactly `n-k+1`
`k`-sets, counting incidences gives

```text
|C| (n-k+1) >= binom(n,k),
```

or

```text
|F| <= (1-1/k) binom(n,k-1).
```

Thus a single edge-count level would need density greater than `1-1/k` before
this extremal argument forces a regular `k`-set.  The coloring by edge count
has `O(k^2)` possible colors on `(k-1)`-sets, so plain pigeonhole density is
far below the threshold.  Any successful use of Lemma 24 must exploit special
structure of the edge-count level sets, not just their number.

## New Proof

No complete proof yet.  The current public literature still marks this as an
open problem, so every new route is being treated as provisional until all
gaps are closed.
