# Dyadic-graph audit of the finite constant-gap proof

## Scope and conclusion

This independently audits finite_constant_gap_ratio_grid.md, concentrating
on its globally disjoint ratio-grid matching and shifted-Cauchy closure. I
found no mathematical defect. Conditional only on the standard uniform
rough-number estimate stated as (7) there, the proof gives an absolute gap
below density one for every nonzero rational additive level.

## 1. Why bounded-length circuit packing cannot work

Fix \(L\geq2\). If
\[
 a_1\cdots a_r=b_1\cdots b_s,\qquad r\ne s,\qquad 1\leq r,s\leq L,
\]
with all factors at most \(N\), then at least one factor is at most
\(N^{1-1/L}\). Indeed, assume \(r>s\). If all factors were larger than
\(N^{1-1/L}\), then
\[
 a_1\cdots a_r>N^{r(1-1/L)}\geq N^{r-1}\geq N^s
 \geq b_1\cdots b_s,
\]
a contradiction. Thus \([1,N^{1-1/L}]\) is an \(o(N)\)-sized transversal
for all unequal relations having at most \(L\) factors on either side. No
fixed-uniformity matching or fractional matching can prove a constant
deficit.

Common dilation also cannot clone such a circuit. If coefficients \(e_n\)
satisfy \(\sum e_n v(n)=0\) but \(E:=\sum e_n\ne0\), replacing every \(n\)
by \(kn\) changes the valuation sum to \(E v(k)\). The ratio-grid proof
correctly avoids these two obstructions by pairing vertices known to have
different additive values.

## 2. Exact dense-rectangle mechanism

Let \(P\subset(X,2X]\) be primes and \(K\subset[1,Y]\), where \(2Y<X\) and
\(2XY\leq N\). The map
\[
 P\times K\longrightarrow[1,N],\qquad (p,k)\longmapsto pk
\]
is injective: if \(pk=q\ell\) and \(p\ne q\), then \(p\mid\ell<p\), which
is impossible. For a completely additive \(f\) and target \(t\), the
fraction of this rectangle on the level \(t\) is
\[
 \sum_x\mu_P(x)\mu_K(t-x).
\]
If this is at least \(1-\eta\), each marginal has an atom of mass at least
\(1-\eta\); for \(\eta<1/3\), their modal values must sum to \(t\).

## 3. Same-band matching

For a prime band \(\mathcal P_i\), the complete multipartite graph on exact
\(f(p)\)-classes has a matching of size at least half the number of
nonmodal primes. Lift a matched pair \((p,q)\) by a \(y\)-smooth \(k\).
The endpoints \(pk,qk\) have different values. Since \(p,q>y\), the unique
prime factor above \(y\) identifies the side, the pair, and then \(k\);
all lifted edges are globally disjoint. The Dickman parameter
\(\log(N/2^{i+1})/\log y\) remains in a compact interval depending only on
fixed \(\alpha\). Consequently (15)--(17), including
\(\sum_i r_i=o(L)\), follow.

## 4. Prime--semiprime allocation and collision ledger

For a fixed target band \(t\), at most \(2|I|=O(L)\) source triples
\((i,j,\varepsilon)\) satisfy \(i+j+\varepsilon=t\). Each requests
\(O(\zeta2^t/L^2)\) modal semiprimes, so the total request is
\(O(\zeta2^t/L)\). A good target band contains \(\gg2^t/L\) modal primes.
Taking \(\zeta\) below the ratio of these constants permits a globally
injective allocation of one target prime to every selected semiprime.

After a smooth lift, a prime endpoint has exactly one prime factor above
\(y\), while a semiprime endpoint has exactly two, counted with
multiplicity. Repeated primes are excluded when \(i=j\). The complete
multiset of factors above \(y\) distinguishes the sides and recovers the
assigned base; division recovers \(k\). Different target bands cannot
collide. Hence every failed modal equation contributes
\(\gg_\alpha N/L^2\) new vertex-disjoint edges, validating (33)--(36).

## 5. Shifted-Cauchy stability

The stability proof is sound. The unshifted equation makes all but
\(O(\epsilon n)\) increments \(F(x+h)-F(x)\) equal a modal \(d_h\).
Intersecting three good sets proves \(d_{h+k}=d_h+d_k\), hence \(d_h=hu\).
An anchor average gives \(F(x)=ux+v\) off \(O(\epsilon n)\) points.
Triangular representation counts then give \(G(s)=us+2v\) off
\(O(\sqrt\epsilon\,n)\) points. The shifted relation forces \(u=0\), and
the macroscopic overlap \(I\cap(I+I)\) forces \(v=0\).

There is one harmless endpoint notation issue: for \(x=z=n-1\), the shifted
output is \(G(2n-1)\), just beyond the set \(T\subset[0,2n-2]\) in (47).
Excluding this single pair repairs the sentence without changing an
\(o(n^2)\) estimate.

## 6. Final transfer

Equation (54) correctly gives \(o(1)\) reciprocal mass for active middle
primes: zero modal bands leave only their \(r_i\)-fraction active, while
the \(o(L)\) exceptional bands contribute \(o(L)O(1/L)=o(1)\). Mertens
and a union bound then reduce the level to primes at most \(y=N^\alpha\),
apart from \(O(\alpha)+o(1)\) of the integers.

The total-variation identity (64) is exact. On
\(D\leq N/y^{u/2}\), input (7) compares point masses uniformly. The model
boundary has probability \(O(1/u)\) because
\(\mathbb E\log D\sim\log y\), and normalization gives the same control
for the actual boundary. Lemma 2's atom estimate is also correct:

* sparse active reciprocal mass makes every nonzero atom small;
* one active small prime bounds every convolution atom by \(7/8\);
* otherwise a subcollection of reciprocal mass in \([1/8,1/4)\) has zero
  atom at most \(e^{-1/8}+1/32\) and every nonzero atom below \(1/4\).

Thus (59) and (78) contradict each other after fixed \(\alpha\) is chosen
small. The quantifier order is correct: choose \(\alpha\), then let
\(N\to\infty\).

## Verdict

The candidate proves an absolute asymptotic density gap for the finite
repetition-allowed reading. It does not address internally distinct
factors. Before promotion, state (7) as a named standard rough-number
theorem and fix the one endpoint notation above; no combinatorial repair is
otherwise needed.
