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
- 2026-05-31: Added a formal conditional proposition: the rectangle covering
  theorem implies the complete-multipartite `q+2` target.  A rectangle
  `r 1_I` corresponds to one induced part taking `r` vertices from every
  multipartite class in `I`; all positive class intersections are equal, so
  the part is regular and has size `r|I|<=q+2`.  This also covers complements,
  i.e. disjoint unions of cliques.
- 2026-05-31: A read-only subagent proved that one-trace amplification over a
  homogeneous base is exhaustive.  For an independent base, adding vertices
  from both `T` and `A\T` to one regular trace-class witness cannot produce a
  new regular graph; the only possibilities are Lemma 14A.1 or the trivial
  independent-set case.  The clique-base dual gives Lemma 14A.2 or the trivial
  clique case.  `PROOF.md` now records this as Lemma 14A.4, pruning the
  single-trace route: future trace progress must combine multiple trace
  classes or use more internal structure.
- 2026-05-31: Updated `rectangle_cover.py` so its search limit counts both
  cached DP states and candidate branches.  This prevents long q=8 sweeps from
  spending minutes inside one high-branching state without producing a useful
  stopping certificate.  With `(bins,cap,max_total)=(8,10,64)` and limit
  `5,000,000`, the sweep reached `1,807,286` integer partitions and stopped at
  the unknown vector
  `(6,6,6,6,5,4,3,2,2,2,1,1,1,1,1,1,1,1,1,1)`.  A direct fixed-vector check
  covers it in `8` rectangles:
  `6^1, 6^1, 6^1, 6^1, 5^1, 3^2, 1^10, 1^7`.
- 2026-05-31: The rectangle-cover subagent did not prove or refute the
  rectangle theorem, but identified a sharper likely finite target: for
  `C>=5,b>=2`, total at most `(b-2)C+6` should be coverable by `b` rectangles
  of area at most `C`.  This would imply the `q`-rectangle theorem by setting
  `b=q,C=q+2`, and it is sharp because `((b-2)C+4,2,1)` of total
  `(b-2)C+7` is not coverable.  The failed full-rectangle induction obstruction
  persists at `(C,b)=(7,3)` with vector `(5,4,4)`, so the next proof attempt
  should be an amortized exchange argument.
- 2026-05-31: Refuted the generalized `+6` rectangle target off the diagonal:
  for `(b,C)=(5,9)`, the vector `(26,4,2,1)` has total
  `33=(b-2)C+6` and no five-rectangle cover.  The next attempted repair was
  the `+4` statement: total at most `(b-2)C+4` should be coverable by `b`
  rectangles of area at most `C`.  It would imply the needed diagonal theorem
  because `(q-2)(q+2)+4=q^2`, and it is preserved by deleting a full
  single-column rectangle.  Exhaustive checks found no counterexample for
  `(b,C,max_total)=(4,9,22),(5,9,31),(6,9,40),(6,10,44)`.  The diagonal target
  is essentially sharp: fixed checks show `(q^2-6,4,2,1)` is not coverable for
  `q=8`, while `(q^2-7,4,2,1)` is coverable for `q=8`.
- 2026-05-31: The rectangle-only diagonal theorem is false.  For `q=9` and
  `q=10`, fixed checks show that `(q^2-7,4,2,1)` has total `q^2` but no cover
  by `q` rectangles of area at most `q+2`; the loss proof generalizes to every
  `q>=9`.  The broader `+4` rectangle target is also false far off the
  diagonal; for example `(b,C)=(5,20)` and vector `(57,4,2,1)` has total
  `(b-2)C+4` and no five-rectangle cover.  The full complete-multipartite
  arithmetic target survives these examples because special `(q+1,1)` bins
  repair them: the checker gives partitions of `(74,4,2,1)` with `8` bins for
  `q=9` and `(93,4,2,1)` with `9` bins for `q=10`.  Pivot: prove the full
  multipartite bin target (rectangles plus special bins), not the
  rectangle-only target.
- 2026-05-31: Added `full_bin_cover.py`, an exact checker for the full
  complete-multipartite bin system: rectangles `r 1_I` plus special
  `(q+1,1)` bins.  It verifies the repaired rectangle counterexamples directly
  and exhaustively checks the full target for `q=5`, `q=6`, and, after adding
  single-class and unit-layer pruning, `q=7`.  A blind `q=8` sweep remains
  too slow for the current candidate ordering; the high-branching test vector
  `(9,8,7,6,6,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)`
  is nevertheless covered by a direct fixed-vector check in `8` bins.
  Candidate ordering still needs optimization before larger exhaustive
  full-bin sweeps are useful.
- 2026-05-31: Recorded the sparse-tail multipartite repair lemma from the
  subagent.  If a vector has one class of size `x`, tail total `A<=q`,
  `x>=(q+1)A`, and total at most `q^2`, then `A` special `(q+1,1)` bins cover
  the tail and the remaining large class fits in at most `q-1-A` single-class
  bins.  This explains why the rectangle-only counterexamples are harmless for
  the full complete-multipartite bin target.
- 2026-05-31: Strengthened the complete-multipartite arithmetic toolkit with
  two lemmas.  The special-plus-excess trimming lemma says that after any
  chosen special bins, it is enough to trim excess above a threshold `B` by
  single-class bins and unit-layer pack the bounded core.  The one-large-class
  repair shows that every vector `(x,tail)` with tail total `<q` and total at
  most `q^2` is coverable, with no lower bound on `x`.  Therefore any
  counterexample to the multipartite bin target must have largest coordinate
  greater than `q` and remaining tail total at least `q`.
- 2026-05-31: Rechecked the full-bin target after the rectangle-only diagonal
  refutation.  `full_bin_cover.py` verifies `(q^2-7,4,2,1)` for every
  `9<=q<=15` with an explicit cover pattern using single-column bins, one
  special `(q+1,1)` bin, and small rectangles; the broader adversarial list
  `(q^2-8,5,2,1)`, `(q^2-8,4,2,1,1)`, `(q^2-9,6,2,1)`,
  `(q^2-9,5,2,1,1)`, `(q^2-10,4,3,2,1)`, and
  `(q^2-12,4,4,2,1,1)` passed for `8<=q<=20`.  Biased random partitions
  near total `q^2` found no full-bin failures through `q=12`.  Exact
  first-layer checks found no full-bin failures at total `q^2+1` for
  `3<=q<=7`, and no failures for `q=6` through total `45=q^2+9`.
  The useful proof invariant is to preserve large coordinates for special-bin
  tail absorption instead of deleting full single-column rectangles greedily.
- 2026-05-31: The independent `multipartite_bin_cover.py` exhaustive checker
  completed the full-bin target for `q=8`: `12,308,138` integer partitions of
  total at most `64` checked, `15,498,424` cached states, `71,697,184`
  candidate branches, and no counterexample.  Thus the complete-multipartite
  `q+2` bin target is now exhaustively verified for every `q<=8`.
- 2026-05-31: Returned briefly to the arbitrary-graph one-shot target at
  `q=9,n=81`.  A local-search coloring run on one random graph with parts
  capped at `11` reduced the violation score to `12` but did not find a
  partition in `30` restarts of `30,000` steps; an exact on-the-fly check was
  killed after producing no output because candidate generation was too slow.
  This is not evidence of a counterexample, only a tooling limit for the
  arbitrary-graph capped partition search at `q=9`.
- 2026-05-31: Added an alternative dyadic conditional that avoids both the
  `q+2` one-shot target and pointwise polylog-saving partitions.  It suffices
  to prove a coarse largest-witness lift, namely every `q`-modular graph on
  `M` vertices has a `2q`-modular induced subgraph on at least `M/(Dq)`
  vertices, plus a single terminal-window lift: every `q`-modular graph on at
  least `q^2` vertices has a `2q`-modular induced subgraph of order between
  `2q` and `2q+s(q)`, where `s(q)=o(q/(log q)^2)`.  After
  `sqrt(log n)` coarse lifts, the retained `q`-modular host is still much
  larger than `q^2`, and Lemma 2A extracts a regular set of size
  `omega(log n)` from the terminal-window witness.  This separates the problem
  into a naive-order dyadic lift and one near-terminal exact-size step.
- 2026-05-31: Recorded a dyadic subagent observation: complete multipartite
  `q`-modular graphs satisfy the coarse `q -> 2q` lift with `D=1`, because
  grouping whole classes by their class-size residue modulo `2q` gives at most
  two `2q`-modular parts and hence retains at least half the vertices.  The
  half-retention factor is sharp at `q=2`: `K_4 union K_{1,3}` is
  `2`-modular but has no `4`-modular induced subgraph on more than `4` of its
  `8` vertices, and disjoint copies preserve the ratio.
- 2026-05-31: Proved the remaining one-large-class boundary.  The
  one-large-class repair now covers every vector `(x,tail)` with
  `sum(tail)<=q` and `x+sum(tail)<=q^2`.  In the boundary case
  `sum(tail)=q`, choose `s` special bins so that
  `x` lies in
  `[s(q+1), s(q+1)+floor((q-s)/2)(q+2)]`; these intervals cover
  `0<=x<=q(q-1)`.  Pair the remaining tail vertices into area-`2` rectangles
  and use the leftover bins for the first class.  Therefore any
  complete-multipartite bin counterexample must have tail total at least
  `q+1` after removing its largest coordinate.
- 2026-05-31: Added a `--max-first` filter to `rectangle_cover.py` so
  rectangle-only sweeps can test bounded-largest-coordinate subproblems while
  reusing the shared DP cache.  Added safe single-column and unit-layer
  pruning to the exhaustive rectangle recursion.  Filtered exhaustive checks
  found no rectangle-cover counterexample for
  `q=6,max_first=13=2q+1`, `q=7,max_first=15=2q+1`, and
  `q=8,max_first=17=2q+1`.  The `q=8` run checked `8,707,829` filtered
  partitions of total at most `64`, skipped `3,600,309` larger-first
  partitions, used `11,084,717` cached states and `67,420,898` candidate
  branches, and found no counterexample.  This supports the next arithmetic
  subtarget: rectangle-only failures may require a coordinate larger than
  `2q+1`.
- 2026-05-31: Added a conditional reduction showing that this bounded-height
  rectangle subtarget is enough for the full complete-multipartite bin target.
  Precisely, if every vector with total at most `(B-2)(q+2)+4` and largest
  coordinate at most `2q+1` has a `B`-rectangle cover with cap `q+2`, then the
  full multipartite target follows: use special bins to reduce every coordinate
  above `2q+1`, then apply the bounded-height rectangle theorem to the
  residual.  Small generalized checks for `(B,C)` equal to
  `(4,7),(5,7),(4,8),(5,8),(6,8),(5,9),(6,9),(7,9)` all passed.
- 2026-05-31: Refuted the bounded-height rectangle hypothesis used in the last
  conditional reduction.  For `B=3` and every `q>=30`, the vector
  `(8,7,6,5,4,3,2,1)` has total `36 <= q+6=(B-2)(q+2)+4` and maximum
  coordinate `8 <= 2q+1`, but it cannot be covered by three rectangles: a
  `B`-rectangle sum has at most `2^B-1` distinct positive coordinate values,
  while this vector has eight.  Local checks with `cap=32` confirm no
  three-rectangle cover and exhibit a four-rectangle cover
  `8^1 4^4 2^4 1^4`.  More generally, `(2^B,2^B-1,...,1)` needs at least
  `B+1` rectangles for all sufficiently large `q`.  Pivot: any replacement
  for the bounded-height reduction must either preserve a distinct-height
  bound in the residual or use special bins/multipartite structure after the
  large-coordinate reduction, rather than asking for arbitrary bounded-height
  rectangle covers.
- 2026-05-31: Added a bounded `--cache-size` option to
  `rectangle_cover.py`.  The `q=7` filtered regression
  `--bins 7 --cap 9 --max-total 49 --max-first 15` still completed with no
  counterexample.  A capped `q=9` diagonal filtered run with
  `--cache-size 8000000` reached `33,000,000` checked partitions at total
  `73`, with `41,382,449` recursive states and `55,691,963` candidate
  branches, before the process was killed without a final verdict.  This is
  only a memory/runtime limit; the diagonal bounded-largest case remains
  unrefuted but is no longer the right standalone target after the
  small-`B` staircase obstruction.
- 2026-05-31: Added the reservoir lifting criterion suggested by the full-bin
  subagent.  If a large coordinate `x` is used as a reservoir, `s` specials
  delete chosen tail units, and the residual tail has a rectangle cover
  `r_j 1_{I_j}` satisfying the lifted area bounds `r_j(|I_j|+1)<=q+2`, then
  adjoining the reservoir to every tail rectangle uses reservoir height
  `H=sum r_j`; the remaining reservoir fits into singleton bins provided
  `s+R<=q`, `x>=s(q+1)+H`, and
  `x-s(q+1)-H <= (q-s-R)(q+2)`.  This exactly repairs the staircase family
  `((q-3)(q+2),8,7,6,5,4,3,2,1)` for every `q>=30`: the vector has no
  `q`-rectangle cover by a tail-height/capacity argument, but one special
  lowers the `8` to `7`, and the tail `(7,7,6,5,4,3,2,1)` is covered by
  three lifted binary rectangles of heights `4,2,1`.  Next target:
  generalize this into a sparse-special rank-reduction lemma for arbitrary
  tails with one large reservoir coordinate.
- 2026-05-31: Added `one_large_tail_scan.py` to make the next reservoir
  target reproducible.  It exhaustively enumerates vectors `(x,tail)` with
  `x>=max(tail)`, `x+sum(tail)<=q^2`, and `sum(tail)<=factor*q`, then calls
  the exact full-bin checker.  With `factor=3`, it found no counterexample for
  `3<=q<=9` (`743,120` cases at `q=9`).  This supports a possible extension
  of the one-large-class repair from tail total `<=q` to at least `<=3q`,
  but remains only finite evidence.
- 2026-05-31: Integrated the sharper slack form of the reservoir certificate.
  If `delta=q^2-x-A`, `s` tail units are deleted by specials, and residual
  tail `z` is represented by `R` lifted-legal rectangles with residual mass
  `B` and reservoir height `H`, the remaining reservoir condition is exactly
  `R(q+2)-(B+H)<=2q+delta`.  The binary-bit version gives an explicit
  certificate when every active bit `h` has support `n_h` with
  `h(n_h+1)<=q+2` and `B+H>=(R-2)q+2R-delta`.  Also recorded a wide-tail
  one-large repair: if `A=q+e`, the tail has at least `e+3` positive
  coordinates, and `x>=(q-3)(q+1)+1`, keep one unit in `e+3` tail coordinates,
  delete the other `q-3` tail units by specials, and lift the resulting
  unit-height rectangle.  Barrier: support sizes and slack prevent a
  distinct-height-only lemma; near terminal slack forces sparse-special
  certificates mostly down to one, two, or three dense lifted rectangles.
- 2026-05-31: Added `reservoir_certificate.py`, a fixed-vector checker for
  the binary reservoir certificate.  On
  `q=30`, `((q-3)(q+2),8,7,6,5,4,3,2,1)` it finds a valid certificate with
  residual tail `(8,6,6,4,4,2,2,0)`, deleted mass `4`, active bits
  `2,4,8`, support counts `4,4,1`, and zero global slack.  This gives a
  second explicit repair of the rectangle-only staircase obstruction and
  provides a way to test future sparse-special lemmas directly.
- 2026-05-31: Closed the pure hole/antihole structural route.  A random graph
  `G(n,1/2)` with `n=2^{(1/2-epsilon)k}` has, with positive probability,
  `alpha,omega<k` and no induced cycle or induced path of order at least `k`
  in either `G` or its complement.  The expected number of long induced cycles
  is dominated by `n^k 2^{-binom(k,2)}=2^{-epsilon k^2+O(k)}`, and the path
  estimate is no larger up to subexponential factors.  Thus the consequences
  “no large clique/independent set, no long hole/antihole, no long
  path/copath” still permit exponential-size graphs and cannot by themselves
  imply `G(k)<=2^{o(k)}`.
- 2026-05-31: Recorded terminal-window dyadic calibration.  A
  `2q`-modular witness of size `2q+r<3q` is either regular or has only two
  degree values `d,d+2q` with `0<=d<=r-1`; hence a nonregular witness in the
  needed window is an almost split low/high graph.  The terminal-window lift
  is already hard for regular graphs.  In a regular twin blowup of a
  `D`-regular base `B`, a selected vector `x_i=|S cap C_i|` is
  `2q`-modular exactly when `(A_B x)_i` is constant modulo `2q` on the
  support, so exact size `2q` asks for a weighted equitable vector of total
  `2q`.  Also recorded the deletion absorption criterion: deleting
  `P` from a `2q`-modular set preserves `2q`-modularity iff `deg_P(v)` is
  constant modulo `2q` on the remaining vertices, literally constant when
  `|P|<2q`.  This makes simple deletion-only absorption implausible in
  generic regular hosts.
- 2026-05-31: Added `weighted_blowup.py` for the regular twin-blowup hard
  core.  Given a base graph `B`, cluster cap `L`, and target `T`, it searches
  for `0<=x_i<=L`, `sum x_i=T`, with `(A_B x)_i` constant over the support.
  The first cheap certificate is equal weights on a regular induced subgraph
  of the base; randomized dense circulant bases with `(n,L,T)` equal to
  `(24,4,16)`, `(32,4,16)`, `(48,4,32)`, and `(64,4,32)` all had witnesses
  within the small search budget.  At `(128,4,64)` the bounded search reports
  `unknown`, not a failure.  Current evidence suggests random dense regular
  bases are not an immediate obstruction to the terminal twin-blowup target.
- 2026-05-31: Added `regular_terminal_sample.py` for the regular-host hard
  core of the terminal dyadic route.  It samples switched circulant regular
  graphs on `q^2` vertices and directly enumerates `2q`-sets looking for a
  regular induced subgraph.  Runs with `q=4` (`50` samples) and `q=5`
  (`10` samples) found exact terminal regular subsets in every sample.  This
  is weak finite evidence only, but it suggests exact terminal failure is not
  easy to find in dense random-like regular hosts.
- 2026-05-31: Added a weaker final dyadic target.  The terminal-window lift
  can be replaced by a direct `q`-modular host theorem: after the same coarse
  lifts, it is enough that every `q`-modular graph on at least `q^2` vertices
  contain a regular induced subgraph of size `phi(q)=omega((log q)^2)`.
  Since a regular host is already solved, the real terminal hard case is a
  nonregular `q`-modular graph with about `q` degree levels, each level having
  average size about `q`; the needed improvement is to combine repeated-degree
  levels to beat the `Theta(log q)` Ramsey extraction from one level.
- 2026-05-31: Refined the nonregular `q`-modular host target with an exact
  trace characterization.  If `deg_H(v)=a+q lambda(v)` and
  `P=V(H)\\S`, then `H[S]` is regular iff
  `deg_P(v)-q lambda(v)` is constant on `S`; it is `2q`-modular iff the same
  quantity is constant modulo `2q`.  Thus multi-level regularity is a
  trace-balanced face condition.  Repeated degree levels alone are too weak:
  a leaf-completion construction embeds any prescribed graph `X` into a
  `q`-modular host while prescribing the `q`-degree levels of the original
  vertices.  Also recorded that sparse or co-sparse regular hosts are easy:
  a `d`-regular graph on `q^2` vertices with `d<=Cq` has an induced matching
  of size at least `q/(4C)`, hence a linear-size regular induced subgraph.
- 2026-05-31: Added `q_modular_host_sample.py` to sample full `q`-modular
  hosts and measure the largest regular induced subgraph.  For `q=4`, bounded
  rejection samples found best regular orders `7` on `n=16` (`11` checked) and
  `9` on `n=20` (`3` checked).  Acceptance is low and this is only a sanity
  check, but it supports the new terminal host target in small cases.
- 2026-05-31: Added two more trace/level obstructions from the terminal-host
  subagent.  First, two degree levels can still have arbitrary internal graphs:
  if the cross-degree prescriptions `c-deg_X(a)` and `c+q-deg_Y(b)` are
  bipartite-graphical, adding such a bipartite graph makes degrees exactly
  `c` on one level and `c+q` on the other.  Thus even two-level structure does
  not constrain internal level graphs.  Second, rank-one minimal trace
  obstructions are small: in Lemma 12's setting, if all difference trace
  vectors lie on one real line, minimality forbids zero vectors and opposite
  signs, while Lemma 15's total imbalance bound gives `|B|<=k-1`.  Therefore
  any large repeated-degree trace obstruction must be high-dimensional.
- 2026-05-31: Added the basic sparse/co-sparse reduction for the `q`-modular
  host theorem.  By Caro--Wei, any graph on at least `q^2` vertices with
  average degree at most `q^2/L` contains an independent set of order
  `Omega(L)`, and the complement gives a clique under the analogous
  co-average condition.  Therefore the hard terminal hosts for
  `L=(log q)^2` have both density and co-density at least
  `Omega(1/(log q)^2)`; the modular trace-balance structure is only needed in
  this ordinary-density core.
- 2026-05-31: Recorded that a flexible `O(q)` partition theorem would provide
  the coarse dyadic lift: if every `q`-modular graph partitions into at most
  `Dq` induced `2q`-modular parts, the largest part has size at least
  `M/(Dq)`.  This is weaker than the fixed-slot/self-labelled targets already
  refuted elsewhere.  Fresh samples found no failures for even graphs on
  `8` and `10` vertices partitioning into four `4`-modular parts, nor for
  `4`-modular graphs on `12` vertices partitioning into eight `8`-modular
  parts.
- 2026-05-31: Weakened the coarse partition target further.  For the
  `q`-modular host route, each dyadic lift may lose a fixed polylogarithmic
  factor: replacing `Dq_i` by `q_i(log q_i)^C` over
  `t=floor(sqrt(log n))` steps costs only
  `prod_{i<t} i^C=2^{o(t^2)}=n^{o(1)}`, so the retained terminal host is still
  much larger than `q_t^2`.  Thus a flexible partition theorem with
  `q polylog(q)` parts plus the modular-host theorem would suffice.
- 2026-05-31: Reduced the coarse flexible partition target to connected
  graphs.  If every connected `q`-modular graph has a `B(q)`-part
  `2q`-modular partition, then every `q`-modular graph has a
  `2q B(q)`-part partition by aligning component pieces in global residue
  slots.  Hence connected `O(1)` parts imply an `O(q)` coarse lift, and
  connected `polylog(q)` parts imply the `q polylog(q)` lift allowed above.
  Also recorded the universal-slot compactness: for fixed source residue and
  bounded part count, flexible partitioning is equivalent to a single
  source-residue-dependent residue multiset working for all graphs, by taking
  disjoint unions over failed slot multisets.
- 2026-05-31: Added `--connected-only` to `modular_partition.py` for
  full-modular sampling.  Connected samples strengthen the coarse-lift
  evidence: `2 -> 4` on `n=10` had minimum flexible color count at most `3`
  in `50` connected accepted samples; `4 -> 8` on `n=12` had minimum at most
  `3` in `20` connected accepted samples, and a direct `3`-color check saw no
  counterexample in `50` connected samples.  For `n=14`, `4 -> 8` had minimum
  at most `3` in `10` connected samples.  This supports the connected
  constant-part target, though it is still small finite evidence.
- 2026-05-31: Pushed the connected `4 -> 8` sampling to `n=16`.  A direct
  three-color connected-source run accepted `20` samples with no
  counterexample, with `2` node-limited skips; a min-color run on `10`
  connected samples had histogram `3:10`.  This continues to support the
  conjectural connected constant-part coarse lift.
- 2026-05-31: Pushed the connected first lift `2 -> 4` further.  Direct
  three-color checks on connected even graphs found no counterexample in
  `100` accepted samples at `n=12` and `100` accepted samples at `n=14`, with
  no node-limited skips.  This supports the focused conjecture that every
  connected even graph has a three-part flexible `4`-modular partition.
- 2026-05-31: Checked several connected Eulerian cactus chains against the
  three-part flexible `2 -> 4` target, including chains of triangles, 5-cycles,
  6-cycles, and mixed odd cycles up to `16` vertices.  All had a flexible
  `4`-modular partition using at most three parts.  Thus the known cactus
  obstructions to self-labelled/fixed-slot strategies do not immediately
  refute the connected flexible three-part conjecture.
- 2026-05-31: Refuted the connected three-part first-lift conjecture.  A
  connected even graph on `13` vertices with edge mask
  `92042955548604715393797` has no partition into three induced
  `4`-modular parts; exact enumeration finds `258` nonempty mod-`4` subsets
  and no covering triple.  It has a four-part partition
  `{0,2,11,12}`, `{1,7,9,10}`, `{3,4,8}`, `{5,6}` with residues
  `0,2,2,0`.  Therefore the connected first-lift theorem, if true, needs at
  least four parts; the broader connected `O(1)` target remains plausible.
- 2026-05-31: Tested the corrected connected first-lift target with four
  parts.  Connected even samples found no `2 -> 4` counterexample with four
  flexible parts in `100` accepted samples at `n=16`; at `n=18`, the run
  accepted `43` connected samples before the `3,000,000` attempt cap and
  likewise found no counterexample.  This supports connected `C=4` as the
  next first-lift target.
- 2026-05-31: Added a connected zero-residue obstruction for the first lift.
  The connected even `10`-vertex mask `22114857535095` has zero-residue
  mod-`4` minimum partition count `5`, but flexible mod-`4` minimum count
  `3` with residues `(1,2,0)`.  Thus any connected first-lift proof must use
  flexible nonzero residues; it cannot reduce to a four-coloring by
  zero-residue induced subgraphs.
- 2026-05-31: Added a middle-density obstruction to exact terminal host
  extraction.  For `q=4`, the `16`-vertex `4`-modular mask
  `840252375412894364828623063537651415` has degree sequence consisting of
  four `5`s and twelve `9`s, edge density `64/120`, and largest regular
  induced subgraph of order only `7<2q`.  The terminal host route therefore
  cannot aim for an exact regular `2q`-set even in two-level middle-density
  hosts; the remaining viable target is still `omega((log q)^2)`.
- 2026-05-31: Added a low-rank trace obstruction bound.  In Lemma 12's
  minimal repeated-degree setting, if the difference trace vectors have real
  span dimension `rho`, then
  `|B| <= max{rho(k-1), (k-1+2rho+3)^rho}` by projecting to `rho` coordinates
  and applying the centered Steinitz partial-sum argument.  This generalizes
  the rank-one collapse: any large trace obstruction must be high-rank, not
  merely high-multiplicity.
- 2026-05-31: Targeted slot sampling for the strongest first-lift survivor
  `(0,0,1,2)` found no counterexample in `50` random even graphs on `14`
  vertices and `20` random even graphs on `16` vertices.  This remains weak
  evidence only, but it keeps `(0,0,1,2)` as the most concrete first-lift
  alignment target.
- 2026-05-31: Strengthened the main conditional reduction.  A connected
  dyadic lift theorem with `B(q)=polylog(q)` parts would alone imply
  `F(n) >= (log_2 n) log_2 log_2 n` for large `n`, without a separate terminal
  host theorem.  Under a no-regular-`R` assumption, every induced subgraph has
  fewer than `R` connected components; after each connected lift, choosing the
  largest connected component costs only `R B(q)`.  Once
  `q_i > R^2 B(q_i)`, the process cannot drop from above `R` to below `R`
  before crossing the terminal threshold `|H_i|<=q_i+1`, where Lemma 2 gives a
  forbidden regular subgraph.  With `R=(log n)log log n`, the initial
  `O(log R)` setup losses are `2^{o(log n)}`, so the argument starts with
  component size still above `R`.
- 2026-05-31: Improved the core reduction using complements.  If a flexible
  partition or large-witness theorem holds for connected `q`-modular graphs,
  it holds for all `q`-modular graphs: the complement of a disconnected graph
  is connected, remains `q`-modular, and induced modularity transfers back
  through complement.  Therefore the large-witness target alone would give the
  stronger conditional bound
  `F(n) >= 2^{c log_2 n / log_2 log_2 n}`.  The remaining central conjecture is:
  every connected dyadic `q`-modular graph has an induced `2q`-modular
  subgraph of size `|V|/polylog(q)`.  A polylog-part partition theorem is only
  one sufficient way to prove this witness conjecture.
- 2026-05-31: The existing disconnected three-part `4 -> 8` obstruction also
  yields a connected obstruction by complementing the five-component
  certificate from Proposition 4E.4.  Thus connected three-part `4 -> 8` is
  false; four parts remain the calibrated constant target for low dyadic
  lifts.
- 2026-05-31: Further weakened the dyadic target.  A polylog-fraction witness
  is unnecessary: it suffices to prove that every connected dyadic
  `q`-modular graph has an induced `2q`-modular witness of size at least
  `|V| psi(q)/q`, where `psi(q)=omega((log q)^2)`.  Iterating with this loss
  keeps the process above the terminal range until `log q=Omega(sqrt(log n))`;
  at the first terminal step Lemma 2 gives a regular graph of size at least
  `psi(q)=omega(log n)`.  Thus the current weakest target is a logarithmic
  saving over the natural `q`-scale loss, not a full polylogarithmic fraction.
- 2026-05-31: Added `two_level_modular_sample.py` for dense two-degree
  `q`-modular stress tests.  For connected graphs with `q=8` and degree levels
  `5,13`, exact `16`-modular witness checks found best maxima `9/18` in three
  samples and `8/20` in five samples after degree-preserving swaps.  These small
  tests do not refute the logarithmic-saving target, but they show randomized
  two-level hosts are a useful hard model for future larger heuristic searches.
- 2026-05-31: Added `--on-the-fly` to `two_level_modular_sample.py` so exact
  maximum target-modular order can be scanned without the large incident-table
  precompute.  A connected `n=24`, `q=8`, degree-level `5,13` sample with
  `8000` swaps had largest `16`-modular witness `9`, ratio `0.375`.
- 2026-05-31: Reassessed the log-squared dyadic witness target.  A random
  dense two-degree heuristic with `N` vertices and two degree values separated
  by `q` suggests that fixed sets of size `N psi(q)/q` are `2q`-modular with
  first moment about `2q(e/(2psi(q)))^s`, so the universal witness theorem is
  probably false once `psi(q)->infinity`.  The viable replacement is a
  witness-or-regular dichotomy.
- 2026-05-31: Added a conditional reduction for that replacement.  It suffices
  to prove a connected dyadic dichotomy: every nonterminal `q`-modular host on
  `M` vertices contains either a `2q`-modular witness of size
  `Omega(M psi(q)/q)` with `psi(q)=omega((log q)^2)`, or a regular induced
  subgraph of size `Omega(max{rho(M),psi(q)})` with `rho(M)=omega(log M)`.
  Early direct regular escapes use `rho(M)=omega(log M)`, late escapes and the
  terminal step use `psi(2^{Theta(sqrt(log n))})=omega(log n)`.
- 2026-05-31: Extended `two_level_modular_sample.py` with `--measure-regular`
  to test the regular side of the dichotomy in the same two-degree samples.
  Exact checks found matching modular and regular maxima in small dense cases:
  `q=8,n=20` degrees `5,13` gave max `16`-modular and regular order `9` in
  three samples; `q=8,n=22` degrees `7,15` gave best `8` with histogram
  `8:1, 9:1`; `q=4,n=18` degrees `7,11` gave best `7`; and `q=4,n=20`
  degrees `8,12` gave best `9`.
- 2026-05-31: Recorded the rigorous iid analogue of the two-degree
  anti-concentration heuristic.  If `H~G(k,1/2)`, `M>=2`, and
  `R=C M^2 log M`, then
  `P(H is M-modular) <= M((1+o_M(1))/M)^(k-R-1)` by sequentially exposing
  future-neighbor blocks and applying the roots-of-unity formula to binomial
  residues.  The missing asymptotic counterexample step is the dense
  fixed-degree version of this anti-concentration lemma.
- 2026-05-31: Extended `q_modular_host_sample.py` to measure the
  target-modular side of the dyadic tradeoff in addition to direct regular
  subgraphs.  Small full `q=4` modular samples again showed matching maxima:
  at `n=12`, ten accepted samples had best regular and `8`-modular order `5`;
  at `n=14`, ten accepted samples had best regular and `8`-modular order `6`.
  The naive full-modular sampler rarely accepts nontrivial `q=8,n=14` samples
  under its current candidate generator, so two-level sampling remains better
  for higher-modulus stress tests.
- 2026-05-31: Added the bounded-spread escape for narrow modular hosts.  Any
  theorem forcing regular induced subgraphs in `N`-vertex graphs with degree
  spread at most `s` immediately handles `q`-modular hosts whose ordinary
  degree levels lie in an interval of length `s`; in particular it handles the
  dense two-degree obstruction model with `s=q`.  A local search found no
  spread-`1`, `n=16` graph with maximum regular order below `7`, but the
  spread-`2`, `n=18` threshold run was too slow and was stopped without a
  useful result.  Exact spread sweeps on `n=7` found minimum regular order `4`
  for both maximum spread `1` (`83,658` graphs checked) and maximum spread `2`
  (`637,372` graphs checked).
- 2026-05-31: Added `--exhaustive` to `q_modular_host_sample.py` for exact
  small tradeoff sweeps.  For `q=2,n=6`, all `2048` full even graphs were
  checked: the Pareto gap first appears in `12` graphs with
  `(max regular,max 4-modular)=(5,6)`, including the star mask `31`, whose
  whole vertex set is `4`-modular but whose leaf set is the regular escape.
  For `q=4,n=7`, all `1184` full `4`-modular graphs had matching regular and
  `8`-modular maxima, as expected below the terminal size where `8`-modularity
  forces actual regularity.
- 2026-05-31: Checked a tempting modulo-zero partition side route.  Tiny
  exhaustive sweeps show that every full `3`-modular graph on `6` vertices
  partitions into three induced `3`-modular zero-residue parts, and every full
  `4`-modular graph on `6` vertices partitions into four induced
  `4`-modular zero-residue parts.  This does not solve the dyadic lift:
  partitioning into `q`-modular zero-residue parts does not control the new
  bit needed for induced `2q`-modularity, and the first-lift obstructions
  already show that naive two-part lifting fails.
- 2026-05-31: Sampled the baseline `4 -> 8` flexible partition problem.
  Twenty accepted full `4`-modular graphs on `10` vertices all partitioned
  into at most three induced `8`-modular parts (`10` were already
  `8`-modular, `4` needed two parts, `6` needed three).  This is only small
  evidence for an `O(q)` baseline partition theorem; it gives no logarithmic
  saving by itself.
- 2026-05-31: A subagent audit found no elementary proof or small obstruction
  for the baseline `O(q)` dyadic partition theorem.  It remains consistent
  with all recorded data, but already contains the hard first-lift target:
  every connected even graph should partition into at most four induced
  `4`-modular parts.  The audit reconfirmed the `n=13` and `n=14` connected
  first-lift masks requiring four parts, the five-mask `4 -> 8` three-part
  obstruction, and positive small data: all `1184` full `4`-modular graphs on
  `7` vertices partition into four induced `8`-modular parts, and all `3074`
  full `3`-modular graphs on `7` vertices partition into three induced
  `6`-modular parts.  The naive split by total degree modulo `2q` fails
  because the induced residue depends on color-dependent cross-degree terms.
- 2026-05-31: Added `--diagnostics` for `slot_partition.py` in the
  `(0,0,1,2)` case.  It prints the two zero-residue cut sides `A,B`, the
  residue-`1` set `C`, the residue-`2` set `D`, and verifies the residual
  cut congruence from Lemma 4I.6.  The connected `n=13` and `n=14` first-lift
  hard masks both pass `(0,0,1,2)`; their diagnostics confirm that the
  residue-`2` and residue-`1` sets are small and the residual cut carries the
  remaining congruence work.  A random even `n=16` sample of `50` graphs found
  no `(0,0,1,2)` failure; an `n=18` sample was too slow and was stopped.
- 2026-05-31: Added `slot_profile.py` to minimize the number of vertices in
  nonzero residue slots for a fixed slot multiset.  For `(0,0,1,2)`, the
  connected `n=13` and `n=14` first-lift masks both have minimum nonzero cost
  `5`: in each case a residue-`2` set of size `3` and a residue-`1` set of
  size `2` suffice, after which the residual splits into the two zero slots.
  The connected zero-residue obstruction mask `22114857535095` has nonzero
  cost `3` for the same slots.
- 2026-05-31: Added `--sample-even` to `slot_profile.py`.  For `(0,0,1,2)`,
  ten random even graphs on `12` vertices had nonzero-cost histogram
  `2:1, 4:5, 5:4`; ten random even graphs on `14` vertices had histogram
  `2:1, 3:2, 4:3, 5:2, 6:2`.  This supports a small-defect first-lift
  heuristic at these sizes, but there is no proof or asymptotic bound yet.
- 2026-05-31: Added `modular_oct.py` for the stronger modular
  odd-cycle-transversal candidate: every even graph should have disjoint
  `C,D` with `G[C]` residue `1 mod 4`, `G[D]` residue `2 mod 4`, and bipartite
  residual.  This implies the `(0,0,1,2)` slot theorem by taking the residual
  bipartition as the two zero slots.  The checker confirms the connected
  `n=13` and `n=14` hard masks, all even graphs through `n=7`, the first
  `50,000` even graphs on `n=8`, and random even samples on `n=10,12,14`.
  The full `n=8` sweep was still too slow and was stopped.  Greedy odd-cycle
  deletion is not a proof because cross-edges among deleted cycles alter the
  internal residues inside their union.
- 2026-05-31: Refuted the modular odd-cycle-transversal strengthening.  A
  random even `16`-vertex graph with mask
  `310072714880078432860970147557715681` has no certificate with bipartite
  residual, as verified by `modular_oct.py`.  It is still even, with degree
  sequence `6^5,8^5,10^3,12^3`, and it does have a `(0,0,1,2)` slot
  partition: `A={0,2,6,7,9,11,12,13,15}`, `B={1,4}`, `C={3,10}`,
  `D={5,8,14}`.  Thus the first-lift slot target survives, but the residual
  must satisfy the full cut congruence of Lemma 4I.6 rather than being
  literally bipartite.  A second random counterexample appeared at `n=18`
  before that longer run was stopped.
- 2026-05-31: Audited minimal-counterexample reductions for modular OCT.
  Disconnected components, isolated vertices, whole cycles, and whole complete
  graphs reduce cleanly.  Cut vertices do not reduce from ordinary witnesses:
  lobe certificates must put the cut vertex in compatible statuses, or the
  same-class degree contributions at the cut vertex add to the wrong residue.
  A rooted residual version would make cut-vertex gluing work for the unrooted
  theorem; exact checks find this rooted version for every root through
  `n=7` and in the hard masks.  Degree-`2` suppression also fails in important
  cases, especially when the suppressed edge has both ends in `C` or lies on a
  residual cycle.
- 2026-05-31: Tested two strengthenings of modular OCT.  The version with
  `C` exactly `1`-regular and `D` exactly `2`-regular passes small even graphs
  through `n=7` and the hard masks, but is false for `K_9`: the original
  modular OCT uses a `7`-vertex clique as the residue-`2` set.  The naive
  two-root residual strengthening is also false: a triangle plus isolated
  vertices cannot keep two adjacent triangle vertices in the residual.  Thus
  the likely induction object is a rooted signature at an articulation, not a
  simple multi-root residual condition.
- 2026-05-31: Refined the bounded-spread target after subagent review.  A
  fixed-spread linear theorem is probably too optimistic because dense random
  adjacent-degree graphs should locally resemble `G(k,1/2)` on induced
  `k`-sets.  The useful terminal-scale target is only
  `Phi(N,q)>=N/q^{1+o(1)}` for `q>=N^{1/3+o(1)}`, or any bound beating
  `max{rho(N),psi(q)}` in the witness-or-regular dichotomy.  Adjacent-degree
  exact samples did not show a small-scale collapse: for degrees `10,11` on
  `n=22`, three connected samples had maximum regular orders `11,12,13`; for
  degrees `11,12` on `n=24`, two connected samples had maximum regular orders
  `13,14`.
- 2026-05-31: Formalized the conditional counterexample to the universal
  log-saving witness theorem.  In the two-degree model with `N=q^3` and degree
  values `(N-q)/2,(N+q)/2`, a fixed-degree anti-concentration estimate
  `P(G[S] is 2q-modular)<=exp(o(|S|))(2q)^-(|S|-1)` for
  `|S|>=N psi(q)/q` would make the expected number of large witnesses tend to
  zero.  Connectivity is harmless: if the sampled witness-free graph is
  disconnected, its complement is connected, remains `q`-modular, and has the
  same target-modular induced sets.
- 2026-05-31: Added a reproducible checker for the surviving strengthened
  first-lift target where the residue-`1` slot in `(0,0,1,2)` must be exactly
  `1`-regular, i.e. an induced matching.  `slot_partition.py` now supports
  `--residue-one-matching`, and the new direct backtracker
  `matching_slot_search.py` verifies the same target by vertex coloring.  The
  strengthened target passes all even graphs through `n=7`, the first
  `200000` even graphs on `n=8`, the known connected `n=13` and `n=14`
  first-lift hard masks, `K_9`, and the `16`-vertex modular-OCT
  counterexample.  Random exact-cover probes on even `n=14,16,18` graphs also
  found no counterexample, but larger dense instances remain search-hard.
  This route survives the OCT refutation because it still permits the
  residual graph to satisfy the full cut congruence instead of being
  bipartite.
- 2026-05-31: Independent subagent audit of the matching-slot first-lift
  target found no counterexample in a stronger sweep: all `2,097,152`
  labelled even graphs on `8` vertices passed.  Added
  `matching_slot_fast.cpp` to make this exact sweep reproducible, and verified
  it locally with `g++ -O3 -std=c++17` followed by
  `/tmp/matching_slot_fast --n 8`;
  random even samples also passed at `n=10` (`200/200`), `n=12` (`100/100`),
  `n=14` (`50/50`), `n=16` (`20/20`), `n=18` (`50/50`), and `n=20`
  (`19/20` certified, one node-limit skip).  The same audit checked complete
  multipartite count models up to four classes of size at most `16` and five
  classes of size at most `8`, again with no counterexample.  This upgrades
  the computational confidence in the matching-slot lemma, but it remains a
  first-lift statement only.
- 2026-05-31: A second subagent audit tested whether the matching-slot idea
  has a clean `4 -> 8` source-residue analogue.  The literal analogue is
  implausible: source residue `1 mod 4` has no surviving four-slot family when
  a residue-`1 mod 8` part is forced to be exactly `1`-regular; the small
  multipartite survivors `(0,0,1,4)`, `(0,1,4,6)`, and `(0,1,5,6)` were all
  killed by random source-`1` samples on `n=10`.  Requiring exact
  `2`-regularity in residue-`2` slots also fails, with complete multipartite
  sizes `(3,7,7,7)` killing `(0,0,2,2)`.  Ordinary source-residue slot lifts
  remain plausible: a compact candidate family surviving the audit is
  `R_0=(0,1,2,4)`, `R_1=(0,0,2,2)`, `R_2=(0,0,1,2)`,
  `R_3=(0,0,1,3)`.  This supports the dyadic witness side but not a direct
  higher-modulus regular-slot escape.
- 2026-05-31: Added a bounded-spread easy-regime lemma.  If an `n`-vertex
  graph has degree spread at most `s` and either its minimum degree or the
  minimum degree of its complement is at most `D`, then it has a regular
  induced subgraph of order at least `n/(D+s+1)` by the greedy/Caro--Wei
  independent-set bound applied to the graph or its complement.  Therefore
  any counterexample to an `n/poly(s)` bounded-spread theorem must be
  medium-density with both graph and complement minimum degree polynomially
  larger than `s`.
- 2026-05-31: Bounded-spread subagent audit found no proof of
  `Phi(n,s)>=n/poly(s)` and no counterexample to the weak `n/(s+2)` scale, but
  confirmed that `Phi(n,1)>=n/2` is false using known spread-`1` masks on
  `n=12` and `n=14`.  It also identified the compensated-double template:
  for any graph `F` with degrees `d_i`, put `F` on one side, `complement(F)`
  on the other, and choose cross-degrees `m-1-d_i` on the first side and
  `d_i+epsilon_i` on the second.  When such a bipartite cross graph exists,
  the resulting graph has degree spread at most `1`.  Thus bounded-spread
  proofs cannot reason only inside a large equal-degree side; the
  compensating side can hide arbitrary internal variation.  Verified
  spread-`1` examples from this template reached regular orders
  `5,6,8,9,10` on `n=12,14,16,18,20`.
- 2026-05-31: Added `compensated_spread.py` to generate the compensated-double
  spread-one template.  The bipartite degree sums require the base graph to
  have about half density: the epsilon count is
  `sum_i(m-1-d_i)-sum_i d_i = m(m-1)-4e(F)`, which must lie between `0` and
  `m`.  Quick random checks produced verified
  spread-one masks with max regular order `7` on `n=14` and `9` on `n=18`,
  matching the qualitative obstruction but not improving the previous
  extremal examples.
- 2026-05-31: Added `--source-residue` to `multipartite_modular.py` fixed-slot
  mode and rechecked the compact ordinary `4 -> 8` source-residue slot
  candidates against complete multipartite graphs with at most six classes and
  class sizes at most `16`.  The four checks all pass:
  source `0` with `(0,1,2,4)` checked `409` size vectors; source `1` with
  `(0,0,2,2)` checked `129`; source `2` with `(0,0,1,2)` checked `169`; and
  source `3` with `(0,0,1,3)` checked `129`.  Without the fixed source
  residue filter, the same slot multisets can be killed by irrelevant source
  classes, so this option is needed for correct dyadic-source calibration.
- 2026-05-31: Added two small positive classes for the first-lift
  matching-slot target.  Every even graph of maximum degree at most `2`
  works by putting odd cycles into the residue-`2` slot and bipartitioning
  the remaining even cycles; complete even graphs work by putting all vertices
  into the zero slot or the residue-`2` slot according as `n` is `1` or
  `3 mod 4`.
- 2026-05-31: Added `--force-color` to `matching_slot_search.py` and tested
  the rooted zero-slot strengthening: every even graph with a specified root
  should have a matching-slot certificate with the root in a zero slot.  Exact
  checks pass for every root in every even graph through `n=7`, and the
  `n=14` hard mask and `n=16` modular-OCT counterexample pass with vertex `0`
  forced into a zero slot.  Recorded the cut-vertex reduction: if this rooted
  strengthening holds for all smaller even lobes, then no connected
  cut-vertex graph is a minimal counterexample to the unrooted matching-slot
  theorem.
- 2026-05-31: Added the linear-algebra shadow of the residual cut equation:
  for any graph `H`, the cut making every same-side degree even is always
  solvable over `F_2` via `(A_H+diag(h))x=h`, where `h` is the degree-parity
  vector.  Hence the obstruction in Lemma 4I.6 is genuinely the second bit,
  not parity.  Also recorded the degree-`2` suppression audit for the
  matching-slot theorem.  If a degree-`2` vertex `v` with nonadjacent
  neighbors `x,y` is suppressed to an edge `xy`, a certificate of the smaller
  graph lifts directly when `x,y` are both in `D`, or when they are in
  different slots but not split as `A/B`.  The boundary patterns not covered
  by this direct lift are `same A`, `same B`, `same C`, and split `A/B`;
  eliminating degree-`2` vertices therefore requires an edge-rooted signature
  theorem or a nonlocal recoloring argument.
- 2026-05-31: Added `--good-edge` to `matching_slot_search.py` to test the
  edge-rooted strengthening needed for degree-`2` suppression.  The target is
  a certificate where a specified edge has endpoints either both in `D`, or in
  different slots but not split between the two zero slots.  Exact checking
  with edge `0:1` passes every even graph through `n=7` in which that edge is
  present (`16,384` graphs at `n=7`), which by relabelling covers every rooted
  edge on at most seven vertices.  The `n=16` modular-OCT counterexample also
  has a good-edge certificate for edge `0:1`.
- 2026-05-31: Extended `matching_slot_fast.cpp` with `--good-edge` and ran the
  full edge-rooted `n=8` sweep.  All `1,048,576` labelled even graphs on
  `8` vertices containing edge `0:1` pass the good-edge matching-slot target.
  This gives stronger finite support for an edge-rooted theorem that would
  make degree-`2` suppression valid in a minimal-counterexample proof.
- 2026-05-31: Ran an `n=9` prefix with
  `/tmp/matching_slot_fast --n 9 --good-edge 0:1 --limit 2000000`; this checks
  `1,000,000` even graphs containing edge `0:1` and found no edge-rooted
  counterexample.  This is prefix evidence only, not an exhaustive `n=9`
  result.
- 2026-05-31: Added `source_slot_finder.py` for source-residue fixed-slot
  searches in the complete multipartite integer model.  For the `8 -> 16`
  dyadic lift, four-slot source-residue families survive all checked
  complete multipartite vectors through six classes of size at most `16`:
  `R_0=(0,0,0,8)`, `R_1=(0,0,2,4)`, `R_2=(0,0,2,6)`,
  `R_3=(0,0,3,5)`, `R_4=(0,4,8,12)`, `R_5=(0,0,5,5)`,
  `R_6=(0,4,6,8)`, and `R_7=(0,0,7,15)`.  Some five-class survivors already
  fail at six classes, e.g. source `6` slots `(0,0,6,7)` on
  `(6,6,6,6,6,6)`, so the slot choices are genuinely source-sensitive.
  A further single-family stress test shows that the displayed source `1`
  choice `(0,0,2,4)` fails by eight classes, on
  `(7,7,7,7,7,15,15,15)`; this does not yet refute four-slot source `1`
  families because the full eight-class candidate search was too expensive.
- 2026-05-31: Replaced `source_slot_finder.py`'s inner complete-multipartite
  check with a legal-bin generator, avoiding the product over all count
  vectors.  Verified it against the slower `multipartite_modular.py` DP on
  small sizes and slot families.  With the faster checker, the `8 -> 16`
  four-slot search through eight classes of size at most `16` completed for
  source residues `1,2,4,5,6,7`: survivor counts were `3,2,3,12,3,8`
  respectively.  Source `0` remained broad (`40` survivors after `80` of
  `88` vectors); source `3` was still slow under this naive candidate loop.
- 2026-05-31: Added the signed-indicator trace refinement.  In the minimal
  repeated-degree host, every outside trace difference vector relative to a
  base vertex is not an arbitrary `{-1,0,1}` vector but a nonzero vector
  `1_S` or `-1_S`.  Added `--trace-cone` to `trace_multiset_bound.py` to
  restrict multiset searches to this actual support.  Short capped runs show
  the restricted search still grows quickly at dimension `5`, so this is a
  structural refinement rather than a closed trace proof.
- 2026-05-31: Made `matching_slot_fast.cpp` chunkable with `--start`,
  `--limit`, and configurable progress output.  Rebuilt with `g++ -O3` and
  verified that the old full edge-rooted `n=8` sweep decomposes into two
  adjacent ranges: `0..1048576` and `1048576..2097152`, each checking
  `524288` even graphs containing edge `0:1` and finding no counterexample.
  A first `n=9` chunk `0..524288` checked `262144` edge-containing even graphs
  and also found no edge-rooted matching-slot counterexample.
- 2026-05-31: Corrected the compensated-spread density calibration.  In
  Lemma 11B the epsilon count is `m(m-1)-4e(F)`, so the base graph must have
  about half of the possible edges, not quarter density.  Updated
  `compensated_spread.py` to sample `p=1/2` by default; a quick
  `m=7,trials=20` check accepted `4` templates and found best regular order
  `8` on `n=14`.
- 2026-05-31: Added Lemma 15B for the signed trace cone.  If all outside
  trace difference vectors in a minimal repeated-degree host have the same
  sign, then the total-imbalance bound gives `|B| <= (k-1)^2`; more generally
  `|B| <= (k-1)^2 + 2C`, where `C` is the coordinate-wise cancellation mass
  between positive and negative trace types.  Updated `trace_multiset_bound.py`
  to report incidence, cancellation mass, and L1 imbalance for `--trace-cone`
  examples.  This isolates the remaining hard trace case as large mixed-sign
  cancellation, not one-sided trace counting.
- 2026-05-31: Tested the naive two-root zero-slot strengthening for the
  matching-slot theorem and found it false.  The graph with mask `1057` on
  `7` vertices is just a triangle on `{0,1,6}` plus four isolated vertices;
  it has a matching-slot certificate, but forcing adjacent triangle vertices
  `0` and `1` into zero slots is impossible.  Therefore any 2-vertex separator
  induction needs a richer boundary signature, not merely a two-root version
  of the cut-vertex rooted-zero candidate.
- 2026-05-31: Improved `source_slot_finder.py` with a canonical sorted-state
  checker for complete multipartite vectors whose class sizes are at most the
  target modulus.  Random checks against the older labelled-class DP passed.
  This completes the previously slow `8 -> 16` source-residue `3` audit
  through eight classes of size at most `16`; exactly twelve four-slot
  families survive:
  `(0,0,3,5)`, `(0,0,3,6)`, `(0,0,3,7)`, `(0,0,3,9)`, `(0,0,3,10)`,
  `(0,0,3,11)`, `(0,1,3,8)`, `(0,2,3,8)`, `(0,3,6,8)`, `(0,3,7,8)`,
  `(0,3,8,10)`, and `(0,3,8,11)`.  Source residue `0` remains the broad
  case with many survivors.
- 2026-05-31: Added `--candidates` to `source_slot_finder.py` for targeted
  source-residue slot checks.  In source residue `0` for the `8 -> 16` lift,
  the five candidate families `(0,0,0,8)`, `(0,0,8,8)`, `(0,0,4,8)`,
  `(0,0,2,8)`, and `(0,0,8,15)` all survive all `88` complete multipartite
  vectors through eight classes of size at most `16`.
- 2026-05-31: Identified a clean source-residue slot pattern in the
  complete-multipartite data.  For `8 -> 16`, every source residue `a mod 8`
  passes all eight-class size-at-most-`16` checks with slots
  `(0,a,8,a+8)`.  The analogous `(0,a,4,a+4)` pattern passes the `4 -> 8`
  checks through eight classes of size at most `8`.  This is now the simplest
  fixed-source dyadic slot family to try to prove or refute beyond the
  multipartite model.
- 2026-05-31: Upgraded the clean source-residue slot pattern to all complete
  multipartite graphs.  If all class sizes are congruent modulo `q`, one part
  takes the common residue layer from every class and has residue `a` or
  `a+q`; the remaining vertices split into a `q`-layer part of residue `0` or
  `q` and a `2q`-multiple layer of residue `0`.  Thus the slots
  `(0,a,q,a+q)` always work for complete multipartite graphs with source
  residue `a`.
- 2026-05-31: Refuted the arbitrary-graph version of the clean slots already
  at `q=2`, source residue `1`.  The 8-vertex odd tree with mask `9954`, edge
  set `02,06,07,12,14,15,23`, and degrees `3,3,3,1,1,1,1,1` has no
  `(0,1,2,3)` mod-`4` slot partition.  Therefore the complete-multipartite
  clean pattern cannot be the full dyadic fixed-slot theorem.
- 2026-05-31: Focused the even-source clean first-lift candidate
  `(0,0,2,2)`.  The fast exact checker confirms that all `2097152` labelled
  even graphs on `8` vertices have such a partition:
  `/tmp/universal_slots_fast --n 8 --candidates 0,0,2,2`.  Additional focused
  random exact-cover checks found no counterexample in `100` even graphs on
  `18` vertices (`seed=200022`) and `25` even graphs on `20` vertices
  (`seed=200020`).  The stronger three-slot shortcut `(0,2,2)` is false:
  the `7`-vertex bowtie mask `148580` (two triangles sharing a vertex plus
  two isolates, edge set `03,06,12,16,26,36`) has no `(0,2,2)` partition but
  does have a `(0,0,2,2)` partition.  Thus the two zero slots are genuinely
  needed in this clean even-source route.
- 2026-05-31: Extended `universal_slots_fast.cpp` with `--degree-parity 0|1`
  and completed the exact odd-degree `n=8` four-slot sweep.  The nine
  surviving multisets are `(0,0,0,0)`, `(0,0,0,1)`, `(0,0,0,2)`,
  `(0,0,1,1)`, `(0,0,1,2)`, `(0,0,2,2)`, `(0,0,2,3)`, `(0,1,1,1)`, and
  `(0,1,1,2)`.  Thus `(0,0,2,2)` survives both parity source classes through
  the exact `n=8` first-lift checks, even though the clean odd-source slots
  `(0,1,2,3)` are killed.  Focused odd-degree random checks also found no
  `(0,0,2,2)` counterexample in `50` samples on `18` vertices (`seed=2181`)
  or `20` samples on `20` vertices (`seed=2201`).  The odd tree mask `9954`
  that kills `(0,1,2,3)` has a two-part zero-residue `(0,0,2,2)` certificate.
- 2026-05-31: Added `--odd-parts` to `universal_slots_fast.cpp` to test the
  complement reduction from odd-degree graphs to even-degree graphs.  The
  reduction is false: `K_{2,6}` (mask `220336191`, edge set
  `01,02,03,04,05,06,17,27,37,47,57,67`) has a `(0,0,2,2)` partition but no
  `(0,0,2,2)` partition with all nonempty parts odd.  In `K_{2,6}`, every
  odd-order even-residue modular part is an independent zero-residue part,
  leaving only two usable zero slots for two even-sized bipartition classes.
- 2026-05-31: Checked the complete multipartite count model for the common
  first-lift slots `(0,0,2,2)` across both parity source classes.  With up to
  `5` classes and class size at most `10`, `multipartite_modular.py --slots
  0,0,2,2` checked `502` parity-modular size vectors with no counterexample;
  source-residue filters checked `417` source-`0` vectors and `85` source-`1`
  vectors, also with no counterexample.  An attempted eight-class size-`12`
  run was stopped for cost and is not evidence.
- 2026-05-31: Added `--force-residue` to `slot_partition.py` and recorded the
  exact two-cut sign form for `(0,0,2,2)`: choose a first split `X,Y`, then
  cut `G[X]` into two `0 mod 4` parts and `G[Y]` into two `2 mod 4` parts;
  a two-part target-`t` cut is equivalent to
  `x_v sum_{u in N(v)} x_u == 2t-deg(v) mod 8`.  The rooted zero-slot
  strengthening is false: the triangle plus four isolates, mask `1057`, has
  a `(0,0,2,2)` partition, but a specified triangle vertex cannot be forced
  into a zero-residue part.  Thus cut-vertex induction for this clean slot
  target needs a richer boundary signature.
- 2026-05-31: Added `clean_slot_split.py` to test fixed first-split rules in
  the two-cut form.  The local degree-high-bit rule fails immediately.  For
  odd source parity, `K_{1,7}` (mask `220336192`) puts only the center in the
  residue-`2` side, impossible for a singleton, although the graph has a
  two-zero-slot certificate.  For even source parity, the graph
  `01,02,03,06,16,26,36` (mask `148519`) has degree sequence
  `4,2,2,2,0,0,4`; the degree rule chooses the independent set `{1,2,3}` as
  the residue-`2` side, but a valid certificate instead uses the triangle
  `{0,3,6}`.  Therefore the first split cannot be a pointwise function of
  degree modulo `4`.
- 2026-05-31: The common first-lift slots do not generalize naively to
  `(0,0,q,q)` at higher dyadic levels.  In the complete multipartite model,
  `(0,0,4,4)` for the `4 -> 8` lift is killed by class sizes `(1,1,1)` in
  source residue `2`, `(1,1,1,1)` in source residue `3`, and
  `(3,3,3,3)` in source residue `1`; only source residue `0` survived the
  bounded five-class size-`8` check.  This reinforces that higher lifts need
  genuinely source-sensitive slots, even if `(0,0,2,2)` works for both
  parity source classes at the first lift.
- 2026-05-31: Added `--max-weight` to `trace_multiset_bound.py` and recorded
  Corollary 15C: if every trace difference in a minimal repeated-degree host
  is supported on one coordinate, then `|B|<=(k-1)^2`.  The reason is that
  `+e_j` and `-e_j` cannot both occur, since the pair would be a balanced
  deletion; hence the coordinate-wise cancellation mass in Lemma 15B is zero.
  Exact bounded searches with singleton supports and graphical compensation
  complete for `d=3,4`, finding best sizes `6` and `12` under caps, consistent
  with the quadratic bound.  Weight-`2` support searches already hit the
  subset-sum cap quickly, so the remaining trace obstruction is genuinely a
  mixed-sign support-hypergraph problem.
- 2026-05-31: Added Lemma 15D for the next trace layer.  If every trace
  difference has support size exactly `2`, the signed traces form a red/blue
  multigraph on the repeated-degree coordinates; a balanced deletion is
  exactly an alternating closed trail.  Thus the first nontrivial support
  layer of the trace route reduces to bounding two-colored multigraphs with
  small red-blue degree imbalance and no alternating closed trail.
- 2026-05-31: Upgraded the support-size-`2` trace layer to a polynomial
  bound.  Convert the red/blue multigraph with no alternating closed trail
  into an acyclic directed multigraph on the `2d` color-states
  `(coordinate,next color)`.  Each state has imbalance at most `d` by Lemma
  15, so decomposing the DAG into source-sink paths of length at most
  `2d-1` gives at most `(2d-1)d^2` directed arcs, hence fewer than `d^3`
  support-size-`2` trace vectors.  Therefore any superpolynomial trace
  obstruction must involve supports of size at least `3` or nontrivial mixing
  between support sizes.
- 2026-05-31: Mixed support-size `1/2` trace searches are still hard.  With
  `d=3`, `--max-weight 2`, and multiplicity cap `4`, the bounded search hit
  the `100000` node cap with a size-`13` zero-sum-free example of total
  `(0,3,-3)` using both pair supports and singleton compensators:
  `4*(1,1,0), 3*(0,-1,-1), 2*(0,1,0), 4*(-1,0,0)`.  This is not a validated
  extremal obstruction, but it confirms that the mixed support case is not
  captured by the pure singleton and pure pair lemmas.
- 2026-05-31: Added Corollary 15F for one easy mixed support case.  If all
  singleton trace differences have the same sign and every coordinate touched
  by a pair trace has such a singleton available, then opposite-sign pair
  traces are forbidden by a three-vector zero sum; all remaining traces have
  one sign, so Lemma 15B gives `|B|<=d^2`.  Thus a large support-`<=2`
  obstruction must use singleton traces of both signs or pair traces touching
  coordinates not covered by a singleton of the global sign.
- 2026-05-31: Added Lemma 15G, the exact mixed support-`<=2` graph model.
  Singleton traces are colored half-edges and pair traces are colored ordinary
  edges.  A balanced deletion is equivalent to either an alternating closed
  trail of ordinary edges or an alternating trail whose two ends are
  half-edges.  The remaining support-`<=2` trace problem is therefore to
  bound colored graphs with half-edges, small red-blue degree imbalance at
  every coordinate, and no such alternating trail.
- 2026-06-01: Repaired the support-`<=2` trace layer proof in Corollary 15H
  by an alternating-trail digraph argument.  The ordinary support-two traces
  form an acyclic state digraph; singleton traces are added as half-edge arcs
  after deleting at most one exceptional copy of each half-edge type.  The
  augmented acyclic digraph has state imbalance `O(d)`, so path decomposition
  gives `|B|<=4d^3`.  Thus any superpolynomial trace obstruction in the
  repeated-degree route must use trace supports of size at least `3`.
- 2026-06-01: Audited the separator step that had been used for Corollary
  15H and Lemma 18A.  Deletion-minimality forbids only `0/1` zero
  subfamilies and does not imply cone separation: `separator_gap.py` verifies
  that `e_1, -1_{1,2}, -1_{1,3}, 1_{2,3}` has no zero subfamily but satisfies
  the positive dependence `2e_1-1_{1,2}-1_{1,3}+1_{2,3}=0`.  Lemma 18A is now
  explicitly conditional on a strict separator; the support-`<=2` proof no
  longer uses one.
- 2026-06-01: Recast Lemma 18A as a conditional bounded-support separator
  bound.
  If every trace difference has support size at most `s` and the trace
  multiset admits a strict separator, a basic feasible solution plus
  Hadamard's determinant bound gives an integer separator with
  `||a||_1<=d s^{d/2}`, hence `|B|<=d^2 s^{d/2}` by Lemma 18.  For fixed
  `s>=3` this remains exponential in `d`, so support `3` is the first layer
  requiring a new cancellation argument rather than determinant bounds.
- 2026-06-01: Added Example 18B and `support3_separator.py`.  There are
  support-`3` signed-indicator systems with total imbalance at most `2` that
  are zero-sum-free but force every integer separator to have Fibonacci-size
  coefficients.  This is only a trace-cone calibration, not a graph-host
  obstruction, but it rules out proving the support-`3` layer by a uniform
  small-separator theorem alone.  Next target: use graphical compensation or
  multiplicity constraints from the repeated-degree host to get cancellation
  beyond what the abstract cone sees.
- 2026-06-01: Strengthened the support-`3` calibration with Example 18C.
  The same vector types admit Fibonacci-size multiplicities with total vector
  supported on a single coordinate of value `-1`; the multiset is still
  zero-sum-free by the strict separator and it satisfies graphical
  compensation by a degree sequence with one degree-`2` vertex and the rest
  degree `1`.  Lemma 16A realizes any graphically compensated zero-sum-free
  trace multiset as an actual minimal repeated-degree host, so this support-3
  packing is not merely formal.  Since the realization can make `B`
  independent, it is not a counterexample to Problem 82; instead it shows
  that the repeated-degree route must exploit regular subgraphs in `B` or
  another property not visible in the trace multiset.
- 2026-06-01: Added Lemma 25 and `degree_variance_identity.py`.  Summing the
  squared degree variance over all `h`-sets expands exactly into a degree
  spread term plus a neighborhood symmetric-difference term.  Therefore any
  counterexample with small degree spread must have large aggregate
  neighborhood diversity.  This gives a possible bridge between bounded-spread
  and Ramsey-core methods, and also warns that bounded-spread alone is
  unlikely to be enough without handling random-like pair diversity.
