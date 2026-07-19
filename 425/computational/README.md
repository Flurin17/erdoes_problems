# Computation for Erdős Problem #425

## Scope

The script exact_f.py computes \(F(n)\) exactly for moderate \(n\).  It is
used to check definitions, generate structural conjectures, and falsify finite
lemmas.  The table is not evidence for an infinite asymptotic.

Semantics are fixed throughout: products are indexed by unordered subsets of
distinct elements.  Diagonal products \(a^2\) are excluded.

## Algorithm and invariant

For \(r=2\), form the four-uniform collision hypergraph on \([n]\).  Its edges
are exactly
\[
 \{w,x,y,z\},\qquad w<x<y<z,\qquad wz=xy.
\]
An admissible set is an independent set, so \(F(n)\) is \(n\) minus the
minimum transversal number.

The exact solver stores the bitset \(U\) of collision edges not yet hit.  Its
invariant is:

> A deletion set extending the current branch hits the original hypergraph
> if and only if it hits every edge in \(U\).

It chooses one uncovered edge and branches on deleting each of its four
vertices.  These branches exhaust every transversal.  Memoization is by the
exact uncovered-edge bitset.  A greedy packing of vertex-disjoint uncovered
edges supplies a valid lower bound; a greedy cover supplies an upper bound.

Collision edges are generated independently in two ways:

1. bucket all unordered pairs by their product;
2. enumerate the unique rectangle parameterization
   \[
   (w,x,y,z)=(ag,bg,ah,bh),\qquad (a,b)=1.
   \]

Self-tests assert that the generators agree.  They also compare the exact
solver with exhaustive subset enumeration and directly check fixed-\(r\)
products for \(r\le4\).

## Reproduction

From the Problem 425 directory:

    PYTHONHASHSEED=0 python3 computational/exact_f.py self-test \
      --edge-max 80 --brute-n 16 --fixed-n 11

    PYTHONHASHSEED=0 python3 computational/exact_f.py table \
      --n-max 45 --output computational/F2-n45.json

    PYTHONHASHSEED=0 python3 computational/exact_f.py verify \
      computational/F2-n45.json --witness-only

    PYTHONHASHSEED=0 python3 computational/exact_f.py verify \
      computational/F2-n45.json --max-n 30

The deterministic run in this repository reported:

- self-test: 0.228 seconds of measured script time;
- exact table through \(n=45\): 7302.212 seconds of measured script time;
- all 45 edge digests and extremal witnesses: verified;
- independent exact optimization readback through \(n=30\): verified;
- edge generators compared for every \(n\le80\);
- exhaustive pair solver comparison for every \(n\le16\);
- direct fixed-\(r\) checks for \(2\le r\le4\), \(n\le11\).

Host scheduling time is intentionally not included in the script runtime.

## Exact output summary

For \(1\le n\le45\),
\[
\begin{array}{c|rrrrrrrrrrrrrrrrr}
n&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16&17\\
\hline
F(n)&1&2&3&4&5&5&6&6&7&7&8&9&10&10&10&11&12
\end{array}
\]
and
\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
n&18&19&20&21&22&23&24&25&26&27&28&29&30&31&32&33\\
\hline
F(n)&12&13&13&13&14&15&15&16&16&16&16&17&17&18&19&19.
\end{array}
\]

Finally,
\[
\begin{array}{c|rrrrrrrrrrrr}
n&34&35&36&37&38&39&40&41&42&43&44&45\\
\hline
F(n)&19&20&20&21&21&21&21&22&23&24&24&24.
\end{array}
\]

F2-n45.json records, for every \(n\), an extremal witness, a deletion set,
the collision-edge count, a SHA-256 digest of the canonical edge list, search
nodes, and runtime. The witness-only verifier regenerates every edge list,
checks its digest, and checks every witness product. The stronger verifier
also reruns the exact optimization (performed through \(n=30\) here).

## Interpretation

The output certifies the listed finite values.  It does not select between
the competing asymptotic semiprime architectures and does not establish a
limit constant.
