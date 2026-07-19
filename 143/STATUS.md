# Status: Erdős #143

## Goal

Decide, for every countably infinite real set $A\subset(1,\infty)$ satisfying
\[
  (\forall x,y\in A)(x\ne y)(\forall k\in\mathbb Z_{\ge1})\quad |kx-y|\ge1,
\]
whether each of the following necessarily holds, keeping the two targets logically separate:
\[
  \sum_{x\in A}\frac1{x\log x}<\infty,
  \qquad
  H_A(n):=\sum_{\substack{x\in A\\x<n}}\frac1x=o(\log n).
\]
The decisive target is a dependency-complete proof of both implications or an explicit counterexample to either one; an intermediate target is a sharp weighted packing estimate that settles at least one.

## Context

- Authoritative input: `PROBLEM.md`, especially its Verbatim statement. No other problem files contained established lemmas at intake.
- The pair quantifier is ordered. Hence for every distinct $x,y\in A$, both $|kx-y|\ge1$ and $|ky-x|\ge1$ hold for every integer $k\ge1$.
- The elements are real, not assumed integral or discrete a priori; $k$ may depend on the ordered pair.
- Taking $k=1$ gives $|x-y|\ge1$. Consequently $A$ is locally finite: every bounded interval contains finitely many points. Thus all bounded partial sums are finite and every nonnegative series over $A$ is enumeration-independent.
- For an ordered pair with $y>x$, the reverse orientation is automatic for $k\ge1$ except possibly $k=1$, while the forward orientation excludes $y$ from every open unit neighborhood $(kx-1,kx+1)$.
- The two questions are not formally identical. Their exact logical relationship is part of the run and will be proved with all endpoint/local-finiteness conditions stated.

## Constraints

- No web search, browser, search engine, social media, erdosproblems.com query, external literature lookup, or Git-history solution search.
- Use only `PROBLEM.md`, this ledger, files explicitly named here as they are created, and standard mathematical knowledge. Any remembered theorem with uncertain hypotheses must be labeled.
- Do not replace real $A$ by integers, assume a fixed $k$, infer a theorem from computation, or weaken strict/non-strict endpoints.
- Treat countability, local finiteness, $x\downarrow1$, ordered orientations, and uniformity of all asymptotic constants explicitly.
- Preserve failed routes with their first invalid inference. Computation must be reproducible and is evidence only unless it exhausts a rigorously finite reduction.
- Only the coordinating root agent may commit or push; subagents may edit only their assigned non-overlapping route files and must not run Git commands.

## Deliverables

- `NOTES.md`: normalized quantifiers, equivalent ratio/logarithmic/interval formulations, boundary cases, and proved lemmas.
- `attempts/`: separate route drafts for the surviving multiplicative-graph, weighted-packing, logarithmic-coordinate, constructive/counterexample, and finite-extremal approaches.
- `computational/`: deterministic finite-model code, assertions, reproduction commands, range/runtime/output interpretation if computation is used.
- `PROOF.md`: only the strongest coherent self-contained argument, clearly labeled complete, conditional, or partial.
- This ledger after each wave: proved facts, counterexamples, ranked routes, exact dead ends, bottleneck, assignments, and honest solution status.
- Coherent commits with messages beginning `143`, pushed when repository/branch state permits.

## Done when

Full local solution: every quantifier and case of the Verbatim statement is handled by a dependency-complete proof or explicit verified counterexample; computations are reproducible; two fresh adversarial referees find no valid unresolved objection; `STATUS.md` and `PROOF.md` do not overclaim; and the result is committed and pushed.

Acceptable substantial partial milestone if a full solution is not yet closed in this run: at least one named structural/weighted lemma is proved, at least one genuinely plausible route is either advanced to a precise open bottleneck or rigorously eliminated, all computational evidence is reproducible, and the milestone is committed and pushed without claiming the main problem solved.

## Research ledger (2026-07-17)

### Completed waves

- **Phase 0:** five independent normalizers checked quantifiers, endpoints,
  equivalent formulations, targets, and trivial ranges.
- **Phase 1:** twenty-nine substantively distinct assignments covered weighted
  packing, dyadic charging, graph/energy/Fourier methods, primitive analogies,
  probabilistic and deterministic constructions, finite extremals, rational
  skeletons, and targeted counterexample searches. More than 70% were
  constructors, lemma-provers, reducers, or experimentalists.
- **Phase 2:** six route teams synthesized non-overlapping drafts under
  `attempts/`: rational/primitive, resonance/depletion, torus/log-comb,
  reciprocal-block construction, tube charging, and finite-grid/skeleton
  computation. Earlier prime-layer drafts are retained as eliminated
  subroutes rather than raw transcripts.

### Proved facts

- Ordered pairs reduce exactly to multiplying the smaller member. Every
  infinite admissible $A$ is $1$-separated, locally finite, automatically
  countable, unbounded, and contained in $[2,\infty)$.
- The exact safe-gap condition is
  $\{y/x\}\in[1/x,1-1/x]$ for $x<y$. Open forbidden endpoints, strict cutoff
  $x<n$, and pair-dependent multipliers have all been retained.
- Convergence of $\sum1/(x\log x)$ implies
  $H_A(n)=o(\log n)$. The converse is false for general $1$-separated sets,
  so the first requested assertion is analytically stronger.
- **Common-lattice theorem:** if $A\subset c\mathbb N$ for one $c>0$, then
  both conclusions hold. `PROOF.md` contains a self-contained primitive-set
  proof, including the finite Euler-product estimate.
- **Finite rationalization:** every finite admissible real configuration can
  be approximated by an admissible common-denominator configuration
  $\{n_i/Q\}$ with $|kn_i-n_j|\ge Q$. Hence a uniform $Q$-thick weighted
  estimate would settle the general first assertion.
- **Fixed-prefix torus theorem:** logarithmic upper density is at most the
  safe-box Haar measure on the actual orbit-closure torus. This proves the
  second conclusion when the reciprocal frequencies have unbounded
  independent harmonic mass (in particular, under full
  $\mathbb Q$-independence).
- **Exact finite blocks:** reciprocal blocks
  $\{T/j:M\le j<2M\}$ are admissible at the sharp scale
  $T=(2M-2)(2M-1)$ and have order-one harmonic mass. Exact cross-block
  determinant and one-anchor dilution bounds are proved.
- **Resonance lemmas:** determinant rigidity below the product scale, an exact
  rational-ray overlap formula, prime-thinned local depletion, primitive
  pointwise multiplier labels, and fractional Hall equivalence are proved.

### Counterexamples to proposed intermediate lemmas

- A single near-dyadic block can have linear occupancy, so no one-shell
  $o(T)$ bound is possible.
- Common-center sets $\{T/p\}$ give arbitrarily large tube multiplicity and
  arbitrarily large prime-reciprocal weighted overlap, even inside one
  infinite admissible primitive integer set. Bounded overlap, naive
  independence, and termwise variance are false.
- Normalized squarefree divisor cubes refute a universal
  $m\,\mathrm{polylog}(m)$ aggregate resonance bound. This uses standard PNT
  asymptotics only for the quantitative growth statement and does not yield a
  counterexample to Problem 143 because the required dilation may be huge.
- A pointwise depletion recurrence depending only on cumulative earlier
  harmonic mass is false: highly resonant primitive prefixes can be followed
  by a dense admissible residue block at a selected scale.
- Generic/transcendental block insertion self-thins at the product-density
  rate and gives convergent target weight; random independent alteration and
  ordinary local-lemma schemes meet the same logarithmic hazard.
- A rational commensurability class need not lie in one fixed $c\mathbb N$;
  raywise primitive estimates therefore do not sum to the real theorem.

### Route ranking

1. **Uniform $Q$-thick packing / carrier-conditioned tube union (highest):**
   exact finite reduction and exact computation exist; the missing estimate
   must exploit thick gaps without assuming bounded overlap.
2. **Multiscale resonance novelty:** determinant and prime-thinning lemmas are
   proved; the missing step is a denominator-and-scale weighted novelty
   inequality that survives gcd logarithms and divisor cubes.
3. **Thinned reciprocal-block counterexample:** isolated blocks have the
   correct divergent weight; the missing step is controlled-scale
   concatenation after all old cross constraints.
4. **Fixed-prefix torus/carrier decomposition:** complete in independent and
   coercive finite-rank cases; missing uniform discrepancy and relative
   carrier depletion prevent the general theorem.
5. **Single-chain, naive random, raw energy, and ordinary valuation-code
   routes:** eliminated at their first exact obstruction and retained only as
   supporting lemmas/falsification tests.

### Computation

`computational/discrete_skeleton_exact.py` is a deterministic exact
maximum-weight-independent-set solver for the $Q$-grid conflict graph. It
asserts the modular criterion against direct multiplier enumeration, uses
rational arithmetic, rechecks invariants, and brute-forces small graphs.
`computational/README.md` records the reproduction command, parameter range,
runtime, exact output summary, and the warning that finite agreement is not a
proof.

### Current status and bottleneck

- **Main claim:** open locally; neither a dependency-complete proof nor a
  divergent admissible construction has been obtained.
- **Strongest coherent result:** the fixed-lattice theorem plus the finite
  rationalization reduction in `PROOF.md`.
- **Current bottleneck:** prove or refute a carrier-conditioned, multiscale
  weighted packing estimate. One exact sufficient formulation is the uniform
  $Q$-thick estimate
  \[
  \sum_{n\in S}\frac{Q}{n\log(n/Q)}\le C_a
  \quad\bigl(|kn-m|\ge Q,\ n\ge aQ\bigr),
  \]
  uniform over finite $S$ and $Q$. A failed uniform finite estimate would not
  alone refute the original infinite assertion; extremizers would still need
  compatible concatenation.
- **Next assignments:** optimize the exact finite $Q$-grid model to identify a
  stable dual certificate or a drifting block family; on the proof side,
  seek a pruned rough-multiple/tube allocation satisfying the Hall inequalities;
  on the construction side, run the exact reciprocal-block breakpoint sweep
  and prove the observed survival law.

### Ambiguities retained

“Does this imply that $A$ is sparse? In particular” poses two separate
explicit questions; no connective or equivalence is asserted. The limit in
$n$ is equivalent along real or integer cutoffs by monotonicity, but the
verbatim strict cutoff $x<n$ is used throughout.

### Second focused wave (2026-07-18)

#### Proved refinements

- The uniform $Q$-thick estimate remains open.
- For the target weight $1/(x\log x)$, continuum prime optimality is proved
  through cutoff $10$; this is not merely a finite-grid computation.
- For $Q=2$, the admissible set $\{7/2,5,6,8,9\}$ refutes crystallization for
  arbitrary decreasing weights, but it does not refute crystallization for
  the target weight.
- Far-side floor/ceiling rounding extracts a primitive subset carrying an
  $\Omega(1/\log X)$ fraction of the target weight.
- The exact static capacity of a multiplier-indexed tube family equals the
  divisibility width of the multiplier set.
- A primitive set can place $\gg1/R$ harmonic mass in each of $R$ arbitrarily
  widely separated shells. This eliminates fixed-arity support-only
  obstructions, not all finite-shell quantitative inequalities.
- An explicit admissible three-point family has no primitive floor/ceiling
  labeling. Its cheapest repair lies at quartic scale and has summable target
  weight across ordinary repetitions.

#### Failed routes

- Crystallization cannot be asserted for arbitrary decreasing objectives.
- Fixed endpoint rounding can be globally inconsistent, and the surviving
  far-side rounding argument loses a logarithmic factor.
- Static tube-chain, prime-filter, rough-multiplier, and separable LP
  estimates that use only one target stop at divisibility width.
- Fixed-arity shell support/zero-pattern obstructions cannot supply the
  required global packing control.

#### Computation

The exact harmonic and dyadic-log computations for
$Q\in\{1,2,3,4\}$ at $X\in\{10,14\}$ and for
$Q\in\{2,4,6,8\}$ at $X=18$, including a separately optimized
forced-off-lattice comparison, remain strictly optimized on $Q\mathbb N$.
The reproduction commands are recorded in `computational/README.md` and are:

```sh
python3 143/computational/qthick_growth.py \
  --q-values 1,2,3,4 --x-values 10,14 \
  --objectives both --dp-limit 32 --compact

python3 143/computational/qthick_growth.py \
  --q-values 2,4,6,8 --x-values 18 \
  --objectives both --dp-limit 32 --compact
```

These exact finite surrogate computations do not evaluate the transcendental
target weight and are not a proof of the uniform estimate.

#### Sharpened bottleneck

Prove a mass-sensitive cumulative carrier-conditioned inequality, or prove a
bounded-weight deletion lemma strong enough to permit primitive endpoint
rounding without the logarithmic loss. The three-point obstruction shows that
such a lemma must charge complete implication cycles rather than pairwise
conflicts. The main claim remains open.

### Third focused wave (2026-07-18)

#### Proved refinements

- **Quotient-rough fiber-packet lemma:** the carrier/fiber products attached
  to all members of a finite $Q$-admissible set are pairwise disjoint, with
  carrier densities of the exact target order $1/(b\log b)$.
- **Weighted pseudoforest deletion theorem:** for the endpoint clause
  multigraph, a satisfiability deletion costs at most its scale-integrated
  bicircular excess $\Xi_f$. Together with bounded label multiplicity, this
  gives $\sum_F f\le\Xi_f(G_F)+4C_{\rm prim}$.
- Adjacent rounding need not be injective: every label has multiplicity at
  most two, with total real weight at most four times the integer-label
  weight. Equality collisions should therefore not be treated as essential
  clauses.
- A strict-divisibility seven-point contradiction exists in $[t,7t]$, and
  linearly many disjoint copies pack into one admissible shell.
- A simpler mixed integer/half-integer block proves that the optimal endpoint
  repair cost in one shell can be $\Theta(1/\log N)$ even without an
  injectivity requirement.

#### Eliminated strengthenings

- Minimal contradictory endpoint cycles do not force quadratic or even
  superlinear scale growth. Only the local two-clause-on-one-pair lemma has a
  quadratic jump.
- Cardinal degree, arboricity, and degeneracy of endpoint conflict graphs are
  unbounded; only scale-weighted excess remains plausible.
- A finite family of affine floor grids cannot give constant primitive
  retention. Divisibility-tree configurations make every fixed grid retain
  an arbitrarily small fraction, although their carrier scale is too large
  to refute the target theorem.
- In the stricter half-integer model where rounded labels must be injective,
  bounded-window satisfiability has the sharp threshold $C=3$: all ceilings
  work in $[N,3N]$, whereas explicit admissible contradictory families occur
  in every sufficiently large $[N,CN]$ for $C>3$. Their contradiction uses
  equality clauses, so it does not survive the bounded-multiplicity collapse.
- No universal $z$-only integrable envelope can close the fiber-packet proof;
  dense single shells saturate its pointwise bound at disjoint logarithmic
  depths.

#### Current route ranking and bottleneck

1. **Periodic packet Hall inequality (highest):** prove or refute
   \[
   d\left(\bigcup_{n\in T}R_n\right)
   \ge\kappa_a\sum_{n\in T}d(R_n)
   \]
   for quotient-rough packets inside every $Q$-admissible set. This directly
   implies the uniform $Q$-thick estimate.
2. **Scale-weighted clause excess:** prove $\Xi_f(G_F)=O(1)$, or the related
   star-capped common-shift hazard bound. Both vanish on the known integer
   optimizers and reciprocal blocks, but incur the sharp $1/\log N$ cost on
   two-scale examples.
3. **Critical-shell concatenation:** construct cross-admissible repaired-core
   blocks at scales $R_j\asymp e^j$, which would give a divergent target sum,
   or prove the carrier depletion that prevents such concatenation.
4. **Continuum dilation:** finite fixed grids fail, but it remains open whether
   some dilation $\lambda\in[1,2]$ always has a primitive rounded subset of
   constant target-weight proportion.

The main claim remains open. The common bottleneck is now sharper: control
the cumulative recurrence of shell-order $1/\log N$ obstructions across one
admissible multiscale configuration. Local cycle growth and local packet
disjointness are both insufficient.
