# Fresh audit of the bounded-active-mass zero-core theorem

Audited file: `rough_concentration_active_core.md`, through Theorem 1 and
the proof ending at (26).  This audit is independent of the later
Halász--Ruzsa dependency.

## Verdict

**Certified.**  I found no invalid inference.  For every fixed (K), the
argument proves the claimed linear zero core uniformly in the completely
additive function and in its moving set of active primes.  Constants and
the lower threshold for (N) may depend on (K), as the theorem allows.

## Checks

1. **Lemma 2 and its constants.**  The Euler product in (5) is exactly the
   Dirichlet series of integers avoiding the finite forbidden set.  Since
   (p^{-\sigma}\leq p^{-1}\leq 1/2), (6) follows from
   \(\log(1-u)\geq-2u\).  Also
   \(\zeta(\sigma)\geq(\sigma-1)^{-1}=\log X/A\).  The unrestricted tail
   is at most
   \(X^{1-\sigma}/(\sigma-1)=e^{-A}\log X/A\), which is one half of the
   lower bound from the Euler product because
   \(A=2K+\log2\).  Thus the stated
   \(d_K=e^{-2K}/(2A)>0\) is valid.  If (X) is nonintegral, replacing it
   by its integer part changes only a harmless endpoint term (or the
   integral comparison can be started at \(\lfloor X\rfloor\)); this has
   no effect on the sufficiently-large-(X) assertion.

2. **Selection of the clean band.**  The (H) bands are disjoint, lie
   below (N^{1/4}<\sqrt N), and
   \(H\varepsilon _0>K\).  Hence (1) forces (11).  The exponent (a)
   ranges over a finite (K)-dependent set.  Taking (i_0) large first
   makes both (2a<1/4) and the later integer-(k) choice valid for every
   possible selected band.

3. **PNT convolution estimate.**  On exponent space the weighted prime
   measure tends locally to (dt/t).  In the central sum interval the
   convolution density
   \[
      \int_{[a,2a]\cap[s-2a,s-a]}\frac{dt}{t(s-t)}
   \]
   is bounded above and below by constant multiples of (1/a), uniformly
   in (s\in[(3-.1)a,(3+.1)a]).  A cell of exponent width (h\asymp1/L)
   corresponds to a prime interval with fixed endpoint ratio
   \(e^{hL}\), so ordinary PNT gives the discrete lower estimate and the
   uniform translate upper estimate in (14).  Any cell-width constants
   introduced later may depend on fixed (K); PNT is then applied after
   (K) is fixed, which is sufficient.  Finally
   \((\nu*\mu)(W)\leq\|\nu\|\sup_x\mu(W-x)\), and similarly for
   \(\mu_0*\nu\), so the choice
   \(\varepsilon _0<c/(4C)\) really yields (16).

4. **Passage to (r)-tuples.**  For sufficiently small (a), the
   interval
   \((1/(3.05a),1/(2.95a))\) contains an integer (k), so (1\) is in
   the interior of (kJ).  Compact interiority gives a positive uniform
   volume of choices of the first (k-1) cells.  Taking cell width a small
   fixed multiple of (1/L), compared with the target width
   \(\log2/L\), makes the corresponding cell boxes disjoint and wholly
   contained in the target.  There are \(\gg_{a}L^{k-1}\) boxes, each of
   mass \(\gg_a L^{-k}\), proving (19), uniformly in the stated (s).
   The union bound for a repeated coordinate is
   \[
      O_r\!\left(\sum_{q>N^a}q^{-2}
        \left(\sum_{p\in I}p^{-1}\right)^{r-2}\right)
      =O_r(N^{-a})=o(1/L),
   \]
   so removing all repeated-prime tuples before dividing by (r!) is
   justified.

5. **Transport, counting, and injectivity.**  For (b\leq N^{\delta_0}),
   (19) is exactly the product window
   \(N/(2b)<Q\leq N/b\).  Since every tuple there has reciprocal weight
   below (2b/N), (24) follows with the correct inequality direction.
   Distinct ordered tuples represent each unordered prime set exactly
   (r!) times.  Every prime factor of (b) is below (N^a), while all
   (q_i) exceed (N^a); unique factorization therefore recovers both
   (b) and the unordered tuple, even when (b) has prime powers.
   All factors are zero-coloured and below (N^{1/4}).  Lemma 2 applies
   to the active primes up to (X=N^{\delta_0}<\sqrt N), and its harmonic
   lower bound is (d_K\delta_0 L), which cancels the (L) in (24) and
   gives the positive (K)-dependent constant in (26).

The one endpoint nicety in item 1 is purely notational and does not alter
the theorem or any constant after increasing the allowed (N_0(K)).
