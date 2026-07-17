# Status: Erdős #786

## Goal

Having disproved the infinite assertion under the repetition-allowed reading,
decide the finite density-\(1-o(1)\) question under that same reading. In
parallel, determine the infinite and finite answers under the internally
repetition-free reading, which the source leaves ambiguous.

## Context

Authoritative input: PROBLEM.md. Under repetitions, NOTES.md proves that PLR
is equivalent to containment in an exact nonzero level of a rational
completely additive function. PROOF.md, certified by fresh audits, proves
that every infinite PLR set has lower density at most \(1/2\). For finite
\(A_N\), current bounds and constructions leave a gap between retained
density \(0.828499\ldots\) and the requested \(1-o(1)\).

## Constraints

No web search, browser, erdosproblems.com query, external literature lookup, repository-wide hidden-solution search, or Git-history solution search. Use only the named local files and standard mathematics, labeling uncertain remembered theorems. Do not infer a proof from computation. Quantify over arbitrary unbounded \(r,s\geq1\); do not confuse rigidity with unique factorization or multiplicative independence. Preserve both density and repetition ambiguities explicitly. Existing unrelated worktree changes in Problems 425 and 796 must remain untouched.

## Deliverables

Maintain the audited infinite proof in PROOF.md; exact structural lemmas in
NOTES.md; serious routes and failures in attempts/; reproducible exact finite
experiments in computational/; and the route ranking below. Commit and push
coherent Problem 786 milestones without including unrelated changes.

## Done when

Full completion requires a rigorous decision of both finite and infinite
questions under the intended convention, explicit resolution or separate
classification of the repetition ambiguity, reproducible computation for any
finite certificate, two fresh audits of each complete candidate, accurate
artifacts, and a successful commit and push.

## State

### Convention ledger

- Primary reading: \(r,s\geq1\), repetitions allowed, natural density.
- Secondary reading: each factor list is internally distinct. It is strictly
  weaker: \(\{4,8\}\) separates the conventions.
- The infinite set may depend on \(\epsilon\). Upper density is never
  substituted for natural or lower density.

### Complete result: infinite repetition-allowed version

Every repetition-allowed PLR set satisfies
\[
\underline d(A)\leq\frac12.
\]
Thus the requested “for every \(\epsilon>0\)” assertion is false (already for
\(\epsilon\leq1/2\)). The proof uses the exact grading theorem, zeta
probability, a zero-drift compound-Poisson representation, and a winding
number bound on nonzero atoms. Two fresh targeted audits found no error.

### Finite proved facts

1. Exact finite PLR is equivalent to
   \(\operatorname{rank}V_A=\operatorname{rank}[V_A\mid\mathbf1]\).
2. A threshold grading gives
   \[
   |A_N|=(c_*+o(1))N,\quad
   c_*=2-2\rho(1+\sqrt e)-\log(1+\sqrt e)
   =0.828499\ldots .
   \]
3. Every finite repetition-allowed PLR set satisfies the stronger bound
   \[
   N-|A_N|\geq cN/\log N
   \]
   for an absolute \(c>0\), by prime--cofactor overlap and multiplicative
   energy. A fresh audit certified the proof.
4. Earlier independent bounds include
   \(m_N+1\geq N^{0.227092\ldots-o(1)}\) and the smooth-number
   self-consistency inequality.
5. Any finite bad set has a bounded circuit witness; modular certificates
   whose lcm exceeds the explicit determinant bound imply exact PLR.

### Route tournament

1. **Finite uniform anti-concentration / robust prime-divisor model.**
   Product-measure transfer is false for moving prime supports. The strongest
   surviving negative route is a multiscale cofactor-profile lemma combining
   row penalties with cross-band additive relations.
2. **Largest-prime/cofactor modal construction.** Only plausible positive
   route. An exact Bellman identity is proved; the natural globally completed
   single-threshold family cannot beat \(0.828499\ldots\) when its lower
   cutoff is at least \(N^{1/4}\).
3. **Multi-band weighted grading.** The single threshold achieves
   \(0.828499\ldots\). Exhaustive rational/binary/ternary finite grids at
   \(N=100000\) found no improvement; moving \(N^{o(1)}\) bands remain open.
4. **Top-slab/hypergraph deletion for distinct factors.** Unequal-cardinality
   relations have a fractional transversal of total \(O(N/\log N)\), but
   sharp clustered circuits leave a cluster-aware integral-rounding gap.
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

Decide whether an \(N\)-dependent rational completely additive function can
have an exact nonzero level containing \(1-o(1)\) of \([1,N]\). Any positive
answer must delete at least \(cN/\log N\); any negative answer needs a
stronger uniform finite anti-concentration or a proof that complete
additivity cannot realize \(o(\log N)\) scale-color changes. The
distinct-factor variant has a separate cluster-aware transversal bottleneck.
