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

`actual_gap_barrier_search.py` searches for inclusion-minimal finite
deletions whose terminal forbidden interval is an actual gap of the finite
set, not merely a gap after the deletion. This models the finite-core
normal form in Corollary 10.3d and Lemmas 10.3e--10.3f.

`interval_barrier_family.py` probes the scalable interval block from
Proposition 10.3g. It enumerates subsets of the high interval \(J\) and
reports which ones have coverage-compatible terminal-gap witnesses. Sample
runs such as `--X 3 --M 8 --max-rank 4` and
`--X 5 --M 12 --max-rank 7` show that the first useful barriers occur at
roughly half the high block and that no pair deletions occur in the tested
coverage-compatible range. With `--no-coverage --witness-cap`, pair holes
do appear, but only as endpoint artefacts beyond the two-sum coverage
interval. Its `--verify-classification` mode exhaustively checks the
threshold-cut classification in Lemma 10.3h for a specified block.

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

`delayed_collective_barrier_search.py` searches for finite analogues of
Corollary 3.1e': all proper subdeletions have early finite order-3 tails,
but one inclusion-minimal collective deletion pushes the finite tail past
the deleted block. The first pair example is
\[
S=\{1,2,3,5,6,7\},\qquad F=\{5,7\},
\]
where the full deletion has minimal holes at `16,17` and finite tail only
from `18`, while the singleton subdeletions have finite tail from `3`.
With `--rank 3`, it finds
\[
S=\{1,2,3,4,5,6,7,8\},\qquad F=\{4,5,6\},
\]
with a minimal hole at `20` and tail from `21`.

`finite_barrier_hypergraph.py` builds the finite residue hypergraph of
deletions \(F\subset S\) for which \((k+1)(S\setminus F)\) is not the whole
group. The default run reports the minimal pair barrier
\(\{0,2\},\{1,3\}\) on \(S=\mathbb Z/4\mathbb Z\). With `--rank3`, it
finds the complete rank-3 barrier on \(S=\mathbb Z/5\mathbb Z\): singleton
and pair deletions are harmless, but every triple deletion is bad. This is
a finite residue model of the high-rank barrier obstruction isolated by
Reduction 0.

`front_barrier_diagnostics.py` checks finite shadows of the higher-front
warnings in `PROOF.md`. It verifies on a finite prefix that the
second-element front `m=x_2` has the expected initial-segment barrier
property for long finite sequences, and that no tested tail contains the
first-Schreier prefix-link family as a subbarrier. This is a combinatorial
sanity check for Warning 8.5a.1 and Lemma 8.5a.2, not an additive model.

`prefix_front_trace.py` checks the first-completion combinatorics behind
Lemmas 3.1c.1--3.1c.2. On finite weak families it verifies that every
barrier edge first completed by a prefix contains the prefix maximum, and
that any shrink omitting that maximum would already lie in the previous
prefix if it remained in the same late-bad family.

`mobile_injective_color_search.py` searches finite additive windows for
the mobile-injective private-color pattern from Warning 8.5a.7. It reports
small inclusion-minimal holes whose Lemma 8.4c row/color graph has a large
matching; the first examples are the parity interval blocks from Example
8.5a.7b, where retained even rows match distinct deleted odd colors. It
also verifies the range-separated packet from Warning 8.5a.7c, including
the fact that each moving color gates both an old row and its retained
mirror while the two-point fiber remains certificate-free. The final block
checks the parity interval examples: for ranks at least four the collective
odd deletion has a mobile-injective hole, but the high-window pair-link
graph has no universal first vertex, so Lemma 13.1j cannot start. It also
verifies the large one-color fiber packet from Example 8.5a.7g.

`fiber_palette_independence.py` checks the finite graph constraints behind
the current large-fiber reduction. On the bipartite six-point window
\(\{8,9,11,13,15,16\}\), it verifies that the unique rows for the gate
\(16\) are independent in the gate-difference graph \(u+16-v\in A\). It
also checks the shifted-overlap toy window \(\{1,2,3,10\}\), where rows
\(\{1,2\}\) with shift \(1\) fail shift-independence and therefore contain
the certificate \(1,2,2\). It also verifies the moving unique-gate packet
from Example 8.5a.7m, including the local hole, both repairs, private rows,
the unbounded reflection center \(m=w-f\), full uniqueness
\(r_{2,A}(u+f)=1\), gate-independence, and
certificate-freeness of \(U\). This supports Lemmas 8.5a.7i--8.5a.7l and
the local-compatibility warning in Example 8.5a.7m.

`selector_barrier_diagnostics.py` checks the finite product-cover condition
behind Corollary 8.5a.7r. Given disjoint packet blocks and proposed
cross-packet edges, it reports selectors choosing one vertex per block that
contain no edge. Local block cuts are uncovered, complete bipartite wiring
between two blocks covers every selector, and sparse wiring leaves explicit
escaping selectors. It also reports the first finite prefix that is already
product-covered, the relevant support sizes, and the selector-cylinder
cover weight \(\sum_G\prod_{j\in\sigma(G)}|F_j|^{-1}\), matching the
finite compactness target in Corollary 8.5a.7t and the union-bound pressure
in Lemma 8.5a.7u.

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

`pair_hole_residue_search.py` searches for the residue-level ingredients of
Example 8.7d: a background set `R`, two exceptional residues `x,y`, a
three-fold hole after deleting `x,y`, and two-center shifted domination. The
first pattern is already modulo `5`:
\[
R=\{0,1\},\qquad x=2,\qquad y=3,\qquad h=4.
\]
This is a local diagnostic only; an integer or staged lift must still stop
other old exceptional representatives from repairing the hole.
The same script prints the \(\mathbb Z/8\) translate-separation diagnostic
for \(R=\{0,1,4\}\): among four protected residues, translates of \(R\) can
separate at most four of the six pairs from all other protected residues,
so the residue pair-hole mechanism cannot support a complete pair system by
phase choices alone.

`certificate_free_stats.py` computes the largest certificate-free subset in
several finite integer-window examples. This is a diagnostic for Lemma
8.6g: fixed-rank large-excess barriers can persist only if every finite
test set has a large certificate-free subset. It also prints
`gamma=|A|/alpha_cert`, the rank threshold from the rank-sensitive
certificate discussion after Lemma 8.6g. The delayed pair window has
`gamma=3`, so it is a local delayed barrier but not a scalable rank-2
certificate-free obstruction.

`star_pair_search.py` searches for the fixed-center star obstruction from
Warning 8.2b. It finds the small window
\(\{1,2,3,4,7,10\}\), with two-sum coverage through \(14\), where center
`1` and old deleted element `3` make the spokes `4,7,10` fail the pair
repair at witnesses `8,11,14`. Restoring either endpoint repairs each
witness, so this is a genuine minimal pair-hole phenomenon for a fixed
prefix.
The same script also prints the finite prefix example
\(\{1,2,3,4,5,6,7\}\), where the star failure for
`D={4,6}`, `d=6`, and `b=7` is minimal only as a triple-prefix hole; it
does not descend to a pair hole after deleting `{6,7}`.

The alternating-deletion warning in `PROOF.md` uses another small window,
\(\{1,2,3,6,7,8\}\): deleting the non-consecutive pair `{6,8}` leaves a
three-sum hole at `14`, with the terminal interval containing only the
deleted point `8`, and the shifted two-sum domination still holds.

`private_sum_matrix.py` checks the extra necessary condition from Lemma
8.4c on this alternating-deletion window, on the first Schreier seed, and
on the P6 pair-edge escape. For each retained padder `e` below a hole
witness it prints which deleted elements `f` satisfy both
`w-e-f in C` and `e+f notin 2C`, except when `w-e` is already a
deleted-pair sum. It also prints `nu_f(e+f)`, the maximum number of
disjoint two-sum representations of `e+f` avoiding `f`, for the matching
capacity obstruction in Lemma 8.4d. The final block prints the
Corollary 3.4g/3.4h star-gate data: retained repairs `w-d=a+b` for each
deleted gate `d` and the full two-sum counts `r2(row+d)` for the bounded
translate rows forced by those repairs. It labels each row as `unique` or
as `overlap:f` according to the Corollary 3.4s branch.

`low_count_star_scan.py` scans finite windows for the Corollary 3.4n
normal form: triples with `d`, `a`, and `w-d-a` outside a protected core and
bounded full count `r2(a+d)`. It contrasts the pinned low-count stars in
`\{1\}\cup2\mathbb N` before and after protecting `1`, and prints the same
diagnostic on the P6 Schreier escape with and without its old core
protected. In the P6 pair-edge escape, the old-core-protected scan has no
fresh `Q=2` star, matching the theoretical point that a viable next stage
must create genuinely unpinned bounded-count rows, not only repairs through
old elements. It also prints the internal translated-Schur count for
`x+y=s+d` inside the displayed row set, corresponding to Corollary 3.4r.

`bridge_repair_search.py` checks the moving-anchor bridge identities from
Lemma 8.2a'. With `--examples`, it finds bridge data for the finite delayed
pair window
\[
S=\{1,2,3,5,6,7\},\qquad F=\{5,7\},
\]
namely `t=1` and rows `(5,3,3),(7,2,6)`. It finds no bridge data for the
rank-three delayed example or for the alternating-deletion pair hole, even
with `--all-orders`, so the bridge identity is a genuine positive mechanism
but not automatic. The same `--all-orders` mode does find unrelated
rank-three windows with bridge data, showing that rank alone is not the
failure. The named examples also include the first Schreier seed edge
`\{1,4\}`, the first Schreier seed triple `\{2,3,4\}`, the tail P5 pair
`\{10,30\}`, and the P6 pair-edge escape `\{10,38\}`; none has bridge data,
even after all deletion orderings are tried. Thus the moving-anchor bridge
route does not by itself break the remaining Schreier/P6 obstruction.

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
Lemma 13.1f in `PROOF.md` extracts a finite forbidden-window obstruction
from these runs. For the P5 seed, a low-excess witness for the new pair
edge `{10,p6}` must have `w-p6>=19`; enumerating the remaining low-excess
range leaves one pair-edge escape, `(p6,w)=(38,58)`, realized after adding
fillers `{40,43,44}`. That escape still fails the full P6 Schreier test
because the new higher-rank edges involving `38` have no compatible
witnesses. Thus the P6 stall is a simultaneous-closure obstruction, not
just a single pair-edge obstruction.
Run `schreier_stage_search.py --p6-pair-diagnostic` to reproduce this
low-excess pair-edge calculation and the protected-filler failure. The same
diagnostic now classifies first candidate failures as poisoned witnesses,
absorbed private-color rows, missing reflected rows, or missing
inclusion-minimal repairs. It also prints the exact protected-filler pair
intervals: after treating `40,43,44` as protected, each pair edge
`\{10,q\}` has every candidate witness in `[q,63]` already lying in
`3(A\setminus\{10,q\})`. The old retained endpoint `38` explains many of
these values but leaves shifted two-sum gaps; the full poisoning uses the
rest of the retained finite window.
Run `schreier_stage_search.py --p6-order-diagnostic` to test the delayed
enumeration variant on the same finite set. It tries all `6!` orders of the
vertices `10,15,18,19,30,38`, with fillers `40,43,44` present but not among
those six protected vertices. No order satisfies all Schreier edges; the
best orders still have three failed edges involving `38`. The prefix
constraints already explain the failure: the good-pair graph forces `10` to
be first, and after `10` no second vertex has all rank-three edges required
against the remaining tail. This is the finite instance of Lemma 13.1j's
complete-prefix-link criterion.
Run `schreier_stage_search.py --p6-enum-search --max-p6 80 --max-extra 1
--max-extra-value 120` for a bounded arbitrary-order extension search from
the P5 seed. It checks all \(p_6\le80\) with at most one delayed filler
through `120`, precomputing which protected subsets have witnesses and then
testing all enumeration orders. It finds no extension; after `p6=38`, no
candidate passes the coverage filter.
The same mode now uses Lemma 13.1j-style lazy prefix-link pruning. With
`--max-p6 55 --max-extra 2 --max-extra-value 95`, it checks `14912`
coverage-passing candidates with up to two delayed fillers and still finds
no arbitrary-order P6 extension.
A wider delayed-filler run,
`schreier_stage_search.py --p6-enum-search --max-p6 45 --max-extra 3
--max-extra-value 75`, checks `89702` coverage-passing candidates and also
finds no arbitrary-order P6 extension. After `p6=38`, no later candidate
passes the coverage filter under these bounds.
Run `bipartite_sidon_window_search.py --max-value 16 --size 6 --limit 10`
for a finite analogue of the bipartite recurrent-Sidon obstruction from
Corollary 13.1l.3. It finds many windows with two certificate-free colors,
a long two-sum coverage interval, and a mixed reflection spike. One top
example is `C={11,15,16}`, `D={8,9,13}`: `2(C∪D)` covers `[16,32]`, and
the mixed center `24` has the three representations
`11+13=15+9=16+8`. This shows the reduced obstruction is locally
compatible. The enhanced output also reports the minimum exact matching
sizes for the cross-residual graphs `C+C+D` and `D+D+C` across the covered
interval; the top interval examples have `(0,0)`, so they do not satisfy
the stronger matching criterion from Lemma 8.6j-7a.
With `--sort matching --max-value 20 --size 8`, the best windows still
have per-color minima `(0,0)` but `best_color_min=1`: for each target in
the covered interval at least one color has a cross-residual edge, yet no
single color supplies edges for the whole interval. This matches the
bounded-transversal/star obstruction rather than the sparse-deletion
matching branch.
The same output now includes `unique_star=(count,d,t,rows)`, the largest
reflected packet with `t-rows` retained and every shifted row `s+d`
uniquely represented in `2A`. The top six-point window has
`unique_star=(5,16,24,[9,11,13,15,16])`, showing that the remaining
unique-gate branch is also locally compatible.
Run `schreier_stage_search.py --pair-edge-search --max-p6 40 --max-u 60
--max-nodes 20000 --max-found 2` for the complementary high-excess
first-pair diagnostic. It looks for pair-private dominated holes for
`\{10,p\}` in the P5 seed while allowing witnesses `w=p+u` above the
low-excess range. It finds extensions at `(p,u,w)=(37,32,69)` with fillers
`{40,41,44,51,54,55,58}` and `(37,43,80)` with fillers
`{40,41,51,52,55,62,65,66,69}`. Both have the local pair witness, but the
core vertices `(10,15,18,19,30,37)` already have no supported order even
when the fillers are delayed: the failed edges are `(15,18,37)`,
`(15,19,37)`, `(15,30,37)`, and `(18,19,30,37)`. Treating the fillers as
protected adds more failures; in the first extension the lower endpoint
`10` has failed pair links to every filler. The rank-three core failures
are fully poisoned in the covered interval after deleting the edge, while
the rank-four edge has candidates that fail inclusion-minimal repair. This
is the finite version of the Corollary 13.1l pressure: high first-pair
excess is possible locally, but it does not resolve the next prefix-link
level.

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

`digital_binary_verify.py` checks the standard binary Raikov-Stöhr example
from Attempt 12 after deleting the even-support elements of the even-position
digit class. Up to the default cap `20000`, the remaining set misses only
`1` and `2` at order `3`, matching the explicit support-splitting proof in
`PROOF.md`.

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
`1,3,21,23,31`. This is recorded as Diagnostic 16.1 in `PROOF.md`: the
third-stage failure is domination-limited, not merely a coverage failure.
A bounded non-greedy DFS with candidate values up to `110`, increments of
size at most `3`, and slack `100` also found no chain beyond depth `2`.
With wider first/second-stage enumeration, alternative first moves exist
but the branches tested still have no third extension.
