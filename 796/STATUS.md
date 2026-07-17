# Status: Erdős #796

## Goal

Determine whether a constant $c$ exists such that
\[
g_3(n)=\frac{n\log\log n}{\log n}+(c+o(1))\frac n{\log n},
\]
identify the candidate $c$, and prove matching lower and upper bounds with
error $o(n/\log n)$.  The first decisive milestone is a rigorously admissible
construction or structural decomposition whose contribution is evaluated
through the $n/\log n$ scale.

## Context

The authoritative input is the `Verbatim statement` in `PROBLEM.md`.
For $A\subseteq[1,n]$, put
\[
r_A(m)=\bigl|\{\{a,b\}\subseteq A:a<b,\ ab=m\}\bigr|.
\]
Then $g_3(n)$ is the maximum of $|A|$ subject to $r_A(m)\leq2$ for
every positive integer $m$.  Reversing factors is not a new representation,
and squares $a^2$ are excluded.  At intake there are no established lemmas or
approved auxiliary files beyond `PROBLEM.md` and this ledger; `NOTES.md`,
`attempts/`, and `computational/` are to be created in this run.

## Constraints

- No web search, browser, erdosproblems.com query, external literature/solution
  lookup, or Git-history search.
- Use only the explicit local context and standard mathematical knowledge;
  label any background theorem whose exact hypotheses are uncertain.
- Preserve $a_1<a_2$: representations are unordered distinct pairs, two are
  allowed, and only a third representation violates admissibility.
- Numerical evidence, heuristics, and agent agreement are not proofs.
- Do not silently repair or weaken the statement; record ambiguities and all
  failed routes precisely.
- The asymptotic concerns $n\to\infty$ through positive integers, and all
  estimates used for the second term must have uniform error $o(n/\log n)$.
- Preserve unrelated worktree changes.  Only the root agent may commit or push.

## Deliverables

- A normalized collision classification and equivalent graph/hypergraph,
  divisor-incidence, valuation-vector, and energy formulations in `NOTES.md`.
- Reproducible exact small-$n$ computation and construction tests under
  `computational/`, with commands, ranges, invariants, runtime, and interpretation.
- Separate files under `attempts/` for serious lower-bound, upper-bound, and
  stability routes, including exact failure points of rejected mechanisms.
- A ranked route ledger, candidate constants, proved facts, current bottleneck,
  and next assignments in this file after every substantial wave.
- A self-contained `PROOF.md` only when a coherent proved argument exists.
- Coherent milestones committed with messages beginning `796:` and pushed.

## Done when

The full run is done only when a construction is proved to satisfy
$r_A(m)\leq2$ for every $m$ and counted through $n/\log n$, every admissible
$A$ satisfies the matching upper bound with the same constant and
$o(n/\log n)$ error, all representation-overlap and endpoint cases are
covered, every finite certificate is reproducible, `PROOF.md` is
dependency-complete, two fresh adversarial agents find no unresolved error,
and the final state is committed and pushed.  If the full asymptotic remains
open in an intermediate wave, a checkable milestone requires at least one
named lemma proved, one major route rigorously eliminated, or one exact
computation reproduced and committed; this does not count as solving the
problem.

## State

Complete locally under the explicitly stated standard quantitative PNT,
prime-Mertens, and weak multiplication-table theorems.  The main claim is
solved with the exact variational constant
\[
c=B_1+C_*.
\]
Four fresh audits found no unresolved mathematical error after one referee's
signed-bound notation objection was repaired.

## Proved facts

1. Distinct factor-pair representations of one product are disjoint.  Hence a
   violation is exactly a six-element nested configuration
   (x_1y_1=x_2y_2=x_3y_3); there are no overlap cases on fewer vertices.
2. The problem is exactly independence in a 6-uniform equal-product
   hypergraph, or equivalently avoidance of a monochromatic (3K_2) in the
   proper product-coloring of (K_n).  The diagonal-corrected convolution and
   restricted-energy identities are recorded in `NOTES.md`.
3. All primes together with squarefree semiprimes crossing the prime split at
   (sqrt n) form an admissible set of size
   \[
   \frac n{\log n}(\log\log n+1+B_1+o(1)),
   \]
   where (B_1) is the prime Mertens constant.
4. More generally, if (D) is strongly multiplicative Sidon (every integer
   has at most one unordered (D)-factorization, diagonals included), then
   \[
   L_n(D)=(D\cap[1,\sqrt n])\cup
     \{dq\leq n:d\in D,\ d\leq\sqrt n,\ q>\sqrt n\text{ prime}\}
   \]
   is admissible.  This is proved by intrinsically recovering the zero, one,
   or two large-prime factors and allowing at most their two orientations.
5. If (E\subseteq\mathbb N_0) is additive Sidon for unordered sums with
   repetition and (0\in E), then
   (\{1\}\cup\{p^e:p\text{ prime},e\in E\setminus\{0\}\}) is strongly
   multiplicative Sidon.  Thus prime cubes and further compatible powers
   already show that the baseline (1+B_1) cannot be the extremal secondary
   coefficient if the full asymptotic exists.
6. For arbitrary (A), the large-prime fibers
   (B_p=\{d:pd\in A\}), (p>\sqrt n), obey the exact cross constraint
   \[
   \#\{(d,e)\in B_p\times B_q:de=t\}\leq2
   \quad(p\ne q).
   \]
7. The \(\sqrt n\)-smooth portion of every admissible \(A\) is
   \(O(n(\log\log n)^2/\log^2n)=o(n/\log n)\).
8. All large-prime fibers can be made self-compatible by
   \(o(n/\log n)\) total deletions.  Equal-product witnesses are disjoint
   across fibers, and the weak multiplication-table theorem controls the
   last capacity blocks.
9. After repair, the problem is exactly the weighted compatible-profile
   model.  A local \(C_4\)-free factorization bound proves its regularized
   finite optima converge, and the actual prime-stratum weights have the
   same limit.

## Constant and route ranking

For finite \(U,V\), put
\[
\mu_{U,V}(t)=|\{(u,v)\in U\times V:uv=t\}|,
\]
and write \(U\sim V\) when this is at most two for every \(t\).  Define
\[
M_K=\max_{\substack{D_k\subseteq[1,k]\\D_i\sim D_j\ \forall i,j}}
\sum_{k\leq K}\frac{|D_k|}{k(k+1)},\qquad
P_K=\sum_{k\leq K}\frac{\pi(k)}{k(k+1)}.
\]
Then
\[
C_*=\lim_{K\to\infty}(M_K-P_K)
\]
exists and is finite, and the proved answer is
\[
\boxed{c=B_1+C_*}.
\]
The explicit three-profile construction in PROOF.md gives
\[
C_*\geq79/60.
\]

1. **Compatible large-prime profiles (complete).**  Gives both the exact
   lower construction and, after repair/homogenization, the upper model.
2. **Smooth-exception 3-graph route (complete).**  Shows smooth elements
   contribute \(o(n/\log n)\).
3. **Witness-repair route (complete).**  Converts prime-specific weak fibers
   to repeatable compatible profiles at negligible cost.
4. **Prime/semiprime graph route (restricted, retained).**  Explains the
   leading term and baseline \(1+B_1\), but not the true secondary constant.
5. **Raw energy and generic hypergraph routes (demoted).**  Useful identities,
   but they lose the secondary scale.

## Current bottlenecks

No mathematical dependency remains open in the asymptotic proof.  Numerically
evaluating \(C_*\) more sharply is an optional finite optimization problem,
not a prerequisite for the exact variational identification.  Only Git
finalization remains.

## Dead or demoted routes

- The conjecture that extremizers consist only of primes and semiprimes is
  false at the secondary scale: admissible coefficient lifts add
  \(\Theta(n/\log n)\) elements of higher \(\Omega\).
- The guess \(c=1+B_1\) is false; it remains a correct baseline lower bound.
- Ordinary second multiplicative energy is too coarse: admissible complete
  bipartite prime-product families asymptotically saturate its capacity, so no
  fixed energy gap can determine \(c\).
- Replacing all quotient fibers by truncations of one common strong-Sidon set
  is false; exact finite profiles are genuinely nonnested.
- Discarding every non-self-compatible fiber is too expensive.  The
  witness-hitting lemma charges only edit distance.

## Computation and audits

- computational/exact_g3.py proves the displayed exact values through
  $n=30$, independently brute-forced through $n=14$.
- computational/profile_search.py exactly optimizes profiles through
  $K=8$, independently verifies $K\leq5$, directly checks lifted
  multiplicities, and certifies the explicit infinite profile's finite core.
- Fresh smooth, fiber-repair, profile, and global referees audited the proof.
  The only mathematical-writing objection was that (5.7) originally used
  signed $\ll$ notation where only a one-sided bound was true; it now states
  the required one-sided inequality explicitly.  Two final post-repair
  referees found no unresolved error.

## Next actions

Re-run final checks, commit only Problem 796 files with a 796-prefixed
message, and push the Problem 796 branch without touching unrelated worktree
changes.
