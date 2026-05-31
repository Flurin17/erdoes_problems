# Erdos Problem 82 Notes

## Problem

For an integer `n`, let `F(n)` be the largest integer such that every graph on
`n` vertices contains a regular induced subgraph on at least `F(n)` vertices.

Equivalently, let `G(k)` be the least integer `m` such that every graph on `m`
vertices contains a regular induced subgraph on at least `k` vertices.  The
target statement is

```text
F(n) / log n -> infinity,
equivalently G(k) <= 2^{o(k)}.
```

All graphs are finite and simple.  An induced subgraph on vertex set `S` is
regular if all vertices of `G[S]` have the same degree inside `S`.

## Known Results To Reconstruct

- Ramsey's theorem gives `F(n) >= c log n` by forcing either a clique or an
  independent set.
- Bollobas observed an upper construction with `F(n) << n^{1/2+o(1)}`;
  Dyson--McKay later improved the construction to `F(n) << sqrt(n)`.
- Fajtlowicz, McColgan, Reid, and Staton computed small Ramsey-type values;
  the modern notation is `G(k)` for "at least k" and `g(k)` for "exactly k".
- Alon, Krivelevich, and Sudakov studied `f(n,c)`, the largest guaranteed
  order of an induced `c`-nearly-regular subgraph, where `Delta <= c delta`.
  Their bounds do not settle the case `c=1`.
- Dyson and McKay (2026) compute exact small values up to `k=5` and improve
  lower bounds for `k=6,7`; this is finite evidence, not an asymptotic proof.
- The current problem page still marks the conjecture as open.

## Failed / Risky Approaches

### Local-minimum degree variance

Idea: choose a `k`-set `S` minimizing the variance of the induced degrees and
try to show that, unless `G[S]` is regular, many outside vertices can be
swapped in to reduce the variance.

Obstruction: for a fixed nonregular `S`, a vertex outside `S` has an arbitrary
binary profile in `{0,1}^S`.  The local-improvement inequalities appear to cut
out a large subset of the cube when the degree vector of `S` is almost
constant, so this route does not currently give a `2^{o(k)}` profile bound.

### Long holes and antiholes

If a graph has an induced cycle of order at least `k`, or the complement of
one, then it has a regular induced subgraph of order at least `k`.  Therefore a
counterexample to `G(k)` has no hole or antihole of length at least `k`, and
also has no clique or independent set of order `k`.

Obstruction: available Erdos--Hajnal-type results for forbidding long holes
and antiholes give polynomial-size homogeneous sets for each fixed forbidden
length, but the quantitative dependence on `k` is far too weak to imply
`G(k) <= 2^{o(k)}`.

### Homogeneous blow-up / block Ramsey

Idea: find many equal-size blocks such that each block is homogeneous and each
pair of blocks is complete or empty.  A regular induced subgraph in the reduced
block graph then lifts to a regular induced subgraph in `G`.

Obstruction: forcing pairwise-uniform blocks of total size `k` by bipartite
Ramsey costs `2^{Theta(k)}` vertices, recovering only the ordinary Ramsey
scale unless a stronger source of structure is found.

### Naive dyadic modular lifting

Idea: use Gallai to get a large even induced subgraph, then hope an even graph
always contains a proportionally large induced subgraph whose degrees are
constant modulo `4`, and iterate.

Obstruction: the brute-force script finds fully even graphs on `7` vertices
whose largest `4`-modular induced subgraph has order only `4`; random fully
even samples on `8` vertices show the same minimum.  This does not refute a
polynomial-loss lifting theorem.

Stronger obstruction: exact parity-graph enumeration on `8` vertices gives
minimum largest `4`-modular witness `4`, and random parity-graph sampling on
`10` vertices found all-even and all-odd graphs with largest `4`-modular
witness exactly `4`.  Thus the statement "parity-modular implies a
`4`-modular induced subgraph on at least half the vertices" is false.

### Repeated-degree route

Idea: use known repeated-degree induced-subgraph relaxations.  If an induced
subgraph `H` has many vertices of one degree and this degree class has constant
degree to its complement in `H`, then that degree class itself is regular.

Obstruction: repeated degree by itself has no trace control.  In the whole
graph, the degree-class bridge can certify only a singleton even when the graph
has a much larger regular induced subgraph; `trace_bridge.py` shows this
already for labelled graphs on `6` vertices and random graphs on `10` vertices.

### Twin quotient / neighborhood diversity

Idea: compress global twin classes.  A large twin class is itself regular, and
a regular induced subgraph in the twin quotient lifts by taking one
representative from each selected class.

Obstruction: the elementary lower bound is only
`max{n/t, c log t}`, where `t` is the number of twin classes.  Optimized over
`t`, this is the ordinary `Omega(log n)` Ramsey lower bound.  Any useful
quotient approach must exploit unequal class sizes or stronger quotient
structure.

### C-Ramsey core

Idea: reduce to graphs with no clique or independent set of order `C log n`
for fixed `C`.  If every fixed-`C` Ramsey graph had
`reg(G)=omega(log |G|)`, then the full conjecture would follow.

Obstruction: known pseudorandomness results for fixed-`C` Ramsey graphs give
many distinct degrees in some induced subgraph, and many different induced
subgraph sizes, but distinctness is the opposite of the repeated-degree
phenomenon needed by the degree-class bridge.  A new argument is needed to
convert Ramsey pseudorandomness into exact induced regularity.

### Equitable partition / color refinement

Idea: the cells of any equitable partition are regular induced subgraphs.
Repeated degree refinement is therefore a certificate for regularity when it
leaves a large cell.

Obstruction: random-like graphs usually refine to singletons.  The experiment
`equitable_partition.py` on random samples with `n=10,12` often returns
`n` cells with maximum cell size `1`, while the true maximum regular induced
subgraph has order `5` or more.  Thus color refinement alone misses the
regular subgraphs in the pseudorandom core.

### Bounded degree spread

Idea: if `A` is an equal-degree class in an induced host `H` and
`|H\A|=s`, then `G[A]` has degree spread at most `s`.  A theorem saying that
graphs with small additive degree spread contain large regular induced
subgraphs would bridge repeated-degree relaxations to the original problem.

Obstruction: no such theorem is currently proved here.  Exhaustive checks show
spread-1 graphs on `6` and `7` vertices force regular induced subgraphs of
order at least `4`, and random spread-2 samples on `12` vertices forced order
at least `6`, but this is only small evidence.  Targeted local search later
found spread-1 graphs on `12` and `14` vertices whose largest regular induced
subgraphs have orders `5` and `6`, respectively, so the natural half-size
linear conjecture is false.

Follow-up searches with a threshold predicate found no spread-1 examples on
`16` vertices with maximum regular order below `7`, and none on `18` vertices
below `8`; later small searches on `20` vertices found none below `8` or
below `9`.  This is weak evidence for a possible lower bound around
`0.4n`, but no theorem is proved.

### Modular exact-size monotonicity

Idea: if a graph has a `q`-modular induced subgraph of order `M`, perhaps it
has `q`-modular induced subgraphs of every smaller order.  This would make
modular terminal arguments much easier because one could first find a large
modular witness and then trim it to the modulus.

Obstruction: false even for regular graphs.  The perfect matching on `6`
vertices is regular, but for moduli `3` and `4` its exact-size modular
spectrum is `{1,2,3,4,6}`, with no witness of size `5`.  Therefore any
exact-size modular proof must construct the desired size directly, not rely
on monotone trimming.

### Minimal repeated-degree host

Idea: choose an induced subgraph `H` that is vertex-minimal subject to
containing `k` equal-degree vertices `A`.  Then no nonempty subset of
`B=H\A` has equal trace-count into every vertex of `A`; otherwise deleting it
preserves the equal-degree class.

Obstruction: this becomes a trace-vector zero-sum problem.  Large multiplicity
of one nonconstant trace type avoids balanced deletion, so an argument also
has to recurse into large trace classes or exploit their internal graph
structure.

Stronger obstruction: even distinct trace types can be exponentially many
without any balanced deletion.  All nonzero vectors in `{0,1}^{k-1}` extended
by a final `0` coordinate form `2^{k-1}-1` distinct traces with no nonempty
subfamily whose coordinate sums are constant.

### Induced path / copath exclusion

Idea: a counterexample to `G(k)` has no induced `P_{2k-1}` and no induced
complement of `P_{2k-1}`, since alternating vertices in such a path give an
independent set of size `k`.

Obstruction: standard chi-bounds for `P_t`-free graphs are far too weak when
`t` is linear in `k`; combined with `omega,alpha<k`, they do not improve the
ordinary Ramsey-scale bound toward `2^{o(k)}`.

### Component / cocomponent restrictions

Idea: a counterexample has fewer than `k` connected components and fewer than
`k` connected components in the complement, since one vertex from each
component gives an independent set, and the complement argument gives a clique.

Obstruction: this is only a coarse structural sanity check.  It prevents
decomposition into many pieces but gives no subexponential bound by itself.

## Promising Lemmas

### Lemma Candidate: hole/antihole reduction

If `reg(G)<k`, then `G` has no induced cycle of length at least `k` and no
induced complement of a cycle of length at least `k`.

This lemma is immediate and reusable, but by itself does not yield the target.

### Lemma Candidate: modular terminal criterion

If `S` is a vertex set with `|S| <= q` and all degrees in `G[S]` are congruent
modulo `q`, then `G[S]` is regular.

This is the clean endpoint of the pair-trace modular approach.

### Lemma Candidate: repeated-degree degree-class bridge

An equal-degree set with constant complement-degree yields a regular induced
subgraph.  This is useful only if a separate argument controls how the repeated
degree is split between the candidate class and its complement.

### Lemma Candidate: twin-quotient lower bound

If `G` has `t` twin classes, then `reg(G) >= max{n/t, c log t}`.  This is a
clean reduction but does not beat Ramsey after optimizing in `t`.

### Proposition Candidate: Ramsey-core reduction

It suffices to prove `reg(G)=omega(log n)` for every fixed-`C` family of
`C`-Ramsey graphs.  This isolates the hard pseudorandom regime.

### Lemma Candidate: equitable-partition cell certificate

Every cell in an equitable partition is regular.  This is a useful structural
certificate but fails to see random-like regular induced subgraphs when the
coarsest equitable partition is discrete.

### Lemma Candidate: repeated-degree bounded-spread bridge

An equal-degree class of order `r` inside a host with `s` outside vertices
induces a graph on `r` vertices with degree spread at most `s`.  This reduces a
piece of the problem to understanding regular induced subgraphs in
additively-near-regular graphs.

### Lemma Candidate: minimal repeated-degree host obstruction

In a minimal host for `k` equal-degree vertices, no nonempty set of outside
vertices has constant trace-count into the equal-degree class.  This translates
the obstruction into a zero-sum/discrepancy condition on trace vectors.

### Lemma Candidate: exponential trace-counting obstruction

There are `2^{k-1}-1` distinct nonconstant trace vectors in `{0,1}^k` with no
balanced nonempty subfamily.  Counting trace types alone cannot give
subexponential progress.

### Lemma Candidate: path/copath exclusion

No counterexample for `G(k)` contains an induced path or induced copath on
`2k-1` vertices.  This is immediate but current quantitative graph-class
bounds do not make it strong enough.

### Lemma Candidate: component/cocomponent restriction

Every counterexample for `G(k)` has fewer than `k` components and fewer than
`k` complement-components.  Useful for checking decompositions, not yet a
source of growth beyond Ramsey.

## Progress Log

- 2026-05-30: Workspace initialized.  Next action: finish literature extraction,
  reconstruct known bounds in local notation, and start proof attempts.
- 2026-05-30: Network downloads failed under sandbox restrictions, so
  literature extraction used the web index and search snippets.  Recorded
  current open status and Dyson--McKay theorem statements visible in indexed
  sources.
- 2026-05-30: Added `EXPERIMENTS/regular_induced.py`.  Exhaustive checks give
  `F(5)=3`, `F(6)=3`, and `F(7)=4`, matching the small classical checkpoint.
  Next action: continue proof search with modular absorption and induced
  density routes.
- 2026-05-30: Modular checks: exhaustive `n=6,7` show every graph has a
  parity-modular induced subgraph of order at least `4`; random samples gave
  minimum seen `9` for `n=14, q=2`, `14` for `n=20, q=2`, and `8` for
  `n=20, q=4`.  The evidence supports large low-modulus witnesses, but the
  modulus-lifting step remains the bottleneck.
- 2026-05-30: Checked the naive lift from full `2`-modularity to
  `4`-modularity.  Exhaustive `n=7` even graphs have worst-case largest
  `4`-modular witness `4`, so no immediate linear-loss dyadic lift is visible.
- 2026-05-30: Added `EXPERIMENTS/trace_bridge.py` and recorded the
  repeated-degree degree-class bridge.  Exhaustive `n=6` and random `n=10`
  checks show that whole-graph repeated-degree classes can have bridge value
  `1`, so repeated-degree theorems need additional complement-degree control
  to be useful.
- 2026-05-30: Added the twin-quotient lower bound.  It clarifies that "few
  trace types" arguments need more than neighborhood-diversity compression,
  because the naive quotient/twin-class dichotomy optimizes to only
  `Omega(log n)`.
- 2026-05-30: Reviewed `PROOF.md` for hidden gaps.  Corrected the conditional
  dyadic proposition so it starts from Gallai's `2`-modular base rather than an
  impossible lossless `1 -> 2` modular lift.
- 2026-05-30: Added `EXPERIMENTS/ramsey_sample.py` and the Ramsey-core
  reduction.  Random samples on `n=10,12` show regular induced subgraphs often
  exceed the largest homogeneous set, consistent with the idea that the
  C-Ramsey core needs a genuinely non-Ramsey mechanism.
- 2026-05-30: Added `EXPERIMENTS/equitable_partition.py` and the equitable
  partition cell lemma.  Random samples usually refine to singleton cells even
  when `reg(G)` is much larger, so this route is only a certificate for
  structured cases, not a full proof.
- 2026-05-30: Added `EXPERIMENTS/degree_spread.py` and the bounded-spread
  bridge.  Exhaustive checks: among labelled graphs with degree spread at most
  `1`, the worst maximum regular induced subgraph has order `4` for `n=6,7`.
  Random spread-2 samples on `n=12` had minimum seen `6`.
- 2026-05-30: Added the induced path/copath exclusion lemma.  It gives another
  hereditary-class reduction for counterexamples, but known `P_t`-free
  chi-bound routes remain quantitatively too weak for `2^{o(k)}`.
- 2026-05-30: Added `EXPERIMENTS/modular_lift.py`.  Exact enumeration of
  all-even and all-odd graphs on `8` vertices gives worst largest
  `4`-modular witness `4`; sampled parity graphs on `10` vertices produced
  verified masks with all degrees even/odd and largest `4`-modular witness
  only `4`, refuting the hoped-for half-size first dyadic lift.
- 2026-05-30: Improved `search_bounded_spread.py` and added mask analysis to
  `degree_spread.py`.  Verified spread-1 masks
  `22368837872701959356` on `12` vertices and
  `146294004578047919044267715` on `14` vertices with maximum regular induced
  orders `5` and `6`.  This refutes the conjecture that spread-1 graphs always
  have a regular induced subgraph on at least half the vertices.
- 2026-05-30: Added the component/cocomponent restriction lemma for
  counterexamples.  This is mainly a structural sanity check for future
  decomposition arguments.
- 2026-05-30: Added the minimal repeated-degree host obstruction.  This gives
  an exact trace-vector condition for why the repeated-degree route fails to
  immediately produce regularity.
- 2026-05-30: Added `EXPERIMENTS/trace_zero_sum.py` and proved the general
  exponential trace-counting obstruction.  Brute force gives maxima
  `1,3,7` for `k=2,3,4`, matching the construction `2^{k-1}-1`.
- 2026-05-30: Added the trace-class recursion lemma, the total trace imbalance
  constraint for repeated-degree hosts, and a corrected exact-size dyadic
  modular program statement.  Next action: test whether zero-sum-free trace
  families with total imbalance at most `k-1` have only subexponential size.
- 2026-05-30: Ran `trace_balance_bound.py` for `k=2,3,4,5`.  The maximum
  distinct admissible sizes remain `1,3,7,15`, so the total trace imbalance
  condition alone still does not break the exponential trace obstruction in
  small dimensions.  Next action: pivot from pure trace counting to arguments
  that also use internal edges in the repeated-degree class or modular lifts.
- 2026-05-30: Added `search_modular_lift.py` and sampled the first dyadic lift
  further.  Even parity graphs had minimum seen largest `4`-modular witness
  sizes `5,6,6,8` for `n=12,14,16,18` in the current runs; local search found
  `6` on `n=16` and `8` on `n=18`.  This remains compatible with a constant
  fraction first lift, but the proof must tolerate losses below one half.
- 2026-05-30: Corrected the dyadic conditional: lower-bound-only modular
  lifting does not imply terminal regularity because the final witness may be
  larger than the modulus.  The proof route now requires exact or otherwise
  size-controlled modular witnesses.  Added `modular_partition.py`; the known
  bad first-lift parity masks fail 2-part `4`-modular partitions but pass
  3-part checks.
- 2026-05-30: Checked exact-size spectra for representative first-lift bad
  masks on `n=10,12,16`; in each case the available `4`-modular sizes were
  all integers from `1` up to the maximum (`4,5,6`, respectively).  This is
  only evidence, not a monotonicity theorem, since modularity is not inherited
  by arbitrary subsets.
- 2026-05-30: Fixed-modulus calibration: exhaustive checks give minimum
  largest `3`-modular witness `3` on `n=6` and `4` on `n=7`; exhaustive
  modulus `4` on `n=7` also gives `4`.  Random modulus-`3` samples on `n=9`
  had minimum seen `4`.  Fixed small moduli appear to force witnesses larger
  than Ramsey in tiny cases, but no general density theorem is proved.
- 2026-05-30: Added the graphical-compensation condition for trace
  obstructions.  The pure trace examples with small total imbalance for
  `k<=5` do not correspond to internal degree sequences on `A`.  With
  graphical compensation enforced, exhaustive distinct-trace maxima are
  `0,2,4,9` for `k=2,3,4,5`; `trace_balance_bound.py` now has a
  `--max-nodes` cap for bounded follow-up searches.
- 2026-05-30: Proved a Steinitz trace bound: in a minimal host for `k`
  repeated degrees, the outside obstruction has size at most
  `(4(k-1)^2+1)^{k-1}`.  This handles multiplicities using the total imbalance
  from equal degrees.  It is structurally useful but still too large
  (`2^{O(k log k)}`) to imply the target.
- 2026-05-30: Added `modular_spectrum.py`.  Exact checks show modular
  exact-size spectra need not be intervals: the perfect matching on `6`
  vertices has modulus-`3` and modulus-`4` spectra `{1,2,3,4,6}`, missing
  size `5`; among parity-modular graphs on `7` vertices, modulus `4` also has
  gaps.  This refutes any route relying on general exact-size monotonicity.
- 2026-05-30: Added a hereditary density-window lemma for counterexamples:
  every induced `u`-vertex subgraph has both edge density and complement edge
  density at least about `1/k` when no regular induced subgraph of order `k`
  exists.  This packages the Caro--Wei obstruction for future density/DRC
  attempts.
- 2026-05-30: Additional spread-1 threshold searches on `20` vertices found no
  examples with maximum regular induced order below `8` or below `9` in short
  local-search runs.  This extends the small evidence for a possible linear
  bounded-spread theorem, but still supplies no proof.
- 2026-05-30: Added a repeated-degree/bounded-spread bridge proposition:
  `F(E(r)) >= Phi(r,(4(r-1)^2+1)^{r-1})`, where `E(r)` forces an induced
  subgraph with `r` equal-degree vertices and `Phi(r,s)` is the guaranteed
  regular induced order in `r`-vertex graphs of spread at most `s`.  This
  makes the repeated-degree route quantitatively explicit, but the present
  spread scale remains too large.
- 2026-05-30: Added `trace_multiset_bound.py`.  With graphical compensation,
  bounded multiset search gives best sizes `0` for difference dimension `1`
  and `3` for dimension `2` with multiplicity cap `4`; a dimension-`3`,
  cap-`2` run with a 50k-node cap was incomplete and found only a size-`2`
  partial example.  Added a subset-sum cap to keep future runs bounded and a
  separating-functional lemma: if all trace vectors have positive weight under
  an integer functional `a`, then `|B| <= (k-1)||a||_1`.
- 2026-05-30: The long exact modular-partition sweep completed: all `2^21`
  even graphs on `8` vertices admit a partition into `3` induced
  `4`-modular parts.  Added `--exhaustive-parity` to
  `modular_partition.py` plus limit/progress flags so this kind of check is
  reproducible without accidentally launching an unbounded run.  A bounded
  rerun over the first `1000` even graphs on `8` vertices saw no
  counterexample, and the full generalized-script rerun later completed with
  `all_ok=2097152`.  This keeps alive a first-lift partition theorem even
  though exact-size monotonicity is false.
- 2026-05-30: Optimized `modular_partition.py` using exact cover over
  precomputed modular subsets and added `--sample-parity`.  Sampled 3-part
  `2 -> 4` partition checks saw no counterexamples for even graphs on
  `n=10` (100 trials), `n=12` (50 trials), `n=14` (20 trials), `n=16`
  (5 trials), and odd graphs on `n=8,10,12` (100, 50, 20 trials).  A bounded
  exact rerun over the first `20000` even `n=8` graphs also saw no
  counterexample.  Two-part checks fail immediately in random even samples on
  `n=8,10`; at this stage three parts looked plausible, but the next
  checkpoint refutes that.
  The stronger version requiring every part to have residue `0 mod 4` is
  false with the same three-color cap and fails quickly in random even `n=8`
  samples, so variable residues or additional parts may be essential.
  Limitation: a bounded partition theorem still needs balance or target-size
  control to imply regularity.
- 2026-05-30: The `3`-part first-lift partition conjecture is false.
  `modular_partition.py` found even masks
  `2354908367450303302346343845` on `14` vertices and
  `543363196844712283609173823066425664` on `16` vertices with no partition
  into three induced `4`-modular parts.  Both have `4`-part partitions; random
  `4`-part checks saw no counterexamples on even `n=14,16,18,20` samples
  (`50,30,20,10` trials).  The first-lift partition route, if true, must
  start with at least four parts.  Added `--find-min-colors`; it verifies that
  both recorded masks have minimum modular partition color number exactly `4`.
- 2026-05-30: Strengthened the partition-tree implication: if every
  `q`-modular induced subgraph can be partitioned into at most `q^alpha`
  induced `2q`-modular parts for some fixed `alpha<1`, then
  `F(n)/log n -> infinity`; constant dyadic part count would be more than
  enough.  Added
  `--sample-full-modular` and `--exhaustive-full-modular` to
  `modular_partition.py`.  Exact checks: every full `4`-modular graph on
  `6` vertices (`184` cases) and on `7` vertices (`1184` cases) has a
  `4`-part partition into induced `8`-modular graphs; in fact `n=7` also
  passes with `2` parts.  Rejection sampling for full `4`-modular graphs on
  `n=8,9,10` saw no `4`-part counterexample, and small `n=8,9` samples saw
  no `2`- or `3`-part counterexample, but acceptance is low.
- 2026-05-30: Added the local congruence criterion for dyadic partitions:
  within a part `P_i`, the residue `deg_H(v)-deg_H(v,V(H)\\P_i) mod 2q` must
  be constant.  Added `--diagnostics` output to `modular_partition.py`.
  Diagnostics on the two minimum-4-color first-lift masks show that pairwise
  cross-degree residues between color classes are not constant, so an
  equitable-style explanation is too strong.
- 2026-05-30: Added minimum-color sampling modes to `modular_partition.py`.
  In random even first-lift samples, `n=14` (30 trials) and `n=16` (20 trials)
  all had minimum color count `3`, so the known color-4 masks appear special
  rather than typical.  In sampled full `4`-modular graphs on `n=8`, the
  `4 -> 8` minimum color count was `1` or `2` in 20 accepted trials.
- 2026-05-30: Added the four-color sign formula for modular partitions and
  `search_modular_partition.py`, a triangle-flip local search over even
  graphs for high first-lift modular partition color number.  The formula is
  exact but currently only reformulates the problem as finding two signings
  with controlled signed neighbor sums.
- 2026-05-30: A bounded run of `search_modular_partition.py` on `n=14`
  found another even graph with first-lift minimum modular partition color
  number exactly `4`, mask `1918387482888137124737399075`; direct diagnostics
  give part sizes/residues `(5,0),(3,2),(2,0),(4,2)`.  A smaller `n=12` run
  with the same cap found only minimum color `3`.  Added a score cache to the
  local-search script because exact partition scoring is the runtime
  bottleneck.
- 2026-05-30: Added the deletion-face characterization: `S` is regular iff
  all one-vertex deletions `S\{v}` have the same edge count.  This gives a
  hypergraph-Ramsey reformulation by coloring `(k-1)`-sets by edge count, but
  the naive density route is too weak: a color class would need density
  greater than `1-1/k` to force the full boundary of a `k`-set by the basic
  covering count, whereas pigeonhole over `O(k^2)` edge-count colors gives
  only `Omega(1/k^2)`.
- 2026-05-30: Added the induced matching/co-induced matching exclusion:
  counterexamples to a regular induced subgraph of order `k` have no induced
  matching of size `ceil(k/2)` in either `G` or its complement.  The obvious
  finite-pattern Ramsey argument on an ordinary matching still gives only an
  exponential bound, so this is structural context rather than a proof.
- 2026-05-30: Added fixed-mask analysis to `regular_induced.py`.  The known
  first-lift color-4 masks are not extremal for ordinary regular witnesses:
  the two `n=14` masks checked have maximum regular order `6` and maximum
  `4`-modular order `6`; the `n=16` mask has maximum regular order `6` and
  maximum `4`-modular order `8`.  Thus high modular partition color is a
  different phenomenon from small largest regular witness in these examples.
- 2026-05-30: Improved `modular_partition.py` sampling for full modulus `4`
  by generating a parity-modular graph first and then filtering for a common
  degree residue modulo `4`; also added an optional exact-cover node limit for
  long heuristic runs.  With the improved sampler, `4 -> 8` partition checks
  saw no `4`-part counterexample in `20` accepted samples on `n=10` and `5`
  accepted samples on `n=12`.
- 2026-05-30: Additional bounded trace-multiset searches in difference
  dimension `3` with graphical compensation remained inconclusive.  With
  multiplicity cap `2`, a 100k-node run found only a size-2 partial example;
  with cap `3`, a 100k-node run found no positive partial example before the
  cap.  These runs are too slow for broad exploration without stronger
  pruning, and they do not improve the Steinitz trace bound.
- 2026-05-30: Reviewed the path-free route and removed an attempted proof
  that a longest induced path dominates; this is false in trees with three
  long arms.  The proof file now records only the safe conclusion: standard
  `P_t`-free chi-bounds are too weak for the target unless supplemented by a
  new structural ingredient.
- 2026-05-30: Added a maximal-induced-matching cover proposition.  If
  `alpha<a`, `omega<=w`, and `im<r`, then a maximal induced matching covers
  the graph up to an independent set and `2(r-1)` neighborhoods, giving
  `|V| <= (a+2r)(2r)^w`.  Applied to Problem 82 this is only `k^{O(k)}`,
  weaker than Ramsey, but it cleanly captures the limitation of the induced
  matching route.
- 2026-05-30: Clarified the zero-residue modular-partition obstruction.  The
  known `n=14` color-4 first-lift masks do have `4`-part partitions with all
  residues `0 mod 4`, but the even `n=8` mask `86423135` has unrestricted
  minimum color count `3` and zero-residue minimum color count `5`.  Thus
  zero-residue lifting is strictly more expensive than residue-flexible
  lifting even at the first dyadic step.
- 2026-05-30: Added the dyadic bit-polynomial lemma: for `q=2^s`, the new
  bit `floor((sum z_i)/q) mod 2` is the elementary symmetric polynomial of
  degree `q` in the neighbor indicators.  This makes the algebraic lifting
  obstruction precise: a direct polynomial-system attack on the `q -> 2q`
  lift has degree growing with `q`, even though the number of color variables
  remains linear in the vertex count.
- 2026-05-30: Refuted the zero-residue dyadic program as a possible route to
  the needed sublinear partition bound.  For every power of two `q`, the
  clique `K_q` is `q`-modular, but any partition into induced subgraphs with
  all degrees `0 mod 2q` must use `q` singleton parts.  Direct checks confirm
  `K_6` needs six `0 mod 8` parts and `K_8` needs eight `0 mod 16` parts.
  Therefore a successful dyadic partition theorem must allow nonzero lifted
  residues depending on the part.
- 2026-05-30: Improved the full-modular sampler again: dyadic sampling now
  recursively conditions on the previous modulus, and `random_parity_mask`
  reuses precomputed edge data instead of rebuilding it every candidate.
  A smoke test for the residue-flexible `8 -> 16` step on `n=12` accepted one
  full `8`-modular graph after `15650` attempts and found a `4`-part
  `16`-modular partition.  A previous pre-optimization `n=12` sampling run was
  too slow, which exposed the precomputation bug.
- 2026-05-31: Added the pairwise merge criterion for modular parts: two
  `M`-modular parts with residues `r_A,r_B` merge exactly when the cross-degree
  residues are constant on both sides and the shifted residues agree.  This
  gives a precise obstruction in a minimum modular partition.
- 2026-05-31: Added `merge_modular_partition.py`, a greedy compression
  heuristic starting from singleton target-modular parts.  On the known
  first-lift hard masks, random merging reaches the optimal `4` parts for the
  `n=14` mask and reaches `4` parts for the `n=16` mask in `3/500` restarts,
  while deterministic largest/smallest merge orders get stuck at `6` parts on
  the `n=16` mask.  This suggests a merge/absorption proof would need
  non-greedy exchange, not just a canonical merge order.
- 2026-05-31: Merge heuristic samples were consistent with small constant
  residue-flexible dyadic partitions: even `n=12` first-lift samples had best
  merge counts `3` or `4`; full `4`-modular `n=10` samples for `4 -> 8` had
  best merge counts at most `3`; full `8`-modular `n=10` samples for
  `8 -> 16` also had best merge counts at most `3`.  These are heuristic
  compression results, not certificates of a universal theorem.
- 2026-05-31: Added `decomposable_partition.py` to test exact
  merge-decomposable modular partitions.  The two known first-lift hard masks
  both have minimum ordinary modular partition count `4` and minimum
  merge-decomposable partition count `4`.  However, they also contain
  nondecomposable modular subsets: `20` such subsets for the `n=14` mask and
  `42` for the `n=16` mask, largest size `5` in both cases.  Thus not every
  modular set has a merge tree, but optimal bounded partitions may still be
  obtainable from merge-decomposable pieces.
- 2026-05-31: Refined the merge-decomposable obstruction.  The cycle `C_5`
  itself is `4`-modular but not merge-decomposable; the script verifies this
  with mask `665`, where the whole set is the unique nondecomposable modular
  subset and the minimum decomposable partition count is `3` instead of `1`.
  A random even `n=10` mask `2019815596227` has a `2`-part ordinary
  `4`-modular partition but needs `3` merge-decomposable parts, so the
  merge-decomposable strengthening is strictly stronger than the ordinary
  modular partition problem even for full partitions.
- 2026-05-31: Strengthened the cycle obstruction: for `n>=4`, `C_n` is
  merge-decomposable as a `4`-modular set only if `n` is even or divisible by
  `3`.  The final merge would have to split the cycle into two proper
  `4`-modular induced subgraphs, hence into two independent sets/matchings;
  the only odd non-bipartite possibility is the repeated `MMI` pattern, which
  forces `3 | n`.  Thus `C_5,C_7,C_11,...` give an infinite family of
  `4`-modular sets that cannot be built by pairwise modular merges.
- 2026-05-31: Additional decomposable-partition sampling found the known gap
  to be small in first-lift random instances.  For even `n=12` parity graphs,
  `100` trials all had ordinary and decomposable minimum partition counts
  equal (`5` cases at `2`, `95` at `3`).  For even `n=14`, `30` trials all had
  equality at `3`.  The `n=10` gap mask still shows the strengthening is not
  equivalent, but no growing gap is visible in these samples.
- 2026-05-31: Added `color_modular_partition.py`, a direct local search over
  fixed-color assignments with a residue-disagreement score and bounded
  Hamming repair.  This resolved an apparent high-color `n=20` first-lift
  candidate (`189143945658397272823308214264933187480527882050749756618`):
  exact cover and greedy merge both stalled, but coloring search plus a
  3-vertex repair found a valid `4`-part `4`-modular partition with part
  sizes/residues `(7,0),(5,2),(4,1),(4,2)`.  Another apparent `n=18` candidate
  was resolved by exact decomposable DP as actually having a `3`-part
  partition.  These were cap artifacts, not counterexamples to the four-part
  first-lift conjecture.
- 2026-05-31: Added the binary parity-split equation and
  `parity_split.py`.  In an even graph with adjacency matrix `A` over `F_2`,
  a bipartition `x` has constant same-color degree parity on each side iff
  `A x = a 1 + b x` for some `a,b in F_2`, so the lower-bit shadow of a
  first-lift split is exactly four linear systems.  On the hard `n=14`, `n=16`
  and `n=20` masks these systems have nontrivial solutions, while `C_5` has
  only trivial solutions.  Random even samples on `n=12` and `n=16` always had
  at least one nontrivial parity-pattern split in the tested runs, so the
  first-lift difficulty appears to be in the next mod-4 bit, not this linear
  lower-bit condition.
- 2026-05-31: Added `hierarchical_lift.py` to test a structured first-lift
  approach: first choose a linear parity-pattern bipartition, then split each
  side into two `4`-modular parts.  This hierarchical strengthening is false.
  The `n=14` hard mask `2354908367450303302346343845` has a `4`-part
  `4`-modular partition, but no partition of this hierarchical form; the
  `n=20` resolved candidate also fails this form.  The `n=16` hard mask does
  admit such a hierarchical partition.  Thus any proof of the four-part
  first-lift conjecture cannot simply split the problem into one parity-linear
  bipartition followed by two independent two-part lifts.
- 2026-05-31: Added a quantitative constant-part corollary to the dyadic
  route.  If every `q`-modular induced subgraph partitions into at most a
  fixed `B` induced `2q`-modular parts, then
  `F(n) >= c_B n^{1/(1+log_2 B)}`.  In particular, the experimentally
  suggested `B=4` theorem at every dyadic step would imply the much stronger
  bound `F(n) >= c n^{1/3}`, still compatible with the Dyson--McKay
  `O(sqrt n)` upper construction.
- 2026-05-31: Extended `color_modular_partition.py` with a full-modular
  sampling mode for higher dyadic lifts.  Four-color residue-flexible searches
  found partitions for all accepted samples in the bounded runs:
  `4 -> 8` on `n=12` (`10/10`) and `n=14` (`5/5`), and `8 -> 16` on `n=12`
  (`3/3`).  These are heuristic local-search certificates for sampled masks,
  not a proof, but they support targeting a uniform constant-part dyadic
  theorem rather than only the first lift.
- 2026-05-31: Added an exhaustive parity minimum-color histogram mode to
  `modular_partition.py`.  The full exact sweep over all `2097152` even graphs
  on `8` vertices gives unrestricted `2 -> 4` modular partition counts
  `1:30720`, `2:946040`, `3:1120392`, with worst value `3`.  In the
  zero-residue variant, the first `200000` graphs already have counts
  `1:699`, `2:6235`, `3:139682`, `4:53240`, `5:144`, with worst value `5` at
  the known mask `86423135`.  This sharpens the finite evidence that residue
  flexibility is essential.
- 2026-05-31: Checked the complete multipartite obstruction class via
  `multipartite_modular.py`.  The exact integer model says a selected bin with
  counts `c_i` is target-modular iff at most one `c_i` is positive or all
  positive `c_i` are congruent modulo the target modulus.  More importantly,
  every complete multipartite `q`-modular graph has an immediate two-part
  `q -> 2q` lift: group whole multipartite classes by their class-size residue
  modulo `2q`.  Bounded certificate checks found worst value `2` for
  `2 -> 4` with up to `6` classes and size `12`, `4 -> 8` with up to `6`
  classes and size `16`, and `8 -> 16` with up to `6` classes and size `24`;
  an exact minimum check for `2 -> 4` with up to `5` classes and size `8`
  also had worst value `2`.  Thus complete multipartite graphs do not refute
  the constant-part dyadic partition route.
- 2026-05-31: Added `twin_blowup_modular.py` for exact dyadic partition
  searches in bounded twin-class blow-ups.  Three-class labelled searches
  found worst value `3` for `2 -> 4` with class sizes up to `6`, and worst
  value `3` for `4 -> 8` with class sizes up to `8`.  A four-class
  `2 -> 4` sweep with sizes up to `4` also had worst value `3`, with `4296`
  source-modular models needing three bins and none needing four.  The clean
  three-bin witness is `K_4` disjoint union `K_{1,3}`: all degrees are odd,
  but no two-color partition has both color classes `4`-modular.  This rules
  out a two-part dyadic theorem even in a tiny twin-blow-up class while still
  leaving the four-part theorem viable.
- 2026-05-31: Added random source-modular sampling to
  `twin_blowup_modular.py`.  A five-class `2 -> 4` sample with sizes up to
  `6` accepted `20` models after `243` attempts and had histogram
  `1:1, 2:14, 3:5`; a five-class `4 -> 8` sample with sizes up to `8`
  accepted `10` models after `1385` attempts and all had two-bin lifts.  No
  twin-blow-up sample has yet required four bins, but three-bin examples are
  common enough that any constant-part theorem should not be expected to
  collapse to two or rely only on complete multipartite residue grouping.
- 2026-05-31: Added residue-signature tools for disjoint unions.  If every
  component has a target-modular partition whose residue signature embeds in
  the same global slot multiset `R`, then their disjoint union has a partition
  using the slots in `R`.  `disjoint_signature.py` found no pair or triple
  obstruction among two `n=8` known masks or two random batches of `n=10`
  even components; the best `n=10` triples still had at least `18` common
  four-slot choices.  `slot_partition.py` tests the stronger first-lift
  aligned-slot target `{0,1,2,3}`.  After fixing the checker to treat slots as
  an unordered multiset, `{0,1,2,3}` worked for the known hard `n=14`, `n=16`,
  and resolved `n=20` masks, for the two apparent random failures
  (`27711936666996894962` on `n=12` and
  `1086409226387921586445119328` on `n=14`), and for random even samples
  (`20` on `n=12`, `10` on `n=14`).  This gives a sharper first-lift target:
  prove every even graph has a `4`-modular partition with signature contained
  in `{0,1,2,3}`.
- 2026-05-31: Reformulated aligned residue slots as self-labelled modular
  colorings.  A partition with residue signature contained in
  `{0,...,M-1}` is equivalent to a label `c:V -> Z/MZ` satisfying
  `deg(v, c^{-1}(c(v))) == c(v) mod M` at every vertex.  This gives a clean
  algebraic target for the first lift (`M=4`).  Exhaustive checks found such
  labelings for every graph on at most `5` vertices for `M=2,3,4,5`, and for
  every graph on `6` vertices for `M=2`; random
  checks found no failures for `M=2,3,4,5,6,8` on `8` and `10` vertices.  The
  hard first-lift masks on `14`, `16`, and the resolved `20` vertices also
  have self-labelled `4`-modular colorings.  Even a theorem for all `M` would
  only yield a `2q`-part `q -> 2q` lift, so it does not by itself prove the
  target, but it may be a useful primitive for absorption or residue-slot
  alignment.
- 2026-05-31: Proved the self-labelled modular coloring theorem for `M=2`.
  Over `F_2`, the desired label vector `x` satisfies the linear system
  `(A+diag(d+1))x=d`, where `d=A1` is the degree-parity vector.  The matrix is
  symmetric, `B1=1`, and every kernel vector is orthogonal to both `1` and
  `d+1`, hence to `d`, so the system is always consistent.  This upgrades the
  `M=2` experimental pattern to a theorem.  The obstruction to extending the
  proof to `M=4` is exactly the nonlinear next binary digit of internal
  degrees.
- 2026-05-31: Added `hier_self_label.py` to test the obvious bootstrapping
  attempt from the new `M=2` theorem to `M=4`: first find a self-labelled
  mod-`2` split, then refine the even side into residues `{0,2}` and the odd
  side into residues `{1,3}` modulo `4`.  This stronger sequential structure
  is false on both known hard first-lift masks (`n=14` and `n=16`).  Hence a
  proof of self-labelled mod-`4` colorings, if true, must choose the two
  residue bits simultaneously rather than by iterating the mod-`2` theorem.
- 2026-05-31: Extended `slot_partition.py` with `--sample-random` and fixed
  the self-labelled slot display for moduli other than `4`.  No local SAT
  solver (`z3`, `pysat`, `pycosat`) is installed, so the current exact checker
  remains subset-DP based.  Additional random graph checks found no
  self-labelled failures for modulus `5` or `6` on `20` random graphs with
  `10` vertices.
- 2026-05-31: The unrestricted self-labelled coloring theorem is false for
  every modulus `M>=3`.  Exhaustive `n=6` checks found the tree mask `659`
  as a counterexample for `M=3,4,5`; its edges are
  `(0,1),(0,2),(0,5),(1,4),(2,3)`, i.e. a tree with branch lengths
  `1,2,2` from its degree-three root.  The obstruction has a short proof:
  each length-two branch forces its internal degree-two vertex to have label
  `1`; then the root cannot be labelled `0`, `1`, or anything else
  consistently with the remaining leaf.  The graph is not even, so it does
  not refute the first-lift target for even graphs.  Exhaustive even-graph
  checking on `n=6` still found no self-labelled `M=4` counterexample
  (`2048` even graphs checked), and an `n=7` exhaustive even-graph check
  found no counterexample among all `32768` Eulerian labelled graphs.  Added
  `--exhaustive-even` to `slot_partition.py` to make this check reproducible.
- 2026-05-31: Added `twin_self_label.py` to test self-labelled colorings in
  twin-class blow-ups without expanding the graph.  The branch-length
  `1,2,2` tree obstruction remains unsatisfied when each class has size `1`,
  but its independent `2`-blow-up has a self-labelled mod-`4` solution:
  classes at the root and its three incident-neighbor positions can be put
  wholly in residue `2`, while the two terminal leaves are put wholly in
  residue `0` (counts `(0,0,2,0)` or `(2,0,0,0)` by class).  A size-`4`
  blow-up also has a solution.  Thus the tree obstruction is not robust under
  the simplest Eulerian blow-ups; the even-degree restriction is doing real
  work rather than merely hiding the same local obstruction.
- 2026-05-31: Extracted the general reason the independent `2`-blowup works:
  every graph `G` has a self-labelled mod-`2` coloring `x`, and assigning both
  twins of `v` in the independent `2`-blowup the label `2x_v` gives
  same-labelled degree `2 * |{u~v: x_u=x_v}| == 2x_v mod 4`.  Thus every
  independent two-blowup is self-labelled mod-`4`.  This is a genuine theorem
  but does not yet cover arbitrary even graphs.
- 2026-05-31: Proved a cactus-class theorem for the restricted first-lift
  target.  If a connected cactus has only cycle blocks and no cycle contains
  adjacent articulation vertices, then it has a self-labelled mod-`4`
  coloring.  The proof labels all articulation vertices `2`; each cycle can
  be made active, contributing `2` at all its articulation vertices, or
  inactive, contributing `0`, by filling the path segments between marked
  vertices with words tiled by `0` and `11`.  The block-cut tree incidence
  matrix over `F_2` then chooses active cycles so every articulation sees an
  odd number of active incident cycles.
- 2026-05-31: The cactus theorem is not sharp.  A small cactus made of a
  central triangle with adjacent articulation vertices and one triangle
  attached at each of the adjacent vertices has a self-labelled mod-`4`
  coloring (`n=7`, mask `1082959`, assignment `1,2,0,0,1,2,2`).  This suggests
  the right extension is a finite rooted cycle-block signature DP, not the
  nonadjacent-articulation restriction itself.
- 2026-05-31: Added `cycle_block_signature.py` and the corresponding
  cycle-block signature criterion for cacti.  A signature records the labels
  of articulation vertices on a cycle and the same-labelled degree
  contributions supplied by that cycle; compatible signatures on the block-cut
  tree patch to a global self-labelled mod-`4` coloring.  The script confirms
  that adjacent marked vertices have feasible signatures beyond the
  active/inactive all-label-`2` patterns used in the first cactus theorem, so
  a finite-state proof for all cycle cacti remains plausible.
- 2026-05-31: Small direct checks of randomly generated cycle cacti with
  `2` or `3` cycle blocks of lengths `3` or `4` found self-labelled mod-`4`
  colorings in all `8` tested cases, including examples with adjacent
  articulation vertices.  This supports pursuing the cycle-block signature
  DP as a route to all Eulerian cactus graphs.
- 2026-05-31: The cycle-block signature DP found and minimized a genuine
  counterexample to the aligned self-labelled first-lift target among
  Eulerian cacti.  The `15`-vertex cactus with cycle blocks
  `(0,1,2,3)`, `(0,4,5)`, `(5,6,7,8)`, `(2,9,10,11)`,
  `(3,12,13,14)` has articulation vertices `0,2,3,5`, signature counts
  `64,16,4,4,4`, and no compatible signature choice.  Its mask is
  `25393864177572795278346554458141`, and direct `slot_partition.py`
  confirms no self-labelled mod-`4` coloring.  However,
  `modular_partition.py --find-min-colors 4` finds a `3`-part ordinary
  `4`-modular partition with residues `(1,0,1)`.  Thus the ordinary
  residue-flexible first-lift route survives, but the aligned slot
  strengthening `{0,1,2,3}` is false.
- 2026-05-31: The ordinary modular partition behavior on cacti is explained
  by a trivial but useful chromatic certificate: every `r`-colorable graph
  partitions into `r` independent sets, hence into `r` zero-residue modular
  parts for every modulus.  Since every cactus is `3`-colorable, every cactus
  has a `3`-part zero-residue modular partition.  The `cactus_modular_dp.py`
  checks all returned residues `(0,0,0)` because they are witnessing this
  chromatic fact, not a deeper modular phenomenon.
- 2026-05-31: Added `universal_slots.py` to test the next weaker alignment
  idea after self-labelled colorings: a fixed multiset of four residues that
  works for every even graph.  Exhaustive checks on all `1024` even graphs on
  `6` vertices leave `14` possible residue multisets; exhaustive checks on
  all `32768` even graphs on `7` vertices kill only `(0,0,0,0)`, leaving
  `13`.  Random sampling found all `13` survive `50` even graphs on `12`
  vertices, while `20` even graphs on `14` vertices kill `(0,0,0,3)` at trial
  `10` (mask `1317212301317005196078255896`), leaving `12` sampled
  survivors.  Thus a universal slot multiset is still possible, but it cannot
  be all-zero or the very sparse `(0,0,0,3)`.
- 2026-05-31: Tested the `12` sampled universal-slot survivors against the
  known hard first-lift masks (`n=14`, `n=16`), the aligned-slot cactus
  obstruction, and the random `n=14` graph that killed `(0,0,0,3)`.  The two
  hard masks and the random killer graph satisfy all `12` candidates.  The
  cactus obstruction kills `(0,1,2,3)` but satisfies the other `11`.  The most
  plausible universal-slot candidates now include multisets with at least two
  zero slots and one nonzero slot, e.g. `(0,0,1,2)`, `(0,0,1,3)`,
  `(0,0,2,3)`, as well as `(0,1,1,2)` and nearby variants.
- 2026-05-31: Proved and recorded the lower-bit reduction for self-labelled
  mod-`4`: after an arbitrary choice of high bit `b`, Lemma 4G applied to the
  subgraph of edges whose endpoints have equal `b` gives a low bit `a` with
  `deg_same(v) == a_v mod 2`.  Thus the lower bit never obstructs
  self-labelled mod-`4`; the problem is to choose `b` and a solution of this
  affine lower-bit system so that `floor(deg_same(v)/2) == b_v mod 2`.
  Added `self4_upper_bit.py` to inspect this upper-bit obstruction.  On the
  hard `n=14` and `n=16` masks, random high-bit samples found no upper-bit
  solution, while the high bit extracted from a known self-labelled coloring
  works.  This suggests the high bit is highly constrained and cannot be
  selected independently of the upper-bit equations.
- 2026-05-31: Added the explicit polynomial form of the self-labelled
  mod-`4` equations.  With label bits `c_v=a_v+2b_v`, the same-label
  indicator on a neighbor is
  `(1+a_u+a_v)(1+b_u+b_v)` over `F_2`; the low-bit equations have degree `2`,
  and the upper-bit equations are the pairwise elementary symmetric sums of
  these indicators and have degree `4`.  The full system has `2n` variables
  but total degree `6n`, so direct Chevalley--Warning does not apply.
- 2026-05-31: Larger random checks for the weakened universal-slot target
  left the same `11` candidate multisets alive.  The command
  `universal_slots.py 16 --sample-even 5 --seed 31` and
  `universal_slots.py 18 --sample-even 3 --seed 82`, restricted to the
  current candidates, both returned survivor count `11`.  The surviving list
  is `(0,0,0,1)`, `(0,0,0,2)`, `(0,0,1,1)`, `(0,0,1,2)`,
  `(0,0,1,3)`, `(0,0,2,2)`, `(0,0,2,3)`, `(0,1,1,1)`,
  `(0,1,1,2)`, `(0,1,1,3)`, and `(0,1,2,2)`.  This is still only evidence
  for the first dyadic lift; it does not address higher moduli or prove a
  uniform partition theorem.
- 2026-05-31: Re-ran the exact randomized universal-slot check more heavily
  on `n=16`: `universal_slots.py 16 --sample-even 30 --seed 1600` left the
  same `11` multisets alive.  This was later superseded by the faster exact
  `n=8` sweep below.
- 2026-05-31: Strengthened the induced-path exclusion.  A forbidden
  counterexample cannot contain an induced path on `3 ceil(k/2)-1` vertices,
  since such a path contains an induced matching of size `ceil(k/2)`, hence a
  regular induced subgraph on at least `k` vertices.  The same holds in the
  complement.  This improves the constant in the path-free reduction but not
  its asymptotic usefulness; standard `P_t`-free machinery still yields only
  `k^{O(k)}`-type bounds.
- 2026-05-31: Added `slot_local_search.py`, a heuristic scorer for fixed
  residue-slot colorings.  Calibration checks on the `15`-vertex cactus
  correctly leave positive score for the killed slots `(0,1,2,3)` and find a
  score-`0` coloring for the surviving slots `(0,0,1,2)`.  An exploratory
  `n=24` sweep was too slow and was stopped; it is not recorded as evidence.
- 2026-05-31: Recorded a degree-barrier lemma for the algebraic dyadic route.
  Even on a star, if `q=2^s` and colors are encoded by `t` bits, the Boolean
  function giving the new dyadic bit of the same-colored leaf count has
  multilinear degree exactly `q t`.  Thus the degree `2q` in the four-color
  sign formula and the higher-degree version from Lemma 5B are intrinsic.
  A direct Chevalley--Warning / Combinatorial Nullstellensatz proof using one
  exact top-bit equation per vertex cannot have the needed degree count.
- 2026-05-31: Added `universal_slots_fast.cpp` and completed the full exact
  labelled even-graph sweep on `n=8` for all `35` four-slot residue multisets.
  The fast checker first reproduced the known `n=7` result (`13` survivors),
  then on `n=8` left exactly ten survivors:
  `(0,0,0,1)`, `(0,0,0,2)`, `(0,0,1,1)`, `(0,0,1,2)`,
  `(0,0,2,2)`, `(0,0,2,3)`, `(0,1,1,1)`, `(0,1,1,2)`,
  `(0,1,2,2)`, and `(0,1,2,3)`.  It killed `(0,0,0,3)` and
  `(0,0,1,3)` with mask `220640831`, and `(0,1,1,3)` with mask
  `220231532`; independent `slot_partition.py` checks confirmed the latter
  two no-certificates.  Since the `15`-vertex cactus already kills
  `(0,1,2,3)`, the combined exact evidence now leaves nine plausible
  universal first-lift slot multisets.
- 2026-05-31: Optimized `universal_slots.py` by indexing target-modular
  subsets by both residue and pivot vertex, avoiding scans through irrelevant
  subsets during the exact-cover recursion.  The optimized script reproduced
  the known `n=7` spot check and completed stronger exact random tests on the
  current nine candidate slots: `25` even graphs on `n=18` with seed `918`
  and `5` even graphs on `n=20` with seed `920`; all nine candidates
  survived.  The current survivor list remains `(0,0,0,1)`, `(0,0,0,2)`,
  `(0,0,1,1)`, `(0,0,1,2)`, `(0,0,2,2)`, `(0,0,2,3)`,
  `(0,1,1,1)`, `(0,1,1,2)`, and `(0,1,2,2)`.
- 2026-05-31: A larger exact random pass killed another universal-slot
  candidate.  `universal_slots.py 14 --sample-even 200 --seed 914` killed
  `(0,1,1,1)` at trial `197` with mask
  `1938867942138712527476832246`; an independent `slot_partition.py` check
  confirms no `(0,1,1,1)` slot partition, while the same graph has
  `(0,0,1,2)` and `(0,1,2,2)` partitions.  A follow-up run
  `universal_slots.py 14 --sample-even 500 --seed 1414` on the remaining
  eight candidates found no further kills.  The current universal first-lift
  slot candidates are `(0,0,0,1)`, `(0,0,0,2)`, `(0,0,1,1)`,
  `(0,0,1,2)`, `(0,0,2,2)`, `(0,0,2,3)`, `(0,1,1,2)`, and
  `(0,1,2,2)`.  A further exact random check on `n=16` with seed `1616`
  over `100` even graphs left the same eight candidates alive.
- 2026-05-31: Recorded a cut-congruence reduction for the strongest
  remaining candidate `(0,0,1,2)`.  After choosing the residue-`1` part `C`
  and residue-`2` part `D`, the two zero slots are equivalent to finding a
  cut of the residual graph `H=G[V\(C union D)]` such that every vertex has
  opposite-side degree congruent to its residual degree modulo `4`.  In signs
  this is `x_v sum_{u in N_H(v)} x_u == -deg_H(v) mod 8`.  This proves the
  candidate for bipartite even graphs and reframes counterexample search as
  an admissible `(C,D)` enumeration plus a mod-`8` signing obstruction.
- 2026-05-31: Extended `multipartite_modular.py` with a fixed-slot count
  model.  Bounded checks with up to `4` multipartite classes and class size
  at most `8` found no complete multipartite obstruction for any of the
  current eight universal slot candidates.  The tool finds a small complete
  multipartite obstruction to the already-killed `(0,1,1,1)` slot:
  class sizes `(2,4,4,4)`.  Added a clean proof that `(0,0,1,2)` covers all
  complete multipartite even graphs.  The even-class case groups whole
  classes by residues `0` and `2` modulo `4`; the odd-class case uses a
  four-case construction by the number of `3 mod 4` classes, splitting such
  classes into pieces of sizes `1 mod 4` and `2 mod 4` when needed.
- 2026-05-31: Validated the complete-multipartite theorem with the fixed-slot
  count model for `(0,0,1,2)` up to `5` classes and class size `12`
  (`922` source-modular size vectors, no counterexample).  A further exact
  random graph check `universal_slots.py 18 --sample-even 50 --seed 1818` on
  the current eight universal slot candidates found no new kill; all eight
  survived.
- 2026-05-31: Added `defect_set.py` to test the stronger one-defect shortcut
  for `(0,0,1,2)`: a residue-`2` set `D` such that `V\D` is zero-residue.
  This condition would prove the slot target with only two nonempty parts, but
  it is much too strong.  The known hard `n=14`, cactus `n=15`, and hard
  `n=16` masks have no such defect set, and `46/50` random even graphs on
  `n=12` with seed `1202` failed it.  Thus the full cut-congruence form in
  Lemma 4I.6 is not an artifact; the residual graph really needs a nontrivial
  two-zero-slot cut in typical cases.
- 2026-05-31: Extended `universal_slots.py` beyond the first lift: it can now
  sample source-`q`-modular graphs and test fixed target slots for `q -> 2q`.
  For `4 -> 8` with four target slots, `3` sampled `4`-modular graphs on
  `n=8` reduced all `330` slot multisets to `33` survivors; `10` samples
  reduced these to `26`; `50` samples reduced them to `18`.  A `K_m` clique
  criterion then killed several deterministic nonstarters, including the
  first-lift slot multiset `(0,0,1,2)` via `K_8`.  After clique tests through
  `K_16` and `25` sampled `4`-modular graphs on `n=10`, the current
  four-slot `4 -> 8` survivors are `(0,0,2,2)`, `(0,0,2,3)`,
  `(0,0,2,4)`, `(0,1,1,2)`, `(0,1,2,2)`, `(0,1,2,3)`,
  `(0,1,2,4)`, `(0,1,2,5)`, and `(0,1,2,6)`.  Conclusion: the first-lift
  fixed-slot theorem, even if true, cannot be iterated unchanged; any dyadic
  constant-part theorem needs modulus-dependent slots or more flexibility.
- 2026-05-31: Re-audited the workspace against the current Problem 82 page and
  the Dyson--McKay arXiv version.  The workspace already had the required
  `NOTES.md`, `LITERATURE.md`, `PROOF.md`, `FORMAL/`, and `EXPERIMENTS/`
  structure; I preserved it and added missing literature details.  The current
  public page still marks the conjecture open, and `PROOF.md` still ends with
  no complete proof.
- 2026-05-31: Added the fixed-`K_r`-free reduction as Proposition 8A.  The
  Ramsey bound `R(r,t) <= O_r(t^{r-1})` implies every fixed-`K_r`-free graph
  has an independent set of polynomial order, hence a regular induced subgraph
  of order `omega(log n)`.  The complement gives the fixed-independence-number
  analogue.  This confirms the comment-thread observation in an elementary
  form but only reduces the hard case to graphs with both clique number and
  independence number tending to infinity.
- 2026-05-31: Added the first-lift chromatic certificate and
  `EXPERIMENTS/first_lift_chromatic.py`.  If `chi(G)<=4` or
  `chi(complement(G))<=4`, then `G` has a four-part `4`-modular partition by
  using independent sets or cliques.  Thus a direct counterexample to the
  flexible first lift must have `chi(G),chi(complement(G))>=5`.  A random
  even-graph check on `n=10` with `300` trials and seed `1510` found one
  high-chromatic candidate, mask `5511811489229`, with
  `chi=chi(complement)=5`; it still has a three-nonempty-part `4`-modular
  partition with residues `(2,2,0)`.  No first-lift counterexample was found.
- 2026-05-31: Improved the Steinitz trace bound in Lemma 17 from
  `(4(k-1)^2+1)^{k-1}` to `(3k)^{k-1}` by applying Steinitz to the centered
  trace vectors `v_b-T/|B|` instead of appending a single correction vector
  `-T`.  This tightens the repeated-degree/bounded-spread bridge but remains
  `2^{Theta(k log k)}`, so it still does not imply `G(k)<=2^{o(k)}`.
  Also noted a caution for future trace searches: the host condition is really
  a spread condition on the `k` coordinate sums, not just an `L_infty` bound
  on the first `k-1` difference coordinates.
- 2026-05-31: Added `--exact-spread` to `trace_balance_bound.py` to test that
  stronger host condition directly.  The exact-spread graphical search gives
  the same complete value `4` for `k=4`; for `k=5`, a `200000` node partial
  search still finds an admissible family of size `8`, so the corrected
  spread filter alone does not collapse the trace obstruction.
- 2026-05-31: Tested a homogeneous-trace amplification idea.  If `A` is an
  independent set, `C_T` is a trace class into `A`, and `C_T` contains an
  independent set `B` of size `s`, then choosing `s` vertices from `T` gives
  an induced `K_{s,s}` when `|T|>=s`, while choosing `s` vertices from
  `A\T` gives an independent set when `|A\T|>=s`.  This is a useful local
  certificate, but it needs `|A|>=ceil(k/2)` to force a regular induced
  subgraph of order at least `k` from one trace class.  Ramsey only provides
  `|A|=Theta(log n)`, so the idea does not beat the Ramsey scale unless one
  can combine many trace classes into a single balanced incidence structure.
- 2026-05-31: Added the universal-slot equivalence for the first lift.  The
  flexible statement "every even graph partitions into at most four
  `4`-modular parts" is equivalent to the existence of one residue multiset
  `R` of size four that works for every even graph.  The nontrivial direction
  uses disjoint unions: if every slot multiset has a killer component, their
  disjoint union is an even graph whose global partition would restrict to a
  forbidden slot partition on one component.  This makes the current eight
  surviving slot multisets decisive targets rather than merely stronger
  variants.
- 2026-05-31: Recorded a density-only DRC limitation.  A `t`-root DRC step in
  a density-`p` graph guarantees only `N p^t` common-neighborhood scale from
  density information alone, and this is tight for near-regular graphs.  Thus
  even in the denser of `G` and its complement, keeping `k` leaves after
  `t` roots needs `N >= k 2^t`; if the hereditary density window is sparse
  with `p=Theta(1/k)`, it needs `N >= k^{t+1}`.  Any DRC route requiring
  `Theta(k)` roots is therefore exponential or worse unless it carries extra
  internal degree control on the leaves.
- 2026-05-31: Added a `--score-all` mode to `universal_slots.py` so the eight
  decisive first-lift slot candidates can be scored on the same sampled even
  graphs.  On `n=12`, `50` even samples with seed `412` were all partitionable
  for every current candidate slot multiset.  Also fixed
  `search_modular_partition.py` so node-limited exact searches are classified
  as `unknown` rather than as no-partition certificates; this prevents false
  counterexample signals in large local searches.
- 2026-05-31: Audited the attempted fixed dyadic universal-slot lemma.  The
  disjoint-union proof is valid only inside a fixed source degree residue
  class modulo `q`, since components with different source residues do not
  form a `q`-modular disjoint union.  `PROOF.md` now states the corrected
  residue-class lemma: a flexible `q -> M` theorem gives one universal slot
  multiset for each source residue `a mod q`, not necessarily a single common
  multiset for all source residues.  The first-lift even-graph lemma remains
  unaffected because its source residue is fixed at `0 mod 2`.
- 2026-05-31: Added source-residue filtering to `universal_slots.py` for the
  corrected dyadic-slot formulation.  For `4 -> 8`, four-slot candidates,
  and `10` sampled `4`-modular graphs on `n=10` in each fixed source residue,
  the sampler still leaves candidates in every residue class: `27` survivors
  for residue `0`, `27` for residue `1`, `20` for residue `2`, and `33` for
  residue `3` with seeds `500,501,502,503`.  This is only small evidence, but
  it supports testing the residue-family version of the dyadic route rather
  than a single common slot family.
- 2026-05-31: Recorded an exact obstruction showing that three target parts
  cannot suffice for the second dyadic lift.  Five `10`-vertex graphs with all
  degrees `2 mod 4` kill all `120` residue triples modulo `8`; their disjoint
  union is source-`2 mod 4` and has no three-part `8`-modular partition.
  Added `slot_obstruction_certificate.py` to verify this certificate.  This
  calibrates the dyadic route: `4 -> 8` needs at least four parts in one
  source residue, but the four-part source-residue version remains plausible.
- 2026-05-31: Added two Ramsey/trace reductions.  Proposition 0A records that
  any exponential-scale counterexample sequence must have both clique number
  and independence number linear in `k`; if either is `o(k)`, the ordinary
  off-diagonal Ramsey bound is already `2^{o(k)}`.  Lemma 14B bounds a graph
  with no regular induced `k`-set by tracing vertices over a maximal
  independent set `A`: each nonempty trace class `C_T` has no clique of order
  `k-1` and no independent set of order `k-|A|+|T|`.  The resulting sum still
  has diagonal-scale exponential terms when `|A|` is close to `k`, so a trace
  proof must couple multiple trace classes rather than Ramsey-bound them
  separately.
- 2026-05-31: Fixed a CLI regression in `modular_partition.py` where
  `--sample-parity` and `--sample-parity-min-colors` passed an obsolete extra
  `limit` argument.  A quick check of the tempting stronger theorem "partition
  into `q` zero-residue mod-`q` parts" found an even `8`-vertex counterexample
  for `q=3`, mask `133782443`, with no three-part partition into induced
  `0 mod 3` subgraphs.  Thus a one-shot zero-residue modular partition theorem
  is also false; residue flexibility remains essential.
- 2026-05-31: Strengthened the homogeneous trace amplification certificate.
  If `A` is independent, all vertices of `B` have the same trace `T subset A`,
  and `G[B]` is `r`-regular on `b` vertices with `b-r<=|T|`, then adjoining
  `b-r` vertices of `T` gives a `b`-regular induced subgraph on `2b-r`
  vertices.  This can amplify dense or medium-density recursive witnesses, but
  high-degree witnesses only add a few vertices; the trace route still needs
  degree control, not just order control, inside trace classes.
- 2026-05-31: Added the clique-base analogue of trace amplification.  If `A`
  is a clique, all vertices of `B` have trace `T subset A`, and `G[B]` is
  `r`-regular on `b` vertices with `r+1<=|A\T|`, then adjoining `r+1`
  vertices of `A\T` gives an `r`-regular induced subgraph on `b+r+1`
  vertices.  Independent bases amplify low-degree witnesses; clique bases
  amplify high-degree witnesses.
- 2026-05-31: Recorded the resulting trace-class degree-window restrictions
  in counterexamples: over an independent base, any regular `b`-vertex
  trace-class witness of degree `r` must have either `b-r>|T|` or
  `2b-r<k`; over a clique base, it must have either `r+1>|A\T|` or
  `b+r+1<k`.  These inequalities are now the target conditions for future
  trace-class combination experiments.
- 2026-05-31: Added `--exhaustive-source-modular` to `universal_slots.py` for
  exact small fixed-source-residue slot sweeps.  For `4 -> 8` with four slots
  on `n=7`, exact enumeration checks `592` source-`0` graphs and leaves `53`
  candidate slot multisets, checks `592` source-`2` graphs and leaves `25`,
  and has no source-`1` or source-`3` graphs because odd source residue is
  incompatible with the even degree sum on an odd number of vertices.
- 2026-05-31: A larger read-only `4 -> 8` source-residue slot audit found no
  four-slot obstruction.  After `1000` accepted `n=10` samples in each source
  residue (`seed=3000+a`), survivor counts among clique-passing slots were
  `7,8,8,6` for residues `0,1,2,3`.  Three simple multisets survived all four
  source residues in that audit: `(0,0,2,2)`, `(0,1,2,2)`, and `(0,1,2,3)`;
  the natural aligned multiset `(0,1,2,3)` also passes all source clique tests
  and remained alive in those samples.  This remains computational evidence
  only, and it should not be extrapolated to higher moduli without new input.
- 2026-05-31: Added the split-graph barrier.  If `V=A union B` with `A` a
  clique and `B` independent, then every regular induced subgraph is already a
  clique or an independent set.  Therefore the reduction to graphs with linear
  clique number and linear independence number cannot be exploited merely by
  taking one large clique and one large independent set and analyzing their
  arbitrary cross-incidence pattern; more global structure is needed.
- 2026-05-31: Proved that split graphs nevertheless satisfy the terminal-size
  partition target.  For `q=ceil(sqrt n)`, split the clique side and
  independent side into chunks of size at most `q+1`; the ceiling inequality
  `ceil(|A|/(q+1))+ceil(|B|/(q+1))<=q` follows from `n<=q^2`.  Thus split
  graphs obstruct the large-clique/large-independent-set trace shortcut, but
  not the capped modular partition program.
- 2026-05-31: Tested size-controlled modular partitions.  Random sampling
  found a `9`-vertex graph, mask `30931749293`, with no balanced three-part
  partition into induced `3`-modular subgraphs of sizes exactly `3,3,3`,
  despite unrestricted three-part mod-`3` partitions appearing easy in small
  samples.  This blocks a tempting way to turn fixed-modulus modular
  partition theorems into large witnesses: balance or size control is a
  genuinely stronger demand.
- 2026-05-31: Added a near-terminal modular extraction lemma and strengthened
  the terminal criterion from size `<=q` to size `<=q+1`.  In the size `q+1`
  case, the only distinct congruent degree values would be `0` and `q`, which
  cannot coexist.  If a `q`-modular graph has `q+s` vertices with `2<=s<q`,
  then its degrees take at most two values; the low-degree class has bounded
  internal maximum degree and the high-degree class has bounded complement
  maximum degree, giving a clique or independent set of order at least
  `(q+s)/(s+1)`.  This helps only when the excess over `q` is small.
- 2026-05-31: Sharpened the quantitative dyadic conditional.  A full
  sublinear power bound `b(q)<=q^alpha` is not necessary: if every dyadic lift
  `q -> 2q` can be done with at most `q/(log_2 q)^C` parts for some `C>2`,
  the largest-part iteration stops at depth `Theta(sqrt(log n))` and the last
  loss still leaves a regular witness of order `(log n)^{C/2-o(1)}`, which is
  `omega(log n)`.  This makes a near-linear but polylog-saving partition
  theorem a viable target.
- 2026-05-31: Proved that complete multipartite graphs are never dyadic
  partition obstructions: if such a graph is `q`-modular, all multipartite
  class sizes are congruent modulo `q`; grouping whole classes by their two
  possible residues modulo `2q` gives at most two induced `2q`-modular parts.
  Complements give the same conclusion for disjoint unions of cliques.
- 2026-05-31: Added a warning about clique-compatible common slots.  Binary
  weights `1,2,4,...,q,2q` give `O(log q)` target slots that pass every clique
  test modulo `2q`, but this does not control multipartite structure.  For
  `q=4`, the uncorrected power-of-two slots `(0,1,3,7)` are already killed by
  `K_{2,2}`, and the lesson remains that slot proofs need
  absorption/repetition beyond subset sums for clique sizes.
- 2026-05-31: Added the perfect-graph reduction.  If `G` is perfect, then
  `n<=alpha(G)omega(G)`, so `G` has a clique or independent set, hence a
  regular induced subgraph, of order at least `sqrt(n)`.  Thus any
  exponential-scale counterexample is non-perfect; by SPGT it has odd holes or
  antiholes, but Lemma 1 already restricts all of them to length `<k`.
- 2026-05-31: Added a non-modular conditional route: if graphs with
  `omega<k` and no induced cycle of length at least `k` have chromatic number
  `2^{o(k)}`, then Problem 82 follows because a counterexample has
  `alpha<k`, `omega<k`, and no such long hole.  Current elementary recursions
  in the workspace only give `2^{O(k log k)}`, so this identifies another
  exact quantitative gap.
- 2026-05-31: Added a one-shot terminal-size modular partition criterion.  If
  every `n`-vertex graph can be partitioned, for `q=ceil(sqrt n)`, into at
  most `q` induced `q`-modular parts each of size at most `q+1`, then Lemma 2
  makes every part regular and the largest part has order at least
  `floor(sqrt n)`.  Exact equal-size balanced partitions are false, but the
  relaxed cap `q+1` survived quick checks: the `n=9,q=3` balanced
  counterexample mask `30931749293` has a three-part mod-`3` partition with
  sizes `4,4,1`, and `200` random `n=10,q=3` samples with max part size `4`
  showed no counterexample.
- 2026-05-31: Relaxed the terminal-size criterion using Lemma 2A.  It is
  enough to partition every `n`-vertex graph, for `q=ceil(sqrt n)`, into at
  most `q` induced `q`-modular parts of size at most `q+s(n)`, provided
  `s(n)=o(sqrt(n)/log n)`.  The largest part has size `Omega(sqrt n)`, and
  the near-terminal extraction gives a regular subset of size at least
  `Omega(sqrt n/(s(n)+1))=omega(log n)`.
- 2026-05-31: Extended `search_modular_partition.py` with `--min-part-size`
  and `--max-part-size` so local search can target terminal-size modular
  partitions.  A quick even-graph search for `n=12,q=4,max_part_size=5`
  evaluated `22` masks with no unknowns and found best minimum color count
  `3`, not a counterexample to the four-part capped target.
- 2026-05-31: Generalized `search_modular_partition.py` with `--unrestricted`
  for all-graph local search via single-edge flips.  A quick unrestricted
  capped search for `n=10,q=3,max_part_size=4` evaluated `61` masks with no
  unknowns and found best minimum color count `3`, again no counterexample to
  the terminal-size target.
- 2026-05-31: Optimized capped exact-cover checks in `modular_partition.py`
  by indexing allowed modular subsets by pivot vertex whenever
  `--max-part-size` is active.  This made terminal-size searches more useful:
  `500` random `n=10,q=4,max_part_size=5` samples had no counterexample; local
  unrestricted searches found best minimum capped color count `4` for
  `n=13`, `n=14`, and `n=15` with no unknowns in the completed runs.  At this
  checkpoint no terminal-size obstruction had appeared, but `n=16,q=4`
  remained too slow for the current exact search.
- 2026-05-31: A subagent independently checked several small terminal-size
  cases without websearch and without editing files.  It exhaustively verified
  all graphs on `n=5,6` for `q=3,max_part_size=4`, rechecked the balanced
  `n=9` counterexample mask `30931749293` and found a capped partition of
  sizes `4,4,1`, verified two known hard `n=14,q=4` masks with cap `5`, and
  sampled unrestricted random graphs through `n=14` plus complete
  multipartite/twin-blowup count models through small total size.  These
  checks found no obstruction below the later `n=25` multipartite example.
- 2026-05-31: Refuted the strict terminal-size partition target by an infinite
  complete-multipartite family.  For every `q>=5`, the graph
  `K_{q^2-q+2,2,1}` has order `n=q^2-q+5`, hence `ceil(sqrt n)=q`, but has no
  partition into at most `q` induced `q`-modular parts of size at most
  `q+1`.  The first case `q=5` is `K_{22,2,1}` on `n=25`; the fixed checker
  confirms it via
  `multipartite_modular.py --target-modulus 5 --cap 5 --max-bin-size 6
  --sizes 1,2,22`, returning `min_bins=NA`; `PROOF.md` now contains a hand
  proof.  Therefore any one-shot route must use the small-excess relaxation or
  a different terminal extraction, not the exact `q+1` cap.
- 2026-05-31: The strict terminal obstruction appears to be a one-unit cap
  issue in the complete-multipartite model.  For `K_{22,2,1}`, cap `q+2=7`
  gives `min_bins=4`; an exact sweep of complete multipartite graphs through
  total size `25` with target modulus `5`, five parts, and max bin size `7`
  found no failures.  Partial sweeps also found no `q+2` failures for
  `q=6` through `5000` generated vectors with up to five classes and for
  `q=7` through `5000` generated vectors with up to four classes, while the
  strict `q+1` cap fails again for `q=6` on `K_{32,2,1}`.  This supports, but
  does not prove, using small excess rather than terminal size.
- 2026-05-31: Added an explicit `q+2` repair for the strict-terminal
  obstruction family.  In `K_{q^2-q+2,2,1}`, take one part with `q+1`
  vertices from the large class plus the singleton, one `(2,2)` part using the
  two medium-class vertices, and split the remaining large-class vertices
  into at most `q-2` independent chunks of size at most `q+2`.  This proves
  that this obstruction only forces excess `2`, not growing excess.
- 2026-05-31: Extended `color_modular_partition.py` with a size-excess
  penalty and replaced its scoring path by adjacency bitmasks instead of the
  `2^n` subset precomputation.  This makes capped modular coloring local
  search viable at `n=25` for unrestricted graphs.  Sanity checks: it finds a
  capped partition for the balanced `n=9` mask `30931749293` with
  `q=3,max_part_size=4`; it finds the exact capped partition for the
  previously hard random `n=16,q=4,max_part_size=6` mask
  `66886435753514383419085300530575522`; and a longer run found a
  `q=5,max_part_size=7` partition for the first random `n=25` mask that the
  short run initially left at score `3`.  These are heuristic successes, not
  certificates for all graphs.
- 2026-05-31: Added `capped_modular_partition.py`, an exact checker that
  enumerates only subsets up to the active cap.  This avoids the full `2^n`
  subset table and makes exact `n=25,q=5,max_part_size=7` checks practical.
  It exactly certifies a partition for the score-`1` random `n=25` mask
  `626652738929200728164847407415762566548667066132033241140782947194049633914703368455711224`
  with parts of sizes `7,7,7,2,2`, and a `100`-sample unrestricted random
  sweep at `n=25,q=5,max_part_size=7` found no counterexample with no
  node-limited instances.  A direct `n=36,q=6,max_part_size=8` random sweep is
  still too slow because the candidate subset count through size `8` is much
  larger.
- 2026-05-31: Improved `capped_modular_partition.py` with `--on-the-fly`,
  which generates candidate parts only for the current uncovered pivot vertex.
  This turned the previously too-slow random checks into quick exact
  certificates: `100` random graphs at `n=36,q=6,max_part_size=8` and `50`
  random graphs at `n=49,q=7,max_part_size=9` all had capped modular
  partitions, with no node limits.  The first hard local-search `n=36` mask
  was also exactly partitioned into part sizes `8,8,8,8,3,1`.  This provides
  stronger evidence for a `q+2` one-shot target, though still no proof.
- 2026-05-31: A read-only subagent found and checked the clean `q+2`
  terminal extraction lemma.  If `H` is `q`-modular and `|H|<=q+2`, then
  either `H` is regular or `|H|=q+2` and `H` is exactly `K_{1,q+1}` or
  `K_{q+1} union K_1`; deleting one vertex always leaves a regular induced
  subgraph.  Consequently, a universal `q+2` capped modular partition theorem
  would imply `F(n)>=floor(sqrt n)-1`, far stronger than the stated
  conjecture.  The next clean finite target is the complete-multipartite
  arithmetic theorem: every class-size vector of total at most `q^2` should
  pack into at most `q` valid bins of size at most `q+2`.
- 2026-05-31: Proved a unit-layer packing lemma for the
  complete-multipartite arithmetic target.  If residual class sizes
  `r_i` satisfy `r_i<=B` and total size at most `B(q+2)`, then assigning each
  class to its `r_i` least-loaded bins packs the residual graph into `B`
  bins of size at most `q+2`, with each bin taking one vertex from every
  assigned class.  Thus complete multipartite graphs with all class sizes at
  most `q` satisfy the `q+2` target.  The remaining gap is to prove that
  single-class chunks from large classes can always reduce to such a residual
  instance without using too many bins.
- 2026-05-31: Added `--print-partition` to `multipartite_modular.py` for fixed
  complete multipartite size vectors.  The family `(1,2,3,q^2-q-2)` shows why
  the unit-layer lemma alone is insufficient: the checker repairs it by using
  repeated `(q+1,1)` special bins between the large class and small classes,
  for example at `q=5` the partition is `(1,0,0,6)`, `(0,1,0,6)`,
  `(0,1,0,6)`, `(0,0,3,0)`.
- 2026-05-31: The second read-only subagent reduced the complete-multipartite
  `q+2` target to a Ferrers rectangle covering problem and identified two
  failed easy strategies.  Threshold truncation fails already for
  `(5,4,3,2,1)` at `q=4`, although it has a three-rectangle cover using
  height-`2` chunks.  Full-bin induction fails for `(5,4,4,4,4)` at `q=5`,
  whose total is `3(q+2)` but which has no legal rectangle of full area
  `q+2=7`; it still packs in four rectangles.  `PROOF.md` now records these
  as warnings for the multipartite arithmetic theorem.
- 2026-05-31: Added `rectangle_cover.py` for the rectangle-only version of the
  complete-multipartite arithmetic theorem.  Exhaustive integer-partition
  checks found no rectangle-cover counterexample for `(bins,cap,max_total)`
  equal to `(5,7,25)` after `9295` vectors and `(6,8,36)` after `99132`
  vectors.  The full `(7,9,49)` sweep is slower than the current Python
  recursion and was killed after about a minute without output.
- 2026-05-31: Optimized `rectangle_cover.py` exhaustive sweeps with a shared
  dynamic-programming cache across integer partitions.  The full
  `(bins,cap,max_total)=(7,9,49)` rectangle-only sweep now completes:
  `1091744` integer partitions checked, `1420692` cached states, and no
  counterexample.  This is currently the strongest evidence that the
  complete-multipartite `q+2` target may hold even without special `(q+1,1)`
  bins.
- 2026-05-31: Began the `q=8` rectangle-only sweep
  `(bins,cap,max_total)=(8,10,64)`.  With an `8,000,000` shared-state limit,
  the checker reached `6,224,263` integer partitions and stopped at an
  unknown vector
  `(14,4,4,3,3,3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1)`.  A direct fixed-vector
  check covers that vector in `8` rectangles:
  `10^1, 4^2, 4^1, 3^3, 3^2, 2^5, 2^3, 1^7`.  A larger `12,000,000`-state
  sweep was killed after several minutes without producing a counterexample
  or final output; progress reporting should be added before the next long
  sweep.
