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
- `search_modular_partition.py`: local search over even graphs, using
  triangle flips to preserve parity, for examples with high first-lift modular
  partition color number.
- `color_modular_partition.py`: local search directly over fixed-color
  assignments, scoring residue disagreement inside color classes; includes a
  bounded Hamming repair step for near-miss colorings and a full-modular
  sampling mode for higher dyadic lifts.
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
  valid subsets by residue and pivot vertex for larger sampled checks.
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
- `multipartite_modular.py`: exact integer model for dyadic modular
  partitions of complete multipartite graphs.  The default mode uses the
  direct residue-grouping certificate; `--exact` computes minimum bin counts
  for small instances.  With `--slots`, it checks fixed target residue slots
  such as `(0,0,1,2)` using partial counts from multipartite classes.
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
  total-imbalance condition, optionally also requiring graphical compensation
  by the internal graph on the repeated-degree class.
- `trace_multiset_bound.py`: bounded multiplicity search for zero-sum-free
  trace multisets with small total imbalance and optional graphical
  compensation; larger runs should use tight caps because subset-sum sets grow
  quickly.
