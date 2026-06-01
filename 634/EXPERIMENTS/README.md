# Experiments

Computational work for Problem #634.

Current components:

- `positive_constructions.py`: exact arithmetic checks for elementary positive
  coordinate certificates and Zhang parameter arithmetic.
- `small_family_coverage.py`: high-level report for small `N`, combining
  recorded positive and negative certificates without guessing.
- `composite_case_dashboard.py`: case dashboard for unresolved composite
  values; it collects elementary positives, source sufficient constructions,
  Zhang hits, equilateral arithmetic candidates, and current template filters
  for requested `N`.
- `composite_gap_scan.py`: concise scanner for requested counts, separating
  classified values from values with surviving encoded candidates and values
  whose remaining gap is source-reduction coverage.
- `equilateral_area_candidates.py`: necessary area and boundary-length filter
  for equilateral outer triangles with a tile angle `pi/3` or `2pi/3`.
- `equilateral_boundary_exact.py`: exact finite boundary-length arithmetic
  enumerator for equilateral outer triangles. For each requested `N`, it uses
  `L=xa+yb+zc` with `x+y+z<=N`, eliminates `L,c`, and solves the resulting
  rational quartics in `a/b`; this supersedes side-bounded brute force for the
  first small composite targets.
- `equilateral_gamma_boundary.py`: local full-boundary side-label star check
  for equilateral outer triangles with `gamma=2pi/3`; it eliminates the
  side-bounded `N=14` `(7,8,13)` and `N=15` `(3,5,7)` candidates.
- `equilateral_pi_boundary.py`: local full-boundary side-label star check for
  equilateral outer triangles with `gamma=pi/3`; it eliminates the side-bounded
  `N=21` `(16,21,19)` and `N=30` `(8,15,13)` candidates.
- `equilateral_lattice_exact_cover.py`: generic triangular-lattice exact-cover
  checker for the equilateral arithmetic candidates. It currently rules out the
  lattice-aligned `N=14` `(7,8,13)` and `N=15` `(3,5,7)` smallest candidates,
  but not arbitrary non-lattice tilings.
- `beeson_3alpha2beta_filter.py`: exact rational-root filter for the five
  Beeson/Laczkovich `3alpha+2beta=pi` necessary equations.
- `beeson_3alpha2beta_sufficient.py`: fast enumerator for the recorded
  sufficient `3alpha+2beta=pi` constructions, including the triquadratic
  condition `N=2K^2-M^2`, `K|M^2`.
- `beeson_3alpha2beta_boundary.py`: local boundary-star feasibility check for
  selected `3alpha+2beta=pi` candidates, plus a generic boundary-integrality
  filter for supported triquadratic, isosceles-beta, and isosceles-alpha
  outer shapes. The boundary-star checks currently rule out the `N=14`
  triquadratic raw candidate `(6,5,9)` in outer sides `(28,15,27)`, the `N=21`
  isosceles-alpha candidate, and triquadratic candidates for `N=46` and `N=56`.
- `beeson_isosceles_alpha_plus_beta_filter.py`: stronger source filter for the
  `3alpha+2beta=pi` isosceles-`alpha+beta` case. The `--counts` option prints
  the source side-count triples after the two reserved `c` edges on each outer
  side; this is a safe diagnostic and accepts the known positive `N=48`
  example.
- `beeson_isosceles_alpha_plus_beta_boundary.py`: boundary-order/nonfit
  obstruction for the `3alpha+2beta=pi` isosceles-`alpha+beta` survivors. It
  closes the Section 11.4 survivor records at `132`, `156`, `175`, `189`,
  `198`, `204`, `224`, and `228`, while preserving the resonant `48` positive
  example. It also closes the `240` survivor by a special `a/c` overhang
  endpoint argument.
- `prime_case_dashboard.py`: high-level report for prime `N`, combining the
  source arithmetic reductions with the `3alpha+2beta=pi` filter.
- `gamma_2pi3_isosceles_filter.py`: exact arithmetic filter from Beeson's
  isosceles `gamma=2pi/3` theorem; `--prime-scan` lists the remaining
  `p == 3 mod 4` prime candidates in that subcase.
- `gamma_2pi3_nonisosceles_exact.py`: exact arithmetic filters for all four
  non-isosceles `gamma=2pi/3` templates, combining BLZ formulas with the
  boundary-integrality product formulas.
- `gamma_2pi3_nonisosceles_boundary.py`: endpoint-pair boundary-star checker
  for exact non-isosceles `gamma=2pi/3` arithmetic candidates in all four BLZ
  templates; currently rules out the recorded candidates for `N=21`, `N=30`,
  `N=55`, `N=88`, `N=105`, `N=120`, and the `N=143` swaps.  In the `100..250`
  dashboard it also removes the later BLZ survivors `154`, `168`, `210`, and
  `220`.
- `gamma_2alpha_boundary.py`: Beeson Lemma 11.14 arithmetic enumerator for the
  isosceles `gamma=2alpha` branch, now also reporting the conservative
  refinement from the two-`c` boundary-edge lemma, base endpoint lemma,
  boundary `c`-parity, and Beeson Lemma 11.17.
- `gamma_2alpha_endpoint_automaton.py`: diagnostic endpoint automaton for
  `gamma=2alpha`; its `angle` mode preserves the open boundary controls, while
  the stricter `fan` mode is only a side-label diagnostic until boundary
  overhangs along interior rays are ruled out.
- `gamma_2alpha_overhang_components.py`: diagnostic enumerator for primitive
  equal-length overhang components such as `a+c=kb`; these matter for interior
  interfaces and calibrate the missing no-overhang lemma needed before the
  `N=63`/`N=99` fan diagnostic can become a proof.
- `gamma_2alpha_overhang_fan.py`: local overhang-aware boundary fan diagnostic;
  it shows that the primitive `a+c=kb` components can support the `c`/non-`c`
  transitions that the strict side-label fan automaton rejects.
- `gamma_2alpha_boundary_transition_demand.py`: dynamic program minimizing the
  number of outer-boundary `c`/non-`c` transitions required by a refined
  `gamma=2alpha` boundary survivor.
- `gamma_2alpha_boundary_fan_inventory.py`: overhang-aware inventory diagnostic
  for the straight boundary fans in a transition-demand witness. It sums the
  side incidences forced by those local fans and currently shows that the
  `N=63` and `N=99` benchmark survivors are not eliminated by this counting
  lower bound.
- `gamma_2alpha_fan_frontier.py`: aggregate version of the boundary-fan
  inventory over all endpoint/mixed boundary-word classes. It shows that all
  `88` endpoint/mixed classes remain feasible under the local fan
  side-incidence bound for both `N=63` and `N=99`.
- `gamma_2alpha_boundary_shell.py`: floating geometry placement of the
  boundary-adjacent tile shell from a transition-demand witness. It merges the
  two duplicated base-corner tiles and checks for remaining positive-area
  overlaps; it is a seed for residual search, not an existence proof.
- `gamma_2alpha_residual_boundary.py`: residual boundary graph extractor for
  the boundary shell. It splits shell edges at T-junctions, separates outer
  boundary atoms from residual atoms, and can write an SVG diagnostic.
- `gamma_2alpha_residual_corner_labels.py`: immediate residual-corner label
  check for the current transition-demand shell. For the displayed `N=99`
  shell, every residual segment is a full indecomposable tile side, but nine
  forced single-angle corners have incompatible adjacent side labels; this
  rules out that shell witness, not every possible boundary ordering.
- `gamma_2alpha_min_shell_census.py`: finite census over the canonical
  endpoint-minimal boundary-shell representatives selected by the transition
  demand path DP. For `N=63` and `N=99` there are eight representatives each,
  and none passes the current overlap/simple-cycle/corner-label filters.
- `gamma_2alpha_random_shell_search.py`: randomized sampler over all
  angle-compatible noncanonical boundary paths for a refined `gamma=2alpha`
  survivor. It applies the same shell filters and is useful for finding
  candidate extensions or stress-testing the endpoint-minimal census, but it is
  not an impossibility proof. The `--max-total-mixed` option stratifies the
  sampler into low-overhang boundary shells; `--exact-quadratic` reruns sampled
  shells through the exact `Q(sqrt(d))` classifier, and `--by-mixed` reports
  status counts by total mixed-transition count. The `--valid-weighted` option
  samples directly from corner-compatible endpoint/mixed classes, weighted by
  the number of boundary shells they represent.
- `gamma_2alpha_overlap_causes.py`: exact valid-weighted sampler focused on
  proper shell overlaps. It records the first exact positive-area overlap by
  outer-side pair, boundary-tile position, and oriented tile label. In a
  seed-`20260601`, `50000`-sample run, proper overlaps concentrate at
  base/equal-side pairs such as `L2` with `B8` and the symmetric right-base
  positions, with no new first-overlap positions beyond the current local pair
  set. The `--outside-local-cover` option conditions samples on avoiding the
  default local overlap cover before running the residual checks.
- `gamma_2alpha_overlap_cover.py`: exact count-only version of the local
  overlap-position diagnostic. For the sampled local pairs
  `L2-B8,R6-B2,R5-B3,R8-B2,R7-B2,L2-B7,R7-B3,L3-B7,R6-B4`, it covers
  `276555680/295877600` boundary shells for `N=63` and
  `8012836776/11122617000` for `N=99` by local positive-area overlap tests;
  expanding to every possible equal-side/base boundary-tile position pair gives
  the same counts. By mixed level, the default/all-pair cover leaves
  `3,382,720`, `9,122,560`, and `6,389,760` outside-cover shells at
  `N=63` mixed `8`, `10`, and `12`, and leaves `136,555,720`,
  `1,050,178,232`, and `1,917,116,232` outside-cover shells at `N=99`
  mixed `8`, `10`, and `12`.
- `gamma_2alpha_overlap_remainder_inventory.py`: grouped count-only inventory
  of the boundary shells outside the local overlap cover. At cap `6`, the
  millions of outside-cover shells collapse to `26` endpoint/mixed boundary
  groups for each benchmark row. For `N=63`, the largest outside-cover mixed
  splits are `(2,1,3)` and `(1,2,3)`, each with `111600` shells, followed by
  `(2,2,2)` with `51840`; for `N=99`, `(2,2,2)` contributes `2095200`, then
  `(2,1,3)` and `(1,2,3)` contribute `947700` each. It also prints top
  c-position, mixed-position, tested-local-label, and oriented fan-transition
  profiles for the outside-cover mass. The oriented fan profile is useful as a
  negative calibration: at mixed exactly `6`, it gives `120224` profile groups
  for `N=63` and `1080609` for `N=99`, so boundary-only fan signatures are too
  fine for manual casework. Raw side-label word triples are also too fine:
  `40560` groups for `N=63` and `418260` for `N=99` at mixed exactly `6`.
- `gamma_2alpha_residual_failure_causes.py`: exact valid-weighted sampler for
  the residual failures after optional local-overlap-cover filtering. It
  refines `not-simple-cycle` into residual graph degree/component profiles,
  records full-side atom and parity profiles, and aggregates forced
  corner-label violation types. In the seed-`20260602`, `50000`-attempt
  outside-cover run, every non-simple residual graph for `N=63` and `N=99` is
  a connected graph with degree-4 pinch vertices, while the all-full residual
  atom profiles have no side-parity mismatch. The non-2-degree vertex incident
  and cyclic incident-label profiles are concentrated in only two profiles,
  `accc` and `aabc`. The sector pass marks shell-occupied sectors exactly from
  the incident shell-tile wedges and classifies the residual sector angles by
  exact cosine tests for `alpha`, `gamma=2alpha`, and straight `pi`. It finds
  that the `accc` residual sectors are locally unfillable (`cc:alpha` and
  `ac/ca:gamma`) under the endpoint automaton, while pure `aabc` pinches are
  locally fillable. The script now reports these as `pinch-sector-obstruction`,
  separating them from the locally fillable `not-simple-cycle` remainder; in
  the seed-`20260602`, `10000`-attempt outside-cover run the split is
  `250/43` for `N=63` and `895/218` for `N=99`. The exact split-cycle component
  diagnostic enumerates the two planar pairings at each degree-4 pinch and
  checks component area, boundary-side upper bounds, side-label parity, and
  forced corner-label compatibility on each split component cycle. In the same
  run, all locally fillable non-simple samples are reclassified as
  `split-corner-label-obstruction`, leaving no sampled residual graph outside
  the three exact residual obstruction statuses.
- `gamma_2alpha_residual_capped_census.py`: deterministic streaming census for
  capped total-mixed boundary shells. It can discard the default local-overlap
  cover with cached local-position polygons, runs the exact coarse shell
  classifier, and refines non-simple residual graphs with the full
  pinch/split-component diagnostics. For total mixed `<=4`, it reproduces the
  exact shell counts and upgrades the old non-simple buckets to exact
  split-corner-label obstructions: `N=63` has `4896`
  corner-label violations and `6144` split-corner-label obstructions; `N=99`
  has `20520` and `42480`. Cap `6` is not yet fully residual-classified; the
  count-only local-overlap cover leaves `415840` mixed-`6` shells for `N=63`
  and `5867040` mixed-`6` shells for `N=99` outside the current local cover.
- `gamma_2alpha_residual_chunked_census.py`: resumable chunk runner for exact
  residual status counts over generated-shell slices. It supports coarse mode
  using the quadratic shell classifier and refined mode using the
  pinch/split-component diagnostic, with either eager or lazy local-cover
  checking. It also has an experimental residual-segment-key diagnostic cache;
  on the first `10000` generated `N=99` mixed-`6` shells this key is too fine,
  with `8029` unique residual keys for `8029` outside-cover shells and no cache
  hits. A first sanity chunk for `N=63`, mixed exactly `6`, outside the
  local cover, processed `2000` generated shells:
  `970` were local-cover hits, and the `1030` diagnosed shells split as
  `838` corner-label violations and `192` non-simple residual graphs. Extending
  through generated shell `10000` gives cumulative exact coarse counts:
  `4899` local-cover hits, `4077` corner-label violations, and `1024`
  non-simple residual graphs. Through generated shell `100000`, the cumulative
  counts are `52430` local-cover hits, `28326` corner-label violations, and
  `19244` non-simple residual graphs. A refined replay of that same prefix,
  stored under `results/n63_mixed6_refined_chunk_0000000_0100000.json`,
  splits the `47570` outside-cover shells as `28326` corner-label violations,
  `3332` pinch-sector obstructions, and `15912` split-corner-label
  obstructions. Through generated shell `200000`, lazy local-cover mode gives
  cumulative coarse counts `139104`, `34292`, and `26604`. Through generated
  shell `500000`, the cumulative coarse counts are `358826`, `61534`, and
  `79640`. The recorded refined chunks through generated shell `500000`
  exactly refine that prefix: `358826` local-cover hits, `61534`
  corner-label violations, `21816` pinch-sector obstructions, and `57824`
  split-corner-label obstructions. The full mixed-`6` `N=63` refined pass is
  now exact and stored in `results/n63_mixed6_refined_summary.json`:
  `940800` local-cover hits, `207888` residual corner-label violations,
  `58224` pinch-sector obstructions, and `149728`
  split-corner-label obstructions.
- `gamma_2alpha_residual_group_probe.py`: stratified exact residual probe for
  outside-cover endpoint/mixed groups. At mixed `6`, it finds outside-cover
  representatives in all `20` cap-`6` endpoint groups for both `N=63` and
  `N=99`; every probed representative falls into one of the exact residual
  obstruction statuses. Its `--group-by word` mode groups by side-label word
  triples and now emits summary JSON. In a first `N=99` mixed-`6` 100k-prefix
  probe, up to two representatives per word group found no mixed-status groups
  among `5600` touched groups; an analogous `N=63` mixed-`8` 20k-prefix probe
  found no mixed-status word groups among `320` touched groups. Its
  `--group-by profile` mode instead groups by
  c-position, mixed-position, and tested-local-label profiles. This is evidence
  for the grouped proof target, not a complete count.
- `gamma_2alpha_word_quotient_census.py`: exact count-plus-representative
  classifier for outside-cover quotient groups. In its default `--quotient word`
  mode it groups by side-label word triples. It reproduces the full
  `N=63` mixed-`6` outside-cover mass as `40560` word groups over `415840`
  shells; classifying up to two representatives in every word group gives no
  mixed-status word group and weighted totals exactly matching the full refined
  census: `207888` corner-label violations, `58224` pinch-sector obstructions,
  and `149728` split-corner-label obstructions. For `N=99` mixed `6`, it
  counts `418260` word groups over `5867040` outside-cover shells; all word
  groups have now been representative-classified with up to two representatives
  per word and no mixed-status word group. The representative weighted totals
  are `2338380` corner-label violations, `775440` pinch-sector obstructions,
  and `2753220` split-corner-label obstructions, recorded in
  `results/n99_mixed6_word_quotient_summary.json`. The runner supports
  `--skip-classified-words` for disjoint classification intervals.
  Its `--classification-mode exhaustive` option checks every oriented
  realization of each selected word group; in the first `150000` `N=99`
  mixed-`6` word groups, all `2281860` outside-cover realizations match the
  word-group status with no count mismatches.
  Stress tests with up to `8` representatives per word also found no
  mixed-status word among the first `2000` word groups or among word groups
  `350001..352000`. A full targeted enumeration of a heaviest `N=99`
  mixed-`6` outside-cover word group of multiplicity `54` found all `54`
  realizations have status `corner-label-violation`.
  A second targeted exhaustive check covers selected `N=99` mixed-`6` word
  groups from all three representative statuses: `9/9` outside-cover
  realizations are pinch-sector obstructions, `12/12` are
  split-corner-label obstructions, and `12/12` are corner-label violations.
  The same quotient does not naively extend to `N=63` mixed `8`: the first
  `50000` word groups include `1152` mixed-status word groups, and a fixed
  word triple with `48` outside-cover realizations splits as `12`
  corner-label violations and `36` pinch-sector obstructions.
  The newer `--quotient profile` mode groups by c-positions, mixed-transition
  positions, tested local-overlap labels, and oriented fan signatures. For
  `N=63` mixed `8`, this gives `1493568` profile groups over `3382720`
  outside-cover shells; the first `10000` profile groups have no mixed
  representative status, with weighted status counts `23660` corner-label,
  `8370` pinch-sector, and `4320` split-corner-label obstructions.
  A generated-shell prefix probe over the first `100000` shells also found no
  mixed-status profile group among `10560` touched groups.
- `gamma_2alpha_word_invariance_probe.py`: exhaustive fixed-word tester for
  selected side-label word triples. It enumerates every oriented boundary
  demand realizing the requested words in the capped shell space, applies the
  local-overlap cover, and classifies all outside-cover realizations. This is
  the direct falsification harness for the pending word-invariance lemma.
- `gamma_2alpha_word_exhaustive_summary.py`: verifier for disjoint exhaustive
  word-quotient interval artifacts. It checks interval lengths, gaps,
  overlaps, mixed-status words, word-count mismatches, and weighted status
  totals. The current summary for the first `150000` `N=99` mixed-`6` word
  groups is stored in
  `results/n99_mixed6_word_exhaustive_summary_000001_150000.json`.
- `gamma_2alpha_residual_certificate_probe.py`: bounded exact probe that runs
  the full residual diagnostic and groups shells by compact obstruction
  certificates: forced-corner violation profiles for simple residual cycles and
  graph/pinch/sector/split profiles for non-simple residual graphs. A first
  mixed-`6` outside-cover slice of `50` diagnosed shells gives `17`
  corner-label certificate types for `N=63` and `18` for `N=99`; this is
  order-biased calibration, not a proof. The probe now supports lazy
  local-cover filtering, generated-shell skips, and JSON output. Recorded
  `N=63` high-mixed outside-cover slices of `1000` diagnosed shells each show
  only the existing exact obstruction statuses: mixed `8` has `904`
  corner-label violations and `96` split-corner-label obstructions, while
  mixed `10` and mixed `12` each have `838` corner-label violations and `162`
  pinch-sector obstructions. The first `N=99` mixed-`6` outside-cover slice of
  `1000` diagnosed shells has `782` corner-label violations and `218`
  split-corner-label obstructions.
- `results/n99_mixed6_refined_chunk_0000000_0100000.json`: first exact
  refined `N=99` mixed-`6` generated-shell prefix. It processes `100000`
  generated shells in `647.8s`, with `19668` local-cover hits and `80332`
  outside-cover obstructions: `62456` corner-label violations and `17876`
  split-corner-label obstructions. This calibrates direct chunking as too slow
  for a full raw `N=99` mixed-`6` pass without a quotient.
- `gamma_2alpha_low_mixed_shell_census.py`: deterministic finite census of all
  boundary shells whose total `c`/non-`c` transition count is at most a cap. For
  the benchmark cap `4`, it enumerates `11040` shells for `N=63` and `63000`
  shells for `N=99`. Its geometry predicates are floating-point diagnostics;
  the exact low-mixed classifications are now supplied by the rational and
  quadratic scripts below.
- `gamma_2alpha_mixed_growth.py`: count-only mixed-transition growth diagnostic
  for the same boundary-shell spaces. Without materializing every shell, it
  shows that the full boundary-order spaces plateau at `295877600` shells for
  `N=63` and `11122617000` shells for `N=99`.
- `gamma_2alpha_rational_shell_census.py`: exact-arithmetic shell classifier
  for rational-coordinate `gamma=2alpha` survivors. It currently applies to
  the `N=99` benchmark; after rational placement it clears denominators and
  uses integer geometry to classify all `63000` total-mixed-`<=4` shell
  demands exactly as `42480` non-simple residual cycles and `20520` residual
  corner-label violations.
- `gamma_2alpha_quadratic_shell_census.py`: exact-arithmetic shell classifier
  for `gamma=2alpha` survivors whose shell coordinates lie in `Q(sqrt(d))`.
  It currently applies to the `N=63` benchmark over `Q(sqrt(5))`; after
  quadratic placement it clears denominators to integer pairs and classifies
  all `11040` total-mixed-`<=4` shell demands exactly as `6144` non-simple
  residual cycles and `4896` residual corner-label violations. It also
  reproduces the endpoint-minimal `N=99` rational checks with `d=1`.
- `isosceles_71_boundary.py`: boundary decompositions and side-to-side parity
  obstruction for the remaining prime `71` isosceles `gamma=2pi/3` candidate.
- `isosceles_71_boundary_sequences.py`: exact boundary side-order/orientation
  enumerator for the same `71` candidate; it rules out arbitrary non-strict
  tilings because the forced base sequence cannot start and end with alpha
  endpoints without producing a forbidden gamma-gamma straight boundary point.
- `isosceles_71_matching.py`: length-only interior side-matching model for the
  same `71` candidate; it records that any non-strict tiling needs an interior
  matched segment of length at least `195`.
- `isosceles_71_interface_angles.py`: local straight-angle feasibility check
  for that forced length-`195` odd-`c` interface.
- `isosceles_71_lattice_coloring.py`: unit-triangular-lattice up/down coloring
  obstruction for the `71` candidate when all vertices lie in the induced
  lattice; this covers strict tilings but not arbitrary shifted T-junctions.
- `isosceles_prime_family.py`: parametrized diagnostics for all surviving
  prime candidates in the isosceles `gamma=2pi/3` filter, including boundary
  decompositions and strict edge-to-edge parity.
- `isosceles_prime_boundary_words.py`: dynamic-programming boundary endpoint
  automaton for those prime candidates, including local side-label matching at
  straight boundary vertices; it supports the general transition-table proof
  that the isosceles `gamma=2pi/3` subcase is impossible.
- `isosceles_prime_matching.py`: length-only side-matching diagnostic for the
  boundary-word survivors; after the stronger transition check there are no
  searched survivors left for it to inspect.
- `blz_gamma_2pi3_nonisosceles_filter.py`: BLZ square-class filters for the
  non-isosceles `gamma=2pi/3` templates; two templates are theorem-level prime
  exclusions, while the other two now include reproducible boundary-integrality
  minima `88` and `264`.
- `zhang_constructive_families.py`: enumerator for Zhang's proved positive
  `2pi/3` and `pi/3` construction families; it does not use Zhang's conjectural
  converses as obstructions.
- `zhang_15_lattice_exact_cover.py`: original special-case exact-cover sanity
  check for the tempting equilateral `N=15` candidate using tile `(3,5,7)`;
  superseded for new checks by `equilateral_lattice_exact_cover.py`.
- `634Triangle.png`: cached copy of the `27`-tiling image linked from the
  Problem #634 page.

Planned components:

- symbolic angle-count equations for triangular tilings;
- boundary side-vector and area constraints;
- small-`n` combinatorial tiling graph enumerators;
- sanity tests against known positive cases and known negatives `7`, `11`.

Important limitation: except where a script is explicitly recording a proved
source theorem or the boundary-integrality lemma from `PROOF.md`, the current
scripts do not search arbitrary tilings and do not prove impossibility. They are
certificate/checking scaffolding.
