# Experiments

Computational checks and generated data for Erdos Problem 82.

- `regular_induced.py`: exhaustive, random, and fixed-mask checks for largest
  regular or modular induced subgraphs.
- `regular_bitset.py`: memory-light fixed-mask regular induced subgraph
  verifier for larger individual graphs, avoiding all-subset precomputation.
- `trace_bridge.py`: tests the degree-class bridge from repeated-degree data
  to regular induced subgraphs.
- `trace_merge_search.py`: searches the one-trace regular merge criterion
  from Lemma 14A.5, reporting regular subsets on the trace and nontrace sides
  whose degree or degree-deficit matches a regular trace-class witness.
- `trace_ramsey_bound.py`: compares the maximal-independent trace Ramsey
  bounds from Lemmas 14B and 14B.1 using the Erdos-Szekeres binomial proxy.
- `ramsey_sample.py`: compares largest homogeneous and regular induced
  subgraphs in random samples.
- `rectangle_cover.py`: exact checker for the Ferrers rectangle-covering
  formulation of complete multipartite capped modular packing, where one
  rectangle `(r^h)` subtracts `r` from `h` classes and has area at most the
  cap.  Long exhaustive sweeps can use `--progress-every`.
- `full_bin_cover.py`: exact checker for the full complete-multipartite
  capped bin model with rectangles plus special `(q+1,1)` bins.  This is the
  arithmetic target that remains after the rectangle-only theorem is refuted.
- `equitable_partition.py`: computes color-refinement/equitable-partition
  cells and the regular-subgraph certificate from the largest cell.
- `degree_spread.py`: filters or samples graphs with bounded degree spread or
  few degree values to test additive near-regularity as a bridge; also verifies
  recorded graph masks with `--mask`.
- `compensated_spread.py`: generates the compensated-double spread-one
  template from Lemma 11B, putting a random base graph on one side, its
  complement on the other, and a bipartite graph with complementary degree
  prescriptions between them.  The default base density is `1/2`, matching
  the degree-sum condition `m(m-1)-4e(F) in [0,m]`.
- `compensated_spread_fast.py`: samples the same template but uses
  `regular_bitset.py` for memory-light fixed-mask verification on larger
  orders.
- `compensated_template_check.py`: verifies a fixed compensated-double
  template mask, reports the base and cross degree prescriptions, and prints
  the profile equations of Lemma 11E for a supplied witness.
- `defect_set.py`: checks the one-defect sufficient condition for the
  `(0,0,1,2)` first-lift slot target, where a residue-`2` part leaves a
  zero-residue complement.
- `search_bounded_spread.py`: local search for bounded-spread graphs with
  unusually small largest regular induced subgraphs.
- `modular_lift.py`: exact parity-graph enumeration and sampling for the
  first dyadic modular lift from parity-modular to `4`-modular witnesses.
- `search_modular_lift.py`: heuristic local search among parity-modular graphs
  for examples with small largest `4`-modular induced subgraphs.
- `modular_partition.py`: brute-force fixed-mask checks for partitions into a
  bounded number of modular induced parts, with parity enumeration/sampling
  modes, full-modular enumeration/sampling modes, size constraints, and an
  optional residue filter; it can also find the minimum working color count
  for a fixed mask up to a specified cap, print partition diagnostics, and
  produce exhaustive parity minimum-color histograms for small `n`.
  Full dyadic-modulus sampling recursively conditions on the previous dyadic
  modulus to improve acceptance; long heuristic runs can use `--node-limit`
  to skip hard exact-cover instances without certifying counterexamples.
  When `--max-part-size` is active, the exact-cover recursion indexes allowed
  modular subsets by pivot vertex rather than enumerating all submasks.
  `--connected-only` filters full-modular samples to connected source graphs,
  which is useful for testing the connected coarse-lift reduction.
- `modular_oct.py`: checks the modular odd-cycle-transversal candidate for
  even graphs: colors `A,B` must be independent, color `C` must have internal
  degree `1 mod 4`, and color `D` internal degree `2 mod 4`.  This stronger
  certificate implies the `(0,0,1,2)` first-lift slot target.  `--root` or
  `--all-roots` tests the rooted variant where specified vertices must remain
  in the bipartite residual.
- `first_lift_chromatic.py`: tests the chromatic pruning lemma for the first
  dyadic lift by sampling or enumerating even graphs, filtering for
  `chi(G),chi(complement(G)) >= 5`, and then running the exact four-part
  `4`-modular partition check.  It can also inspect a fixed mask with
  `--mask`.
- `search_modular_partition.py`: local search over even graphs, using
  triangle flips to preserve parity, for examples with high first-lift modular
  partition color number.  Node-limited exact searches are reported as
  unknown rather than as counterexample certificates.  It also accepts
  `--min-part-size` and `--max-part-size` to test size-controlled modular
  partition targets, and `--unrestricted` switches to all graphs with
  single-edge flips.  Merge-restart fallback is only used when no size
  constraint is active.
- `color_modular_partition.py`: local search directly over fixed-color
  assignments, scoring residue disagreement inside color classes; includes a
  bounded Hamming repair step for near-miss colorings and a full-modular
  sampling mode for higher dyadic lifts.  `--max-part-size` adds a size-excess
  penalty so score zero means the coloring is both modular and capped.
- `capped_modular_partition.py`: exact-cover checker for capped modular
  partitions that enumerates only subsets up to `--max-part-size`, avoiding
  the `2^n` subset table used by `modular_partition.py`; includes
  `--sample-random` for unrestricted capped checks such as `n=25,q=5`.
  `--on-the-fly` generates candidate parts only for the current pivot vertex,
  which is much faster for random large capped searches.
- `cycle_block_signature.py`: enumerates finite signatures of cycle blocks
  for cactus-graph self-labelled mod-`4` coloring tests, recording marked
  articulation labels and their same-labelled degree contributions from the
  cycle.
- `cactus_signature_dp.py`: solves the cycle-block signature constraint
  problem on generated or specified cycle cacti using the block-cut tree,
  allowing much larger cactus tests than direct subset partition search.
- `cactus_modular_dp.py`: analogous cycle-cactus DP for ordinary
  residue-flexible modular partitions with a fixed number of colors and
  global residues; useful for comparing against the stricter self-labelled
  signatures.
- `slot_partition.py`: exact checker for partitions whose target-modular
  part residues must fit a prescribed residue-slot multiset, such as
  `{0,1,2,3}` for the first lift from even graphs to `4`-modular parts; it
  also checks the equivalent self-labelled form `deg_same(v) == label(v)` and
  supports even-graph or unrestricted random sampling, plus exhaustive
  Eulerian-graph checks for small `n`.  With slots `0,0,1,2`,
  `--diagnostics` prints the residue-`1` and residue-`2` sets and the residual
  cut-congruence rows from Lemma 4I.6.  `--residue-one-matching` additionally
  requires every residue-`1` part modulo `4` to be exactly `1`-regular.
  `--force-residue v:r` forces vertex `v` into some part of residue `r`; the
  option may be repeated.
- `matching_slot_search.py`: direct vertex-coloring backtracker for the
  stronger `(0,0,1,2)` first-lift target in which the residue-`1` color class
  must be an induced matching.  This is often faster than exact-cover subset
  enumeration on fixed hard masks and supports exhaustive even-graph prefixes
  with `--limit` plus per-instance `--node-limit`.  Use `--force-color v:c`
  to test rooted variants, e.g. forcing a specified root into a zero slot.
  Use `--good-edge u:v` to require the endpoints of an existing edge to be in
  a pattern that lifts across degree-`2` suppression.
- `matching_slot_fast.cpp`: C++ exact checker for the same matching-slot
  target on small even graphs.  It is intended to make the full labelled
  `n=8` even-graph sweep reproducible, and also supports `--good-edge u:v`
  for the edge-rooted degree-`2` suppression strengthening.  Use `--start`
  and `--limit` to split the free-edge bit range into reproducible chunks,
  and `--progress --progress-every N` for long runs.
- `slot_profile.py`: optimizes a fixed-slot partition by minimizing the number
  of vertices outside a chosen residue, useful for testing whether
  `(0,0,1,2)` first-lift partitions can be proved by a small-defect plus
  residual-cut argument.  `--sample-even` profiles random even graphs.
- `clean_slot_split.py`: tests fixed choices of the first split in the
  two-cut formulation of the clean `(0,0,2,2)` slots.  The `--degree-rule`
  mode puts a vertex in the residue-`2` side according to the high bit of its
  total degree after subtracting the common source parity.
- `universal_slots.py`: tests whether a fixed residue-slot multiset works for
  every even graph at the first lift, either exhaustively for small `n` or by
  random even-graph sampling at larger `n`.  Its exact-cover recursion indexes
  valid subsets by residue and pivot vertex for larger sampled checks.  It can
  also sample source-modular graphs for higher dyadic lifts, such as
  `4 -> 8`, with `--sample-source-modular`, and can restrict those samples to
  a fixed source degree residue with `--source-residue`.  For small `n`, use
  `--exhaustive-source-modular` for an exact fixed-source-residue sweep.  Use
  `--score-all` with `--sample-even` or `--sample-source-modular` to score all
  supplied candidate slot multisets on the same sampled graphs instead of
  discarding candidates after their first failure.
- `slot_obstruction_certificate.py`: verifies finite certificates showing
  that a list of source-residue graphs kills every fixed target residue-slot
  multiset with a prescribed slot count.
- `universal_slots_fast.cpp`: C++ exhaustive checker for the same fixed-slot
  question.  It is intended for the full labelled fixed-degree-parity sweep
  on `n=8`, where the Python exact-cover loop is too slow.  Use
  `--degree-parity 0` for even graphs and `--degree-parity 1` for odd-degree
  graphs.  The optional `--odd-parts` flag requires every nonempty part in
  the slot partition to have odd cardinality, useful for testing complement
  reductions.
- `slot_local_search.py`: simulated-annealing heuristic for fixed residue-slot
  colorings.  It directly scores a coloring against prescribed residues and
  is useful for larger exploratory searches where exact slot DP is too slow;
  nonzero scores are not counterexample certificates.
- `self4_upper_bit.py`: for a fixed high-bit labeling in a candidate
  self-labelled mod-`4` coloring, solves the guaranteed lower-bit linear
  system and checks whether any low-bit solution also satisfies the upper-bit
  equations.
- `disjoint_signature.py`: computes all residue signatures of bounded modular
  partitions of small components and tests whether disjoint unions can align
  component signatures into a common set of global residue slots.
- `parity_split.py`: exact `F_2` linear algebra for bipartitions of even
  graphs where same-color internal degree parity is constant on each side.
- `hierarchical_lift.py`: tests a structured first-lift strategy: choose a
  parity-pattern bipartition, then split each side into two target-modular
  parts.
- `hier_self_label.py`: tests the stronger bootstrapping route where the
  first bipartition is specifically self-labelled modulo `2`, then the even
  side is split into residues `{0,2}` and the odd side into `{1,3}` modulo
  `4`; the two residue pairs can be overridden to test nearby hierarchical
  slot routes.
- `merge_modular_partition.py`: greedy compression heuristic that starts from
  singleton modular parts and repeatedly merges pairs whose union remains
  modular; useful for testing whether bounded modular partitions might have a
  merge/absorption proof.
- `decomposable_partition.py`: exact dynamic program for the stronger notion
  of merge-decomposable modular parts, comparing the minimum ordinary modular
  partition with the minimum partition into parts buildable by modular merges;
  includes a parity-sampling mode for finding gaps between the two parameters.
- `modular_spectrum.py`: checks which exact sizes occur as modular induced
  subgraphs and searches for gaps in the spectrum.
- `weighted_blowup.py`: searches for weighted exact-terminal witnesses in
  regular twin blowups.  For a base graph `B`, cap `L`, and target `T`, it
  looks for integer vectors `0<=x_i<=L`, `sum x_i=T`, such that
  `(A_B x)_i` is constant over the support of `x`.  This is the finite
  hard-core model for terminal dyadic lifts in regular twin blowups.
- `regular_terminal_sample.py`: samples switched circulant regular graphs on
  `q^2` vertices and checks, by fixed-size subset enumeration, whether they
  contain a regular induced subgraph on exactly `2q` vertices.
- `q_modular_host_sample.py`: samples full `q`-modular host graphs and
  measures their largest regular induced subgraph and largest induced
  target-modular subgraph, testing the tradeoff in witness-or-regular
  dichotomy targets.  Use `--exhaustive` for small labelled sweeps and
  `--target-modulus` to override the default target `2q`.
- `two_level_modular_sample.py`: generates connected graphs with two prescribed
  degree levels `d` and `d+q`, randomizes them by degree-preserving swaps, and
  measures the largest induced `2q`-modular witness.  This stress-tests dyadic
  witness conjectures on dense `q`-modular graphs that are usually not already
  `2q`-modular.  Use `--on-the-fly` to avoid the exponential incident-table
  precompute and scan larger exact subset spaces.  Use `--measure-regular` to
  measure the largest regular induced subgraph in the same samples, which is
  useful for testing witness-or-regular dichotomy targets.
- `multipartite_modular.py`: exact integer model for modular
  partitions of complete multipartite graphs.  The default mode uses the
  direct residue-grouping certificate; `--exact` computes minimum bin counts
  for small instances.  With `--slots`, it checks fixed target residue slots
  such as `(0,0,1,2)` using partial counts from multipartite classes;
  `--source-residue` restricts this fixed-slot mode to one source degree
  residue class modulo `--source-modulus`.
  `--max-bin-size` adds terminal-size caps, `--max-total-size` bounds the
  generated search space by total graph order, and `--sizes` verifies a fixed
  complete multipartite instance such as the `K_{22,2,1}` strict-terminal
  obstruction.  Add `--print-partition` with `--sizes` to print one minimum
  bin packing certificate.
- `source_slot_finder.py`: enumerates source-residue fixed slot multisets and
  filters them through the complete multipartite integer model.  It applies
  the dyadic clique subset-sum test by default, then keeps only slot families
  that partition all generated source-residue multipartite size vectors.  Its
  checker generates only legal modular bins, and when all class sizes are at
  most the target modulus it canonicalizes by sorted remaining capacities, so
  it is faster than the general product-count DP in `multipartite_modular.py`
  on larger class counts.  Use `--candidates` for targeted checks of
  semicolon-separated residue multisets.
- `twin_blowup_modular.py`: exact weighted congruence model for graphs with a
  bounded number of twin classes, allowing each class to be a clique or an
  independent set and each pair of classes to be complete or empty.
- `twin_self_label.py`: exact count-model search for self-labelled modular
  colorings in bounded twin-class quotients, useful for testing blow-ups of
  small obstructions without expanding all twin vertices.
- `trace_zero_sum.py`: brute force for distinct trace-vector families with no
  balanced subfamily in the minimal repeated-degree host obstruction.
- `trace_balance_bound.py`: brute force for distinct trace families that have
  no balanced subfamily even after imposing the repeated-degree host's small
  total-imbalance condition, optionally using the exact spread condition on
  all `k` trace coordinates and optionally requiring graphical compensation by
  the internal graph on the repeated-degree class.
- `trace_multiset_bound.py`: bounded multiplicity search for zero-sum-free
  trace multisets with small total imbalance and optional graphical
  compensation; `--trace-cone` restricts the support to the actual signed
  indicator vectors arising from graph traces relative to a base vertex and
  reports the incidence, cancellation mass, and L1 imbalance from Lemma 15B.
  `--max-weight W` restricts trace-difference supports to size at most `W`.
  Larger runs should use tight caps because subset-sum sets grow quickly.
- `support3_separator.py`: verifies the support-`3` signed-indicator systems
  from Examples 18B and 18C, including support sizes, total imbalance, the
  explicit strict separator, Fibonacci separator lower bounds, exponential
  bounded-imbalance multiplicities, and graphical compensation.
- `separator_gap.py`: verifies the four-vector support-`<=2` example showing
  that deletion-minimality, which forbids only `0/1` zero subfamilies, does
  not imply the strict cone separation used in conditional separator bounds.
- `degree_variance_identity.py`: verifies the pair-expanded identity for the
  total squared degree variance over all `h`-vertex induced subgraphs.  This
  supports the diversity-counting route in Lemma 25.
- `edge_perturbation_witness.py`: inspects regular induced witnesses created
  by adding a missing edge or deleting an existing edge, supporting the
  edge-extremal defect-witness lemma.
- `edge_saturate.py`: greedily adds or deletes edges while preserving absence
  of a threshold-size regular induced subgraph, producing small edge-maximal
  or edge-minimal examples for perturbation checks.
- `pair_difference_template.py`: searches the two-pole amplification template
  from Lemma 27, where equal-sized homogeneous subsets of
  `N(u)\N(v)` and `N(v)\N(u)` combine with `u,v` to form a regular induced
  subgraph.
- `balanced_pair_extension.py`: searches the broader Lemma 27A criterion,
  where equal-sized one-sided difference subsets only need to induce the
  required regular graph between themselves, not a homogeneous template.
- `pair_defect_witness.py`: checks the two-defect pair-role equations from
  Lemma 27H for near-regular witnesses created by edge perturbations.
- `pair_role_witness.py`: prints the exact four-role pair profile equations
  from Lemma 27C for a supplied regular witness and optional pair.
- `pair_role_signature.py`: scans largest regular witnesses for the number
  and sizes of nonempty pair roles, with an option to generate Paley graphs.
- `regular_witness.py`: prints one largest regular induced witness for a
  fixed graph mask, including degrees, witness edges, and optional split-side
  counts/profiles for structured examples.
- `profile_absorption_search.py`: searches across a prescribed cut for a
  largest regular witness satisfying the split profile equations of Lemma 30,
  reporting the internal-plus-cross degree profiles on each side.
