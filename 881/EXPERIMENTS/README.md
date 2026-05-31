# Experiments for Erdős Problem #881

Finite experiments here are only heuristic. They search for local analogues
of the two competing mechanisms:

* positive deletion: after deleting a sparse set, enough representations
  remain at one higher order;
* counterexample gadgets: every element has a private witness that cannot be
  repaired by adding one extra summand.

The current script `finite_gadgets.py` searches for small finite sets
\(T\subset[0,D]\) such that \(T+T=[0,2D]\) and each element of \(T\)
participates in at least one private two-sum. It also demonstrates the
mixed-radix product construction, starting from \(\{0,1,3,4\}\), that gives
arbitrarily large finite gadgets. These are candidate local building blocks
for \(k=2\) counterexample attempts, but an infinite block construction must
also control cross-block three-sum repairs.

`search_safe_gadgets.py` searches for a stronger local property: private
two-sums \(u\) for which \(u-e\notin T+T\) for a finite forbidden set of
earlier shifts \(e\). A sample run with forbidden set `{1}` finds
`T=[0,4,8,10,13,15,20]`, whose two-sum set contains the interval `[12,21]`
and whose elements all have `{1}`-safe private sums.

`cyclic_minimal_deletions.py` checks a finite cyclic analogue: minimal
2-bases in \(\mathbb Z/m\mathbb Z\) and whether some one-point deletion is
a 3-basis. The output is mixed; this is a warning that finite residue
models alone cannot prove the asymptotic statement.

`random_one_point_deletion.py` samples finite interval sets \(A\subset[1,N]\)
whose two-sums cover a tail and then checks one-point deletion at order 3 on
the same finite tail. It often finds examples where every deletion fails on
that finite window. These are finite-threshold artefacts, not counterexamples:
an infinite order-3 basis may require a larger threshold after deletion.

`efficient_block_search.py` searches for finite interval blocks whose
two-sums cover a long interval and whose elements have order-3 witnesses
safe against a prescribed finite set of earlier shifts. It is aimed at the
block-counterexample route; failures here are heuristic evidence for the
coverage-efficiency obstruction, not proof.

`cyclic_barriers.py` checks a finite residue analogue of the barrier
counterexample target: residue 2-bases \(S\) such that deleting any pair
of residues destroys 3-basis status. Such examples are plentiful in small
cyclic groups, but lifting them to integer element deletions is the hard
part.

`rep_hypergraph_stats.py` computes finite representation-hypergraph edge
counts, maximum degrees, and greedy matching sizes for sample models. It is
meant to sanity-check the matching criterion in Proposition 3.4.

`delayed_gap_sim.py` is a toy finite-window simulation for the delayed-gap
mechanism: after deleting one element, it estimates the first tail point
where order-3 coverage resumes. Large threshold/deleted-element ratios are
finite analogues of the threshold-control obstruction in Warning 3.0.

`stage_buffer_search.py` searches directly for small finite stages of the
Proposition 13.1 type that also leave two-sum coverage beyond the declared
endpoint. That extra buffer is necessary if the stage is to be iterated,
because the next stage's new elements must be larger than the previous
declared endpoint. The current version also filters out the lowest
padding-range artefacts by requiring the candidate witness to remain above
the old two-sum coverage base after subtracting the least retained old
element.

`collective_barrier_search.py` searches for finite windows where all
one-point deletions preserve order-3 coverage on the window, but some pair
deletions create holes. This models the remaining \(k=2\) finitely-bad
case, where any obstruction must be genuinely collective rather than
one-point.

`collective_rank_search.py` searches the same finite-window analogue at a
chosen rank. With `--rank 3`, the first small example is
\[
A=\{1,2,3,4,5,6,8,9\}
\]
on the window \([9,18]\), which is inside the two-sum coverage interval:
every singleton and pair deletion still covers the window at order \(3\),
but several triple deletions create holes. The `--allow-uncovered` flag
also reports endpoint artefacts beyond the two-sum coverage range.
With `--rank 4 --max-value 14 --max-size 10 --window 12`, the first small
example is
\[
A=\{1,2,3,4,5,6,8,9,10,11\}
\]
on the window \([12,22]\), again inside the two-sum coverage interval:
all deletions of size \(<4\) preserve order-3 coverage on the test window,
while several four-point deletions create holes.

`finite_barrier_hypergraph.py` builds the finite residue hypergraph of
deletions \(F\subset S\) for which \((k+1)(S\setminus F)\) is not the whole
group. The default run reports the minimal pair barrier
\(\{0,2\},\{1,3\}\) on \(S=\mathbb Z/4\mathbb Z\). With `--rank3`, it
finds the complete rank-3 barrier on \(S=\mathbb Z/5\mathbb Z\): singleton
and pair deletions are harmless, but every triple deletion is bad. This is
a finite residue model of the high-rank barrier obstruction isolated by
Reduction 0.

`two_center_residue.py` verifies the residue example
\(\{0,1,2,4\}\subset\mathbb Z/7\mathbb Z\): it is a 2-basis, all singleton
deletions remain 3-bases, but deleting \(\{0,1\}\) creates a 3-sum hole
whose reflected-cover obstruction genuinely needs two centers. It also
checks the complete pair-barrier example
\(\{0,1,2,3\}\subset\mathbb Z/5\mathbb Z\) from Example 8.7b and the
finite-center incoherence example from Example 8.8, where every deleted
pattern is repairable by some retained center but no single center works
coherently.
It also checks the \(\mathbb Z/13\mathbb Z\) model from Example 8.7e, where
a certificate-free three-point set supports complete inclusion-minimal pair
holes.

`certificate_free_stats.py` computes the largest certificate-free subset in
several finite integer-window examples. This is a diagnostic for Lemma
8.6g: fixed-rank large-excess barriers can persist only if every finite
test set has a large certificate-free subset.

`schreier_stage_search.py` looks for the first finite analogue of the
Schreier-stage criterion. It finds
\[
A=\{1,2,3,4,8\},
\]
whose two-sums cover through \(12\), and whose first protected Schreier
edges \(\{1,2\},\{1,3\},\{1,4\},\{2,3,4\}\) have minimal dominated
three-fold holes at \(6,7,10,12\), respectively. This is only a local
gadget and does not address iteration.
With `--extend-first --max-new 5 --max-candidate 55`, it tries to add up to
five new elements through `55` and checks all Schreier edges among the first
five protected elements; no second-stage extension is found in that bounded
search.
The direct mode can also search for more protected points. With
`--protected-count 6 --max-value 17 --max-size 9`, it finds
\(\{1,2,4,5,6,8,14,16,17\}\), with all twelve Schreier edges among the
first six protected points carrying minimal dominated holes.
The `--min-protected` option forces the protected Schreier points away from
the small coverage core. With
`--protected-count 4 --min-protected 10 --max-value 30 --max-size 10`, the
script finds \(\{1,2,4,5,8,10,15,18,19\}\), protected tail
\(\{10,15,18,19\}\), and coverage through \(30\).
The `--tail-chain` mode records the extension obtained by adding `30`,
then checks all sixth protected points up to `120` with up to three extra
fillers through `151`; it finds no P6 extension in that bounded search.

`cross_stage_pair_search.py` searches for local stages satisfying the
cross-stage pair-barrier criterion in Proposition 13.1c. It finds a short
initial chain but stalls quickly in the default bounded greedy search,
highlighting how demanding it is to protect every old-new pair while
continuing two-sum coverage. The default search additionally requires the
declared endpoint to be at least the largest new element; this filters for
genuinely local pair witnesses and is stronger than the proposition, which
would also allow dormant new elements above the declared endpoint.

`cross_stage_pair_dfs.py` performs a bounded depth-first search for the same
criterion, so early greedy choices can be revisited. With its default small
parameters it finds a non-greedy three-stage chain
\[
\{1,2\}\to\{1,2,4\}\to\{1,2,4,6,7\}\to\{1,2,4,6,7,8\},
\]
with endpoints \(4,7,15\), but no fourth stage in that bounded search.
Thus the two-stage greedy stall was not conclusive; the next obstruction is
simultaneous protection after several old elements are present.
The `--minimal` flag requires each old-new pair hole to be repaired when
either endpoint is restored. Under the same default bounds it finds only
one stage,
\[
\{1,2\}\to\{1,2,4,5\},
\]
with endpoint \(9\), and no second stage.

`reflection_certificate_verify.py` instantiates the balanced-certificate
construction from Theorem 2.3 in the model \(A=\mathbb N\), and verifies
for small parameters that every deleted multiset of size at most \(k\) has
the required repair from the protected reservoir.

`adjacent_stage_search.py` tests a possible \(k=3\) disproof route:
constructing an order-3 basis that is ordinary minimal as an order-4 basis.
It searches finite stages where new elements extend three-sum coverage and
already have local four-sum private witnesses. The default greedy run finds
two endpoint-style stages and then stalls, reflecting the same buffer
obstruction seen in the \(k=2\) stage searches.
A separate bounded non-greedy DFS over increments of size at most `3`,
candidate values up to `100`, and a two-point buffer again found depth only
`2`; its best alternative chain starts with adding `{4,11}` and then
`{18,21}`.

`robust_booster_residue.py` searches cyclic residue models for a finite
booster that lowers the order while private residue holes survive with the
booster retained. It finds the \(k=3\) pattern
\(S=\{0,1,3\}\subset\mathbb Z/10\mathbb Z\), \(f=5\): \(4S\) and
\(3(S\cup\{f\})\) cover all residues, but deleting any residue of \(S\)
leaves a four-sum residue hole even with \(f\) available. This is only a
residue seed; an integer lift must still force single-integer, not
whole-residue-class, privacy.

`robust_booster_stage_search.py` tries to lift that residue seed to finite
integer stages with fixed booster \(5\) and mutable elements in residues
\(0,1,3\pmod {10}\). It finds one buffered stage
\(\{1,3,20,21\}\to\{1,3,20,21,30,31\}\), with witnesses \(37\) and \(38\)
after deleting \(30\) and \(31\), then stalls in the default greedy search.
Run it with `--extend` to reproduce a bounded second-stage check through
new elements up to `120` of size at most `5`, plus random larger increments;
that extended check also finds no continuation.

`robust_booster_pair_stage_search.py` tests the more plausible cross-stage
pair-barrier version of the same \(k=3\) seed. It finds two buffered stages,
first adding `23` and then adding `30,31`; every old-new pair has a local
four-sum witness. Its `--extend` mode checks the next stage through new
elements up to `160` of size at most `4`, plus random increments of sizes
`5` through `12`, and finds no continuation.
Run it with `--diagnose` to see the immediate obstruction: the only
residue-restricted singleton candidates that extend coverage are `41` and
`43`, and both fail the pair-witness condition against old elements
`1,3,21,23,31`.
A bounded non-greedy DFS with candidate values up to `110`, increments of
size at most `3`, and slack `100` also found no chain beyond depth `2`.
With wider first/second-stage enumeration, alternative first moves exist
but the branches tested still have no third extension.
