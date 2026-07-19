# Audit of `adaptive_rounding.md`

## Verdict

The main asymptotic result is correct after one local repair.  The first
displayed finite-choice lemma is false for small moduli as stated, but the
proof only uses it for a modulus tending to infinity, where the repaired
lemma applies.  I found no further invalid inference in the band estimate,
the power reduction, the archimedean localization, or the Halasz/Fourier
step.

## First invalid inference and exact repair

Equation (3) cannot hold uniformly over *all* primes `q` with a positive
constant depending only on `D`.  For example, take

\[
 q=2,\qquad a=1,\qquad E=\{0,1\},\qquad z=0.
\]

For each residue `j`, one can choose `e` so that `j+e=0 (mod 2)`, and hence
every minimum in (3) is zero.  More generally, the same obstruction occurs
whenever the reductions of `E` cover all residues modulo `q`.  This is also
where the proof on lines 36--41 implicitly needs the additive `O(D)` term
in the union bound to be small compared with `q`.

The needed repaired lemma is:

> For every fixed `D` there are `q_0(D)` and `c_D>0` such that (3) holds
> whenever `q>=q_0(D)`, `1<=a<q`, and `1<=|E|<=D`.

Indeed, for a fixed `e`, the set on which the loss is below `eta` has at
most `A q sqrt(eta)+A` residues, for an absolute `A`.  The union has at most
`ADq sqrt(eta)+AD` residues.  First choose `eta=(8AD)^{-2}` and then require
`q>=4AD`; at least (say) `q/2` residues have loss at least `eta`, giving
`c_D=eta/2`.  This also makes explicit that `E` must be nonempty.

In the application, `D=|E_C|` is fixed while

\[
 q\asymp (\log K)^{1/4}\longrightarrow\infty.
\]

Thus `q>=q_0(D)` for all sufficiently large `N`, and this defect does not
affect the theorem.  Equation (4) should likewise include
`q>=q_0(C)` (and is only needed in that range).

## Band estimate

On the `j`th band, `x_p` lies in `(j,j+1]`, so integrality and (1) give
`B_N(p)=j+e_p` with `e_p` in a fixed set of size `O_C(1)`.  Replacing
`gamma x_p` by `gamma j` changes each cosine loss by
`O(|gamma|/q)`.  Across a block of `q` consecutive bands, freezing
`gamma j` changes it by `O(|gamma|)`.  After multiplication by the prime
harmonic weights, the total perturbation is therefore
`O(|gamma| log K)=o(1)` in the stated range.

The PNT-Mertens estimate (7) is uniform here because the smallest endpoint
has logarithm at least `(q^2/K) log N`; summing its absolute errors gives

\[
 O\!\left(\frac{K}{\log N}\sum_{j=q^2}^{K-1}\frac1j\right)
 =O\!\left(\frac{K\log K}{\log N}\right)=o(1).
\]

Within a complete block the weights are relatively
`1+O(q/j)=1+O(1/q)` since `j>=q^2`.  The repaired circle lemma hence yields
a constant fraction of

\[
 \sum_{q^2\le j<K}\frac1j
 =\log(K/q^2)+O(1).
\]

For the stated general range `q=o(K^{1/3})`, this is bounded below by a
positive constant times `log K`; for the selected modulus it is
`(1+o(1))log K`.  Thus (4) is quantitatively valid after adding the lower
bound on `q`.

## Power reduction and archimedean localization

For unit complex numbers,

\[
 1-\Re(z^q\overline{w^q})
 =\tfrac12|z^q-w^q|^2
 \le q^2\tfrac12|z-w|^2.
\]

Summing this with `z=g_a(p)` and `w=p^{it}`, and using `g_a(p)^q=1`,
proves (10) from the assumed bound with no missing factor.

The estimates (11)--(12) have the required uniformity for
`|u|<=qK`: (11) is the standard PNT-Mertens partial-summation estimate;
for `1<=|u|<=qK`, comparison at
`sigma=1+1/log N` gives

\[
 \sum_{p\le N}\frac{\cos(u\log p)}p
 \le \log|\zeta(\sigma+iu)|+O(1)
 \ll \log\log(3+|u|)+1,
\]

which yields (12).  Since `K=floor(log log N)` and
`qK=K(log K)^{1/4+o(1)}`, the right side of (12) is
`K-O(log log K)`, much larger than `delta log K`.  Hence (10) first forces
`|u|<1`.  Equation (11) then yields
`|u| log N <= O(K^{C_0 delta})`.  Choose
`delta<min(c_C,1/(4C_0))`; the harmless leading constant is absorbed by
the strict exponent inequality, so

\[
 |\gamma|=\frac{|u|\log N}{2\pi K}\le K^{-3/4}
\]

for sufficiently large `N`.  The identity between the resulting cosine
and the prime summand of the pretentious distance is exact.  Estimate (4)
then contradicts the hypothesized distance, proving (9), with its implicit
constant allowed to depend on `C`.

## Halasz normalization and Fourier inversion

The quoted quantitative Halasz form is correctly normalized for

\[
 \mathcal M=\min_{|t|\le T}\sum_{p\le N}
 \frac{1-\Re(g(p)p^{-it})}{p},\qquad T=K,
\]

and gives an error `O(T^{-1/2})`.  With
`q asymp (log K)^{1/4}`, (9) gives

\[
 \mathcal M\gg_C \frac{\log K}{q^2}
 \asymp_C \sqrt{\log K}.
\]

Consequently both `(1+M)e^{-M}` and `K^{-1/2}` are
`o(q^{-1})`, uniformly in `1<=a<q`.  Fourier inversion has error at most
the supremum of these nontrivial Fourier coefficients (not `q` times that
supremum), since its outer factor is `1/q`; hence (16) follows with
`o(q^{-1})`.  Containment of an exact integer level in a residue class then
gives (2).

## Ancillary statements

Equations (18)--(20) are also valid (with fixed `u>=1` in the Dickman
statement): integers on which the congruence can fail form either the
union of the indicated prime divisibility events or, in (20), a subset of
the nonsmooth integers.  The two lexicographic observations use
`0<=b_N(n)<=K` and `|d_N(n)|<=D floor(log_2 N)`, respectively, and are
correct.
