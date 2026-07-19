# Status: Erdős #451

## Goal

Determine the sharp asymptotic growth (including a leading constant if one is
meaningful) of the least integer $n_k>2k$ such that
$\prod_{i=1}^k(n_k-i)$ has no prime divisor $p$ with $k<p<2k$.  The decisive
target is a construction locating an admissible $n\le U(k)$ together with an
obstruction ruling out every $2k<n<L(k)$, where $L(k)$ and $U(k)$ have
matching asymptotic scale.

## Context

The authoritative input is the verbatim statement in `PROBLEM.md`.  Put
$\mathcal P_k=\{p:p\text{ prime},\ k<p<2k\}$ and
$P_k=\prod_{p\in\mathcal P_k}p$ (empty product $1$).  For $p\in\mathcal P_k$,
the interval $[n-k,n-1]$ contains $k$ integers and has endpoint difference
$k-1<p$, hence contains at most one
multiple of $p$.  Therefore
\[
p\nmid\prod_{i=1}^k(n-i)\quad\Longleftrightarrow\quad
n\bmod p\notin\{1,\ldots,k\}.
\]
Thus $n_k$ is the least integer $n>2k$ in the simultaneous residue system
$n\bmod p\in\{0,k+1,\ldots,p-1\}$ for every $p\in\mathcal P_k$.  There are
$p-k$ allowed residues modulo $p$, so the exact density over a full period is
$\prod_{p\in\mathcal P_k}(p-k)/p$; this alone gives no useful localization
below a full period.  The source does not specify that $k$ is a positive
integer; the standard intended reading $k\in\mathbb Z_{\ge1}$ is adopted.
For $k=1$, $\mathcal P_k$ is empty and $n_1=3$.

## Constraints

No web search, browser, external literature lookup, erdosproblems.com query, or
Git-history/repository search for a hidden solution.  Only `PROBLEM.md`, this
ledger, files created during this run, and standard mathematical knowledge may
be used.  The prime interval is open at both endpoints; $n>2k$ is strict; $n$
and $k$ are integers; repeated factors do not affect avoidance.  Remembered
theorems with uncertain hypotheses must be labelled.  Density heuristics and
finite computation are not proofs of an unbounded claim.  Any upper bound must
localize an admissible representative, and any lower bound must cover every
candidate in its stated range.

## Deliverables

`NOTES.md` containing normalized definitions, exact equivalences, proved
lemmas, and calculations; route-specific files in `attempts/`; deterministic
segmented-sieve/modular-jumping code and documented exact small values in
`computational/`; the strongest coherent self-contained result in `PROOF.md`;
and, if feasible, a finite-core check or formalization in `lean/`.  The ledger
must rank surviving routes, preserve exact failure points, display the proof
dependency graph, and state the current bottleneck honestly.

## Done when

Full completion requires a dependency-complete upper and lower estimate of the
same sharp scale for all positive integral $k$ (with small cases and every
endpoint handled), reproducible certificates for finite claims, two fresh
adversarial audits with no unresolved valid objection, accurate `STATUS.md` and
`PROOF.md`, and a committed and pushed final state.  A partial milestone is
checkable only when it proves a named nontrivial lemma or bound, rigorously
eliminates a route, or commits a reproducible exhaustive computation with its
scope proved.

## State

Active, Phase 3.  The sharp asymptotic is open locally.  Phase 0 and the
32-route broad search are complete; five routes survived the tournament.  The
best closed lower-bound node has been independently audited, and lemma closure
is focused on anchored localization for the upper bound.

## Research ledger

- **Proved:** exact residue/CRT-box/covering/binomial equivalences; the audited
  quotient-comb/Brun--Titchmarsh lower bound
  $n_k\ge k^{2\log2-o(1)}$; the independent prime-gap layer bound
  $n_k\gg k^2/\Delta_k$; and the explicit construction
  $n_k\le(k+1)P_k/p_*=(1/2+o(1))P_k=\exp((1+o(1))k)$.
  Exact values through $k=50$ have verified cover certificates and two
  independent recomputations.
- **Counterexamples:** none yet.
- **Route ranking:** (1) anchored Fourier/conductor grouping for the missing
  upper localization; (2) multi-candidate CRT with hereditary joint
  discrepancy; (3) quotient-comb and averaged prime-gap tails (closed lower
  bound, stronger conditional consequences); (4) exact covering frontier and
  prime gaps; (5) modular-jump computation/certificates.
- **Dead or sharply obstructed routes:** density alone, ordinary Jacobsthal,
  canonical LLL, standalone larger sieve, absolute Brun inclusion-exclusion,
  one-state greedy CRT, Minkowski, polynomial-degree/CN, and averaged second
  moment.  Marginal-only CRT beam induction is also false, even for prefixes:
  filtering an almost perfectly balanced prefix by a singleton allowed class
  can concentrate all survivors in $o(r)$ classes modulo a future prime $r$.
- **Dependency graph:** exact residues $\to$ phased CRT/Fourier identity and
  density asymptotic; these feed two open signed count estimates at
  $H_\pm=\exp((2\log2\pm\varepsilon)k/\log k)$; those two estimates would give
  the conjectured logarithmic asymptotic.  The quotient-comb lower node and
  period-scale upper node are closed independently.
- **Current bottleneck:** collective cancellation in the high-conductor
  Fourier tail at the fixed anchor $2k$, equivalently hereditary joint
  (conditional, not marginal) discrepancy for adaptively filtered CRT beams.
- **Newly closed Phase 3 nodes:** all fixed Fourier support sizes are
  $o(H\delta_k)$ for $H=\exp(Ck/\log k)$, with the elementary bound useful
  only through support $O(k/\log^2k)$.  Almost all Fourier $L^2$ energy lies
  at conductors $d>H$, where blockwise Cauchy--Schwarz loses at least the
  spatial factor $\sqrt{d/H}$.  Prefix-specific two-prime discrepancy likewise
  controls only $O(k/\log^2k)$ sequential filters.
- **Next assignments:** attack the two-prime hereditary extension lemma and
  signed conductor blocks; extend exact experiments only to falsify these
  lemmas, not as proof.
