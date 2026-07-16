# Status: Erdős #425

## Goal

For the natural one-parameter normalization of the verbatim statement, determine whether there is a constant $c$ for which
\[
F(n)=\pi(n)+(c+o(1))n^{3/4}(\log n)^{-3/2},
\]
and, if so, identify and prove the exact value of $c$. Independently, for every fixed integer $r\ge 2$, prove or disprove that every $A\subseteq[n]$ whose distinct $r$-subsets have pairwise distinct products satisfies
\[
|A|\le \pi(n)+O_r\!\left(n^{(r+1)/(2r)}\right).
\]

The decisive target of this run is a dependency-complete proof/counterexample for the pair problem; until that closes, a run milestone must instead be a proved structural reduction, a rigorously derived candidate constant, a sharpened bound, a solved nontrivial special case, or a precise falsification of a major route.

## Context

- Authoritative input: the `Verbatim statement` in `PROBLEM.md`.
- For the pair problem, $[n]=\{1,\dots,n\}$ and the condition is that $\{a,b\}\mapsto ab$ is injective on the set $\binom A2$ of unordered subsets with two **distinct** elements.
- The displayed source definition uses $A\subseteq\{1,\ldots,N\}$ while naming the extremal function $F(n)$. Taken literally with unrelated $N$ and $n$, it does not define a one-variable function. The working normalization is therefore $N=n$; the ill-posed literal reading and this justification will be recorded explicitly in `NOTES.md`.
- For the generalization, $r$ is fixed (with asymptotics as $n\to\infty$), elements inside each product are distinct, and the product map on all of $\binom Ar$ is required to be injective. The implicit constant is allowed to depend on $r$.
- `NOTES.md` now contains the normalized statement and the first accepted exact lemmas: four-distinct collision/rectangle equivalences, restricted-energy and valuation formulations, the semiprime $C_4$ model, and the fixed-$r$ collision-rank criterion.

## Constraints

- No web search, browsers, external literature/solution lookup, repository-wide hidden-solution search, Git-history solution search, or query to erdosproblems.com.
- Use only the explicitly permitted local files, new work produced in this run, and standard mathematical knowledge; mark any recalled theorem whose exact hypotheses are uncertain.
- Do not infer a proof from computation, agent agreement, elegance, or confidence. Every asymptotic error and dependence of constants must be justified.
- Treat prime powers, semiprimes, small-prime-factor integers, and rough integers explicitly; exclude every type of product collision in constructions.
- Keep genuinely different upper- and lower-bound mechanisms independent until each has precise lemmas. Preserve failed routes and their first invalid inference.
- Only the root agent may run Git commands, commit, or push; unrelated user work must be preserved.

## Deliverables

- `NOTES.md`: normalized definitions and quantifiers, boundary cases, equivalent graph/hypergraph, valuation-vector, energy, and dyadic formulations, plus completely proved supporting lemmas.
- `attempts/`: one distilled file per serious route, including exact obstructions for failed routes and a proof-dependency graph for the leader.
- `computational/`: deterministic exact/heuristic searches with invariant, command, range, runtime, independent small checks, output summary, and rigorous interpretation.
- `PROOF.md`: only the strongest coherent, self-contained proof/counterexample draft once one exists; no brainstorming.
- A research ledger here after each substantial wave, ranking routes and naming the current bottleneck and next assignments.
- Coherent milestones committed with messages beginning `425:` and pushed, without committing caches, raw transcripts, or unsupported claims.

## Done when

The pair problem is complete only when the $N/n$ ambiguity and every quantifier are resolved; matching upper and lower arguments give the same $c$ with a genuine uniform $o(1)$; every collision and endpoint case is covered; all invoked theorems and computations are dependency-complete/reproducible; at least two fresh adversarial referees find no unresolved error; `PROOF.md` is self-contained; and the final state is committed and pushed.

The fixed-$r$ problem is complete only when the assertion is proved for every fixed $r\ge2$ with explicit $r$-dependence conventions, or a rigorous counterexample is supplied. If neither full target closes in this run, completion requires at least one substantial milestone named in the Goal, accurately recorded and committed.

## Research ledger

### State

Phase 0 normalization is complete. Both main claims remain open locally, but the run now has exact structural reductions and a rigorously checkable semiprime construction mechanism. A multiscale lower construction with a substantially larger provisional constant is under independent audit.

### Proved facts

- The unique coherent one-parameter repair of the source is $N=n$; pair injectivity is injectivity of $\binom A2\to\mathbb N$, and the fixed-$r$ statement has quantifiers $\forall r\ge2$ fixed, $\exists C_r,n_0(r)$, $\forall n\ge n_0(r)$.
- A nontrivial pair collision necessarily uses four distinct elements and is exactly a multiplicative rectangle $(gx)(hy)=(gy)(hx)$.
- Pair injectivity is equivalent to uniqueness of sums of two distinct valuation columns and to equality in the restricted multiplicative-energy lower bound.
- Squarefree semiprimes indexed by a simple graph form a pair-admissible set exactly when the graph is $C_4$-free. If graph endpoint primes are deleted and all other primes retained, disjoint endpoint classes eliminate all prime/semiprime cross-collisions.
- For $m=|A|$, if $\kappa(A)$ is the least rank of a disjoint equal-product subset relation, then
  \[
  P_r(A)\iff \kappa(A)>\min(r,m-r).
  \]
  This proves complement duality, all padding thresholds, and the necessity of treating $r$ as fixed.
- In the disjoint-prime bipartite semiprime model, girth greater than $2r$ is sufficient for fixed-$r$ injectivity: after common factors/edges cancel, any balanced red-blue trade decomposes into an alternating even cycle of length at most $2r$.
- Prime powers contribute only $O(\sqrt n)=o(n^{3/4}(\log n)^{-3/2})$ by count, although their cross-layer collisions are not negligible automatically.

### Construction ledger

1. **Accepted mechanism:** a $C_4$-free graph on the primes at most $\sqrt n$ gives the familiar scale and the rigorous lower coefficient $\sqrt2$, using the standard asymptotic $\operatorname{ex}(m,C_4)=(1/2+o(1))m^{3/2}$.
2. **Under audit:** a single unbalanced factor rectangle optimizes at $t=3^{-1/2}$ and gives coefficient $4/3^{3/4}\approx1.754765$ via a restricted projective-plane incidence graph.
3. **Under audit:** disjoint reciprocal prime annuli and independent incidence components give the provisional coefficient
   \[
   C(\rho)=2\sqrt2\,(1-\rho^{-1})^{3/2}\rho^{-1/4}(1-\rho^{-1/2})^{-1},
   \]
   maximized near $\rho=7-2\sqrt6$ with value about $2.874$. Uniform PNT, finite-field sizing, truncation, and the variable-ratio global optimization still require proof-level checking.

### Warnings and eliminated shortcuts

- Ordinary multiplicative energy is not equivalent to the restricted problem because equations $ab=c^2$ are allowed.
- A raw divisor graph need only exclude $C_4$'s with four distinct labels; ordinary $C_4$-freeness is sufficient but not necessary.
- Adjoining $1$ is not automatically safe: $\{2,3,6\}$ is pair-admissible but $1\cdot6=2\cdot3$.
- Pair injectivity does not imply fixed-$r$ injectivity: $\{1,2,6,7,15,35\}$ is pair-admissible but has a $3$-product collision.
- For semiprime fixed-$r$ models, forbidding only one cycle length is insufficient; all alternating even cycles through length $2r$ must be excluded.

### Current bottleneck

The pair problem's first bottleneck is to determine the optimal weighted $C_4$-free semiprime construction under $pq\le n$ (including compatible multiscale blocks) and then prove that non-semiprime layers cannot improve its leading coefficient. The fixed-$r$ bottleneck is an arbitrary-integer reduction matching the high-girth semiprime exponent.

### Next assignments

Launch the mandated broad constructive search across independent lower-bound architectures, arithmetic upper reductions, weighted graph optimization, energy/valuation methods, exact computation, and fixed-$r$ hypergraph routes. Then cluster only mechanisms with a proved lemma or a precise falsification test.
