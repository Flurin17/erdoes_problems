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

**Corollary 0B.1: Split Graphs Are Linearly Easy.**  If `G` is a split graph
on `n` vertices, then

```text
reg(G) >= n/2.
```

Proof.  Let `V(G)=A union B` be a split partition with `A` a clique and `B`
an independent set.  The larger of `A` and `B` has order at least `n/2`, and
it induces a regular subgraph.  QED.

Thus Lemma 0B should be read only as a warning that mixed regular witnesses
need not exist in split graphs.  Split graphs themselves are far from the
hard regime because their defining partition already supplies a linear
homogeneous, hence regular, induced subgraph.

## Lemma 0B.2: Complete Multipartite Graphs Are Logarithmically Easy

Let `G` be a complete multipartite graph on `n>=1` vertices.  Then `G`
contains a regular induced subgraph on at least

```text
n/H_n
```

vertices, where `H_n=1+1/2+...+1/n`.  The same conclusion holds for the
complement of a complete multipartite graph, that is, for a disjoint union of
cliques.

Proof.  Let the multipartite class sizes be `s_1,...,s_m`.  For an integer
`t>=1`, put

```text
a_t = |{i : s_i >= t}|.
```

If `a_t>0`, choose exactly `t` vertices from each class with size at least
`t`.  The induced graph is complete `a_t`-partite with all parts of size
`t`, hence it is regular of degree `(a_t-1)t` and has order `t a_t`.

Let

```text
M=max_{t>=1} t a_t.
```

Since `a_t=0` for `t>n`,

```text
n=sum_i s_i = sum_{t>=1} a_t <= sum_{t=1}^n M/t = M H_n.
```

Thus some `t` gives a regular induced subgraph of order `M>=n/H_n`.

For a disjoint union of cliques, apply the same argument to the clique sizes:
choosing exactly `t` vertices from every clique of size at least `t` gives a
disjoint union of equal `t`-cliques, which is `(t-1)`-regular.  QED.

This is much stronger than the conjectured `omega(log n)` lower bound on this
model class.  It also explains why the complete multipartite obstructions
appearing in the modular-partition route are obstructions to particular
dyadic lift statements, not to the existence of large regular induced
subgraphs themselves.

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

## Proposition 0D: A Self-Contained Random Lower Construction

There is an absolute constant `c>0` such that

```text
G(k) > c k^{5/4}
```

for all sufficiently large `k`.

Equivalently, for infinitely many `n`,

```text
F(n) <= C n^{4/5}.
```

This is much weaker than the Bollobas--AKS--Dyson--McKay constructions above,
but it is a completely local reconstruction showing why polynomial-size bad
graphs are easy to obtain.

Proof.  Let `N` be chosen later and take `G` from `G(N,1/2)`.  Fix a set
`T` of `t` vertices, where `t>=k`, and split it as

```text
T=A union B,       |A|=floor(t/2),       |B|=ceil(t/2).
```

Condition on all edges inside `A`.  For each `a in A`, the number

```text
X_a=deg(a,B)
```

is an independent `Bin(|B|,1/2)` random variable.  If `G[T]` is regular, then
the quantities

```text
deg_{G[A]}(a)+X_a,        a in A,
```

are all equal.  Thus, for any fixed internal degrees
`c_a=deg_{G[A]}(a)`, regularity forces the independent variables `X_a+c_a`
to be all equal.

Let

```text
p_b=max_j Pr[Bin(b,1/2)=j],        b=|B|.
```

For arbitrary integer offsets `c_a`,

```text
Pr[X_a+c_a is constant over A]
 <= p_b^{|A|-1},
```

because after singling out one vertex of `A` and summing over the common
value, every other factor is at most `p_b`.  The elementary central-binomial
bound gives `p_b <= 3/sqrt(t)` for all `t>=2`, since `b>=t/2`.  Since
`|A|-1>=t/2-2`, for all sufficiently large `t`,

```text
Pr[G[T] is regular] <= (3/sqrt(t))^{t/2-2}.
```

The expected number of regular induced subgraphs of order exactly `t` is at
most

```text
binom(N,t) (3/sqrt(t))^{t/2-2}
 <= (t/9) (e sqrt(3) N / t^{5/4})^t.
```

Choose

```text
N <= (20 e sqrt(3))^{-1} k^{5/4}.
```

Then for every `t>=k`,

```text
e sqrt(3) N / t^{5/4} <= 1/20,
```

and the expected number of regular induced subgraphs of order at least `k` is
at most

```text
sum_{t=k}^N (t/9) 20^{-t} < 1
```

for all sufficiently large `k`.  Hence some `N`-vertex graph has no regular
induced subgraph on at least `k` vertices, proving `G(k)>N`.  This gives the
claimed polynomial lower bound after adjusting the absolute constant.  QED.

The same elementary conditioning argument gives the usual homogeneous-random
scale up to an arbitrarily small power loss.

**Proposition 0E: A Self-Contained `G(n,1/2)` Lower Bound.**  For every
`epsilon>0` there is a constant `c_epsilon>0` such that, for all sufficiently
large `k`,

```text
G(k) > c_epsilon k^{3/2-epsilon}.
```

Equivalently, the homogeneous random graph construction gives
`F(n) <= n^{2/3+o(1)}` along an unbounded sequence of `n`.

Proof.  It is enough to consider `0<epsilon<1/4`; larger values follow by
decreasing `epsilon`.  Put `delta=epsilon`, and let `G` be sampled from
`G(N,1/2)`.

Fix a `t`-vertex set `T`, with `t>=k`, and split it as

```text
T=A union B,       |B|=ceil(delta t),       |A|=t-|B|.
```

Condition on all edges of `G[T]` except the edges between `A` and `B`.  For
each `a in A`, write

```text
X_a=deg(a,B).
```

The random variables `X_a`, `a in A`, are independent
`Bin(|B|,1/2)` variables.  After the conditioning, the rest of the degree of
`a` in `T` is a fixed integer `c_a`.  If `G[T]` is regular, then the shifted
variables

```text
X_a+c_a,        a in A,
```

are all equal.  If

```text
p_b=max_j Pr[Bin(b,1/2)=j],        b=|B|,
```

then, for arbitrary integer offsets `c_a`,

```text
Pr[X_a+c_a is constant over A] <= p_b^{|A|-1}.
```

Indeed, sum over the value taken by one distinguished shifted variable; each
other shifted variable has every point mass at most `p_b`.

The central-binomial bound gives

```text
p_b <= 3/sqrt(b) <= (3/sqrt(delta)) t^{-1/2}.
```

For all sufficiently large `t`, because `|B|=ceil(delta t)` and
`delta<1/4`,

```text
|A|-1 >= (1-2delta)t.
```

Therefore, with `C_delta=3/sqrt(delta)`,

```text
Pr[G[T] is regular] <= (C_delta t^{-1/2})^{(1-2delta)t}.
```

The expected number of regular induced subgraphs of order exactly `t` is at
most

```text
binom(N,t) (C_delta t^{-1/2})^{(1-2delta)t}
 <= ( e C_delta N / t^{3/2-delta} )^t,
```

after increasing `C_delta` harmlessly to absorb the exponent
`1-2delta`.  Choose

```text
N <= (2eC_delta)^{-1} k^{3/2-delta}.
```

Since `t>=k`, the last displayed expectation is at most `2^{-t}`.  Summing
over all `t>=k` gives total expectation less than `1` for large `k`.
Therefore some graph on `N` vertices has no regular induced subgraph of order
at least `k`, proving

```text
G(k)>N >= c_epsilon k^{3/2-epsilon}
```

after adjusting constants and returning to `delta=epsilon`.  QED.

Optimizing the split parameter slowly with `k` gives a more explicit
logarithmic loss.

**Proposition 0F: A Log-Loss Homogeneous Random Lower Bound.**  There is an
absolute constant `c>0` such that, for all sufficiently large `k`,

```text
G(k) > c k^{3/2} / sqrt(log k).
```

Proof.  Let `L=log k`, and take `G` from `G(N,1/2)`.  For every fixed
`t`-vertex set `T`, with `k<=t<=N`, split

```text
T=A union B,       |B|=ceil(t/L),       |A|=t-|B|.
```

Condition on all edges of `G[T]` except the cross edges between `A` and `B`.
As in Proposition 0E, regularity of `G[T]` forces the independent binomial
variables

```text
X_a=deg(a,B),        a in A,
```

after fixed integer shifts, to all take one common value.  Hence, writing
`b=|B|` and `p_b=max_j Pr[Bin(b,1/2)=j]`,

```text
Pr[G[T] is regular] <= p_b^{|A|-1}.
```

The central-binomial bound gives

```text
p_b <= 3/sqrt(b) <= 3 sqrt(L/t).
```

For large `k`, `|A|-1 >= (1-2/L)t`.  Put

```text
q_t=3 sqrt(L/t).
```

Since `t<=N`, and we will choose `N<=k^{3/2}`, we have
`log t <= 2 log k=2L` for large `k`.  Therefore

```text
q_t^{-2/L}
 = exp((2/L) log(1/q_t))
 <= exp((1/L) log t) <= e^2
```

after increasing the final constant harmlessly.  Thus

```text
Pr[G[T] is regular]
 <= q_t^{(1-2/L)t}
 <= (3e^2 sqrt(L/t))^t.
```

The expected number of regular induced subgraphs of order exactly `t` is
therefore at most

```text
binom(N,t) (3e^2 sqrt(L/t))^t
 <= (3e^3 N sqrt(L) / t^{3/2})^t.
```

Choose

```text
N <= (6e^3)^{-1} k^{3/2}/sqrt(L).
```

Then for every `t>=k` the last expectation is at most `2^{-t}`.  Summing over
`t>=k` gives total expectation less than `1` for all large `k`.  Hence some
`N`-vertex graph has no regular induced subgraph on at least `k` vertices,
and the displayed lower bound for `G(k)` follows.  QED.

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

## Lemma 3A: GF(2)-Nullity Gives A Large Even Witness

Let `A_G` be the adjacency matrix of an `n`-vertex graph `G` over `F_2`, and
let

```text
nu = dim ker A_G.
```

Then `G` contains an induced subgraph on at least `nu` vertices in which every
degree is even.

Proof.  Let `K=ker A_G`.  Choose `nu` coordinate positions on which the
projection `K -> F_2^nu` is an isomorphism.  This is possible by taking pivot
coordinates from a row-reduced basis of `K`.  Therefore there is a vector
`x in K` whose projection to these coordinates is the all-one vector.  Its
support `S` has size at least `nu`.

Since `A_G x=0`, every vertex of `G`, and in particular every vertex of `S`,
has an even number of neighbors in `S`.  Thus `G[S]` has all degrees even.
QED.

This is weaker than Gallai's theorem unless the nullity is large, but it gives
a useful linear-algebra diagnostic for parity-based constructions: low
`F_2`-rank forces a large `2`-modular witness before any Gallai partitioning is
used.

## Lemma 3B: Binary Eigenspaces Give Parity-Modular Witnesses

Let `A_G` be the adjacency matrix of an `n`-vertex graph `G` over `F_2`.  For
`lambda in F_2`, put

```text
nu_lambda = dim ker(A_G + lambda I).
```

Then `G` contains an induced subgraph on at least `nu_lambda` vertices in
which every degree is congruent to `lambda modulo 2`.

Proof.  Let `K=ker(A_G+lambda I)`.  As in Lemma 3A, choose `nu_lambda`
coordinate positions on which projection from `K` is an isomorphism, and take
`x in K` whose projection to these coordinates is the all-one vector.  Let

```text
S={v : x_v=1}.
```

Then `|S|>=nu_lambda`.  For every `v in S`, the `v`-coordinate of
`A_G x = lambda x` gives

```text
deg_{G[S]}(v) congruent lambda mod 2,
```

because over `F_2` the indicator vector of `S` is exactly `x`.  Hence `G[S]`
has the claimed parity-modular source residue.  QED.

Lemma 3A is the case `lambda=0`.  The `lambda=1` case is useful for diagnostics
because it gives a large odd induced subgraph whenever `A_G+I` has large
kernel.  Thus a graph that avoids large parity-modular witnesses from linear
algebra must have both binary eigenspaces small, even though Gallai still
always supplies a large even witness by a nonlinear partition argument.

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

## Lemma 4A.2: Low-Chromatic Graphs Are Dyadic-Partition Easy

Let `M` be any positive integer.  Every graph `G` can be partitioned into
`chi(G)` induced `M`-modular subgraphs.  It can also be partitioned into
`chi(complement(G))` induced `M`-modular subgraphs.

Consequently, for any proposed dyadic partition theorem of the form

```text
every q-modular graph partitions into at most b(q) induced 2q-modular graphs,
```

a counterexample must satisfy

```text
chi(G)>b(q)       and       chi(complement(G))>b(q).
```

Proof.  A proper coloring of `G` partitions `V(G)` into independent sets, and
each independent set is `0`-regular, hence `M`-modular.  A proper coloring of
`complement(G)` partitions `V(G)` into cliques in `G`; each clique is regular,
hence also `M`-modular.  Taking `M=2q` proves the final assertion.  QED.

Thus the dyadic partition route has the same qualitative hard core as the
original Ramsey problem: low chromatic number or low clique-cover number is
already handled.  Any obstruction to a sublinear-exponent or polylog-saving
dyadic partition theorem must be simultaneously high-chromatic and
high-cochromatic, in addition to satisfying the modular source condition.

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

The same idea has a sharper bipartite form that matches the two-degree
completion model more closely.

**Lemma: Bipartite Cross-Edge Modular Anti-Concentration.**  Let `X,Y` be
disjoint vertex sets of sizes `a,b`.  Fix arbitrary graphs on `X` and on
`Y`, and then choose all cross edges between `X` and `Y` independently with
probability `1/2`.  Let `M>=2`, and put

```text
R = C M^2 log M
```

with `C` sufficiently large.  If `b>=R`, then the probability that all
vertices of `X` have the same degree modulo `M` in the resulting graph on
`X union Y` is at most

```text
((1+o_M(1))/M)^(a-1),
```

uniformly in `a,b` and in the fixed internal graph on `X`.  Consequently, if
`a,b>=R`, the probability that the whole graph on `X union Y` is
`M`-modular is at most

```text
((1+o_M(1))/M)^(max(a,b)-1).
```

Proof.  For each `x in X`, write

```text
D_x = c_x + Z_x,
```

where `c_x` is the fixed degree of `x` inside `X`, and
`Z_x~Bin(b,1/2)` is its random cross-degree into `Y`.  The variables
`Z_x`, `x in X`, are independent.  The roots-of-unity estimate used in the
previous lemma gives

```text
max_r P(D_x congruent r mod M) <= (1+o_M(1))/M
```

for every `x`, uniformly in the shift `c_x`, because `b>=R`.

Pick one vertex `x_0 in X`.  The event that all `D_x` have one common residue
is

```text
union_r {D_x congruent r mod M for every x in X}.
```

Using independence and summing over the residue of `D_{x_0}`,

```text
P(D_x all equal mod M)
 = sum_r P(D_{x_0}=r mod M) prod_{x != x_0} P(D_x=r mod M)
 <= ((1+o_M(1))/M)^(a-1).
```

This proves the first assertion.  If `a,b>=R`, apply the first assertion to
the larger of the two sides, using the other side as the random target.  The
event that the whole graph is `M`-modular implies, in particular, that all
degrees on that larger side are equal modulo `M`.  QED.

This lemma is the unconditioned version of the fixed-degree
anti-concentration estimate needed above.  The remaining obstacle is that the
uniform two-degree model conditions the same cross-edge variables on many row
and column sum constraints; a successful switching or local-CLT transfer would
need to show that the displayed residue anti-concentration survives that
conditioning on every fixed large test set.

**Corollary: Semi-Random Two-Block First-Moment Bound.**  In the setting of
the bipartite cross-edge lemma, suppose now that `|X|=|Y|=N`, while the
internal graphs on `X` and `Y` are still arbitrary and fixed.  Let `Z_{x,y}`
be the number of induced `M`-modular sets `S` with

```text
|S cap X|=x,        |S cap Y|=y.
```

If `x,y>=R=C M^2 log M`, then

```text
E Z_{x,y}
 <= binom(N,x) binom(N,y)
    ((1+o_M(1))/M)^(max(x,y)-1).
```

Proof.  Fix subsets `X_0 subset X`, `Y_0 subset Y` of sizes `x,y`.  The
induced graph on `X_0 union Y_0` is generated by fixed internal graphs and
independent random cross edges.  By the bipartite lemma, the probability that
this fixed set is `M`-modular is at most

```text
((1+o_M(1))/M)^(max(x,y)-1),
```

because both sides of the fixed set have size at least `R`.  Summing over the
`binom(N,x)binom(N,y)` choices of `X_0,Y_0` gives the displayed expectation.
QED.

**Corollary: Semi-Random Balanced Witnesses Above The `N/sqrt(M)` Scale.**
In the same semi-random two-block model, fix `A>e`.  Let

```text
T >= max { R, A N / sqrt(M) }.
```

Then the expected number of `M`-modular induced sets `S` satisfying

```text
|S cap X| >= T,        |S cap Y| >= T
```

is at most

```text
N^2 M rho_M^T,
```

where `rho_M=(1+o_M(1)) e^2/A^2`.  In particular, for fixed `A>e` and
`M` sufficiently large, `rho_M<1`; if also `T/log(NM)->infinity`, then with
probability tending to `1` there is no such balanced `M`-modular induced set.

Proof.  Put `c_M>=1`, `c_M=1+o_M(1)`, for the factor in the previous
corollary.  For fixed `x,y>=T`, let `L=max(x,y)`.  The standard binomial
estimate gives

```text
binom(N,x)binom(N,y) <= (eN/T)^(x+y) <= (eN/T)^(2L).
```

Therefore

```text
E Z_{x,y}
 <= (eN/T)^(2L) (c_M/M)^(L-1)
 <= M (c_M e^2 N^2/(T^2 M))^L.
```

Since `T>=A N/sqrt(M)`, the parenthesized factor is at most

```text
rho_M = c_M e^2/A^2.
```

Summing over at most `N^2` choices of the pair `(x,y)` and using `L>=T`
gives the displayed bound.  The final statement follows from Markov's
inequality.  QED.

For balanced choices `x~y`, this first moment has exponent roughly

```text
x log(eN/x)+y log(eN/y)-x log M.
```

Thus the row/column residue information alone does not yet recover the full
independent-edge heuristic when `N/x` is comparable to `M`; it saves one
power of `M` per vertex on only one side.  The corollary makes the loss
quantitative: this one-sided first moment rules out balanced witnesses only
above the `N/sqrt(M)` scale.  This identifies a precise technical bottleneck
for the two-degree anti-concentration route: one must extract additional
independent constraints from the opposite side, or prove that fixed-degree
conditioning creates enough effective randomness to recover the expected
`(2q)^-(|S|-1)` scale.

In the uniform two-degree model one would need the analogue

```text
P(G[S] is 2q-modular) <= exp(o(|S|)) (2q)^-(|S|-1)
```

for every fixed `S` with `|S|>=q^2 psi(q)`.  A dense switching or local-CLT
argument should replace the independent binomial variables above by
conditional hypergeometric variables with variance `Theta(|S|-i)`.  This is
currently an obstruction lemma to prove, not an established fact.

The helper `EXPERIMENTS/hypergeom_residue.py` calibrates this first
conditioning layer.  It computes the residue distribution of a hypergeometric
cross-degree after fixing one row sum.

**Lemma: Exact Hypergeometric Residue Fourier Formula.**  Let
`X` have the hypergeometric distribution obtained by drawing `d` elements
from an `N`-element population with `K` marked elements.  Let `M>=2`, and let
`zeta=exp(2 pi i/M)`.  Then for every residue `r mod M`,

```text
P(X congruent r mod M)
 = 1/M sum_{j=0}^{M-1} zeta^{-rj}
   [u^d](1+zeta^j u)^K(1+u)^{N-K} / binom(N,d).
```

Consequently, if

```text
B = max_{1<=j<M}
    |[u^d](1+zeta^j u)^K(1+u)^{N-K}| / binom(N,d),
```

then every residue class has probability at most

```text
(1+(M-1)B)/M
```

and total variation distance from uniform is at most `(M-1)B/2`.

Proof.  The probability generating function of `X` is

```text
E w^X = sum_x binom(K,x)binom(N-K,d-x) w^x / binom(N,d)
      = [u^d](1+wu)^K(1+u)^{N-K} / binom(N,d).
```

The roots-of-unity filter gives

```text
1_{X congruent r mod M}
 = 1/M sum_{j=0}^{M-1} zeta^{j(X-r)}.
```

Taking expectations and substituting the generating function proves the
displayed formula.  The `j=0` term is exactly `1/M`; bounding all nonzero
Fourier terms in absolute value by `B` gives the pointwise upper bound.  For
total variation, write each residue probability as `1/M+e_r`.  The same
Fourier bound gives `sum_r |e_r| <= M(M-1)B/M=(M-1)B`, and total variation is
half of this sum.  QED.

Thus the one-row fixed-degree problem is reduced to bounding explicit
Krawtchouk-type coefficients.  The script reports the maximum nontrivial
Fourier bias `B` after computing the residue distribution directly.

**Lemma: Central Hypergeometric Residue Mixing.**  Let `X` have the
hypergeometric distribution obtained by drawing `m` elements from a
`2m`-element population with exactly `m` marked elements.  Let `M>=2`, and
let `zeta=exp(2 pi i/M)`.  For every `1<=j<M`,

```text
|E zeta^{jX}|
 <= 2 sqrt(m) ((1+|cos(pi j/M)|)/2)^m.
```

Consequently, for an absolute constant `C`, if

```text
m >= C M^2 log M,
```

then

```text
max_r P(X congruent r mod M) <= (1+o_M(1))/M.
```

Proof.  Pair each marked element with one unmarked element.  For a selected
`m`-set, let `Y` be the number of pairs from which exactly one element is
selected.  Conditional on the pair-state pattern, the choices inside these
`Y` split pairs are independent fair choices between marked and unmarked
elements.  The unsplit pairs contribute a deterministic phase to
`zeta^{jX}`, while each split pair contributes a factor with absolute value

```text
|(1+zeta^j)/2| = |cos(pi j/M)|.
```

Writing `t=|cos(pi j/M)|`, we get

```text
|E zeta^{jX}| <= E t^Y.
```

The probability generating function for `Y` is

```text
E t^Y = [x^m](1+2tx+x^2)^m / binom(2m,m),
```

because one pair contributes weight `1`, `2tx`, or `x^2` according as zero,
one, or two of its elements are selected.  Evaluating the numerator
polynomial at `x=1` gives

```text
[x^m](1+2tx+x^2)^m <= (2+2t)^m.
```

Using the elementary central-binomial lower bound

```text
binom(2m,m) >= 4^m/(2 sqrt(m))
```

gives the displayed Fourier estimate.

For the residue bound, the roots-of-unity formula gives

```text
P(X congruent r mod M)
 <= 1/M (1 + sum_{j=1}^{M-1} |E zeta^{jX}|).
```

Put `ell=min(j,M-j)`.  Since

```text
(1+|cos(pi j/M)|)/2 = cos^2(pi ell/(2M))
```

and `cos u <= exp(-2u^2/pi^2)` for `0<=u<=pi/2`, the Fourier estimate is at
most

```text
2 sqrt(m) exp(-m ell^2/M^2).
```

Summing over `j` gives

```text
sum_{j=1}^{M-1} |E zeta^{jX}|
 <= 4 sqrt(m) sum_{ell>=1} exp(-m ell^2/M^2).
```

If `m>=C M^2 log M` with `C` large enough, the last expression is `o_M(1)`.
Substitution into the roots-of-unity bound proves the claim.  QED.

**Lemma: General Hypergeometric Residue Mixing From Paired Mass.**  Let
`X` have the hypergeometric distribution obtained by drawing `d` elements
from an `N`-element population with `K` marked elements, where
`0<d<N`.  Put

```text
p=d/N,        L=min(K,N-K).
```

Let `M>=2`, let `zeta=exp(2 pi i/M)`, and put

```text
Lambda = L p(1-p).
```

There is an absolute constant `C_0` such that, for every `1<=j<M`,

```text
|E zeta^{jX}|
 <= C_0 sqrt(Np(1-p))
    exp(-2(1-|cos(pi j/M)|) Lambda).
```

Consequently, for every `A>0` there is a constant `C_A` such that if

```text
Lambda >= C_A M^2 log(NM),
```

then

```text
max_r P(X congruent r mod M) <= (1+(NM)^(-A))/M.
```

Proof.  Pair `L` marked elements with `L` unmarked elements.  The remaining
`N-2L` unpaired elements, if any, all have the same mark status.  For
`1<=j<M`, write `t=|cos(pi j/M)|`, so `|1+zeta^j|=2t`.

The probability generating numerator for `E zeta^{jX}` is

```text
[x^d](1+(1+zeta^j)x+zeta^j x^2)^L Q(x),
```

where `Q(x)` is either `(1+x)^(N-2L)` or `(1+zeta^j x)^(N-2L)`,
according to whether the unpaired elements are unmarked or marked.  Taking
absolute values coefficientwise gives

```text
|E zeta^{jX}|
 <= [x^d](1+2tx+x^2)^L(1+x)^(N-2L) / binom(N,d).
```

Set `x_0=p/(1-p)`.  Since all coefficients in the numerator are nonnegative,

```text
[x^d](1+2tx+x^2)^L(1+x)^(N-2L)
 <= x_0^(-d)(1+2tx_0+x_0^2)^L(1+x_0)^(N-2L).
```

The elementary Stirling lower bound for the binomial point probability gives

```text
binom(N,d) >= c x_0^(-d)(1+x_0)^N / sqrt(Np(1-p))
```

with an absolute `c>0`.  Hence

```text
|E zeta^{jX}|
 <= C_0 sqrt(Np(1-p))
    ((1+2tx_0+x_0^2)/(1+x_0)^2)^L.
```

Using `x_0/(1+x_0)^2=p(1-p)`, the last ratio is

```text
1 - 2(1-t)p(1-p).
```

This is at most `exp(-2(1-t)p(1-p))`, proving the Fourier estimate.

For the residue bound, let `ell=min(j,M-j)`.  Since

```text
1-|cos(pi j/M)| >= c ell^2/M^2
```

for an absolute `c>0`, the Fourier estimate gives

```text
sum_{j=1}^{M-1} |E zeta^{jX}|
 <= C_0 sqrt(Np(1-p))
    2 sum_{ell>=1} exp(-c Lambda ell^2/M^2).
```

If `Lambda>=C_A M^2 log(NM)` with `C_A` large enough, this sum is at most
`(NM)^(-A)`.  The roots-of-unity formula then gives the displayed pointwise
residue bound.  QED.

**Corollary: Configuration Prefix Rows Have Hypergeometric Residues.**  In
the bipartite configuration model, suppose a row of degree `d` is matched
uniformly to `d` currently unmatched column stubs among `N_*` total remaining
column stubs, of which `K_*` belong to a fixed marked set of columns.  Let
`X` be the number of matched stubs landing in the marked columns.  Put

```text
p=d/N_*,        Lambda=min(K_*,N_*-K_*) p(1-p).
```

If `Lambda>=C_A M^2 log(N_*M)`, then

```text
max_r P(X congruent r mod M) <= (1+(N_*M)^(-A))/M.
```

Proof.  Conditional on the current column capacities, the next row's `d`
stubs are a uniform `d`-subset of the `N_*` remaining column stubs.  The
number that land in the marked columns is therefore hypergeometric with
population size `N_*`, marked count `K_*`, and draw size `d`.  Apply the
general hypergeometric residue-mixing lemma.  QED.

This proves the desired one-row residue mixing in the balanced
row-conditioned model.  It still does not handle the simultaneous column-sum
conditioning in the true fixed two-degree graph model, but it replaces the
first conditioning layer by a theorem rather than a numerical heuristic.

**Corollary: Balanced Row-Regular Cross-Edge Anti-Concentration.**  Let
`X,Y` be disjoint vertex sets with `|Y|=2m`.  Fix an arbitrary graph on `X`.
Independently for each `x in X`, choose exactly `m` neighbors of `x` in `Y`,
uniformly among all `m`-subsets of `Y`.  Let `Y_0 subset Y` have size `m`,
let `X_0 subset X` have size `a`, and let `M>=2`.  If

```text
m >= C M^2 log M
```

for a sufficiently large absolute constant `C`, then the probability that
the degrees of all vertices in `X_0` inside the induced graph on
`X_0 union Y_0` are congruent modulo `M` is at most

```text
((1+o_M(1))/M)^(a-1),
```

uniformly in `a,m`, in the fixed graph on `X`, and in the chosen set `Y_0`.

Proof.  For `x in X_0`, write the induced degree of `x` in
`X_0 union Y_0` as

```text
c_x + Z_x,
```

where `c_x` is its fixed degree inside `X_0`, and `Z_x` is the number of
chosen row-neighbors of `x` that lie in `Y_0`.  Since `x` chooses exactly
`m` elements from a `2m`-set with `m` marked elements `Y_0`, the variable
`Z_x` has the central hypergeometric distribution from the central
hypergeometric lemma above.
The choices for different `x` are independent.  Therefore each shifted
variable `c_x+Z_x` has every residue class modulo `M` with probability at
most `(1+o_M(1))/M`.

Pick one vertex `x_* in X_0`.  Summing over the residue of its degree and
using independence for all other vertices gives

```text
P(all degrees on X_0 are congruent mod M)
 <= ((1+o_M(1))/M)^(a-1).
```

QED.

This is exactly the row-sum-conditioned analogue of the earlier independent
cross-edge lemma in the balanced half-density case.  The true two-degree
model further conditions column sums, so this corollary is still not the
needed fixed-degree anti-concentration theorem; it isolates the remaining
obstacle as the transfer from independent row-regular choices to a
biregular, or nearly biregular, contingency table.

**Lemma: Sequential Residue Anti-Concentration.**  Let
`Z_1,...,Z_a` be random variables taking values in `Z/MZ`.  Suppose that for
some `eta`, for every `i=2,...,a` and every history
`Z_1=z_1,...,Z_{i-1}=z_{i-1}` of positive probability,

```text
max_r P(Z_i=r | Z_1=z_1,...,Z_{i-1}=z_{i-1}) <= eta.
```

Then

```text
P(Z_1=Z_2=...=Z_a) <= eta^(a-1).
```

Proof.  Decompose according to the common residue:

```text
P(Z_1=...=Z_a)
 = sum_r P(Z_1=r)
         prod_{i=2}^a P(Z_i=r | Z_1=...=Z_{i-1}=r).
```

Each conditional factor in the product is at most `eta`, and
`sum_r P(Z_1=r)=1`.  QED.

**Corollary: Prefix Row Mixing Is Enough For Biregular Residues.**  Let
`B` be a random bipartite graph with left side `X`, right side `Y`, and a
distribution supported on graphs with prescribed left degrees.  Fix
`X_0={x_1,...,x_a} subset X`, a set `Y_0 subset Y`, a modulus `M`, and
arbitrary shifts `c_i in Z/MZ`.  Reveal the neighborhoods of
`x_1,...,x_a` in this order.  If for every `i>=2`, after every positive
probability history of the first `i-1` revealed neighborhoods,

```text
max_r P(c_i+|N_B(x_i) cap Y_0| congruent r mod M | history) <= eta,
```

then

```text
P(c_1+|N_B(x_1) cap Y_0| = ... =
  c_a+|N_B(x_a) cap Y_0| mod M) <= eta^(a-1).
```

In particular, proving `eta=(1+o_M(1))/M` for long prefixes in the uniform
simple biregular model would give the same equal-row-residue estimate as in
the independent row-regular corollary.

Proof.  Apply the preceding lemma to

```text
Z_i = c_i + |N_B(x_i) cap Y_0| mod M.
```

The shifts absorb the already fixed degrees inside `X_0`, so equality of the
`Z_i` is exactly the one-sided modular condition needed for the row degrees in
`X_0 union Y_0`.  QED.

**Corollary: Configuration-Model Multirow Residue Anti-Concentration.**  In
the bipartite configuration model with prescribed row degrees, fix rows
`x_1,...,x_a`, a marked set of column vertices `Y_0`, a modulus `M`, and
shifts `c_i in Z/MZ`.  Reveal the stubs of `x_1,...,x_a` in this order.  Let
`N_i` be the number of unmatched column stubs and `K_i` the number of those
stubs that lie in columns of `Y_0` immediately before row `x_i` is exposed,
and let `d_i` be the degree of row `x_i`.  Suppose that for some `A>0`, every
positive-probability prefix history and every `i=2,...,a` satisfy

```text
Lambda_i :=
min(K_i,N_i-K_i) (d_i/N_i)(1-d_i/N_i)
    >= C_A M^2 log(N_i M).
```

Let

```text
eta_i = sup (1+(N_iM)^(-A))/M,
```

where the supremum is over all allowed prefix histories before row `x_i`.
Then

```text
P(c_1+|N(x_1) cap Y_0| = ... =
  c_a+|N(x_a) cap Y_0| mod M)
 <= prod_{i=2}^a eta_i.
```

In particular, if every prefix history has `N_iM >= L` and the displayed
paired-mass condition holds, the right side is at most

```text
((1+L^(-A))/M)^(a-1).
```

Proof.  Conditional on any prefix history, row `x_i` chooses a uniform
`d_i`-subset of the remaining `N_i` column stubs.  Its number of hits in
`Y_0` is therefore hypergeometric with marked count `K_i`.  The paired-mass
assumption and the configuration-prefix hypergeometric corollary give, for
every residue `r`,

```text
P(c_i+|N(x_i) cap Y_0| congruent r mod M | history)
 <= (1+(N_iM)^(-A))/M.
```

Apply the sequential residue anti-concentration lemma, allowing the bound
`eta` to vary with `i` and multiplying the resulting conditional bounds.
QED.

This completes the anti-concentration argument in the configuration model
under an explicit remaining-stub mass condition.  The only missing step for
simple biregular graphs is the simplicity-distortion transfer stated below.

**Lemma: Single-Row Column Conditioning Is Harmless In Biregular Graphs.**
Let `B` be sampled uniformly from all simple `d`-regular bipartite graphs with
left side `X` and right side `Y`, where `|X|=|Y|=N`.  Fix `x in X` and
`Y_0 subset Y` with `|Y_0|=K`.  Then

```text
|N_B(x) cap Y_0|
```

has the hypergeometric distribution obtained by drawing `d` elements from an
`N`-element population with `K` marked elements.

In particular, when `N=2m`, `K=d=m`, and `m>=C M^2 log M`, the residue of
`|N_B(x) cap Y_0|` modulo `M` is `(1+o_M(1))/M`-uniform.

Proof.  The uniform model is invariant under every permutation of the right
side `Y`.  Since every sampled graph has `deg_B(x)=d`, the random set
`N_B(x)` is supported on `d`-subsets of `Y`.  For any two `d`-subsets
`S,S' subset Y`, choose a permutation of `Y` sending `S` to `S'`.  This
permutation is a bijection from graphs with `N_B(x)=S` to graphs with
`N_B(x)=S'`.  Hence `N_B(x)` is a uniform `d`-subset of `Y`.  Intersecting a
uniform `d`-subset with the fixed marked set `Y_0` gives exactly the stated
hypergeometric distribution.  The final assertion is the central
hypergeometric residue-mixing lemma.  QED.

This lemma shows that column-sum conditioning does not damage the marginal
distribution of one row.  The missing fixed-degree anti-concentration theorem
is therefore a genuinely multi-row dependence problem: after conditioning on
the first few rows, the remaining column capacities are no longer uniform,
and one needs a switching or martingale argument proving that enough rows
still have near-hypergeometric residue mixing on the tested set.

**Lemma: Configuration-To-Simple Conditioning Transfer.**  Fix bipartite
degree sequences on left side `X` and right side `Y`, and sample the
bipartite configuration model with these degrees.  Let `Simp` be the event
that the configuration is simple.  Conditional on `Simp`, the resulting
simple bipartite graph is uniform among all simple bipartite graphs with the
prescribed degree sequences.

Consequently, let `E_conf` be any event in the configuration model and
`E_simple` an event in the uniform simple model such that, on `Simp`,
`E_conf` is exactly the pullback of `E_simple`.  If

```text
P_conf(Simp | E_conf) <= K P_conf(Simp),
```

then

```text
P_simple(E_simple) <= K P_conf(E_conf).
```

Proof.  Every simple bipartite graph with the prescribed degree sequence is
represented by exactly

```text
prod_{x in X} d_x!  prod_{y in Y} c_y!
```

configurations: the row stubs incident with each `x` may be permuted
arbitrarily among its neighbors, and likewise the column stubs incident with
each `y`.  This number depends only on the degree sequences, not on the
simple graph.  Therefore the configuration model conditioned on `Simp` is the
uniform simple model.

For the inequality,

```text
P_simple(E_simple)=P_conf(E_conf | Simp)
                  =P_conf(E_conf) P_conf(Simp | E_conf)/P_conf(Simp)
                  <= K P_conf(E_conf).
```

QED.

**Corollary: Simplicity Distortion Is The Biregular Switching Target.**  In
the setting of the previous lemma, fix `X_0={x_1,...,x_a}`, `Y_0`, a modulus
`M`, and shifts `c_i`.  Let `E_simple` be the simple-graph event that

```text
c_1+|N(x_1) cap Y_0| = ... =
c_a+|N(x_a) cap Y_0|       mod M.
```

Let `E_conf` be the corresponding configuration event with
`|N(x_i) cap Y_0|` replaced by the number of row stubs of `x_i` matched to
column stubs belonging to vertices of `Y_0`.  Assume that in the
configuration model

```text
P_conf(E_conf) <= eta^(a-1)
```

and that the simplicity event has distortion at most `K` on this residue
event:

```text
P_conf(Simp | E_conf) <= K P_conf(Simp).
```

Then the uniform simple model satisfies

```text
P_simple(E_simple) <= K eta^(a-1).
```

In particular, a switching theorem giving `K=exp(o(a))` together with
`eta=(1+o_M(1))/M` would transfer the configuration-model prefix mixing
bound to the simple biregular model at the exponential scale needed in the
first-moment obstruction.

Proof.  Under `Simp`, a row has at most one edge to each column vertex, so
stub hits in columns of `Y_0` are exactly distinct neighbor hits in `Y_0`.
Thus `E_conf` pulls back `E_simple` on the simple configurations, and the
conditioning-transfer lemma applies.  QED.

The helper `EXPERIMENTS/biregular_residue_sample.py` probes this remaining
dependence by sampling simple regular bipartite graphs with degree-preserving
switches and comparing equal-residue probabilities against the independent
hypergeometric-row prediction.  For example,

```text
python3 82/EXPERIMENTS/biregular_residue_sample.py \
  --n 128 --degree 64 --marked 64 --rows 3 --modulus 8 \
  --samples 2000 --burnin 10000 --between 500 --seed 83128
```

reports empirical probability `0.0175` versus independent-row prediction
`0.016253`.  This is only finite evidence; it suggests that the multi-row
conditioning may be controllable in dense balanced cases, but supplies no
asymptotic switching bound.

The exact dynamic program `EXPERIMENTS/biregular_residue_exact.py` gives
small labelled checks without sampling.  It groups the column side by
remaining capacities inside and outside `Y_0`; this makes exact enumeration
possible for small balanced cases.  The commands

```text
python3 82/EXPERIMENTS/biregular_residue_exact.py \
  --n 8 --degree 4 --marked 4 --rows 3 --modulus 4
python3 82/EXPERIMENTS/biregular_residue_exact.py \
  --n 10 --degree 5 --marked 5 --rows 3 --modulus 4
python3 82/EXPERIMENTS/biregular_residue_exact.py \
  --n 12 --degree 6 --marked 6 --rows 3 --modulus 4
```

report exact equal-row-residue probabilities

```text
0.150371377245717603835041,
0.110390208666622881332398,
0.102981196977735162641382,
```

versus independent-row predictions

```text
0.159930029154518950437318,
0.127173091458805744520030,
0.110864262702684021624821.
```

Thus these finite balanced cases do not show positive correlation large
enough to threaten the desired anti-concentration transfer.  They remain
finite calibration only; the required theorem is still the simplicity
distortion/switching bound above.

The same exact DP also rules out a stronger shortcut.  The command

```text
python3 82/EXPERIMENTS/biregular_residue_exact.py \
  --n 8 --degree 4 --marked 4 --rows 4 --modulus 4
```

reports exact probability

```text
0.0769772002163447221387533
```

whereas the independent-row prediction is

```text
0.0754145772594752186588921.
```

The ratio is about `1.02072`.  Thus the desired switching theorem cannot be
the naive assertion that equal-residue events in the simple regular model are
always no more likely than under independent hypergeometric rows.  The
available target is necessarily weaker: an `exp(o(a))` distortion bound is
still compatible with this exact positive finite correlation.

The same exact script can inspect the sequential condition directly.  With
`--prefix-next 3`, it reports the distribution of the fourth row's residue
conditional on the first three rows having one common residue.  For

```text
(N,d,|Y_0|,M)=(8,4,4,4),(10,5,5,4),(12,6,6,4),
```

the conditional next-row maximum probabilities are respectively

```text
0.531031205921509084582683,
0.394465256057708166368660,
0.434251675695444427491401.
```

The corresponding one-row hypergeometric maximum probabilities are

```text
0.514285714286,
0.396825396825,
0.432900432900.
```

Thus the prefix conditioning introduces only a small finite distortion in
these tests, sometimes upward and sometimes downward.  This is still far from
an asymptotic proof, but it validates the formulation of the switching target
as a sequential point-probability bound rather than only an aggregate
all-rows estimate.

For example,

```text
python3 82/EXPERIMENTS/hypergeom_residue.py \
  --population 8192 --marked 4096 --draws 4096 --modulus 32
```

has variance about `512` and maximum residue probability only `1.00011` times
uniform; the maximum nontrivial Fourier bias is about `5.2e-5`.  The general
paired-mass quantity is `Lambda=1024`, and the unit-constant paired-mass
Fourier bound is about `0.00236`.  By contrast,

```text
python3 82/EXPERIMENTS/hypergeom_residue.py \
  --population 2048 --marked 256 --draws 1024 --modulus 32
```

has variance about `56` and maximum residue probability about `1.70` times
uniform; the maximum nontrivial Fourier bias is about `0.34`.  Here
`Lambda=64`, and the paired-mass bound is correspondingly useless
(`12.22` before the hidden absolute constant is inserted).  This finite
calibration is consistent with a local-CLT requirement on the scale of `M^2`
variance for residue mixing, but it does not address the harder column-sum
conditioning in the true fixed two-degree model.

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

**Conditional Corollary: Fixed-Degree Anti-Concentration Refutes Sublinear
Two-Degree Partition Lifts.**  Assume the anti-concentration hypothesis from
the preceding proposition.  Let `b(q)=o(q)` along dyadic `q`.  Then for all
sufficiently large dyadic `q` there is a connected two-degree `q`-modular
graph with no partition into at most `b(q)` induced `2q`-modular subgraphs.

Proof.  Put

```text
psi(q)=q/b(q).
```

After increasing `q` if necessary, `psi(q)->infinity` and `b(q)>=1`.  The
preceding conditional proposition gives a connected `q`-modular graph
`G_q` on `N=q^3` vertices, with degrees taking the two values
`(N-q)/2` and `(N+q)/2`, and with no induced `2q`-modular subgraph of order
at least

```text
N psi(q)/q = N/b(q).
```

If `G_q` had a partition into at most `b(q)` induced `2q`-modular subgraphs,
one part would have order at least `N/b(q)`, contradicting the choice of
`G_q`.  QED.

Thus, unless the fixed-degree anti-concentration heuristic is false, the
dyadic partition-only route cannot have the sublinear part count required by
Conditional Proposition "Sublinear-Exponent Dyadic Partitioning Would
Suffice".  The viable dyadic target must use a regular alternative, as in the
witness-or-regular dichotomy.

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

The same four-part lower bound already appears at the next tested dyadic
scale.

**Computational Proposition: Connected `8 -> 16` Lift Requiring Four
Parts.**  There is a connected `8`-modular graph on `22` vertices which has
no partition into three induced `16`-modular subgraphs, but does have such a
partition into four parts.

Proof.  In the edge ordering used by `EXPERIMENTS/regular_induced.py`, take
the mask

```text
2425868777297445838675614324200469721061724971533052238852775774199814.
```

The graph has degree sequence

```text
(6,6,6,6,6,6,6,6,6,6,6,14,14,14,14,14,14,14,14,14,14,14),
```

so all degrees are congruent modulo `8`, and the checker verifies that the
graph is connected.  Exact subset enumeration gives

```text
max_16_modular_order=7.
```

Therefore no three-part `16`-modular partition can exist: in any partition of
`22` vertices into three parts, one part has size at least `ceil(22/3)=8`.
On the other hand,

```text
python3 82/EXPERIMENTS/large_modular_partition.py 22 \
  2425868777297445838675614324200469721061724971533052238852775774199814 \
  --modulus 16 --find-min-colors 6 --node-limit 50000000
```

returns `min_colors=4`, with partition

```text
0,1,2,3,0,3,1,3,2,2,1,1,3,0,0,0,2,2,0,1,0,2
```

and part data

```text
color0:size7:residue2
color1:size5:residue0
color2:size6:residue5
color3:size4:residue1.
```

Thus the connected flexible dyadic lift, even if true, cannot be improved to
three parts at `q=8`.  QED.

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

**Lemma: Weighted Twin Blowups Inherit Quotient Regularity.**  Let `B` be a
graph on vertex set `{1,...,r}`.  Form an independent twin blowup `G` by
replacing vertex `i` with an independent cluster `C_i` of size `s_i`, and
joining `C_i` completely to `C_j` exactly when `ij in E(B)`.  For `t>=1`,
let

```text
I_t={i : s_i>=t}.
```

Then

```text
reg(G) >= max_{t>=1} t * reg(B[I_t]).
```

In particular, if `a_t=|I_t|`, then

```text
reg(G) >= max_{t>=1} t * F(a_t).
```

Proof.  Fix `t` and let `J subset I_t` induce a `d`-regular subgraph of
`B[I_t]` on `reg(B[I_t])` vertices.  Choose exactly `t` vertices from each
cluster `C_i` with `i in J`, and choose no other vertices.  In the induced
subgraph of `G`, every selected vertex in a cluster `C_i`, `i in J`, is
adjacent to all `t` selected vertices in each of the `d` neighboring clusters
inside `J`, and to no selected vertices in its own independent cluster.
Therefore every selected vertex has degree `td`, so the selected set is
regular of order `t|J|`.  Taking the maximum over `t` proves the first
displayed bound.  The second follows from the definition of `F(a_t)`, applied
to the quotient induced on `I_t`.  QED.

Thus independent twin blowups do not create a fundamentally new obstruction:
they transform the original problem into a weighted Ferrers maximum
`max_t t F(a_t)`.  With only the Ramsey bound `F(m)>=c log m`, this gives at
best another logarithmic lower bound in the worst case, so the lemma is not a
proof of Problem 82 by itself.  It does show that any sublogarithmic-looking
blowup obstruction must already encode hard quotient graphs across many
weight levels.

**Corollary: Superlog Lower Bounds Are Stable Under Twin Blowups.**  Let
`phi` be a nondecreasing function on positive integers with `phi(m)>=1` and

```text
phi(m)/log m -> infinity.
```

Suppose that every graph on `m` vertices has a regular induced subgraph on at
least `phi(m)` vertices.  Then every independent twin blowup `G` on `n`
vertices satisfies

```text
reg(G)/log n -> infinity
```

uniformly over all choices of quotient graph and cluster sizes.

Proof.  Let `a_t=|{i:s_i>=t}|` be the Ferrers profile of the cluster sizes,
so

```text
n=sum_{t>=1} a_t.
```

By the preceding lemma,

```text
reg(G) >= W := max_{t>=1} t phi(a_t),
```

where terms with `a_t=0` are ignored.  We show that `W/log n -> infinity`
for every Ferrers profile.

Fix `A>0`.  Choose `epsilon>0` so small that `epsilon A<1/3`.  Since
`phi(m)/log m -> infinity`, there is `m_0` such that

```text
log m <= epsilon phi(m)       for all m>=m_0.
```

For every `t` with `a_t>=m_0`,

```text
a_t <= exp(epsilon phi(a_t)) <= exp(epsilon W/t).
```

For `a_t<m_0` we use the trivial bound `a_t<=m_0`.  Also, whenever `a_t>0`,
we have `t<=W` because `phi(a_t)>=1`.  Therefore

```text
n <= m_0 W + sum_{1<=t<=W} exp(epsilon W/t)
   <= m_0 W + W exp(epsilon W).
```

If `W<=A log n`, then the last expression is at most

```text
m_0 A log n + A log n * n^{epsilon A},
```

which is smaller than `n` for all sufficiently large `n`, because
`epsilon A<1`.  This contradiction shows that `W>A log n` for all large `n`.
Since `A` was arbitrary, `W/log n -> infinity`, and hence
`reg(G)/log n -> infinity`.  QED.

This closure result is deliberately circular: taking `phi=F` would be exactly
the desired theorem on the quotient layers.  Its value is diagnostic.  Any
attempted counterexample built only by replacing quotient vertices with twin
clusters would have to contain the original hard problem in the quotient
sequence itself; the blowup weights cannot be the source of a new
Ramsey-scale obstruction.

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

The fixed-mask mode of `EXPERIMENTS/first_lift_chromatic.py` confirms that
the recorded `3`-part first-lift obstructions lie at or near this chromatic
boundary.  The masks

```text
2354908367450303302346343845       (n=14),
543363196844712283609173823066425664       (n=16)
```

both have `chi(G)=chi(complement(G))=5` and do admit four-part
`4`-modular partitions.  The later local-search mask

```text
1918387482888137124737399075       (n=14)
```

has `chi(G)=5` and `chi(complement(G))=4`, so the chromatic certificate itself
already explains why it cannot obstruct the four-part first lift.

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

**Corollary 4E.2A: Universal Slot Theorems Are Componentwise.**  Fix
`q,M,B,a`, and a residue multiset `R` of size `B` modulo `M`.  The following
are equivalent.

1. Every graph of source residue `a mod q` has an `R`-slot partition into
   induced `M`-modular subgraphs.
2. Every connected graph of source residue `a mod q` has such an `R`-slot
   partition.

Proof.  The first statement implies the second.  Conversely, suppose every
connected graph in the source class has an `R`-slot partition.  If `G` is any
graph in the source class, then every connected component of `G` is still in
the same source class, because vertex degrees are unchanged inside connected
components.  Apply the connected hypothesis to each component and then align
the component partitions into the global slots of `R` using Lemma 4E.  QED.

Thus any minimal counterexample to a fixed source-residue universal-slot
statement may be assumed connected.  This does not by itself solve the
problem, but it justifies filtering computational searches to connected
graphs after a candidate slot multiset has been fixed.

**Conditional Proposition 4E.2B: Source-Residue Dyadic Lifts Would Suffice.**
Let `b(q)` be a function on dyadic integers.  Suppose that, for every dyadic
`q>=2`, every residue `a mod q`, and every graph whose degrees are all
congruent to `a mod q`, the vertex set can be partitioned into at most
`b(q)` induced `2q`-modular subgraphs.  If there is a fixed `alpha<1` such
that

```text
b(q) <= q^alpha
```

for all sufficiently large dyadic `q`, then `F(n)/log n -> infinity`.

In particular, the conclusion follows if for every sufficiently large dyadic
`q` and every source residue `a mod q` there is a universal residue multiset
`R_{q,a}` of size at most `q^alpha` modulo `2q` for the lift
`a mod q -> 2q`.

Proof.  Let `H` be any `q`-modular induced subgraph of an ambient graph.
Then all degrees in `H` have some common source residue `a mod q`.  Applying
the assumed source-residue lift to `H` partitions `V(H)` into at most `b(q)`
induced `2q`-modular subgraphs.  Thus the hypothesis of Conditional
Proposition "Sublinear-Exponent Dyadic Partitioning Would Suffice" holds with
the same function `b(q)`, and the desired conclusion follows.

For the final assertion, Lemma 4E.2 says that a universal slot multiset
`R_{q,a}` for each source residue is equivalent to the corresponding
source-residue partition theorem.  QED.

This is the exact formal role of the source-sensitive slot searches below.
They are not trying to find one residue multiset that works for all
`q`-modular graphs at a fixed dyadic step; they are trying to make the
function `b(q)` small after the source residue is fixed.  A uniform
four-slot theorem for every dyadic `q` and every source residue would settle
Erdos Problem 82 by this proposition.

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

The other natural three-slot simplification, keeping the two zero slots but
using only one residue-`2` slot, is also false.

**Computational Counterexample: The Three-Slot `(0,0,2)` Strengthening Is
False.**  There is an even graph on `8` vertices with no `(0,0,2)` modular
partition.

Proof.  In the edge order used by `EXPERIMENTS/regular_induced.py`, take the
mask

```text
225409983.
```

The edge set is

```text
01, 02, 03, 04, 05, 06, 12, 13, 14, 16, 17,
23, 24, 26, 27, 34, 35, 37, 45, 47, 57, 67.
```

The degree sequence is

```text
6,6,6,6,6,4,4,6,
```

so the graph is even.  The exact fixed-slot checker, now allowing candidate
multisets with fewer than four slots, gives

```text
/tmp/universal_slots_fast --n 8 --degree-parity 0 --candidates 0,0,2
```

and reports `slots=0,0,2 bad=225409983`.  Direct verification with

```text
python3 82/EXPERIMENTS/slot_partition.py 8 --mask 225409983 --slots 0,0,2
```

returns `slot_partition=no`.

This graph is not a counterexample to the matching-slot target.  The command

```text
python3 82/EXPERIMENTS/matching_slot_search.py 8 --mask 225409983
```

finds the certificate

```text
A={0,1,2,3,4},  B={5},  C={6,7},  D=empty.
```

Here `A` is a `K_5`, hence zero-residue modulo `4`; `B` is independent; and
`C` is the induced edge `67`.  Thus the exact matching slot repairs a genuine
three-slot obstruction.  QED.

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

The formerly plausible computational `4 -> 8` ordinary-slot family was

```text
R_0=(0,1,2,4),   R_1=(0,0,2,2),
R_2=(0,0,1,2),   R_3=(0,0,1,3),
```

where `R_a` is meant for graphs whose total degree residue is `a mod 4`.
It was useful finite evidence but is now refuted as a universal four-slot
source-residue theorem.  The refutation is important: it shows that the
dyadic route cannot rely on a uniform four-slot theorem at every level,
although Conditional Proposition 4E.2B remains available with any
sublinear-in-`q` part bound.

The checker `EXPERIMENTS/source_slots_fast.cpp` verifies the old family
exactly for all labelled `8`-vertex graphs whose degrees are congruent modulo
`4`.  It enumerates the graph induced by vertices `0,...,n-2` and solves the
edges to the last vertex so that every degree has the prescribed source
residue modulo `4`.  For `n=8` the exact source-residue counts and four-slot
survivor counts are:

```text
source 0: 23552 graphs, 49 surviving four-slot multisets,
source 1:  7168 graphs, 15 surviving four-slot multisets,
source 2:  7168 graphs, 17 surviving four-slot multisets,
source 3: 23552 graphs, 23 surviving four-slot multisets.
```

The displayed old family `R_0,R_1,R_2,R_3` survives in the corresponding
source classes.  The cleaner complete-multipartite pattern also survives in
sources `0` and `1`, but is killed in sources `2` and `3`; this agrees with
the explicit masks recorded below.  The exact checks are reproduced by

```text
/tmp/source_slots_fast --n 8 --source-modulus 4 --target-modulus 8 --source-residue 0 --candidates '0,0,4,4;0,1,2,4'
/tmp/source_slots_fast --n 8 --source-modulus 4 --target-modulus 8 --source-residue 1 --candidates '0,1,4,5;0,0,2,2'
/tmp/source_slots_fast --n 8 --source-modulus 4 --target-modulus 8 --source-residue 2 --candidates '0,2,4,6;0,0,1,2'
/tmp/source_slots_fast --n 8 --source-modulus 4 --target-modulus 8 --source-residue 3 --candidates '0,3,4,7;0,0,1,3'
```

The same family also survives initial nonterminal chunks beyond the full
`n=8` sweep.  For `n=9`, the range `0 <= internal_bits < 10000000` checks
`18153` source-`0` graphs and `20876` source-`2` graphs; source residues `1`
and `3` are impossible on `9` vertices by degree-sum parity.  For `n=10`, the
two ranges

```text
0 <= internal_bits < 2000000,
2000000 <= internal_bits < 4000000
```

check respectively

```text
source 0: 131 and 205 graphs,
source 1: 852 and 358 graphs,
source 2: 16640 and 5861 graphs,
source 3: 1891 and 2754 graphs,
```

with no counterexample to the displayed old source-residue family.  These are
finite prefix checks, not a proof, and the next deterministic sample refutes
the source-`0` member.

**Computational Proposition: Four Source-`0` Slots Do Not Suffice For
`4 -> 8`.**  There is no four-element residue multiset `R` modulo `8` such
that every graph whose degrees are all `0 mod 4` has a partition into induced
`8`-modular subgraphs with residue signature contained in `R`.

Proof.  The deterministic seeded command

```text
/tmp/source_slots_fast --n 11 --source-modulus 4 --target-modulus 8 \
  --source-residue 0 --slot-count 4 --random-samples 5000000 \
  --seed 1100 --quiet-kills
```

checks `2986` labelled source-`0 mod 4` graphs on `11` vertices.  For every
four-slot multiset except the following five, one of these checked graphs is
a concrete counterexample:

```text
(0,0,2,2),  (0,1,1,2),  (0,1,2,2),
(0,1,2,3),  (0,2,2,2).
```

The old candidate `(0,1,2,4)` is killed in this sample by the `11`-vertex
mask

```text
11691695018335739,
```

whose degree sequence is

```text
8,8,4,4,4,4,8,4,4,4,4.
```

The five survivors are killed by complete multipartite source-`0` graphs:

```text
(0,0,2,2)  is killed by class sizes (3,3,3,3,3),
(0,1,1,2)  is killed by class sizes (2,6,6),
(0,1,2,2)  is killed by class sizes (2,6,6),
(0,1,2,3)  is killed by class sizes (4,4,4,4,4,4),
(0,2,2,2)  is killed by class sizes (4,8,8,8).
```

In each listed complete multipartite graph, every vertex degree is `0 mod 4`.
The fixed-slot checks are certified by `EXPERIMENTS/multipartite_modular.py`
with `--source-modulus 4 --source-residue 0 --target-modulus 8 --slots R`.
Thus every four-element residue multiset modulo `8` has a source-`0`
counterexample.  By Lemma 4E.2, even the flexible four-part source-`0`
`4 -> 8` lift is false.  QED.

This obstruction does not disprove Conditional Proposition 4E.2B; the
proposition only requires `b(q)<=q^alpha` for large dyadic `q`, and the
exceptional behavior at `q=4` can be absorbed into the initial constant.
It does, however, rule out the previously hoped-for uniform four-slot theorem
and forces the dyadic route to aim for a growing but sublinear part bound, or
for a different witness-or-regular dichotomy.

As a first calibration after this obstruction, the same `n=11`, source-`0`
sample with `--slot-count 5` leaves `52` of the `792` five-slot multisets
alive.  This is only an exploratory lower-bound calibration for the slot
count; no five-slot source-`0` theorem has been identified.  Among the
surviving candidates, the simple multiset

```text
(0,0,0,1,4)
```

passes the full `n=8` and `n=9` source-`0` sweeps, deterministic
`20,000,000`-sample source-`0` probes on `n=10` and `n=11`, a deterministic
`50,000,000`-sample source-`0` probe on `n=12`, and the first `100`
source-`0` complete-multipartite vectors with at most six classes of size at
most `16`.  The exact `n=9` sweep checks `1,409,024` source-`0` graphs; its
connected, minimum-degree-`4` subcheck contains `1,216,702` graphs.  The
`n=12` connected, minimum-degree-`4` random probe with `50,000,000` sampled
internal graphs checks `8876` accepted graphs.  This is the current smallest
concrete replacement target for the refuted four-slot source-`0` theorem, but
it remains only finite evidence.

For comparison, the source-`2` four-slot candidate `(0,0,1,2)` survives the
full exact `n=9` source-`2` sweep, which checks `229,376` source-modular
graphs.  Thus the first exact odd-order obstruction is currently confined to
source residue `0`, where four slots are already known to be impossible.

The five-slot candidate is genuinely five-slot, not merely a padded four-slot
candidate.

**Computational Example: The Candidate `(0,0,0,1,4)` Can Need All Five
Slots.**  There is a source-`0 mod 4` graph with an
`(0,0,0,1,4)`-slot partition and with no partition using only four of those
five slots.

Proof.  Let `R=(0,0,0,1,4)`.  Its distinct four-element submultisets are

```text
(0,0,1,4),     (0,0,0,4),     (0,0,0,1).
```

The `9`-vertex graph with mask

```text
56480298224
```

has degree sequence

```text
4,4,4,4,4,4,4,4,8
```

and is source-`0 mod 4`.  The exact command

```text
/tmp/source_slots_fast --n 9 --source-modulus 4 --target-modulus 8 \
  --source-residue 0 --candidates '0,0,1,4;0,0,0,4;0,0,0,1'
```

kills `(0,0,1,4)` and `(0,0,0,4)` on this mask, while `(0,0,0,1)` survives
the full `n=9` sweep.  The `11`-vertex graph with mask

```text
10809538658185181
```

has degree sequence

```text
8,4,8,8,4,8,4,8,8,4,4
```

and is also source-`0 mod 4`.  The seeded command

```text
/tmp/source_slots_fast --n 11 --source-modulus 4 --target-modulus 8 \
  --source-residue 0 --candidates '0,0,0,1' \
  --random-samples 100000 --seed 1100
```

kills `(0,0,0,1)` on this mask.

Now take the disjoint union of these two graphs.  Each component has an
`R`-slot partition because `R` passes the full `n=9` source-`0` sweep and the
same seeded `n=11` sample containing the second mask.  Lemma 4E aligns the
two component partitions into the global slots of `R`.

If the disjoint union had an `R`-slot partition using at most four nonempty
slots, then its used residue signature would be contained in one of the three
four-element submultisets displayed above.  Restricting that partition to the
component that kills the corresponding submultiset gives a contradiction.
Therefore all five slots of `R` are required.  QED.

This example should not be confused with a flexible four-part obstruction.
The fixed-signature obstruction is created by disjoint-union incompatibility:
different components force different four-slot signatures.  When the residue
signature is allowed to vary from graph to graph, the current finite evidence
points in the opposite direction.  The checker
`EXPERIMENTS/source_slots_fast.cpp` has a `--flexible-parts` mode that tests
existence of some partition into a prescribed number of target-modular parts,
ignoring fixed residue slots.  It verifies that every source-`0 mod 4` graph
in the exact `n=9` solved-edge sweep has a flexible four-part `8`-modular
partition; this checks `1,409,024` graphs.  The connected, minimum-degree-`4`
subcheck of the same sweep checks `1,216,702` graphs and also passes.
Deterministic random probes also find no flexible four-part counterexample in
`29,804` accepted source-`0` graphs on `11` vertices, nor in `8864` accepted
connected, minimum-degree-`4` source-`0` graphs on `12` vertices.

Thus the fixed-source universal-slot compactness route and the connected
flexible coarse-lift route have different obstruction profiles.  The
source-`0` five-slot evidence rules out a universal four-slot theorem, but it
does not rule out a connected four-part flexible `4 -> 8` theorem, which is
the formulation relevant to the coarse-lift propositions above.

Even three flexible parts are surprisingly robust in the small source-specific
checks, though they are false in general by Computational Proposition 4E.4
and its connected-complement corollary.  The exact `n=8` and `n=9` source-`0`
sweeps both have flexible three-part `8`-modular partitions for every checked
graph.  The exact `n=9` source-`2` sweep also passes with three flexible
parts.  Deterministic `n=10` random probes with `50,000,000` sampled internal
graphs find no three-part counterexample in any source residue modulo `4`;
the accepted counts in source residues `0,1,2,3` are respectively
`96,849`, `96,006`, `35,389`, and `35,450`.  A connected, minimum-degree-`4`
source-`0` probe on `n=12` also passes with three flexible parts, checking
`8894` accepted graphs.  These data suggest that the connected three-part
obstruction is larger or more structured than the current random source
models, and that a connected four-part `4 -> 8` theorem remains a plausible
local target.

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

For the flexible part-count formulation, complete multipartite graphs satisfy
an even stronger theorem.

**Lemma: Complete Multipartite Flexible Two-Part Lift.**  Let `q` be a
positive integer and let `H` be a complete multipartite graph whose vertex
degrees are all congruent modulo `q`.  Then `V(H)` can be partitioned into at
most two induced `2q`-modular subgraphs.

Proof.  Let the multipartite class sizes be `s_1,...,s_t`, and let
`N=sum_i s_i`.  A vertex in class `i` has degree `N-s_i`.  Since all degrees
are congruent modulo `q`, all class sizes are congruent modulo `q`.

There are therefore at most two possible residues for the class sizes modulo
`2q`: say `r` and `r+q`.  Let `A` be the union of all classes whose size is
`r mod 2q`, and let `B` be the union of all classes whose size is
`r+q mod 2q`, omitting either set if it is empty.

Consider one of these two induced subgraphs, say on a union `U` of whole
classes whose sizes are all congruent to `c mod 2q`.  If `U` meets class `i`,
then every vertex in that class has internal degree

```text
|U|-s_i congruent |U|-c mod 2q.
```

This residue is independent of the class `i`, so `H[U]` is `2q`-modular.
Thus `A` and `B` give the required partition.  QED.

This lemma explains why complete multipartite graphs have not obstructed the
connected flexible coarse-lift route: their apparent fixed-slot complexity is
only a residue-alignment issue.  The obstruction from Computational
Proposition 4E.4 is not complete multipartite.

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

The same failure persists at the next dyadic step, even in source residues
where the current irregular four-slot candidates survive.  For source
residue `2 mod 4`, the `8`-vertex mask

```text
176527396
```

has degree sequence

```text
2,2,2,2,2,2,6,2,
```

and no `(0,2,4,6)` partition modulo `8`, while it does have a
`(0,0,1,2)` partition modulo `8`.  For source residue `3 mod 4`, the mask

```text
196192817
```

has degree sequence

```text
3,3,3,3,3,3,7,3,
```

and no `(0,3,4,7)` partition modulo `8`, while it does have a
`(0,0,1,3)` partition modulo `8`.  The four checks are

```text
python3 82/EXPERIMENTS/slot_partition.py 8 --mask 176527396 --modulus 8 --slots 0,2,4,6
python3 82/EXPERIMENTS/slot_partition.py 8 --mask 176527396 --modulus 8 --slots 0,0,1,2
python3 82/EXPERIMENTS/slot_partition.py 8 --mask 196192817 --modulus 8 --slots 0,3,4,7
python3 82/EXPERIMENTS/slot_partition.py 8 --mask 196192817 --modulus 8 --slots 0,0,1,3
```

Thus the clean complete-multipartite pattern should be treated only as a
model-class theorem, not as a plausible universal fixed-slot lift.

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

**Lemma: One Degree Residue Is Trivial For The Matching-Slot Target.**  Let
`G` be an even graph.  If every vertex of `G` has degree congruent to
`0 mod 4`, then `G` has a matching-slot partition.  The same holds if every
vertex has degree congruent to `2 mod 4`.

Proof.  In the first case put all vertices in one of the zero slots and leave
the other slots empty.  In the second case put all vertices in the residue-`2`
slot `D`.  The required same-slot degrees are then just the original degrees
of `G`.  QED.

Consequently, a minimal counterexample to the matching-slot target must have
at least one vertex of degree `0 mod 4` and at least one vertex of degree
`2 mod 4`.

**Proposition: Complete Multipartite Even Graphs Satisfy The Matching-Slot
Target.**  Let `G` be a complete multipartite graph all of whose degrees are
even.  Then `G` has a partition `A,B,C,D` such that `A` and `B` have internal
degree `0 mod 4`, `C` is empty, and `D` has internal degree `2 mod 4`.

Proof.  Let the multipartite class sizes be `s_1,...,s_t`.  Since every
degree is even, the numbers `s_i` all have the same parity as
`N=sum_i s_i`.

First suppose all `s_i` are even.  Let `I_0={i:s_i congruent 0 mod 4}` and
`I_2={i:s_i congruent 2 mod 4}`.  Put all classes in `I_0` into `A`.  This
induces a complete multipartite graph in which every positive class
intersection has size `0 mod 4`, so every internal degree is `0 mod 4`.

If `|I_2|` is odd, put all classes in `I_2` into `B`; every vertex in such a
part has internal degree

```text
2(|I_2|-1) congruent 0 mod 4.
```

If `|I_2|` is even, put all classes in `I_2` into `D`; if the set is
nonempty, every vertex there has internal degree

```text
2(|I_2|-1) congruent 2 mod 4.
```

This covers the even-class case.

Now suppose all `s_i` are odd.  Then `t` is odd.  For each class with
`s_i congruent 1 mod 4`, reserve the whole class as a `1 mod 4` piece.  For
each class with `s_i congruent 3 mod 4`, reserve a piece of size `s_i-2`,
which is positive and congruent to `1 mod 4`, and leave a residual piece of
size `2`.  Let `R` be the set of classes with such residual pieces.

If `t congruent 1 mod 4`, put all reserved `1 mod 4` pieces into `A`.  Since
there are `t` positive pieces of the same residue, every vertex in `A` has
internal degree

```text
t-1 congruent 0 mod 4.
```

If `|R|` is odd, put all residual `2`-pieces into `B`, giving internal degree
`2(|R|-1) congruent 0 mod 4`.  If `|R|` is even, put all residual `2`-pieces
into `D`, giving internal degree `2(|R|-1) congruent 2 mod 4` when nonempty.

It remains to handle `t congruent 3 mod 4`.  Put all reserved `1 mod 4`
pieces into `D`; their internal degree is `t-1 congruent 2 mod 4`.  If
`|R|` is odd, put all residual `2`-pieces into `A`, where they have internal
degree `2(|R|-1) congruent 0 mod 4`.  If `|R|` is even and nonzero, put one
residual `2`-piece alone into `A` and all remaining residual `2`-pieces into
`B`; a one-class part is independent, and the remaining number of residual
pieces is odd, so `B` has internal degree `0 mod 4`.  If `R` is empty there
is nothing more to place.

In all cases the described pieces partition the vertex set, `C` is empty, and
the induced same-slot degrees have the required residues.  QED.

The verifier `EXPERIMENTS/matching_multipartite.py` checks the corresponding
integer count model.  For example,

```text
python3 82/EXPERIMENTS/matching_multipartite.py --max-classes 5 --max-size 10
python3 82/EXPERIMENTS/matching_multipartite.py --max-classes 6 --max-size 12 --max-total 30
python3 82/EXPERIMENTS/matching_multipartite.py --max-classes 7 --max-size 10 --max-total 28
```

check `417`, `508`, and `459` even complete multipartite size vectors,
respectively, with no counterexample.

The data currently support a sharper matching-slot strengthening.

**One-Edge Matching-Slot Candidate.**  Every even graph has a matching-slot
partition `A,B,C,D` in which the induced matching slot `C` is either empty or
a single edge.

This candidate is strictly stronger than the matching-slot target and strictly
weaker than the false three-slot `(0,0,2)` target.  The latter is exactly the
case `C=empty`; the mask `225409983` above shows that an induced edge may be
needed.

Equivalently, every even graph `G` should satisfy one of the following two
alternatives:

1. `V(G)` has a partition into two `0 mod 4` parts and one `2 mod 4` part;
2. there is an edge `uv` such that `V(G)\{u,v}` has a partition into two
   `0 mod 4` parts and one `2 mod 4` part.

Indeed, if a one-edge matching-slot certificate has `C=empty`, then the first
alternative holds.  If `C={u,v}`, then `uv` is an edge and the remaining slots
`A,B,D` form a `(0,0,2)` partition of `G-\{u,v}`; edges from `u` or `v` to
the other slots are irrelevant because they are cross-slot edges.  Conversely,
either displayed alternative gives a matching-slot certificate by taking
`C=empty` or `C={u,v}`.  Thus the one-edge candidate is a deletion-of-one-edge
endpoint version of the three-slot `(0,0,2)` problem.

The checker `EXPERIMENTS/matching_slot_fast.cpp` supports this strengthening
with `--max-c-vertices 2`.  It verifies the full labelled `n=8` even-graph
sweep, split into eight adjacent chunks of `262144` free-edge masks:

```text
/tmp/matching_slot_fast --n 8 --max-c-vertices 2 --limit 262144
/tmp/matching_slot_fast --n 8 --max-c-vertices 2 --start 262144 --limit 524288
/tmp/matching_slot_fast --n 8 --max-c-vertices 2 --start 524288 --limit 786432
/tmp/matching_slot_fast --n 8 --max-c-vertices 2 --start 786432 --limit 1048576
/tmp/matching_slot_fast --n 8 --max-c-vertices 2 --start 1048576 --limit 1310720
/tmp/matching_slot_fast --n 8 --max-c-vertices 2 --start 1310720 --limit 1572864
/tmp/matching_slot_fast --n 8 --max-c-vertices 2 --start 1572864 --limit 1835008
/tmp/matching_slot_fast --n 8 --max-c-vertices 2 --start 1835008
```

Each command checks `262144` even graphs and finds no counterexample, for a
total of `2097152` labelled even graphs.  Initial `n=9` probes also find no
counterexample:

```text
/tmp/matching_slot_fast --n 9 --max-c-vertices 2 --limit 1000000
/tmp/matching_slot_fast --n 9 --max-c-vertices 2 --start 1000000 --limit 2000000
/tmp/matching_slot_fast --n 9 --max-c-vertices 2 --min-degree 4 --mixed-degree-residue --limit 10000000
```

These respectively check `1000000`, `1000000`, and `173715` filtered even
graphs.  The last command is the high-minimum-degree, mixed-degree-residue
regime left by the conditional reductions.  This is finite evidence only, but
the one-edge version is a sharper target for future structural arguments.

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
counterexample.  A later chunk

```text
/tmp/matching_slot_fast --n 9 --good-edge 0:1 --start 2000000 --limit 2100000
```

checks another `50000` edge-containing even graphs with no counterexample.
No proof is currently known.

**Conditional Lemma: Shape Of A Minimal Matching-Slot Counterexample.**
Suppose that the rooted zero-slot matching candidate and the edge-rooted
good-pattern matching candidate hold for every even graph with fewer vertices
than a vertex-minimal counterexample `G` to the unrooted matching-slot target.
Then `G` is connected, has no cut vertex, and every degree-`2` vertex of `G`
has adjacent neighbors.

Proof.  If `G` were disconnected, then each connected component would be an
even graph with fewer vertices than `G`.  The rooted zero-slot candidate on
each nontrivial component implies an ordinary matching-slot certificate for
that component; isolated vertices are put in a zero slot.  Taking the union
of the component certificates gives a certificate for `G`, because there are
no edges between components and the residue requirements are checked inside
each component.  This contradicts the choice of `G`, so `G` is connected.

If `G` had a cut vertex, Lemma "Cut-Vertex Reduction From Rooted Zero-Slot
Lobes" would apply, again using the rooted zero-slot candidate on the smaller
lobes, and would give an unrooted matching-slot certificate for `G`.  Hence
`G` has no cut vertex.

Finally let `v` be a degree-`2` vertex with distinct nonadjacent neighbors
`x,y`.  Form the smaller graph

```text
G' = G - v + xy.
```

The graph `G'` is even: the only affected remaining vertices are `x` and `y`,
and each loses one incident edge to `v` and gains the edge `xy`.  By the
edge-rooted good-pattern candidate applied to the rooted edge `xy` in `G'`,
there is a matching-slot certificate of `G'` in one of the two good endpoint
patterns.  Lemma "Direct Lifts Across Degree-`2` Suppression" then lifts that
certificate to a matching-slot certificate of `G`, a contradiction.  Thus the
neighbors of every degree-`2` vertex in `G` must be adjacent.  QED.

**Lemma: Direct Lifts Across Triangular Degree-`2` Suppression.**  Let `G` be
an even graph, let `v` be a degree-`2` vertex whose neighbors `x,y` are
adjacent, and let

```text
G' = G - v - xy.
```

Suppose `G'` has a matching-slot certificate in which `x` and `y` lie in
different slots and are not split between the two zero slots `A` and `B`.
Then `G` has a matching-slot certificate.

Proof.  In passing from `G'` to `G`, we add the edge `xy` and the new vertex
`v` adjacent to both `x` and `y`.  Since `x` and `y` lie in different slots,
the new edge `xy` is a cross-slot edge and does not change any same-slot
degree.  Since the endpoint slots are not exactly `A` and `B`, at least one
zero slot is unused by the two endpoints.  Put `v` in such an unused zero
slot.  Then the two edges incident with `v` are also cross-slot edges, so the
same-slot degrees of `x` and `y` remain unchanged, while `v` has same-slot
degree `0`.  All slot conditions are preserved.  QED.

The corresponding universal nonedge-rooted endpoint statement is false.  In
the empty graph on at least two vertices, every vertex in any matching-slot
certificate must lie in one of the two zero slots: an isolated vertex cannot
lie in the exact matching slot `C` or in the residue-`2` slot `D`.  Therefore
two prescribed nonadjacent vertices cannot be placed in different slots
without being split between `A` and `B`.  The new checker option
`--good-nonedge` verifies this obstruction immediately:

```text
python3 82/EXPERIMENTS/matching_slot_search.py 7 --exhaustive-even --good-nonedge 0:1
/tmp/matching_slot_fast --n 8 --good-nonedge 0:1
```

both report the empty graph, `mask=0`, as the first counterexample.  Thus
triangular degree-`2` suppression cannot be handled by a direct rooted
endpoint condition alone; it requires a recoloring argument or a richer
boundary signature.

There is a slightly richer direct repair that covers this empty-graph
obstruction.  Keep the notation of the triangular suppression lemma.  Suppose
`G'` has a matching-slot certificate in which `x` and `y` are split between
the two zero slots.  If one endpoint, say `y`, has no neighbor in its own
zero slot and no neighbor in the matching slot `C`, then the certificate also
lifts to `G`: move `y` into `C`, put the new vertex `v` into `C`, and leave
all other vertices fixed.  The edge `xy` is still a cross-slot edge.  The new
edge `vy` gives both `v` and `y` exactly one same-`C` neighbor, while the edge
`vx` is cross-slot.  No old zero-slot or matching-slot degree is changed,
because `y` had no neighbors in those two affected slots.

This suggests the following richer nonedge-rooted boundary condition for the
triangle case: either the direct different-slot condition of the previous
lemma holds, or the endpoints are split between `A` and `B` and one endpoint
is isolated from both its own zero slot and `C`.  The Python checker option
`--triangle-nonedge` tests exactly this condition.  It verifies all even
graphs on at most `7` vertices for the rooted nonedge `0:1`:

```text
python3 82/EXPERIMENTS/matching_slot_search.py 7 --exhaustive-even --triangle-nonedge 0:1
```

The C++ checker ports the same condition and verifies the full labelled
`n=8` rooted-nonedge sweep, plus a prefix at `n=9`:

```text
/tmp/matching_slot_fast --n 8 --triangle-nonedge 0:1
/tmp/matching_slot_fast --n 9 --triangle-nonedge 0:1 --limit 10000000
```

These commands respectively check `1048576` and `5000000` even graphs with
`01` nonadjacent, with no counterexample.

This is only finite evidence, but it identifies a plausible boundary
signature for handling degree-`2` triangles in a minimal-counterexample
induction.

**Conditional Lemma: Triangle Boundary Eliminates Degree Two.**  Suppose that
the rooted zero-slot matching candidate, the edge-rooted good-pattern
candidate, and the triangle-nonedge boundary condition above hold for every
even graph with fewer vertices than a vertex-minimal counterexample `G` to
the unrooted matching-slot target.  Then `G` has minimum degree at least `4`.

Proof.  By the previous conditional minimal-counterexample lemma, `G` is
connected, has no cut vertex, and every degree-`2` vertex has adjacent
neighbors.  Since `G` is connected, a degree-`0` vertex can occur only when
`G` has one vertex, which is trivially covered by a zero slot.  Thus a
nontrivial minimal counterexample has no degree-`0` vertices.

It remains to exclude a degree-`2` vertex `v`.  Let its adjacent neighbors be
`x,y`; the edge `xy` is present by the previous conditional lemma.  Form

```text
G' = G - v - xy.
```

The graph `G'` is even, because `x` and `y` each lose exactly two incident
edges, namely the edge to `v` and the edge `xy`, while all other vertex
degrees are unchanged.  It has fewer vertices than `G`, and `x,y` are
nonadjacent in `G'`.  By the triangle-nonedge boundary condition applied to
the rooted nonedge `xy` in `G'`, there is a matching-slot certificate of
`G'` satisfying either the direct boundary pattern or the one-endpoint
zero-to-matching recoloring repair.  The direct triangular suppression lemma
and the subsequent recoloring repair lift this certificate to `G`, a
contradiction.  Hence no degree-`2` vertex exists.  All degrees in an even
graph are even, so the minimum degree is at least `4`.  QED.

The fast checker now supports this post-reduction regime directly through
`--min-degree`, and it can also keep only the mixed degree-residue case forced
by the one-residue lemma using `--mixed-degree-residue`.  The commands

```text
/tmp/matching_slot_fast --n 8 --min-degree 4
/tmp/matching_slot_fast --n 9 --min-degree 4 --limit 10000000
/tmp/matching_slot_fast --n 9 --min-degree 4 --triangle-nonedge 0:1 --limit 10000000
/tmp/matching_slot_fast --n 10 --min-degree 4 --start 1234567890 --limit 1235567890
/tmp/matching_slot_fast --n 8 --min-degree 4 --mixed-degree-residue
/tmp/matching_slot_fast --n 9 --min-degree 4 --mixed-degree-residue --limit 10000000
/tmp/matching_slot_fast --n 9 --min-degree 4 --mixed-degree-residue --triangle-nonedge 0:1 --limit 10000000
/tmp/matching_slot_fast --n 10 --min-degree 4 --mixed-degree-residue --start 1234567890 --limit 1235567890
```

respectively check `188790`, `181088`, `81996`, `23124`, `169330`,
`173715`, `77030`, and `22863` filtered even graphs with no counterexample.
An additional `n=9` mixed-residue chunk

```text
/tmp/matching_slot_fast --n 9 --min-degree 4 --mixed-degree-residue --start 10000000 --limit 11000000
/tmp/matching_slot_fast --n 9 --min-degree 4 --mixed-degree-residue --triangle-nonedge 0:1 --start 10000000 --limit 11000000
```

checks `20469` and `9264` further filtered graphs, respectively, again with
no counterexample.
These are finite calibrations of the minimum-degree-four mixed-residue regime
left by the conditional reductions, not proof of the matching-slot target.

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
reg(G) >= max { n/t(G), reg(Q) } >= max { n/t(G), c log t(G) },
```

where `Q` is the twin quotient and `c>0` is an absolute Ramsey constant.

Proof.  Some twin class has order at least `n/t(G)`.  Since a twin class
induces either a clique or an independent set, it is regular.

For the quotient term, choose one representative from each twin class in a
regular induced subgraph of `Q`.  The representatives induce the same graph
inside `G`, so `reg(G)>=reg(Q)`.  Ramsey's theorem gives
`reg(Q)>=c log t(G)` because cliques and independent sets are regular.  QED.

Optimizing the displayed lower bound over `t` gives only `Omega(log n)`.
Thus neighborhood diversity alone cannot prove the target; it must be coupled
with a stronger statement about the quotient or with a way to use class sizes.

**Corollary 7.0A: Perfect Twin Quotients Are Polynomially Easy.**  If the
twin quotient `Q` of an `n`-vertex graph `G` is perfect, then

```text
reg(G) >= n^{1/3}.
```

Proof.  Let `t=t(G)`.  By Lemma 1A applied to the perfect quotient,
`reg(Q)>=sqrt(t)`.  Lemma 7 gives

```text
reg(G) >= max(n/t, sqrt(t)).
```

If `t<=n^{2/3}`, the first term is at least `n^{1/3}`; if
`t>=n^{2/3}`, the second term is at least `n^{1/3}`.  QED.

Therefore a Ramsey-scale counterexample cannot be explained by twin classes
whose quotient is perfect.  After quotienting twins, the hard quotient must
itself lie in the imperfect Ramsey core.

**Lemma 7.1: Modular Quotient Reduction.**  Let
`V(G)=V_1 union ... union V_m` be a partition into graph modules: for every
`i` and every vertex `x notin V_i`, either `x` is adjacent to all vertices of
`V_i` or to none of them.  Let `Q` be the quotient graph on
`{1,...,m}`, with `ij in E(Q)` exactly when all edges between `V_i` and
`V_j` are present.  Then

```text
reg(G) >= max_i reg(G[V_i]),
reg(G) >= reg(Q).
```

Consequently, if `G` has no regular induced subgraph on at least `k`
vertices, then every module `G[V_i]` and the quotient `Q` also have no
regular induced subgraph on at least `k` vertices.

Proof.  The first inequality is immediate because every induced subgraph
inside a module is also induced in `G`.

For the quotient inequality, let `J subset {1,...,m}` induce a `d`-regular
subgraph of `Q`.  Choose one representative vertex `v_i in V_i` for every
`i in J`.  The graph induced by these representatives in `G` is exactly
`Q[J]`, because module adjacency between two distinct parts is complete or
empty according to the quotient edge.  Hence the representative set is
`d`-regular in `G`.  Taking `J` of maximum regular order in `Q` proves
`reg(G)>=reg(Q)`.  The final assertion is the contrapositive of the two
inequalities.  QED.

This reduction is useful for modular decomposition: substitution operations
do not create a new obstruction unless both the substituted pieces and the
quotient remain hard.  In particular, a minimal counterexample can be assumed
prime with respect to any nontrivial module partition after recursively
discarding module or quotient witnesses.

The helper `EXPERIMENTS/module_diagnostics.py` checks this obstruction on
small fixed masks.  It finds that the `14`-vertex add-saturated
threshold-`7` mask has proper modules, the largest of size `13`, while the
delete-saturated `14`-vertex mask and the `12`-vertex `C_reg(1,5)>12` mask
are prime:

```text
python3 82/EXPERIMENTS/module_diagnostics.py 14 \
  --mask 765415324481232608887291903
python3 82/EXPERIMENTS/module_diagnostics.py 14 \
  --mask 88255234986600583676821506
python3 82/EXPERIMENTS/module_diagnostics.py 12 \
  --mask 25366485577502803966
```

Thus modular quotient structure explains part of one finite example but not
the rigid finite obstruction masks.

**Lemma 7.2: Substitution Regularity Criterion.**  Let `G` be obtained by
substituting graphs `H_i` into the vertices of a quotient graph `Q`:

```text
V(G)=V_1 union ... union V_m,       G[V_i]=H_i,
```

and for `i != j` all edges between `V_i` and `V_j` are present exactly when
`ij in E(Q)`.  Let `J subset {1,...,m}`.  Suppose that for each `i in J`
there is a regular induced subgraph `S_i subset V_i` of order `s_i>0` and
degree `r_i`.  Then

```text
S = union_{i in J} S_i
```

is regular in `G` if and only if the quantities

```text
r_i + sum_{j in J, ij in E(Q)} s_j
```

are the same for all `i in J`.

In particular, if `Q[J]` is `d`-regular and the pieces `S_i` all have the
same order `s` and the same internal degree `r`, then `S` is regular of
order `s|J|`.

Proof.  For a vertex `v in S_i`, its degree inside `G[S]` is the sum of its
internal degree inside `S_i` and the sizes of all selected neighboring
modules in the quotient:

```text
deg_{G[S]}(v)=r_i + sum_{j in J, ij in E(Q)} s_j.
```

This expression is independent of the choice of `v in S_i` because `S_i` is
regular.  Therefore the union is regular exactly when the displayed value is
independent of `i`.  If `Q[J]` is `d`-regular and all `s_i=s`, all `r_i=r`,
then the displayed degree is `r+ds` for every `i`.  QED.

This is the precise substitution analogue of the profile-absorption
criterion.  It shows why modular decomposition is not solved merely by the
quotient reduction: one may also need to coordinate regular witnesses inside
several modules so that their internal degrees and quotient-weighted external
degrees balance.

**Corollary 7.3: Ramsey Multiplication Across Large Modules.**  Let
`V(G)=V_1 union ... union V_m` be a partition into modules with quotient
`Q`.  Fix an integer `ell>=1`, and let `B` be the set of indices `i` for
which

```text
|V_i| >= R(ell,ell).
```

Then

```text
reg(G) >= (ell/2) c log |B|
```

for an absolute Ramsey constant `c>0`, whenever `|B|>=2`.  More precisely,
`reg(G) >= ell floor(c log |B|/2)`.

Proof.  For every `i in B`, Ramsey's theorem gives either a clique or an
independent set of order `ell` inside `G[V_i]`.  Mark `i` by one of the two
types that exists, choosing arbitrarily if both exist.  Ramsey's theorem
applied to the quotient graph `Q[B]` gives a clique or independent set
`J_0 subset B` of size at least `c log |B|`.  At least half of the vertices
of `J_0` have the same internal type; let `J` be that same-type subcollection.

For every `i in J`, choose the corresponding homogeneous `ell`-set `S_i` in
`V_i`.  These pieces all have the same order `ell` and the same internal
degree, either `0` or `ell-1`.  Since `J` is still a clique or independent
set in the quotient, `Q[J]` is regular.  Lemma 7.2 therefore makes
`union_{i in J} S_i` a regular induced subgraph of `G`, of order
`ell |J| >= ell floor(c log |B|/2)`.  QED.

Thus a modular-decomposition proof can multiply internal and quotient Ramsey
gains whenever many modules are large.  A hard substitution counterexample
must distribute its mass so that, for every useful `ell`, only few modules
are large enough to force homogeneous `ell`-sets, or else the quotient on
those large modules has already produced the regular witness above.

**Corollary 7.4: Module-Size Tail Constraint In Counterexamples.**  Let `G`
have no regular induced subgraph on at least `k` vertices, and let
`V(G)=V_1 union ... union V_m` be any partition into modules.  There is an
absolute constant `C` such that for every `ell>=1`,

```text
|{i : |V_i| >= R(ell,ell)}| <= exp(C k/ell).
```

Proof.  Let `B={i: |V_i|>=R(ell,ell)}`.  If `|B|>=2`, Corollary 7.3 gives

```text
k > reg(G) >= (c ell/2) log |B|
```

after changing constants to absorb the floor.  Hence

```text
log |B| <= C k/ell
```

for an absolute `C`.  The cases `|B|<2` are absorbed by increasing `C`.
QED.

This tail constraint is still not a proof of the conjecture, because a
counterexample could have a hard prime quotient with many small modules, or a
hierarchy of substitutions whose mass avoids every fixed internal Ramsey
scale.  It does, however, rule out substitution trees with a broad layer of
large modules unless the desired regular subgraph has already appeared.

## Lemma 7A: Low Adjacency Rank Gives A Large Regular Class

Let `A_G` be the adjacency matrix of an `n`-vertex graph `G`, viewed over any
field, and suppose

```text
rank(A_G) = r.
```

Then

```text
reg(G) >= n/2^r.
```

Consequently, if `G` has no regular induced subgraph on at least `k` vertices,
then

```text
rank(A_G) > log_2(n/k)
```

over every field.

Proof.  Choose `r` pivot columns for the row space of `A_G`.  Projection to
these coordinates is injective on the row space: if two row vectors have the
same projected coordinates, their difference is a row-space vector whose pivot
coordinates are all zero, and hence it is the zero vector.

Every row of `A_G` is a `0`-`1` vector, so there are at most `2^r` possible
projections to the pivot coordinates.  Therefore at least `n/2^r` vertices
have identical full adjacency rows.  If `u` and `v` are two distinct vertices
with identical adjacency rows, then comparing the coordinate `u` gives

```text
A_G(u,u)=A_G(v,u).
```

The left side is `0`, while `A_G(v,u)=A_G(u,v)`.  Hence `u` and `v` are
nonadjacent.  Thus a whole row class is an independent set, and is therefore a
regular induced subgraph.  The final assertion is the contrapositive.  QED.

This isolates another easy regime: a counterexample on `n` vertices with
target `k` must have adjacency rank larger than `log_2(n/k)` over every
field.  The bound is not by itself stronger than Ramsey in the hard range, but
it rules out any proof route that tries to hide all structure inside a
low-rank adjacency model.

## Lemma 7B: Low Shifted Adjacency Rank Gives A Large Clique

Let `A_G` be the adjacency matrix of an `n`-vertex graph `G`, viewed over any
field, and suppose

```text
rank(A_G+I) = r.
```

Then

```text
reg(G) >= n/2^r.
```

Consequently, if `G` has no regular induced subgraph on at least `k` vertices,
then

```text
rank(A_G+I) > log_2(n/k)
```

over every field.

Proof.  Apply the pivot-column argument from Lemma 7A to the rows of
`A_G+I`.  Since those rows are also `0`-`1` vectors, at most `2^r` distinct
rows occur, so some row class has size at least `n/2^r`.

If two distinct vertices `u,v` have identical rows in `A_G+I`, compare the
coordinate `u`.  The `u`-row has value `1` at coordinate `u`, while the
`v`-row has value `A_G(v,u)`.  Hence `A_G(u,v)=1`.  Thus every row class of
`A_G+I` is a clique, and is therefore a regular induced subgraph.  The final
assertion is the contrapositive.  QED.

Combining Lemmas 7A and 7B, a hard counterexample must have both `A_G` and
`A_G+I` of rank larger than `log_2(n/k)` over every field.  This is still a
weak condition in the Ramsey-scale range, but it excludes both independent
and clique twin-collapse models by the same linear-algebra certificate.

**Corollary 7C: Hereditary Rank Obstruction In Counterexamples.**  Let `G`
have no regular induced subgraph on at least `k` vertices.  Then for every
vertex set `U` with `u=|U|>=k`, the adjacency matrix `A_U` of `G[U]` satisfies

```text
rank(A_U) > log_2(u/k),
rank(A_U+I) > log_2(u/k)
```

over every field.

Equivalently, every induced subgraph `G[U]` has fewer than `2^r k` vertices
whenever either `rank(A_U)<=r` or `rank(A_U+I)<=r`.

Proof.  Since every regular induced subgraph of `G[U]` is a regular induced
subgraph of `G`, the induced graph `G[U]` also has no regular induced subgraph
on at least `k` vertices.  Apply Lemmas 7A and 7B to `G[U]`.  QED.

This local form is often the useful one: any proposed proof that decomposes a
counterexample into degree buckets, trace classes, pair-role middle graphs, or
ordered representatives must either keep those induced pieces high-rank in
both senses or find the desired regular subgraph inside one piece.

**Corollary 7D: Exact Degree Buckets Are Locally High-Rank Or Small.**  Let
`G` have no regular induced subgraph on at least `k` vertices, and let `B` be
an exact global degree class of size `b>=k`.  Then the adjacency matrix
`A_B` of `G[B]` satisfies

```text
rank(A_B) > log_2(b/k),
rank(A_B+I) > log_2(b/k)
```

over every field.  Equivalently, if either rank is at most `r`, then
`b<2^r k`.

Proof.  This is Corollary 7C applied to the induced subgraph on `B`.  QED.

This is not a replacement for Corollary 28D.2's `2P_h(h-1)`
degree-bucket bound,
but it supplies an independent local obstruction: a large exact-degree bucket
in a counterexample must be a high-rank bounded-spread graph.

**Corollary 7E: Bounded-Spread Low-Bucket-Rank Easy Case.**  Let `G` be an
`n`-vertex graph with no regular induced subgraph on at least `k` vertices.
Suppose the global degrees of `G` take values in a set `D` of size `t`.  Fix a
field and an integer `r`.  If every exact degree bucket `B_d` satisfies

```text
rank(A_{B_d}) <= r        or        rank(A_{B_d}+I) <= r,
```

then

```text
n < t 2^r k.
```

In particular, if the degree spread of `G` is at most `s`, then the same
hypothesis gives

```text
n < (s+1)2^r k.
```

Proof.  By Corollary 7D, every nonempty bucket with either displayed rank at
most `r` has size less than `2^r k`.  Summing over the `t` nonempty degree
values gives the first bound.  If the degree spread is at most `s`, then at
most `s+1` integer degree values occur.  QED.

Thus a bounded-spread proof cannot be completed by reducing all exact degree
buckets to low-rank models.  Any counterexample beyond the displayed bound
must contain a high-rank bucket, in both the adjacency and shifted-adjacency
senses.

The script `EXPERIMENTS/subset_rank_profile.py` calibrates how weak this
obstruction is near the threshold.  On the `14`-vertex add-saturated
threshold-`7` mask `765415324481232608887291903`, the minimum `F_2` ranks of
`A_U` over `u`-vertex induced subgraphs for `u=7,...,14` are

```text
2,2,4,4,6,8,8,10,
```

and the corresponding shifted ranks of `A_U+I` are

```text
3,3,5,5,7,7,9,11.
```

On the delete-saturated mask `88255234986600583676821506`, the respective
rank profiles are

```text
2,4,4,6,8,10,12,14,
3,5,5,7,9,9,11,13.
```

Thus small counterexamples may contain threshold-sized induced pieces of very
low rank; Corollary 7C becomes strong only for pieces whose order is much
larger than `k 2^r`.

The script `EXPERIMENTS/degree_bucket_profile.py` applies the same diagnostics
to exact global degree buckets.  On the `14`-vertex add-saturated
threshold-`7` mask, the largest bucket has degree `9`, size `6`, maximum
regular order `4`, `F_2` ranks `rank(A_B)=4`, `rank(A_B+I)=5`, and maximum
row-difference diameters

```text
global=4, internal=4, external=2.
```

On the delete-saturated mask, the largest bucket has degree `3`, size `8`,
maximum regular order `5`, `F_2` ranks `6` and `7`, and maximum
row-difference diameters

```text
global=6, internal=4, external=4.
```

These buckets are below or just above the threshold, so the rank obstruction
is again only a calibration; larger examples would need the bucket size to
exceed `k 2^r` before Corollary 7D forces a regular `k`-set.  The small
diameters are consistent with Corollary 28D.3, but the ranks show that small
diameter is not by itself a low-rank certificate.

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

The helper `EXPERIMENTS/equitable_partition.py` now has a fixed-mask mode for
this certificate.  On the `14`-vertex threshold-`7` add-saturated mask
`765415324481232608887291903`, color refinement gives `6` cells with largest
cell size `4`, while the true maximum regular induced order is `6`.  On the
delete-saturated mask `88255234986600583676821506`, and on the
`C_reg(1,5)>12` mask `25366485577502803966`, color refinement is discrete
even though their maximum regular induced orders are respectively `6` and
`4`.  Thus this certificate explains only the structured part of the finite
examples and misses regular witnesses in rigid examples.

## Lemma 10A: Automorphism Orbits Are Regular

Let a group `Gamma` act on a graph `G` by automorphisms.  Then every orbit of
this action induces a regular subgraph.  In particular, if `G` has no regular
induced subgraph on at least `k` vertices, then every automorphism orbit of
`G` has size less than `k`.

Proof.  Let `O` be an orbit and let `x,y in O`.  Choose
`gamma in Gamma` with `gamma x=y`.  Because `gamma` is an automorphism and
preserves the orbit `O`, it maps

```text
N_G(x) cap O
```

bijectively onto

```text
N_G(y) cap O.
```

Thus every vertex of `O` has the same number of neighbors inside `O`, so
`G[O]` is regular.  The final assertion is immediate.  QED.

This is a special source of equitable partition cells: automorphism orbits are
equitable, and transitive induced subgraphs are regular.  Therefore highly
symmetric constructions cannot be extremal at scales above the target.

The helper `EXPERIMENTS/automorphism_orbits.py` checks this certificate for
small fixed masks.  On the `14`-vertex threshold-`7` add-saturated mask
`765415324481232608887291903`, the largest automorphism orbit has size `4`.
On the delete-saturated mask `88255234986600583676821506` and on the
`C_reg(1,5)>12` mask `25366485577502803966`, all automorphism orbits are
singletons.  Thus the recorded finite obstructions are not explained by large
symmetry; the first has only small residual symmetry, and the latter two are
rigid under this diagnostic.

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

**Computational Example 11F: Larger Compensated Templates At The Half-Size
Boundary.**  The memory-light verifier `EXPERIMENTS/regular_bitset.py`
extends exact fixed-mask checks beyond the all-subset precomputation range
used by `regular_induced.py`.  In compensated spread-one samples, it verifies
the following two larger masks.

For `m=11`, the graph on `22` vertices with mask

```text
1514445400399818308793001504185320897379013154226396489070190770383185
```

has degree sequence

```text
10^20, 11^2
```

and maximum regular induced order exactly `11`: the command

```text
python3 82/EXPERIMENTS/regular_bitset.py 22 --mask 1514445400399818308793001504185320897379013154226396489070190770383185 --threshold 12
```

reports no regular induced subgraph of order at least `12`, while

```text
python3 82/EXPERIMENTS/regular_bitset.py 22 --mask 1514445400399818308793001504185320897379013154226396489070190770383185 --threshold 11
```

finds an order-`11` witness.

For `m=12`, the graph on `24` vertices with mask

```text
92539845710879666640401066284165863542407620232601075165182118091113678175564578752
```

has degree sequence

```text
11^16, 12^8
```

and maximum regular induced order exactly `12`: the threshold-`13` check is
negative, and the threshold-`12` check finds a witness.  These examples do
not restore the false universal half-size theorem from Example 11C, but they
show that the compensated family oscillates around the half-size boundary in
small samples rather than immediately producing a decreasing ratio.

**Lemma 11G: Deletion Certificate For Spread-One Regularity.**  Let `G` be a
graph whose degrees are all `d` or `d+1`.  Put

```text
epsilon(v)=deg_G(v)-d in {0,1}.
```

For a vertex set `S` and its complement `T=V(G)\S`, the induced graph `G[S]`
is regular if and only if the quantity

```text
deg_G(v,T)-epsilon(v)
```

is constant over all `v in S`.

Proof.  For `v in S`,

```text
deg_{G[S]}(v) = deg_G(v)-deg_G(v,T)
              = d + epsilon(v) - deg_G(v,T).
```

The left-hand side is independent of `v in S` exactly when
`deg_G(v,T)-epsilon(v)` is independent of `v in S`.  QED.

Thus the spread-one problem can be phrased as a deletion-trace problem: find a
small deletion set `T` such that all surviving low-degree vertices have one
common trace size into `T`, while all surviving high-degree vertices have
trace size larger by one.  This is the bounded-spread analogue of Lemma 12's
minimal repeated-degree obstruction, but now the target is constructive rather
than obstruction-minimal.

The helper `EXPERIMENTS/spread_one_deletion_certificate.py` displays this
certificate for fixed witnesses.  On Example 11C, it finds a maximum
order-`5` witness and verifies that the values `deg(v,T)-epsilon(v)` are
constant on the witness:

```text
python3 82/EXPERIMENTS/spread_one_deletion_certificate.py 12 --mask 72400984189589100935
```

This reformulation suggests a concrete route for spread-one graphs: prove
that every two-degree graph has an offset-trace deletion certificate with
`|T|=n-o(n/log n)`, or even with `|S|=omega(log n)`.  The compensated examples
show that `T` need not be small; the useful question is whether one can always
make the surviving trace-equalized set substantially larger than the Ramsey
scale.

**Lemma 11H: Bounded-Spread Deletion And Modular Certificates.**  Let `G` be
a graph, let `d` be an integer, and write

```text
deg_G(v)=d+epsilon(v)
```

on a vertex set `S`, with no restriction on the integer offsets
`epsilon(v)`.  Put `T=V(G)\S`.  Then:

1. `G[S]` is regular if and only if `deg_G(v,T)-epsilon(v)` is constant over
   `v in S`;
2. for a positive integer `q`, the induced graph `G[S]` is `q`-modular if and
   only if `deg_G(v,T)-epsilon(v)` is constant modulo `q` over `v in S`.

Consequently, if the modular condition in (2) holds and `|S|<=q+1`, then
`G[S]` is regular.

Proof.  For every `v in S`,

```text
deg_{G[S]}(v)=deg_G(v)-deg_G(v,T)
             =d+epsilon(v)-deg_G(v,T).
```

Equality of these induced degrees is exactly equality of
`deg_G(v,T)-epsilon(v)`, and congruence modulo `q` is exactly congruence of
the same quantities modulo `q`.  The final assertion is Lemma 2.  QED.

This is the common algebra behind the bounded-spread and modular programs.
The deletion set `T` plays the role of an absorber whose trace vector cancels
the ambient degree offsets on the surviving vertices.  For exact regularity
the cancellation is over the integers; for dyadic lifting it is cancellation
modulo the current modulus.

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

## Lemma 14A.5: One-Trace Regular Merge

Let `A` be a vertex set in `G`, let `T subset A`, and let

```text
C_T = {v in V(G)\A : N_G(v) cap A = T}.
```

Suppose `B subset C_T` induces an `r`-regular graph on `b` vertices.

1. If `X subset T` induces a `d`-regular graph on `x` vertices and

```text
x-d = b-r,
```

then `G[B union X]` is regular on `b+x` vertices.

2. If `X subset A\T` induces an `r`-regular graph on `x` vertices, then
   `G[B union X]` is regular on `b+x` vertices.

Proof.  In the first case, every vertex of `B` is adjacent to every vertex of
`X`, so its degree in `G[B union X]` is `r+x`.  Every vertex of `X` has
degree `d+b`.  The displayed equality is exactly `r+x=d+b`, so the union is
regular.

In the second case, there are no edges between `B` and `X`, so vertices of
`B` and vertices of `X` keep their internal degrees.  Both internal degrees
are `r`, and the union is regular.  QED.

The independent-base Lemma 14A.1 is the special case of (1) where `X` is an
independent set of order `b-r`.  The clique-base Lemma 14A.2 is the special
case of (2) applied with a clique `A` and an `(r+1)`-vertex clique inside
`A\T`.  Lemma 14A.5 is the usable recursive form: a high-multiplicity trace
class is dangerous not only when the base contains a large homogeneous set,
but whenever the trace side contains a regular subgraph with matching
degree-deficit, or the nontrace side contains a regular subgraph of the same
degree.

**Corollary 14A.6: One-Trace Merge Restrictions In Counterexamples.**  Let
`G` have no regular induced subgraph on at least `k` vertices.  In the setting
of Lemma 14A.5:

1. If `X subset T` is `d`-regular on `x` vertices and

```text
x-d=b-r,
```

then `b+x<k`.

2. If `X subset A\T` is `r`-regular on `x` vertices, then `b+x<k`.

Proof.  Otherwise Lemma 14A.5 gives a regular induced subgraph on at least
`k` vertices.  QED.

These restrictions are still not enough by themselves, because they require
a matching degree or degree-deficit inside `T` or `A\T`, not just a large
regular subgraph somewhere in the base.  They do, however, identify the exact
degree data that a trace-class recursion must preserve.

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

## Lemma 14B.1: Large Traces Have A Stronger Independent-Set Cap

Let `G` have no regular induced subgraph on at least `k` vertices, and let
`A` be a maximal independent set of size `h<k`.  For nonempty
`T subset A`, write `j=|T|` and define `C_T` as in Lemma 14B.  Then
`G[C_T]` has no clique of order `k-1` and no independent set of order

```text
tau(j)=
  k-h+j             if j < ceil(k/2),
  ceil(k/2)         if j >= ceil(k/2).
```

Consequently,

```text
|V(G)| <= h + sum_{j=1}^{h} binom(h,j) ( R(k-1,tau(j)) - 1 ).
```

Proof.  The clique exclusion is the same as in Lemma 14B: if
`Q subset C_T` is a clique of order `k-1`, then `Q union {a}` is a clique of
order `k` for any `a in T`.

The independent-set exclusion from Lemma 14B also still applies: an
independent set `B subset C_T` of order `k-h+j`, together with `A\T`, is an
independent set of order `k`.

There is an additional exclusion when `j>=ceil(k/2)`.  If
`B subset C_T` is independent of order `ceil(k/2)`, choose
`X subset T` with `|X|=|B|`.  Since `A` is independent, `X` is independent;
since every vertex of `B` has trace `T`, the graph on `B union X` is
`K_{|B|,|B|}`, which is regular on at least `k` vertices.  This is impossible.

Thus the forbidden independent-set threshold is `k-h+j` for small traces and
`ceil(k/2)` for large traces.  Summing over all nonempty trace classes gives
the displayed bound.  QED.

This is a genuine improvement over Lemma 14B only for large traces
`|T|>=ceil(k/2)`.  It still leaves exponential-size sums in the hardest
linear-homogeneous regime, but it shows that one-trace amplification already
removes the weakest Ramsey terms from the maximal-independent-set trace
decomposition.

The script `EXPERIMENTS/trace_ramsey_bound.py` compares Lemma 14B and
Lemma 14B.1 using the binomial Erdos--Szekeres proxy
`R(a,b)<=binom(a+b-2,a-1)`.  For example, at `(k,h)=(80,70)`, the proxy
improves from `2^191.61` to `2^183.82`.  This is a real constant-factor
exponent saving in that range, but it is still exponential in `k`.

**Corollary 14B.2: Maximal Clique Version.**  Let `G` have no regular induced
subgraph on at least `k` vertices, and let `A` be a maximal clique of size
`h<k`.  For each nonempty `T subset A`, put

```text
C_T = {v in V(G)\A : (A\N_G(v)) cap A = T},
```

so `T` is the set of non-neighbors of `v` inside the clique `A`.  With
`tau(j)` as in Lemma 14B.1,

```text
|V(G)| <= h + sum_{j=1}^{h} binom(h,j) ( R(k-1,tau(j)) - 1 ).
```

Proof.  Apply Lemma 14B.1 to `complement(G)`.  Regular induced subgraphs are
preserved by complementation, and the maximal clique `A` in `G` is a maximal
independent set in `complement(G)`.  Traces in the complement are exactly
non-neighborhoods inside the clique in `G`.  QED.

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

## Lemma 18D: Bounded-Support Trace Recursion

Let `G` be a graph with no regular induced subgraph on at least `k` vertices.
Let `H` be a minimal repeated-degree host as in Lemma 12, with repeated class
`A={a_1,...,a_k}` and outside set `B`.  Encode outside vertices by the
signed-indicator trace differences from Lemma 12A, relative to `a_k`.

Suppose every outside trace difference has support size at most `s`.  Then

```text
|B| < 2 ( sum_{i=1}^s binom(k-1,i) ) G(k).
```

Proof.  By Lemma 12A, every trace difference is one of

```text
1_S       or       -1_S
```

where `emptyset != S subset {1,...,k-1}`.  Under the support bound
`|S|<=s`, the number of possible signed trace-difference types is at most

```text
2 sum_{i=1}^s binom(k-1,i).
```

For any fixed type `tau`, let `C_tau` be the set of vertices of `B` with that
trace difference.  If `|C_tau|>=G(k)`, then the induced graph `G[C_tau]`
contains a regular induced subgraph on at least `k` vertices, by the
definition of `G(k)`.  This is also an induced regular subgraph of `G`,
contradicting the hypothesis.  Hence every type class has size less than
`G(k)`, and summing over the possible types gives the displayed bound.  QED.

This lemma is intentionally recursive and therefore not a proof of the main
conjecture.  Its value is diagnostic: for `s=o(k/log k)`, the number of
support-`<=s` trace types is `2^{o(k)}`, so a support-restricted obstruction
larger than `2^{o(k)}G(k)` must already contain a hard graph inside one
identical-trace class.  The support-three constructions in Examples 18B and
18C therefore show that small support, imbalance control, and graphical
compensation do not suffice unless one also uses the induced graph structure
inside high-multiplicity trace classes.

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

**Lemma 22A: Matching Conflict Graphs Are Dense.**  Let `G` have no regular
induced subgraph on at least `k` vertices, and put

```text
r=ceil(k/2).
```

Let `M` be any matching in `G`, with `m` edges.  Define the conflict graph
`C_M` on the edges of `M` by joining two matching edges when there is at least
one edge of `G` between their endpoint pairs.  Then

```text
alpha(C_M) < r
```

and therefore

```text
e(C_M) > (m/2)(m/r - 1).
```

The same statement holds for any matching in the complement of `G`, with
conflicts measured in the complement.

Proof.  If `C_M` had an independent set of `r` matching edges, then those
`r` edges would have no cross edges between them in `G`; they would induce an
induced matching of size `r`, hence a `1`-regular induced subgraph on
`2r>=k` vertices.  This contradicts Lemma 22.

For the edge lower bound, let `d_bar=2e(C_M)/m` be the average degree of the
conflict graph.  Caro--Wei gives

```text
alpha(C_M) >= m/(d_bar+1).
```

Since `alpha(C_M)<r`, we have `d_bar>m/r-1`, which is the displayed bound on
`e(C_M)`.

Applying the same argument in the complement of `G` proves the complement
statement, because an induced matching in the complement gives a regular
induced subgraph in `G` after complementing degrees.  QED.

Thus large ordinary matchings in a counterexample must be highly entangled:
most matched-edge pairs must have cross edges once the matching size is much
larger than `k`.  This is stronger than merely excluding one induced matching,
but still not enough by itself to beat the exponential Ramsey-scale matching
pattern argument.

The diagnostic script `EXPERIMENTS/matching_conflict_profile.py` computes this
conflict graph for fixed masks.  On the `14`-vertex threshold-`7`
add-saturated mask `765415324481232608887291903`, a maximum matching in `G`
has `7` edges and complete conflict graph (`21` conflict edges, independence
`1`), while a maximum matching in the complement has `6` edges, `7` conflict
edges, and conflict independence `2`.  On the delete-saturated mask
`88255234986600583676821506`, the corresponding graph/complement conflict
independences are `3` and `1`.  Since `ceil(7/2)=4`, these finite examples
fit the lemma but also show that the density lower bound can be quite far
from tight near the target size.

**Corollary 22B: Large Matchings Are Densely Conflicted.**  Let `G` be an
`n`-vertex graph with no regular induced subgraph on at least `k` vertices,
and put `r=ceil(k/2)`.  Then both `G` and its complement contain matchings of
size

```text
m > (n-k)/2.
```

For any maximum matching `M` in either graph, the corresponding conflict graph
has

```text
e(C_M) > (m/2)(m/r - 1).
```

In particular, if `n/k -> infinity`, then these conflict graphs have average
degree at least `(1+o(1)) n/k`.

Proof.  Let `M` be a maximal matching in `G`, and let `U` be the vertices not
covered by `M`.  If two vertices of `U` were adjacent, the matching would not
be maximal.  Thus `U` is independent.  Since an independent set of order `k`
is a forbidden regular induced subgraph, `|U|<k`, and so

```text
|M|=(n-|U|)/2 > (n-k)/2.
```

The same argument in the complement gives a matching of this size there,
because a clique of order `k` in `G` is also forbidden.  Applying Lemma 22A to
a maximum matching gives the displayed conflict-edge bound.  The final
average-degree statement uses `m>(n-k)/2` and `r=ceil(k/2)`.  QED.

This corollary is still a density statement about an auxiliary graph, not a
direct regular-subgraph construction.  Its value is to isolate a concrete
place where a future proof could try to exploit more than the mere absence of
an induced matching: for large counterexamples, every maximum matching in both
`G` and its complement is forced into a conflict graph with growing average
degree.

**Lemma 22C: Uniform Matching Patterns Need Not Give More Than One Endpoint
Per Edge.**  For every `q>=1`, there is a graph `H_q` with a matching of size
`q` such that the cross-edge pattern between every two matching edges is the
same, but

```text
reg(H_q)=q.
```

Proof.  Let `A={a_1,...,a_q}` be a clique, let `B={b_1,...,b_q}` be an
independent set, and add exactly the matching edges `a_i b_i` between `A` and
`B`.  The edges `a_i b_i` form a matching of size `q`.  For any two matching
edges `a_i b_i` and `a_j b_j`, the only cross edge among their four endpoints
is `a_i a_j`; hence the matching has a single cross-edge pattern.

The graph is split, with clique part `A` and independent part `B`.  By
Lemma 0B, every regular induced subgraph of a split graph is either a clique
or an independent set.  The largest clique has size `q`, namely `A`, and the
largest independent set also has size `q`, for example `B`.  Therefore
`reg(H_q)=q`.  QED.

Thus a proof that first Ramsey-extracts a matching whose pairwise cross-edge
pattern is constant cannot by that fact alone force more than `q` regular
vertices from `q` matching edges.  The helper
`EXPERIMENTS/matching_pattern_profile.py` enumerates the `16` uniform
two-edge cross patterns; for `q=8` it reports minimum maximum regular order
`8`, attained by patterns `1,2,4,8`.  The matching route must therefore use
additional structure of the conflict graph or of the ambient graph, not just a
monochromatic cross-pattern submatching.

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

**Corollary 26A: Bounded Row-Diameter Graphs Are Linearly Easy.**  Let `G`
be an `n`-vertex graph.  Suppose that for every distinct pair `u,v`,

```text
|(N(u) triangle N(v))\{u,v}| <= D.
```

Then

```text
reg(G) >= (n-1)/(4(2D+1)).
```

In particular, if the row diameter is at most `2`, then

```text
reg(G) >= (n-1)/20.
```

Proof.  The hypothesis gives `bar sigma<=D`.  Substitute this into the
clique-or-independent-set lower bound from Lemma 26.  QED.

This is the positive counterpart to Corollary 28D.3.  Small row diameter
inside a whole induced graph is not a hard case at all: it gives a linear
homogeneous, hence regular, induced subgraph.  The exact-degree bucket
obstruction is subtler because Corollary 28D.3 controls rows of bucket
vertices in the ambient graph, while the induced bucket itself may still
interact with a large and varying exterior.

**Lemma 26B: Local Row-Ball Homogeneous Set.**  Let `v` be a vertex of `G`,
and let `U subset V(G)\{v}` be such that

```text
|(N(u) triangle N(v))\{u,v}| <= D       for every u in U.
```

Then `G[U]` contains a clique or independent set, and hence a regular induced
subgraph, of order at least

```text
|U| / (2(D+1)).
```

If, in addition, all vertices of `U` are either adjacent to `v` or all
nonadjacent to `v`, then the lower bound improves to

```text
|U|/(D+1).
```

Proof.  Partition

```text
U_A=U cap N(v),       U_B=U \ N(v).
```

For `u in U_A`, every nonneighbor of `u` inside `U_A` contributes to
`(N(u) triangle N(v))\{u,v}`, because `v` is adjacent to all of `U_A`.
Thus the complement of `G[U_A]` has maximum degree at most `D`, and `G[U_A]`
contains a clique of order at least `|U_A|/(D+1)`.

For `u in U_B`, every neighbor of `u` inside `U_B` contributes to the same
symmetric difference, because `v` is adjacent to none of `U_B`.  Thus
`G[U_B]` has maximum degree at most `D`, and it contains an independent set
of order at least `|U_B|/(D+1)`.

One of `U_A,U_B` has size at least `|U|/2`, giving the first bound.  If all
of `U` lies in one side, the factor `2` is not needed.  QED.

Lemma 26 is the average form of this local cleaning step: it finds a vertex
`v` with a large row-ball `U` by averaging and Markov's inequality.  The local
form can be applied directly when a proof route produces many vertices whose
rows are close to one reference row.

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

The broader signature scan

```text
python3 82/EXPERIMENTS/pair_role_signature.py 12 --mask 72400984189589100935
```

inspects all `48` maximum regular witnesses and reports
`min_pair_nonempty_roles=3`.  Thus, in this graph, every maximum witness needs
at least three pair roles; the two-role balanced extension cannot recover a
maximum witness by choosing a different pair.

**Example 27E: Four Pair Roles Can Be Unavoidable In A Regular Witness.**
Let `p>=13` be a prime with `p congruent 1 mod 4`, and let `P_p` be the Paley
graph on `F_p`: two vertices are adjacent when their difference is a nonzero
quadratic residue.  Then `P_p` is regular, but for every pair of vertices in
the full regular witness `V(P_p)`, all four pair roles `A,B,C,E` from
Lemma 27C are nonempty.

Proof.  Let `chi` be the quadratic character modulo `p`, with `chi(0)=0`.
Because `p congruent 1 mod 4`, `chi(-1)=1`, so the Paley graph is undirected
and every vertex has degree

```text
d=(p-1)/2.
```

By translation, it is enough to count common neighbors of `0` and `a != 0`.
For `x notin {0,a}`, the vertex `x` is adjacent to both if and only if
`chi(x)=chi(x-a)=1`.  Hence the number `N(a)` of common neighbors is

```text
N(a)=1/4 sum_{x notin {0,a}} (1+chi(x))(1+chi(x-a)).
```

The four sums are

```text
sum 1 = p-2,
sum_{x notin {0,a}} chi(x) = -chi(a),
sum_{x notin {0,a}} chi(x-a) = -chi(-a)=-chi(a),
sum_x chi(x(x-a)) = -1.
```

The last identity is the standard quadratic character sum for a nonconstant
quadratic with distinct roots.  Therefore

```text
N(a)=(p-3-2chi(a))/4.
```

For an adjacent pair this gives

```text
|C|=(p-5)/4,       |A|=|B|=d-1-|C|=(p-1)/4,
|E|=p-2-|A|-|B|-|C|=(p-1)/4.
```

For a nonadjacent pair it gives

```text
|C|=(p-1)/4,       |A|=|B|=d-|C|=(p-1)/4,
|E|=p-2-|A|-|B|-|C|=(p-5)/4.
```

All four quantities are positive for `p>=13`.  Thus no pair in the full
regular witness has fewer than four nonempty roles.  QED.

For `p=13`, the verification command

```text
python3 82/EXPERIMENTS/pair_role_signature.py 13 --paley-prime 13
```

reports `max_regular_order=13` and `min_pair_nonempty_roles=4`.  Thus any
proof that starts from an already-found regular witness and then tries to
select a pair with at most three nonempty roles is false.  Pair-role
absorption must allow all four roles, or it must find a different witness.

## Lemma 27F: Edge-Extremal Counterexamples Have Two-Defect Witnesses

Fix `k`, and let `G` be a graph with no regular induced subgraph on at least
`k` vertices.

1. Suppose `G` is edge-maximal with this property: adding any missing edge to
   `G` creates a regular induced subgraph on at least `k` vertices.  Then for
   every nonedge `uv` of `G`, there is a set `S` containing `u,v`, with
   `|S|>=k`, such that in `G[S]` the vertices `u` and `v` have one common
   degree `D-1`, while every vertex of `S\{u,v}` has degree `D`.

2. Suppose `G` is edge-minimal with this property: deleting any existing edge
   from `G` creates a regular induced subgraph on at least `k` vertices.  Then
   for every edge `uv` of `G`, there is a set `S` containing `u,v`, with
   `|S|>=k`, such that in `G[S]` the vertices `u` and `v` have one common
   degree `D+1`, while every vertex of `S\{u,v}` has degree `D`.

Proof.  For (1), let `G^+=G+uv`.  By edge-maximality, `G^+` contains a
regular induced subgraph `G^+[S]` of order at least `k`.  If `S` did not
contain both `u` and `v`, then `G[S]=G^+[S]`, giving a forbidden regular
induced subgraph in `G`.  Thus `u,v in S`.  Let the common degree in
`G^+[S]` be `D`.  Passing from `G^+[S]` to `G[S]` deletes exactly the edge
`uv`, so the degrees of `u` and `v` drop by one and all other degrees are
unchanged.

The proof of (2) is identical with `G^-=G-uv`: the regular witness in `G^-`
must contain both endpoints, and restoring the edge raises only the degrees
of `u` and `v` by one.  QED.

In the edge-maximal case, the witness is a shifted version of the pair-role
equations from Lemma 27C.  With respect to the nonedge `uv`, write
`S\{u,v}=X union Y union Z union W` for the one-sided, common-neighbor, and
common-nonneighbor roles.  The equality of the two deficient endpoint degrees
forces `|X|=|Y|`; if their common degree is `D-1`, then the middle vertices
must have internal degrees

```text
D-1 on X union Y,       D-2 on Z,       D on W.
```

Thus an edge-maximal counterexample contains a large two-defect
profile-absorption witness at every missing edge.  The edge-minimal case gives
the complementary surplus version at every present edge.  This reframes
edge-extremal counterexamples as graphs saturated with near-regular induced
subgraphs, rather than as graphs with no regularity structure at all.

The script `EXPERIMENTS/edge_perturbation_witness.py` inspects this mechanism
for fixed masks.  On the `12`-vertex compensated template from Example 11C,
which has maximum regular induced order `5`, the threshold-`6` checks report
that `17` of the `33` missing-edge additions and `17` of the `33` edge
deletions create a regular induced subgraph on at least `6` vertices; every
reported witness contains the perturbed pair.  The commands are

```text
python3 82/EXPERIMENTS/edge_perturbation_witness.py 12 --mask 72400984189589100935 --threshold 6 --mode add
python3 82/EXPERIMENTS/edge_perturbation_witness.py 12 --mask 72400984189589100935 --threshold 6 --mode delete
```

This graph is not asserted to be edge-extremal; the computation is only a
sanity check that the two-defect witnesses appear naturally near small
bounded-spread examples.

**Computational Example 27G: Saturated Twelve-Vertex Counterexamples.**  The
script `EXPERIMENTS/edge_saturate.py` greedily turns a fixed graph with no
regular induced `k`-set into an edge-maximal or edge-minimal graph with the
same property.

Starting from the `12`-vertex compensated template of Example 11C and using
threshold `k=6`, edge-addition saturation produces the mask

```text
72413377920641400783.
```

It has no regular induced subgraph of order at least `6`; all `17` remaining
missing-edge additions create one, and every reported witness contains the
added pair.  The verification commands are

```text
python3 82/EXPERIMENTS/edge_saturate.py 12 --mask 72400984189589100935 --threshold 6 --mode add
python3 82/EXPERIMENTS/regular_bitset.py 12 --mask 72413377920641400783 --threshold 6
python3 82/EXPERIMENTS/edge_perturbation_witness.py 12 --mask 72413377920641400783 --threshold 6 --mode add
```

Edge-deletion saturation from the same starting graph produces the mask

```text
56205204850483501447.
```

It also has no regular induced subgraph of order at least `6`; all `19`
remaining edge deletions create one, again with witnesses containing the
deleted pair.  Thus both edge-extremal forms in Lemma 27F occur in small
examples.

The same saturation check extends to the spread-one `14`-vertex threshold-`7`
mask

```text
146294004578047919044267715.
```

Greedy edge-addition saturation gives

```text
765415324481232608887291903,
```

with no regular induced subgraph of order at least `7`; all `18` remaining
missing-edge additions create such a witness, and all reported witnesses
contain the added pair.  Greedy edge-deletion saturation gives

```text
88255234986600583676821506,
```

with no regular induced subgraph of order at least `7`; all `19` remaining
edge deletions create such a witness, again containing the deleted pair.  The
verification commands are

```text
python3 82/EXPERIMENTS/edge_saturate.py 14 \
  --mask 146294004578047919044267715 --threshold 7 --mode add
python3 82/EXPERIMENTS/edge_saturate.py 14 \
  --mask 146294004578047919044267715 --threshold 7 --mode delete
python3 82/EXPERIMENTS/regular_bitset.py 14 \
  --mask 765415324481232608887291903 --threshold 7
python3 82/EXPERIMENTS/regular_bitset.py 14 \
  --mask 88255234986600583676821506 --threshold 7
python3 82/EXPERIMENTS/edge_perturbation_witness.py 14 \
  --mask 765415324481232608887291903 --threshold 7 --mode add
python3 82/EXPERIMENTS/edge_perturbation_witness.py 14 \
  --mask 88255234986600583676821506 --threshold 7 --mode delete
```

The perturbation script now also reports witness-size histograms.  For these
two saturated masks the add-saturated witnesses have order histogram
`7:17,8:1`, and the delete-saturated witnesses have order histogram
`7:12,8:7`.

## Lemma 27H: Pair-Role Equations For Two-Defect Witnesses

Let `u,v` be two vertices in a graph `G`, and put `delta=1` if `uv in E(G)`
and `delta=0` otherwise.  Let `M` be disjoint from `{u,v}` and partition `M`
into four pair roles

```text
X=N(u)\N(v),              Y=N(v)\N(u),
Z=N(u) cap N(v),          W=V(G)\({u,v} union N(u) union N(v)),
```

intersected with `M`.  Let `tau` be one of `-1,0,1`.  Then the induced graph
on `{u,v} union M` has degree `D+tau` at both `u` and `v`, and degree `D` at
every vertex of `M`, if and only if

```text
|X|=|Y|,
D=delta+|X|+|Z|-tau,
deg_M(x)=D-1       for x in X union Y,
deg_M(z)=D-2       for z in Z,
deg_M(w)=D         for w in W.
```

Proof.  The degrees of `u` and `v` in the full induced graph are

```text
delta+|X|+|Z|,       delta+|Y|+|Z|,
```

respectively.  They are equal exactly when `|X|=|Y|`, and requiring this
common value to be `D+tau` gives the displayed formula for `D`.

Every vertex in `X union Y` is adjacent to exactly one of `u,v`; every vertex
in `Z` is adjacent to both; every vertex in `W` is adjacent to neither.
Therefore a middle vertex has total degree `D` exactly when its degree inside
`M` is respectively `D-1`, `D-2`, or `D`.  QED.

The case `tau=0` is Lemma 27C.  The case `tau=-1` is the deficient endpoint
form produced by adding a missing edge to an edge-maximal counterexample in
Lemma 27F.  The case `tau=1` is the surplus endpoint form produced by
deleting an edge from an edge-minimal counterexample.  The script
`EXPERIMENTS/pair_defect_witness.py` checks these equations for fixed
witnesses.

For example, in the add-saturated mask `72413377920641400783`, adding the
missing edge `0-5` creates a regular `6`-vertex witness.  Before adding the
edge, the witness

```text
{0,1,4,5,6,9}
```

has endpoint degrees `3,3` at `0,5` and middle degrees all `4`, so
`tau=-1`.  In the delete-saturated mask `56205204850483501447`, deleting the
edge `0-1` creates a regular witness; before deletion, the witness

```text
{0,1,6,8,10,11}
```

has endpoint degrees `2,2` and middle degrees all `1`, so `tau=1`.  In both
cases `pair_defect_witness.py` verifies the displayed pair-role equations.

**Corollary 27I: Large Two-Defect Witnesses Are Medium-Degree.**  Let `G`
have no regular induced subgraph on at least `k` vertices.  Suppose
`S` has order `m>=k` and satisfies the conclusion of Lemma 27H for some
`tau in {-1,0,1}`: two distinguished vertices have degree `D+tau` in `G[S]`,
and all other vertices have degree `D`.  Then

```text
D + 2tau/m + 1 > m/k,
m - D - 2tau/m > m/k.
```

In particular, if `m/k -> infinity`, then the middle degree `D` is neither
`o(m/k)` nor `m-o(m/k)`.

Proof.  The average degree of `G[S]` is

```text
bar d = D + 2tau/m.
```

Since `G[S]` has no independent set of order `k`, the Caro--Wei bound gives

```text
k > alpha(G[S]) >= m/(bar d+1),
```

which is the first inequality.  Applying the same argument to
`complement(G[S])`, whose average degree is `m-1-bar d`, and using that a
clique of order `k` in `G[S]` is also a forbidden regular induced subgraph,
gives

```text
k > alpha(complement(G[S]))
  >= m/(m-bar d),
```

which is the second inequality.  QED.

Thus edge-extremal saturation cannot be exploited only through very sparse or
very dense defect witnesses: any witness substantially larger than the target
order is automatically in the same medium-density regime that appears in the
bounded-spread and variance routes.

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

**Lemma 28B: The Two Balanced Pair Parameters Are Complement-Dual.**  For
every `h>=3`,

```text
P_h^+ = P_h^-.
```

Proof.  Put `r=ceil((h-2)/2)`.  We show `P_h^- <= P_h^+`; the reverse
inequality is identical.  Let `M=P_h^+`, and let `H` be any graph whose vertex
set is the disjoint union of two marked sets `A,B` of size `M`.  Apply the
definition of `P_h^+` to the complement graph `bar H`, with the same marked
sets.  If `bar H` contains a regular induced subgraph on at least `h`
vertices, then its complement inside the same vertex set is a regular induced
subgraph of `H` on the same order.  Otherwise there are sets
`X subset A`, `Y subset B`, with `|X|=|Y|=r`, such that
`bar H[X union Y]` is `r`-regular.  Since `|X union Y|=2r`, the graph
`H[X union Y]` is

```text
(2r-1-r) = r-1
```

regular.  This is exactly the second alternative in the definition of
`P_h^-`.  Hence `P_h^- <= P_h^+`, and complementing again gives equality.
QED.

Thus the local pair-difference problem has only one parameter.  We may write
`P_h` for this common value when no confusion is possible.  The unresolved
quantitative target is to prove `P_h=2^{o(h)}` or to replace `P_h` by an even
more efficient non-Ramsey extraction from the two one-sided difference sets.

**Computational Example 28C: Small Balanced-Pair Obstructions.**  The script
`EXPERIMENTS/balanced_pair_parameter_search.py` searches marked two-part
graphs for the obstruction in the definition of `P_h`.  It found the
following exact certificates.

For `h=6`, `r=2`, and marked side size `M=6`, the mask

```text
1680212686667006004
```

has no regular induced subgraph on at least `6` vertices and has no choice
`X subset A`, `Y subset B`, `|X|=|Y|=2`, for which `G[X union Y]` is
`2`-regular.  Thus `P_6^+>6`, and by Lemma 28B also `P_6>6`.  The fixed-mask
verification command is

```text
python3 82/EXPERIMENTS/balanced_pair_parameter_search.py --h 6 --m 6 --mode plus --mask 1680212686667006004
```

The smaller side-size `M=5` obstruction is also visible in both
complement-dual modes.  For example, the masks

```text
10189312835074
9980350930911
```

certify respectively the `2`-regular and `1`-regular middle obstructions at
`h=6, M=5`.

For `h=7`, `r=3`, and `M=7`, the mask

```text
1274636503928019582602515941
```

has no regular induced subgraph on at least `7` vertices and no balanced
`3`-regular middle graph, giving `P_7>7`.  The fixed-mask verification is

```text
python3 82/EXPERIMENTS/balanced_pair_parameter_search.py --h 7 --m 7 --mode plus --mask 1274636503928019582602515941
```

These examples are small, but they calibrate the pair route: the desired
local theorem cannot be a trivial one-sided pigeonhole statement.  A short
hill-climb search at `h=6, M=8` found no obstruction, but this is only a
calibration run rather than evidence for the exact value of `P_6`.

**Lemma 28D: The Pair Parameter Controls One-Sided Differences.**  Let
`h>=3`, and let `P=P_h` be the common balanced pair parameter from
Lemma 28B.  If `G` has no regular induced subgraph on at least `h` vertices,
then for every pair `u,v`, with

```text
A=N(u)\N(v),       B=N(v)\N(u),
```

one has

```text
min(|A|,|B|) < P.
```

Consequently,

```text
|(N(u) triangle N(v))\{u,v}| < 2P + |deg_G(u)-deg_G(v)|.
```

Proof.  Suppose first that `uv` is an edge and that both `A` and `B` have
size at least `P`.  Choose marked subsets `A_0 subset A`, `B_0 subset B` of
size `P`.  By the definition of `P=P_h^+`, the induced graph on
`A_0 union B_0` either contains a regular induced subgraph on at least `h`
vertices, impossible in `G`, or contains balanced sets `X subset A_0`,
`Y subset B_0` with `|X|=|Y|=r=ceil((h-2)/2)` such that
`G[X union Y]` is `r`-regular.  Lemma 27A then makes
`{u,v} union X union Y` regular on `2r+2>=h` vertices, again impossible.

If `uv` is a nonedge, the same argument uses `P=P_h^-` and the
`(r-1)`-regular middle alternative.  Lemma 28B identifies the two parameters.
Thus `min(|A|,|B|)<P` in all cases.

Finally

```text
|(N(u) triangle N(v))\{u,v}| = |A|+|B|
                              = 2 min(|A|,|B|)
                                + ||A|-|B||,
```

and `||A|-|B||=|deg_G(u)-deg_G(v)|`, since the possible edge `uv` contributes
equally to the two degrees.  QED.

**Corollary 28D.1: Linear Bounded-Spread Bound From The Pair Parameter.**
Let `h>=3`, and put `P=P_h`.  Let `G` be an `n`-vertex graph with degree
spread at most `s`.  If `G` has no regular induced subgraph on at least `h`
vertices, then

```text
n <= 8h(2P+s+1/2)+1.
```

Proof.  If `n<h`, the displayed inequality is immediate because `P>=1` and
`h>=3`.  Assume `n>=h`.  By Lemma 28D, every pair of vertices satisfies

```text
sigma(u,v)=|(N(u) triangle N(v))\{u,v}|
          < 2P+|deg_G(u)-deg_G(v)|
          <= 2P+s.
```

Thus the average `bar sigma` from Lemma 26 is also less than `2P+s`.
Lemma 26, applied to a graph with no regular induced subgraph on `h`
vertices, gives

```text
bar sigma >= (n-1)/(8h)-1/2.
```

Combining the last two inequalities gives

```text
(n-1)/(8h)-1/2 < 2P+s,
```

which implies the displayed bound after harmlessly replacing the strict
inequality by a non-strict one.  QED.

**Corollary 28D.2: Exact Degree Classes Are Small.**  Let `h>=3`, put
`P=P_h`, and let `G` be a graph with no regular induced subgraph on at least
`h` vertices.  If `U` is a set of vertices all having the same degree in
`G`, then

```text
|U| <= 1+(2P-1)(h-2) <= 2P(h-1).
```

Proof.  If `|U|<=1`, this is immediate.  Fix `v in U`, and put
`U'=U\{v}`.  Partition

```text
A=U' cap N(v),        B=U'\N(v).
```

For every `u in U'`, the two one-sided differences

```text
N_G(u)\N_G(v),        N_G(v)\N_G(u)
```

have the same size, because `deg_G(u)=deg_G(v)`.  Lemma 28D says their common
size is less than `P`.

If `u in A`, then `u in N_G(v)\N_G(u)`.  Every nonneighbor of `u` inside `A`
also lies in `N_G(v)\N_G(u)`.  Hence, for `P=1`, the set `A` is empty; for
`P>=2`, the complement of `G[A]` has maximum degree at most `P-2`.  Greedily
coloring this complement with `P-1` colors shows that, since `G` has no
clique of order `h` and every clique of order `h-1` in `A` would extend with
`v` to a clique of order `h`,

```text
|A| <= (P-1)(h-2).
```

If `u in B`, then every neighbor of `u` inside `B` lies in
`N_G(u)\N_G(v)`.  Thus `G[B]` has maximum degree at most `P-1`.  Greedily
coloring `G[B]` with `P` colors shows that, since `G` has no independent set
of order `h` and every independent set of order `h-1` in `B` would extend
with `v` to an independent set of order `h`,

```text
|B| <= P(h-2).
```

Adding `v`, `A`, and `B` gives the displayed bound.  QED.

**Corollary 28D.3: Exact Degree Buckets Have Small Row Diameter.**  Let
`h>=3`, put `P=P_h`, and let `G` be a graph with no regular induced
subgraph on at least `h` vertices.  If `U` is a set of vertices all having
the same degree in `G`, then for every two distinct `u,v in U`,

```text
|(N_G(u) triangle N_G(v))\{u,v}| <= 2P-2.
```

Consequently the traces of the adjacency rows of vertices in `U`, restricted
either to `U` or to `V(G)\U`, have pairwise Hamming distance at most
`2P-2`.

Proof.  As in Corollary 28D.2, the two one-sided differences
`N_G(u)\N_G(v)` and `N_G(v)\N_G(u)` have the same size because
`deg_G(u)=deg_G(v)`.  Lemma 28D says this common size is less than `P`.
Since it is an integer, it is at most `P-1`.  Removing the possible
coordinates `u` and `v` can only decrease the symmetric difference, so the
displayed inequality follows.  Restricting coordinates to `U` or to its
complement can only decrease Hamming distance.  QED.

This row-diameter form is a useful local obstruction, but by itself it does
not create the high-rank contradiction from Corollary 7D.  For every `m`,
the `m` vectors

```text
r_i=e_0+e_i,        1<=i<=m,
```

all have Hamming weight `2`, pairwise Hamming distance `2`, and rank `m`
over every field: in a linear relation, the `e_i` coordinate forces the
coefficient of `r_i` to be zero for each `i`.  Thus equal weights and tiny
diameter do not imply low rank without additional graph-theoretic structure.

**Definition 28D.4: The Full-Drop Ordered Parameter.**  For integers
`P,h>=1`, let `C_full(P,h)` be the least integer `m` such that every ordered
graph `H` on vertices

```text
v_1<...<v_m
```

with

```text
|(N_H(v_i)\N_H(v_j))\{v_i,v_j}| < P        for every i<j
```

contains a clique or independent set of order `h`.

This is stronger than the column-drop condition below: the representative
graph obtained from exact degree classes satisfies a full one-sided
neighborhood nesting condition, not just a bound on losses among earlier
rows.

**Lemma 28D.5: One-Sided Full-Drop Peeling Bound.**  For every `P,h>=1`,

```text
C_full(P,h) <= P(h-1)(h-2)+h.
```

Proof.  Let `H` be a full-drop ordered graph with no clique or independent
set of order `h`.  We prove that

```text
|V(H)| <= (h-1)(P(h-2)+1).
```

The claim is trivial for `h=1`, so assume `h>=2`.  Let `W` be a nonempty
ordered induced subgraph of `H`, with first vertex `a`.  The full-drop
condition is inherited by `H[W]`.

First consider `A=N_{H[W]}(a)`.  For every `u in A`, every nonneighbor of
`u` inside `A` lies in

```text
(N_{H[W]}(a)\N_{H[W]}(u))\{a,u},
```

which has size less than `P` because `a` is first.  Thus the complement of
`H[A]` has maximum degree at most `P-1`.  Greedily color this complement
with at most `P` colors.  Each color class is a clique in `H[A]`, and since
no clique of order `h-1` can occur in `A` without extending with `a` to a
clique of order `h`, every color class has size at most `h-2`.  Therefore

```text
|A| <= P(h-2).
```

Delete `a` and all of `A`.  This removes at most `P(h-2)+1` vertices.

Starting with `W_0=V(H)`, repeat this deletion process while the current set
is nonempty, and record the first vertex `a_t` of the current set.  Every
later recorded vertex survived the deletion of all neighbors of `a_t`, and
hence is nonadjacent to `a_t`.  Thus the recorded first vertices form an
independent set.

If `|V(H)|>(h-1)(P(h-2)+1)`, then after `h-1` deletion steps at least one
vertex remains, so the process records `h` pairwise nonadjacent vertices.
This is forbidden.  Therefore the displayed upper bound on `|V(H)|` holds,
which is equivalent to the stated bound on `C_full(P,h)`.  QED.

**Lemma 28D.5a: Exact Full-Drop Threshold At `P=1`.**  For every `h>=2`,

```text
C_full(1,h)=2h-2.
```

Proof.  First we prove the upper bound.  Let `H` be an ordered graph
satisfying the full-drop condition with `P=1`, that is,

```text
N(v_i)\{v_j} subset N(v_j)\{v_i}       whenever i<j.
```

We claim that every nonempty induced subgraph `J` of `H`, with its inherited
order, has

```text
alpha(J)+omega(J) >= |V(J)|+1.
```

The proof is by induction on `|V(J)|`.  Let `x` be the first vertex of `J`.
If `x` is isolated in `J`, then applying the induction hypothesis to
`J-x` gives

```text
alpha(J)+omega(J) >= (alpha(J-x)+1)+omega(J-x) >= |V(J)|+1.
```

Otherwise let `y` be the first neighbor of `x` in `J`.  We show that `y` is
universal in `J`.  If `z` lies before `y`, then `x<z<y` and `xy` is an edge;
the full-drop condition applied to the pair `x<z` forces `zy` to be an edge,
because otherwise `y` would lie in `N(x)\N(z)`.  If `z` lies after `y`, then
there are two cases.  If `xz` is an edge, applying the condition to `x<y`
forces `yz` to be an edge.  If `xz` is not an edge, applying the condition to
`x<z` with the witness `y` forces `yz` to be an edge.  Thus `y` is adjacent
to every other vertex of `J`.

Removing this universal vertex and applying induction gives

```text
alpha(J)+omega(J) >= alpha(J-y)+(\omega(J-y)+1) >= |V(J)|+1.
```

This proves the claim.

Consequently, if `|V(H)|>=2h-2`, then

```text
max(alpha(H),omega(H)) >= (|V(H)|+1)/2 > h-1,
```

so `H` contains a clique or independent set of order at least `h`.  Hence
`C_full(1,h)<=2h-2`.

For the lower bound, take the disjoint union of `h-2` isolated vertices and a
clique of order `h-1`, ordered with all isolated vertices first and all clique
vertices last.  This graph satisfies the `P=1` full-drop condition: an earlier
isolated vertex has empty neighborhood, and two clique vertices have identical
neighborhoods outside each other.  Its largest clique has order `h-1`, and
its largest independent set consists of all `h-2` isolated vertices plus at
most one clique vertex, also of order `h-1`.  Thus
`C_full(1,h)>2h-3`, and the upper bound gives equality.  QED.

**Lemma 28D.5b: A Linear Lower Construction At `P=2`.**  For every `h>=4`,

```text
C_full(2,h) > 4h-7.
```

Proof.  Put `t=h-3`.  Construct an ordered graph `H_t` as follows.

First take vertices

```text
a_1,...,a_t, b_1,...,b_t
```

in this order, with only the matching edges `a_i b_i` among them.  Next take
five vertices

```text
c_0,c_1,c_2,c_3,c_4
```

in this order, spanning the `5`-cycle with edges

```text
c_0c_1, c_0c_2, c_1c_3, c_2c_4, c_3c_4.
```

Finally take `t` pairs

```text
p_1,q_1, ..., p_t,q_t,
```

ordered by pairs.  The top layer is the complete `t`-partite graph with
parts `{p_i,q_i}`.  Join every `c_j` to every top-layer vertex, and add no
other edges.  The total order is

```text
2t+5+2t = 4h-7.
```

We first check the full-drop condition with `P=2`.  For an early matching
vertex, its only neighbor is its mate, so against any later vertex it loses
at most that one neighbor.  Inside the ordered `5`-cycle, a direct check of
the displayed edge list shows that for every earlier-later pair, the earlier
vertex has at most one cycle-neighbor not seen by the later vertex.  Top
vertices are common neighbors of all cycle vertices, so they do not add
cycle-to-cycle losses.

For a cycle vertex compared to a later top vertex, the cycle vertex is
adjacent to all top vertices, while the top vertex is nonadjacent exactly to
the other vertex in its own top part; all cycle vertices are adjacent to the
top vertex.  Thus the loss has size at most one.  For two top vertices, their
neighborhoods differ only by the mate of one or the other top part, so the
earlier-to-later loss again has size at most one.  Therefore

```text
|(N(v_i)\N(v_j))\{v_i,v_j}| < 2
```

for every `i<j`.

It remains to bound homogeneous sets.  The graph is the disjoint union of the
matching component on the `a_i,b_i` vertices and the joined component

```text
C_5 join T,
```

where `T` is the complete `t`-partite graph with parts of size `2`.  The
matching component has clique number `2` and independence number `t`.  The
joined component has

```text
omega(C_5 join T)=omega(C_5)+omega(T)=2+t=h-1,
```

and, because a join permits no independent set using both sides,

```text
alpha(C_5 join T)=max(alpha(C_5),alpha(T))=2.
```

Thus every clique in `H_t` has order at most `h-1`, and every independent set
has order at most `t+2=h-1`.  Hence `H_t` has no clique or independent set of
order `h`, while it has `4h-7` vertices and satisfies the `P=2` full-drop
condition.  This proves `C_full(2,h)>4h-7`.  QED.

**Lemma 28D.5b.1: Triangle-Free `P=2` Full-Drop Graphs Are Half
Independent.**  Let `H` be an ordered graph on `n` vertices satisfying the
`P=2` full-drop condition.  If `H` is triangle-free, then

```text
alpha(H) >= (n-1)/2.
```

Consequently, if `omega(H)<=2`, then

```text
alpha(H)+omega(H) >= (n+3)/2.
```

Proof.  We prove the first assertion by induction on `n`; the empty graph is
also allowed in the induction, with independence number `0`.  Let `a` be the
first vertex in the order, and put `A=N_H(a)`.  As in Lemma 28D.5 with
`P=2`, the complement of `H[A]` has maximum degree at most `1`.  Since `H` is
triangle-free, `A` is independent.  Therefore `|A|<=2`.

Let

```text
B=V(H)\({a} union A).
```

Then `a` is nonadjacent to every vertex of `B`.  If `|A|<=1`, the graph
`H[B]` is again triangle-free and satisfies the inherited `P=2` full-drop
condition.  By induction,

```text
alpha(H[B]) >= (|B|-1)/2.
```

Adding `a` to an independent set in `B` gives

```text
alpha(H) >= 1+(|B|-1)/2 = (|B|+1)/2.
```

If `A` is empty, then `n=|B|+1`, and this lower bound is `n/2`.  If `A` has
one vertex, then `n=|B|+2`, and the lower bound is `(n-1)/2`.

It remains to handle `|A|=2`; write `A={x,y}`.  For every `b in B`, the
comparison of `a` with the later vertex `b` gives

```text
|(N(a)\N(b))\{a,b}| <= 1.
```

Since `N(a)=A` and neither `x` nor `y` is one of the excluded endpoints, the
vertex `b` is adjacent to at least one of `x,y`.  Put

```text
X=N(x) cap B,        Y=B\X.
```

Every vertex in `X` is adjacent to `x`, so `X` is independent because `H` is
triangle-free.  Every vertex in `Y` is not adjacent to `x`, hence is adjacent
to `y`, so `Y` is independent for the same reason.  Thus `H[B]` is bipartite
with parts `X,Y`, and has an independent set of order at least `|B|/2`.
Adding `a` to this independent set gives

```text
alpha(H) >= 1+|B|/2 = (n-1)/2.
```

All cases prove `alpha(H)>=(n-1)/2`.

If `omega(H)=1`, then `H` is independent and the final assertion is trivial.
If `omega(H)=2`, the first assertion gives

```text
alpha(H)+omega(H) >= (n-1)/2+2 = (n+3)/2.
```

QED.

**Lemma 28D.5b.2: The Four-Neighbor First-Vertex Case At `P=2`,
`omega<=3`.**  Let `H` be an ordered graph on `n` vertices satisfying the
`P=2` full-drop condition and with `omega(H)<=3`.  Suppose that the first
vertex `a` has exactly four neighbors.  Then

```text
alpha(H) >= ceil((n-3)/2).
```

Proof.  Put `A=N(a)` and `B=V(H)\({a} union A)`.  As in Lemma 28D.5, the
complement of `H[A]` has maximum degree at most `1`.  Since `omega(H)<=3`,
the graph `H[A]` has no triangle, because any triangle in `A` would extend
with `a` to a `4`-clique.  On four vertices, these two facts force
`complement(H[A])` to be a perfect matching.  Write its two matching edges as

```text
u_1u_2,        v_1v_2.
```

Thus `H[A]` is the complete bipartite graph with nonedges inside
`{u_1,u_2}` and inside `{v_1,v_2}`.

For every `b in B`, the full-drop condition applied to the pair `a<b` gives

```text
|A\N(b)| <= 1,
```

because neither endpoint is in `A`.  If `bb'` is an edge inside `B`, then
`N(b) cap N(b') cap A` cannot contain an edge of `H[A]`; otherwise that edge
together with `b,b'` would form a `4`-clique.  Therefore the two missed
vertices of `A` for `b` and `b'` must be exactly `u_1,u_2`, or exactly
`v_1,v_2`.  In particular, vertices missing no member of `A` are isolated in
`H[B]`, and every edge of `H[B]` runs either between the class missing `u_1`
and the class missing `u_2`, or between the class missing `v_1` and the class
missing `v_2`.

Hence `H[B]` is bipartite; for example put the classes missing `u_1` or
`v_1`, together with the isolated no-miss class, on one side, and the classes
missing `u_2` or `v_2` on the other.  Thus

```text
alpha(H[B]) >= ceil(|B|/2).
```

The vertex `a` is nonadjacent to all of `B`, so adding it to a maximum
independent set in `B` gives

```text
alpha(H) >= 1+ceil(|B|/2).
```

Since `n=|B|+5`, the right side is `ceil((n-3)/2)`.  QED.

**Lemma 28D.5b.3: The `omega<=3` Case At `P=2`.**  Let `H` be an ordered
graph on `n` vertices satisfying the `P=2` full-drop condition.  If
`omega(H)<=3`, then

```text
alpha(H) >= ceil((n-3)/2).
```

Consequently,

```text
alpha(H)+omega(H) >= ceil((n+3)/2).
```

Proof.  The displayed independence bound is proved by induction on `n`, with
the empty graph allowed and the assertion trivial for `n<=3`.  Let `a` be the
first vertex of a nonempty graph `H`, put

```text
A=N(a),        B=V(H)\({a} union A),
```

and write `d=|A|`.  As in Lemma 28D.5, the complement of `H[A]` has maximum
degree at most `1`.  Since `omega(H)<=3`, the graph `H[A]` is triangle-free:
otherwise a triangle in `A` would extend with `a` to a `4`-clique.  Therefore
`d<=4`, because a graph on at least five vertices whose complement has maximum
degree at most `1` contains a triangle.

If `d<=2`, then `H[B]` inherits the `P=2` full-drop condition and still has
clique number at most `3`.  Since we are past the trivial cases `n<=3`, the
set `B` is nonempty.  By induction and the trivial bound
`alpha(H[B])>=1`,

```text
alpha(H[B]) >= max(1, ceil((|B|-3)/2)).
```

The vertex `a` is nonadjacent to every vertex of `B`, so

```text
alpha(H) >= 1+max(1, ceil((|B|-3)/2)) >= ceil((n-3)/2),
```

where the last inequality uses `n=|B|+d+1` and `d<=2`.

If `d=4`, Lemma 28D.5b.2 gives the required bound.  It remains to handle
`d=3`.  In this case `H[A]` is a path of length two: write its nonadjacent
leaves as `x,y`, and its center as `z`.

We first show that `H[B]` is triangle-free.  Suppose instead that
`T subset B` is a triangle.  Since `a` is first, every vertex of `T` is
adjacent to at least two vertices of `A`.  If some vertex of `A` were adjacent
to all three vertices of `T`, that vertex together with `T` would form a
`4`-clique.  Hence each vertex of `A` is missed by some member of `T`.  As
`|A|=|T|=3` and every member of `T` misses at most one vertex of `A`, the
missed vertices are all distinct.  Let `t_z in T` be the vertex missing
`z`, and let `t_x in T` be the vertex missing `x`.

Now compare the two ordered vertices `x` and `t_z`.  If `x<t_z`, then
`x` is adjacent to both `a` and `z`, while `t_z` is adjacent to neither; both
`a` and `z` are counted in

```text
(N(x)\N(t_z))\{x,t_z},
```

contradicting the `P=2` full-drop condition.  If `t_z<x`, then `t_z` is
adjacent to both `y` and `t_x`, while `x` is adjacent to neither `y` nor
`t_x`; both vertices are counted in

```text
(N(t_z)\N(x))\{t_z,x},
```

again a contradiction.  Thus `H[B]` is triangle-free.

Lemma 28D.5b.1 applied to `H[B]` gives

```text
alpha(H[B]) >= (|B|-1)/2.
```

Adding `a` to an independent set in `B` gives

```text
alpha(H) >= 1+(|B|-1)/2 = (|B|+1)/2.
```

Since now `n=|B|+4`, this is at least `ceil((n-3)/2)`.  This completes the
induction and proves the independence bound.

For the final assertion, if `omega(H)<=2`, Lemma 28D.5b.1 already gives
`alpha(H)+omega(H)>=(n+3)/2`.  If `omega(H)=3`, then the independence bound
just proved gives

```text
alpha(H)+omega(H) >= ceil((n-3)/2)+3 = ceil((n+3)/2).
```

QED.

**Lemma 28D.5b.4: Maximal Even First Neighborhoods At `P=2`.**  Let `s>=1`,
and let `H` be an ordered graph on `n` vertices satisfying the `P=2`
full-drop condition.  Suppose that the first vertex `a` has exactly `2s`
neighbors and that

```text
omega(H) <= s+1.
```

Then

```text
alpha(H)+omega(H) >= ceil((n+3)/2).
```

Proof.  Put `A=N(a)` and `B=V(H)\({a} union A)`.  The complement of `H[A]`
has maximum degree at most `1`.  Since every clique in `A` extends with `a`,
we also have `omega(H[A])<=s`.  On `2s` vertices this forces
`complement(H[A])` to be a perfect matching.  Write its pairs as

```text
{p_1,q_1}, ..., {p_s,q_s}.
```

Equivalently, `H[A]` is the complete `s`-partite graph with parts
`{p_i,q_i}`.

Every vertex `b in B` misses at most one vertex of `A`, by applying the
full-drop condition to the pair `a<b`.  We claim that `H[B]` is bipartite.
For a vertex `b in B`, call its type `p_i` if it misses `p_i`, call its type
`q_i` if it misses `q_i`, and call it type `*` if it misses no vertex of
`A`.

Let `bb'` be an edge in `H[B]`.  If the union of the vertices of `A` missed by
`b` or `b'` is not exactly the two endpoints of one pair `{p_i,q_i}`, then

```text
A cap N(b) cap N(b')
```

intersects every pair `{p_i,q_i}`.  Choosing one vertex from each pair gives
an `s`-clique in this common neighborhood, and together with the edge `bb'`
this forms a clique of order `s+2`, contradicting `omega(H)<=s+1`.
Therefore every edge of `H[B]` runs between the type `p_i` class and the type
`q_i` class for some common index `i`; type `*` vertices are isolated.
Putting all `p_i`-type vertices and all type `*` vertices on one side, and
all `q_i`-type vertices on the other, gives a bipartition of `H[B]`.

Hence

```text
alpha(H[B]) >= ceil(|B|/2).
```

The vertex `a` is nonadjacent to every vertex of `B`, so

```text
alpha(H) >= 1+ceil(|B|/2).
```

Also `a` together with one vertex from each pair `{p_i,q_i}` is a clique of
order `s+1`, so `omega(H)=s+1`.  Since `n=|B|+2s+1`,

```text
alpha(H)+omega(H)
  >= 1+ceil(|B|/2)+s+1
  = ceil((n+3)/2).
```

QED.

**Lemma 28D.5b.5: Maximal Odd First Neighborhoods At `P=2`.**  Let `s>=1`,
and let `H` be an ordered graph on `n` vertices satisfying the `P=2`
full-drop condition.  Suppose that the first vertex `a` has exactly `2s-1`
neighbors and that

```text
omega(H) <= s+1.
```

Then

```text
alpha(H)+omega(H) >= ceil((n+3)/2).
```

Proof.  Put `A=N(a)` and `B=V(H)\({a} union A)`.  The complement of `H[A]`
has maximum degree at most `1`, and `omega(H[A])<=s`.  Since `|A|=2s-1`,
this forces `complement(H[A])` to be a matching of size `s-1`, together with
one unmatched vertex.  Thus `H[A]` is a complete `s`-partite graph with
`s-1` parts of size `2` and one singleton part.  Write the paired parts as

```text
{p_1,q_1}, ..., {p_{s-1},q_{s-1}},
```

and write the singleton part as `{z}`.  The vertex `a` together with one
vertex from each part is a clique of order `s+1`, so `omega(H)=s+1`.

We claim that `H[B]` is triangle-free.  For `s=1` this is immediate from
`omega(H)<=2`, so assume `s>=2`.  Suppose for contradiction that
`T subset B` is a triangle.  Every vertex of `T` misses at most one vertex of
`A`, by applying the full-drop condition to `a` and that vertex.

If the common neighborhood

```text
C=A cap N(T)
```

intersected at least `s-1` of the `s` parts of `H[A]`, then `C` would contain
a clique of order `s-1`, and this clique together with the triangle `T` would
form a clique of order `s+2`, contradicting `omega(H)<=s+1`.  Hence the
union of the vertices of `A` missed by members of `T` must cover at least two
parts of `H[A]`.  It has size at most `3`, and only one part is a singleton,
so it must consist of the singleton `z` and both endpoints of one paired part,
say `{p_1,q_1}`.  Thus there are vertices `t_z,t_p in T` such that `t_z`
misses `z` and `t_p` misses `p_1`.

Now compare the ordered vertices `p_1` and `t_z`.  If `p_1<t_z`, then `p_1`
is adjacent to both `a` and `z`, while `t_z` is adjacent to neither; both
vertices are counted in

```text
(N(p_1)\N(t_z))\{p_1,t_z},
```

contradicting the `P=2` full-drop condition.  If `t_z<p_1`, then `t_z` is
adjacent to both `q_1` and `t_p`, while `p_1` is adjacent to neither `q_1`
nor `t_p`; both vertices are counted in

```text
(N(t_z)\N(p_1))\{t_z,p_1},
```

again a contradiction.  Therefore `H[B]` is triangle-free.

By Lemma 28D.5b.1,

```text
alpha(H[B]) >= (|B|-1)/2.
```

Adding `a` gives

```text
alpha(H) >= 1+(|B|-1)/2,
```

and since `alpha(H)` is an integer, this is

```text
alpha(H) >= ceil((|B|+1)/2).
```

Since `n=|B|+2s`, the last displayed bound and `omega(H)=s+1` imply

```text
alpha(H)+omega(H)
  >= ceil((|B|+1)/2)+s+1
  = ceil((n+3)/2).
```

QED.

**Corollary 28D.5b.6: The High First-Degree Case At `P=2`.**  Let `H` be an
ordered graph on `n` vertices satisfying the `P=2` full-drop condition, and
let `omega=omega(H)`.  If the first vertex has degree at least

```text
2omega-3,
```

then

```text
alpha(H)+omega(H) >= ceil((n+3)/2).
```

Proof.  Let the first degree be `d`.  As in Lemma 28D.5, the first
neighborhood has complement maximum degree at most `1`, and since every
clique in that neighborhood extends with the first vertex, the usual matching
cover bound gives

```text
d <= 2omega-2.
```

Thus `d` is either `2omega-2` or `2omega-3`.  In the first case apply
Lemma 28D.5b.4 with `s=omega-1`; in the second case apply Lemma 28D.5b.5
with the same value of `s`.  QED.

**Lemma 28D.5b.7: First-Neighborhood Part Covering At `P=2`.**  Let `H` be
an ordered graph satisfying the `P=2` full-drop condition, let `a` be its
first vertex, and put

```text
A=N(a),        B=V(H)\({a} union A),        omega=omega(H).
```

Let `P_1,...,P_r` be the parts of `A` induced by the connected components of
`complement(H[A])`; each part has size `1` or `2`, and `H[A]` is complete
multipartite with these parts.  If `T subset B` is a clique of order `t`, and

```text
M_T={x in A : x is nonadjacent to some vertex of T},
```

then:

1. `|M_T|<=t`;
2. `M_T` contains all vertices of at least `r+t-omega` of the parts
   `P_i` (with this assertion void when `r+t<=omega`).

Proof.  The part decomposition is just the statement that the complement of
`H[A]` has maximum degree at most `1`, proved in Lemma 28D.5.  For every
`b in B`, the full-drop condition applied to `a<b` gives `|A\N(b)|<=1`;
therefore the union of the missed sets over the `t` vertices of `T` has size
at most `t`.  This proves (1).

Let `C=A\M_T` be the common neighborhood of `T` inside `A`.  A clique in
`H[C]` is obtained by choosing one vertex from every part `P_i` that
intersects `C`, because all edges between different parts are present.  If
`M_T` fully contains fewer than `r+t-omega` parts, then `C` intersects more
than `omega-t` parts, so `C` contains a clique of order greater than
`omega-t`.  Together with the clique `T`, this would give a clique in `H` of
order greater than `omega`, a contradiction.  Thus `M_T` fully contains at
least `r+t-omega` parts.  QED.

This lemma isolates the remaining obstruction in the `P=2` full-drop
`alpha+omega` problem.  When `r=omega-1`, taking `t=2` already forces every
edge in `B` to miss both endpoints of one size-two part; this is the bipartite
mechanism in Lemma 28D.5b.4.  When `r<=omega-2`, edges in `B` may be
unconstrained by the first neighborhood, and a different source of one extra
independent vertex is needed to close the induction.

**Corollary 28D.5b.8: Induction Deficit Forces Covered Parts.**
Use the notation of Lemma 28D.5b.7, and put `b=|B|`.  Let
`omega_B=omega(H[B])`, and define the one-step induction deficit

```text
D = ceil((|V(H)|+3)/2)
    -1-ceil((b+3)/2)
    -(omega-omega_B).
```

If `D>0`, then every maximum clique `T` of `H[B]` fully covers at least `D`
of the first-neighborhood parts `P_i` from Lemma 28D.5b.7.

Proof.  Let `d=|A|` and let `r` be the number of parts in the decomposition
of `A`.  Since every part has size at most `2`,

```text
ceil(d/2) <= r.
```

Also `|V(H)|=b+d+1`, and therefore

```text
ceil((|V(H)|+3)/2)-1-ceil((b+3)/2) <= ceil(d/2) <= r.
```

Consequently

```text
D <= r-(omega-omega_B)=r+omega_B-omega.
```

Applying Lemma 28D.5b.7 to any clique `T subset B` of order `omega_B` shows
that `T` fully covers at least `r+omega_B-omega` first-neighborhood parts,
and hence at least `D` of them when `D>0`.  QED.

**Lemma 28D.5b.9: A Clique Cannot Fully Cover Two Parts If One Has Size
Two.**  Use the notation of Lemma 28D.5b.7.  Let `T subset B` be a clique.
If `T` fully covers a first-neighborhood part of size `2`, then `T` fully
covers no other first-neighborhood part.

Proof.  Suppose, for contradiction, that `T` fully covers a size-two part
`{x,x'}` and also fully covers a distinct part containing a vertex `y`.
Choose vertices `t_x,t_y in T` such that `t_x` is nonadjacent to `x` and
`t_y` is nonadjacent to `y`.  Such vertices exist by full coverage.  Since
every vertex of `B` misses at most one vertex of `A`, the vertex `t_y` is
adjacent to `x` and `x'`.

Compare the ordered pair `x,t_y`.  If `x<t_y`, then `x` is adjacent to both
`a` and `y`, while `t_y` is adjacent to neither `a` nor `y`.  These two
vertices are counted in

```text
(N(x)\N(t_y))\{x,t_y},
```

contradicting the `P=2` full-drop condition.  If `t_y<x`, then `t_y` is
adjacent to both `t_x` and `x'`, while `x` is adjacent to neither: `t_x`
misses `x`, and `x'` lies in the same first-neighborhood part as `x`.  These
two vertices are counted in

```text
(N(t_y)\N(x))\{t_y,x},
```

again contradicting the `P=2` full-drop condition.  QED.

Consequently, in the situation of Corollary 28D.5b.8, if the induction
deficit `D` is at least `2`, then the `D` forced covered parts must all be
singleton parts of the first neighborhood.  Any residual proof can therefore
split into a one-paired-part deficit and an all-singleton deficit.

**Lemma 28D.5b.10: Order Constraint For Covered Singleton Parts.**  Use the
notation of Lemma 28D.5b.7.  Let `T subset B` be a clique, and suppose that
two distinct singleton first-neighborhood parts `{x}` and `{y}` are fully
covered by `T`.  Let `t_x,t_y in T` be vertices with `t_x` nonadjacent to
`x` and `t_y` nonadjacent to `y`.  Then

```text
t_x < y        and        t_y < x.
```

Proof.  Since every vertex of `B` misses at most one vertex of `A`, the
vertices `t_x` and `t_y` are distinct, `t_x` is adjacent to `y`, and `t_y` is
adjacent to `x`.

If `y<t_x`, then `y` is adjacent to both `a` and `x`, while `t_x` is adjacent
to neither `a` nor `x`.  These two vertices are counted in

```text
(N(y)\N(t_x))\{y,t_x},
```

contradicting the `P=2` full-drop condition.  Thus `t_x<y`.  The proof of
`t_y<x` is symmetric.  QED.

Thus an all-singleton induction deficit has a rigid order pattern: each
clique vertex that misses one covered singleton must occur before every other
covered singleton.  This is the remaining ordered configuration not excluded
by Lemma 28D.5b.9.

**Lemma 28D.5b.11: Covered Singleton Parts Give Regular Witnesses.**  Use the
notation of Lemma 28D.5b.7.  Let `T subset B` be a clique.  Suppose `S` is a
set of singleton first-neighborhood parts, identified with their unique
vertices, and that `T` fully covers every singleton in `S`.  Then `H`
contains a regular induced subgraph of order `2|S|`.

Proof.  For each `x in S`, choose a vertex `t_x in T` nonadjacent to `x`.
The chosen vertices `t_x` are distinct, because every vertex of `B` is
nonadjacent to at most one vertex of `A`.  Put

```text
T_S={t_x : x in S}.
```

The set `S` is a clique, since its vertices lie in distinct singleton parts
of `H[A]`.  The set `T_S` is a clique because it is contained in `T`.  For
`x,y in S`, the vertex `t_x` is adjacent to `y` whenever `y != x`, again
because `t_x` misses at most one vertex of `A`; and by construction `t_x` is
nonadjacent to `x`.  Therefore `H[S union T_S]` is the complete graph on
`2|S|` vertices with the matching `x t_x`, `x in S`, removed.  It is regular
of degree `2|S|-2`.  QED.

Consequently, in any graph with no regular induced subgraph of order at least
`h`, a clique in `B` can fully cover fewer than `ceil(h/2)` singleton
first-neighborhood parts.  This is a direct regularity obstruction, not just
a homogeneous-set obstruction.

**Lemma 28D.5c: Full-Drop Core Extension Lower Construction.**  Fix
`P>=1`.  Let `R` be an ordered graph on `q` vertices satisfying the
`P`-full-drop condition, and suppose

```text
alpha(R), omega(R) <= s,        s>=P.
```

Then for every `h>=s+2`,

```text
C_full(P,h) > 2P(h-s-1)+q.
```

Proof.  Put `t=h-s-1`.  We construct an ordered graph `H` on
`2Pt+q` vertices.

The first block `L` is a disjoint union of `t` cliques of order `P`, ordered
clique by clique.  The middle block is a copy of `R` with its given order.
The final block `T` is a complete `t`-partite graph with all parts of size
`P`, again ordered part by part.  Join every vertex of `R` to every vertex of
`T`, and add no edges between `L` and `R union T`.

We check the full-drop condition.  Inside `L`, an earlier vertex can lose at
most the other `P-1` vertices of its own clique when compared with a later
vertex.  From `L` to any later block the same bound holds, because vertices
outside `L` have no neighbors in `L`.  Inside `R` the condition holds by
hypothesis.  From `R` to `T`, a vertex of `R` is adjacent to all of `T`, while
a top vertex is nonadjacent only to the other `P-1` vertices in its own top
part; all vertices of `R` are common neighbors.  Inside `T`, two vertices in
the same part have the same external neighborhood, and two vertices in
different parts differ in the earlier-to-later direction only on the later
vertex's `P-1` part-mates.  Thus every earlier-later loss has size less than
`P`.

Now bound homogeneous sets.  The left block has clique number `P` and
independence number `t`.  The joined component `R join T` has

```text
omega(R join T) <= omega(R)+t <= s+t = h-1,
```

and

```text
alpha(R join T)=max(alpha(R), alpha(T)) <= max(s,P)=s.
```

Since `H` is the disjoint union of `L` and `R join T`, its clique number is at
most `h-1`, and its independence number is at most

```text
t+s=h-1.
```

Therefore `H` satisfies the `P`-full-drop condition, has `2Pt+q` vertices,
and has no clique or independent set of order `h`.  This proves the
displayed lower bound.  QED.

Taking `R=K_P`, `q=s=P`, gives the explicit general lower bound

```text
C_full(P,h) > 2P(h-P-1)+P        for h>=P+2.
```

For `P=2`, the `5`-cycle core in Lemma 28D.5b improves the additive constant
from this clique-core construction.

**Lemma 28D.5d: Full-Drop Graphs Are Degenerate In Terms Of Clique
Number.**  Let `H` be a `P`-full-drop ordered graph with clique number
`omega`.  Then every induced subgraph of `H` has a vertex of degree at most

```text
P(omega-1).
```

Consequently,

```text
alpha(H) >= |V(H)|/(P(omega-1)+1).
```

Proof.  Let `J` be a nonempty induced subgraph of `H`, with inherited order,
and let `a` be the first vertex of `J`.  Put `A=N_J(a)`.  For every
`u in A`, every nonneighbor of `u` inside `A` lies in

```text
(N_J(a)\N_J(u))\{a,u},
```

which has size less than `P`.  Therefore the complement of `J[A]` has maximum
degree at most `P-1`, and is greedily colorable with at most `P` colors.  Each
color class is a clique in `J[A]`.  Since any clique in `A` extends with `a`
to a clique one vertex larger, every such color class has size at most
`omega-1`.  Hence

```text
deg_J(a)=|A| <= P(omega-1).
```

Thus every induced subgraph has a vertex of degree at most `P(omega-1)`, so
`H` is `P(omega-1)`-degenerate.  Greedy coloring colors `H` with at most
`P(omega-1)+1` colors, and the largest color class is an independent set of
the displayed order.  QED.

**Lemma 28D.5e: Two-Ended Linear Full-Drop Bound.**  For every `P>=1` and
`h>=2`,

```text
C_full(P,h) <= 4P(h-2)+2.
```

Proof.  Let `H` be a `P`-full-drop ordered graph on
`v_1<...<v_n` with no clique or independent set of order `h`.  We prove

```text
n <= 4P(h-2)+1.
```

Fix an index `i`, and work in the suffix induced by
`{v_i,v_{i+1},...,v_n}`.  Let `A_i` be the later neighbors of `v_i`.  For
each `x in A_i`, every nonneighbor of `x` inside `A_i` is an element of

```text
(N(v_i)\N(x))\{v_i,x},
```

computed inside the suffix, and hence there are at most `P-1` such
nonneighbors.  Thus the complement of `H[A_i]` has maximum degree at most
`P-1`, so it is colorable with at most `P` colors.  A color class is a clique
in `H[A_i]`; if such a clique had order `h-1`, adjoining `v_i` would give a
clique of order `h`.  Hence

```text
|A_i| <= P(h-2).
```

Now work in the prefix induced by `{v_1,...,v_i}`.  Let `D_i` be the earlier
nonneighbors of `v_i`.  For any earlier vertex `x`, its neighbors in `D_i`
are contained in

```text
(N(x)\N(v_i))\{x,v_i},
```

computed inside the prefix.  Therefore every vertex of the prefix has at
most `P-1` neighbors in `D_i`, and in particular `H[D_i]` has maximum degree
at most `P-1`.  Greedy coloring gives an independent set in `H[D_i]` of size
at least `|D_i|/P`; if such an independent set had order `h-1`, adjoining
`v_i` would give an independent set of order `h`.  Therefore

```text
|D_i| <= P(h-2).
```

Count ordered pairs `v_i<v_j`.  Edge pairs are counted by the later-neighbor
sets `A_i`, and nonedge pairs are counted by the earlier-nonneighbor sets
`D_j`.  Hence

```text
binom(n,2) <= sum_i |A_i| + sum_i |D_i|
            <= 2nP(h-2).
```

For `n>=1`, this gives `(n-1)/2 <= 2P(h-2)`, so
`n<=4P(h-2)+1`.  Thus every `P`-full-drop ordered graph on at least
`4P(h-2)+2` vertices contains a clique or independent set of order `h`.
QED.

**Corollary 28D.6: Global Reduction Through Full-Drop Ordering.**  For every
`h>=3`, with `P=P_h`,

```text
G(h) <= 2P(h-1) C_full(P,h)
     <= 2P(h-1)(4P(h-2)+2)
     <= 8h^2P^2.
```

Proof.  Let `G` be a graph with no regular induced subgraph on at least `h`
vertices.  Partition `V(G)` into exact global degree classes.  By Corollary
28D.2, every nonempty degree class has size at most `2P(h-1)`.

Choose one representative from each nonempty degree class and order the
representatives by increasing degree:

```text
v_1<...<v_b.
```

For `i<j`, the representative degrees are strictly increasing.  With

```text
A=N_G(v_i)\N_G(v_j),       B=N_G(v_j)\N_G(v_i),
```

we have `|A|<|B|`, and Lemma 28D gives `min(|A|,|B|)<P`.  Hence

```text
|(N_G(v_i)\N_G(v_j))\{v_i,v_j}| < P.
```

Restricting to representatives shows that their ordered induced graph
satisfies the full-drop condition.  If `b>=C_full(P,h)`, the representatives
contain a clique or independent set of order `h`, which is a regular induced
subgraph of `G`, impossible.  Thus `b<C_full(P,h)`.  Multiplying by the
degree-class size bound gives

```text
|V(G)| < 2P(h-1) C_full(P,h).
```

The first displayed inequality follows from the definition of `G(h)`, the
second from Lemma 28D.5e, and the final coarse bound from `h>=3` and `P>=1`.
QED.

**Definition 28D.6a: The Regular Full-Drop Parameter.**  For integers
`P,h>=1`, let `C_full^reg(P,h)` be the least integer `m` such that every
ordered graph on `m` vertices satisfying the `P`-full-drop condition contains
a regular induced subgraph on at least `h` vertices.

Since every clique and every independent set is regular,

```text
C_full^reg(P,h) <= C_full(P,h) <= 4P(h-2)+2        for h>=2.
```

**Corollary 28D.6b: Global Reduction Through Regular Full-Drop.**  For every
`h>=3`, with `P=P_h`,

```text
G(h) <= 2P(h-1) C_full^reg(P,h).
```

Proof.  Let `G` be a graph with no regular induced subgraph on at least `h`
vertices.  As in Corollary 28D.6, each exact global degree class has size at
most `2P(h-1)`, and one representative from each nonempty degree class,
ordered by increasing degree, satisfies the `P`-full-drop condition.

If the representative graph had at least `C_full^reg(P,h)` vertices, it would
contain a regular induced subgraph on at least `h` representatives.  The same
vertex set induces the same regular graph in `G`, contradiction.  Therefore
there are fewer than `C_full^reg(P,h)` nonempty degree classes, and

```text
|V(G)| < 2P(h-1) C_full^reg(P,h).
```

The displayed upper bound for `G(h)` follows.  QED.

This regular full-drop parameter is the natural home for Lemma 28D.5b.11:
covered singleton parts may give a large regular witness even when they do
not immediately improve the homogeneous `alpha+omega` bound.

**Definition 28D.6b.1: The Loss Graph At `P=2`.**  Let `H` be a
`P=2` full-drop ordered graph on vertices `v_1<...<v_m`.  The loss graph
`L(H)` is the graph on the same vertex set in which `v_i v_j`, `i<j`, is an
edge exactly when

```text
|(N_H(v_i)\N_H(v_j))\{v_i,v_j}| = 1.
```

Thus a nonedge of `L(H)` is a pair with zero earlier-to-later loss.

**Lemma 28D.6b.2: Loss-Independent Sets Are `P=1` Full-Drop.**  Let `H` be a
`P=2` full-drop ordered graph.  If `I` is an independent set in `L(H)`, then
`H[I]`, with the inherited order, satisfies the `P=1` full-drop condition.
Consequently,

```text
reg(H) >= ceil((|I|+1)/2).
```

Proof.  For any two vertices `v_i<v_j` in `I`, the `P=2` full-drop condition
says the earlier-to-later loss has size at most `1`, and independence in
`L(H)` says it is not equal to `1`.  Hence it is `0`.  This is precisely the
`P=1` full-drop condition on `H[I]`.  Lemma 28D.5a proves that every
`P=1` full-drop ordered graph on `s` vertices satisfies
`alpha+\omega>=s+1`, so it contains a clique or independent set, hence a
regular induced subgraph, of order at least `ceil((s+1)/2)`.  QED.

Thus proving a half-size regular theorem for `P=2` full-drop graphs reduces
to understanding the case where the loss graph itself has small independence
number.  The lower family in Lemma 28D.6c has a large loss-independent block,
so it is extremal for a subtler reason than loss-graph density.

**Lemma 28D.6b.3: Legal Right Extensions At `P=2`.**  Let `H` be a
`P=2` full-drop ordered graph on vertices `v_1<...<v_m`, and let `D` be a
subset of `V(H)`.  Form an ordered graph `H^D` by adding a new last vertex
`w` which is nonadjacent exactly to the old vertices in `D`.  Then `H^D` is
again `P=2` full-drop if and only if the following two conditions hold.

1. Every old vertex has at most one neighbor in `D`.
2. Whenever `i<j` and

```text
|(N_H(v_i)\N_H(v_j))\{v_i,v_j}| = 1,
```

if `v_j in D`, then `v_i in D`.

Equivalently, `D` is an open packing in `H` and is down-closed with respect to
the ordered saturated-loss relation.

Proof.  Old pairs `v_i<v_j` have the same old loss as before, except that the
new coordinate `w` contributes one additional loss exactly when `w` is
adjacent to `v_i` and nonadjacent to `v_j`, that is, when
`v_i notin D` and `v_j in D`.  Since old losses are `0` or `1`, all old pairs
remain legal exactly when no saturated pair of loss `1` has
`v_i notin D` and `v_j in D`.  This is condition 2.

It remains to check pairs `v_i<w`.  For such a pair,

```text
(N_{H^D}(v_i)\N_{H^D}(w))\{v_i,w}
```

is precisely the set of old neighbors of `v_i` which lie in `D`.  Thus its
size is less than `2` for every `i` exactly when every old vertex has at most
one neighbor in `D`.  This is condition 1.  The two conditions together are
therefore necessary and sufficient.  QED.

**Corollary 28D.6b.4: Last-Vertex Sparse Nonneighbor Decomposition.**  Let
`H` be a `P=2` full-drop ordered graph, let `z` be its last vertex, and put

```text
C=N_H(z),        D=V(H)\({z} union C).
```

Then every vertex of `H-z` has at most one neighbor in `D`.  In particular,
`H[D]` has maximum degree at most `1`, and the bipartite graph between `C`
and `D` has degree at most `1` on the `C` side.  Consequently

```text
reg(H) >= max { reg(H[C]), ceil(|D|/2) }.
```

Proof.  View `H` as a right extension of `H-z`; the set `D` is exactly the
set of old nonneighbors of the new last vertex `z`.  Lemma 28D.6b.3 says
that every old vertex has at most one neighbor in `D`, giving the first
claims.

A graph of maximum degree at most `1` is a disjoint union of isolated
vertices and edges.  If it has `s` isolated vertices and `e` edge components,
then its isolated vertices form a `0`-regular induced subgraph of order `s`,
while its edge components together form a `1`-regular induced subgraph of
order `2e`.  Since `max(s,2e)>=ceil((s+2e)/2)=ceil(|D|/2)`, the displayed
lower bound follows, together with the inherited regular witnesses inside
`H[C]`.  QED.

**Lemma 28D.6c: A Linear Lower Construction For Regular Full-Drop At
`P=2`.**  For every `h>=7`,

```text
C_full^reg(2,h) > 2h.
```

Proof.  Put `t=h-3`.  We construct an ordered graph `H_t` on `2h=2t+6`
vertices.  First take four vertices

```text
p_0,p_1,q_0,q_1
```

with only the two matching edges `p_0q_0` and `p_1q_1`.  Next take an
independent set `M` of size `t`, then a clique `K` of size `t`, and finally
two vertices `u_0,u_1`.  Order the vertices in these four blocks.  Join every
vertex of `K` to every vertex of `M` and to `q_1`; join `u_0,u_1` to every
earlier vertex but not to each other; add no other edges.

The `P=2` full-drop condition is immediate from the ordered construction.
When a later vertex lies in `M`, an earlier special vertex loses at most its
matching mate, and earlier vertices of `M` lose nothing.  When a later vertex
lies in `K`, an earlier special vertex loses at most one of
`p_0,p_1,q_0`, and an earlier vertex of `M` loses nothing.  A later top
vertex is adjacent to every earlier vertex, so it creates no earlier-to-later
loss.  The remaining comparisons are inside the first four vertices, where
the earlier vertex loses at most its matching mate, and inside `K`, where
neighborhoods are nested up to the excluded endpoints.

We prove that `H_t` has no regular induced subgraph of order at least
`h=t+3`.  Let `S` be a regular induced subgraph, and write `z` for the number
of selected top vertices.  Also write `m,c` for the numbers of selected
vertices from `M,K`, and write `x_0,x_1,y_0,y_1 in {0,1}` for the indicators
that `p_0,p_1,q_0,q_1`, respectively, are selected.

First suppose `z=0`.  If `m>0` and `c>0`, then vertices of `M` have degree
`c`, while vertices of `K` have degree `c-1+m+y_1`; regularity gives

```text
m+y_1=1.
```

Thus `m=1` and `y_1=0`.  If `c>=2`, then none of `p_0,p_1,q_0` can be
selected, since their degrees are at most `1`; hence `|S|=c+1<=t+1`.  If
`c=1`, then among `p_0,p_1,q_0` only the adjacent pair `p_0,q_0` can have
degree `1`, so `|S|<=4<t+3`.

If `m>0` and `c=0`, vertices of `M` have degree `0`, so the selected
first-four vertices must be independent in the two-edge matching
`p_0q_0,p_1q_1`.  At most two such vertices can be selected, giving
`|S|<=m+2<=t+2`.

If `m=0` and `c>0`, then vertices of `K` have degree `c-1+y_1`.  When
`y_1=0`, this degree is `c-1`: for `c>=3`, no first-four vertex can also have
that degree, while for `c<=2` the total size is at most `6<t+3`.  Hence
`|S|<=t` or `|S|<t+3`.  When `y_1=1`, the degree of a vertex in `K` is `c`;
regularity at `q_1`, whose degree is `x_1+c`, forces `x_1=0`.  If `c>=2`, no
other first-four vertex can have degree `c`, so `|S|=c+1<=t+1`; if `c=1`,
then at most the pair `p_0,q_0` can be added, giving `|S|<=4<t+3`.

Finally, if `m=c=0`, then `S` lies inside the first four vertices and has size
at most `4<t+3`.  Therefore `|S|<h` when `z=0`.

If `z=1`, the selected top vertex has degree `|S|-1`, so every other selected
vertex must be adjacent to every other non-top selected vertex.  The non-top
graph has clique number `t+1`, for instance `K union {q_1}` or `K` plus one
vertex of `M`, and no larger clique.  Hence `|S|<=t+2<h`.

It remains to consider `z=2`.  Let `X` be the selected non-top set.  The two
top vertices have degree `|S|-2=|X|`, so each vertex of `X` must have degree
`|X|-2` inside `X`.  Equivalently, the complement of `H_t[X]` is `1`-regular.

In the complement of the non-top graph, each vertex of `M` is adjacent to all
other vertices of `M` and to all four special vertices, but to no vertex of
`K`; each vertex of `K` is adjacent only to `p_0,p_1,q_0`; and the first four
vertices induce the `4`-cycle

```text
p_0p_1q_0q_1p_0
```

in the complement.  If `X` contains a vertex of `M`, then the complement
degree of every selected `M` vertex is `(m-1)+x_0+x_1+y_0+y_1`, so

```text
m+x_0+x_1+y_0+y_1=2.
```

If a vertex of `K` were also selected, it would need exactly one selected
neighbor among `p_0,p_1,q_0` in the complement; that special vertex would then
be adjacent in the complement to both the selected `M` vertex and the selected
`K` vertex, contradiction.  Thus `c=0` and `|X|=2`.

If `X` contains no vertex of `M`, then every selected vertex of `K` must have
exactly one selected complement-neighbor among `p_0,p_1,q_0`.  If `c>=2`,
that unique special vertex would have complement degree at least `2`; hence
`c<=1`.  With `c=0`, the first four vertices have no induced `1`-regular
subgraph larger than an edge.  With `c=1`, the unique selected vertex of `K`
must be matched in the complement to exactly one of `p_0,p_1,q_0`, and no
additional first-four complement edge can be selected.  Hence `|X|<=2` in all
cases.  Therefore `|S|<=4<t+3`, since `t>=4`.

All cases give `|S|<h`.  Thus `H_t` is a `P=2` full-drop ordered graph on
`2h` vertices with no regular induced subgraph of order at least `h`, proving
the displayed lower bound.  QED.

**Lemma 28D.6d: The Regular Full-Drop Lower Family Is Right-Extension
Critical.**  Let `H_t` be the ordered graph from Lemma 28D.6c, with
`h=t+3>=7`.  If a new last vertex `w` is added so that the resulting ordered
graph still satisfies the `P=2` full-drop condition, then the extended graph
contains a clique of order `h`.

Proof.  Let `U={u_0,u_1}` be the final top pair of `H_t`, and let
`X=V(H_t)\U` be the non-top vertices.  Comparing `u_0` with the new last
vertex `w` shows that `w` is nonadjacent to at most one vertex of `X`, since
`N(u_0)=X`; the same conclusion follows from `u_1`.

We first show that `w` is adjacent to both top vertices.  If, say, `w` were
nonadjacent to `u_0`, then choose a vertex `x in X` adjacent to `w`, possible
because `w` misses at most one vertex of `X` and `|X|>=2`.  In the ordered
pair `x<u_0`, the earlier vertex `x` is adjacent to both `u_1` and `w`,
whereas `u_0` is adjacent to neither.  This gives two vertices in

```text
(N(x)\N(u_0))\{x,u_0},
```

contradicting the `P=2` full-drop condition.  The proof for `u_1` is the
same.

It remains to identify the possible non-top vertex missed by `w`.  Since
`w` is adjacent to both top vertices and misses at most one vertex of `X`,
all vertices of `X` except possibly one are adjacent to `w`.  If the missed
vertex were `p_1`, then the ordered pair `p_0<p_1` would have both `q_0` and
`w` in the earlier-to-later loss.  If it were `q_0`, the pair `p_1<q_0`
would have both `q_1` and `w` in the loss.  If it were `q_1`, or any vertex
of `M union K`, the pair `p_0<q_1` or respectively `p_0<y` would have both
`q_0` and `w` in the loss.  All alternatives contradict full-drop.  Therefore
the only non-top vertex that `w` may miss is `p_0`.

Thus `w` is adjacent to `q_1`, to both top vertices, and to every vertex of
`K`.  Hence

```text
K union {q_1,u_0,w}
```

is a clique of order `t+3=h`.  QED.

**Computational Calibration 28D.7: Small Full-Drop Values.**  The script
`EXPERIMENTS/full_drop_census.py` exactly enumerates small ordered graphs
satisfying the full-drop condition and reuses the regular-witness checker.
The commands

```text
python3 82/EXPERIMENTS/full_drop_census.py 5 --p 1
python3 82/EXPERIMENTS/full_drop_census.py 6 --p 2
python3 82/EXPERIMENTS/full_drop_census.py 8 --p 2 --search-h 4 --max-nodes 50000
python3 82/EXPERIMENTS/full_drop_census.py 13 --p 2 --search-h 5 --max-nodes 100000
```

report respectively:

```text
P=1, n=5: checked_full_drop=16,   min_max_homogeneous=3, min_max_regular=3
P=2, n=6: checked_full_drop=1622, min_max_homogeneous=3, min_max_regular=3
P=2, n=8: DFS found max_full_drop=1 with max_homogeneous=3 and max_regular=4.
P=2, n=13: DFS found max_full_drop=1 with max_homogeneous=4 and max_regular=6.
```

These checks are only finite calibration.  Their role is to verify the new
full-drop predicate and to confirm that it is genuinely stronger than the
older column-drop predicate used below.

The construction in Lemma 28D.5b is generated by
`EXPERIMENTS/full_drop_p2_construction.py`.  For example,

```text
python3 82/EXPERIMENTS/full_drop_p2_construction.py 4
python3 82/EXPERIMENTS/full_drop_p2_construction.py 5
python3 82/EXPERIMENTS/full_drop_p2_construction.py 6
```

reproduce the `n=9` and `n=13` search certificates above and give the next
case `n=17`, always with maximum full drop `1` and maximum homogeneous order
`h-1`.  These examples may contain regular induced subgraphs larger than
`h`; they calibrate the homogeneous full-drop parameter, not the regular
column-drop parameter.

The regular full-drop parameter from Definition 28D.6a is genuinely distinct
from the homogeneous one.  The commands

```text
python3 82/EXPERIMENTS/full_drop_p2_regular_construction.py 5
python3 82/EXPERIMENTS/full_drop_p2_regular_construction.py 6
python3 82/EXPERIMENTS/full_drop_p2_regular_construction.py 9
python3 82/EXPERIMENTS/full_drop_census.py 8 --p 2 --search-regular-h 5 --max-nodes 200000 --progress 50000
python3 82/EXPERIMENTS/full_drop_census.py 9 --p 2 --search-regular-h 5 --max-nodes 200000 --progress 50000
python3 82/EXPERIMENTS/full_drop_census.py 10 --p 2 --search-regular-h 5 --max-nodes 500000 --progress 100000
python3 82/EXPERIMENTS/full_drop_census.py 11 --p 2 --search-regular-h 5 --max-nodes 1000000 --progress 100000
```

verify the construction of Lemma 28D.6c in the small cases `h=5,6` and one
larger sample `h=9`, and also
find `P=2` full-drop ordered graphs with no regular induced subgraph of order
`5` on `8`, `9`, and `10` vertices, respectively, while the `n=11` search
exhausts the DFS tree in `65,904` nodes with `result=False`.  Thus, subject
to this finite verifier,

```text
C_full^reg(2,5)=11.
```

The `n=10` certificate has columns

```text
0,0,1,2,0,0,56,120,255,255,
```

with `max_full_drop=1`, `clique_number=4`, `independence_number=4`, and
`max_regular=4`.

The auxiliary script `EXPERIMENTS/full_drop_regular_frontier.py` checks
whether obstructions at one order have legal right-extensions that remain
obstructions.  The command

```text
python3 82/EXPERIMENTS/full_drop_regular_frontier.py 10 --p 2 --h 5 --max-nodes 200000 --progress 50000
```

visits `65,904` search nodes, checks `9,656` terminal `10`-vertex
obstructions to regular `5`-sets, and finds `extendable=0`, matching the
exact value `C_full^reg(2,5)=11`.

The script `EXPERIMENTS/full_drop_regular_min.py` exactly enumerates
`P=2` full-drop ordered graphs and minimizes the largest regular induced
subgraph.  The commands

```text
python3 82/EXPERIMENTS/full_drop_regular_min.py 5 --p 2
python3 82/EXPERIMENTS/full_drop_regular_min.py 6 --p 2
python3 82/EXPERIMENTS/full_drop_regular_min.py 7 --p 2
python3 82/EXPERIMENTS/full_drop_regular_min.py 8 --p 2
python3 82/EXPERIMENTS/full_drop_regular_min.py 9 --p 2
```

give

```text
n=5: min_max_regular=3
n=6: min_max_regular=3
n=7: min_max_regular=4
n=8: min_max_regular=4
n=9: min_max_regular=4.
```

Together with the `n=10` obstruction to regular `5`-sets and the
`C_full^reg(2,5)=11` computation, this gives

```text
n=10: min_max_regular=4,       n=11: min_max_regular=5.
```

These data support the sharp fixed-`P=2` possibility that every `P=2`
full-drop ordered graph on `n` vertices has a regular induced subgraph of
order at least `floor((n-1)/2)`, with Lemma 28D.6c showing this would be
best possible up to the endpoint.

For the next order, the command

```text
python3 82/EXPERIMENTS/full_drop_census.py 12 --p 2 --search-regular-h 6 --max-nodes 300000 --progress 100000
```

finds a `P=2` full-drop ordered graph on `12` vertices with no regular
induced subgraph of order `6`, proving computationally that

```text
C_full^reg(2,6)>12.
```

One certificate has columns

```text
0,0,1,2,0,0,0,120,248,504,1023,1023,
```

with `max_full_drop=1`, `clique_number=5`, `independence_number=5`, and
`max_regular=5`.

The helper `EXPERIMENTS/full_drop_alpha_omega.py` tests a stronger possible
`P=2` theorem, suggested by Lemma 28D.5b:

```text
alpha(H)+omega(H) >= (|V(H)|+3)/2
```

for every `P=2` full-drop ordered graph `H`.  Exact DFS enumeration at
`n=8` and `n=9`,

```text
python3 82/EXPERIMENTS/full_drop_alpha_omega.py 8 --p 2 --progress 20000
python3 82/EXPERIMENTS/full_drop_alpha_omega.py 9 --p 2 --progress 100000
```

check respectively all `58,604` and `366,012` ordered graphs satisfying the
condition.  The `n=8` run reports

```text
best_alpha=4,       best_omega=2,       best_sum=6.
```

The extremal columns are

```text
0,0,0,0,1,2,4,8,
```

that is, a matching of size `4` ordered with all left endpoints first.  The
`n=9` run also has `best_sum=6`, with extremal columns

```text
0,0,1,2,0,0,16,48,96.
```

The same script reports the best independence number in each clique-number
bucket.  At `n=8`, the bucket summary is

```text
omega=1: min_alpha=8
omega=2: min_alpha=4
omega=3: min_alpha=3
omega=4: min_alpha=2
omega=5: min_alpha=2
omega=6: min_alpha=2
omega=7: min_alpha=2
omega=8: min_alpha=1.
```

At `n=9`, the bucket summary is

```text
omega=1: min_alpha=9
omega=2: min_alpha=4
omega=3: min_alpha=3
omega=4: min_alpha=2
omega=5: min_alpha=2
omega=6: min_alpha=2
omega=7: min_alpha=2
omega=8: min_alpha=2
omega=9: min_alpha=1.
```

The same script now also reports first-degree refinements of these buckets.
For example, at `n=8` the tight `omega=4`, `alpha=2` examples occur with
first degree `3,4,5,6`, while at `n=9` the only tight `omega=4`,
`alpha=2` bucket found by the exact enumeration has first degree `6`.  This
suggests that the next fixed-clique case after Lemma 28D.5b.3 must handle
large first neighborhoods rather than the low-degree induction cases.

The script `EXPERIMENTS/full_drop_p2_gap_audit.py` audits the complementary
question after Lemma 28D.5b.3 and Corollary 28D.5b.6: among graphs not already
covered by `omega<=3` or by high first degree, how far can the simple
induction on the nonneighbors of the first vertex fall short?  Exact runs

```text
python3 82/EXPERIMENTS/full_drop_p2_gap_audit.py 8
python3 82/EXPERIMENTS/full_drop_p2_gap_audit.py 9 --progress 200000
```

again find no violation of

```text
alpha(H)+omega(H) >= ceil((|V(H)|+3)/2).
```

The theorem-level lower bound obtained by applying only the conjectured
inequality to the first-vertex nonneighbor side is short by at most one in
both exact audits (`max_induction_gap=1`).  However, using the actual
`alpha` of that nonneighbor side closes the gap in all enumerated cases:
`max_actual_gap=0` at `n=8` and `max_actual_gap=-1` at `n=9`.  This suggests
that a full proof of the `P=2` alpha-plus-omega conjecture should show that
the first-vertex nonneighbor side cannot itself be extremal in precisely the
cases where the naive induction is one short.

The same audit also verifies Lemmas 28D.5b.9 and 28D.5b.10 on these exact
censuses: both runs report

```text
part_rule_violations=0
singleton_order_violations=0.
```

This is only finite calibration, but it supports the possibility that the
current quadratic upper bound for `C_full(2,h)` is far from sharp.

**Lemma 28E: Ordered Graphs With Few Inversions Have Large Homogeneous
Sets.**  Let `H` be a graph whose vertices are linearly ordered as
`v_1,...,v_m`.  Call a triple `i<j<k` an inversion if

```text
v_i v_j in E(H),       v_i v_k notin E(H).
```

If the total number of inversions is less than

```text
binom(m,3) / binom(s,3)
```

for some integer `m>=s>=3`, then `H` contains a clique or independent set
of order at least `sqrt(s)`.

Proof.  Choose a uniformly random `s`-element subset of the ordered vertex
set.  The expected number of inversions inside it is less than `1`, so some
`s`-subset has no inversion.  Restrict to such a subset, preserving the
inherited order.

Define a relation `prec` on this subset by

```text
v_i prec v_j       iff       i<j and v_i v_j in E(H).
```

The relation is transitive: if `i<j<k`, `v_i v_j` is an edge, and
`v_j v_k` is an edge, then the absence of inversions forces `v_i v_k` to be
an edge.  Hence `prec` is a partial order.  Chains in this partial order are
cliques of `H`, and antichains are independent sets of `H`, because two
vertices are comparable exactly when they are adjacent.

In every finite partial order, the product of the largest chain size and the
largest antichain size is at least the number of elements: otherwise the
levels by longest-chain length would give fewer than `s` elements.  Therefore
this `s`-vertex inversion-free induced subgraph contains a clique or
independent set of order at least `sqrt(s)`.  QED.

**Lemma 28E.1: Sparse Inversions Give Large Homogeneous Sets.**  Let `H` be a
graph whose `m` vertices are linearly ordered.  Let `I` be the number of
inversion triples in this order.  If `m>=2s` and

```text
I < m^3/(8s^2),
```

then `H` contains a clique or independent set of order greater than
`sqrt(s)`.

Proof.  Choose a random subset `R` of the ordered vertex set by keeping each
vertex independently with probability

```text
p=2s/m.
```

The assumption `m>=2s` makes `p<=1`.  The expected value of

```text
|R| - #{inversion triples contained in R}
```

is

```text
pm - p^3 I > 2s - (8s^3/m^3)(m^3/(8s^2)) = s.
```

Thus some choice of `R` has `|R|` minus its number of inversion triples larger
than `s`.  Delete one vertex from each inversion triple in `R`.  The remaining
ordered set has more than `s` vertices and no inversion triple.

As in Lemma 28E, on an inversion-free ordered set the relation

```text
v_i prec v_j       iff       i<j and v_i v_j in E(H)
```

is a partial order whose chains are cliques and whose antichains are
independent sets.  The chain-antichain product bound gives a clique or
independent set of order greater than `sqrt(s)`.  QED.

**Computational Calibration 28E.2: Inversion-Free Graphs Do Not Show A
Large Extra Gain.**  The script `EXPERIMENTS/no_inversion_regular.py`
enumerates or samples ordered graphs with no inversion triples.  Such a graph
is encoded by thresholds `t_i`, where vertex `i` is adjacent to a later vertex
`j` exactly when `j>=t_i`.

Exact enumeration gives:

```text
python3 82/EXPERIMENTS/no_inversion_regular.py 8 --exact
python3 82/EXPERIMENTS/no_inversion_regular.py 9 --exact --progress 100000
```

For `m=8`, among all `40320` threshold sequences, the minimum possible
maximum regular induced order is `4`; the minimum possible maximum homogeneous
order is `3`.  For `m=9`, among all `362880` threshold sequences, the same
minimum maximum regular order is `4`, while the minimum maximum homogeneous
order is again `3`.  One extremal `m=9` threshold sequence is

```text
(1, 2, 5, 5, 7, 9, 9, 9, 9).
```

Random samples at larger orders found:

```text
python3 82/EXPERIMENTS/no_inversion_regular.py 14 --samples 500 --seed 82014 --progress 100
python3 82/EXPERIMENTS/no_inversion_regular.py 16 --samples 200 --seed 82016 --progress 50
```

with smallest sampled maximum regular orders `6` and `6`, respectively.
The same script also has a threshold-mutation mode.  For example,

```text
python3 82/EXPERIMENTS/no_inversion_regular.py 16 --hill-climb 80 --restarts 3 --seed 816 --progress 40 --temperature 0.4
python3 82/EXPERIMENTS/no_inversion_regular.py 20 --samples 100 --seed 8220 --progress 20
```

found examples with maximum regular orders `6` and `7`, respectively.  These
checks do not prove an upper construction, but they suggest that the
inversion-free step may at best improve the chain-antichain `sqrt(m)` bound by
small constants or logarithmic factors.  A proof route that needs a power
improvement inside Lemma 28E.1 should therefore first produce a structural
reason not visible in the full class of inversion-free ordered graphs.

The fixed-threshold witness mode gives a little more information about the
current hard examples:

```text
python3 82/EXPERIMENTS/no_inversion_regular.py 16 --thresholds 6,11,4,10,12,7,7,12,14,11,13,16,16,14,15,16
python3 82/EXPERIMENTS/no_inversion_regular.py 20 --thresholds 4,14,11,6,17,10,7,18,17,14,13,12,19,16,18,19,17,19,19,20
```

In both cases the largest regular witness printed by the script is an
independent set, of orders `6` and `7`.  Thus these particular inversion-free
examples are not hiding larger mixed regular witnesses; their obstruction is
already visible at the homogeneous chain-antichain level.

**Lemma 28E.3: The Homogeneous Bound In Inversion-Free Graphs Is Sharp.**
For every integer `q>=2`, there is an inversion-free ordered graph on `q^2`
vertices whose largest clique or independent set has order exactly `q`.

Proof.  Put the vertices in the order

```text
1,2,...,q^2
```

and join `i<j` if and only if

```text
j-i >= q.
```

This graph is inversion-free: if `i<j<k` and `ij` is an edge, then
`j-i>=q`, hence `k-i>=q`, so `ik` is also an edge.

In any clique, consecutive selected vertices in the ambient order differ by
at least `q`.  Thus a clique of order `r` spans distance at least
`(r-1)q`, which is at most `q^2-1`; hence `r<=q`.  This is sharp because

```text
1, 1+q, 1+2q, ..., 1+(q-1)q
```

is a clique of order `q`.

In any independent set, no two selected vertices differ by at least `q`.
Therefore all selected vertices lie in an interval of length at most `q-1`,
so the independent set has order at most `q`.  This is sharp because
`{1,...,q}` is independent.  QED.

This lemma shows that Lemma 28E's final chain-antichain step cannot be
improved, in general, if the output sought from an inversion-free ordered
graph is only a clique or independent set.  It does not rule out finding
larger mixed regular induced subgraphs in special inversion-free graphs; for
example, the sliding-window graph above itself contains large complete
multipartite regular induced subgraphs.  The obstruction is specifically to
the homogeneous extraction used in Proposition 28F.

**Lemma 28E.3a: The Sliding-Window Example Is Regularly Easy.**  In the
sliding-window graph from Lemma 28E.3 on vertices `1,...,q^2`, where
`ij` is an edge exactly when `|i-j|>=q`, there is a regular induced subgraph
on at least

```text
(q-1)(floor((q^2-q+1)/(2q-2))+1) = (1/2+o(1))q^2
```

vertices.

Proof.  Put `s=q-1` and `d=2q-2`.  For every integer

```text
0 <= t <= floor((q^2-q+1)/(2q-2)),
```

take the block

```text
B_t={1+td, 2+td, ..., q-1+td}.
```

The displayed upper bound on `t` is exactly the condition that the last
vertex of `B_t` is at most `q^2`.  Inside a single block, all pairwise
distances are at most `q-2`, so the block is independent.  Between consecutive
blocks, the distance from the last vertex of `B_t` to the first vertex of
`B_{t+1}` is

```text
(1+(t+1)d) - (q-1+td) = q,
```

so every vertex of `B_t` is adjacent to every vertex of every later block.
Thus the union of these blocks induces a complete multipartite graph with
equal part size `q-1`.  It is therefore regular, and its order is the
displayed number.  QED.

**Definition 28E.4: The Column-Drop Ordered Parameter.**  For integers
`P,h>=1`, let `C_drop(P,h)` be the least integer `m` such that every ordered
graph `H` on vertices

```text
v_1<...<v_m
```

with

```text
|{ i<j : v_i v_j in E(H), v_i v_k notin E(H) }| < P
```

for every ordered pair `j<k`, contains a clique or independent set of order
`h`.

The condition says that, as one moves from column `j` to a later column `k`,
fewer than `P` earlier rows are lost from the earlier-neighborhood.  The
representative graph in Proposition 28F satisfies exactly this stronger
pointwise condition, not merely a bound on the total number of inversions.

**Lemma 28E.4a: Clique-Rank Constraint Under Column Drop.**  Let `H` be an
ordered graph on

```text
v_1<...<v_m
```

satisfying the defining column-drop condition with parameter `P`.  For each
`j`, let `rho(j)` be the largest order of a clique whose maximum vertex in
the order is `v_j`.  If `a<b` and `v_a v_b` is an edge, then

```text
rho(b) >= rho(a)-P+2.
```

Consequently, if `rho(a) >= rho(b)+P-1`, then `v_a v_b` is not an edge.

Proof.  Let `C` be a clique of order `rho(a)` whose maximum vertex is `v_a`.
Every vertex of `C\{v_a}` has index below `a` and is adjacent to `v_a`.
Apply the column-drop condition to the pair `a<b`.  Fewer than `P` earlier
vertices are adjacent to `v_a` and nonadjacent to `v_b`.  Hence at least

```text
rho(a)-1-(P-1) = rho(a)-P
```

vertices of `C\{v_a}` are also adjacent to `v_b`.  These vertices, together
with `v_a` and `v_b`, form a clique whose maximum vertex is `v_b`, because
`C` was already a clique and `v_a v_b` is an edge.  Therefore
`rho(b)>=rho(a)-P+2`.

The final assertion is the contrapositive: if `v_a v_b` were an edge, the
displayed inequality would give `rho(b)>=rho(a)-P+2`, contradicting
`rho(a)>=rho(b)+P-1`.  QED.

**Lemma 28E.5: Exact Value At One Drop.**  For every `h>=2`,

```text
C_drop(1,h) = (h-1)^2+1.
```

Proof.  The condition with `P=1` says that the displayed set is empty for
every `j<k`, which is exactly the absence of inversion triples.  Lemma 28E,
applied with `s=m`, shows that every inversion-free ordered graph on `m`
vertices has a clique or independent set of order at least `sqrt(m)`.
Therefore `m>(h-1)^2` forces a clique or independent set of order at least
`h`, so

```text
C_drop(1,h) <= (h-1)^2+1.
```

For the reverse inequality, apply Lemma 28E.3 with `q=h-1`.  It gives an
inversion-free ordered graph on `(h-1)^2` vertices whose largest clique or
independent set has order exactly `h-1`.  Hence
`C_drop(1,h)>(h-1)^2`, proving equality.  QED.

**Lemma 28E.6: Global Reduction Through The Column-Drop Parameter.**  For
every `h>=3`, with `P=P_h`,

```text
G(h) <= 2 P(h-1) C_drop(P,h).
```

Proof.  Let `G` be a graph with no regular induced subgraph on at least `h`
vertices.  Partition its vertices into exact global degree classes.  By
Corollary 28D.2, every nonempty degree class has size at most `2P(h-1)`.

Choose one representative from each nonempty degree class and order the
representatives by increasing global degree:

```text
v_1<...<v_b.
```

For `j<k`, Lemma 28D gives

```text
|N(v_j)\N(v_k)| < P,
```

because `deg(v_j)<deg(v_k)`.  Therefore, in the ordered representative graph,
the number of earlier vertices `v_i`, `i<j`, such that `v_i v_j` is an edge
and `v_i v_k` is not an edge is also less than `P`.  Thus the representative
graph satisfies the defining column-drop condition for `C_drop(P,h)`.

If `b>=C_drop(P,h)`, the representative graph contains a clique or
independent set of order `h`.  The same vertices form a clique or independent
set in `G`, hence a regular induced subgraph on `h` vertices, contradiction.
So

```text
b < C_drop(P,h).
```

Multiplying the number of degree classes by the maximum degree-class size
gives

```text
|V(G)| <= 2P(h-1) (C_drop(P,h)-1) < 2P(h-1) C_drop(P,h).
```

Therefore every graph on at least `2P(h-1) C_drop(P,h)` vertices has a
regular induced subgraph on at least `h` vertices, proving the displayed
bound for `G(h)`.  QED.

Before the full-drop refinement in Corollary 28D.6, this gave the polynomial
reduction through the crude
estimate

```text
C_drop(P,h) <= 4P h^4+1,
```

which follows by summing the column-drop bounds to get fewer than
`P binom(m,2)` total inversions and then applying Lemma 28E.1 with
`s=h^2`.  Lemma 28E.5 shows that this crude route loses real information:
at `P=1`, the exact value is quadratic in `h`, while the sparse-inversion
estimate gives only a quartic bound.  Corollary 28D.6 now bypasses this loss
by using the stronger full-drop condition; the column-drop parameter remains
useful as a diagnostic for what can and cannot be proved from the weaker
earlier-row information alone.

**Computational Calibration 28E.7: Small Column-Drop Values.**  The script
`EXPERIMENTS/column_drop_census.py` exactly enumerates labelled ordered graphs
with bounded maximum column drop.  The commands

```text
python3 82/EXPERIMENTS/column_drop_census.py 6 --p 2
python3 82/EXPERIMENTS/column_drop_census.py 7 --p 2 --progress 500000
python3 82/EXPERIMENTS/column_drop_census.py 6 --p 3
```

report:

```text
P=2, n=6:  checked_column_drop=15920,  min_max_homogeneous=3
P=2, n=7:  checked_column_drop=480776, min_max_homogeneous=3
P=3, n=6:  checked_column_drop=30256,  min_max_homogeneous=3
```

Thus, for example, the exact census proves

```text
C_drop(2,4) > 7.
```

This is only a small finite calibration, but it confirms that the
column-drop parameter is not collapsing immediately to the inversion-free
case once one drop per column pair is allowed.

The same script also has a depth-first construction mode.  The command

```text
python3 82/EXPERIMENTS/column_drop_census.py 12 --p 2 --search-h 4 --max-nodes 100000 --progress 20000
```

finds the column sequence

```text
0,0,1,1,3,6,14,38,78,87,319,415
```

with labelled mask

```text
7508164912550504206.
```

Fixed-mask inspection,

```text
python3 82/EXPERIMENTS/column_drop_census.py 12 --mask 7508164912550504206
```

reports maximum column drop `1` and maximum homogeneous order `3`.  Hence the
search certificate proves the stronger finite lower calibration

```text
C_drop(2,4) > 12.
```

The same fixed-mask inspection also reports a regular induced subgraph of
order `6` in this ordered graph.  Thus this homogeneous column-drop
obstruction is not a regular obstruction for the representative step in the
global problem.  To separate these notions, `column_drop_census.py` has a
regular-aware search mode:

```text
python3 82/EXPERIMENTS/column_drop_census.py 10 --p 1 --search-regular-h 5
python3 82/EXPERIMENTS/column_drop_census.py 12 --p 1 --search-regular-h 6
python3 82/EXPERIMENTS/column_drop_census.py 13 --p 2 --search-regular-h 5
```

These produce ordered graphs with maximum column drop respectively `0,0,1`
and largest regular induced orders `4,5,4`.  The data suggest that replacing
homogeneous extraction by regular extraction may improve constants or small
parameters in the degree-bucket representative argument, but it does not yet
give a theorem-level improvement over the full-drop reduction.

One small exact lower calibration for the regular column-drop parameter is
the following.  The ordered graph on `12` vertices with edge mask

```text
25366485577502803966
```

has maximum column drop `0` and largest regular induced subgraph of order
`4`, verified by

```text
python3 82/EXPERIMENTS/column_drop_census.py 12 \
  --mask 25366485577502803966
```

Thus

```text
C_reg(1,5)>12.
```

The dedicated suffix-threshold search
`EXPERIMENTS/threshold_regular_dfs.py` closes this finite case and the two
previous nontrivial cases.  For
`P=1`, the column-drop condition means exactly that each row's later
neighborhood is a suffix, so when the ordered graph is built one column at a
time, the next column is obtained from the previous one by turning on an
arbitrary subset of rows that were still off, together with an arbitrary
choice for the immediate predecessor.  The command

```text
python3 82/EXPERIMENTS/threshold_regular_dfs.py 13 --h 5 --progress 0
```

exhausts this search tree and reports

```text
n=13
h=5
nodes=186020
status=unsat
```

Thus every inversion-free ordered graph on `13` vertices has a regular
induced subgraph on at least `5` vertices.  Combining this exact upper
calibration with the `12`-vertex lower example gives

```text
C_reg(1,5)=13.
```

The same exact DFS gives

```text
C_reg(1,3)=5,       C_reg(1,4)=7.
```

The lower certificates are found at `n=4` for `h=3` and at `n=6` for `h=4`;
the next orders are exhausted with status `unsat`.

For the next value, the same script quickly finds a `13`-vertex lower
certificate:

```text
python3 82/EXPERIMENTS/threshold_regular_dfs.py 13 --h 6 --progress 0
```

with threshold sequence

```text
2,4,6,8,9,13,13,13,11,10,13,12,13
```

and maximum regular induced order `5`.  Thus

```text
C_reg(1,6)>13.
```

By contrast, Lemma 28E.5 gives `C_drop(1,5)=17`.  Thus even in the first
nontrivial regular column-drop case, regular extraction improves the
homogeneous column-drop bound.  The improvement is finite and does not yet
give a theorem-level asymptotic gain over the full-drop reduction, but it
confirms that the regular representative step is genuinely sharper than the
chain-antichain extraction.

**Definition 28E.8: The Regular Column-Drop Parameter.**  For integers
`P,h>=1`, let `C_reg(P,h)` be the least integer `m` such that every ordered
graph on `m` vertices satisfying the column-drop condition

```text
|{ i<j : v_i v_j in E(H), v_i v_k notin E(H) }| < P
```

for every ordered pair `j<k` contains a regular induced subgraph on at least
`h` vertices.

Since cliques and independent sets are regular,

```text
C_reg(P,h) <= C_drop(P,h).
```

**Lemma 28E.9: Global Reduction Through Regular Column Drop.**  For every
`h>=3`, with `P=P_h`,

```text
G(h) <= 2 P(h-1) C_reg(P,h).
```

Proof.  Let `G` be a graph with no regular induced subgraph on at least `h`
vertices.  Partition `V(G)` into exact global degree classes.  By Corollary
28D.2, every nonempty degree class has size at most `2P(h-1)`.

Choose one representative from each nonempty degree class and order the
representatives by increasing degree.  As in Lemma 28E.6, Lemma 28D implies
that this ordered representative graph satisfies the column-drop condition
with parameter `P`: for `j<k`, fewer than `P` earlier representatives are
adjacent to `v_j` and nonadjacent to `v_k`.

If the number of representatives were at least `C_reg(P,h)`, then the
representative graph would contain a regular induced subgraph on at least
`h` vertices.  The same vertex set induces the same graph inside `G`, so this
would be a forbidden regular induced subgraph of `G`.  Hence there are fewer
than `C_reg(P,h)` nonempty degree classes.  Multiplying by the degree-class
size bound gives

```text
|V(G)| < 2P(h-1) C_reg(P,h).
```

Therefore every graph on at least `2P(h-1) C_reg(P,h)` vertices contains a
regular induced subgraph on at least `h` vertices.  QED.

This is formally sharper than Lemma 28E.6.  It would prove Problem 82 under
the target

```text
P_h C_reg(P_h,h) = 2^{o(h)}.
```

At present this is not known to be easier than proving `P_h=2^{o(h)}`:
Lemma 28G shows that the balanced pair parameter itself has the same
subexponential scale as `G`.

**Proposition 28F: Polynomial Global Reduction To The Balanced Pair
Parameter.**  For every `h>=3`,

```text
G(h) <= 8 h^2 P_h^2.
```

Consequently, a proof that `P_h=2^{o(h)}` would prove Erdős Problem 82.

Proof.  This is the final inequality of Corollary 28D.6.  If
`P_h=2^{o(h)}`, then the polynomial factor `8h^2` is also
`2^{o(h)}`, so the displayed inequality gives `G(h)=2^{o(h)}`.  This is the
inverse form of `F(n)/log n -> infinity`.  QED.

**Lemma 28G: The Balanced Pair Parameter Has The Same Subexponential Scale As
`G`.**  For every `h>=3`,

```text
G(ceil(h/2)) <= P_h <= ceil(G(h)/2).
```

Consequently,

```text
P_h=2^{o(h)}    iff    G(h)=2^{o(h)}.
```

Proof.  The upper bound is immediate from the definition of `G(h)`: if
`M>=ceil(G(h)/2)`, then any graph on two marked parts of size `M` has at
least `G(h)` vertices, and therefore already satisfies the first alternative
in the definition of `P_h`.

For the lower bound, put `k=ceil(h/2)` and let `J` be a graph on
`G(k)-1` vertices with no regular induced subgraph on at least `k` vertices.
Let `H` be the disjoint union of two copies of `J`, with one copy marked as
`A` and the other as `B`.  Then `H` has no regular induced subgraph on at
least `h` vertices: if `S=S_A union S_B` were regular in the disjoint union,
then each nonempty `S_A,S_B` would induce a regular graph of the same degree,
and if `|S|>=h`, at least one of `S_A,S_B` would have order at least
`ceil(h/2)=k`, contradicting the choice of `J`.

Now let `r=ceil((h-2)/2)`.  Since there are no edges between `A` and `B`, no
sets `X subset A`, `Y subset B` with `|X|=|Y|=r` can make
`H[X union Y]` `r`-regular: every vertex has at most `r-1` possible neighbors
inside its own side and none across the cut.  Thus the plus version of the
balanced pair property fails for side size `G(k)-1`, so
`P_h^+>=G(k)`.  By Lemma 28B, `P_h=P_h^+`, proving the lower bound.

If `G(h)=2^{o(h)}`, the displayed upper bound gives `P_h=2^{o(h)}`.  The
reverse implication is Proposition 28F.  QED.

This lemma clarifies the role of the pair route.  It does not make the
problem easier by changing the exponential scale: the local parameter is
subexponentially equivalent to `G`.  The gain is structural.  Proposition 28F
shows that controlling the marked two-part obstruction automatically controls
all global counterexamples with only a polynomial loss.

**Corollary 28G.1: Polynomial Lower Calibration For `P_h`.**  The
self-contained random lower bound of Proposition 0F gives an absolute
constant `c>0` such that, for all sufficiently large `h`,

```text
P_h >= c h^{3/2}/sqrt(log h).
```

Using the recorded Dyson--McKay lower construction

```text
G(k) >= (9/163) k^2
```

for all large `k`, one obtains the stronger literature-dependent calibration

```text
P_h >= (9/652+o(1)) h^2.
```

Proof.  Lemma 28G gives

```text
P_h >= G(ceil(h/2)).
```

Substituting `k=ceil(h/2)` into Proposition 0F proves the first display,
after changing the absolute constant.  Substituting the recorded
Dyson--McKay lower bound gives

```text
P_h >= (9/163) ceil(h/2)^2 = (9/652+o(1))h^2.
```

QED.

Thus the explicit linear parity obstruction below is not the dominant known
lower scale for `P_h`; its value is structural, because it exhibits an
infinite cross-profile obstruction not inherited from disjoint copies of
ordinary regular-induced-subgraph counterexamples.

**Lemma 28H: Spectrum-Disjoint Disjoint-Union Lower Bounds For `P_h`.**  Let
`J_1,J_2` be two graphs on the same number `M` of vertices.  Suppose:

1. neither `J_i` has a regular induced subgraph on at least `h` vertices;
2. there are no regular induced subgraphs `R_i subset J_i` of the same degree
   with

```text
|R_1|+|R_2| >= h.
```

Then `P_h>M`.

Proof.  Form a graph `H` by taking the disjoint union of `J_1` and `J_2`,
and mark the two components as `A` and `B`.  Because there are no edges
between `A` and `B`, no balanced sets `X subset A`, `Y subset B` with
`|X|=|Y|=r=ceil((h-2)/2)` can make `H[X union Y]` `r`-regular: every vertex
has at most `r-1` possible neighbors inside its own marked side.

It remains to check that `H` has no regular induced subgraph on at least
`h` vertices.  A regular induced subgraph of a disjoint union is either
contained in one component, excluded by (1), or is a disjoint union of
regular induced subgraphs of the two components with the same degree.  The
latter case is excluded by (2).  Therefore `H` fails both alternatives in the
definition of `P_h^+` at side size `M`, so `P_h^+>M`.  Lemma 28B gives
`P_h=P_h^+`, hence `P_h>M`.  QED.

Lemma 28G is the special case where both `J_i` have no regular induced
subgraph of order at least `ceil(h/2)`.  Lemma 28H shows that larger local
lower bounds may be possible by separating the regular degree spectra of the
two marked components, not only by making each component hard below half the
target order.  The script `EXPERIMENTS/regular_spectrum.py` computes these
spectra and checks the condition in (2) for fixed masks.

There is a simple explicit instance of this spectrum separation.  For every
`h>=5`,

```text
D_spec(h) >= h,       P_h >= h.
```

Indeed, take `M=h-1`, let `J_1` be the disjoint union of one edge and
`h-3` isolated vertices, and let `J_2=K_{h-1}`.  Neither graph has `h`
vertices.  In `J_1`, the largest `0`-regular induced subgraph has order
`h-2`, the largest `1`-regular induced subgraph has order `2`, and no regular
induced subgraph has degree at least `2`.  In `J_2`, the largest regular
subgraph of degree `d` has order `d+1`.  Thus the largest same-degree total
orders are `h-1` for `d=0`, `4` for `d=1`, and at most `h-1` for all other
degrees.  Since `h>=5`, no same-degree pair has total order at least `h`.
Lemma 28H gives `P_h>h-1`, and the definition of `D_spec` gives
`D_spec(h)>h-1`.

The same idea can be pushed a little further with split spectra.  For every
`h>=5`, set

```text
r=floor((h-1)/2),        M=floor((h-3+r+h-1)/2).
```

Let

```text
J_1=K_r union I_{M-r},        J_2=K_{h-1} union I_{M-h+1},
```

where `I_t` denotes an independent set of order `t`.  Then

```text
D_spec(h)>M,        P_h>M.
```

Indeed, in a graph `K_a union I_b`, the largest `0`-regular induced subgraph
has order `b+1`, and the largest positive-degree `d`-regular induced subgraph
has order `d+1` for `1<=d<a` and order `0` for `d>=a`.  Neither `J_i` has a
regular induced subgraph on `h` vertices: the clique parts have sizes `r` and
`h-1`, while

```text
(M-r)+1<h,        (M-h+1)+1<h.
```

For degree `0`, the two largest side witnesses have total order

```text
(M-r+1)+(M-h+2)=2M-r-h+3 <= h-1,
```

by the definition of `M`.  For positive degrees common to both spectra, the
degree is at most `r-1`, so the largest same-degree total order is at most

```text
2r <= h-1.
```

Thus no same-degree pair reaches total order `h`, and Lemma 28H gives the
claimed lower bound.  The verifier
`EXPERIMENTS/split_spectrum_construction.py` checks these spectrum summaries
for finite ranges.

For example, with `h=6` and component order `M=5`, the masks

```text
478,       35
```

have regular spectra

```text
1:0 2:0 2:1 3:2,
1:0 2:0 2:1 3:0,
```

respectively.  The only order-`3` regular subgraphs have different degrees,
so no same-degree pair reaches total order `6`.  Lemma 28H therefore gives a
disjoint-union proof of `P_6>5`, verified by

```text
python3 82/EXPERIMENTS/regular_spectrum.py 5 --h 6 --mask-a 478 --mask-b 35
```

The same mechanism reaches the current small `P_7` calibration.  For `h=7`
and component order `M=7`, the masks

```text
287010,       2096239
```

have spectra

```text
1:0 2:0 2:1 3:0 3:2 4:0 4:1,
1:0 2:0 2:1 3:2 4:3 5:4.
```

For each degree, the largest same-degree orders in the two components sum to
at most `6`, so Lemma 28H gives a disjoint-union proof of `P_7>7`.  This is
verified by

```text
python3 82/EXPERIMENTS/regular_spectrum.py 7 --h 7 --mask-a 287010 --mask-b 2096239
```

A random spectrum search also finds the next instance: for `h=8`, the masks

```text
7877621,       155665244
```

on `8` vertices have no same-degree regular spectrum entries whose orders sum
to `8`, giving `P_8>8` by the same disjoint-union mechanism.  The verification
command is

```text
python3 82/EXPERIMENTS/regular_spectrum.py 8 --h 8 --mask-a 7877621 --mask-b 155665244
```

Two more finite calibrations were found by the same disjoint-spectrum search.
For `h=9`, the following masks on `10` vertices have maximum same-degree total
`8`:

```text
11928016833367,       5536596681199
```

and hence give

```text
D_spec(9)>10,        P_9>10.
```

For `h=10`, the following masks on `12` vertices have maximum same-degree
total `9`:

```text
57469909479292894705,       7851332248695866876
```

and hence give

```text
D_spec(10)>12,       P_10>12.
```

The verification commands are

```text
python3 82/EXPERIMENTS/regular_spectrum.py 10 --h 9 \
  --mask-a 11928016833367 --mask-b 5536596681199
python3 82/EXPERIMENTS/regular_spectrum.py 12 --h 10 \
  --mask-a 57469909479292894705 --mask-b 7851332248695866876
```

Random probes with component orders `13` and `14` for `h=10` did not find a
disjoint-spectrum obstruction; the best sampled maximum same-degree totals
were `10` and `11`, respectively.  Thus the current finite data suggest that
the disjoint-spectrum obstruction grows past the target, but not rapidly in
these small cases.

**Corollary 28I: The Spectrum-Matching Parameter Is A Lower Subproblem.**  Let
`D_spec(h)` be the least integer `M` with the following property: for every
pair of graphs `J_1,J_2` on `M` vertices, either one of the two graphs has a
regular induced subgraph on at least `h` vertices, or there are regular
induced subgraphs `R_i subset J_i` of the same degree with

```text
|R_1|+|R_2| >= h.
```

Then

```text
G(ceil(h/2)) <= D_spec(h) <= G(h),
P_h >= D_spec(h).
```

In particular,

```text
D_spec(h)=2^{o(h)}    iff    G(h)=2^{o(h)}.
```

Proof.  The upper bound `D_spec(h)<=G(h)` is immediate: if each `J_i` has
`G(h)` vertices, then each graph separately has a regular induced subgraph on
at least `h` vertices.

For the lower bound, let `k=ceil(h/2)` and take two copies of a graph on
`G(k)-1` vertices with no regular induced subgraph on at least `k` vertices.
No regular subgraphs in the two copies can have total order at least `h`,
because then one copy contributes at least `k` vertices.  Hence the
spectrum-matching property fails below `G(k)`.

Finally, if `M<D_spec(h)`, there is a pair `J_1,J_2` failing the
spectrum-matching property.  Lemma 28H gives `P_h>M`.  Since this holds for
every `M<D_spec(h)`, we get `P_h>=D_spec(h)`.  QED.

Thus the local pair problem contains a purely one-component spectral
matching problem before any cross-edge structure appears.  The displayed
sandwich also shows that this spectral matching problem is subexponentially
equivalent to Erdős Problem 82 itself: if `D_spec(h)=2^{o(h)}`, then
`G(t)<=D_spec(2t)=2^{o(t)}`, while the reverse implication follows from
`D_spec(h)<=G(h)`.

**Corollary 28J: A Homogeneous Ramsey Upper Bound For `D_spec`.**  Let
`k=ceil(h/2)`.  Then

```text
D_spec(h) <= R(k,h).
```

Proof.  Let `J_1,J_2` be two graphs on `M>=R(k,h)` vertices.  If either graph
has an independent set of order `h`, then it has a regular induced subgraph
on at least `h` vertices and the first alternative in the definition of
`D_spec(h)` holds.

Otherwise, Ramsey's theorem gives a clique of order at least `k` in each
`J_i`.  Taking a `k`-clique in each graph gives two regular induced subgraphs
of the same degree `k-1` and total order `2k>=h`.  Thus the spectrum-matching
alternative holds.  QED.

This upper bound is only exponential in `h`; it is the spectrum analogue of
the ordinary Ramsey bound.  To prove `D_spec(h)=2^{o(h)}`, and hence to remove
this disjoint-union obstruction to the pair route, one must use
nonhomogeneous regular spectrum entries rather than only cliques and
independent sets.

**Conditional Corollary 28J.1: Spectrum Mass Would Give Quadratic
`D_spec`.**  For a graph `J`, let

```text
s_d(J)=max{|S| : J[S] is d-regular},
```

with `s_d(J)=0` if there is no induced `d`-regular subgraph.  Suppose that
every `M`-vertex graph `J` satisfies the spectrum-mass inequality

```text
sum_d s_d(J) >= M.
```

Then

```text
D_spec(h) <= floor((h-1)^2/2)+1.
```

Proof.  Let

```text
M >= floor((h-1)^2/2)+1,
```

and let `J_1,J_2` be graphs on `M` vertices.  If either graph has a regular
induced subgraph on at least `h` vertices, then the first alternative in the
definition of `D_spec(h)` holds.

Otherwise every regular induced subgraph in either graph has order at most
`h-1`.  Hence only degrees `0,1,...,h-2` can contribute to the spectra.  Put
`s_d=s_d(J_1)` and `t_d=s_d(J_2)`.  If the spectrum-matching alternative
failed, then for every `d`,

```text
s_d+t_d <= h-1.
```

Summing over the `h-1` possible degrees gives

```text
sum_d s_d + sum_d t_d <= (h-1)^2.
```

But the assumed spectrum-mass inequality gives

```text
sum_d s_d + sum_d t_d >= 2M > (h-1)^2,
```

contradiction.  Therefore some degree `d` has `s_d+t_d>=h`, which is exactly
the spectrum-matching alternative.  QED.

**Conditional Corollary 28J.1a: Spectrum Mass Would Solve The Problem
Polynomially.**  If every graph `J` satisfies

```text
sum_d s_d(J) >= |V(J)|,
```

then for every `k>=2`,

```text
G(k) <= floor((2k-1)^2/2)+1 < 2k^2.
```

Consequently `F(n)/log n -> infinity`.

Proof.  Apply Corollary 28I with `h=2k`, giving

```text
G(k) <= D_spec(2k).
```

Conditional Corollary 28J.1 gives

```text
D_spec(2k) <= floor((2k-1)^2/2)+1 < 2k^2.
```

Thus `G(k)=O(k^2)`, which is much stronger than `G(k)=2^{o(k)}` and hence is
equivalent to `F(n)/log n -> infinity`.  QED.

**Lemma 28J.2: Spectrum Mass Is Superadditive Over Components.**  Let
`G_1,...,G_t` be the connected components of a graph `G`.  With
`s_d` as in Corollary 28J.1,

```text
s_d(G) >= sum_{i=1}^t s_d(G_i)        for every d,
```

and therefore

```text
sum_d s_d(G) >= sum_{i=1}^t sum_d s_d(G_i).
```

Consequently, to prove the spectrum-mass inequality

```text
sum_d s_d(G) >= |V(G)|
```

for all graphs, it is enough to prove it for connected graphs.

Proof.  For a fixed degree `d`, choose in each component `G_i` an induced
`d`-regular subgraph of order `s_d(G_i)`, omitting components with
`s_d(G_i)=0`.  The union of these vertex sets induces the disjoint union of
`d`-regular graphs, hence is itself `d`-regular, and has order
`sum_i s_d(G_i)`.  This proves the first display.  Summing over `d` gives the
second.  If the desired inequality holds for connected graphs, applying it to
each component and then using superadditivity gives it for `G`.  QED.

**Lemma 28J.3: Forests Satisfy Spectrum Mass.**  If `F` is a forest on `n`
vertices, then

```text
sum_d s_d(F) >= n.
```

Proof.  A forest has no nonempty induced `d`-regular subgraph for `d>=2`,
because every nonempty forest has a vertex of degree `0` or `1`.  Thus it is
enough to prove

```text
alpha(F) + 2 nu_ind(F) >= n,
```

where `nu_ind(F)` is the maximum size of an induced matching in `F`; then
`s_0(F)=alpha(F)` and `s_1(F)=2nu_ind(F)`.

Let `mu(F)` be the ordinary matching number.  Since forests are bipartite,
Konig's theorem gives

```text
alpha(F)=n-mu(F).
```

It remains to show `nu_ind(F)>=mu(F)/2`.  Let `M` be a maximum matching in
`F`, and build a conflict graph `C` whose vertices are the edges of `M`, with
two matching edges adjacent in `C` exactly when some edge of `F` joins their
endpoints.  Contract every edge of `M` in the forest `F`; after deleting
irrelevant vertices and edges, the graph `C` is a subgraph of the contracted
forest, so `C` is itself a forest.  Therefore `C` has an independent set of
size at least `|M|/2=mu(F)/2`.

An independent set in `C` is precisely a submatching of `M` in which no two
chosen edges have an edge of `F` between their endpoints.  Hence it is an
induced matching in `F`.  Thus `nu_ind(F)>=mu(F)/2`, and

```text
alpha(F)+2nu_ind(F) >= n-mu(F)+mu(F)=n.
```

QED.

**Lemma 28J.4: Regular Feedback Sets Force Spectrum Mass.**  Let `G` be a
graph with a vertex partition

```text
V(G)=R union F
```

such that `G[F]` is a forest and `G[R]` is `d`-regular for some `d>=2`.
Then

```text
sum_j s_j(G) >= |V(G)|.
```

Proof.  Independent sets and induced matchings in `G[F]` remain independent
sets and induced matchings in `G`, so Lemma 28J.3 applied to the forest
`G[F]` gives

```text
s_0(G)+s_1(G) >= alpha(G[F])+2nu_ind(G[F]) >= |F|.
```

Since `G[R]` is an induced `d`-regular subgraph of `G` and `d>=2`, it
contributes in a degree not already used by `s_0` or `s_1`, so

```text
s_d(G) >= |R|.
```

Adding the two displays gives the claim.  QED.

**Corollary 28J.5: Pseudoforests Satisfy Spectrum Mass.**  If every
connected component of `G` has at most one cycle, then

```text
sum_d s_d(G) >= |V(G)|.
```

Proof.  By Lemma 28J.2 it is enough to handle one connected component.  If
the component is a tree, this is Lemma 28J.3.  Otherwise let `C` be its unique
cycle.  The cycle is induced, since a chord would create a second cycle, so
`C` is an induced `2`-regular subgraph.  Removing `V(C)` leaves a forest
`F`, so Lemma 28J.4 applies with `R=V(C)` and `d=2`.  QED.

**Lemma 28J.6: Split Graphs Satisfy Spectrum Mass.**  If `G` is a split
graph, then

```text
sum_d s_d(G) >= |V(G)|.
```

Proof.  Fix a split partition `V(G)=A union B`, where `A` is a clique and
`B` is independent.  Put `a=|A|` and `b=|B|`.  The independent side gives

```text
s_0(G) >= b.
```

If `a>=2`, then for every `1<=d<=a-1`, the clique `A` contains a clique of
order `d+1`, hence an induced `d`-regular subgraph of order `d+1`.  Therefore

```text
sum_d s_d(G) >= b + sum_{d=1}^{a-1} (d+1)
              = b + (a-1)(a+2)/2
              >= b+a.
```

If `a=0`, then `G` is independent and `s_0(G)=|V(G)|`.  If `a=1` and the
single vertex of `A` has no neighbor in `B`, then again `G` is independent.
If `a=1` and there is an edge, then `s_1(G)>=2`, while `s_0(G)>= b`, so the
spectrum mass is at least `b+2>=b+1=|V(G)|`.  QED.

**Computational Example 28K: `D_spec(6)` Separates From The Full Pair
Parameter.**  The exact checker `EXPERIMENTS/dspec_exact.py` enumerates all
labelled graphs on `M` vertices by their regular degree spectrum summaries.
For `h=6`, it reports:

```text
python3 82/EXPERIMENTS/dspec_exact.py 5 --h 6
python3 82/EXPERIMENTS/dspec_exact.py 6 --h 6
```

The first command finds a spectrum-disjoint obstruction at `M=5`; the second
checks all `32768` labelled graphs on `6` vertices and finds no
spectrum-disjoint pair obstruction.  Thus

```text
D_spec(6)=6.
```

By contrast, Computational Example 28C gives a marked two-part obstruction at
`h=6, M=6`, verified by

```text
python3 82/EXPERIMENTS/balanced_pair_parameter_search.py --h 6 --m 6 --mode plus --mask 1680212686667006004
```

so `P_6>6=D_spec(6)`.  Therefore the full pair parameter has genuinely
cross-component obstructions beyond disjoint-union spectrum separation,
already at the first nontrivial calibrated value.

The helper `EXPERIMENTS/marked_pair_profile.py` inspects this cross-component
mechanism.  On the same `P_6` obstruction, with the first six vertices as
`A` and the last six as `B`, it reports

```text
side_compatible_pairs=18
regular_unions=0
left_spectrum=0:3 1:4 2:4
right_spectrum=0:3 1:2 2:4
```

Thus the two sides have many same-degree regular spectrum pairs whose orders
sum to at least `6`; these would create regular subgraphs in the disjoint
union.  The cross edges destroy all of them by making the cross-degree
profiles nonconstant.  The verification command is

```text
python3 82/EXPERIMENTS/marked_pair_profile.py 12 --mask 1680212686667006004 --split 6 --h 6
```

This identifies the next local obstacle after spectrum matching: even when
same-degree side witnesses exist, one must find such witnesses whose
cross-degree profiles compensate rather than split.

**Computational Calibration 28K.1: Spectrum Matching Above The Half
Threshold.**  The exact spectrum checker also confirms that the `h=7`
spectrum obstruction already appears at component order `7`:

```text
python3 82/EXPERIMENTS/dspec_exact.py 7 --h 7
```

It checks all `2097152` labelled graphs on `7` vertices, finds `53` distinct
counterexample spectrum summaries, and gives the obstruction

```text
mask_a=2248,          summary_a=0:4 1:4 2:3,
mask_b=375775,        summary_b=0:2 1:2 2:3 3:4 4:5 5:6.
```

For each common degree, the displayed maximum orders sum to at most `6`, so
this proves `D_spec(7)>7`.

A random spectrum search finds a component-order `8` obstruction for the same
target:

```text
python3 82/EXPERIMENTS/regular_spectrum.py 8 --h 7 --mask-a 111173317 --mask-b 238248447
```

The spectra are

```text
1:0 2:0 2:1 3:0 3:2 4:1,
1:0 2:0 2:1 3:0 3:2 4:3 5:4,
```

and the maximum same-degree total is `6`.  Hence `D_spec(7)>8`.  A random
search at component order `9` with `500` samples found no obstruction; its
best sampled same-degree total was already `7`.

Random searches show that this spectrum-disjoint mechanism becomes much less
visible above the trivial half-target lower bound.  The command

```text
python3 82/EXPERIMENTS/regular_spectrum.py 17 --h 10 --samples 50 --seed 17
```

finds `42` sampled graphs with no regular induced subgraph on at least `10`
vertices but no disjoint-union spectrum obstruction among them; the best pair
already has maximum same-degree total `13`.  Similarly,

```text
python3 82/EXPERIMENTS/regular_spectrum.py 18 --h 10 --samples 20 --seed 18
```

finds `16` sampled counterexamples and no spectrum obstruction, with best
maximum same-degree total `14`.  This is not a proof of an upper bound for
`D_spec(10)`, but it is useful calibration: beyond the lower bound inherited
from `G(ceil(h/2))`, random nonhomogeneous spectra seem to overlap quickly.

**Computational Candidate 28L: A Parity Cross-Profile Family.**  The script
`EXPERIMENTS/parity_pair_construction.py` generates the following marked
two-part graph with `|A|=|B|=h`.  On the `A` side put one edge `a_0a_1` and
make all other `A` vertices isolated.  On the `B` side put a clique on
`b_0,...,b_{h-2}` and make `b_{h-1}` isolated.  Between the sides, join
`a_i` to `b_j` exactly when

```text
i+j is even.
```

The construction is not currently proved to work for all `h`.  Exact checks
with the same verifier used for `P_h` show:

```text
h=5,6:   not an obstruction,
h=7..11: plus obstruction at side size M=h.
```

For example,

```text
python3 82/EXPERIMENTS/parity_pair_construction.py 9
```

reports no regular induced subgraph on at least `9` vertices and no balanced
plus middle of side size `4`.  If the pattern could be proved for all large
`h`, it would give `P_h>h` for all large `h`.  This is still only a linear
lower bound, but it supplies a structured test family for any proposed
cross-profile matching theorem.

Because the construction has only seven vertex types, the stronger checker
`EXPERIMENTS/parity_pair_symbolic.py` tests it by type counts rather than by
all subsets.  It verifies the same failures at `h=5,6` and no regular
`h`-set or balanced plus middle for every `7<=h<=40`:

```text
python3 82/EXPERIMENTS/parity_pair_symbolic.py --min-h 5 --max-h 40
```

The type-count reduction used by that script is as follows.  Let `z=b_{h-1}`
be the isolated vertex on the `B` side, and let `p` be the parity of `h-1`.
For a selected set, write

```text
x_0,x_1,zeta in {0,1}
```

for whether `a_0,a_1,z` are selected, and write

```text
x_e,x_o,y_e,y_o
```

for the numbers of selected even and odd `A`-isolates and even and odd
vertices from the `B`-clique.  Put

```text
X_e=x_0+x_e,      X_o=x_1+x_o,      Y=y_e+y_o.
```

Then the degrees of the nonempty selected types are:

```text
a_0:              x_1+y_e+zeta*1_{p=0},
a_1:              x_0+y_o+zeta*1_{p=1},
A-even isolates:  y_e+zeta*1_{p=0},
A-odd isolates:   y_o+zeta*1_{p=1},
B-even clique:    Y-1+X_e,
B-odd clique:     Y-1+X_o,
z:                X_e if p=0, and X_o if p=1.
```

Thus a regular induced subgraph of this construction is exactly a feasible
integer choice of these seven parameters for which all displayed degrees
corresponding to nonempty selected types are equal.  A balanced plus middle
is the same system with the additional constraints

```text
x_0+x_1+x_e+x_o = y_e+y_o+zeta = floor((h-1)/2)
```

and common displayed degree `floor((h-1)/2)`.  This is a finite arithmetic
form of the parity candidate; a proof of the candidate for all large `h`
would amount to excluding these integer solutions.

One half of the candidate has a short proof.

**Lemma 28M: The Parity Construction Has No Balanced Plus Middle.**  For
`h>=7`, the parity construction in Candidate 28L has no sets
`X subset A`, `Y subset B` with

```text
|X|=|Y|=r=floor((h-1)/2)
```

such that the induced graph on `X union Y` is `r`-regular.

Proof.  Since `h>=7`, we have `r>=3`.  Suppose such sets `X,Y` exist.  Let
`C=Y cap {b_0,...,b_{h-2}}` be the selected part of the clique core, and let
`zeta` indicate whether the isolated vertex `z=b_{h-1}` is selected.  Then

```text
|C|=r-zeta >= r-1 >= 2.
```

Among the `r` selected vertices of `A`, at least one is an isolate `a_i` with
`i>=2`.  Let `q` be its parity.  The selected neighbors of this isolate are
exactly the selected `B` vertices of parity `q`, including `z` only when
`z` has parity `q`.  Its degree is `r`, while there are only `r` selected
vertices on the `B` side.  Therefore all selected vertices of `Y` have parity
`q`: the core vertices in `C` all have parity `q`, and if `z` is selected
then `z` also has parity `q`.

It follows that no selected `A`-isolate of the other parity can occur, since
it would have degree `0`.  The endpoint among `a_0,a_1` of the other parity
also cannot occur: it sees no selected `B` vertex and has at most one neighbor
inside `A`, so its degree is at most `1<r`.  Hence every selected vertex of
`A` has parity `q`, so the number `X_q` of selected `A` vertices of parity
`q` is exactly `r`.

Now take any selected vertex of the clique core `C`, which exists because
`|C|>=2`.  Its degree inside `X union Y` is

```text
|C|-1+X_q = (r-zeta)-1+r.
```

For `zeta in {0,1}` and `r>=3`, this is larger than `r`, contradicting
`r`-regularity.  QED.

It remains to rule out all large regular sets.  The same type notation gives
a short proof.

**Lemma 28N: The Parity Construction Has No Large Regular Set.**  For
`h>=7`, the parity construction in Candidate 28L has no regular induced
subgraph on at least `h` vertices.

Proof.  Let `S` be a regular induced subgraph of the construction.  Use the
notation from Candidate 28L:

```text
X_0=x_0+x_e,       X_1=x_1+x_o,
Y_0=y_e,           Y_1=y_o,        Y=Y_0+Y_1,
```

and let `p` be the parity of `z=b_{h-1}`.  First suppose that `S` is contained
in one side.  On the `A` side the only non-isolated edge is `a_0a_1`, so every
regular induced subgraph has order at most `h-1`.  On the `B` side the clique
core has order `h-1`, and adding the isolated vertex `z` to two or more core
vertices destroys regularity; again every regular induced subgraph has order
at most `h-1`.  Hence we may assume that `S` meets both sides.

If the common degree of `S` is `0`, then `S` is independent.  An independent
set with no selected clique-core vertex has size at most `h-1`: without `z`
this is the independence number of the one-edge graph on `A`, and with `z`
one may use only the `A` vertices of parity opposite to `p`.  If an
independent set contains a clique-core vertex of parity `q`, it contains no
other clique-core vertex and no `A` vertex of parity `q`; hence its size is at
most

```text
1+1+ceil(h/2) <= h-1
```

for `h>=7`.  Thus every regular set of order at least `h` has positive common
degree `d`.

Assume from now on that `d>0`.  If `Y=0`, then `S` contains `z` and some
vertices of `A`.  If `X_p>=2`, then a selected `A`-isolate of parity `p` has
degree `1`, while `z` has degree `X_p>=2`, a contradiction.  If
`X_{1-p}>=2`, then a selected `A`-isolate of parity `1-p` has degree `0`,
also a contradiction.  Hence `|S|<=X_0+X_1+1<=3<h`.

Now suppose exactly one clique-core parity is selected.  Say `Y_q=Y>0` and
`Y_{1-q}=0`.  The selected core vertices have degree

```text
d=Y-1+X_q.
```

If `X_{1-q}>=2`, then a selected `A`-isolate of parity `1-q` has degree
`zeta` when `p=1-q` and degree `0` otherwise.  Since `d>0`, regularity would
force `zeta=1`, `p=1-q`, and `d=1`; but then the selected vertex `z` has
degree `X_{1-q}`, forcing `X_{1-q}=1`, a contradiction.  Therefore
`X_{1-q}<=1`.

If `X_q>=2`, then a selected `A`-isolate of parity `q` has degree
`Y+zeta*1_{p=q}`.  Equating this with the core degree gives

```text
X_q=1+zeta*1_{p=q}.
```

Thus `X_q=2`, `zeta=1`, and `p=q`; but then `z` has degree `X_q=2`, so
`d=2`, while the core degree is `Y+1`.  Hence this exceptional case has
`Y=1` and contributes at most

```text
Y+X_q+X_{1-q}+zeta <= 1+2+1+1=5<h.
```

In the remaining case `X_q<=1`, and therefore

```text
|S|=Y+X_q+X_{1-q}+zeta <= Y+3 <= ceil((h-1)/2)+3 <= h-1
```

for every `h>=7`.

It remains to consider the case in which both clique-core parities are
selected.  Equality of the two core degrees gives

```text
Y-1+X_0=Y-1+X_1,
```

so `X_0=X_1=:X`.  Because `S` is not contained in `B`, we have `X>=1`.  For
each parity `q`, choose a selected `A` vertex of parity `q`.  Its degree is at
most

```text
Y_q+1+zeta*1_{p=q},
```

where the `1` allows for the possible edge `a_0a_1`.  Since the selected core
vertices of parity `q` have degree `Y-1+X`, we get

```text
Y-1+X <= Y_q+1+zeta*1_{p=q}.
```

Equivalently,

```text
X+Y_{1-q} <= 2+zeta*1_{p=q}.
```

Summing this inequality over `q=0,1` gives

```text
2X+Y <= 4+zeta.
```

Therefore

```text
|S|=2X+Y+zeta <= 4+2zeta <= 6<h,
```

because `h>=7`.  All cases give `|S|<h`.  QED.

Combining Lemmas 28M and 28N, the parity construction is a genuine infinite
family of balanced-pair obstructions.

**Corollary 28O: A Linear Lower Bound for the Pair Parameter.**  For every
`h>=7`,

```text
P_h^+>h.
```

Consequently, using Lemma 28B, the common balanced pair parameter satisfies
`P_h>h` for every `h>=7`.

Proof.  Candidate 28L gives a marked graph with `|A|=|B|=h`.  Lemma 28N rules
out the first alternative in the definition of `P_h^+`, and Lemma 28M rules
out the balanced plus middle of side size `floor((h-1)/2)=ceil((h-2)/2)`.
Thus side size `h` does not force the defining alternatives, so `P_h^+>h`.
Lemma 28B identifies `P_h^+` and `P_h^-`.  QED.

**Corollary 28P: The Parity Obstruction Is Not A Spectrum Obstruction.**  For
every `h>=7`, the marked graph in Candidate 28L fails the balanced-pair
alternatives at side size `h`, even though its two marked sides contain
same-degree regular induced subgraphs whose total order is at least `h`.

Proof.  Corollary 28O proves that the marked graph fails the balanced-pair
alternatives.  It remains only to exhibit the side witnesses.  On the `A`
side, delete one endpoint of the unique edge `a_0a_1`; the remaining
`h-1` vertices form an independent set, hence a `0`-regular induced subgraph.
On the `B` side, take the isolated vertex `z=b_{h-1}` together with any one
vertex of the clique core.  These two vertices are nonadjacent in `G[B]`, so
they form a `0`-regular induced subgraph.  The two side-regular witnesses
have the same degree and total order

```text
(h-1)+2=h+1.
```

By Lemma 28N, however, no choice of side witnesses in this marked graph merges
to a regular induced subgraph on at least `h` vertices.  Thus the obstruction
comes from cross-profile failure, not from absence of same-degree side
spectrum matches.  QED.

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

**Corollary 29A: Side-Regular Merge Criterion.**  Let `X,Y` be disjoint
vertex sets.  Suppose `G[X]` is `a`-regular and `G[Y]` is `b`-regular.  Then
`G[X union Y]` is regular if and only if there is an integer `c` such that

```text
deg(v,Y)=c          for every v in X,
deg(w,X)=c+a-b      for every w in Y.
```

In particular, if `a=b`, then two same-degree side-regular witnesses merge
precisely when all vertices in `X union Y` have one common cross-degree into
the opposite side.

Proof.  Apply Lemma 29.  Since `i_X(v)=a` on `X` and `i_Y(w)=b` on `Y`, the
regularity equations become

```text
a+deg(v,Y)=D,       b+deg(w,X)=D.
```

Taking `c=D-a` gives the displayed criterion.  QED.

This is the formal version of the obstruction measured by
`EXPERIMENTS/marked_pair_profile.py`.  The first `P_6` marked obstruction has
many same-degree side-regular pairs, but Corollary 29A fails for every one
because the cross-degrees into the opposite side are not constant.

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

No complete proof yet.  The strongest current reduction in this workspace is

```text
G(h) <= 8h^2 P_h^2,
```

where `P_h` is the balanced marked-pair parameter from Lemma 28B.  Lemma 28G
still gives

```text
G(ceil(h/2)) <= P_h <= ceil(G(h)/2),
```

so proving `P_h=2^{o(h)}` is subexponentially equivalent to the original
problem.  The full-drop refinement removes the previous ordered
sparse-inversion loss, but it does not by itself create a non-circular
recurrence for `P_h`.  The remaining gap is therefore a genuinely new
subexponential argument for the balanced marked-pair problem, or a different
route that avoids this equivalent local obstruction.
