# Status: Erdős #415

## Goal

Under the strict every-pattern normalization below, determine a constant $c$ and
prove
\[
F(n)=(c+o(1))\log\log\log n.
\]
Equivalently, obtain matching uniform estimates for the worst first-occurrence
threshold $M_k$.  Also determine, without conflating the questions, whether the
decreasing permutation is the first missing pattern and whether the natural
ordering of $\phi(1),\ldots,\phi(k)$ maximizes a precisely defined frequency.

The immediate decisive target is a quantitative construction realizing every
prescribed $\sigma\in S_k$, together with a universal obstruction of matching
leading constant for the hardest $\sigma$.

## Context

- Authoritative input: the `Verbatim statement` in `PROBLEM.md`.  No previously
  proved local lemma has yet been imported.
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
- Exact inversion target: $F(n)=(c+o(1))\log_3 n$ corresponds (subject to the
  usual inverse-threshold bracketing, to be proved) to
  \[
  \log_3 M_k=(1/c+o(1))k,
  \quad\text{equivalently}\quad
  \log\log M_k=\exp((1/c+o(1))k),
  \]
  where $\log_3=\log\log\log$.

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

## Done when

The main question is complete only when every $\sigma\in S_k$ is realized below
a uniform proved threshold, a universal matching obstruction determines the
same leading constant, the inverse-threshold argument yields $c$, all parameter
ranges and ties are handled, and a dependency-complete `PROOF.md` survives at
least two fresh adversarial audits.  The decreasing-pattern and frequency
questions require their own rigorous proofs or counterexamples under explicit
definitions.  All computation used as a certificate must be reproducible, and
the final accurate state must be committed and pushed.

## State

Phase-0 normalization completed.  Main and subsidiary claims remain open
locally.  No candidate constant is yet claimed.

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
