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

Even two degree levels can have essentially arbitrary internal graphs, as long
as the cross-degree prescriptions are graphical.

**Lemma: Two-Level Completion Obstruction.**  Let `A` and `B` be disjoint
finite sets, let `X` be a graph on `A`, let `Y` be a graph on `B`, and fix an
integer `c`.  Suppose the integers

```text
r_a = c - deg_X(a)          for a in A,
s_b = c+q - deg_Y(b)        for b in B
```

are nonnegative, satisfy `r_a<=|B|` and `s_b<=|A|`, have equal total sum, and
are bipartite-graphical as degree prescriptions between `A` and `B`.  Then
there is a graph `H` on `A union B` such that `H[A]=X`, `H[B]=Y`, every
vertex of `A` has degree `c`, and every vertex of `B` has degree `c+q`.
In particular, `H` is `q`-modular and has exactly two degree levels modulo
ordinary equality.

Proof.  Add between `A` and `B` a bipartite graph with degrees `r_a` on the
`A` side and `s_b` on the `B` side.  Then each `a in A` has total degree
`deg_X(a)+r_a=c`, and each `b in B` has total degree
`deg_Y(b)+s_b=c+q`.  QED.

This rules out any proof that treats the internal graphs of one or two large
degree levels as constrained by `q`-modularity alone.  The usable structure is
the cross-level trace balance forced by the whole graph.

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

The disconnected case of such a partition theorem can be reduced to connected
components at the cost of residue slots.

**Lemma: Connected Flexible Partitions Suffice For Coarse Lifts.**  Suppose
that every connected `q`-modular graph can be partitioned into at most `B(q)`
induced `2q`-modular subgraphs.  Then every `q`-modular graph can be
partitioned into at most `2q B(q)` induced `2q`-modular subgraphs.

Proof.  Partition each connected component separately into at most `B(q)`
target-modular pieces.  Each piece has a degree residue modulo `2q`.  For each
residue `rho in Z/(2q)Z`, create `B(q)` global slots.  Within a fixed
component, inject its pieces of residue `rho` into the `B(q)` slots for
`rho`.  Finally take, for every global slot, the disjoint union of all pieces
assigned to that slot across all components.  A disjoint union of
`2q`-modular graphs with the same residue is again `2q`-modular, and the
number of slots is `2q B(q)`.  QED.

Consequently, a connected `O(1)`-part theorem gives an `O(q)` flexible
partition theorem, and a connected `polylog(q)`-part theorem gives the
`q polylog(q)` coarse lift allowed above.  The disjoint-union obstructions to
fixed slots do not attack this connected formulation.

For flexible part count, a complement trick removes even this residue-slot
loss.

**Lemma: Complement Reduction For Flexible Lifts.**  Fix moduli `q` and `M`.
If every connected `q`-modular graph has a partition into at most `B` induced
`M`-modular subgraphs, then every `q`-modular graph has such a partition.
Likewise, if every connected `q`-modular graph on `N` vertices contains an
induced `M`-modular subgraph on at least `N/B` vertices, then every
`q`-modular graph has such a witness.

Proof.  The assertions are trivial for connected graphs.  Let `G` be a
disconnected `q`-modular graph on at least two vertices.  Then `complement(G)`
is connected, and its degrees are

```text
|V(G)|-1-deg_G(v),
```

so it is also `q`-modular.  Apply the connected hypothesis to
`complement(G)`.  If `S` is an induced `M`-modular subgraph in the complement,
then `G[S]` is also `M`-modular, since complementing an induced graph changes
every internal degree from `d` to `|S|-1-d`.  The same argument transfers every
part of an `M`-modular partition of `complement(G)` back to an `M`-modular part
of `G`.  The one-vertex case is immediate.  QED.

Thus a connected flexible theorem is equivalent to the corresponding theorem
for all graphs.  This makes the large-witness version the cleanest remaining
target.

## Conditional Proposition: Connected Polylog Witnesses Suffice Strongly

Suppose there are constants `K>=1` and `C` such that, for every dyadic
`q=2^i`, every connected `q`-modular graph `H` contains an induced
`2q`-modular subgraph on at least

```text
|V(H)| / (K (log_2(2q))^C)
```

vertices.  Then there is a constant `c>0` such that, for all sufficiently large
`n`,

```text
F(n) >= 2^{c log_2 n / log_2 log_2 n}.
```

In particular, `F(n)/log n -> infinity`.

Proof.  By the complement reduction, the same large-witness statement holds
for every `q`-modular graph, connected or not.  Put `L=log_2 n`, and choose a
constant `c>0` small enough in terms of `K,C`.  Starting from Gallai's
`2`-modular induced subgraph on at least `n/2` vertices, recursively choose an
induced `q_{i+1}`-modular subgraph of size at least

```text
m_i / (K(i+1)^C),       q_i=2^i.
```

After `t` dyadic steps this gives

```text
m_t >= n / (2 K^t ((t+1)!)^C).
```

Let

```text
T = floor(c L / log_2 L).
```

By Stirling's estimate,

```text
log_2(2 K^T ((T+1)!)^C) = O(T log_2 T) <= L/3
```

for `c` sufficiently small and all large `n`.  Hence

```text
m_T >= 2^{2L/3},
```

while `q_T=2^T=2^{o(L)}`.  The same lower bound, with a smaller denominator,
holds at every earlier index `i<=T`; hence `m_i>q_i+1` throughout this range.
Therefore the process has not yet entered the terminal range `m_i<=q_i+1` by
time `T`.

Let `t>T` be the first index with `m_t<=q_t+1`; such an index exists because
eventually `q_t>n`.  Then Lemma 2 makes the `q_t`-modular graph on `m_t`
vertices regular.  Since `m_{t-1}>q_{t-1}+1`, the last lifting step also gives

```text
m_t >= q_{t-1} / (K(t+1)^C)
    >= 2^T / (K(t+1)^C).
```

Here `t<=L+1` at the first terminal time, because `q_{L+1}>n`.  Thus

```text
m_t >= 2^{cL/log_2 L} / poly(L)
     >= 2^{c' L/log_2 L}
```

for a smaller positive constant `c'`.  This regular induced subgraph has the
claimed order.  QED.

The partition form is a sufficient way to prove the witness hypothesis: if
every connected `q`-modular graph has a `polylog(q)`-part induced
`2q`-modular partition, then one part has the required size, and the
conditional proposition applies.

The polylogarithmic-loss hypothesis is much stronger than necessary.  A
sublinear-in-`q` loss with a logarithmic saving already suffices.

## Conditional Proposition: A Log-Squared Saving In Dyadic Witnesses Suffices

Let `psi(q)` be a function on dyadic integers with

```text
psi(q) = omega((log_2 q)^2).
```

Suppose that, for every dyadic `q>=2`, every connected `q`-modular graph `H`
contains an induced `2q`-modular subgraph on at least

```text
|V(H)| psi(q) / q
```

vertices.  Then `F(n)/log n -> infinity`.

Proof.  By the complement reduction, the same witness statement holds for all
`q`-modular graphs.  Let `G` be an `n`-vertex graph, put `L=log_2 n`, and start
from Gallai's `2`-modular induced subgraph of size at least `n/2`.  Recursively
choose dyadic witnesses, writing `m_i` for the size at modulus `q_i=2^i`.
Thus

```text
m_{i+1} >= m_i psi(q_i)/q_i.
```

Since `psi(q)>=1` for all sufficiently large dyadic `q`, discarding finitely
many initial steps only changes constants.  For all later steps,

```text
m_i >= n / 2^{O(i^2)}.
```

Hence for every fixed small `c>0`, if `i<=c sqrt L`, then `m_i>q_i+1` for all
sufficiently large `n`.  Let `t` be the first index with `m_t<=q_t+1`; such a
`t` exists because eventually `q_t>n`.  The preceding bound gives

```text
t >= c sqrt L.
```

At this first terminal index, Lemma 2 makes the `q_t`-modular graph regular.
Moreover `m_{t-1}>q_{t-1}+1`, so the final witness step gives

```text
m_t >= m_{t-1} psi(q_{t-1})/q_{t-1}
    >= psi(q_{t-1}).
```

Since `log_2 q_{t-1}=t-1=Omega(sqrt L)`, the assumption on `psi` gives

```text
m_t = omega(L) = omega(log_2 n).
```

Thus every sufficiently large `n`-vertex graph has a regular induced subgraph
of order `omega(log n)`.  QED.

This is now the weakest dyadic target in the workspace: prove a connected
large-witness lift with loss `q/omega((log q)^2)`.  A partition theorem with at
most `q/omega((log q)^2)` induced `2q`-modular parts would imply it, but a
direct large-witness proof may be easier.

However, this universal witness hypothesis now looks too strong.  The dense
two-degree model gives the right warning.  Take `N` much larger than `q`, and
consider a random connected graph whose degrees take two values differing by
exactly `q`, with each value appearing on about half of the vertices.  Such a
graph is `q`-modular but typically not `2q`-modular.  For a fixed set `S` of
size

```text
s = N psi(q) / q,
```

the residues of the induced degrees in `G[S]` should behave close to
independent uniform residues modulo `2q` once `psi(q)->infinity`.  The first
moment heuristic for `2q`-modular sets is then

```text
E #{S: |S|=s, G[S] is 2q-modular}
    roughly <= binom(N,s) (2q)^(1-s)
    <= 2q (e/(2 psi(q)))^s,
```

which tends to `0` for every `psi(q)->infinity`.  Thus the natural witness
scale in this random model is `N/q`, not `N omega((log q)^2)/q`.  The
calculation is not yet a rigorous construction because the prescribed-degree
conditioning must be controlled, but it is strong enough to redirect the proof
search: a successful dyadic theorem should be a witness-or-regular dichotomy,
not a universal large-witness theorem.

The corresponding independent-edge anti-concentration estimate is elementary;
the missing part is transferring it to the dense fixed-degree model.

**Lemma: Independent-Edge Modular Anti-Concentration.**  Let `H` be sampled
from `G(k,1/2)`, let `M>=2`, and put

```text
R = C M^2 log M
```

with `C` a sufficiently large absolute constant.  If `k>R+1`, then

```text
P(H is M-modular) <= M ((1+o_M(1))/M)^(k-R-1),
```

where `o_M(1)->0` as `M->infinity`, uniformly in `k`.

Proof.  For `X_h~Bin(h,1/2)` and every residue `r mod M`, the roots-of-unity
filter gives

```text
P(X_h congruent r mod M)
 = 1/M sum_{j=0}^{M-1} zeta^{-rj} ((1+zeta^j)/2)^h,
```

where `zeta` is a primitive `M`th root of unity.  For `j!=0`,

```text
|(1+zeta^j)/2| = |cos(pi j/M)| <= exp(-c min(j,M-j)^2/M^2).
```

Therefore, for all `h>=R`,

```text
max_r P(X_h congruent r mod M) <= (1+o_M(1))/M.
```

Order the vertices as `1,...,k`.  For each `i<=k-R-1`, expose only the edges
from `i` to vertices `i+1,...,k`.  These exposed blocks are independent, and
each block contributes a binomial `Bin(k-i,1/2)` variable to the degree of
vertex `i`.  Fix a candidate common residue `r mod M`.  At the moment the
`i`th block is exposed, all earlier-neighbor contributions to the degree of
`i` are already fixed, so the requirement `deg_H(i) congruent r mod M` imposes
one residue condition on this independent binomial variable.  The preceding
bound applies because `k-i>=R+1`.  Multiplying over
`i=1,...,k-R-1` and summing over the `M` possible common residues proves the
claim.  QED.

In the uniform two-degree model one would need the analogue

```text
P(G[S] is 2q-modular) <= exp(o(|S|)) (2q)^-(|S|-1)
```

for every fixed `S` with `|S|>=q^2 psi(q)`.  A dense switching or local-CLT
argument should replace the independent binomial variables above by
conditional hypergeometric variables with variance `Theta(|S|-i)`.  This is
currently an obstruction lemma to prove, not an established fact.

**Conditional Proposition: Fixed-Degree Anti-Concentration Refutes The
Universal Witness Target.**  Let `psi(q)->infinity` along dyadic `q`, and put

```text
N=q^3,        d_-=(N-q)/2,        d_+=(N+q)/2.
```

Let `G_q` be uniformly sampled from all labelled graphs on a fixed partition
`V=L union H`, `|L|=|H|=N/2`, in which vertices of `L` have degree `d_-` and
vertices of `H` have degree `d_+`.  Suppose that, uniformly for all fixed
sets `S subset V` with

```text
|S| >= N psi(q)/q,
```

one has

```text
P(G_q[S] is 2q-modular) <= exp(o(|S|)) (2q)^-(|S|-1).
```

Then for all sufficiently large dyadic `q` there exists a connected
`q`-modular graph on `N` vertices with no induced `2q`-modular subgraph of
order at least `N psi(q)/q`.

Proof.  Every graph in the model is `q`-modular because its two degree values
differ by exactly `q`.  Let `K=N psi(q)/q`.  By the assumed
anti-concentration and the union bound, the expected number of induced
`2q`-modular sets of order at least `K` is at most

```text
sum_{k>=K} binom(N,k) exp(o(k)) (2q)^-(k-1).
```

For `k>=K`,

```text
binom(N,k) (2q)^-(k-1)
    <= 2q (eN/(2qk))^k
    <= 2q (e/(2psi(q)))^k.
```

Since `psi(q)->infinity`, the displayed sum tends to `0`.  Hence with
positive probability `G_q` has no such large `2q`-modular induced subgraph.
Choose one such graph `G`.

If `G` is connected, we are done.  If `G` is disconnected, then
`complement(G)` is connected.  Complementing preserves `q`-modularity of the
whole graph, since degrees change from `d` to `N-1-d`, and it preserves
target-modularity of every induced set: inside a set `S`, degrees change from
`e_v` to `|S|-1-e_v`, so equality of residues modulo `2q` is unchanged.
Thus `complement(G)` is the desired connected example.  QED.

This proposition explains why the witness-or-regular dichotomy above is the
right replacement target.  The anti-concentration hypothesis is plausible in
the dense fixed-degree model but remains unproved here.

## Conditional Proposition: A Witness-Or-Regular Dyadic Dichotomy Suffices

Let `psi(q)` be an eventually nondecreasing function on dyadic integers and
let `rho(M)` be an eventually nondecreasing function on positive integers such
that

```text
psi(q) = omega((log_2 q)^2),        rho(M) = omega(log_2 M).
```

After replacing them by smaller eventual monotone minorants, assume also that
`1<=psi(q)<=q` and `1<=rho(M)<=M` for all sufficiently large arguments.
Suppose there is an absolute constant `0<a<=1` such that, for every dyadic
`q>=2`, every connected `q`-modular graph `H` on `M>q+1` vertices has at least
one of the following two induced subgraphs:

1. an induced `2q`-modular subgraph on at least

```text
a M psi(q) / q
```

vertices;

2. a regular induced subgraph on at least

```text
a max { rho(M), psi(q) }
```

vertices.

Then `F(n)/log n -> infinity`.

Proof.  By the complement reduction, the same dichotomy holds for all
`q`-modular graphs, not only connected ones: both modularity and regularity of
an induced subgraph transfer through complement.

It is enough to prove that, for every fixed `A>0`, every sufficiently large
`n`-vertex graph has a regular induced subgraph of order at least
`A log_2 n`.  Let `G` be an `n`-vertex graph, write `L=log_2 n`, and put
`q_i=2^i`.  Choose a small fixed `epsilon>0` and set

```text
T = floor(epsilon sqrt L).
```

Start with Gallai's induced `2`-modular subgraph of order at least `n/2`.
Recursively, while the current `q_i`-modular graph `H_i` is not terminal
(`|V(H_i)|>q_i+1`), apply the dichotomy.  If the regular alternative has size
at least `A L`, we are done.  Otherwise the `2q_i`-modular witness alternative
must occur, and we continue with such a witness.  Write `m_i=|V(H_i)|`.

Every witness step loses at most a factor `q_i/(a psi(q_i))`.  Since only
finitely many initial dyadic levels have `psi(q_i)<1`, all witness steps before
time `T` give

```text
m_i >= n / 2^{O(i^2)},
```

with a constant depending only on `a` and the finite initial values of `psi`.
Choose `epsilon` small enough that, for all `i<T`,

```text
m_i >= 2^{gamma L}
```

for some fixed `gamma>0`, whenever the process reaches stage `i` without
already finding a regular induced subgraph of order `A L`.  In particular
`m_i>q_i+1` for all `i<T` and large `n`, so the process cannot become terminal
before time `T`.

If the regular alternative occurs at some `i<T`, then its size is at least
`a rho(m_i)`.  Since `rho` is eventually nondecreasing and
`rho(M)=omega(log M)`, the lower bound `m_i>=2^{gamma L}` gives

```text
a rho(m_i) >= a rho(2^{gamma L}) > A L
```

for all sufficiently large `n`, and we are done.  If the regular alternative
occurs at some nonterminal `i>=T`, then its size is at least
`a psi(q_i)`.  By eventual monotonicity,

```text
a psi(q_i) >= a psi(2^T) = omega(T^2) = omega(L),
```

so this is again larger than `A L` for all sufficiently large `n`.

Let `t` be the first terminal index.  We have `t>=T`.  Since `H_t` is
`q_t`-modular and `m_t<=q_t+1`, Lemma 2 makes `H_t` regular.  Such a `t`
exists by time `L+1`, since `q_{L+1}>n>=m_i`.  If no earlier regular
alternative has already finished the proof, the previous step was
nonterminal, so `m_{t-1}>q_{t-1}+1`, and the forced witness step gives

```text
m_t >= a m_{t-1} psi(q_{t-1}) / q_{t-1}
    > a psi(q_{t-1}).
```

Since `t>=T`, we have `q_{t-1}>=2^{T-1}`, and eventual monotonicity gives

```text
psi(q_{t-1}) >= psi(2^{T-1}) = omega((T-1)^2) = omega(L).
```

Thus the terminal regular graph has order greater than `A L` for all large
`n`.  Consequently every large enough `n`-vertex graph has a regular induced
subgraph of order at least `A log_2 n`.  As `A` was arbitrary, `F(n)/log n ->
infinity`.  QED.

The dense two-degree model is consistent with this dichotomy: it appears to
have no `2q`-modular witness much larger than `N/q`, but its largest regular
induced subgraph should also live near the same `N/q` scale, far above both
`rho(N)` and `psi(q)` when `N` is polynomially larger than `q`.

One way to isolate the direct-regular side of the dichotomy is through
bounded degree spread.

**Lemma: Bounded-Spread Escape For Narrow Modular Hosts.**  Let `Phi(N,s)` be
a function such that every `N`-vertex graph whose degrees lie in an interval
of length at most `s` contains a regular induced subgraph of order at least
`Phi(N,s)`.  If a `q`-modular graph `H` on `N` vertices has all ordinary
degrees in an interval of length at most `s`, then `H` satisfies the direct
regular alternative with lower bound `Phi(N,s)`.

In particular, a two-degree `q`-modular graph with degree values `d` and
`d+q` has a regular induced subgraph of order at least `Phi(N,q)`.

Proof.  This is just the definition of `Phi`, applied to the underlying graph
`H`.  In the two-degree case the degree spread is exactly `q` unless one of
the two levels is empty, in which case `H` is already regular.  QED.

Thus the random two-degree obstruction to the universal witness theorem would
be harmless for the dichotomy if one could prove, for instance,

```text
Phi(N,q) >= N/q^{1+o(1)}
```

or even just `Phi(N,q) >= max{rho(N),psi(q)}` in the parameter range
`N=q^3`, `psi(q)=omega((log q)^2)`.  This bounded-spread problem is far weaker
than the full dichotomy but is a useful local test for the random obstruction
model.

The target should remain scale-sensitive.  An unqualified bound
`Phi(N,s)>=N/poly(s)` would give a linear-size regular induced subgraph for
fixed `s`; dense random graphs with two adjacent prescribed degrees are a
plausible obstruction to such a strong statement.  The terminal-scale form
needed here is much weaker:

```text
Phi(N,q) >= N/q^{1+o(1)}       when q >= N^{1/3+o(1)},
```

or any substitute that beats both `rho(N)` and `psi(q)` in the dyadic
dichotomy.  Small exact and sampled spread-one data do not yet refute even
linear behavior, but the completion lemmas above show that a proof cannot use
degree levels alone.

The connected formulation still cannot demand too few parts.  The first
dyadic lift already has a connected example requiring four flexible parts.

**Example: Connected First-Lift Graph Requiring Four Parts.**  Let `G` have
vertices `0,...,12` and edge set

```text
(0,1) (0,3) (0,9) (0,10)
(1,3) (1,4) (1,7) (1,8) (1,10)
(2,3) (2,4) (2,6) (2,9)
(3,4) (3,6) (3,7) (3,8) (3,9) (3,10) (3,12)
(4,5) (4,7) (4,8) (4,11) (4,12)
(5,7) (5,8) (5,11)
(6,9) (6,11)
(7,8) (7,9) (7,11) (7,12)
(8,9) (8,10) (8,11)
(9,10) (9,11)
(10,12).
```

Its degrees are

```text
(4,6,4,10,8,4,4,8,8,8,6,6,4),
```

so `G` is connected and `2`-modular.  An exact subset enumeration finds only
`258` nonempty vertex sets whose induced degrees are congruent modulo `4`,
and no three pairwise disjoint such sets cover `V(G)`.  Thus `G` has no
partition into at most three induced `4`-modular subgraphs.  It does have a
four-part partition:

```text
{0,2,11,12},      {1,7,9,10},      {3,4,8},      {5,6},
```

with residues respectively `0,2,2,0` modulo `4`.  Hence a connected
first-lift theorem, if true, must allow at least four parts.

Residue flexibility is also essential; even connected first-lift examples
cannot be forced into zero-residue parts.

**Computational Proposition: Connected Zero-Residue First Lift Is False.**
There is a connected even graph on `10` vertices that cannot be partitioned
into four induced subgraphs whose internal degrees are all `0 mod 4`, although
it can be partitioned into three induced `4`-modular subgraphs with flexible
residues.

Proof.  In the edge ordering used by `EXPERIMENTS/regular_induced.py`, take
the mask

```text
22114857535095.
```

The graph has degree sequence

```text
(6,4,6,4,2,4,4,6,2,2),
```

so it is connected and even.  The exact partition checker verifies that the
minimum number of zero-residue modulo-`4` parts is `5`, by

```text
python3 82/EXPERIMENTS/modular_partition.py 10 22114857535095 \
  --modulus 4 --find-min-colors 6 --required-residue 0
```

It also verifies that the flexible minimum is `3`, with one partition having
residues `(1,2,0)`, by

```text
python3 82/EXPERIMENTS/modular_partition.py 10 22114857535095 \
  --modulus 4 --find-min-colors 4 --diagnostics
```

Thus the connected coarse-lift theorem, if true, must use nonzero residues and
cannot be reduced to a zero-residue coloring theorem.  QED.

There is also a compactness-style universal-slot reformulation for fixed part
count.  Fix a source residue `a mod q` and an integer `B`.  If every
`q`-modular graph with source residue `a` has some `B`-part `2q`-modular
partition, then there is a residue multiset `R_{q,a,B}` of size `B` modulo
`2q` that works for every such graph.  Indeed, if every residue multiset
failed on some graph, take the disjoint union of one failure for each
multiset.  Any `B`-part partition of the union would have some residue
signature `R`, but the component chosen to kill `R` could not be partitioned
with that signature.  Thus flexible bounded-part partitioning is equivalent to
proving source-residue-dependent universal slots.

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

The stronger exact endpoint is false even without assuming the host is regular.

**Computational Proposition: Exact `2q` Host Extraction Is False.**  For
`q=4`, there is a `4`-modular graph on `q^2=16` vertices whose largest regular
induced subgraph has order `7<2q`.

Proof.  In the edge ordering used by `EXPERIMENTS/regular_induced.py`, take
the mask

```text
840252375412894364828623063537651415.
```

The graph has `64` edges out of `binom(16,2)=120`, so it lies in the
middle-density range rather than in the sparse or co-sparse easy cases.  Its
degree sequence consists of four vertices of degree `5` and twelve vertices of
degree `9`; hence all degrees are congruent to `1 mod 4` and the whole graph is
`4`-modular with only two ordinary degree levels.

The exact regular-induced-subgraph checker gives

```text
python3 82/EXPERIMENTS/regular_induced.py 16 \
  --mask 840252375412894364828623063537651415 --modulus 4
```

with output

```text
max_regular_order=7
max_4_modular_order=16.
```

Thus one cannot strengthen the terminal host theorem to guarantee a regular
induced subgraph on `2q` vertices.  The viable terminal target remains the
weaker asymptotic demand `omega((log q)^2)`.  QED.

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

By the complement reduction, this obstruction can be made connected.

**Corollary: Connected Three-Part `4 -> 8` Lifts Are False.**  There is a
connected `4`-modular graph that cannot be partitioned into three induced
`8`-modular subgraphs.

Proof.  Let `H` be the disconnected graph from Computational Proposition 4E.4,
the disjoint union of the five listed `10`-vertex graphs.  It is `4`-modular
with source residue `2 mod 4`, and has no three-part induced `8`-modular
partition.  Its complement is connected and is again `4`-modular, with source
residue

```text
49-2 congruent 3 mod 4,
```

because `H` has `50` vertices.  If `complement(H)` had a three-part
`8`-modular partition, complementing each induced part would give a three-part
`8`-modular partition of `H`, contradiction.  QED.

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

The same fast checker also supports the fixed odd-degree source class.  On
`8` vertices, the exact odd-degree sweep leaves exactly nine four-slot
multisets:

```text
(0,0,0,0), (0,0,0,1), (0,0,0,2), (0,0,1,1),
(0,0,1,2), (0,0,2,2), (0,0,2,3), (0,1,1,1),
(0,1,1,2).
```

In particular, the simple slots `(0,0,2,2)` survive both source parities at
the first lift through the exact `n=8` checks.  The odd tree that kills the
clean source-residue slots `(0,1,2,3)` has an even stronger
`(0,0,2,2)` certificate: its vertices split into the two zero-residue parts
`{0,1,3}` and `{2,4,5,6,7}`.

The following exact form isolates what a proof of this candidate must supply.

**Lemma 4I.5B: Two-Cut Form For The Slots `(0,0,2,2)`.**  A graph `G` has a
`4`-modular partition with residue signature contained in `(0,0,2,2)` if and
only if there is a partition

```text
V(G)=X union Y
```

such that `G[X]` has a cut whose two sides both have internal degree
`0 mod 4`, and `G[Y]` has a cut whose two sides both have internal degree
`2 mod 4`.  Empty sides are allowed and impose no degree condition.

Equivalently, for a graph `H` and a target `t in {0,2}`, a cut of `H` into
parts of residue `t`, ignoring any empty side, is the same as a sign vector
`x:V(H)->{+1,-1}` satisfying

```text
x_v sum_{u in N_H(v)} x_u congruent 2t - deg_H(v) mod 8
```

for every vertex `v`.

Proof.  The first statement is just the grouping of the four slots according
to whether their target residue is `0` or `2`: put the two zero-residue parts
inside `X` and the two residue-`2` parts inside `Y`, and conversely split
`X` and `Y` by the two displayed cuts.

For the sign formulation, let `S_x(v)=sum_{u in N_H(v)} x_u`.  The number of
same-side neighbors of `v` is

```text
(deg_H(v) + x_v S_x(v))/2.
```

This number is congruent to `t mod 4` exactly when

```text
deg_H(v) + x_v S_x(v) congruent 2t mod 8,
```

which is the displayed congruence.  QED.

Thus the lower parity bit is not the obstruction: Lemma 4I.6B gives a cut
with even same-side degree in any fixed `X` or `Y`.  The hard step is choosing
`X` so that the upper bit can be made `0` on `X` and `1` on `Y` by the two
sign equations.

A purely local choice of this first split does not work.  Suppose all degrees
of `G` are congruent to `p mod 2`.  One might try to put a vertex `v` into
the residue-`2` side exactly when

```text
(deg_G(v)-p)/2 congruent 1 mod 2.
```

This degree-high-bit rule is false already for the odd star `K_{1,7}`.  Here
`p=1`; the seven leaves have high bit `0`, while the center has high bit `1`.
The center alone cannot be split into residue-`2` parts, since a singleton has
internal degree `0`.  Nevertheless `K_{1,7}` has a `(0,0,2,2)` certificate:
put the center in one zero slot and all leaves in the other zero slot.

The same failure occurs in the even source class.  The graph with edge set

```text
01, 02, 03, 06, 16, 26, 36
```

has degree sequence `4,2,2,2,0,0,4`; the degree-high-bit rule chooses
`Y={1,2,3}`, which is independent and hence cannot be split into
residue-`2` parts.  But the graph has a `(0,0,2,2)` certificate by taking the
triangle `{0,3,6}` as a residue-`2` part and putting
`{1,2,4,5}` into a zero part.  Thus the first split in Lemma 4I.5B must be
chosen using global structure, not just the total degree residues.

Nor does the common first-lift pattern extend naively to higher dyadic
moduli.  At the `4 -> 8` lift, the source-independent slots `(0,0,4,4)` are
already killed by cliques: `K_3` has degree `2 mod 4`, but an `8`-modular
clique part of residue `0` or `4` must have size `1 or 5 mod 8`, so two
zero-residue slots and two residue-`4` slots cannot cover three vertices.
Similarly `K_4` has degree `3 mod 4` and needs four singleton zero-residue
parts.  A complete multipartite check also kills source residue `1` on class
sizes `(3,3,3,3)`.  Thus even if the common `(0,0,2,2)` first-lift theorem is
true, higher dyadic fixed-slot lifts must again depend on the source residue
or use a more flexible family.

A natural attempt to deduce the odd-degree source case from the even case by
complementation is too strong.  If `G` is odd-degree on an even number of
vertices, then `bar G` is even-degree.  A `(0,0,2,2)` partition of `bar G`
whose nonempty parts all have odd size would transform back into a
`(0,0,2,2)` partition of `G`, because complementing a part of odd order sends
an even residue to an even residue.  However such odd-sized certificates need
not exist.

**Example: Odd-Sized Complement Certificates Are Not Forced.**  The even
graph `K_{2,6}` has a `(0,0,2,2)` partition, but no such partition in which
every nonempty part has odd size.

Proof.  The bipartition classes themselves give a two-part zero-residue
certificate for `K_{2,6}`.  Now consider an induced subgraph using `a`
vertices from the side of size `2` and `b` vertices from the side of size
`6`.  If both `a,b` are positive, the two sides have internal degrees `b`
and `a`, so an even-residue modular part requires

```text
a congruent b congruent 0 or 2 mod 4.
```

Such a mixed part has even order.  Hence every odd-order even-residue part is
independent and lies wholly inside one bipartition side; it has residue `0`.
The two residue-`2` slots therefore cannot be used, and the two zero slots
cannot cover both bipartition classes by odd independent sets, since both
classes have even size.  Thus no odd-sized `(0,0,2,2)` certificate exists.
QED.

The compiled checker finds this obstruction with

```text
/tmp/universal_slots_fast --n 8 --degree-parity 0 \
  --candidates 0,0,2,2 --odd-parts
```

as mask `220336191`.

A rooted zero-slot version is also false, so cut-vertex induction cannot use
the same boundary condition as the matching-slot candidate below.

**Example: Rooted Zero Slots Are Not Forced For `(0,0,2,2)`.**  There is an
even graph with a `(0,0,2,2)` partition, but with no such partition placing a
specified vertex in a zero-residue part.

Proof.  Let `G` be the disjoint union of a triangle on vertices `{0,1,6}` and
four isolated vertices, and force vertex `0` into a zero-residue part.  The
graph has a `(0,0,2,2)` partition by putting the whole triangle into one
residue-`2` slot and the isolated vertices into a zero slot.

In any `(0,0,2,2)` partition, a residue-`2` part cannot contain a nonempty
proper subset of the triangle: a singleton has internal degree `0`, and an
edge has internal degree `1` at its endpoints.  A zero-residue part can
contain at most one triangle vertex, because two adjacent triangle vertices
have internal degree `1`, while all three have internal degree `2`.
Therefore, if vertex `0` is placed in a zero slot, the remaining triangle
vertices `1` and `6` cannot both be placed in zero slots and cannot form
residue-`2` parts without `0`.  This contradiction proves the rooted claim.
QED.

The exact checker verifies the obstruction as mask `1057`:

```text
python3 EXPERIMENTS/slot_partition.py 7 --exhaustive-even \
  --slots 0,0,2,2 --force-residue 0:0
```

One tempting simplification of the surviving clean even-source candidate
`R=(0,0,2,2)` is false: the two zero slots cannot be merged into one.

**Example: The Three-Slot `(0,2,2)` Strengthening Is False.**  There is an
even graph with a `(0,0,2,2)` partition but no `(0,2,2)` partition.

Proof.  Let `G` be the graph on vertices `0,...,6` with edge set

```text
03, 06, 12, 16, 26, 36.
```

Equivalently, `G` is two triangles, `036` and `126`, sharing the vertex `6`,
together with two isolated vertices.  Its degree sequence is

```text
2,2,2,2,0,0,4,
```

so it is even.  A `(0,0,2,2)` partition exists, for instance

```text
{0,4,5}, {1,2,6}, {3}, empty,
```

with residues `0,2,0,0` after ordering into the slots.

Now suppose that a `(0,2,2)` partition exists.  In this graph every induced
`2 mod 4` part must have internal degree exactly `2` at each of its vertices.
The only such nonempty induced parts are the two triangles `036` and `126`:
any proper subset of a triangle has a vertex of internal degree `0` or `1`,
and any set meeting both triangles without being exactly one triangle gives
the shared vertex and some leaf unequal internal degrees, or gives a leaf
internal degree other than `2`.  The two available residue-`2` slots therefore
cannot cover both triangles, because they overlap at vertex `6`.  If only one
triangle is placed in a residue-`2` slot, the two non-shared vertices of the
other triangle are adjacent and cannot both lie in the single zero slot, while
a singleton cannot lie in a residue-`2` slot.  This contradiction proves that
no `(0,2,2)` partition exists.  QED.

Computationally, the exact checker first finds this graph as the `n=7` killer
for the three-slot shortcut:

```text
python3 EXPERIMENTS/universal_slots.py 7 --candidates 0,2,2
```

with mask `148580`.  The same mask is accepted by

```text
python3 EXPERIMENTS/slot_partition.py 7 --mask 148580 --slots 0,0,2,2.
```

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

The lower bit of this residual cut equation is never the obstruction.

**Lemma 4I.6B: The Parity Shadow Of The Residual Cut Is Always Solvable.**
Let `H` be any graph.  Then there is a cut `V(H)=A union B` such that every
vertex has even same-side degree.

Proof.  Work over `F_2`.  Let `A_H` be the adjacency matrix of `H`, let
`h=A_H 1` be the degree-parity vector, and encode the cut by
`x_v=0` on one side and `x_v=1` on the other.  The parity of the same-side
degree at `v` is

```text
(A_H x)_v + h_v(1+x_v).
```

Thus the condition that every same-side degree is even is the linear system

```text
(A_H + diag(h)) x = h.
```

Put `L=A_H+diag(h)`.  Since `L` is symmetric, `h` lies in the column space of
`L` if and only if `y dot h=0` for every `y in ker L`.  If `L y=0`, then

```text
0 = y dot L y = sum_v h_v y_v,
```

because the off-diagonal edge terms occur twice and vanish in characteristic
`2`.  Hence `y dot h=0` for every kernel vector, so the system is solvable.
Any solution gives the desired cut.  QED.

Consequently, the hard part of Lemma 4I.6 is the second binary digit of the
same-side degrees after deleting `C` and `D`; it is a quadratic condition on
the chosen parity-solution space.  A purely linear `F_2` proof can at best
solve this lower-bit shadow.

The following stronger formulation was a tempting way to force the residual
cut congruence by literal bipartiteness.

**False Candidate: Modular Odd-Cycle Transversal.**  Every even graph `G` has
disjoint vertex sets `C,D` such that:

1. every vertex of `G[C]` has degree congruent to `1 mod 4`;
2. every vertex of `G[D]` has degree congruent to `2 mod 4`;
3. `G[V(G)\(C union D)]` is bipartite.

If true, this candidate would imply that every even graph has a `4`-modular
partition with residue signature contained in `(0,0,1,2)`.

Proof of implication.  Let `A,B` be a bipartition of the residual graph
`H=G[V(G)\(C union D)]`.  Then `A` and `B` are independent, hence
zero-residue modulo `4`; by hypothesis `C` has residue `1` and `D` has
residue `2`.  Therefore `A,B,C,D` form the required `(0,0,1,2)` slot
partition.  Equivalently, Lemma 4I.6 applies because every residual edge is
across the cut, so

```text
deg_H(v, opposite side) = deg_H(v)
```

for every residual vertex.  QED.

The candidate is stronger than Lemma 4I.6 because it requires the residual
cut congruence to hold by literal bipartiteness.  It is consistent with the
known first-lift hard examples: in the `13`-vertex connected example one
certificate is

```text
A={3,11}, B={0,2,8}, C={4,5,6,9}, D={1,7,10,12},
```

and in the `14`-vertex connected hard mask one certificate is

```text
A={0,13}, B={2,5,6}, C={3,4,7,8}, D={1,9,10,11,12}.
```

The naive proof by greedily deleting chordless odd cycles is insufficient: an
odd cycle itself is a valid residue-`2` set, but cross-edges among several
deleted cycles change the internal degrees inside their union.  Any proof of
the candidate lemma needs an absorption or switching step that controls these
cross-edge contributions.

In fact the candidate is false.

**Computational Counterexample: Modular OCT Is False.**  There is an even
graph on `16` vertices with no modular odd-cycle-transversal certificate.

Proof.  In the edge order used by `EXPERIMENTS/regular_induced.py`, take the
mask

```text
310072714880078432860970147557715681.
```

The exact checker

```text
python3 82/EXPERIMENTS/modular_oct.py 16 \
  --mask 310072714880078432860970147557715681
```

returns `modular_oct=no`.  The graph is even, with degree sequence

```text
6,6,6,6,6,8,8,8,8,8,10,10,10,12,12,12.
```

It is not a counterexample to the `(0,0,1,2)` slot target.  The exact slot
checker gives the partition

```text
A={0,2,6,7,9,11,12,13,15},
B={1,4},
C={3,10},
D={5,8,14},
```

where `A,B` are the two zero-residue parts, `C` has residue `1`, and `D` has
residue `2`.  The residual graph on `A union B` is not required to be
bipartite; instead it satisfies the weaker cut congruence from Lemma 4I.6.
Thus the modular OCT strengthening fails, while the original first-lift slot
target survives.  QED.

**Surviving Candidate: Matching Residue-`1` Slot.**  A different
strengthening of the same first-lift slot target is still consistent with the
current data:

```text
Every even graph has a partition A,B,C,D such that
G[A] and G[B] have all degrees 0 mod 4,
G[C] is exactly 1-regular,
and G[D] has all degrees 2 mod 4.
```

This would imply the `(0,0,1,2)` slot target because an induced matching is
`1`-modular modulo `4`.  It is incomparable with the modular OCT candidate:
it keeps the residue-`1` set very rigid, but it still allows the residual
`A union B` to satisfy only the cut congruence of Lemma 4I.6 rather than being
bipartite.

The exact checker `EXPERIMENTS/slot_partition.py --residue-one-matching` and
the direct coloring checker `EXPERIMENTS/matching_slot_search.py` verify this
candidate for all even graphs on at most `7` vertices, the known connected
first-lift hard masks on `13` and `14` vertices, `K_9`, and the `16`-vertex
modular-OCT counterexample above.  An independent subagent audit also checked
all `2097152` labelled even graphs on `8` vertices; this sweep is reproducible
with `EXPERIMENTS/matching_slot_fast.cpp`.  Larger random exact-cover probes
on even graphs with `14`, `16`, and `18` vertices also found no
counterexample, although dense random
instances can be search-hard and timed out probes are not treated as
evidence.

No proof is known from this candidate yet.  A plausible proof would need to
explain why the residue-`1` corrections can always be chosen as an induced
matching while the remaining residue errors are absorbed by the residue-`2`
set and the residual mod-`4` cut equation.

This matching-slot strengthening should not be expected to iterate literally.
At the next dyadic step `4 -> 8`, source-residue tests show that forcing an
exact `1`-regular residue-`1` slot fails in source residue `1 mod 4` on small
random and multipartite examples.  Thus even if the first-lift matching
candidate is true, the higher-dyadic route needs ordinary source-residue
slots, a more flexible regular alternative, or a different witness-or-regular
dichotomy.

The current computational `4 -> 8` ordinary-slot candidates include the
source-residue family

```text
R_0=(0,1,2,4),   R_1=(0,0,2,2),
R_2=(0,0,1,2),   R_3=(0,0,1,3),
```

where `R_a` is meant for graphs whose total degree residue is `a mod 4`.
This is only finite evidence for a source-residue four-part lift, not a
proof.  It also illustrates why higher dyadic slots must depend on the source
residue and cannot simply reuse `(0,0,1,2)`.  In the complete-multipartite
count model, this four-family passes all source-filtered checks through six
multipartite classes of size at most `16`, using `EXPERIMENTS/multipartite_modular.py`
with `--source-residue`; the same tests without source filtering give
irrelevant counterexamples from other source classes.

The same complete-multipartite fixed-slot model remains consistent one dyadic
level higher.  The helper `EXPERIMENTS/source_slot_finder.py` first filters
slot multisets by the source-residue clique subset-sum test and then checks
the multipartite bin-packing model.  For the `8 -> 16` lift, the following
four-slot source-residue families all pass the complete-multipartite checks
through six multipartite classes of size at most `16`:

```text
R_0=(0,0,0,8),     R_1=(0,0,2,4),
R_2=(0,0,2,6),     R_3=(0,0,3,5),
R_4=(0,4,8,12),    R_5=(0,0,5,5),
R_6=(0,4,6,8),     R_7=(0,0,7,15).
```

This is still only structured finite evidence.  It does not prove a lift for
arbitrary `8`-modular graphs, and some families that pass the five-class
multipartite sweep already fail at six classes, for example source residue
`6` with slots `(0,0,6,7)` on class sizes `(6,6,6,6,6,6)`.  The useful
conclusion is calibration: complete multipartite graphs do not yet obstruct
a four-part source-residue lift at `8 -> 16`, but the fixed slots become more
source-sensitive as the modulus grows.

The displayed choices should not be mistaken for stable conjectural families.
For instance, the source-residue `1` choice `(0,0,2,4)` passes the six-class
check but fails when the class-size vector `(7,7,7,7,7,15,15,15)` is included.
Using the faster legal-bin generator in `EXPERIMENTS/source_slot_finder.py`,
the full eight-class search for source residue `1` leaves three other
four-slot families:

```text
(0,0,1,9),   (0,0,9,10),   (0,1,8,9).
```

The analogous eight-class searches also leave small survivor lists for source
residues `2,3,4,5,6,7`; source residue `0` has many survivors and remains the
broadest complete-multipartite fixed-slot case.  Targeted source-residue `0`
checks through all `88` eight-class vectors show that at least the five
families

```text
(0,0,0,8),   (0,0,8,8),   (0,0,4,8),
(0,0,2,8),   (0,0,8,15)
```

survive this model, so source `0` is not close to being obstructed by these
small complete multipartite tests.  For source residue `3`, the
canonicalized checker completes the eight-class search and leaves exactly the
following twelve four-slot families:

```text
(0,0,3,5),    (0,0,3,6),    (0,0,3,7),
(0,0,3,9),    (0,0,3,10),   (0,0,3,11),
(0,1,3,8),    (0,2,3,8),    (0,3,6,8),
(0,3,7,8),    (0,3,8,10),   (0,3,8,11).
```

Among these data there is a particularly simple pattern.  For the `8 -> 16`
lift, every source residue `a mod 8` passes the complete-multipartite check
through eight classes of size at most `16` with the four slots

```text
R_a = (0, a, 8, a+8)       modulo 16.
```

The analogous family `(0,a,4,a+4)` also passes the `4 -> 8` checks.  In fact
this clean pattern is forced by a simple layer argument for every complete
multipartite graph, without a class-size cap.

**Lemma: Complete Multipartite Clean Source Slots.**  Let `q` be a positive
integer and let `H` be a complete multipartite graph whose class sizes are all
congruent modulo `q`.  Suppose every vertex degree of `H` is congruent to
`a mod q`.  Then `V(H)` can be partitioned into at most three induced
`2q`-modular subgraphs, with residues belonging to

```text
{0, q, a, a+q}   modulo 2q.
```

Proof.  Let the class sizes be `s_1,...,s_t`, and let
`s_i congruent r mod q`.

First suppose `r>0`.  Choose a set `X` containing exactly `r` vertices from
every multipartite class.  If `t=1`, then `H[X]` is independent and has
residue `0`.  If `t>=2`, then all positive class intersections in `X` have
the same size `r`, so `H[X]` is `2q`-modular, and every vertex in `X` has
internal degree

```text
tr-r = (t-1)r  modulo 2q.
```

Modulo `q`, this residue is `(t-1)r`, which is the common degree residue
`a`, because `sum_i s_i - s_j congruent tr-r mod q`.  Hence the residue of
`H[X]` modulo `2q` is either `a` or `a+q`.

After removing `X`, each class has size divisible by `q`.  In each remaining
class write the size as

```text
2q h_i + epsilon_i q,        epsilon_i in {0,1}.
```

Let `Y` contain exactly `epsilon_i q` vertices from class `i`, and let `Z`
contain all remaining vertices.  The set `Y` has either no positive class
intersections, one positive class intersection, or all positive intersections
equal to `q`; therefore `H[Y]` is `2q`-modular with residue `0` or `q`.
Every positive class intersection in `Z` is divisible by `2q`, so `H[Z]` is
`2q`-modular with residue `0`.

If `r=0`, skip the set `X` and apply the same `Y,Z` construction directly to
the original class sizes.  Since in this case every vertex degree of `H` is
`0 mod q`, the allowed residue set is just `{0,q}` with repetitions.  Removing
empty parts in either case gives the required partition.  QED.

This lemma explains why the source-residue family `(0,a,q,a+q)` survives the
complete-multipartite checks and shows that complete multipartite graphs are
not an obstruction to this clean fixed-slot dyadic lift.  It does not prove
the corresponding fixed-slot theorem for arbitrary graphs.

The arbitrary-graph version of this clean pattern is already false at the
first dyadic lift.

**Example: Clean Source Slots Fail For Odd Graphs.**  There is a graph whose
degrees are all `1 mod 2` and whose vertex set cannot be partitioned into
`4`-modular parts with residue signature `(0,1,2,3)`.

Proof.  On vertices `0,...,7`, take the graph with edge set

```text
02, 06, 07, 12, 14, 15, 23.
```

In the edge ordering used by `EXPERIMENTS/regular_induced.py`, its mask is

```text
9954.
```

Its degrees are

```text
3,3,3,1,1,1,1,1,
```

so it has source residue `1 mod 2`.  The exact checker

```text
python3 EXPERIMENTS/slot_partition.py 8 --mask 9954 --slots 0,1,2,3
```

returns `slot_partition=no`.  Thus the clean source-residue slots
`(0,a,q,a+q)` cannot be promoted directly from complete multipartite graphs
to all graphs.  QED.

This counterexample is useful calibration.  Source-residue dependence is
necessary, but not sufficient; arbitrary graph lifts need more flexible slot
families, additional parts, or a witness-or-regular alternative.

A rooted strengthening was the natural route for this false candidate and is
still useful for understanding why the attempt breaks.

Two elementary graph classes satisfy the stronger matching-slot target.

**Lemma: The Matching-Slot Target Holds For Maximum Degree At Most Two.**
Let `G` be an even graph with maximum degree at most `2`.  Then `G` has a
partition `A,B,C,D` such that `A` and `B` have internal degree `0 mod 4`,
`C` is exactly `1`-regular, and `D` has internal degree `2 mod 4`.

Proof.  Such a graph is a disjoint union of isolated vertices and cycles.
Put every odd cycle wholly into `D`; each of its vertices has internal degree
`2`.  The remaining graph is a disjoint union of isolated vertices and even
cycles, hence is bipartite.  Put the two sides of a bipartition into `A` and
`B`, and take `C=empty`.  Then `A` and `B` are independent, and the displayed
partition has the required residues.  QED.

**Lemma: Complete Even Graphs Satisfy The Matching-Slot Target.**  If `K_n`
is even, equivalently `n` is odd, then `K_n` has a matching-slot partition.

Proof.  If `n congruent 1 mod 4`, put all vertices in one zero slot, since
`K_n` has degree `n-1 congruent 0 mod 4`.  If `n congruent 3 mod 4`, put all
vertices in `D`, since `n-1 congruent 2 mod 4`.  QED.

The following rooted form is stronger and is the right object for cut-vertex
induction.

**Rooted Zero-Slot Matching Candidate.**  For every even graph `G` and every
vertex `r`, there is a matching-slot partition `A,B,C,D` in which `r` lies in
one of the zero-residue slots.

Computationally, `EXPERIMENTS/matching_slot_search.py --force-color r:0`
confirms this rooted form for every root in every even graph through
`7` vertices, and for the current hard masks tested above.

This single-root formulation is close to the limit of what can be asked in
this direction.  The naive two-root strengthening is false even for graphs of
maximum degree `2`.

**Example: Two Prescribed Zero Roots Are Impossible.**  Let `G` be the
disjoint union of a triangle on vertices `{0,1,6}` and four isolated
vertices.  Then `G` is even and satisfies the matching-slot target, but no
matching-slot certificate places both `0` and `1` in zero-residue slots.

Proof.  The graph has a certificate by putting the edge `{1,6}` in the
matching slot `C` and putting all remaining vertices, including `0`, in a
zero slot.  This is the certificate found by
`EXPERIMENTS/matching_slot_search.py 7 --mask 1057`.

Suppose instead that both adjacent triangle vertices `0` and `1` lie in
zero-residue slots.  If they lie in the same zero slot, then each has at least
one same-slot neighbor inside the triangle, impossible because a zero slot
requires same-slot degree divisible by `4` and the triangle has maximum
degree `2`.  If they lie in different zero slots, then the third triangle
vertex `6` cannot lie in either zero slot, because it would create same-slot
degree `1` for itself and for one of `0,1`.  It also cannot lie in `C`,
because then it has no same-`C` neighbor, and it cannot lie in `D`, because
then it has same-`D` degree `0` instead of `2 mod 4`.  This contradiction
proves the claim.  QED.

Thus a 2-vertex separator induction cannot simply ask every lobe to put both
boundary vertices into zero slots.  It needs a genuine two-root boundary
signature that records colors and same-color degree contributions at the two
boundary vertices.

**Lemma: Cut-Vertex Reduction From Rooted Zero-Slot Lobes.**  Suppose the
rooted zero-slot matching candidate holds for every even graph with fewer
vertices than a connected even graph `G`.  If `G` has a cut vertex, then `G`
satisfies the unrooted matching-slot target.

Proof.  Let `v` be a cut vertex.  For each component `K` of `G-v`, put
`G_K=G[K union {v}]`.  As in the modular-OCT cut-vertex reduction, `G_K` is
even: every vertex of `K` has its original even degree, and the number of
edges from `v` into `K` is even by summing degrees over `K`.

Apply the rooted zero-slot candidate to each `G_K`, rooted at `v`, and rename
the two zero slots within each lobe so that `v` belongs to the global slot
`A`.  Take the union of all lobe `A`-, `B`-, `C`-, and `D`-sets, identifying
the common vertex `v`.

For every vertex other than `v`, its same-slot neighbors all lie in its own
lobe, so its required condition is unchanged.  For `v`, the same-`A` degree
is the sum of its lobe same-`A` degrees, each of which is `0 mod 4`; hence the
global same-`A` degree is also `0 mod 4`.  The union of the `C`-sets remains
an induced matching because distinct lobes are disjoint and meet only at
`v`, which is in `A`; likewise the union of the `D`-sets remains
`2 mod 4`.  Therefore the global partition is a matching-slot certificate for
`G`.  QED.

Degree-`2` suppression has a more delicate boundary obstruction.

**Lemma: Direct Lifts Across Degree-`2` Suppression.**  Let `G` be an even
graph, let `v` be a degree-`2` vertex with nonadjacent neighbors `x,y`, and
let `G'=G-v+xy`.  Suppose `G'` has a matching-slot certificate.  This
certificate lifts directly to a matching-slot certificate of `G` in each of
the following cases:

1. `x` and `y` both lie in the residue-`2` slot `D`; put `v` in `D`.
2. `x` and `y` lie in different slots and are not split between the two zero
   slots `A` and `B`; put `v` in a zero slot different from both endpoint
   slots.

Proof.  In the first case, the edge `xy` is a same-`D` edge in `G'`.  Removing
it decreases the same-`D` degree of `x` and `y` by `1`, and adding `v` to `D`
adds one same-`D` neighbor back to each.  The new vertex `v` has same-`D`
degree `2`, so the residue-`2` condition is preserved.

In the second case, `xy` is a cross-slot edge in `G'`, so deleting it does not
change any same-slot degree of `x` or `y`.  Since the two endpoint slots are
not exactly `A` and `B`, at least one zero slot is unused by the endpoints.
Putting `v` in such a zero slot gives `v` same-slot degree `0` and does not
change the same-slot degree of either endpoint.  All other vertices are
unchanged.  QED.

The endpoint patterns not covered by this direct lift are `same A`, `same B`,
`same C`, and split `A/B`.  Thus a minimal counterexample with a suppressible
degree-`2` vertex would force an edge-rooted obstruction in the smaller graph
`G'`: every matching-slot certificate of `G'` must place the new edge `xy` in
one of these bad boundary patterns, unless a nonlocal recoloring is used.
This explains why the current reductions do not yet allow us to assume
minimum degree at least `4`; the missing induction object must record
edge-rooted slot and local same-degree signatures, not just unrooted
certificates.

This motivates the following edge-rooted strengthening.

**Edge-Rooted Good-Pattern Matching Candidate.**  For every even graph `G`
and every edge `xy`, there is a matching-slot certificate in which the
endpoints `x,y` are either both in `D`, or are in different slots but not split
between `A` and `B`.

If true, this candidate would make degree-`2` suppression a valid
minimal-counterexample reduction by the previous lemma.  The checker
`EXPERIMENTS/matching_slot_search.py --good-edge 0:1` verifies this
edge-rooted candidate for every even graph on at most `7` vertices with edge
`01` present; by relabelling this is the same as every rooted edge on at most
`7` vertices.  The C++ checker `EXPERIMENTS/matching_slot_fast.cpp` verifies
the same edge-rooted candidate for all `1048576` even labelled graphs on
`8` vertices containing edge `01`.  The checker is now range-chunkable; as a
sanity check, the `n=8` edge-rooted sweep splits into two adjacent free-edge
bit ranges, each checking `524288` edge-containing even graphs with no
counterexample, and the first `n=9` chunk
`0 <= bits < 524288` checks `262144` edge-containing even graphs with no
counterexample.  No proof is currently known.

**Rooted Modular OCT Variant.**  For every even graph `G` and every vertex
`r`, there is a modular odd-cycle-transversal certificate as above in which
`r` lies in the bipartite residual.

This rooted variant, if true below a graph `G`, would give the following
rigorous cut-vertex reduction for the unrooted modular OCT candidate.

**Lemma: Cut-Vertex Reduction From Rooted Lobes.**  Suppose the rooted
candidate holds for every even graph with fewer vertices than `G`.  If `G` is
a connected even graph with a cut vertex, then `G` satisfies the unrooted
modular OCT candidate.

Proof.  Let `v` be a cut vertex.  For each component `K` of `G-v`, let

```text
G_K = G[K union {v}].
```

Every `G_K` is even.  Indeed, all vertices of `K` have in `G_K` the same
degree they have in `G`, hence even.  Also the number of edges from `v` into
`K` is even, because

```text
sum_{x in K} deg_G(x) = 2e(G[K]) + e_G(v,K)
```

has even left-hand side.

Apply the rooted candidate to each `G_K`, rooting at `v`.  Taking the union of
the certificates over all lobes and identifying the common vertex `v` gives a
global certificate: the `C`-parts and `D`-parts have the same internal
residues because different lobes meet only at the residual vertex `v`, and the
residual bipartitions combine by placing every copy of `v` on the same side.
QED.

For the rooted variant itself, the same reduction would require a two-root
or prescribed-independent-set strengthening in the lobe that contains the
global root.  The exact checker finds the one-root strengthening for every
root in all even graphs through `7` vertices and in the current hard masks,
but this multi-root strengthening has not been proved.

In fact, the naive two-root strengthening is false.  Take a triangle and add
isolated vertices, and prescribe two adjacent triangle vertices to be
residual.  The third triangle vertex cannot be placed alone in `C` or `D`,
while placing it residual would leave a triangle in the residual.  Thus a
rooted induction through cut vertices needs a richer rooted signature at the
articulation vertex, not merely a demand that every specified vertex remain
residual.

Some minimal-counterexample reductions are immediate, but they leave the
rooted-gluing issue as the real obstacle.

**Lemma: Basic Reductions For Modular OCT Counterexamples.**  A minimal
counterexample to the modular OCT candidate is connected, has no isolated
vertices, is not a cycle, and is not a complete graph.

Proof.  Disconnected graphs reduce componentwise: an even graph's components
are even, and the union of component certificates is a certificate for the
disjoint union.  Isolated vertices may be left in the bipartite residual, so a
minimal nontrivial counterexample has none.

If `G=C_n` is a cycle, then for even `n` the whole graph is bipartite and may
be the residual, while for odd `n` taking `D=V(G)` works because every vertex
has degree `2`, hence residue `2 mod 4`.

If `G=K_n` is even, then `n` is odd.  For `n=1`, leave the vertex residual.
For `n congruent 3 mod 4`, take `D=V(G)`.  For
`n congruent 1 mod 4` and `n>1`, take `D` to be any `n-2` vertices and leave
the remaining two vertices residual; `K_{n-2}` has degree
`n-3 congruent 2 mod 4`, and two residual vertices induce a bipartite graph.
QED.

The standard next reductions are not currently valid.  If `v` is a cut
vertex, ordinary lobe certificates do not necessarily glue: they must place
`v` in compatible statuses, and if `v` lies in `C` or `D`, the local
same-class degree contributions have to sum to `1` or `2 mod 4` respectively.
This is why the rooted residual version appears naturally.

Degree-`2` suppression has similar edge-rooted defects.  If `v` has
nonadjacent neighbors `x,y`, then `G-v+xy` is even, but a certificate in the
suppressed graph need not lift.  The direct lift fails when `x,y` both lie in
`C`, since replacing the edge `xy` by the path `xvy` changes their `C`-degrees
and gives `v` two `C`-neighbors if placed in `C`.  It can also fail when `x,y`
are residual and the edge `xy` lies on a residual cycle, because subdividing
one edge flips the parity of that cycle.  Thus a minimal counterexample cannot
yet be assumed to have minimum degree at least `4`.

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

There is an elementary easy regime for bounded-spread graphs.

**Lemma 11A: Sparse Or Co-Sparse Bounded-Spread Graphs.**  Let `G` be an
`n`-vertex graph whose degrees lie in an interval of length `s`.  If
`delta(G)<=D`, then `G` has an independent set of order at least

```text
n/(D+s+1).
```

If `delta(complement(G))<=D`, then `G` has a clique of order at least the
same quantity.  In either case `G` contains a regular induced subgraph of
order at least `n/(D+s+1)`.

Proof.  If `delta(G)<=D`, then every degree of `G` is at most `D+s`, so the
greedy/Caro--Wei bound gives

```text
alpha(G) >= n/(D+s+1).
```

An independent set is a regular induced subgraph.  Applying the same argument
to the complement gives the clique statement.  QED.

Thus a putative bound such as `Phi(n,s)>=n/poly(s)` is already true unless
both `G` and its complement have minimum degree larger than a polynomial in
`s`.  The hard bounded-spread regime is therefore medium-density and
near-regular, consistent with the adjacent-degree random samples.

There is also a structural reason why bounded spread alone does not make an
equal-degree class transparent.

**Lemma 11B: Compensated Double Spread-One Template.**  Let `F` be a graph on
`m` vertices `1,...,m` with degrees `d_i`.  Suppose there is a bipartite graph
`X` with left side `A={a_i}` and right side `B={b_i}` such that

```text
deg_X(a_i)=m-1-d_i,
deg_X(b_i)=d_i+epsilon_i,        epsilon_i in {0,1}.
```

Construct a graph `G` on `A union B` by putting a copy of `F` on `A`, a copy
of `complement(F)` on `B`, and the cross graph `X` between `A` and `B`.
Then every vertex in `A` has degree `m-1`, and every vertex `b_i in B` has
degree `m-1+epsilon_i`.  Hence `G` has degree spread at most `1`.

Proof.  In `A`, vertex `a_i` has `d_i` neighbors from `F` and
`m-1-d_i` cross-neighbors in `X`, so its total degree is `m-1`.  In `B`,
vertex `b_i` has `m-1-d_i` neighbors inside `complement(F)` and
`d_i+epsilon_i` cross-neighbors, so its total degree is
`m-1+epsilon_i`.  QED.

This template embeds an arbitrary graph `F` as half of a spread-one graph.
The cross-degree sums impose the calibration

```text
sum_i epsilon_i = sum_i (m-1-d_i) - sum_i d_i
                = m(m-1) - 4e(F).
```

Thus this exact spread-one template is possible only when
`0 <= m(m-1)-4e(F) <= m`, so the base graph has about half of the possible
edges, not quarter density.

Thus a bounded-spread proof cannot simply take a large exact-degree side and
argue from its internal graph alone; the other side can compensate the degree
variation almost arbitrarily.  The remaining hope for bounded spread is a
global argument using both sides or the regular subgraphs created by the
compensating cross graph.

**Computational Example 11C: The Compensated Template Need Not Have A
Half-Size Regular Witness.**  The graph on vertices `0,...,11` with edge set

```text
0-1, 0-2, 0-3, 0-8, 0-9,
1-2, 1-3, 1-6, 1-7,
2-3, 2-6, 2-9,
3-7, 3-8,
4-6, 4-7, 4-8, 4-9, 4-11,
5-6, 5-7, 5-8, 5-9, 5-10,
6-10, 6-11,
7-10, 7-11,
8-10, 8-11,
9-10, 9-11,
10-11
```

has degree sequence

```text
5,5,5,5,5,5,6,6,6,6,6,6
```

and largest regular induced subgraph of order `5`.

This is the mask

```text
72400984189589100935
```

in the edge order used by `EXPERIMENTS/regular_induced.py`.  The verification
commands are

```text
python3 82/EXPERIMENTS/degree_spread.py 12 --mask 72400984189589100935
python3 82/EXPERIMENTS/regular_witness.py 12 --mask 72400984189589100935 --split 6
```

The graph was generated by `EXPERIMENTS/compensated_spread.py` with `m=6`.
Thus even the compensated double spread-one model need not contain a regular
induced subgraph on half its vertices.  Any theorem strong enough for
bounded-spread graphs must allow smaller, profile-absorbed witnesses.

**Lemma 11D: The Compensated Template Inherits Side Witnesses.**  In the
construction of Lemma 11B, if the base graph `F` contains a regular induced
subgraph on `t` vertices, then `G` contains a regular induced subgraph on
`t` vertices.  The same holds if `complement(F)` contains one.

Proof.  The side `A` of `G` induces exactly `F`, and the side `B` induces
exactly `complement(F)`.  Any regular induced subgraph contained wholly in
one side remains an induced regular subgraph of the whole graph, since
external vertices are not included in the induced subgraph.  QED.

Thus the compensated template is not a new lower-bound construction by
itself.  It is a calibration for bounded-spread methods: any proof that uses
only the degree interval must still be able to see regular witnesses either
inside an arbitrary medium-density side or through profile absorption across
the compensating cut.

**Lemma 11E: Profile Equations In The Compensated Template.**  In the setting
of Lemma 11B, let `U` be a set of indices on the `A` side and `V` a set of
indices on the `B` side.  For `i in U`, write

```text
d_U(i)=|N_F(i) cap U|,       x_V(i)=|N_X(a_i) cap {b_j:j in V}|.
```

For `j in V`, write

```text
d_V(j)=|N_F(j) cap V|,       x_U(j)=|N_X({a_i:i in U}, b_j)|.
```

Then the induced subgraph on

```text
{a_i:i in U} union {b_j:j in V}
```

is regular if and only if there is an integer `D` such that

```text
d_U(i)+x_V(i)=D                 for every i in U,
|V|-1-d_V(j)+x_U(j)=D           for every j in V.
```

Proof.  On the `A` side, the internal graph is `F[U]`, so the internal degree
of `a_i` is `d_U(i)`, and its cross-degree into the chosen `B` vertices is
`x_V(i)`.  On the `B` side, the internal graph is `complement(F[V])`, so the
internal degree of `b_j` is `|V|-1-d_V(j)`, and its cross-degree into the
chosen `A` vertices is `x_U(j)`.  Lemma 29 applied to this cut gives exactly
the displayed equations.  QED.

Thus regular witnesses in the compensated template are solutions of a fixed
cut-degree system over the base graph `F` and the compensating bipartite graph
`X`.  The side-inheritance Lemma 11D corresponds to the special cases
`V=empty` or `U=empty`; the examples above show that genuinely mixed
solutions can be larger than the available one-side witnesses.

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

## Lemma 12A: Trace Vectors Are Signed Indicators

In the setting of Lemma 12, fix the last vertex `a_k` as a base and encode
each `b in B` by

```text
v_b = (1_{ba_1}-1_{ba_k}, ..., 1_{ba_{k-1}}-1_{ba_k}).
```

Then every `v_b` is a nonzero vector of one of the two forms

```text
1_S        or        -1_S
```

for a nonempty subset `S subset {1,...,k-1}`.

Proof.  If `b` is nonadjacent to `a_k`, then the coordinates of `v_b` are
`0` or `1`, so `v_b=1_S` for the set of neighbors of `b` inside
`{a_1,...,a_{k-1}}`.  If `b` is adjacent to `a_k`, then the coordinates are
`0` or `-1`, so `v_b=-1_S` for the set of non-neighbors of `b` inside
`{a_1,...,a_{k-1}}`.

The set `S` cannot be empty.  If `v_b=0`, then deleting the single vertex `b`
would subtract the same number of incident edges from every vertex in `A`,
leaving `k` equal-degree vertices in the proper induced subgraph `H-b`.  This
contradicts the minimality assumption in Lemma 12.  QED.

Thus the trace obstruction is narrower than an arbitrary zero-sum-free
sequence in `{-1,0,1}^{k-1}`.  It is a pair of positive set systems whose
nonzero subset-sum sets must be disjoint.  The script
`EXPERIMENTS/trace_multiset_bound.py --trace-cone` restricts the multiset
search to this signed-indicator cone.  This refinement has not yet yielded a
proof; even the restricted subset-sum search grows quickly once `k=6`.

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

The signed-indicator form gives one small but useful sharpening: large trace
obstructions must use genuine cancellation between positive and negative
trace types.

**Lemma 15B: Large Trace-Cone Obstructions Need Mixed-Sign Cancellation.**
In the setting of Lemma 12A, put `d=k-1` and write each outside trace
difference vector as `sigma_b 1_{S_b}`, where
`sigma_b in {+1,-1}` and `emptyset != S_b subset {1,...,d}`.  For each
coordinate `j`, let

```text
p_j = |{b : sigma_b=+1 and j in S_b}|,
n_j = |{b : sigma_b=-1 and j in S_b}|.
```

Then

```text
sum_j |p_j-n_j| <= d^2.
```

Moreover, if

```text
C = sum_j min(p_j,n_j)
```

is the total coordinate-wise cancellation mass, then

```text
|B| <= d^2 + 2C.
```

In particular, if all trace vectors have the same sign, then `|B|<=d^2`.

Proof.  By Lemma 15, the total difference vector

```text
T = sum_{b in B} sigma_b 1_{S_b}
```

has `||T||_infty <= d`; its `j`th coordinate is `p_j-n_j`.  Hence

```text
sum_j |p_j-n_j| <= d * d = d^2.
```

Let

```text
I = sum_b |S_b| = sum_j (p_j+n_j)
```

be the total trace incidence.  Since every `S_b` is nonempty, `|B|<=I`.
For each coordinate,

```text
p_j+n_j = |p_j-n_j| + 2 min(p_j,n_j).
```

Summing over `j` gives

```text
|B| <= I = sum_j |p_j-n_j| + 2C <= d^2 + 2C.
```

If all trace vectors have the same sign, then `C=0`, proving the final claim.
QED.

Thus any superquadratic minimal repeated-degree obstruction is not merely a
large one-sided set system; it must contain many positive and negative traces
that cancel on the same coordinates while still avoiding an exactly balanced
nonempty submultiset.  This identifies the remaining trace problem as a
structured cancellation problem rather than a pure trace-counting problem.

**Corollary 15C: Singleton Trace Differences Are Small.**  In the setting of
Lemma 12A, suppose every outside trace difference vector is supported on a
single coordinate, so each vector is one of `+e_j` or `-e_j`.  Then

```text
|B| <= (k-1)^2.
```

Proof.  Put `d=k-1`.  For a fixed coordinate `j`, the multiset cannot contain
both `+e_j` and `-e_j`, because that pair would have zero sum and deleting the
corresponding two outside vertices would preserve equal degrees on `A`,
contradicting Lemma 12.  Hence for every coordinate at least one of `p_j,n_j`
is zero, so the cancellation mass `C=sum_j min(p_j,n_j)` from Lemma 15B is
zero.  Lemma 15B gives `|B|<=d^2`.  QED.

Thus a minimal repeated-degree host with more than quadratic many outside
vertices must contain trace differences supported on at least two coordinates.
The next hard case is therefore a genuinely mixed-sign hypergraph of trace
supports, not merely many vertices that distinguish one repeated vertex at a
time.

**Lemma 15D: Two-Coordinate Trace Differences Are Alternating-Trail
Obstructions.**  In the setting of Lemma 12A, suppose every outside trace
difference has support of size exactly `2`.  Build a two-colored multigraph
`L` on coordinate set `{1,...,d}` as follows: a vector `+1_{i,j}` is a red
edge `ij`, and a vector `-1_{i,j}` is a blue edge `ij`, retaining
multiplicities.  Then the minimality condition from Lemma 12 is equivalent to
the assertion that `L` has no nonempty closed trail whose edge colors
alternate red, blue, red, blue, ...

Proof.  A nonempty submultiset of trace vectors has sum zero exactly when, in
the corresponding colored submultigraph `L'`, every coordinate is incident
with equally many red and blue selected edges.  If `L` contains an alternating
closed trail, selecting the edges of that trail gives such an `L'`, hence a
balanced deletion, contradicting Lemma 12.

Conversely suppose a nonempty selected submultigraph `L'` has equal red and
blue degree at every vertex.  Take a maximal alternating trail in `L'` with no
repeated edge.  At every internal vertex of the trail, the number of used red
and blue incidences is equal.  At the current terminal vertex, if the last
used edge is red and the trail is not already closed, the used red incidence
count exceeds the used blue incidence count by one.  Since the total red and
blue degrees of this vertex in `L'` are equal, there is an unused blue edge
available to continue the trail.  The same argument with colors interchanged
applies after a blue edge.  Hence a maximal alternating trail can stop only by
closing.  Its closed segment is a nonempty alternating closed trail.  Thus a
balanced deletion exists if and only if an alternating closed trail exists.
QED.

Together with Lemma 15B, this says that any trace obstruction with
two-coordinate supports is a two-colored multigraph with bounded red-blue
degree imbalance and no alternating closed trail.  Proving a subexponential
bound in this colored-graph model would eliminate the first nontrivial support
layer of the trace route.

In fact this colored-graph model is already polynomially bounded.

**Corollary 15E: Pure Two-Coordinate Trace Obstructions Are Polynomial.**  In
the setting of Lemma 12A, suppose every outside trace difference vector has
support of size exactly `2`.  Then, with `d=k-1`,

```text
|B| <= d^2(2d-1)/2 < d^3.
```

Proof.  Use the red/blue multigraph `L` from Lemma 15D.  Let

```text
r_i = red degree of coordinate i,     b_i = blue degree of coordinate i.
```

By Lemma 15, `|r_i-b_i|<=d` for every coordinate `i`.

Build a directed multigraph `D` with vertex set

```text
{(i,R),(i,B): 1<=i<=d}.
```

For each red edge `ij` of `L`, add arcs

```text
(i,R)->(j,B),     (j,R)->(i,B),
```

and for each blue edge `ij`, add arcs

```text
(i,B)->(j,R),     (j,B)->(i,R).
```

A directed cycle in `D` is exactly an alternating closed walk in `L`; deleting
repeated closed subwalks from a shortest such walk gives an alternating
closed trail.  By Lemma 15D no such trail exists, so `D` is acyclic.

The imbalance at the state `(i,R)` is

```text
out_D(i,R)-in_D(i,R) = r_i-b_i,
```

and the imbalance at `(i,B)` is `b_i-r_i`.  Hence every state has imbalance
at most `d` in absolute value.  In any finite acyclic directed multigraph,
the arcs decompose into directed paths from vertices of positive imbalance to
vertices of negative imbalance: repeatedly follow an outgoing arc from a
positive-imbalance vertex until reaching a sink in the remaining acyclic
graph, delete that path, and continue.  Each path has length at most
`|V(D)|-1=2d-1`, and the total number of paths counted with multiplicity is
the total positive imbalance, at most

```text
(1/2) sum_{v in V(D)} |out_D(v)-in_D(v)| <= (1/2)(2d)d=d^2.
```

Therefore

```text
|E(D)| <= (2d-1)d^2.
```

Since each trace vector of support size `2` contributes exactly two arcs to
`D`, we get

```text
|B| = |E(D)|/2 <= d^2(2d-1)/2.
```

QED.

Thus a superpolynomial trace obstruction cannot live entirely in the first
two support layers separately.  It must either use supports of size at least
`3`, or use a genuinely mixed system in which singleton and two-coordinate
traces compensate one another in a way not captured by Corollaries 15C and
15E.

There is also a simple mixed-support case that collapses.

**Corollary 15F: One-Signed Singleton Cover Gives Quadratic Size.**  In the
setting of Lemma 12A, suppose every trace difference has support size at most
`2`.  Suppose further that there is a set `U` of coordinates such that:

1. for every `i in U`, at least one singleton trace `+e_i` occurs;
2. every singleton trace is `+e_i` with `i in U`;
3. every two-coordinate trace has both endpoints in `U`.

Then `|B|<=d^2`, where `d=k-1`.  The same conclusion holds with all singleton
traces `-e_i` instead.

Proof.  Assume the singleton traces are positive; the negative case is
identical after multiplying every trace vector by `-1`.  If a negative
two-coordinate trace `-1_{i,j}` occurred, then by hypothesis the singleton
traces `+e_i` and `+e_j` both occur.  Selecting one copy of each of

```text
e_i,  e_j,  -1_{i,j}
```

would give a zero-sum deletion, contradicting Lemma 12.  Thus every
two-coordinate trace is also positive.  All trace vectors have the same sign,
so Lemma 15B gives `|B|<=d^2`.  QED.

Consequently, any support-at-most-two obstruction larger than quadratic must
either contain singleton traces of both signs, or contain two-coordinate
traces touching a coordinate with no singleton of the relevant global sign.
This matches the small mixed-support searches: the first large examples use
singleton compensators with incompatible signs.

The general support-at-most-two case has the following exact graph model.

**Lemma 15G: Mixed Singleton/Pair Traces Are Half-Edge Alternation
Obstructions.**  In the setting of Lemma 12A, suppose every outside trace
difference has support size at most `2`.  Build a colored multigraph with
half-edges on the coordinate set `{1,...,d}` as follows:

* `+e_i` is a red half-edge incident with `i`;
* `-e_i` is a blue half-edge incident with `i`;
* `+1_{i,j}` is a red ordinary edge `ij`;
* `-1_{i,j}` is a blue ordinary edge `ij`.

Then the minimality condition from Lemma 12 is equivalent to the assertion
that this colored graph has neither

1. an alternating closed trail consisting of ordinary edges, nor
2. an alternating trail whose two end edges are half-edges and whose internal
   edges are ordinary.

Here "alternating" means that consecutive incidences at every coordinate have
opposite colors.

Proof.  A selected submultiset of trace vectors has sum zero exactly when, at
every coordinate, the selected red incidences and blue incidences are equal.
If an alternating closed trail of ordinary edges exists, or if an alternating
trail begins and ends with half-edges, then selecting the vectors represented
by the edges of that trail gives equal red and blue incidence at every
coordinate on the trail and zero incidence elsewhere.  This is a balanced
deletion, forbidden by Lemma 12.

Conversely, suppose a nonempty selected subgraph has equal red and blue
incidence at every coordinate.  If some component has no half-edge, then it
is an ordinary two-colored multigraph with equal red and blue degree at every
vertex; the maximal-trail argument from Lemma 15D gives an alternating closed
trail.  Otherwise take a component containing a half-edge.  Start from a
half-edge and extend an alternating trail through unused selected incidences.
At an internal coordinate, the used red and blue incidences are paired, so if
the trail enters by one color and has not stopped at a half-edge, the equality
of selected red and blue incidences supplies an unused incidence of the other
color.  Since the selected incidence set is finite, the process either reaches
a second half-edge, giving an alternating half-edge-to-half-edge trail, or
repeats a coordinate with the same next required color, giving an alternating
closed trail.  Thus any balanced deletion contains one of the two displayed
objects.  QED.

This lemma is the precise mixed support-`<=2` residue of the trace route.
Corollary 15E bounds the case with no half-edges, and Corollary 15F removes a
one-signed covered half-edge case.  The remaining finite problem is to bound
colored graphs with half-edges, small red-blue degree imbalance at every
coordinate, and no alternating closed or half-edge-to-half-edge trail.

The whole support-`<=2` layer is in fact polynomially bounded by a directed
alternating-trail argument.

**Corollary 15H: Support-At-Most-Two Trace Obstructions Are Cubic.**  In the
setting of Lemma 12A, suppose every outside trace difference vector has
support size at most `2`.  Then, with `d=k-1`,

```text
|B| <= 4d^3       for d>=2.
```

Proof.  Use the colored graph with half-edges from Lemma 15G.  First ignore
the half-edges and build the ordinary alternating digraph `D` on states

```text
(i,R), (i,B),       1<=i<=d.
```

A red ordinary edge `ij` contributes arcs

```text
(i,R)->(j,B),       (j,R)->(i,B),
```

and a blue ordinary edge contributes the same arcs with `R` and `B`
interchanged.  A directed cycle in `D` is an alternating closed walk of
ordinary edges, and a shortest such cycle gives an alternating closed trail.
By Lemma 15G, `D` is acyclic.

For a half-edge `h` of color `C` at coordinate `i`, write

```text
tau(h)=(i,C),       sigma(h)=(i,opposite(C)).
```

Thus an alternating trail that starts with `h` and then uses ordinary edges
corresponds to a directed path in `D` starting at `sigma(h)`, while a trail
ending with `h` corresponds to a path ending at `tau(h)`.

Call a half-edge type exceptional if `D` contains a directed path from
`sigma(h)` to `tau(h)`.  Such a type can occur with multiplicity at most one:
if two copies occurred, the path together with the two copies would be an
alternating trail whose two ends are half-edges, forbidden by Lemma 15G.  Since
there are only `2d` half-edge types, there are at most `2d` exceptional
half-edges.

Delete these exceptional half-edges.  For any two remaining half-edges
`h,h'`, there is no directed path in `D` from `sigma(h)` to `tau(h')`: if
`h != h'` this is exactly a forbidden half-edge-to-half-edge alternating
trail, and if `h=h'` it is the nonexceptional condition.

Now form an augmented digraph `D^+` by adding, for every remaining half-edge
`h`, the arc

```text
tau(h)->sigma(h).
```

The graph `D^+` is acyclic.  Indeed, a directed cycle with no added arc would
be a directed cycle of `D`.  If a directed cycle uses added arcs, then between
two consecutive added arcs on the cycle there is a directed path in `D` from
`sigma(h)` to `tau(h')` for remaining half-edges `h,h'`, which was just
excluded.

Let `Delta_i` be the total red-minus-blue incidence imbalance at coordinate
`i`, including ordinary edges and all half-edges.  Lemma 15 gives
`|Delta_i|<=d`.  In `D^+`, the imbalance `out-in` at `(i,R)` is `Delta_i`
with the contribution of the deleted exceptional half-edges at `i` removed,
and the imbalance at `(i,B)` is its negative.  At each coordinate there are at
most two exceptional half-edge types, each with multiplicity at most one, so
every state of `D^+` has imbalance at most `d+2` in absolute value.

As in Corollary 15E, the arcs of an acyclic directed multigraph decompose into
directed source-sink paths.  Here there are `2d` states, so every path has
length at most `2d-1`, and the number of paths is at most the total positive
imbalance:

```text
(1/2) sum_{x in V(D^+)} |out(x)-in(x)| <= d(d+2).
```

Therefore

```text
|E(D^+)| <= (2d-1)d(d+2).
```

Each ordinary support-two trace contributes two arcs to `D^+`, and each
remaining support-one trace contributes one added arc.  Hence the number of
nonexceptional trace vectors is at most `|E(D^+)|`.  Adding back the at most
`2d` exceptional half-edges gives

```text
|B| <= (2d-1)d(d+2)+2d = 2d^3+3d^2 <= 4d^3
```

for every `d>=2`.  QED.

Therefore any superpolynomial repeated-degree trace obstruction must include
trace vectors whose supports have size at least `3`.  The first genuinely
unresolved trace layer is a signed `3`-uniform-and-larger hypergraph problem,
not a graph or half-edge problem.

One genuinely low-dimensional trace obstruction does collapse.

## Lemma 15A: Rank-One Trace Obstructions Are Small

In the setting of Lemma 12, encode each `b in B` by the difference trace vector

```text
v_b = (1_{ba_1}-1_{ba_k}, ..., 1_{ba_{k-1}}-1_{ba_k})
      in {-1,0,1}^{k-1}.
```

If all nonzero vectors `v_b` lie on one real line, then `|B|<=k-1`.

Proof.  No vector `v_b` is zero: if one were zero, then deleting the single
vertex `b` would subtract the same number of neighbors from every `a_i`,
preserving equal degrees on `A` and contradicting the minimality in Lemma 12.

Since the nonzero `v_b` lie on one line and have coordinates in
`{-1,0,1}`, they are all equal to either `w` or `-w` for a fixed nonzero
`w in {-1,0,1}^{k-1}` with `||w||_infty=1`.  If both signs occur, deleting
one vertex of each sign gives total difference vector zero, so the deleted
pair has equal trace count on every `a_i`, again contradicting Lemma 12.
Hence all `v_b` have the same sign.

The total difference vector `sum_{b in B} v_b` is just the trace-sum imbalance
relative to `a_k`; by Lemma 15 its infinity norm is at most `k-1`.  Since each
summand has the same sign and infinity norm `1`, there are at most `k-1`
summands.  QED.

Thus any large minimal repeated-degree obstruction must have genuinely
high-dimensional trace variation.  One-directional imbalance cannot sustain
the obstruction.

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

## Lemma 16A: Trace Compensation Realizes Minimal Hosts

Let `M` be a multiset of nonzero signed indicators in `Z^{k-1}`, each of the
form `1_S` or `-1_S`, and suppose no nonempty submultiset of `M` sums to zero.
Write

```text
T=sum_{v in M} v.
```

Suppose there is a graph `J` on vertices `a_1,...,a_k`, with degree sequence
`e_1,...,e_k`, such that

```text
e_i-e_k = -T_i       for 1<=i<=k-1.
```

Then there is a graph `H` containing `A={a_1,...,a_k}` such that:

1. the vertices of `A` have equal degree in `H`;
2. the trace-difference multiset of `B=V(H)\A` relative to `a_k` is exactly
   `M`;
3. no nonempty subset of `B` can be deleted while preserving equal degrees on
   all vertices of `A`.

Moreover, `B` may be chosen independent.

Proof.  Start with `J` on `A`.  For each vector `1_S in M`, add a new vertex
`b` that is nonadjacent to `a_k`, adjacent to `a_i` for `i in S`, and
nonadjacent to `a_i` for `i notin S`.  For each vector `-1_S in M`, add a new
vertex `b` that is adjacent to `a_k`, nonadjacent to `a_i` for `i in S`, and
adjacent to `a_i` for `i notin S`.  Put no edges inside the set `B` of new
vertices.

By construction, each new vertex has the prescribed trace difference vector.
If `t_i=|N_H(a_i) cap B|`, then

```text
t_i-t_k = T_i.
```

Therefore

```text
deg_H(a_i)-deg_H(a_k)
  = (e_i-e_k)+(t_i-t_k)
  = -T_i+T_i
  = 0,
```

so all vertices of `A` have equal degree in `H`.

If a nonempty `X subset B` could be deleted while preserving equal degrees on
`A`, then its trace-difference sum would be zero, contradicting the
assumption on `M`.  QED.

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

The same argument improves when the trace vectors span low dimension.

## Lemma 17A: Low-Rank Steinitz Bound For Minimal Trace Obstructions

In the setting of Lemma 12, let `rho` be the real dimension of the span of the
difference trace vectors `v_b` from Lemma 17, and put `d=k-1`.  Then

```text
|B| <= max { rho d, (d+2rho+3)^rho }.
```

Proof.  If `rho=0`, then every `v_b` is zero, contradicting the minimality
condition from Lemma 12 unless `B` is empty.  Assume `rho>=1`.

Choose `rho` coordinate projections on `R^d` whose restriction to the span of
the vectors `v_b` is injective.  This is possible by choosing pivot coordinates
from any rank-`rho` coordinate submatrix.  Let

```text
w_b in Z^rho
```

be the projected vector.  Since the projection is injective on the span, a
nonempty submultiset of the `w_b` sums to zero if and only if the corresponding
submultiset of the `v_b` sums to zero.  By Lemma 12, no such nonempty zero-sum
submultiset exists.

Let

```text
T = sum_{b in B} w_b,       m=|B|.
```

The projected total satisfies `||T||_infty<=d` by Lemma 15, and each `w_b` has
infinity norm at most `1`.  If `m<rho d`, we are done.  Otherwise define

```text
u_b = w_b - T/m.
```

The vectors `u_b` sum to zero and have infinity norm at most
`1+d/m<=1+1/rho`.  By the Steinitz rearrangement lemma in dimension `rho`, the
`u_b` can be ordered so that every centered partial sum `Q_j` has infinity norm
at most

```text
rho(1+d/m) <= rho+1.
```

For the corresponding original projected partial sums

```text
P_j = sum_{i<=j} w_i = Q_j + (j/m)T,
```

each coordinate lies in an interval of length at most

```text
d + 2(rho+1).
```

Thus each coordinate has at most `d+2rho+3` integer values, so the `m+1`
partial sums lie in a box containing at most `(d+2rho+3)^rho` lattice points.
They are all distinct, since two equal partial sums would give a nonempty
zero-sum block.  Therefore

```text
m+1 <= (d+2rho+3)^rho.
```

Combining this with the case `m<rho d` proves the displayed bound.  QED.

This sharpens the message of Lemma 15A: large trace obstructions cannot hide in
a low-dimensional subspace.  Any trace-based proof of the terminal host theorem
must either force low rank from graph structure or exploit genuinely
high-dimensional trace variation.

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

For trace systems that do admit a genuine separator, bounded support gives a
better, but still insufficient, determinant bound.

**Lemma 18A: Conditional Bounded-Support Separator Bound.**  In the setting
of Lemma 12, suppose every trace difference vector `v_b` has support size at
most `s`.  Suppose in addition that the trace multiset admits a strict
separating functional: there is a real vector `x` such that

```text
x dot v_b > 0       for every b in B.
```

Then there is an integer vector `a in Z^d`, `d=k-1`, such that

```text
a dot v_b >= 1       for every b in B,
```

and

```text
||a||_1 <= d s^{d/2}.
```

Consequently,

```text
|B| <= d^2 s^{d/2}.
```

Proof.  Scaling the given separating vector gives a feasible system

```text
v_b dot x >= 1,       b in B.
```

This rational polyhedron is nonempty and is defined by an integer matrix
whose rows have Euclidean norm at most `sqrt s`.  By the standard basic
feasible solution bound for rational linear inequalities, it contains a
rational point whose denominators and numerators are bounded by the largest
absolute determinant of a square submatrix of the coefficient matrix.  By
Hadamard's inequality, every such determinant is at most `s^{d/2}`.  Clearing
denominators gives an integer vector `a` satisfying all inequalities
`a dot v_b>=1` and `||a||_infty<=s^{d/2}`.  Therefore
`||a||_1<=d s^{d/2}`.

Applying Lemma 18 gives `|B|<=d||a||_1<=d^2 s^{d/2}`.  QED.

The separator hypothesis is essential.  Deletion-minimality forbids only
`0/1` submultisets summing to zero, not arbitrary nonnegative integer
dependencies.  For example, in dimension `3` the support-at-most-two family

```text
e_1,   -1_{1,2},   -1_{1,3},   1_{2,3}
```

has no nonempty subfamily summing to zero, but

```text
2e_1 - 1_{1,2} - 1_{1,3} + 1_{2,3} = 0.
```

Hence no strict separator can be positive on all four vectors.  Corollary 15H
uses the alternating half-edge structure precisely to avoid this gap.

For fixed `s>=3` this is only `2^{O(d)}`, not `2^{o(d)}`.  Thus the cubic
support-`<=2` argument uses special graph structure that is absent from the
conditional bounded-support determinant estimate.  The support-`3` trace
layer is the first place where a genuinely new cancellation argument is
needed.

The determinant estimate is not merely wasteful in a superficial way: support
`3` trace systems can force exponentially large separating coefficients.

**Example 18B: Support-Three Separators Can Be Exponential.**  For every
`t>=2`, there is a zero-sum-free signed-indicator multiset in dimension
`d=2t+2`, with every support of size at most `3` and total vector of
infinity norm at most `2`, such that every integer separator
`a` satisfying `a dot v>=1` for all vectors in the multiset has
`||a||_infty >= F_t`, where `F_t` is the Fibonacci sequence with
`F_0=F_1=1`.

Proof.  Use coordinates

```text
p_0,...,p_t, n_0,...,n_t.
```

Take the following trace vectors:

```text
 e_{p_i}                         for 0<=i<=t,
-e_{n_i}                         for 0<=i<=t,
 e_{p_i}+e_{n_{i-1}}+e_{n_{i-2}}  for 2<=i<=t,
-(e_{n_i}+e_{p_i}+e_{p_{i-1}})    for 1<=i<=t.
```

All supports have size at most `3`.  The total vector has every coordinate in
`{-2,-1,0,1}` by direct counting: each interior coordinate appears once as a
singleton and is cancelled by the adjacent triple constraints, with only the
end coordinates missing one adjacent cancellation.

The system is zero-sum-free because it has a strict real separator.  For
example, choose positive numbers `P_i,N_i` recursively by

```text
P_0=P_1=N_0=1,       N_1=P_1+P_0+1,
P_i=N_{i-1}+N_{i-2}+1  for i>=2,
N_i=P_i+P_{i-1}+1      for i>=2,
```

and set

```text
x_{p_i}=P_i,       x_{n_i}=-N_i.
```

Then every displayed trace vector has positive dot product with `x`, so no
nonempty nonnegative integer combination can sum to zero.

Now let `a` be any integer separator with `a dot v>=1` on all displayed
vectors.  The singleton constraints force

```text
a_{p_i}=:P'_i >= 1,        -a_{n_i}=:N'_i >= 1.
```

The triple constraints force, for `i>=2`,

```text
P'_i >= N'_{i-1}+N'_{i-2}+1,
```

and, for `i>=1`,

```text
N'_i >= P'_i+P'_{i-1}+1.
```

In particular `P'_0,P'_1>=1`, and for every `i>=3`,

```text
P'_i >= P'_{i-1}+P'_{i-2}.
```

Thus `P'_t>=F_t`, proving `||a||_infty>=F_t`.  QED.

This example is not claimed to be a full repeated-degree host obstruction:
it records only the trace-cone, zero-sum-free, small-total-imbalance
phenomenon.  Its purpose is to show that Lemma 18 cannot handle the
support-`3` layer by a uniform small-separator theorem.  Any successful trace
argument at support `3` must use additional structure, such as graphical
compensation or multiplicity/degree information from the ambient graph.

The same support-`3` pattern also has an exponential primal form.  Thus even
total imbalance and graphical compensation do not by themselves give a
subexponential trace count.

**Example 18C: Exponential Support-Three Trace Packings.**  For every
`t>=2`, there is a signed-indicator multiset in dimension `d=2t+2`, with every
support of size at most `3`, such that:

1. no nonempty submultiset has sum zero;
2. the total vector has infinity norm `1`;
3. the total vector admits graphical compensation in the sense of Lemma 16;
4. the multiset has at least `F_t` vectors.

Proof.  Use the same vector types and coordinates as Example 18B.  Let
`x_i` be the multiplicity of the singleton `e_{p_i}`, let `y_i` be the
multiplicity of `-e_{n_i}`, let `a_i` be the multiplicity of

```text
e_{p_i}+e_{n_{i-1}}+e_{n_{i-2}}       (2<=i<=t),
```

and let `b_i` be the multiplicity of

```text
-(e_{n_i}+e_{p_i}+e_{p_{i-1}})        (1<=i<=t).
```

Define the triple multiplicities backwards as follows:

```text
a_t=1,       b_t=b_{t-1}=1.
```

For `i=t-1,t-2,...,2`, first set

```text
a_i=b_i+b_{i+1},
```

and then set

```text
b_{i-1}=a_i+a_{i+1}.
```

Then set

```text
x_0=b_1,       x_1=b_1+b_2,       x_i=0 for 2<=i<=t,
y_0=a_2,       y_i=0 for 1<=i<=t.
```

A direct coordinate count gives total `0` on every coordinate except
`n_t`, where the total is `-1`.  Indeed,

```text
p_0: x_0-b_1=0,
p_1: x_1-b_1-b_2=0,
p_i: a_i-b_i-b_{i+1}=0        (2<=i<=t-1),
p_t: a_t-b_t=0,
```

and

```text
n_0: -y_0+a_2=0,
n_i: a_{i+1}+a_{i+2}-b_i=0    (1<=i<=t-2),
n_{t-1}: a_t-b_{t-1}=0,
n_t: -b_t=-1.
```

All selected vector types are among the types in Example 18B, and the strict
separator constructed there is positive on each type.  Therefore every
nonempty submultiset has positive separator dot product and cannot sum to
zero.

The size is exponential.  The sequence `b_i` satisfies, for `1<=i<=t-2`,

```text
b_i=a_{i+1}+a_{i+2}
    =(b_{i+1}+b_{i+2})+a_{i+2}
    >= b_{i+1}+b_{i+2},
```

with `b_{t-1}=b_t=1`.  With the convention `F_0=F_1=1`, this implies
`b_1>=F_t` for every `t>=3`; the case `t=2` has seven vectors and is
immediate.  The total number of vectors is at least `b_1`.

Finally the total vector admits graphical compensation.  In difference
coordinates relative to the base vertex, only one coordinate has total `-1`.
Take the internal degree of the base vertex and all zero-total coordinates to
be `1`, and take the exceptional coordinate's internal degree to be `2`.
This degree sequence is graphical: use a length-two path through the
degree-`2` vertex and pair the remaining degree-`1` vertices by a matching.
Thus Lemma 16 is satisfied, and Lemma 16A realizes the multiset as an actual
minimal repeated-degree host, with `B` independent.  QED.

Consequently, the repeated-degree trace route cannot be completed by proving
a subexponential upper bound for `|B|` from support size, total imbalance, and
graphical compensation alone.  A successful argument must use regular
subgraphs inside the outside trace classes, or some other structure beyond
the trace multiset.

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

## Lemma 25: Degree-Variance Diversity Certificate

Let `G` be a graph on `n` vertices, and fix `h` with `2<=h<=n`.  For
`S subset V(G)`, write `deg_S(v)` for the degree of `v` in `G[S]`, and put

```text
V_h(G) =
sum_{|S|=h} sum_{u<v in S} (deg_S(u)-deg_S(v))^2.
```

For vertices `u,v`, let

```text
sigma(u,v)=|(N(u) triangle N(v)) \ {u,v}|.
```

Then

```text
V_h(G)
= binom(n-4,h-4) sum_{u<v} (deg_G(u)-deg_G(v))^2
  + binom(n-4,h-3) sum_{u<v} sigma(u,v),
```

where `binom(a,b)=0` if `b<0` or `b>a`.

Consequently, if `G` has no regular induced subgraph on `h` vertices, then

```text
(h-1) binom(n,h)
<= binom(n-4,h-4) sum_{u<v} (deg_G(u)-deg_G(v))^2
 + binom(n-4,h-3) sum_{u<v} sigma(u,v).
```

In particular, if the degree spread of `G` is at most `s`, every pair of
vertices has `sigma(u,v)<=D`, and `n>=2h>=8`, then a graph with no regular
induced `h`-set must satisfy

```text
1 <= 16 h^3 s^2 / n^2 + 8 h^2 D / n.
```

Thus `n>8h^{3/2}s` and `n>16h^2D` together force a regular induced subgraph on
`h` vertices.

Proof.  Fix an unordered pair `u,v`, and write

```text
x_w = 1_{uw in E(G)} - 1_{vw in E(G)}
```

for `w notin {u,v}`.  If `S={u,v} union T`, where `|T|=h-2`, then

```text
deg_S(u)-deg_S(v) = sum_{w in T} x_w,
```

since the edge `uv`, if present, contributes equally to both degrees.  Let
`N=n-2` and `r=h-2`.  Summing the square over all such `T` gives

```text
sum_{|T|=r} (sum_{w in T} x_w)^2
= binom(N-2,r-2) (sum_w x_w)^2
  + binom(N-2,r-1) sum_w x_w^2.
```

Here

```text
sum_w x_w = deg_G(u)-deg_G(v),
sum_w x_w^2 = sigma(u,v).
```

Since `N-2=n-4`, this proves the displayed identity after summing over all
pairs `u<v`.

If an `h`-set `S` is not regular, then at least one pair of vertices in `S`
has unequal induced degrees.  For any integers `d_1,...,d_h`,

```text
sum_{i<j} (d_i-d_j)^2
```

is at least `h-1`.  Indeed, choose an integer cut `a` such that at least one
entry is at most `a` and at least one entry is at least `a+1`; if there are
`r` entries on the first side, then the `r(h-r)` cross pairs all differ by at
least `1`, and `r(h-r)>=h-1`.  Therefore every nonregular `h`-set satisfies

```text
sum_{u<v in S} (deg_S(u)-deg_S(v))^2 >= h-1.
```

When no regular `h`-set exists, summing this inequality over all `S` gives
the second display.

For the final estimate, use

```text
sum_{u<v} (deg_G(u)-deg_G(v))^2 <= binom(n,2)s^2,
sum_{u<v} sigma(u,v) <= binom(n,2)D.
```

If `n>=2h>=8`, then

```text
binom(n-4,h-4)/binom(n,h) <= 16h^4/n^4,
binom(n-4,h-3)/binom(n,h) <= 8h^3/n^3.
```

Substitution gives the claimed necessary inequality.  QED.

This identity is a useful diagnostic for low-diversity routes.  A large
counterexample with small degree spread must have many pairs with large
neighborhood symmetric difference.  Thus a bounded-spread proof cannot depend
only on the degree interval; it must also handle graph families with strong
pairwise neighborhood diversity, which is exactly the random-like regime.

**Corollary 25A: Low-Spread Counterexamples Are Neighborhood-Diverse.**  Let
`G` be an `n`-vertex graph with degree spread at most `s`, and suppose `G` has
no regular induced subgraph on `h` vertices.  If `n>=2h>=8` and

```text
n > 8h^{3/2}s,
```

then

```text
(1/binom(n,2)) sum_{u<v} sigma(u,v) >= n/(16h^2).
```

Proof.  Let

```text
bar sigma = binom(n,2)^{-1} sum_{u<v} sigma(u,v).
```

The proof of Lemma 25, with `D` replaced by this average, gives

```text
1 <= 16 h^3 s^2 / n^2 + 8 h^2 bar sigma / n.
```

The assumption `n>8h^{3/2}s` makes the first term less than `1/4`, so the
second term is greater than `1/2`.  Hence `bar sigma >= n/(16h^2)`.  QED.

The average-diversity conclusion in Corollary 25A is, by itself, too weak.
Ordinary homogeneous-set exclusion already forces a stronger lower bound.

## Lemma 26: Homogeneous Exclusion Forces Larger Neighborhood Diversity

Let `G` be an `n`-vertex graph and put

```text
bar sigma = (1/binom(n,2)) sum_{u<v} |(N(u) triangle N(v)) \ {u,v}|.
```

Then `G` contains a clique or independent set of order at least

```text
(n-1)/(4(2 bar sigma + 1)).
```

Consequently, if `G` has no regular induced subgraph on `h` vertices, then

```text
bar sigma >= (n-1)/(8h) - 1/2.
```

Proof.  Choose a vertex `v` whose average `sigma(u,v)` over
`u in V(G)\{v}` is at most `bar sigma`; such a vertex exists because the
average over all ordered pairs is `bar sigma`.  By Markov's inequality, the
set

```text
U={u != v : sigma(u,v) <= 2 bar sigma}
```

has size at least `(n-1)/2`.

Partition `U` into

```text
A=U cap N(v),       B=U \ N(v).
```

One of `A,B` has size at least `(n-1)/4`.  If `|A|` is that large, then for
every `u in A`, the number of nonneighbors of `u` inside `A` is at most
`sigma(u,v)<=2 bar sigma`, because `v` is adjacent to every vertex of `A`.
Thus the complement of `G[A]` has maximum degree at most `2 bar sigma`, so
`G[A]` contains a clique of order at least `|A|/(2 bar sigma+1)`.

If `|B|` is large instead, then for every `u in B`, the number of neighbors of
`u` inside `B` is at most `sigma(u,v)<=2 bar sigma`, because `v` is adjacent
to no vertex of `B`.  Hence `G[B]` has maximum degree at most
`2 bar sigma`, so it contains an independent set of order at least
`|B|/(2 bar sigma+1)`.

In either case there is a clique or independent set of order at least
`(n-1)/(4(2 bar sigma+1))`.  Such a set is regular.  If no regular induced
subgraph on `h` vertices exists, this lower bound is less than `h`, which
rearranges to the displayed inequality.  QED.

Therefore the variance identity cannot settle the problem using only the
average value of `sigma(u,v)`: every counterexample already has
`bar sigma=Omega(n/h)`, whereas Corollary 25A only recovers
`Omega(n/h^2)` under a low-spread hypothesis.  Any successful variance route
must exploit a finer distributional feature of the pair differences or a
stronger way to use low degree spread.

## Lemma 27: Pair-Difference Amplification Template

Let `u,v` be two vertices of a graph `G`, and put

```text
A=N(u)\N(v),       B=N(v)\N(u).
```

Let `delta=1` if `uv in E(G)` and `delta=0` otherwise.  Suppose there are
sets `X subset A` and `Y subset B` with `|X|=|Y|=r` such that:

1. if `delta=1`, then `X` and `Y` are independent and every edge between
   `X` and `Y` is present;
2. if `delta=0`, then `X` and `Y` are cliques and no edge between `X` and
   `Y` is present.

Then `G[{u,v} union X union Y]` is regular on `2r+2` vertices.

Proof.  If `delta=1`, then `u` is adjacent to `v` and to all vertices of
`X`, while `v` is adjacent to `u` and to all vertices of `Y`; both have degree
`r+1` in the displayed set.  A vertex of `X` is adjacent to `u` and to all
`r` vertices of `Y`, and has no neighbors in `X`; it also has degree `r+1`.
The same holds for every vertex of `Y`.

If `delta=0`, then `u` is adjacent exactly to the `r` vertices of `X` and
`v` exactly to the `r` vertices of `Y`.  A vertex of `X` is adjacent to `u`
and to the other `r-1` vertices of the clique `X`, and to no vertex of `Y`;
again it has degree `r`.  The vertices of `Y` are identical.  QED.

This is the local way in which a large symmetric difference can create a
regular induced subgraph.  It also explains why neighborhood diversity alone
does not immediately improve the Ramsey scale: finding the displayed
homogeneous pattern inside `A` and `B` is itself a Ramsey-type problem unless
additional structure is available.

## Lemma 27A: Balanced Pair-Difference Extension

Let `u,v` be two vertices of a graph `G`, put

```text
A=N(u)\N(v),       B=N(v)\N(u),
```

and let `delta=1` if `uv in E(G)` and `delta=0` otherwise.  Suppose there are
sets `X subset A` and `Y subset B` with `|X|=|Y|=r` such that
`G[X union Y]` is `(r-1+delta)`-regular.  Then

```text
G[{u,v} union X union Y]
```

is `(r+delta)`-regular on `2r+2` vertices.

Proof.  The vertices `u` and `v` have degrees `r+delta` in the displayed
induced subgraph: each sees exactly its own one-sided set, and they also see
each other precisely when `delta=1`.  Every vertex of `X` is adjacent to `u`
and not to `v`, and every vertex of `Y` is adjacent to `v` and not to `u`.
Since `G[X union Y]` is `(r-1+delta)`-regular, each vertex of
`X union Y` has total degree

```text
1 + (r-1+delta) = r+delta
```

after `u` and `v` are added.  QED.

Lemma 27 is the homogeneous special case: when `uv` is an edge, an induced
`K_{r,r}` between independent `X,Y` is `r`-regular on `X union Y`; when `uv`
is a nonedge, the disjoint union of two `r`-cliques is `(r-1)`-regular.  Thus
the real pair-difference target is not necessarily a homogeneous bipartite
pattern, but a balanced regular induced subgraph of degree exactly one below
or equal to half its order inside the one-sided difference graph.

**Computational Example 27B: Balanced Pair Extension Can Recover A Missed
Witness.**  On the compensated spread-one graph with `n=20` and mask

```text
869050638646044852707838394808533153088750733938973226828
```

the homogeneous search from Lemma 27 finds only a regular induced subgraph of
order `6`, even though the true maximum regular induced order is `10`.  The
broader Lemma 27A search finds an order-`10` witness.  The relevant pair is
the nonedge `16,19`; with

```text
X={8,10,14,17},       Y={0,2,3,6},
```

the induced graph on `X union Y` is `3`-regular, and adjoining `16,19`
produces a `4`-regular induced graph on

```text
{0,2,3,6,8,10,14,16,17,19}.
```

The verification commands are

```text
python3 82/EXPERIMENTS/pair_difference_template.py 20 --mask 869050638646044852707838394808533153088750733938973226828
python3 82/EXPERIMENTS/balanced_pair_extension.py 20 --mask 869050638646044852707838394808533153088750733938973226828
```

This example shows that the Ramsey bottleneck in Lemma 28 is partly an
artifact of forcing the middle graph to be homogeneous.  However, Lemma 27A
is still not exhaustive: on the `12`-vertex compensated template from
Example 11C, the best balanced pair extension has order `4`, while the true
maximum regular induced order is `5`.  Full profile absorption remains the
larger target.

## Lemma 27C: Pair-Role Profile Extension Criterion

Let `u,v` be two vertices of a graph `G`, and put `delta=1` if
`uv in E(G)` and `delta=0` otherwise.  Partition
`V(G)\{u,v}` into four sets

```text
A=N(u)\N(v),              B=N(v)\N(u),
C=N(u) cap N(v),          E=V(G)\({u,v} union N(u) union N(v)).
```

Choose subsets `X subset A`, `Y subset B`, `Z subset C`, and `W subset E`,
and put `M=X union Y union Z union W`.  Then

```text
G[{u,v} union M]
```

is regular if and only if the following two conditions hold:

1. `|X|=|Y|`;
2. with

```text
D=delta+|X|+|Z|,
```

the degrees inside `G[M]` satisfy

```text
deg_M(x)=D-1       for x in X union Y,
deg_M(z)=D-2       for z in Z,
deg_M(w)=D         for w in W.
```

Proof.  The vertices `u` and `v` have degrees

```text
delta+|X|+|Z|,       delta+|Y|+|Z|,
```

respectively, so they have equal degree exactly when `|X|=|Y|`; their common
degree is then `D`.  A vertex in `X union Y` is adjacent to exactly one of
`u,v`, a vertex in `Z` is adjacent to both, and a vertex in `W` is adjacent to
neither.  Therefore such a vertex has total degree `D` in
`G[{u,v} union M]` exactly when its degree inside `M` is respectively
`D-1`, `D-2`, or `D`.  QED.

Lemma 27A is the special case `Z=W=empty`, where all selected middle vertices
have the same offset from the pair and hence the same required degree inside
`M`.  Lemma 27C is the exact two-pole version of the general split
compensation criterion in Lemma 29.

**Computational Example 27D: The Twelve-Vertex Template Needs A Pair Role.**
For the `12`-vertex compensated template from Example 11C, the maximum
regular witness

```text
{2,3,8,9,11}
```

is captured by Lemma 27C using the edge pair `2,3`.  Relative to this pair,

```text
X={9},       Y={8},       Z=empty,       W={11}.
```

Here `D=2`; inside `M={8,9,11}`, vertices `8` and `9` have middle-degree `1`
and one incident edge to the pair, while vertex `11` has middle-degree `2`
and no incident edge to the pair.  Thus all three middle vertices have total
degree `2`, matching the pair vertices.  The verification command is

```text
python3 82/EXPERIMENTS/pair_role_witness.py 12 --mask 72400984189589100935 --witness 2,3,8,9,11 --pair 2,3
```

## Lemma 28: Ramsey Bound For Pair-Difference Amplification

Let `BR(p,q)` be the least integer `N` such that every bipartite graph with
both parts of size at least `N` contains either a complete `K_{p,p}` or an
empty `K_{q,q}` between the two parts.  Put

```text
r=ceil((h-2)/2),       q=ceil(h/2),
T_h = R(h, BR(r,q)).
```

If `G` has no regular induced subgraph on `h` vertices, then for every pair
`u,v`, with

```text
A=N(u)\N(v),       B=N(v)\N(u),
```

we have

```text
min(|A|,|B|) < T_h.
```

Consequently,

```text
sigma(u,v) < 2T_h + |deg_G(u)-deg_G(v)|.
```

Proof.  Suppose first that `uv` is an edge and that `|A|,|B|>=T_h`.  Since
`G` has no clique of order `h`, Ramsey's theorem gives an independent set
`A_0 subset A` of order `BR(r,q)`.  Similarly `B` contains an independent set
`B_0` of order `BR(r,q)`.

Apply the definition of `BR(r,q)` to the bipartite graph between `A_0` and
`B_0`.  If it contains a complete `K_{r,r}`, then Lemma 27 gives a regular
induced subgraph on `2r+2>=h` vertices.  If it contains an empty `K_{q,q}`,
then the corresponding subsets of `A_0` and `B_0` together form an independent
set of order `2q>=h`, again a regular induced subgraph.  Both alternatives
are impossible.

If `uv` is a nonedge, the same argument is applied with cliques replacing
independent sets.  Since `G` has no independent set of order `h`, each of
`A` and `B` contains a clique of order `BR(r,q)`.  Between these cliques, an
empty `K_{r,r}` gives the nonedge case of Lemma 27, while a complete
`K_{q,q}` gives a clique of order `2q>=h`.  Again both alternatives are
impossible.

Thus `min(|A|,|B|)<T_h` for every pair.  Finally

```text
sigma(u,v)=|A|+|B|,
| |A|-|B| | = |deg_G(u)-deg_G(v)|,
```

because the possible edge `uv` contributes equally to both degrees.  Hence
`sigma(u,v)=2 min(|A|,|B|)+|deg_G(u)-deg_G(v)| < 2T_h+|deg_G(u)-deg_G(v)|`.
QED.

Combining Lemma 28 with Lemma 25 gives a bounded-spread theorem, but only at
the usual Ramsey scale.  If the degree spread is at most `s`, then every pair
has

```text
sigma(u,v) < 2T_h+s.
```

Lemma 25 therefore forces a regular induced `h`-set whenever

```text
n > 8h^{3/2}s
and
n > 16h^2(2T_h+s).
```

Since `T_h` is already exponential or worse in `h`, this does not imply
`G(h)<=2^{o(h)}`.  The value of the lemma is diagnostic: any successful
pair-difference proof must replace the internal Ramsey extraction in `A` and
`B`, or the bipartite Ramsey extraction between them, by a more efficient use
of counterexample structure.

## Conditional Proposition 28A: Balanced Pair-Difference Spread Bound

For `h>=3`, put `r=ceil((h-2)/2)`.  Define `P_h^+` to be the least integer
`M` with the following property: for every graph `H` whose vertex set is the
disjoint union of two marked sets `A,B` of size `M`, either `H` has a regular
induced subgraph on at least `h` vertices, or there are sets `X subset A`,
`Y subset B` with
`|X|=|Y|=r` such that `H[X union Y]` is `r`-regular.

Define `P_h^-` similarly, with "`H[X union Y]` is `(r-1)`-regular" replacing
"`r`-regular", and put

```text
P_h=max(P_h^+,P_h^-).
```

If every graph with degree spread at most `s` and with

```text
n > 8h^{3/2}s,
n > 16h^2(2P_h+s)
```

vertices is considered, then it contains a regular induced subgraph on at
least `h` vertices.

Proof.  Let `G` be an `n`-vertex graph of degree spread at most `s`, and
suppose for contradiction that `G` has no regular induced subgraph on
`h` vertices.

Fix a pair `u,v`, and set

```text
A=N(u)\N(v),       B=N(v)\N(u).
```

If `uv` is an edge and `min(|A|,|B|)>=P_h^+`, choose marked subsets
`A_0 subset A` and `B_0 subset B` of size `P_h^+`.  Applying the definition
of `P_h^+` to `G[A_0 union B_0]`, the first alternative is impossible, so we
obtain `X subset A_0`, `Y subset B_0` of size `r` such that
`G[X union Y]` is `r`-regular.  Lemma 27A then gives a regular induced
subgraph of `G` on `2r+2>=h` vertices, a contradiction.  Hence in the edge
case `min(|A|,|B|)<P_h^+`.

The nonedge case is identical using `P_h^-` and the `(r-1)`-regular middle
graph in Lemma 27A.  Therefore every pair satisfies

```text
min(|A|,|B|)<P_h.
```

Since

```text
sigma(u,v)=|A|+|B|
          =2 min(|A|,|B|)+| |A|-|B| |,
```

and `||A|-|B||=|deg_G(u)-deg_G(v)|<=s`, every pair has

```text
sigma(u,v)<2P_h+s.
```

Lemma 25 now applies with `D=2P_h+s`.  The two displayed lower bounds on `n`
contradict the necessary inequality for a graph with no regular induced
`h`-set.  QED.

Thus a subexponential bound for the balanced pair parameters `P_h^+` and
`P_h^-` would immediately replace the Ramsey quantity `T_h` in bounded-spread
arguments.  This still would not by itself prove the full conjecture, because
one also needs a way to reduce arbitrary counterexamples to a useful
bounded-spread regime; it isolates the exact local improvement required from
the pair-difference route.

## Lemma 29: Split Compensation Criterion

Let `X,Y` be disjoint vertex sets in a graph `G`.  For `x in X` put

```text
i_X(x)=deg_{G[X]}(x),       c_Y(x)=|N(x) cap Y|,
```

and define `i_Y(y),c_X(y)` analogously for `y in Y`.  Then `G[X union Y]` is
regular if and only if there is an integer `D` such that

```text
i_X(x)+c_Y(x)=D       for every x in X,
i_Y(y)+c_X(y)=D       for every y in Y.
```

Equivalently, the cross-degree profile between the two sides exactly
compensates the internal-degree profiles on the two sides.

Proof.  For a vertex `x in X`, its degree in `G[X union Y]` is exactly
`i_X(x)+c_Y(x)`.  For a vertex `y in Y`, it is `i_Y(y)+c_X(y)`.  Thus all
degrees in `G[X union Y]` are equal precisely when the displayed equations
hold for a common value `D`.  QED.

Lemma 27 is the special case in which the internal and cross profiles are
constant on each of the four roles `u,v,X,Y`.  The larger regular witnesses in
the compensated spread-one samples use the full compensation criterion:
neither side is internally regular and the cross graph is not biregular, but
the sums are constant.  This points back toward degree-profile absorption
rather than purely homogeneous pair templates.

## Lemma 30: Profile Absorption Reformulation Across A Cut

Let `V(G)=P union Q` be a fixed partition.  For `X subset P` and `Y subset Q`,
define the profile vectors

```text
alpha_X(x)=deg_{G[X]}(x)      for x in X,
beta_Y(x)=|N(x) cap Y|        for x in X,
gamma_Y(y)=deg_{G[Y]}(y)      for y in Y,
eta_X(y)=|N(y) cap X|         for y in Y.
```

Then `G[X union Y]` is regular if and only if the two finite multisets

```text
{ alpha_X(x)+beta_Y(x) : x in X },
{ gamma_Y(y)+eta_X(y) : y in Y }
```

are both singletons with the same value.

Equivalently, after choosing the internal sets `X` and `Y`, the cross graph
between them must realize prescribed degree lists

```text
beta_Y(x)=D-alpha_X(x),       x in X,
eta_X(y)=D-gamma_Y(y),        y in Y,
```

for some integer `D`.

Proof.  The first statement is Lemma 29 with notation adapted to the ambient
cut `P,Q`.  The second is just a rearrangement of the same equal-degree
equations: once `X` and `Y` are fixed, the internal degrees
`alpha_X,gamma_Y` are fixed, and regularity is exactly the assertion that the
cross degrees into the other side match the displayed residual demands for a
common `D`.  QED.

This reformulation identifies the next nonhomogeneous target.  Pair-template
arguments choose `X,Y` so that the residual demands are constant.  The
compensated spread-one examples show that useful witnesses can have genuinely
varying residual demands, so a proof must either find such demand-realizing
cross subgraphs efficiently or prove that a counterexample has a large
regular witness elsewhere.

## Lemma 31: Profile-Class Pigeonhole In A Split Witness

Let `G[X union Y]` be `D`-regular.  For each `x in X`, record its profile

```text
p(x)=(deg_{G[X]}(x), |N(x) cap Y|),
```

and define profiles on `Y` analogously.  Then every profile lies on the line

```text
a+b=D.
```

Consequently there are at most `D+1` possible profiles on each side.  In
particular, `X` contains a subset of size at least `|X|/(D+1)` all of whose
vertices have the same internal degree into `X` and the same cross-degree into
`Y`; the same holds for `Y`.

Proof.  The equation `a+b=D` is exactly Lemma 29.  Since both entries are
nonnegative integers, there are at most `D+1` possibilities.  The pigeonhole
principle gives the final assertion.  QED.

This is a weak but useful compression of profile absorption.  If a large
regular witness has small degree `D`, then one side contains a large
single-profile class.  The difficulty is that equal total internal degree
into `X` is weaker than regularity inside the profile class itself, so this
does not by itself reduce profile absorption to the pair-template or
trace-class arguments.

**Corollary 31A: Profile Classes In A Counterexample Are Small.**  Let `G`
have no regular induced subgraph on `h` vertices.  Suppose `S=X union Y`
induces a `D`-regular graph.  Then every profile class from Lemma 31 has size
less than `G(h)`.  Consequently,

```text
|X| < (D+1)G(h),       |Y| < (D+1)G(h).
```

Applying the same assertion in the complement gives the stronger pair of
bounds with `D` replaced by

```text
min(D, |S|-1-D).
```

Proof.  Any profile class is itself a vertex set in `G`; if it had at least
`G(h)` vertices, the definition of `G(h)` applied to the induced graph on
that class would give a regular induced subgraph on at least `h` vertices in
`G`, a contradiction.  Lemma 31 gives at most `D+1` profile classes on each
side, so the displayed bounds follow.

The complement of `G[S]` is `(|S|-1-D)`-regular.  Regular induced subgraphs
are preserved by complementation, and the profile-class argument applies to
the same cut in the complement.  Taking the better of the graph and complement
bounds gives the final statement.  QED.

This corollary is circular if used with the unknown function `G(h)`, but it is
a useful structural warning.  A profile-absorption proof that hopes to improve
`G(h)` must exploit medium-degree witnesses or use information beyond the
existence of repeated profile classes; low-degree and co-low-degree witnesses
quickly collapse back to the original problem inside one profile class.

## New Proof

No complete proof yet.  The current public literature still marks this as an
open problem, so every new route is being treated as provisional until all
gaps are closed.
