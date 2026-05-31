# Experiments

Computational checks and generated data for Erdos Problem 82.

- `regular_induced.py`: exhaustive, random, and fixed-mask checks for largest
  regular or modular induced subgraphs.
- `trace_bridge.py`: tests the degree-class bridge from repeated-degree data
  to regular induced subgraphs.
- `ramsey_sample.py`: compares largest homogeneous and regular induced
  subgraphs in random samples.
- `equitable_partition.py`: computes color-refinement/equitable-partition
  cells and the regular-subgraph certificate from the largest cell.
- `degree_spread.py`: filters or samples graphs with bounded degree spread or
  few degree values to test additive near-regularity as a bridge; also verifies
  recorded graph masks with `--mask`.
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
- `first_lift_chromatic.py`: tests the chromatic pruning lemma for the first
  dyadic lift by sampling or enumerating even graphs, filtering for
  `chi(G),chi(complement(G)) >= 5`, and then running the exact four-part
  `4`-modular partition check.
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
  Eulerian-graph checks for small `n`.
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
  question.  It is intended for the full labelled even-graph sweep on `n=8`,
  where the Python exact-cover loop is too slow.
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
- `multipartite_modular.py`: exact integer model for modular
  partitions of complete multipartite graphs.  The default mode uses the
  direct residue-grouping certificate; `--exact` computes minimum bin counts
  for small instances.  With `--slots`, it checks fixed target residue slots
  such as `(0,0,1,2)` using partial counts from multipartite classes.
  `--max-bin-size` adds terminal-size caps, `--max-total-size` bounds the
  generated search space by total graph order, and `--sizes` verifies a fixed
  complete multipartite instance such as the `K_{22,2,1}` strict-terminal
  obstruction.
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
  compensation; larger runs should use tight caps because subset-sum sets grow
  quickly.
