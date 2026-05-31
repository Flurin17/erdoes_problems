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

## Lemma 2: Modular Terminal Criterion

Let `q` be a positive integer and let `S` be a vertex set with `|S| <= q`.  If
all degrees in `G[S]` are congruent modulo `q`, then `G[S]` is regular.

Proof.  Every degree in `G[S]` lies in the interval `[0, |S|-1]`, whose length
is at most `q-1`.  Two integers in this interval that are congruent modulo `q`
are equal.  Hence all induced degrees are equal.  QED.

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
|B| <= (4(k-1)^2+1)^{k-1}.
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

Use the standard Steinitz rearrangement lemma in this form: if vectors in
`R^d` have infinity norm at most `R` and sum `0`, then they can be ordered so
that every partial sum has infinity norm at most `dR`.  Apply it to the
zero-sum sequence consisting of the `m` vectors `v_b` and the single vector
`-T`.  All these vectors have infinity norm at most `d`, so there is a cyclic
ordering whose partial sums have infinity norm at most `d^2`.  Rotate this
cyclic order so that `-T` is last.  The partial sums of the preceding `m`
original trace vectors then all have infinity norm at most `2d^2`.

If two of these `m+1` partial sums were equal, the consecutive block between
them would be a nonempty submultiset of the `v_b` with sum `0`, contradicting
Lemma 12.  Hence the `m+1` partial sums are distinct lattice points in the box

```text
[-2d^2,2d^2]^d.
```

This box contains `(4d^2+1)^d` lattice points, so

```text
m+1 <= (4d^2+1)^d.
```

The displayed bound follows after replacing `d` by `k-1`.  QED.

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
S(r) = (4(r-1)^2+1)^{r-1}.
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
