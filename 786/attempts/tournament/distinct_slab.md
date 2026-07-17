# Distinct-factor route: top slabs and primitive valuation circuits

## Outcome

This note treats the internally repetition-free convention. After cancelling
common factors, a bad relation is a pair of disjoint sets

\[
S,T\subset[2,N],\qquad \prod_{a\in S}a=\prod_{b\in T}b,\qquad |S|\ne|T|.
\]

The route is not yet a solution. It proves:

1. a sharp top-slab lower bound on the support of every bad relation;
2. a connected prime-token representation of every support-minimal relation;
3. an explicit fractional transversal of total cost \(O(N/\log N)\);
4. count bounds by support and imbalance;
5. squarefree primitive examples based on \(K_{D,D+1}\), showing that the
   support bound is asymptotically sharp and raw circuit counting cannot
   supply the needed rounding.

The exact remaining issue is a fractional-to-integral transversal theorem
for this arithmetic circuit clutter.

## 1. Primitive signed circuits

Write \(v(n)=(v_p(n))_p\). A signed valuation relation in
\(U\subseteq[2,N]\) is a pair of nonempty disjoint sets \(S,T\subseteq U\)
such that

\[
\sum_{a\in S}v(a)=\sum_{b\in T}v(b).
\]

Its imbalance is \(d(S,T)=\bigl||T|-|S|\bigr|\). It is bad when
\(d(S,T)>0\). Call it **conformally primitive** when it contains no nonempty
proper subrelation \(S'\subseteq S,T'\subseteq T\) with equal products. This
is the useful meaning of “circuit” below; it is not necessarily an ordinary
rational matroid circuit.

### Lemma 1 (primitive reduction)

Every bad relation contains a conformally primitive bad relation. Thus a set
is product-length rigid for internally distinct lists if and only if it
contains no conformally primitive bad circuit.

**Proof.** Starting with a bad relation, suppose it contains a proper
subrelation \((S',T')\). If \(|S'|\ne|T'|\), replace the relation by this
smaller bad one. If \(|S'|=|T'|\), remove it; the complement is a smaller
relation with the original nonzero imbalance. Repeat. Support strictly
decreases, so the process terminates at a conformally primitive bad relation.
A one-sided terminal relation is impossible because every factor exceeds
\(1\). \(\square\)

It is therefore enough, and necessary, to hit the supports of primitive bad
circuits.

## 2. Sharp top-slab bounds

For \(1<y<N\), put

\[
U_y=\{n\in\mathbb N:y\le n\le N\},\qquad H=\log(N/y).
\]

Endpoint rounding is harmless.

### Lemma 2 (support and imbalance)

Let \((S,T)\) be a bad relation in \(U_y\), oriented so that

\[
r=|S|<s=|T|,\qquad d=s-r,\qquad k=r+s.
\]

Then

\[
sH\ge d\log N,                                                    \tag{2.1}
\]

and hence

\[
s\ge\left\lceil\frac{d\log N}{H}\right\rceil,\qquad
k\ge2\left\lceil\frac{d\log N}{H}\right\rceil-d.                 \tag{2.2}
\]

Equivalently,

\[
d\le\frac{kH}{2\log N-H}.                                        \tag{2.3}
\]

**Proof.** Product equality gives

\[
y^s\le\prod_{b\in T}b=\prod_{a\in S}a\le N^r.
\]

Using \(\log y=\log N-H\) and \(r=s-d\) yields (2.1). Equation (2.2)
follows from \(k=2s-d\); substituting \(s=(k+d)/2\) in (2.1) gives
(2.3). \(\square\)

If \(y=N/h\), an imbalance-one circuit therefore has support at least

\[
2\frac{\log N}{\log h}-1.                                       \tag{2.4}
\]

For example, deleting the first \(N/\log\log N=o(N)\) integers forces
support

\[
(2-o(1))\frac{\log N}{\log\log\log N}.
\]

For a fixed support \(k\), (2.3) also leaves only

\[
O\!\left(1+\frac{k\log h}{\log N}\right)                         \tag{2.5}
\]

possible positive imbalances, with the parity constraint \(d\equiv k\pmod2\).

### Exact deficit identity

Set

\[
\delta_N(n)=\log(N/n).
\]

The same relation satisfies

\[
\sum_{b\in T}\delta_N(b)-\sum_{a\in S}\delta_N(a)=d\log N.        \tag{2.6}
\]

Thus every bad circuit contains at least \(\log N\) units of unsigned
deficit. This is more useful than support length alone.

## 3. An \(O(N/\log N)\) fractional transversal

Let \(\mathcal C(U)\) be the hypergraph whose edges are supports of primitive
bad circuits in \(U\). Denote its integral and fractional transversal
numbers by \(\tau(\mathcal C)\) and \(\tau^*(\mathcal C)\).

### Lemma 3 (deficit transversal)

The weights

\[
x_n=\frac{\delta_N(n)}{\log N}\qquad(n\in U)                     \tag{3.1}
\]

are a fractional transversal, and

\[
\sum_{n\in U}x_n\le\frac{N-1}{\log N}.                           \tag{3.2}
\]

Consequently,

\[
\tau^*(\mathcal C(U))\le\frac{N-1}{\log N}.                      \tag{3.3}
\]

**Proof.** By (2.6), every circuit \(C=S\cup T\) obeys

\[
\sum_{n\in C}\delta_N(n)
\ge\left|\sum_{b\in T}\delta_N(b)-\sum_{a\in S}\delta_N(a)\right|
=d(S,T)\log N\ge\log N.
\]

This proves every covering constraint. Moreover,

\[
\sum_{n=1}^N\delta_N(n)=N\log N-\log(N!).
\]

Since

\[
\log(N!)\ge\int_1^N\log t\,dt=N\log N-N+1,
\]

(3.2) follows. \(\square\)

### Exact bottleneck

For any \(y=o(N)\), a transversal \(D_N\) of \(\mathcal C(U_y)\) gives a
rigid set \(A_N=U_y\setminus D_N\). Conversely, the deleted set of every
rigid subset of \(U_y\) is such a transversal. Hence the top-slab route
succeeds exactly when

\[
\tau(\mathcal C(U_y))=o(N)                                      \tag{3.4}
\]

for some \(y=o(N)\). In view of Lemma 3, the following stronger estimate
would suffice:

\[
\frac{\tau(\mathcal C(U_y))}{\tau^*(\mathcal C(U_y))}
=o(\log N).                                                       \tag{3.5}
\]

A constant or \(\operatorname{polyloglog}N\) gap would be ample. No such
rounding theorem is proved here.

## 4. Connected prime-token representation

### Lemma 4 (factor-transfer graph)

Let \((S,T)\) be conformally primitive. For every prime \(p\), match the
occurrences of \(p\), counted with multiplicity, on the two sides. Regard a
matched pair as an edge labelled \(p\) between the corresponding vertices of
\(S\) and \(T\). The resulting bipartite multigraph \(G\) has:

1. \(G\) connected, for every choice of occurrence matchings;
2. incident-label product equal to \(n\) at vertex \(n\);
3. degree \(\Omega(n)\) at vertex \(n\);
4. if \(k=|S|+|T|\) and \(E=|E(G)|\), then

   \[
   E=\sum_{a\in S}\Omega(a)=\sum_{b\in T}\Omega(b)\ge k-1.        \tag{4.1}
   \]

**Proof.** Product equality supplies equal numbers of \(p\)-occurrences on
the two sides, so the matching exists and properties 2 and 3 are immediate.
If \(G\) were disconnected, the vertices of any component would contain both
ends of every matched occurrence incident with them. Their products on the
two sides would be equal, giving a nonempty proper conformal subrelation.
This contradicts primitivity. Finally, a connected graph on \(k\) vertices
has at least \(k-1\) edges. \(\square\)

Thus this is not an arbitrary long-edge hypergraph: every obstruction
supports a connected, multiplicatively labelled transfer graph. Any rounding
proof must exploit that structure.

## 5. Circuit counts and an alteration criterion

Let \(M=|U|\), and let \(R_{r,s}(U)\) count oriented relations with
\(|S|=r<s=|T|\), primitive or not. Then

\[
R_{r,s}(U)\le {M\choose r}{M\choose s-1}.                         \tag{5.1}
\]

Indeed, record \(S\) and \(T\) with its largest element omitted. The omitted
element is uniquely determined as the quotient of the two known products,
so this encoding is injective. For support \(k\) and imbalance \(d\),

\[
r=(k-d)/2,\qquad s=(k+d)/2,
\]

and (5.1) applies subject to (2.3). In particular,

\[
\log R_{r,s}(U)
\le r\log\frac{eM}{r}+(s-1)\log\frac{eM}{s-1}.                   \tag{5.2}
\]

This rigorous count is much too large for a direct union bound.

There is a precise weighted alteration statement. Let \(\mathcal R(U)\)
contain every primitive oriented circuit. For \(\lambda\ge1\), independently
delete \(n\) with probability

\[
q_n=\min(1,\lambda x_n).
\]

If a circuit of imbalance \(d\) has no \(q_n=1\), its survival probability
is at most

\[
\prod_{n\in C}(1-\lambda x_n)
\le\exp\!\left(-\lambda\sum_{n\in C}x_n\right)
\le e^{-\lambda d}.
\]

Adding one vertex from every surviving circuit gives

\[
\tau(\mathcal C(U))
\le\frac{\lambda N}{\log N}
  +\sum_{C\in\mathcal R(U)}e^{-\lambda d(C)}.                    \tag{5.3}
\]

Thus a weighted circuit-count estimate making the final sum \(o(N)\) for
some \(\lambda=o(\log N)\) would solve the problem. The next construction
shows why counting individual circuits is intrinsically too crude.

## 6. Sharp squarefree circuits from \(K_{D,D+1}\)

### Lemma 5 (complete-bipartite circuit)

Fix \(D\ge2\), and assign distinct primes

\[
p_{ij}\qquad(1\le i\le D,\ 1\le j\le D+1)
\]

to the edges of \(K_{D,D+1}\). Define

\[
a_i=\prod_{j=1}^{D+1}p_{ij},\qquad
b_j=\prod_{i=1}^{D}p_{ij}.                                      \tag{6.1}
\]

Then all \(2D+1\) integers in (6.1) are distinct and squarefree, and

\[
\prod_{i=1}^{D}a_i=\prod_{j=1}^{D+1}b_j.                         \tag{6.2}
\]

This is a conformally primitive bad circuit of imbalance \(1\).

**Proof.** Every edge prime occurs once on each side. Unique factorization
shows that all vertex products are distinct. For a conformal subrelation,
let \(I\) be its chosen rows and \(J\) its chosen columns. Balancing
\(p_{ij}\) says

\[
\mathbf 1_{i\in I}=\mathbf 1_{j\in J}.
\]

For every \(i,j\), these equalities force either \(I=J=\varnothing\) or all
rows and columns to be chosen. \(\square\)

Choose all edge primes in \([Q,2Q]\), and put

\[
y=Q^D,\qquad N=(2Q)^{D+1}.
\]

Every vertex lies in \([y,N]\), while

\[
H=\log(N/y)=\log Q+(D+1)\log2
\]

and

\[
\frac{\log N}{H}
=\frac{(D+1)(\log Q+\log2)}{\log Q+(D+1)\log2}
=(1+o(1))(D+1)                                                   \tag{6.3}
\]

when \(D/\log Q\to0\). Thus the actual support \(2D+1\) asymptotically meets
(2.2). Also

\[
\frac yN=\frac1{2^{D+1}Q}=o(1),
\]

so sharpness occurs inside density-\(1-o(1)\) top slabs. The standard prime
number theorem supplies the \(D(D+1)\) primes after \(Q\) is chosen large
relative to \(D\).

These circuits are extremely numerous. If \([Q,2Q]\) contains \(L\) primes
and \(L\ge2D(D+1)\), distinct assignments to the labelled edges yield at
least

\[
\frac{(L)_{D(D+1)}}{D!(D+1)!}                                   \tag{6.4}
\]

different oriented supports. Unique factorization and
\(\gcd(a_i,b_j)=p_{ij}\) reconstruct an assignment up to row and column
permutations. With \(L\asymp Q/\log Q\), the logarithm of (6.4) is

\[
(1+o(1))D(D+1)\log Q=(1+o(1))D\log N.                            \tag{6.5}
\]

Therefore neither an \(N^{o(1)}\) circuit-count bound, a stronger universal
support bound, nor a claim that every circuit contains a perfect power can
hold.

Yet this huge family is cheaply clustered: each circuit contains all
\(D+1\) column products below

\[
(2Q)^D=\frac{N}{2Q}=o(N).
\]

Deleting that lower band hits the whole family. This demonstrates exactly
why (5.3), which charges circuits one at a time, loses the relevant overlap.

## 7. Proposed mechanism and weakest unsupported step

The viable dependency chain is:

1. pass to \(U_y\) with \(y=o(N)\);
2. reduce to primitive circuits by Lemma 1;
3. use the deficit fractional cover from Lemma 3;
4. cluster circuits via their connected prime-token graphs, sharing either a
   low-scale vertex set or a maximal-prime transfer pattern;
5. round one representative per cluster at total cost \(o(N)\).

Steps 1–3 are rigorous. Lemma 4 supplies the structure for step 4, but no
adequate clustering theorem is known. The first unsupported step is thus:

> **Arithmetic circuit rounding lemma.** For some \(y=o(N)\), the clutter
> of conformally primitive prime-token circuits on \([y,N]\) has transversal
> number at most \(o(\log N)\) times its deficit fractional-transversal
> number.

Together with Lemma 3, this would prove the finite density-\(1-o(1)\)
assertion under distinct factors. Lemma 5 proves that its argument must be
cluster-aware: minimum support, squarefreeness, and raw counts are
insufficient.

## 8. Falsification tests and next action

Lemma 5 already falsifies any proposed assertion that:

- primitive bad circuits are asymptotically longer than (2.2);
- there are only polynomially or \(N^{o(1)}\) many primitive circuits;
- every primitive imbalance circuit contains a prime power;
- independent deletion plus a union bound over individual circuits closes
  the problem.

A concrete finite test for a proposed rounding lemma is:

1. enumerate subset products in a small top slab, keyed by product and
   cardinality;
2. cancel intersections and retain conformally primitive cross-cardinality
   collisions;
3. compute the fractional and integral hitting numbers of their supports;
4. adjoin the explicit \(K_{D,D+1}\) circuits and test the proposed pivot or
   cluster rule on them.

The next mathematical action is maximal-prime elimination in Lemma 4:
group circuits by the vertices incident with their largest prime, cancel
that label, and seek a recursive charge to lower-scale vertices. The target
is a cluster cover of cost

\[
O\!\left(\frac{N\,\operatorname{polyloglog}N}{\log N}\right).
\]

If this recursion fails, the useful negative artifact would be an explicit
family of primitive circuits with integral transversal number \(\Omega(N)\);
that would show the top-slab route itself cannot yield density one.
