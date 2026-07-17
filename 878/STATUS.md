# Status: Erdős #878

## Goal

Resolve every subquestion in the verbatim statement.  The immediate decisive
targets are: (i) an exact finite partition formula for `F(n)` on each prime
support, with the convention about `1` separated explicitly; (ii) independent
dependency-complete arguments for the two almost-all estimates, the extremal
asymptotic, equality counting, and the summatory function `H(x)`.

## Context

The authoritative input is `PROBLEM.md`.  For a positive integer `n>1`, write
`P(n)={p:p|n}` and

`L_p(n)=floor(log n/log p)`, so `p^{L_p(n)} <= n < p^{L_p(n)+1}` and
`f(n)=sum_{p|n} p^{L_p(n)}`.  The exponent of `p` in `n` is irrelevant to this
summand except for deciding membership in `P(n)`.  For `n=1`, the prime support
and the sum are empty, hence `f(1)=0`.

In `F(n)`, the maximizing family is finite, consists of distinct positive
integers at most `n`, has pairwise gcd `1`, and every prime dividing a member
lies in `P(n)`.  There is a genuine source ambiguity: by the usual vacuous
reading, `1` is admissible and belongs to every optimum; under the likely
intended non-unit reading all `a_i>1`.  Both readings will be tracked.  The
number `k` of terms is variable; the empty family has sum `0`.

No earlier local lemmas are assumed at intake.  Files allowed as context are
`PROBLEM.md`, this ledger, and artifacts named here as they are created:
`NOTES.md`, `PROOF.md`, `attempts/`, `computational/`, and `lean/`.

## Constraints

- No web search, browser, erdosproblems.com query, external literature lookup,
  repository-wide solution search, or Git-history solution search.
- “Almost all” means outside a set of natural density zero as `n -> infinity`.
- `A(n) \gg B(n)` means there is an absolute constant `c>0` and an absolute
  threshold `N` such that `A(n)>=cB(n)` on the asserted almost-all set for
  `n>=N`; any weaker dependence must be stated.
- Maxima `max_{n<=x}` are over positive integers `n` (and are empty if `x<1`);
  asymptotic questions concern real `x -> infinity`.  Counts and `H(x)` use
  positive integers `n<x` exactly as written.
- Standard mathematical knowledge may be used from memory, but any uncertain
  theorem statement or hypothesis must be labelled.  Computation and agent
  agreement are not proof.
- The exact hypotheses, uniformity, and constants of any analytic number
  theory input must appear in the dependency graph.
- Only the coordinating root agent uses Git.  Other agents must not run Git
  commands or edit shared synthesis files unless explicitly assigned.

## Deliverables

- Exact fixed-support optimization formula for `F(n)`, including one-prime,
  two-prime, squarefree, smooth, and highly composite support consequences.
- `NOTES.md` containing normalized definitions, equivalent formulations,
  proved lemmas, and exact discontinuities of `p^{L_p(n)}`.
- Separate route drafts in `attempts/` and a dependency graph for each of:
  almost-all `f`, almost-all `F`, extremal `f`, equality `f=F`, and `H(x)`.
- Deterministic scripts and documented finite experiments under
  `computational/`, with commands, ranges, invariants, and interpretation.
- `PROOF.md` containing only the strongest coherent self-contained proved
  result, with conditional and open claims plainly separated.
- A research ledger below recording proved facts, counterexamples, dead routes,
  route ranking, bottlenecks, assignments, and honest completion state.

## Done when

The full run is done only when every quantifier and convention in `PROBLEM.md`
is addressed by dependency-complete proofs/counterexamples; every finite
certificate is reproducible; at least two fresh adversarial referees find no
valid objection to a complete candidate; earlier objections are resolved;
`STATUS.md` and `PROOF.md` do not overclaim; and the final state is committed
and pushed.  A coherent interim milestone requires at least one named lemma
proved, one route rigorously eliminated, or one reproducible computation, plus
an explicit remaining bottleneck.

## Normalization and ambiguities (intake)

1. For every `p|n`, `L_p(n)>=1`; no logarithm is needed for `n=1` because its
   support is empty.
2. `p^{L_p(n)} = n p^{-{log_p n}}`, where `{ }` is fractional part, except at
   exact integral `log_p n`, where the fractional part is `0`; as a function of
   real `y>=1`, it is constant on `[p^j,p^{j+1})` and jumps from `p^{j-1}` to
   `p^j` at `y=p^j`.
3. If `1` is admissible, adjoining it preserves distinctness and coprimality
   and raises every non-unit optimum by `1`.  Thus `F_unit(n)=F_{>1}(n)+1` for
   all `n>=2`, while `F_unit(1)=1` and `F_{>1}(1)=0`.  In particular, under the
   unit-admissible reading `f(n)=F(n)` has no solutions.  This observation is
   elementary but the equality question strongly suggests the author intended
   `a_i>1`; results will state which branch they use.
4. “For all `x`” is ambiguous for nonintegral `0<x<1`; the substantive reading
   is real `x>=1`, equivalently integer cutoffs after applying `floor(x)`.

## Research ledger

### State

Active; partial solution.  Phase 0, the 29-assignment constructive wave, and
the six-route tournament are complete.  Both almost-all assertions are proved
and have passed two fresh adversarial audits each.  The exact optimization,
literal-unit branch, a running-max counterexample, an oscillatory asymptotic
for `H`, and a sharp maximal-order limsup are also proved.  Four substantive
questions remain open locally: the full maximal-order limit, eventual
running-max equality, the nonunit equality-count asymptotic, and the uniform
`H(x)<<x log_4 x` bound.

### Proved facts

- The normalization and unit-admissibility observations above.
- Exact partition formula
  `F_{>1}(n)=max_Pi sum_{B in Pi}M_n(B)` and subset dynamic program.
- `F_{>1}(n)>=max(n,f(n))`, exact one- and two-prime formulas, and the
  all-subsets iff criterion for `F_{>1}(n)=f(n)`.
- Exact finite prime/block identity for `H(x)` after writing `n=pm`.
- `H(x)<<x log_3 x`, hence `f(n)=o(n log_2 n)` outside a density-zero set.
- By a two-band Fourier/sieve/matching construction,
  `F(n)>>n log_2 n` outside a density-zero set.
- Explicit pointwise oscillatory expansion
  `H(x)=M(x)+zeta(2)x/log x+O(x/log^2 x)`, with the full fixed-order
  expansion in `attempts/H.md`.
- Arbitrarily large `x` satisfy `H(x)>>x log_4 x`, so the proposed bound is
  order-sharp if true and no constant-linear pointwise asymptotic exists.
- `max_{n<=x}f(n)<=(1+o(1))x log x/log_2 x`, and the normalized limsup is
  exactly `1` by the averaged prime-power crowding construction.
- `F(210)>=442>383=max_{m<=210}f(m)`, disproving running-max equality for
  all cutoffs.

### Counterexamples / dead routes

- Full-block or pairwise merge tests do not characterize `f=F`; `n=120` and
  `n=3689` give explicit obstructions recorded in `NOTES.md`.
- Treating `1` as admissible makes both equality questions immediately
  negative; any nontrivial equality route must explicitly use `a_i>1`.
- A proposed full maximal-order proof used the Selberg integral
  `J(X,h)<<Xh log^2X` at `h=X^{o(1)}`.  Three independent audits identified
  this as unavailable unconditionally (it is available under RH), so the
  route is retained only as conditional and no full limit is claimed.
- Ordinary Brun--Titchmarsh or a naive large sieve cannot control the
  medium-prime phase intervals in the `H` problem once they become shorter
  than one; the first missing lemma is recorded below.

### Route ranking after tournament

1. **Complete:** almost-all `F`, via logarithmic prime bands, a uniform
   shrinking-target lemma, interval-sieve transference, and bipartite matching.
2. **Complete:** almost-all `f`, via `H(x)<<x log_3 x` and Markov.
3. **Strong partial:** `H`, with an explicit pointwise oscillatory asymptotic,
   an order-sharp subsequence lower bound, and one isolated phase lemma.
4. **Strong partial:** extremal `f`, with the matching upper bound and sharp
   limsup; full uniform lower bound remains open.
5. **Partial:** equality count, with exact all-subsets and `omega<=3`
   classifications but no large-core tail theorem.
6. **Partial:** running maxima, with “all `x`” disproved at `210`; eventual
   equality remains open.

### Current bottleneck

For `H`, prove
`sum_{log_2 x<p<(log x)^2}u_p(x)e^{-u_p(x)}/p << log_4 x`.
For extremal `f`, prove a uniform prime-power crowding lemma at every prescribed
height `T=log x` without an RH-level short-interval input.  For equality
counting, prove a uniform large-core/largest-prime tail theorem.

### Next assignments

Commit and push the audited partial solution.  Subsequent work should assign
agents directly to the three bottleneck lemmas above.
