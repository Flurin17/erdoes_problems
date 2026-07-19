# Weighted endpoint-clause excess

## Status

This route reduces the target series to a precise scale-weighted excess of an
endpoint-divisibility clause multigraph. The reduction is complete; the
uniform excess bound is open. Parallel clauses must be retained.

Put $f(x)=1/(x\log x)$. For a nonintegral $x$, let a Boolean state choose
one of $\lfloor x\rfloor,\lceil x\rceil$. Two states on distinct points
conflict when their selected positive integers are unequal and one divides
the other. Equality may be ignored: it creates only bounded multiplicity,
as proved below. A conflict gives the $2$-clause forbidding that state pair.
Integral points can be represented by dummy Boolean variables whose two
states denote the same fixed integer; a strict conflict then produces the
two clauses needed to forbid it independently of the dummy state.

## 1. Bounded multiplicity transfer

**Lemma 1.** Let $A\subset[2,\infty)$ be $1$-separated, and choose for each
$x\in A$ an adjacent integer label $r(x)$. If the set of distinct labels is
primitive, then
\[
\sum_{x\in A}f(x)\le4\sum_{n\in r(A)}f(n).               \tag{1}
\]

**Proof.** Points labeled $n$ lie in the open interval $(n-1,n+1)$, except
for the possible integral point $n$ itself. Three such points cannot be
$1$-separated. More precisely, there is at most one point in $(n-1,n)$ and
at most one in $(n,n+1)$; if $n$ itself occurs, neither can occur. For the
upper point $x>n$, monotonicity gives $f(x)\le f(n)$. For the lower point
$n-1<x<n$, one has $n<x+1\le3x/2$ and $\log n\le2\log x$, so
$f(x)\le3f(n)$. This proves (1). $\square$

The primitive-set theorem in `../PROOF.md` therefore gives an absolute
constant $C_{\rm prim}$ with
\[
\sum_{x\in A}f(x)\le4C_{\rm prim}                       \tag{2}
\]
whenever the endpoint formula is satisfiable.

## 2. Clause multigraph and weighted excess

For a finite endpoint formula $\Phi$, form a multigraph $G$: variables are
vertices and every forbidden state pair contributes one edge. Different
clauses on the same variable pair remain parallel edges. Give vertex $v$
weight $w_v=f(x_v)$. For $t\ge0$, let
\[
G_t=G[\{v:w_v\ge t\}],
\]
and define
\[
\Xi_w(G)=\int_0^\infty
 \sum_{C\in\operatorname{comp}(G_t)}
 (|E(C)|-|V(C)|)_+\,dt.                                 \tag{3}
\]

**Theorem 2 (weighted pseudoforest deletion).** There is a set of variables
$D$ whose deletion makes $\Phi$ satisfiable and such that
\[
\sum_{v\in D}w_v\le\Xi_w(G).                            \tag{4}
\]

**Proof.** Give an edge $uv$ weight $c_{uv}=\min(w_u,w_v)$. Edge sets whose
components contain at most one cycle are the independent sets of the
bicircular matroid. Its rank on a multigraph $H$ is
\[
r_{\rm bic}(E(H))=
\sum_{C\in\operatorname{comp}(H)}\min(|E(C)|,|V(C)|).   \tag{5}
\]
This follows componentwise by taking a spanning tree and, when present, one
additional edge. The finite matroid greedy theorem supplies a maximum-weight
pseudoforest $P$. Layer cake and (5) give
\[
\sum_{e\notin P}c_e
=\int_0^\infty\bigl(|E(G_t)|-r_{\rm bic}(E(G_t))\bigr)dt
=\Xi_w(G).                                               \tag{6}
\]

Delete a lighter endpoint of every edge outside $P$. The union of these
chosen vertices costs at most the left side of (6), and every surviving
clause edge lies in a subgraph of $P$.

It remains to note that every $2$-CNF whose clause multigraph is a
pseudoforest is satisfiable. In the edge-vertex incidence bipartite graph,
every edge subset $F$ meets at least $|F|$ vertices, because every subgraph
of a pseudoforest has at most as many edges as vertices. Hall's theorem
matches each clause edge injectively to one of its endpoint variables. Set
each matched variable opposite the state forbidden by its matched clause;
every clause is then satisfied at its matched endpoint. This proves (4).
$\square$

Parallel edges are essential. A simple interaction graph can be a triangle
even when two clauses on each pair force an inconsistent parity cycle; its
simple-graph excess would be zero, while the clause multigraph detects the
obstruction.

Combining Lemma 1 and Theorem 2 gives the exact sufficient estimate
\[
\sum_{x\in F}f(x)
\le \Xi_f(G_F)+4C_{\rm prim}                             \tag{7}
\]
for every finite admissible $F\subset[2,\infty)$. Thus
\[
\boxed{\sup_F\Xi_f(G_F)<\infty}                          \tag{8}
\]
would prove the first assertion of Problem 143, and hence also the second.

For ordered points $x_1<\cdots<x_m$, (3) is the finite sum
\[
\Xi_f(G)=\sum_{j=1}^m
 (f(x_j)-f(x_{j+1}))
 \sum_{C_j\in\operatorname{comp}(G[\{x_1,\ldots,x_j\}])}
 (|E(C_j)|-|V(C_j)|)_+,
\quad f(x_{m+1})=0,                                     \tag{9}
\]
Formula (9) makes the remaining requirement a genuinely scale-weighted
cycle-excess bound.

## 3. A simpler branching sufficient condition

Orient the simple interaction graph from smaller to larger points and let
$P(y)$ be the earlier neighbors of $y$. If a deletion leaves
$|P(y)|\le1$ at every surviving vertex, process points increasingly. One
previously selected integer excludes at most one of the two consecutive
labels of the new point, so greedy endpoint rounding succeeds.

Equivalently, it suffices to hit every backward cherry
\[
\{y,x,z\},\qquad x,z\in P(y),\quad x\ne z.               \tag{10}
\]
If a fractional cherry cover has cost $C$, thresholding it at $1/3$ gives an
integral deletion of cost at most $3C$. This is weaker than Theorem 2 but
offers a concrete Hall-type target.

## 4. Exact obstruction and bottleneck

The excess cannot be bounded one shell at a time by a summable quantity.
There are admissible finite sets contained in $[N,3N]$ for which every
primitive adjacent labeling requires deletion weight $\gg1/\log N$; see
`rounding_shell_obstructions.md`. Their clause multigraphs have linear
cycle excess in that shell.

The open step in (8) is therefore cross-scale: prove that shell contributions
of order $1/\log N$ cannot recur at geometrically successive scales inside
one admissible set. This is the same carrier-conditioned accumulation issue
that remains in the quotient-rough packet route.
