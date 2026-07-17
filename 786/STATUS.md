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
3. If \(m_N=N-|A_N|\), the Dirichlet argument gives
   \(m_N+1\geq N^{0.227092\ldots-o(1)}\).
4. The active-prime chain/smooth-number lemma strengthens this condition:
   if \(m_N=o(N)\), then necessarily \(m_N=N^{1-o(1)}\).
5. Any finite bad set has a bounded circuit witness; modular certificates
   whose lcm exceeds the explicit determinant bound imply exact PLR.

### Route tournament

1. **Finite uniform anti-concentration / robust prime-divisor model.**
   Highest promise for a negative answer; must turn product-measure
   anti-concentration into a bound for uniform \([1,N]\).
2. **Largest-prime/cofactor modal construction.** Only plausible positive
   route; local greedy choice is rigorously capped at \(1/2\), so any success
   needs globally non-greedy small-prime weights.
3. **Multi-band weighted grading.** The single threshold achieves
   \(0.828499\ldots\); perturbations confined above its threshold do not
   improve it. Broad lower bands remain unresolved.
4. **Top-slab/hypergraph deletion for distinct factors.** Unequal-cardinality
   relations in a top slab must be long, but a sparse transversal bound is
   missing.
5. **Conditioned Euler/divisor-box measures.** Could strengthen the finite
   obstruction if a sufficiently flat multiplicative measure is constructed.

### Dead or sharply limited routes

- Exclusive protected markers have density at most \(1/e\).
- Pure modular certificates provide exactness but no dense common level.
- Naive compactness loses density; naive block unions introduce cross-block
  relations.
- The canonical local modal recursion chooses a nonzero weight at \(2\) and
  is capped at \(1/2\).

### Current bottleneck

Decide whether an \(N\)-dependent rational completely additive function can
have an exact nonzero level containing \(1-o(1)\) of \([1,N]\). Any positive
answer must have exceptional size \(N^{1-o(1)}\); any negative answer needs a
uniform finite anti-concentration mechanism. The distinct-factor variant has
a separate sparse-transversal bottleneck.
