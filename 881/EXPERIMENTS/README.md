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
in Lemma 8.5a.7u. The complete rank-3 product wiring example is the
abstract pair-free product cover left after Corollaries 8.5a.7v--8.5a.7x:
it covers every selector with weight \(1\), but only at support rank \(3\).

`product_rank3_terminal_cover.py` verifies a finite arithmetic realization
of that abstract rank-three shape. For
\[
A=\{1,3,4,5,8,10,11,12\}
\]
and packets \(\{4,10\},\{5,11\},\{8,12\}\), every selector triple has an
inclusion-minimal terminal-gap witness in \([14,23]\), while all singleton
and pair deletions remain three-fold covered on that same window. This is
the finite warning recorded as Example 8.5a.7z; the coverage point \(24\)
is the one-point stage buffer from Lemma 13.1d. The script also groups
shared witness values by their selector families and checks the
two-transversal condition from Lemma 8.5a.7z.4 on the actual shifted
two-sum supports, then checks the common-core spike dichotomy from Lemma
8.5a.7z.5. It also prints the finite deleted-gate maps for each selector
witness, separating retained mirrors from deleted-pair exception rows in
the reflected-front bookkeeping of Target 8.5a.7z.8.

`product_rank3_extension_search.py` starts from that window and tries to add
a fourth two-point packet, optionally with fillers. It requires every three
of the four packets to have complete selector-triple terminal-gap witnesses,
while all singleton and pair deletions remain harmless on the witness
window. The bounded run
`--max-value 30 --max-fillers 2` checks `20961` candidates and finds no
extension, recording Diagnostic 8.5a.7z.2.

`selector_reflected_front_search.py` tests the stricter reflected-front
bookkeeping from Target 8.5a.7z.8 on fixed finite windows. On the seed
window, the default run finds terminal gate-map candidates for all eight
selector triples. With `--require-retained-mirrors`, only four candidates
remain; adding `--require-all-gates-active` leaves three selector triples.
Thus the local product cover in Example 8.5a.7z relies substantially on
deleted-pair exception rows and is not already a full retained-mirror front.
For each retained gate, the script also reports the unique-gate rows and
fixed shifted-overlap rows from Lemma 8.5a.7z.10, plus whether those
singleton or pair spike supports are already holes for the same witness.
On the strict seed run, all such promotion flags are false; with
`--promotion-radius 5`, the strict run still has no nearby singleton or
pair holes.
`selector_pair_promotion_scan.py` aggregates the same shifted-overlap
branches and classifies repair triples. In the strict retained-mirror and
all-gates-active run it finds `6` directed shifted-overlap branches, no
pair holes at the original witness or within radius `5`, and every original
witness repair after deleting the pair uses the remaining active selector.
In the broader default run it finds `34` directed branches, still no holes
on the original witness window `[14,23]`, and the only nearby pair holes
are the later `(10,11,12)` cases at `26`, `27`, and `28`.

`spike_no_promotion_gadget.py` verifies a range-separated local gadget where
a rank-three witness has a shifted-overlap spike on one deleted pair, but
every pair deletion is harmless at that same witness because the remaining
active color repairs it. This records Diagnostic 8.5a.7z.12; Example
8.5a.7z.12a gives the corresponding arbitrary-size finite construction.
`spike_interval_filler_pressure.py` then adds retained low-interval fillers
to the same gadget. In the default instance, radius `5003` still does not
repair the witness, while radius `5004` does via
`5004+5004+89992=100000`; this is the first point where the interval's
two-sum coverage reaches the private spike sum \(f+\min U\).
`spike_safe_filler_profile.py` adds the maximal harmless low band and a
second retained band above all private spike sums. After removing the
single middle-packet complement `14000`, the full set has continuous
two-sum coverage through `30000`, while the retained set still misses all
private spike sums and does not repair the witness `100000`. This shows
that the initial coverage gap in Example 8.5a.7z.12a can be bridged
locally; the remaining stage obstruction is freezing the much later witness.
`spike_safe_extension_search.py` then tries one-point safe retained
extensions from the same profile at scale `100`. With beam `8`, coverage
extends from `3000` to `6488` and stalls at `6489`; with beam `32`, it
extends only to `6501`. The next-gap candidates are unsafe almost entirely
because each candidate plus an existing retained pair sums to the witness.
It also checks two-point batches for the stalled next gap and finds none in
the scale `100` and `200` runs. The scale `200` run gives the same ratio,
reaching `12947` below witness `20000`.
With `--allow-pairs`, the search may use safe two-point batches earlier in
the beam. This improves the scale `100` beam-`32` endpoint to `6578` and
the scale `200` beam-`8` endpoint to `12980`, but both still stall below
the witness with no safe one- or two-point way to cover the final gap.
The script also prints a reflected next-gap blocker certificate. In the
scale `100`, beam-`8`, `--allow-pairs` run, `d=w-p=3494` is retained and
all `1034` one-point candidates satisfy `d+a in 2C`, so Lemma
8.5a.7z.12e'' blocks every finite batch at that final gap. The explicit
flag is `no_finite_batch_by_12e_prime=True`. It also prints the
deleted-gate reflection check from Corollary 8.5a.7z.12e''': once `d` is
retained, retained old summands are automatic, and the default terminal
state has `d+{1000,1007,2000} subset 2C`. Corollary 8.5a.7z.12g records
the complementary bound: at fixed deleted packet `F`, such retained-defect
walls have size at most `|F+F|` above the order-2 threshold.
The seed geometry can be varied with `--upper-stop` and `--upper-policy`.
At scale `100`, interval upper endpoints `1200,1400,1600,1800` still end
in reflected blockers, with best cover endpoints `6465,6506,6200,6550`.
A greedy-safe upper band with endpoint `2500` reaches `6898`; endpoints
`3200` and `5000` start with coverage `6899` and immediately stall at
`6900`, again with a deleted-gate reflected blocker. The adjacent endpoint
`3000` also stalls at `6900` with no safe one- or two-point batch even
though `d=3100` is not retained. The script reports the one-sided
saturation certificate from Lemma 8.5a.7z.12h: `2312` saturated one-point
candidates and `1138/1138` saturated two-point splits. So the observed
pair-saturation obstruction is broader than the clean retained-defect
certificate. The `shadow_translation_summary` output records the normal
form from Lemma 8.5a.7z.12h.1: at endpoint `3000`, `d=3100` is not
retained but lies in `2C`, and `2311` old rows satisfy `d+a in 2C`.
The `shadow_escape_set_summary` output records the equivalent escape-set
form from Corollary 8.5a.7z.12h.2: there are no old-row escapes, the split
escape set has `2312` points but no complementary pair summing to `6900`,
and the half-candidate is saturated. Only `2` escape points lie below
`p/2`; their complements are already in the old set. This is the finite
instance of Warning 8.5a.7z.12h.3, so escape-set size alone cannot force a
safe split.
`shadow_escape_counterexample.py` verifies the parametric warning that even
initial interval coverage and a genuine minimal terminal hole do not force
escape-set balance. For `--L 5 --N 20`, it reports
`C=[1,2,3,4,5,20,21,22,23,24]`, `F=[11,30]`, first gap `p=11`, hole
`w=54`, no old-row escapes, and high-sided split escape set `[6,7,8,9,10]`
with no complementary pair.
The safe-extension script now also prints `final_defect_origin`. In the
greedy-safe upper-stop `2500` run, the final defect `3101` was added as the
first retained filler; in the default run, the final defect `3494` was
added at step `63`. This is the finite shadow of Lemma 8.5a.7z.12h.5:
safe fillers become future retained defects unless a private gate remains.
Lemma 8.5a.7z.12h.6 records the other branch: if many fillers survive to
their future gaps under the same witness and deleted packet, they must
produce large private-gate fibers, feeding back into the compressed-spike
diagnostics.
Corollary 8.5a.7z.12h.7 packages this as a trichotomy for retained fillers:
future full-gap, private-gate fiber, or reflected wall after gate absorption.
Corollary 8.5a.7z.12h.8 aggregates this over finite filler tests: a frozen
witness runway either leaves many future two-sum gaps or produces a large
private-gate fiber.
The reusable sweep mode
`--upper-policy greedy-safe --sweep-upper-stops 2400 2500 2600 2700 2800 2900 3000 3050 3100 3150 3200`
prints the same no-safe-one/no-safe-two obstruction throughout that
transition range.
With `--avoid-reflected-blockers`, the scale `100`, beam-`8` run reaches
only `6503`; at the stopping step it has `128` raw extensions and `0`
surviving the reflected-blocker filter. This tests the escape of avoiding
the bad final state and shows that, in this finite profile, the immediate
safe moves all enter reflected-blocker states.

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
Run it with `--high-excess` to require the stronger escape condition
`w - b - 2 * min(A) >= max(old)`; in the same third-stage seed, candidates
`41` and `43` have zero high-excess pair witnesses.
A bounded non-greedy DFS with candidate values up to `110`, increments of
size at most `3`, and slack `100` also found no chain beyond depth `2`.
With wider first/second-stage enumeration, alternative first moves exist
but the branches tested still have no third extension.

`high_excess_pair_seed_search.py` searches for non-residue singleton
stages satisfying the same high-excess condition. It finds the local seed
`old=[1,2,3,4]`, endpoint `4`, new point `8`, declared endpoint `17`,
and coverage through `20`; all old-new pairs have high-excess witnesses.
The greedy high-excess singleton chain then adds `19`, declares endpoint
`29`, covers through `31`, and stalls at the third stage. This records
local compatibility of the high-excess escape without giving an iterable
construction.
The same script also searches the non-singleton-new subcase, requiring
witnesses to remain in `4(A\\{b})`. Its first seed is `old=[1,2,3,6]`,
endpoint `7`, new point `9`, declared endpoint `19`, and coverage through
`21`; the greedy non-singleton chain stalls at the next stage.
Run it with `--block` to check high-excess block continuations of size at
most `3` and candidate values up to `100` from the two stalled seeds. It
finds no continuation after checking `57155` three-point blocks from
`[1,2,3,4,8,19]` and `85320` from `[1,2,3,6,9]`.

`pair_shadow_rows.py` also reports Corollary 16.6b row-load statistics for
the robust-booster third-stage candidates. For `b=41` and `b=43`, only old
endpoints `5,20,30` have non-singleton pair witnesses in the checked
window; after selecting one endpoint per distinct witness value, the
reflected rows have no overlap. This supports the current diagnosis that
the seed fails before a reusable moving row-bank forms.

`k3_pair_stage_dfs.py` is an unrestricted bounded DFS for Proposition
13.1e with `k=3`, without the modulo-10 booster restriction. With default
bounds it finds depth-four chains such as
`[1,2,3,4] -> +7 -> +17 -> +27 -> +37`, with endpoints
`15,26,36,46` and coverage through `18,28,38,48`. The tempting periodic
continuation by `47` fails the pair-witness condition, and a bounded
three-point search through candidate `120` finds no next stage.

`singleton_high_excess_stage_search.py` tests the stricter Lemma 16.9
singleton target: every new `b` needs `w notin 4(A\\{b})` and
`w - b - 2 * min(A) >= max(A)`. It finds only the first stage
`[1,2,3,4] -> +8`, with witness `18`, endpoint `18`, and coverage through
`20`; the next step fails after checking blocks up to size `3` and
candidate values up to `150`.
Lemma 16.10 explains the one-marker version: `[1,...,L] -> +2L` is always
a strict singleton-high-excess first stage for `L >= 4`, but a later single
marker begins beyond `4L+2` and leaves a three-sum coverage gap before its
required high-excess witness.
Lemma 16.11 records the corresponding block burden: if the next block has
minimum `x`, then `[x+3L+1, 2x]` must be covered by one new block element
plus `2([1,...,L] union {2L}) = [2,3L] union {4L}`.

`row_collision_scanner.py` checks singleton row-bank collisions. For
`A={1,2,3,4,8,19,20,28,33}`, `b=33`, and `d=40`, it verifies coverage
through `76`, confirms `73 notin 4(A\\{33})`, prints all eight rows
`40-p in 2A`, and reports no retained collision of `40-p in 2C` with
`33+p in 2C`. It also prints the one-term reflected row behind the unique
`b`-dependent row: for `p=3`, `40-33-3=4`.

`prepared_marker_followup_search.py` starts from that prepared marker stage
at endpoint `74` and tries to protect `19,20,28,33,8` in the next bounded
stage. It finds no ordinary singleton witness after adding blocks up to
size `3` through candidate `180`, and no strict high-excess witness after
blocks up to size `2` through candidate `150`. It also reports the best
failed declaration windows: for all five tested targets, the ordinary
block `(75,77,85)` makes every value of `[85,131]` represented but
poisoned in the complement of the target, while the strict block `(75,81)`
does the same on `[81,97]`.

Lemma 16.14 in `PROOF.md` records the exact diagnostic behind this output:
for `C=A\\{q}`, a candidate `w` is private after deleting `q` exactly when
`w-p notin 3C` for every retained padder `p`. The follow-up windows fail
because represented candidates already lie in some `p+3C`; the
interval-marker seed escapes precisely by leaving all those shifted
three-sum gaps open.

Lemma 16.15 gives the row-bank follow-up to the scanner's collision test:
if a private witness `w=q+d` has a retained padder `p` with `q+p in 2C`,
then the forced row `d-p` must be `q`-dependent, so `d-q-p in A`.
Diagnostics that print b-dependent rows are therefore also printing
one-term reflected rows.
The prepared marker has one reflected row, `p=3 -> 4`, and seven
unique-gate translates `33+p notin 2C`, matching Lemmas 16.17-16.18.
Here the secondary center is `d-b=7`, so Lemma 16.19 predicts that all
tested rows `p>6` must be unique-gate; the scanner reports exactly that
for `8,19,20,28`. The scanner also checks the Corollary 16.22
gate-independence condition `p+b-r notin A` among unique-gate rows; the
prepared marker has no violations.

Lemma 16.16 records the adjacent-block obstruction for old fillers. If a
later block starts above `4 max(S)`, then any private order-4 witness for
an old target below the two-new range is just `p + z` with one new `p` and
an old three-sum private hole `z` for that target. New high blocks cannot
create such singleton protection from scratch in the one-new range.

`delayed_collective_barrier_search.py --rank 3 --max-value 32 --max-size 12`
reproduces the local rank-three delayed examples from `PROOF.md`, starting
with `S=[1,...,8]`, `F=(4,5,6)`, and witness `20`; variants `(4,5,9)` and
`(4,6,9)` also appear. These remain block-local fixed-rank cuts, not
unbounded barriers.

`balanced_k3_certificate_stats.py` brute-forces the finite certificate
condition used in Corollary 16.20. For the dense interval `[1,...,8]`, the
largest balanced-certificate-free subset has size `2`, so every half-sized
subset has a certificate. For the prepared row-bank set
`{1,2,3,4,8,19,20,28,33}`, the largest such subset has size `6`, showing
that sparse prepared blocks can evade the reflected-branch finite test.
Corollary 16.22 then says the surviving unique-gate rows should be read as
a moving gate-independent packet, not just as isolated two-sum accidents.

`unique_gate_interval_marker.py` verifies Example 16.23 for several
interval-marker sizes. It checks that `[1,L] union {2L}` has a full
unique-gate, gate-independent packet on `[1,L]` with private witness
`4L+2`, while `[1,L]` still contains the balanced certificate `1,2,2,2`.

`interval_marker_next_block_search.py` focuses on the first seed
`[1,4] union {8}` and searches larger strict singleton continuation blocks
with a bitset sumset engine. The default run checks all blocks of size at
most `6` with candidate values through `50`; it finds no block where every
new element has a strict singleton order-4 witness below the new declared
endpoint.
This implements the exact witness-window criterion of Corollary 16.25:
private candidates for `q` are represented values in `4S` that avoid every
shift `p + 3(S \\ {q})` from retained padders `p`.
The diagnostic now also reports sparse-protection debt. Under the default
bounds, the best eligible size-6 block is `(19,25,26,39,43,44)`, declared
at `95`; only `19` and `39` have strict singleton witnesses, and only `39`
lies in the common-row pressure range from Corollary 16.29.

`interval_marker_deferred_followup.py` starts from that best debt block and
tries to protect the deferred fillers `25,26,43,44` in one later bounded
stage. With blocks of size at most `2` and candidates through `150`, every
target fails in both ordinary and strict high-excess modes; the best window
is `(99,132)` after adding `(96,99)`, and all represented candidates in
that window are already poisoned by retained-padder shifts.

`bridge_sidon_pressure.py` evaluates Corollary 16.28 numerically. For the
interval-marker model with `L=4`, the default run shows the first possible
next marker `x=19` is still in the near-range escape, while
`x=1600=100L^2` is already beyond the Sidon-pressure threshold: any bridge
block inside `[x,2x-2]` covering `[x+13,2x]` cannot have a simultaneous
gate-independent half-packet over its own rows. It also reports the
bounded-staggered Corollary 16.33 tests for `1`, `2`, and `4` witness
windows.

`interval_central_sum_band.py` checks Lemma 16.54: after deleting at most
`r` points from an interval `[a,b]`, the central band
`[2a+2r,2b-2r]` remains inside the retained two-sumset. The companion
`interval_gate_profile.py` checks the interval-only inequality behind
Corollary 16.59: the number of gate-dependent rows is at most twice the
gate's distance from the central gate range `[a+2r,b-2r]`.
