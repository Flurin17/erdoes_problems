# Status: Erdős #425

## Goal

For the natural one-parameter normalization of the verbatim statement,
determine whether there is a constant \(c\) for which
\[
F(n)=\pi(n)+(c+o(1))n^{3/4}(\log n)^{-3/2},
\]
and, if so, identify and prove the exact value of \(c\). Independently, for
every fixed integer \(r\ge2\), prove or disprove that every \(A\subseteq[n]\)
whose distinct \(r\)-subsets have pairwise distinct products satisfies
\[
|A|\le \pi(n)+O_r\!\left(n^{(r+1)/(2r)}\right).
\]

The decisive target remains a dependency-complete proof or counterexample for
the pair problem. Until that closes, a run milestone must be a proved
structural reduction, rigorously derived candidate constant, sharpened bound,
solved nontrivial special case, or precise falsification of a major route.

## Context

- Authoritative input: the `Verbatim statement` in `PROBLEM.md`.
- For the pair problem, \([n]=\{1,\dots,n\}\), and
  \(\{a,b\}\mapsto ab\) is required to be injective on unordered subsets of
  two distinct elements.
- The source uses \(A\subseteq\{1,\ldots,N\}\) while naming the function
  \(F(n)\). With unrelated \(N,n\), this does not define a one-variable
  function. The unique natural normalization is \(N=n\), as recorded in
  `NOTES.md`.
- In the generalization, \(r\) is fixed as \(n\to\infty\); factors inside a
  product are distinct elements, all of \(\binom Ar\) is compared, and the
  implicit constant may depend on \(r\).
- `NOTES.md` contains the normalized statement, collision/rectangle,
  valuation, restricted-energy, semiprime-graph, fixed-\(r\) rank, and new
  mixed-rank design lemmas.

## Constraints

- No web search, browser, external literature or solution lookup,
  repository-wide hidden-solution search, Git-history solution search, or
  query to erdosproblems.com.
- Use only permitted local files, new work from this run, and standard
  mathematical knowledge; mark recalled theorems whose exact hypotheses are
  uncertain.
- Computation, confidence, elegance, and agent agreement are not proofs.
  Every asymptotic error and dependence of constants must be justified.
- Treat prime powers, semiprimes, small-prime-factor integers, and rough
  integers explicitly, and exclude every product-collision type.
- Preserve genuinely different upper and lower mechanisms and the exact first
  failure of eliminated routes.
- Only the root agent may commit or push; unrelated user work must be
  preserved.

## Deliverables

- `NOTES.md`: normalized definitions, equivalent formulations, calculations,
  and completely proved supporting lemmas.
- `attempts/`: one distilled file per serious route, including exact
  obstructions for failed routes and the leader's proof dependencies.
- `computational/`: deterministic searches with invariant, command, range,
  runtime, independent checks, summary, and rigorous interpretation.
- `PROOF.md`: only the strongest coherent self-contained proof or
  counterexample draft, explicitly labeled partial until the main theorem
  closes.
- This research ledger after each substantial wave, with route ranking,
  bottlenecks, and next assignments.
- Coherent milestones committed with messages beginning `425:` and pushed,
  without caches, raw transcripts, or unsupported claims.

## Done when

The pair problem is complete only when the \(N/n\) ambiguity and every
quantifier are resolved; matching upper and lower arguments give the same
\(c\) with a genuine uniform \(o(1)\); every collision and endpoint case is
covered; all dependencies and computations are reproducible; at least two
fresh adversarial referees find no unresolved error; `PROOF.md` is
self-contained; and the final state is committed and pushed.

The fixed-\(r\) problem is complete only when the assertion is proved for
every fixed \(r\ge2\), with the correct dependence convention, or a rigorous
counterexample is supplied. Neither full target is currently complete.

## Research ledger

### State

Phase 0 and the 36-assignment broad search are complete. Both main claims
remain open locally. The strongest dependency-complete lower theorem now
strictly beats the formerly optimized disjoint-annulus constant: a binary
mixed-rank construction proves a uniform gain over \(c_0\) and an explicit
subsequence constant greater than \(3\). On the upper side, the
two-flattening theorem closes the comparable canonical two-prime critical
band at the target order, but the global exact-constant synthesis remains
open.

### Proved facts

- The unique coherent one-parameter repair is \(N=n\). Pair injectivity is
  injectivity of \(\binom A2\to\mathbb N\), and the fixed-\(r\) quantifiers
  are \(\forall r\ge2\) fixed, \(\exists C_r,n_0(r)\), \(\forall n\ge n_0(r)\).
- A nontrivial pair collision uses four distinct elements and is exactly a
  multiplicative rectangle \((gx)(hy)=(gy)(hx)\).
- Pair injectivity is equivalent to uniqueness of sums of two distinct
  valuation columns and to equality in the restricted multiplicative-energy
  lower bound.
- Squarefree semiprimes indexed by a simple graph are pair-admissible exactly
  when the graph is \(C_4\)-free. Deleting graph endpoint primes and retaining
  every other prime excludes all prime/semiprime cross-collisions.
- If \(\kappa(A)\) is the least rank of a disjoint equal-product subset
  relation, then
  \[
  P_r(A)\iff \kappa(A)>\min(r,|A|-r).
  \]
  This gives complement duality and every padding threshold.
- In the disjoint-prime bipartite semiprime model, girth greater than \(2r\)
  is sufficient for fixed-\(r\) injectivity: a balanced red-blue trade
  decomposes into an alternating even cycle of length at most \(2r\).
- Pure prime powers contribute only \(O(\sqrt n)\), although their
  cross-layer collisions are not automatically negligible.
- If canonical \(a=d(pq)\) has primes \(p\le q\le Kp\), all such elements in
  a pair-admissible set total
  \[
  O_K\!\left(n^{3/4}(\log n)^{-3/2}\right).
  \]
  The proof combines the flattenings \(d--(pq)\) and \((d,p)--q\), switching
  at \(p\asymp n^{1/4}\sqrt{\log n}\). Two fresh agents audited its
  degeneracies, prime counts, small scales, and dyadic sums.
- In that sector, the subfamily with \(P^+(d)>q\) is smaller:
  \[
  O_K\!\left(n^{3/4}(\log n)^{-2}\right).
  \]
  This replaces the false pointwise claim \(P^+(d)=O(p)\); explicit canonical
  examples have \(P^+(d)\asymp p^2\).
- For every \(q=2^k\), an explicit binary mixed-rank family gives a typed
  \(C_4\)-free graph with
  \[
  |X_1|=|A|q,\quad |X_2|=2|B|q,\quad |Y_1|=q^2,\quad |Y_2|=3q^2,
  \]
  degrees \(q,2q\), and exactly \(q/2\) type-\(Y_1\) neighbors at each
  type-\(X_2\) vertex. Within-type differences are invertible and cross
  restrictions are injective.
- Applying this design to adjacent Bellman levels proves, for some absolute
  \(\eta>0\),
  \[
  \liminf_{n\to\infty}
  \frac{F(n)-\pi(n)}{n^{3/4}(\log n)^{-3/2}}
  \ge \frac{2^{11/4}}{3^{3/4}}+\eta.
  \]
  A finite phase cover from the irrational rotation
  \(-\log_2((\sqrt5-1)/2)\) removes the powers-of-two loss.
- On a scale-matched subsequence the same construction gives
  \[
  \limsup_{n\to\infty}
  \frac{F(n)-\pi(n)}{n^{3/4}(\log n)^{-3/2}}
  \ge c_*=3.0009864793\ldots>3,
  \]
  with the exact radical expression and a rational certificate in `PROOF.md`.
  Thus \(c_0\) is not the global lower constant.

### Construction ledger

1. **Proved and independently audited:** the binary mixed-rank construction
   gives the uniform \(c_0+\eta\) lower bound and exact subsequence constant
   \(c_*>3\).
2. **Proved baseline:** the Bellman reciprocal-annulus construction gives
   \[
   \liminf\frac{F(n)-\pi(n)}{n^{3/4}(\log n)^{-3/2}}
   \ge c_0=\frac{2^{11/4}}{3^{3/4}}=2.951151\ldots .
   \]
   This is the exact optimum among the analyzed disjoint components, not
   among all semiprime graphs.
3. **Proved precursors:** a single unbalanced rectangle gives
   \(4/3^{3/4}\), and constant-ratio annuli give \(2.873958\ldots\).
4. **Open stronger profile:** the fully saturated two-level fractional
   \(C_4\) profile would improve \(c_0\) by about \(0.091\), more than the
   current component. It is reduced exactly to a block-intersection graph
   packing, equivalently a typed strong difference family. Both marginals
   exist. Standard affine/projective, subplane, Latin-subsquare,
   parallel-class, translation/Sidon, and independent-random templates fail
   for exact recorded reasons; nonlinear realizability remains open.

### Warnings and eliminated shortcuts

- Ordinary multiplicative energy is not the restricted problem because
  equations \(ab=c^2\) are allowed.
- A raw divisor graph need exclude only \(C_4\)'s with four distinct labels;
  ordinary \(C_4\)-freeness is sufficient but not necessary.
- Adjoining \(1\) is unsafe in general: \(1\cdot6=2\cdot3\).
- Pair injectivity does not imply fixed-\(r\) injectivity:
  \(\{1,2,6,7,15,35\}\) has a three-product collision.
- For fixed-\(r\) semiprime models, forbidding only one cycle length is
  insufficient; all alternating even cycles through length \(2r\) matter.
- Elements with \(\Omega\ge3\) are not lower order: fixed-kernel families
  such as \(2pq\) contribute at the target scale.
- Arbitrary cofactor fibers cannot be compressed to a prime-sized quotient
  alphabet: coprime doubletons give \(\Theta(z^2)\) disjoint quotient spectra.
- Largest-prime incidence girth loses relations internal to composite
  cofactors, as the family \(uv^2\) demonstrates.

### Route tournament

1. **Mixed-rank semiprime lower route — strongest closed route.** `PROOF.md`
   is dependency-complete for the new lower bounds. Next optimize longer
   mixed windows and compare with the stronger saturated profile.
2. **Arithmetic colored-kernel upper route — strongest global upper route.**
   Canonical roughness, imbalanced ratios, the far large-prime tail, and every
   comparable canonical two-prime factor are controlled at target order.
   Remaining work is the one-prime/at-least-three-prime synthesis and exact
   rather than order-only constants.
3. **Exchange and prime-deficit charging — supporting upper route.** Exact
   simultaneous-prime blockers and a strict-Hall ledger control large-prime
   tails but leave a missing-prime two-core.
4. **Restricted quotient energy — closed special case, failed globally.** It
   proves the target upper order for primes plus \(\Omega\le2\), but a
   primitive-fiber construction falsifies arbitrary-cofactor compression.
5. **Fixed-\(r\) high-girth route — strongest generalization route.** The
   prime/semiprime model is reduced to a stated asymmetric girth theorem; for
   arbitrary integers the remaining obligation is a smooth-core lemma.
6. **Exact computation — implemented and reproduced.** The collision
   hypergraph solver computes \(F(n)\) exactly through \(45\), cross-checks
   independent edge generators through \(80\), agrees with exhaustive search
   through \(16\), and checks fixed \(2\le r\le4\) through \(11\).

### Audit record

- Two fresh referees audited the baseline theorem: one checked collision
  classes, projective-plane sizing, prime intervals, endpoints, and fixed-\(J\)
  quantifiers; the other checked the Bellman telescoping, optimizer,
  recurrence, orientation, and coefficient.
- Two further fresh audits checked the mixed-rank advance. One verified every
  finite-field map, affine-graph intersection, part count, degree split,
  endpoint allocation, and collision reduction. The other independently
  checked the limiting ratio, irrational-phase cover, one-sided power-of-two
  slack, PNT uniformity, and cover/truncation order. Neither found an
  unresolved objection.
- `PROOF.md` contains an exact rational certificate for \(c_*>3\), so the
  decimal is not being used as evidence.
- These audits certify only the displayed lower results, not a matching upper
  bound, existence of the limit, or the full fixed-\(r\) assertion.

### Current bottleneck

For the pair problem: (i) optimize the proved mixed-rank components, or
realize/refute the stronger saturated four-part profile, to identify a
credible sharp lower constant; and (ii) turn the order-scale upper reductions
into an exact-constant variational bound covering the one-prime and
at-least-three-prime sectors. For fixed \(r\), prove the smooth-core estimate
in `attempts/fixed_r.md`.

### Next assignments

Optimize the binary mixed-rank construction over longer Bellman windows;
continue the typed difference-family route for the stronger profile;
synthesize remaining canonical upper sectors with explicit constants; prove
the fixed-\(r\) smooth-core lemma; and keep `PROOF.md` explicitly partial
until matching global bounds exist.
