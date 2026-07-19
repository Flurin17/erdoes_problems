# Status: Erdős #786

## Goal

Consolidate and adversarially audit the now-complete negative solution of
both questions under the literal repetition-allowed reading. In parallel,
continue the separate internally repetition-free variant left ambiguous by
the source, without importing the grading theorem as a necessary condition.

## Context

Authoritative input: PROBLEM.md. Under repetitions, NOTES.md proves that PLR
is equivalent to containment in an exact nonzero level of a rational
completely additive function. PROOF.md proves that every infinite PLR set
has lower density at most \(1/2\), and that some absolute \(\eta>0\) satisfies
\(|A_N|\leq(1-\eta)N\) for every finite repetition-allowed PLR set. The
finite proof combines exact Halász--Ruzsa concentration with an audited
boundary sieve for bounded active-prime harmonic mass.

## Constraints

No web search, browser, erdosproblems.com query, external literature lookup, repository-wide hidden-solution search, or Git-history solution search. Use only the named local files and standard mathematics, labeling uncertain remembered theorems. Do not infer a proof from computation. Quantify over arbitrary unbounded \(r,s\geq1\); do not confuse rigidity with unique factorization or multiplicative independence. Preserve both density and repetition ambiguities explicitly. Existing unrelated worktree changes in Problems 425 and 796 must remain untouched.

## Deliverables

Maintain the audited infinite proof in PROOF.md; exact structural lemmas in
NOTES.md; serious routes and failures in attempts/; reproducible exact finite
experiments in computational/; and the route ranking below. Commit and push
coherent Problem 786 milestones without including unrelated changes.

## Done when

The repetition-allowed reading is complete when the infinite and finite
negative proofs are dependency-complete, receive two fresh targeted audits,
and are committed and pushed with accurate ledgers. Full ambiguity closure
would additionally require a decision of the internally distinct reading;
until then it must remain explicitly classified as open rather than being
silently identified with the literal reading.

## State

### Convention ledger

- Primary reading: \(r,s\geq1\), repetitions allowed, natural density.
- Secondary reading: each factor list is internally distinct. It is strictly
  weaker: \(\{4,8\}\) separates the conventions.
- The infinite set may depend on \(\epsilon\). Upper density is never
  substituted for natural or lower density.

### Complete result: repetition-allowed version

Every repetition-allowed PLR set satisfies
\[
\underline d(A)\leq\frac12.
\]
Thus the requested “for every \(\epsilon>0\)” assertion is false (already for
\(\epsilon\leq1/2\)). The proof uses the exact grading theorem, zeta
probability, a zero-drift compound-Poisson representation, and a winding
number bound on nonzero atoms. Two fresh targeted audits found no error.

There is also an absolute \(\eta>0\) such that every finite
repetition-allowed PLR set satisfies
\[
 |A_N|\leq(1-\eta)N.
\]
Hence the finite density-\(1-o(1)\) assertion is false. The proof splits by
the reciprocal mass \(H=\sum_{f(p)\ne0}1/p\): exact Halász--Ruzsa
concentration handles large \(H\); for bounded \(H\), a lightly deleted
polynomial prime band transports a harmonic supply of zero-core anchors to
\(c_HN\) distinct zero-valued integers in \((N/2,N]\). Independent audits
certified both the analytic exact-atom specialization and the full
convolution/injectivity ledger.

### Finite proved facts

1. Exact finite PLR is equivalent to
   \(\operatorname{rank}V_A=\operatorname{rank}[V_A\mid\mathbf1]\).
2. Every nonzero exact additive level, and hence every finite
   repetition-allowed PLR set, omits an absolute positive proportion.
3. A threshold grading gives
   \[
   |A_N|=(c_*+o(1))N,\quad
   c_*=2-2\rho(1+\sqrt e)-\log(1+\sqrt e)
   =0.828499\ldots .
   \]
4. The earlier quantitative bound
   \[
   N-|A_N|\geq cN/\log N
   \]
   for an absolute \(c>0\), by prime--cofactor overlap and multiplicative
   energy. A fresh audit certified the proof.
5. Still earlier independent bounds include
   \(m_N+1\geq N^{0.227092\ldots-o(1)}\) and the smooth-number
   self-consistency inequality.
6. Any finite bad set has a bounded circuit witness; modular certificates
   whose lcm exceeds the explicit determinant bound imply exact PLR.

### Route tournament

1. **Exact concentration plus bounded-budget boundary sieve (complete).**
   Halász--Ruzsa gives \(O(H^{-1/2})\) point concentration for large active
   harmonic mass. For bounded \(H\), a fixed-fold local prime convolution
   and harmonic zero-core anchors give a linear zero fiber. This proves the
   finite absolute gap without an invalid product-measure transfer.
2. **Largest-prime/cofactor modal construction.** Only plausible positive
   route. An exact Bellman identity is proved; the natural globally completed
   single-threshold family cannot beat \(0.828499\ldots\) when its lower
   cutoff is at least \(N^{1/4}\).
3. **Multi-band weighted grading.** The single threshold achieves
   \(0.828499\ldots\). Exhaustive rational/binary/ternary finite grids at
   \(N=100000\) found no improvement; moving \(N^{o(1)}\) bands remain open.
4. **Top-slab/hypergraph deletion for distinct factors.** Unequal-cardinality
   relations have an \(o(N)\) fractional transversal, but no integral
   rounding is known. Explicit primitive squarefree circuits of support
   \((2+o(1))\log N/\log\log N\) occur already in the rough slab
   \((N/(C\log N),N]\), showing that deleting only a lower initial segment
   does not solve this variant.
5. **Conditioned Euler/divisor-box measures.** Could strengthen the finite
   Canonical power-Euler laws, positive mixtures, divisor boxes, and
   two-sided-flat product laws are rigorously ruled out. An arbitrary
   one-sided uniformly integrable product law remains a precise gap.

### Reproducible finite computation

- computational/modal_exact.py exactly computes the maximum additive level:
  the complete table is certified for \(2\leq N\leq50\), with \(M(60)=39\).
  Independent exhaustive subset/rank search agrees through \(N=14\).
- computational/multiband_search.py exhaustively checked the recorded
  three-/four-band and binary/ternary grids. At \(N=100000\), the best
  threshold has \(80421\) elements; the best genuine multisegment candidate
  has \(79612\).
- Coordinator reruns reproduced the modal table and both exact rank checks
  for the \(N=100000\) binary multiband search.

### Dead or sharply limited routes

- Exclusive protected markers have density at most \(1/e\).
- Pure modular certificates provide exactness but no dense common level.
- Naive compactness loses density; naive block unions introduce cross-block
  relations.
- The canonical local modal recursion chooses a nonzero weight at \(2\) and
  is capped at \(1/2\).
- Independent-geometric prime models fail uniformly for moving supports:
  the \(p>\sqrt N\) threshold has uniform mass \(\log2\) but product-model
  mass \((\log2)/2\).

### Current bottleneck

The literal repetition-allowed problem is solved negatively. The remaining
mathematical ambiguity is the internally distinct-factor variant. Its bad
relations can be logarithmically long and clustered; the known fractional
transversal has total \(o(N)\), but no cluster-aware integral rounding or
opposite constant-gap theorem is known. Determining that variant, and the
sharp finite repetition-allowed extremal constant between the construction
\(0.828499\ldots\) and the qualitative upper gap, are separate open tasks.
