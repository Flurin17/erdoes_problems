# Oriented return times from a CRT-box chain

## Setup

Let
\[
 \mathcal P=\{p:k<p<2k\},\qquad P=\prod_{p\in\mathcal P}p,
\]
and put
\[
 q_p=p-k,\qquad r_p=q_p-1=p-k-1,
 \qquad \mathbf r=(r_p)_{p\in\mathcal P}.
\]
After translating by (t=n-(k+1)), admissibility is exactly
\[
 t\bmod p\in\{0,1,\ldots,r_p\}\quad(p\in\mathcal P),
 \qquad t\ge k.
\]
Under the CRT identification define
\[
 V=\prod_{p\in\mathcal P}\{0,1,\ldots,r_p\},
 \qquad
 \tau_k=\min\{t\ge k:t\bmod P\in V\}.
\]
Then (n_k=k+1+\tau_k).  Write
\[
 R=\sum_{p\in\mathcal P}r_p,
 \qquad r_{\min}=\min_{p\in\mathcal P}r_p,
 \qquad U=P-k-1.
\]

The top vector \(\mathbf r\) has representative (U), since
\(r_p\equiv-(k+1)\pmod p\).  Every representative of (V) lies in
([0,U]): if (t=P-s), (1\le s\le k), then
\[
 t\bmod p=p-s\ge p-k=r_p+1.
\]
Consequently, for the CRT representative \(\rho(x)\in[0,P)\),
\[
 \rho(\mathbf r-x)=U-\rho(x),                  \tag{1}
\]
and equivalently
\[
 -V=(k+1)+V.                                   \tag{2}
\]
Also
\[
 V\cap[0,k)=\{0,1,\ldots,r_{\min}\}.          \tag{3}
\]

## The block-path theorem

**Theorem.** Suppose either (r_{\min}=0) and (R\ge2), or
(r_{\min}>0) and (|\mathcal P|\ge4).  Then
\[
 \boxed{R\tau_k\le P-k-1},                     \tag{4}
\]
and hence
\[
 \boxed{
 n_k\le k+1+\left\lfloor\frac{P-k-1}{R}\right\rfloor .
 }                                              \tag{5}
\]

### Construction of the chain

The (r_p) are distinct.  Assume first that (r_{\min}>0).  Order the
coordinates so that the unique minimum and maximum (r_p) are interior
blocks, leaving two nonextreme coordinates as the first and last blocks.
Starting at (0), increase the first coordinate one unit at a time to its
top, then the second, and so on.  This saturated block path is a chain
\[
 C=\{c_0,c_1,\ldots,c_R\},\qquad c_0=0,quad c_R=\mathbf r.             \tag{6}
\]

The two exceptional difference families are
\[
 d\mathbf1\quad(1\le d\le r_{\min})             \tag{7}
\]
and
\[
 \mathbf r-d\mathbf1\quad(0\le d\le r_{\min}). \tag{8}
\]
No chain difference has form (7).  Such a segment has positive increment in
every coordinate, hence spans every interior block.  Its increment in the
interior maximum block is (r_{\max}>r_{\min}\), not (d).

No chain difference has form (8), except the endpoint difference
\(\mathbf r=c_R-c_0\).  Both endpoint block lengths exceed
(r_{\min}\), so such a segment spans all interior blocks.  In the interior
maximum block its increment is (r_{\max}), whereas (8) asks for
(r_{\max}-d); hence (d=0), which forces the two endpoints.

If (r_{\min}=0), the zero coordinate rules out every positive diagonal
difference (7), and (8) permits only (d=0).  Thus any saturated block path
has the same property.  The condition (R\ge2) ensures an internal chain
point, so the exceptional endpoints will not form an ordinary linear gap.

### Numerical orientation of the gaps

Sort the representatives of the chain:
\[
 0=a_0<a_1<\cdots<a_R=U.                        \tag{9}
\]
The endpoints make the known cyclic wrap gap (P-U=k+1).  The (R)
ordinary gaps satisfy
\[
 D_j=a_j-a_{j-1},qquad \sum_{j=1}^R D_j=U.      \tag{10}
\]
Their endpoint vectors are comparable.

If coordinate order agrees with numerical order, (D_j\bmod P\in V).
Were (D_j<k), then (D_j<p) for every relevant prime and the coordinate
difference would be (D_j\mathbf1), contradicting (7).  Hence
(D_j\ge k), and (D_j) is an anchored return.

If the two orders disagree, (D_j\bmod P\in-V=(k+1)+V).  No positive
integer at most (k) is in (-V), so (D_j\ge k+1), and
\[
 T_j=D_j-(k+1)\in V.                            \tag{11}
\]
If (T_j<k), (3) gives (0\le T_j\le r_{\min}), and the positive
coordinate difference is
\[
 \mathbf r-T_j\mathbf1,                        \tag{12}
\]
contradicting (8).  The sole permitted endpoint pair is the excluded cyclic
wrap, not an ordinary gap.  Thus (T_j\ge k), so
\(\tau_k\le T_j<D_j\).

Every ordinary gap is therefore at least \(\tau_k\).  Summing (10) proves
(4).  This is also an explicit construction: compute and sort the CRT
representatives of the block path, take a least ordinary gap, and output
either (t=D_j) or (t=D_j-(k+1)), according to its orientation.

## Scope and small-dimensional fallback

The theorem applies for all sufficiently large (k), since PNT gives
(|\mathcal P|\sim k/\log k\).  For two or three positive coordinates, fix a
coordinate (f) with (r_f>r_{\min}) and take a saturated chain in the
slice (x_f=0).  It has
\[
 L=1+R-r_f
\]
points.  Its differences cannot have form (7), or form (8), because the
(f)-coordinate of those vectors is respectively positive or
(r_f-d>0).  All (L) cyclic gaps are nonexceptional, giving
\[
 \tau_k\le\left\lfloor\frac P{1+R-r_f}\right\rfloor .                 \tag{13}
\]
Choosing the second-smallest (r_f) maximizes the denominator.  With one
relevant prime (p), directly \(\tau_k=p\).  Empty and remaining finite
cases are covered by the exact residue definition and the repository's
finite certificates.

## Asymptotic consequence

Partial summation and PNT give
\[
 R=\sum_{k<p<2k}(p-k-1)
  =\left(1+o(1)\right)\int_k^{2k}\frac{x-k}{\log x}\,dx
  =\left(\frac12+o(1)\right)\frac{k^2}{\log k}.                       \tag{14}
\]
Thus
\[
 \boxed{n_k\le k+1+(2+o(1))P\frac{\log k}{k^2}}                      \tag{15}
\]
and, since \(\log P=k+o(k)\), this remains \(\exp(k+o(k))\).  It is a
polynomial improvement over the previous ((1/2+o(1))P) construction, not
the conjectural \(\exp((2\log2+o(1))k/\log k)\) scale.

The denominator (R) is optimal for a pairwise-comparable-family plus
cyclic-pigeonhole method: a product-box chain has at most (R+1) points, and
every chain of that size contains (0,\mathbf r), whose wrap gap is the
trivial (k+1).

## Why unsigned recurrence tools stop short

Let (Q=|V|=\prod_pq_p) and \(\delta=Q/P\).

### Signed Blichfeldt recurrence

Set (L=2k+1), (M=\lfloor P/Q\rfloor), and consider the (M+1)
translates (jL+V) in the CRT group.  Their total cardinality exceeds (P),
so two overlap.  For large (k) this gives
\[
 2k<d\le(2k+1)\lfloor\delta^{-1}\rfloor<P
\]
with signed coordinate representatives
\[
 -r_p\le e_p\le r_p.                            \tag{16}
\]
Uniformly nonnegative signs give (d\in V); uniformly nonpositive signs
give (d-(k+1)\in V) by (2).  Mixed signs are the precise obstruction.
Symmetric Blichfeldt or Minkowski therefore reaches reciprocal density up to
a polynomial, but only in the signed difference box.

Indeed,
\[
 V-V=(k+1)+2V,qquad |V-V|=\prod_p(2q_p-1),      \tag{17}
\]
and
\[
 \frac{|V-V|}{|V|}
 =\prod_p\left(2-\frac1{q_p}\right)
 =\exp\left((\log2+o(1))\frac{k}{\log k}\right). \tag{18}
\]
The gain from symmetrization equals the exponential number of sign cells;
only the two uniform orientations return to the one-sided box.

### Kac/average-gap recurrence

The (Q) cyclic gaps between all representatives of (V) sum to (P), so
their average is (P/Q=\delta^{-1}), the finite cyclic Kac identity.  This
finds a short gap between unspecified points, but only in (V-V), with
uncontrolled coordinate signs.  It does not control the distinguished
return after (t=k); the universal top-to-zero chord of length (k+1)
merely recovers the trivial shifted return (t=0).

This is intrinsic to translation-invariant additive data.  In
\(\mathbb Z/N\mathbb Z),
\[
 A=\{0,1,\ldots,L-1\}\quad\hbox{and}\quad -A
\]
have identical difference sets, autocorrelations, energies, and covering
invariants, but least positive representatives (1) and (N-L+1).

### Generic poset pigeonhole

The product poset (V) has (R+1) rank levels, so it has an antichain of
size at least
\[
 \frac Q{R+1}.                                  \tag{19}
\]
Partitioning the CRT group into coordinate cells of side at most (q_p)
gives signed-small differences inside each cell, but common signs require a
comparable pair.  Taking a largest antichain in every cell leaves at least
(P/(R+1)) group elements without any forced same-cell comparable pair.
Thus a cardinality-only cell/poset argument can still require
\(\exp(k+o(k))\) orbit points.  The successful chain construction instead
uses the common complement (1), the known wrap gap, and a deliberately
oriented family.

The remaining sharp upper bound requires anchored, orientation-sensitive
cancellation or discrepancy, not volume, symmetric recurrence, or additive
growth alone.
