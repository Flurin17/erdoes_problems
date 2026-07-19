# Status: Erdős #415

## Goal

Produce an Erdős-submission-ready package for the corrected sharp theorem
\[
\log_3M_k=k(\log_3k+\gamma-\mu)+o(k),
\qquad
F(n)=\frac{\log_3n}{\log_6n+\gamma-\mu+o(1)},
\]
where $\mu=\sum_p p^{-1}\log(p/(p-1))$.  This disproves a positive-constant
$\log_3n$ law.  The package must include a dependency-complete readable proof,
reproducible finite computations, an explicitly corresponding Lean theorem
with no `sorry`, `admit`, `sorryAx`, or problem-specific axiom, exact
Lean/mathlib build information and `#print axioms` disclosure, and an AI-use
statement.  Also retain the $k=4$ counterexample to decreasing finite
extremality and the fixed-$k$ frequency theorem/counterexample for the natural
order, but do not let subsidiary claims obscure the formalized main claim.

## Context

- Authoritative input: the `Verbatim statement` in `PROBLEM.md`.
- Unless a convention is explicitly varied, $k,n\ge1$ and $m\ge0$ are
  integers.  The choice $m\ge0$ is natural because the source refers to
  $\phi(1),\ldots,\phi(k)$.  Since $\phi(1)=\phi(2)=1$, the $m=0$ window
  realizes no strict pattern for $k\ge2$; requiring $m\ge1$ gives the same
  $M_k$ for $k\ge2$ and $F(n)$ for $n\ge2$.  Only $k=1$ changes.
- For $\sigma\in S_k$, say that $\sigma$ occurs at $m$ when
  \[
  \phi(m+\sigma(1))<\phi(m+\sigma(2))<\cdots<
  \phi(m+\sigma(k)).
  \]
  Thus $\sigma(1)$ indexes the smallest totient and $\sigma(k)$ the largest.
- A tuple containing equal totients realizes **no** strict permutation.  Tied
  tuples are retained in counts and searches as non-occurrences; they are not
  silently discarded or tie-broken.
- Define
  \[
  M(\sigma)=\min\{m+k:m\ge0\text{ and }\sigma\text{ occurs at }m\},
  \qquad M_k=\max_{\sigma\in S_k}M(\sigma),
  \]
  with value $+\infty$ if the relevant set is empty.  Under the normalization,
  \[
  F(n)=\max\{k:M_k\le n\}.
  \]
- The phrase “any of the $k!$ possible ordering patterns appears” is genuinely
  ambiguous: literally it can mean “at least one,” which is nearly vacuous,
  while the nontrivial reading is “each/every.”  The main analysis uses the
  latter, as requested, without altering the verbatim statement.
- The existential reading measures the longest consecutive block of
  pairwise-distinct totients.  A common-witness reading
  $\exists m\,\forall\sigma$ is impossible for $k\ge2$.
- All logarithms are natural, $c>0$, and asymptotics are as $n\to\infty$.
- The cited “natural ordering” is not a defined strict permutation for any
  $k\ge2$, because $\phi(1)=\phi(2)$.  A tie rule or weak-order formulation is
  required.
- Exact inversion: threshold heredity turns
  \[
  \log_3M_k=k(\log_3k+a+o(1))
  \]
  into $F(n)=\log_3n/(\log_6n+a+o(1))$.
- Existing candidate artifacts are `PROOF.md`, `NOTES.md`, the route files in
  `attempts/`, and the deterministic programs in `computational/`.  There was
  no Lean project or formal proof at the start of this submission-readiness
  run.

## Constraints

- No web search, browser, external solution lookup, erdosproblems.com query, or
  Git-history search.  Use only the named local files and standard mathematical
  knowledge.
- Do not convert computation, heuristics, confidence, or agent agreement into
  proof.  State uncertain remembered theorems with their uncertainty.
- Preserve the source ambiguity, strict inequalities, tied tuples, and every
  quantifier.  Track all estimates uniformly in $k$.
- A prescribed-prime construction must prove CRT compatibility and control the
  effect of every unprescribed prime divisor and of the factors $m+i$.
- A lower bound for $M_k$ must constrain all realizations, not just a selected
  CRT architecture.  Frequency claims may not assume independence of shifted
  totients.
- Preserve unrelated worktree changes.  Only the root agent may commit or push.
- A compiled declaration is not accepted as a formal proof if its transitive
  axioms include `sorryAx` or a custom axiom encoding the desired conclusion.
  Standard Lean axioms must be disclosed rather than hidden.
- Pin the exact Lean/mathlib revision and give commands that work from a clean
  checkout.  Do not claim that formalization covers more of the source problem
  than the formal theorem actually states.

## Deliverables

1. `NOTES.md` containing the normalization, equivalent formulations, inversion,
   and proved lemmas.
2. Separate route drafts under `attempts/` for constructions, obstructions,
   optimization, and frequency analysis.
3. Reproducible programs and concise results under `computational/` for exact
   small-$k$ first occurrences, ties, frequencies, and prime-allocation models.
4. A ranked route ledger and explicit dependency graph in this file, including
   failed routes and exact failure points.
5. `PROOF.md` containing only the strongest coherent self-contained argument,
   clearly labeled complete, conditional, or partial.
6. Coherent mathematical milestones committed and pushed without including
   unrelated user changes.
7. A self-contained Lean project under `lean/`, with a named main theorem,
   exact toolchain/library pins, clean `lake build`, clean source scan for
   `sorry`/`admit`/custom `axiom`, captured `#print axioms` output, a precise
   informal-to-formal correspondence note, and an AI-use disclosure.

## Done when

The submission package is complete only when every $\sigma\in S_k$ is realized below
a uniform proved threshold, a universal matching obstruction determines the
same leading constant, the inverse-threshold argument yields $c$, all parameter
ranges and ties are handled, and a dependency-complete `PROOF.md` survives at
least two fresh adversarial audits.  The decreasing-pattern and frequency
questions require their own rigorous proofs or counterexamples under explicit
definitions.  All computation used as a certificate must be reproducible, and
the Lean main theorem corresponding to the claimed informal result must build
without proof holes or hidden result axioms.  The exact build, source scan, and
axiom-print commands must succeed; at least two fresh agents must audit both
the human proof and the formal correspondence; and the final accurate state
must be committed and pushed to `codex/415`.

## State

Submission-readiness audit in progress.  The repository contains a strong
candidate human proof, but at the start of this run it was not self-contained,
had no Lean project, did not record a Lean/mathlib version or axiom printout,
and described the literal constant question too loosely.  It is therefore not
yet accurate to call the package formally verified or submission-ready.

### Phase-0 normalization (2026-07-18)

1. The adopted nontrivial predicate is
   \[
   \forall\sigma\in S_k\ \exists m=m(\sigma)\ge0:\quad m+k\le n,
   \quad \phi(m+\sigma(1))<\cdots<\phi(m+\sigma(k)).
   \]
   The witness may depend on the pattern.  This is an explicit normalization
   of “any,” not a claim that the English is unambiguous.
2. Literally the source permits $c=0$.  The sharp theorem would therefore
   answer the displayed question “yes, degenerately with $c=0$,” while proving
   that no positive $c$ works.  The final submission must say both.
3. The source does not specify $m\ge0$ versus $m\ge1$.  Only the $k=1$
   boundary changes; every $k\ge2$ result is identical because the $m=0$
   window contains the tie $\phi(1)=\phi(2)$.
4. The decreasing-pattern question is normalized as
   $M((k,k-1,\ldots,1))=M_k$.  The exact facts $M_3=315$,
   $M((4,3,2,1))=826<827=M((3,2,1,4))$ give the stronger cutoff
   counterexample $F(826)=3$: descent has appeared, while another 4-pattern
   has not.
5. “Natural” and “most likely” are undefined without a tie rule and a
   probability model.  The candidate proof treats only stable index
   tie-breaking and aggregate weak-order refinements under limiting natural
   density; it must not claim to settle arbitrary repairs.
6. A faithful Lean target must use `Nat.totient` in the occurrence predicate
   and prove the sharp limit itself.  An abstract inversion theorem or a
   theorem taking the number-theoretic conclusion as a hypothesis is useful
   but is not a formal verification of the main claim.
7. Phase 0 found no local Lean executable, toolchain, mathlib checkout, or
   existing formalization.  The filesystem was full; the authorized log-cache
   deletion did not immediately reclaim its space, apparently because the
   desktop process retained the unlinked database.
8. The small-range scan has a reproducible empty-result reporting bug at
   `--limit 6 --max-k 6`; this does not affect the recorded million-point
   certificate but must be repaired before submission.

### Proved normalization facts

1. Extending a $j$-pattern to a $k$-pattern and truncating an occurrence proves
   $M_j\le M_k-(k-j)$.  Thus finite thresholds strictly increase and
   \[
   F(n)\ge k\Longleftrightarrow M_k\le n,
   \qquad F(n)=k\Longleftrightarrow M_k\le n<M_{k+1}.
   \]
2. Assuming every $M_k$ is finite,
   \[
   F(n)\sim c\log_3n\Longleftrightarrow \log_3M_k\sim k/c.
   \]
3. With $m\ge0$, $M_1=1$, $M((1,2))=3$, and
   $M((2,1))=M_2=6$.  Hence $F(n)=1$ for $1\le n\le5$ and $F(6)=2$.
4. Put $D_k=(k,k-1,\ldots,1)$.  The clean “first missing” formulation is
   $M(D_k)=M_k$ for every $k$ (or eventually).  Once all first occurrences are
   finite, their endpoints are distinct—one endpoint determines one window—so
   a last pattern is automatically unique.
5. Use
   \[
   N_\sigma(x)=\#\{0\le m\le x-k:\sigma\text{ occurs at }m\}.
   \]
   Tied windows count for no pattern.  Conditioning on a tie-free window
   divides every $N_\sigma$ by the same denominator and preserves rankings,
   but finite eventual dominance, natural density, upper density, and
   logarithmic density remain distinct possible meanings of “most likely.”

### Audited main theorem

Let
\[
\mu=\sum_p\frac1p\log\frac p{p-1}.
\]
The full-control CRT construction proves, uniformly in $\sigma\in S_k$,
\[
\log_3M(\sigma)
\le k(\log_3k+\gamma-\mu)+o(k).
\]
The decreasing pattern and an unavoidable early primorial multiple prove the
matching architecture-independent lower bound.  Therefore
\[
\log_3M_k=k(\log_3k+\gamma-\mu)+o(k),
\quad
F(n)=\frac{\log_3n}{\log_6n+\gamma-\mu+o(1)}.
\]
Thus $F(n)/\log_3n\to0$: no positive $c$ exists in the proposed scale (while
the literal degenerate choice $c=0$ hides the sharp answer).

### Subsidiary results

- **Decreasing-first-missing is false.**  Two independent finite totient
  implementations certify
  \[
  M((4,3,2,1))=826<827=M((3,2,1,4)).
  \]
- **Frequencies exist.**  For every fixed strict pattern, $N_\sigma(x)/x$
  has a positive natural density equal to an exact Haar-profinite chamber
  probability.
- **Natural-most-frequent is false under canonical repairs.**  At $k=3$, if
  $q\in(0,1)$ is the odd-prime range probability defined in `PROOF.md`, then
  $d(123)=q/6<1/4-q/12=d(213)$.  Aggregating all natural weak-order refinements
  also loses to a same-shape competitor by $(1-q)/4$.

### Route ranking

The broad Phase-1 wave used 32 distinct assignments; 26 were constructors,
lemma provers, reducers, or experimentalists and 6 were obstruction/falsifier
roles.  Duplicate routes were clustered before retaining the following:

1. `attempts/crt_full_control.md`: sharp uniform construction; survives.
2. `attempts/primorial_obstruction.md`: sharp universal obstruction; survives.
3. `attempts/frequency_profinite.md`: fixed-$k$ density theorem; survives.
4. `computational/verify_k4_counterexample.py`: finite exact certificate;
   survives two independent implementations.
5. `attempts/weaker_and_dead_routes.md`: parity, entropy, divisor-only,
   independence, and prime-tuple routes, with their first failures preserved.

### Proof dependency graph

- **Standard:** PNT $\vartheta(x)\sim x$; Mertens product theorem; CRT;
  Euler divergence of $\sum_p1/p$ and Sperner (frequency part only).
- **Proved locally:** maximal loss occurs at a primorial; mean baseline loss is
  $\mu k+o(k)$; private-prime greedy packing; exact residue compatibility;
  rough-tail and raw-$\phi$ gap bounds; early primorial propagation; large-prime
  uniqueness; threshold inversion; profinite transfer and atomlessness.
- **Finite certificate:** exact first endpoints $826$ and $827$, exhaustively
  checked through the claimed endpoints by two totient algorithms.
- **Open nodes:** none in the mathematical proof.  Only the environment-blocked
  remote push remains in the requested workflow.

### Adversarial audit ledger

- Construction referee found one local cutoff-pricing gap: Mertens had been
  applied after an optional enlargement.  Repaired by taking the cutoff to be
  exactly the last allocated prime; the same referee rechecked and found no
  remaining objection.
- Obstruction/inversion referee checked orientation, primorial propagation,
  all $o(k)$ terms, the $n^k$ conversion, and the $\log_6n$ inversion; no valid
  objection.
- Frequency referee requested an explicit positivity argument.  Added the
  finite private-prime cylinder plus Markov tail proof; its other checks found
  no substantive objection.
- Statement/computation referee reran both programs and found one reporting
  issue: incomplete $k=5,6$ scans were labeled `false` rather than unknown.
  Repaired with a tri-state field; the $k=4$ certificate was independently
  reproduced exactly.
- A fresh post-repair main referee reported the theorem dependency-complete
  under the explicitly stated standard results.

### Computation

`computational/pattern_scan.py` exhaustively scanned all windows through
$10^6$ for $k\le6$ (recorded runtime 11.943987 seconds), with a gcd-definition
cross-check through $500$.  `computational/verify_k4_counterexample.py`
independently checks the decisive finite counterexample through $827$.
