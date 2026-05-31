# Literature For Erdos Problem 82

This file tracks material linked from the Erdos Problems page and nearby
references.

## Erdos Problems page

Source: `https://www.erdosproblems.com/82`

The page states the conjecture as `F(n) / log n -> infinity`, equivalently
`G(n) <= 2^{o(n)}`.  It records the elementary Ramsey lower bound
`F(n) >= c log n`.  It also records the open status, Bollobas's observation
`F(n) << n^{1/2+o(1)}`, the AKS upper improvement
`F(n) <= n^{1/2} (log n)^{O(1)}`, and Dyson--McKay's further improvement
`F(n) << sqrt(n)`.  In inverse notation, it records
`G(1)=1`, `G(2)=2`, `G(3)=5`, `G(4)=7`, `G(5)=17`,
`G(6) >= 21`, `G(7) >= 30`, and
`G(k) >= (9/163) k^2` for all large `k`.

## Alon--Krivelevich--Sudakov, "Large nearly regular induced subgraphs"

Sources: arXiv `0710.2106`, SIAM J. Discrete Math. 22 (2008), 1325--1337.

They define `f(n,c)` as the largest `f` such that every `n`-vertex graph has an
induced subgraph on at least `f` vertices with `Delta <= c delta`.  The case
`c=1` is the regular-induced-subgraph problem.  The paper proves upper and
lower bounds for fixed `c>1` and gives constructions showing that one cannot
force very large nearly-regular induced subgraphs in general.  One explicit
upper statement visible in the indexed PDF text is that, for every large `n`,
there is a graph on `n` vertices in which every `K`-nearly-regular induced
subgraph has at most `7 K n / log n` vertices.

For Problem 82, the main relevance is methodological and historical: the
paper attacks a relaxed version of regularity and improves known upper
constructions, but it does not prove `F(n)=omega(log n)`.

## Dyson--McKay, "Ramsey numbers for regular induced subgraphs"

Sources: arXiv `2604.08215`; Brendan McKay's combinatorial data page.

Notation in the paper:

- `R_k(n)` is the set of graphs on `n` vertices with no induced regular
  subgraph of order exactly `k`.
- `R_{>=k}(n)` is the set of graphs on `n` vertices with no induced regular
  subgraph of order at least `k`.
- `N_k` and `N_{>=k}` are the least orders forcing those properties.  In this
  workspace, `N_{>=k}=G(k)`.

Indexed theorem statements record:

- `N_5 = 21` and `N_{>=5} = 17`.
- `N_6 >= 28`, `N_{>=6} >= 21`, `N_7 >= 48`, `N_{>=7} >= 30` in the arXiv
  statement visible to the search index.
- McKay's data page currently reports larger exact/search data for the
  "exactly k" variant, including `N_7 >= 71`; this is distinct from `G(7)`.
- The Erdos Problems page records the asymptotic consequence
  `G(k) >= (9/163) k^2` for all large `k`.

Thus the current best published upper construction for `F(n)` is quadratic in
the inverse form: `G(k) >= c k^2`, equivalently `F(n) <= C sqrt(n)`.

The introduction also records the older inverse bounds in the `N_{>=k}`
notation: Bollobas proved `N_{>=k} >= k^{2-o(1)}`, and
Alon--Krivelevich--Sudakov improved this to
`N_{>=k} = Omega(k^2/(log k)^{3/2})`.  It contrasts these heterogeneous random
constructions with the homogeneous random graph `G(n,1/2)`, where the largest
regular induced subgraph is typically `Theta(n^{2/3})`.

## Fajtlowicz--McColgan--Reid--Staton

Source: Ars Combinatoria 39 (1995), 149--154, "Ramsey numbers for induced
regular subgraphs".

The abstract says the paper considers two Ramsey-type variations asking for
the number of vertices needed to force an induced regular subgraph on a
prescribed number of vertices.  Later sources cite it for the early exact
small-value theory, including `G(1)=1`, `G(2)=2`, `G(3)=5`, `G(4)=7`, and the
early lower bound `G(5) >= 12` as reported on the Erdos Problems page.  The
original full text has not been locally downloaded because network downloads
are blocked in this session.

## Comments, OEIS, Computations

The discussion thread for Problem 82 records computational counts for graphs
with no induced regular subgraph of order at least `5`, from `1` through `16`
vertices:

```text
1, 2, 4, 11, 31, 130, 728, 6027, 66308, 818276, 8336902,
45933753, 79888458, 23814804, 512906, 954.
```

The same thread records earlier examples showing `G(6) >= 19` and
`G(7) >= 28`; these have since been superseded by Dyson--McKay.

OEIS A394563 is the sequence `G(k)` in this notation.  OEIS A390257 is the
minimum, over `n`-vertex graphs, of the largest regular induced subgraph order,
that is `F(n)`.

A GitHub repository `rsh3khar/erdos-82` advertises a CEGAR SAT extension check
around McKay's `n=28` graphs for sizes `7--9`; this is computational support
for finite lower-bound searches, not an asymptotic proof.

## Formal Lean Statement

The Google DeepMind formal-conjectures entry formalizes the problem statement
in Lean.  The rendered page states that `F(n)` is maximal such that every graph
on `n` vertices contains a regular induced subgraph on at least `F(n)`
vertices.  I did not use the Lean file for proof development beyond checking
that the formalized target matches the informal statement.

## Related 2026 Pair-Trace Paper

Source: arXiv `2604.23882`, "Pair-Trace Absorption Certificates for Regular
Induced Subgraphs".

This paper develops a dyadic modular-witness absorption framework.  A set is
`q`-modular if all its induced degrees are congruent modulo `q`; once a set
`U` has `|U| <= q` and all internal degrees congruent modulo `q`, `G[U]` is
regular.  The indexed abstract and summary explicitly say that the paper gives
finite absorption-or-obstruction certificates and "does not claim to solve
that problem or to improve the general lower bound for `F(n)`."

Section 4 defines `M(q,m)` for powers of two `q` as the least `N` such that
every graph on at least `N` vertices contains a `q`-modular witness of exactly
`m` vertices.  Ramsey gives finiteness because cliques and independent sets are
`q`-modular.  The conditional threshold theorem is relevant because a
subexponential bound for appropriate `M(q,m)` would imply the desired
subexponential bound for `G(k)`, but the paper only isolates the needed local
lifting certificates.

## Parity-Constrained Induced Subgraphs

Gallai's theorem says that every graph admits a bipartition
`V(G)=V_1 union V_2` such that both `G[V_1]` and `G[V_2]` have all degrees
even.  Consequently every `n`-vertex graph has an induced subgraph of order at
least `ceil(n/2)` with all degrees even.  Search-indexed sources also record
the mixed even/odd partition variant.

The odd analogue is substantially harder: Scott proved every connected
`n`-vertex graph has an odd induced subgraph of order at least `c n/log n`;
Ferber--Krivelevich later proved a linear lower bound `n/10000` for graphs
with no isolated vertices.  These results are relevant to the modular route,
but parity alone does not solve Problem 82 because a large even induced
subgraph is not necessarily regular.

## Repeated-Degree Relaxations

Source: "Induced subgraphs with many repeated degrees" and follow-up work on
large induced subgraphs with three repeated degrees.

These papers study relaxations motivated by the regular-induced-subgraph
problem.  One parameter asks for the least threshold forcing an induced
subgraph with at least `k` vertices of the same degree, and a stronger
parameter asks for at least `k` vertices attaining the maximum degree.  These
relaxations are easier than exact regularity.  For Problem 82, the useful
bridge is degree-split based: if an equal-degree class also has a constant
number of neighbors outside itself, then the class is regular.  Identical
external traces are a stronger sufficient condition for this constant
outside-degree condition.  The obstruction is that repeated-degree theorems do
not by themselves control how the degree is split between the repeated-degree
class and its complement.

## Ramsey-Graph Pseudorandomness

For a fixed constant `C`, an `n`-vertex graph is often called `C`-Ramsey if it
has no clique or independent set larger than `C log n`.  Bukh--Sudakov proved
that every such graph contains a large induced subgraph with many distinct
degrees; later work by Jenssen--Keevash--Long--Yepremyan improved the distinct
degree bound.  Other work of Narayanan and collaborators shows that Ramsey
graphs induce subgraphs with many different edge/vertex-size pairs.

For Problem 82 this supports a useful reduction: it is enough to prove
`reg(G)=omega(log n)` for every fixed-`C` Ramsey graph.  However, distinct
degree results do not directly give regular induced subgraphs.
