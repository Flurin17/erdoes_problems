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

Phase 0 and the 36-assignment broad search are complete. Both main claims remain open locally. The run has a dependency-complete improved lower theorem, several proved upper reductions, exact counterexamples to major shortcuts, and a route tournament with explicit bottlenecks. A new two-flattening theorem now closes the formerly open comparable canonical two-prime critical band at the target order.

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
- If canonical \(a=d(pq)\) has primes \(p\le q\le Kp\), then all such
  elements in a pair-admissible set total
  \[
  O_K\!\left(n^{3/4}(\log n)^{-3/2}\right).
  \]
  The proof combines the two \(C_4\)-free flattenings \(d--(pq)\) and
  \((d,p)--q\), switching at \(p\asymp n^{1/4}\sqrt{\log n}\). Two fresh
  agents independently audited the collision degeneracies, prime counts,
  small scales, and dyadic endpoint sums.
- Within that sector, the subfamily for which \(P^+(d)>q\) is smaller:
  \[
  O_K\!\left(n^{3/4}(\log n)^{-2}\right).
  \]
  This replaces the false pointwise claim \(P^+(d)=O(p)\); explicit canonical
  examples have \(P^+(d)\asymp p^2\).

### Construction ledger

1. **Proved and independently audited:** the Bellman-optimized reciprocal-annuli construction in PROOF.md gives
   \[
   \liminf_{n\to\infty}
   \frac{F(n)-\pi(n)}
        {n^{3/4}(\log n)^{-3/2}}
   \ge c_0,\qquad
   c_0=\frac{2^{11/4}}{3^{3/4}}=2.951151\ldots .
   \]
   This is the exact optimum among the disjoint interval-incidence components analyzed there, not a global optimum over all semiprime graphs.
2. **Proved precursor:** a single unbalanced factor rectangle gives $4/3^{3/4}$; constant-ratio reciprocal annuli give $2.873958\ldots$. Both are strictly subsumed by item 1.
3. **Open construction bottleneck:** a two-level fractional $C_4$ profile would improve $c_0$ by about $0.091$ and satisfies every aggregate two-path inequality. It is now reduced exactly to packing the block-intersection graph of one asymptotically saturated transversal design into the complement of another, equivalently constructing a typed strong difference family. Both marginal designs exist. Standard affine/projective, subplane, Latin-subsquare, parallel-class, translation/Sidon, and independent-random templates cannot realize the coupling; random alteration has a constant loss, while all tested rank, spectral, pencil, and pair-capacity inequalities retain slack. Abstract nonlinear realizability remains open.

### Warnings and eliminated shortcuts

- Ordinary multiplicative energy is not equivalent to the restricted problem because equations $ab=c^2$ are allowed.
- A raw divisor graph need only exclude $C_4$'s with four distinct labels; ordinary $C_4$-freeness is sufficient but not necessary.
- Adjoining $1$ is not automatically safe: $\{2,3,6\}$ is pair-admissible but $1\cdot6=2\cdot3$.
- Pair injectivity does not imply fixed-$r$ injectivity: $\{1,2,6,7,15,35\}$ is pair-admissible but has a $3$-product collision.
- For semiprime fixed-$r$ models, forbidding only one cycle length is insufficient; all alternating even cycles through length $2r$ must be excluded.
- Elements with $\Omega\ge3$ are not lower order: fixed-kernel families such as $2pq$ can contribute at the full target scale.
- Arbitrary cofactor fibers cannot be compressed to a prime-sized quotient alphabet: coprime doubletons give $\Theta(z^2)$ disjoint quotient spectra.
- Largest-prime incidence girth alone loses multiplicative relations internal to composite cofactors, as the family $uv^2$ demonstrates.

### Route tournament

1. **Bellman semiprime lower construction — strongest closed route.** Complete proof in PROOF.md; remaining question is whether coupled multiscale designs beat it.
2. **Arithmetic colored-kernel upper route — strongest global upper route.** Canonical roughness, very imbalanced ratios, and the far large-prime tail are controlled at the target order. The two-flattening theorem now handles every comparable canonical two-prime factor, including the former large-kernel/small-prime gap. The remaining work is to synthesize the one-prime and at-least-three-prime sectors with the prime ledger and then recover exact, rather than order-only, constants.
3. **Exchange and prime-deficit charging — strong supporting route.** Exact simultaneous-prime blockers and a strict-Hall ledger are proved; they control large-prime tails but leave a genuine missing-prime two-core.
4. **Restricted quotient energy — closed special case, failed globally.** It proves the target-order upper bound for primes plus numbers of $\Omega\le2$, but an explicit primitive-fiber construction falsifies the required arbitrary-cofactor compression.
5. **Fixed-$r$ high-girth route — strongest generalization route.** The exact bipartite semiprime equivalence is proved, and the claimed upper bound is proved for the prime/semiprime model conditional only on a stated standard asymmetric girth theorem. For arbitrary integers, all large-largest-prime fibers reduce to the claimed scale; a smooth-core lemma remains.
6. **Exact computation — implemented and reproduced.** The deterministic
   collision-hypergraph solver computes \(F(n)\) exactly through \(n=45\),
   records extremal witnesses and edge digests, compares two independent edge
   generators through \(n=80\), agrees with exhaustive search through
   \(n=16\), and directly checks fixed \(2\le r\le4\) cases through \(n=11\).
   All 45 edge digests and witnesses were checked, and independent exact
   optimization readback was rerun through \(n=30\).

### Audit record

- Two fresh referees independently audited the partial theorem in PROOF.md.
  One checked all collision classes, projective-plane sizing, prime intervals,
  endpoint costs, and the fixed-\(J\) liminf quantifiers. The other checked
  the Bellman transformation, telescoping tail, optimizer, equality
  recurrence, side orientation, and coefficient. Neither found an unresolved
  error.
- This audit certifies only the displayed liminf lower bound. It does not
  certify a matching upper bound, existence of the limit, or the full
  fixed-\(r\) assertion.

### Current bottleneck

For the pair problem there are now two explicit bottlenecks: (i) decide the finite/asymptotic four-part $C_4$ packing that tests whether coupled semiprime blocks beat $c_0$; and (ii) turn the order-scale upper reductions, now including the complete comparable two-prime sector, into an exact-constant variational bound. For fixed $r$, prove the smooth-core estimate recorded in attempts/fixed_r.md.

### Next assignments

Use the exact solver to test the coupled four-part packing at increasing finite
orders; pursue the equivalent typed difference-family/graph-packing lemma;
synthesize the remaining canonical upper sectors and optimize their constants;
verify the fixed-\(r\) prime/semiprime theorem's asymmetric girth dependency;
and keep PROOF.md explicitly partial until matching global bounds exist.
