# Erdős Problem #634 Notes

## Problem

Classify the positive integers `n` for which at least one triangle admits a dissection into `n` congruent triangles.

The tile triangle is not required to be similar to the large triangle unless explicitly stated.

## Working Vocabulary

- A tiling is a finite dissection of one triangle into `n` congruent triangular
  tiles. Vertices of tiles may lie in the relative interiors of sides of other
  tiles unless a construction or proof imposes a stricter edge-to-edge model.
- A monohedral triangular dissection means all tiles are congruent, with reflections allowed.
- A rep-tile case means the large triangle is similar to the tile. These are substantially more rigid than the general problem.
- If the tile has side lengths `(a,b,c)` and area `A`, then the tiled triangle has area `nA`.
- Boundary side vectors of the large triangle are sums of signed/rotated tile side vectors.

## Known Positive Families To Reconstruct

- `n = m^2`: split every side of any triangle into `m` equal pieces and use the standard grid by lines parallel to the three sides.
- `n = 2m^2`: split an isosceles triangle by its symmetry altitude, then subdivide each half into `m^2`.
- `n = 3m^2`: split an equilateral triangle by joining its center to the vertices, then subdivide each of the three congruent triangles.
- `n = 6m^2`: split an equilateral triangle by joining the center to the vertices and side midpoints, then subdivide the six congruent `30-60-90` triangles.
- `n = a^2 + b^2`: right-triangle/Pythagorean-sum construction; see `PROOF.md` for coordinates.
- Zhang `2pi/3` families: for integer tile `(a,b,c)` with `c^2=a^2+ab+b^2`, sufficiently large `m^2ab` occurs as an equilateral tiling; Zhang also gives several other quadratic-count families for the remaining `2pi/3` templates.

## Known Obstructions To Reconstruct

- `n = 7` impossible.
- `n = 11` impossible.
- `n = 14` and `n = 15` impossible in this workspace: the same source split
  used for `22` leaves only exact equilateral and `3alpha+2beta` candidates,
  and all are removed by the recorded boundary/Section 11.4 filters.
- `n = 21` and `n = 30` impossible in this workspace: exact `pi/3`
  equilateral candidates and the remaining non-isosceles `gamma=2pi/3`
  candidates are removed by boundary-star checks, while the other source rows
  have no survivor.
- `n = 22` impossible in this workspace: the published Laczkovich/Beeson source
  case split reduces the count to exact arithmetic branches, and each branch is
  eliminated in `PROOF.md`.
- `n = 33` and `n = 35` impossible in this workspace: the exact source-row
  filters leave only a `33` isosceles `gamma=2pi/3` arithmetic candidate and
  isosceles-`alpha+beta` raw roots; these are eliminated by the
  boundary-transition lemma and Beeson's Section 11.4 filter.
- `n = 38`, `n = 39`, and `n = 42` impossible in this workspace: exact
  equilateral checks, source-row arithmetic filters, and the `39`
  boundary-integrality obstruction remove all candidates.
- `n = 46` and `n = 51` impossible in this workspace: exact equilateral and
  non-isosceles `gamma=2pi/3` branches are empty, while the remaining
  isosceles/`3alpha+2beta` candidates fail boundary-transition, boundary-star,
  or Section 11.4 filters.
- `n = 55` impossible in this workspace: exact equilateral `pi/3` candidates
  and the one non-isosceles `gamma=2pi/3` candidate fail boundary-star checks,
  and the `3alpha+2beta` raw roots fail Beeson's Section 11.4 filter.
- `n = 56` impossible in this workspace: the exact equilateral and
  `3alpha+2beta` candidates fail boundary-star/Section 11.4 checks, and the
  local Beeson Lemma 11.14 `gamma=2alpha` enumeration returns no candidate.
- `n = 57` and `n = 62` impossible in this workspace: both are squarefree
  composite counts outside the elementary positive forms; exact equilateral,
  `gamma=2pi/3`, and `3alpha+2beta` source-row filters leave no survivor.
- `n = 60` impossible in this workspace: all non-`gamma=2alpha` source rows
  are eliminated locally, and the remaining `gamma=2alpha` candidate is removed
  by the local c-edge lower-bound/base endpoint refinement plus Beeson
  Lemma 11.17.
- `n = 63` and `n = 99` remain open in this workspace: all other source rows
  are eliminated locally, and the final `gamma=2alpha` boundary patterns are
  the current benchmark survivors. Local overhang fans using `ca | bbb` for
  `63` and `ca | bbbbb` for `99` show that the strict side-label fan diagnostic
  is not enough. The boundary-fan side-incidence inventory also has slack:
  minima `(39,35,31)` inside `(56,54,56)` for `63`, and `(48,34,40)` inside
  `(92,86,92)` for `99`. The floating boundary-shell placement has no proper
  positive-area overlaps after merging the two duplicate base-corner tiles,
  leaving residual tile areas `42` and `74`. Exact shell classifiers now remove
  all total-mixed-`<=4` boundary shells in both benchmark rows: `63` has `6144`
  non-simple residual cycles and `4896` residual corner-label violations over
  `Q(sqrt(5))`, while `99` has `42480` non-simple residual cycles and `20520`
  residual corner-label violations over `Q`. Conditioning on the exact local
  overlap cover shows the remaining sampled failures are residual, not hidden
  proper overlaps: a seed-`20260602`, `50000`-attempt exact sampler outside the
  cover found only residual corner-label violations and connected non-simple
  residual graphs with one or more degree-4 pinch vertices. The all-full
  residual atom profiles in that sample have no side-parity mismatch, so a
  parity-only residual invariant is not enough. The non-2-degree residual
  vertices in the same run have only two incident-label profiles, `accc` and
  `aabc`, making those local pinch stars the next finite obstruction target.
  The sector pass now marks shell-occupied sectors and classifies the
  `alpha`/`gamma`/`pi` sector angles exactly; every sampled `accc` pinch has
  locally unfillable residual sectors, while pure `aabc` pinches are locally
  fillable and need a stronger component/topology invariant. In a
  seed-`20260602`, `10000`-attempt outside-cover sample, this refines the former
  non-simple bucket into `250` local pinch-sector obstructions and `43`
  locally fillable non-simple graphs for `63`, and `895` plus `218` for `99`.
  An exact split-cycle
  component diagnostic now checks planar pairings, component areas, boundary
  side-count bounds, side parity, and split component corner labels. The same
  sample reclassifies all locally fillable non-simple residual graphs as
  split-corner-label obstructions, leaving only exact residual obstruction
  statuses in the sampled outside-cover remainder. The deterministic capped
  residual census now promotes the entire total-mixed-`<=4` exact shell space:
  `63` has `4896` residual corner-label violations and `6144`
  split-corner-label obstructions, while `99` has `20520` and `42480`.
  The exact local-overlap cover removes `940800` of the `1356640` mixed-`6`
  shells for `63` and `7941960` of the `13809000` mixed-`6` shells for `99`;
  the outside-cover mixed-`6` remainders are still unclassified. Grouping those
  remainders by endpoint/mixed boundary signatures collapses them to `26`
  groups for each row; the largest cap-`6` targets are mixed splits
  `(2,1,3)`, `(1,2,3)`, and `(2,2,2)` for `63`, and `(2,2,2)`, `(2,1,3)`,
  and `(1,2,3)` for `99`. A stratified representative probe reaches all `20`
  mixed-`6` endpoint groups in both rows, and every probed representative
  already has one of the exact residual obstruction statuses; the missing step
  is proving that those obstructions cover whole groups rather than selected
  representatives. A two-representative `99` probe shows mixed statuses inside
  the `(1,3,2)` endpoint groups, so endpoint/mixed grouping alone is too coarse.
  Adding oriented fan-transition data to the count-only profile goes too far in
  the other direction: the mixed-`6` outside-cover remainder has `120224`
  fan-profile groups for `63` and `1080609` for `99`. The next promising
  quotient should use residual obstruction certificates rather than boundary
  profiles alone; raw label-word triples are also too fine, with `40560`
  mixed-`6` groups for `63` and `418260` for `99`. A first
  residual-certificate probe on `50` mixed-`6`
  outside-cover shells gives only corner-label violations but already splits
  into `17` certificate types for `63` and `18` for `99`, so even the residual
  proof likely needs a structural forced-corner lemma rather than a tiny
  certificate table. Extending the local-overlap test from the default sampled
  pairs to every possible equal-side/base boundary-tile position pair gives no
  additional coverage for either benchmark row; the high-mixed outside-cover
  mass is therefore not a missed local side-base overlap. For `63`, the
  outside-cover counts at mixed `8`, `10`, and `12` are `3382720`,
  `9122560`, and `6389760`; for `99`, they are `136555720`, `1050178232`,
  and `1917116232`. The chunked coarse census now gives a resumable exact
  counting path; its first `63` mixed-`6` outside-cover chunk processed `2000`
  generated shells, with `970` local-cover hits and outside-cover statuses
  `838` corner-label violations plus `192` non-simple residual graphs. Through
  generated shell `10000`, the cumulative exact coarse counts are `4899`
  local-cover hits, `4077` corner-label violations, and `1024` non-simple
  residual graphs. Through generated shell `100000`, the cumulative exact
  coarse prefix counts are `52430` local-cover hits, `28326` corner-label
  violations, and `19244` non-simple residual graphs. The recorded refined
  replay of that same first `100000` generated shells has `52430` local-cover
  hits and splits the `47570` outside-cover shells as `28326` corner-label
  violations, `3332` pinch-sector obstructions, and `15912`
  split-corner-label obstructions. Through generated shell `200000`, lazy
  local-cover mode gives cumulative coarse counts `139104`, `34292`, and
  `26604`. Through generated shell `500000`, the cumulative exact coarse prefix
  counts are `358826`, `61534`, and `79640`. The recorded refined chunks
  through generated shell `500000` exactly refine that prefix: `358826`
  local-cover hits, `61534` corner-label violations, `21816` pinch-sector
  obstructions, and `57824` split-corner-label obstructions. The full
  mixed-`6` `63` refined pass is now exact: `940800` local-cover hits,
  `207888` residual corner-label violations, `58224` pinch-sector
  obstructions, and `149728` split-corner-label obstructions. This closes the
  mixed-exactly-`6` finite shell stratum for `63`; higher mixed counts still
  need a structural cutoff or a broader exact pass. First recorded
  high-mixed certificate slices for `63`, outside the local cover, remain
  within the same obstruction vocabulary: among the first `1000` diagnosed
  shells at mixed `8`, `904` are corner-label violations and `96` are
  split-corner-label obstructions; at mixed `10` and `12`, each first slice has
  `838` corner-label violations and `162` pinch-sector obstructions. The
  analogous first `99` mixed-`6` slice has `782` corner-label violations and
  `218` split-corner-label obstructions.
- `n = 66`, `n = 69`, and `n = 70` impossible in this workspace: these
  squarefree composite counts are outside the elementary positive forms, and
  exact equilateral plus source-row filters leave no survivor.
- `n = 76` and `n = 92` impossible in this workspace: all source rows are empty
  or locally eliminated, and the only `gamma=2alpha` survivor in each case is
  removed by the local c-edge lower-bound/base endpoint refinement plus Beeson
  Lemma 11.17.
- `n = 78`, `n = 86`, `n = 87`, `n = 88`, `n = 91`, `n = 93`, `n = 94`, and `n = 95`
  impossible in this workspace: these squarefree composite counts are outside
  the elementary positive forms except for non-squarefree `88`, whose
  `gamma=2alpha` enumeration is empty; exact equilateral scans are empty
  except for two `95` candidates, and those fail the boundary-star check.
- Primes `p = 4r + 3` are explicitly not proved impossible in the source
  corpus. Beeson says this is a hope, not even labelled a conjecture in his
  slides. This workspace now records a derived proof of the prime obstruction,
  assuming the source case reductions summarized in `PROOF.md`.
- `p = 19` is the benchmark case listed as open in the source corpus; this
  workspace now records a derived obstruction ruling it out.
- A 2026 external GitHub draft by David Turturean claims a full prime-count
  dichotomy matching the workspace prime ledger. Keep this separate from the
  published source corpus until independently checked. First pass: Beeson IV
  supports local reuse of Lemma 12's sweep technique, but the draft's
  base-corner setup and width contradiction remain unaudited.
- Beeson's isosceles `gamma=2pi/3` arithmetic filter is now fully removed by a
  local boundary-transition lemma: an outer base side with `alpha` corners at
  both ends cannot be tiled by full tile sides once the side labels in the
  straight boundary vertex stars are enforced.
- If the small triangle is similar to the large triangle, Snover-Waiveris-Williams give the complete restrictions: `N` is a square, a sum of two squares, or three times a square.
- `SOURCE_REDUCTION_AUDIT.md` records the exact source-reduction bridges still
  needed before the current "no encoded survivor" dashboards can be promoted to
  negative classifications.

## Small Cases Ledger

| n | status | reason |
|---:|:---|:---|
| 1 | positive | trivial |
| 2 | positive | isosceles triangle bisected by symmetry altitude |
| 3 | positive | equilateral triangle by joining center to vertices |
| 4 | positive | square family |
| 5 | positive | `1^2 + 2^2` |
| 6 | positive | primitive `6` or `6*1^2` |
| 7 | negative | Beeson theorem |
| 8 | positive | `2*2^2` or `2^2+2^2` |
| 9 | positive | square family |
| 10 | positive | `1^2+3^2` or `2*?` |
| 11 | negative | Beeson theorem |
| 12 | positive | `3*2^2` |
| 13 | positive | `2^2+3^2` |
| 14 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 15 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 16 | positive | square family |
| 17 | positive | `1^2+4^2` |
| 18 | positive | `2*3^2` |
| 19 | negative in this workspace | source reductions plus boundary integrality in final BLZ `gamma=2pi/3` cases |
| 20 | positive | `2^2+4^2` |
| 21 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 22 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 23 | negative in this workspace | prime `3 mod 4` source reduction |
| 24 | positive | `6*2^2` |
| 25 | positive | square family |
| 26 | positive | `1^2+5^2` |
| 27 | positive | `3*3^2` |
| 28 | positive | Beeson `3alpha+2beta=pi` table |
| 29 | positive | `2^2+5^2` |
| 30 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 31 | negative in this workspace | prime `3 mod 4` source reduction |
| 32 | positive | `2*4^2` |
| 33 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 34 | positive | `3^2+5^2` |
| 35 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 36 | positive | square family |
| 37 | positive | `1^2+6^2` |
| 38 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 39 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 40 | positive | `2^2+6^2` |
| 41 | positive | `4^2+5^2` |
| 42 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 43 | negative in this workspace | prime `3 mod 4` source reduction |
| 44 | positive | Beeson `3alpha+2beta=pi` table |
| 45 | positive | `3^2+6^2` |
| 46 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 47 | negative in this workspace | prime `3 mod 4` source reduction |
| 48 | positive | Beeson `3alpha+2beta=pi` table |
| 49 | positive | square family |
| 50 | positive | `1^2+7^2` |
| 51 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 52 | positive | `4^2+6^2` |
| 53 | positive | `2^2+7^2` |
| 54 | positive | `6*3^2` |
| 55 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 56 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 57 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 58 | positive | `3^2+7^2` |
| 59 | negative in this workspace | prime `3 mod 4` source reduction |
| 60 | negative in this workspace | source case split plus local `gamma=2alpha` c-edge/base endpoint/Lemma 11.17 obstruction |
| 61 | positive | `5^2+6^2` |
| 62 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 63 | open in this workspace | final `gamma=2alpha` boundary pattern survives without no-overhang lemma |
| 64 | positive | square family |
| 65 | positive | `1^2+8^2` |
| 66 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 67 | negative in this workspace | prime `3 mod 4` source reduction |
| 68 | positive | `2^2+8^2` |
| 69 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 70 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 71 | negative in this workspace | prime `3 mod 4` source reduction |
| 72 | positive | `2*6^2` |
| 73 | positive | `3^2+8^2` |
| 74 | positive | `5^2+7^2` |
| 75 | positive | `3*5^2` |
| 76 | negative in this workspace | source case split plus local `gamma=2alpha` c-edge/base endpoint/Lemma 11.17 obstruction |
| 77 | positive | Beeson `3alpha+2beta=pi` table |
| 78 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 79 | negative in this workspace | prime `3 mod 4` source reduction |
| 80 | positive | `4^2+8^2` |
| 81 | positive | square family |
| 82 | positive | `1^2+9^2` |
| 83 | negative in this workspace | prime `3 mod 4` source reduction |
| 84 | positive | Beeson `3alpha+2beta=pi` table |
| 85 | positive | `2^2+9^2` |
| 86 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 87 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 88 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 89 | positive | `5^2+8^2` |
| 90 | positive | `3^2+9^2` |
| 91 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 92 | negative in this workspace | source case split plus local `gamma=2alpha` c-edge/base endpoint/Lemma 11.17 obstruction |
| 93 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 94 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 95 | negative in this workspace | source case split plus exact composite benchmark in `PROOF.md` |
| 96 | positive | `6*4^2` |
| 97 | positive | `4^2+9^2` |
| 98 | positive | `2*7^2` |
| 99 | open in this workspace | final `gamma=2alpha` boundary pattern survives without no-overhang lemma |
| 100 | positive | square family |

Important distinction: "positive square class" and "smallest representative" are different. A construction of `15m^2` for all large `m` proves positive infinitely many `n` with squarefree kernel `15`, but it does not prove `n=15`.

## Research Threads

1. Normalize tile coordinates and derive all boundary vectors of possible tiled triangles from sums of edge vectors.
2. Classify rep-tile cases separately from non-similar tilings.
3. Generate explicit coordinate certificates for each claimed construction family.
4. Reproduce known impossibility proofs for `7` and `11`.
5. Test small `n` by combinatorial enumeration of triangular tiling graphs plus nonlinear side/angle feasibility checks.
6. Keep the `71` length-only side-matching and lattice-coloring diagnostics as
   sanity checks for future invariants, but the boundary-transition lemma is now
   the decisive isosceles `gamma=2pi/3` obstruction.
7. With prime cases classified and the first small composite obstructions
   through `55` promoted to workspace negative theorems, shift effort back to
   the remaining composite values not covered by the positive families.
   The exact equilateral
   boundary-length scan gives candidates:
   `14` from the `2pi/3` tile `(7,8,13)` in an equilateral side-`28` triangle,
   and `15` from `(3,5,7)` in an equilateral side-`15` triangle. The
   `equilateral_gamma_boundary.py` full-boundary star check eliminates both
   candidates before any interior search; combined with the source split and
   the `3alpha+2beta` filters, this now gives negative workspace proofs for
   both counts.
   The same equilateral boundary-star workflow eliminates the exact
   `pi/3` candidates for `21` and `30`, namely `(16,21,19)` in side `84` and
   `(8,15,13)` in side `60`, including their `a,b` swaps; combined with the
   source split and non-isosceles `gamma=2pi/3` endpoint checks, this now gives
   negative workspace proofs for both counts.
   The composite dashboard currently shows two remaining open values below
   `100`, namely `63` and `99`, both through final `gamma=2alpha` boundary
   patterns. Values
   `14`, `15`, `21`, `22`, `30`, `33`, `35`, `38`, `39`, `42`, `46`, `51`,
   `55`, `56`, `57`, `60`, `62`, `66`, `69`, `70`, `76`, `78`, `86`,
   `87`, `88`, `91`, `92`, `93`, `94`, and `95` are now upgraded from
   dashboard evidence to proof entries.
   The newer
   eliminations beyond `30` include a generic `3alpha+2beta` boundary-integrality
   filter for supported triquadratic, isosceles-beta, and isosceles-alpha
   outer shapes; `46` and `56` by triquadratic boundary-star checks; and
   `55`, `88`, `105`, `120`, and `143` by non-isosceles `gamma=2pi/3`
   endpoint boundary-star checks. In the range `100..250`, the former
   `3alpha+2beta` isosceles-`alpha+beta` survivor records at `132`, `156`,
   `175`, `189`, `198`, `204`, `224`, `228`, and `240` are now removed by a
   boundary order plus side-difference nonfit obstruction, with `240` requiring
   a separate resonant `a/c` overhang endpoint argument because `c-a=12=3a`.
   Separate `gamma=2alpha` survivors in this range still require the
   no-overhang fan gap or another obstruction; the active `100..250` gamma
   survivor values are `132`, `135`, `156`, `171`, `175`, `176`, `189`, `198`,
   `204`, `207`, `224`, `228`, and `240`.
   A recurring subfamily has consecutive Lemma 11.14 parameters
   `(k,m)=(t,t+1)`, sides `(t^2,2t+1,t(t+1))`, relation `a+c=t b`, and
   boundary-survivor count `N=9(2t+1)`. Its boundary words are
   `L=baa b^(t-2) ccb`, `R=aa b^t cc`, and `B=baaabbccc`, with boundary
   counts `(7,2t+3,7)` and interior counts `(18t+2,16t+6,18t+2)`.
   The current boundary DP finds that every active gamma survivor below `250`
   needs only four outer-boundary `c`/non-`c` transitions, so any obstruction
   must account for four overhang rays globally. For the benchmark rows, the
   stronger all-straight-boundary fan inventory still leaves side-incidence
   slack, so the next obstruction has to use placement/order information rather
   than only counting labels consumed by local fans. A boundary-shell residual
   search is now the most concrete next construction/obstruction route; `99`
   is the cleaner first target because the residual shell boundary is a single
   simple cycle in the current floating model. Exact residual corner-label
   passes rule out the displayed minimum-transition shells for both benchmark
   values, but not yet all possible boundary orderings. A finite census over
   the eight canonical endpoint-minimal representatives for each of `63` and
   `99` also eliminates those representatives by overlap, non-simple residual
   boundary, or residual corner-label mismatch. A randomized noncanonical shell
   sampler found no survivor in fixed-seed `30000`-attempt runs (`795` unique
   shells for `63`, `648` for `99`), but this is evidence rather than an
   exhaustive certificate. The exact `Q(sqrt(d))` sampler also found no pass in
   an uncapped seed-`6342026`, `200000`-attempt run (`5247` unique `63` shells,
   `4270` unique `99` shells), or in a valid-weighted seed-`20260601`,
   `50000`-attempt run that produced `49991` valid `63` shells and `50000`
   valid `99` shells. Exact overlap-cause sampling on the valid-weighted run
   shows proper overlaps concentrate at base/equal-side pairs, especially
   `L2` with `B8` and the symmetric right-base positions; no new first-overlap
   positions appeared beyond the current local pair set. Turning those sampled local
   positions into exact count filters covers `276555680` of `295877600`
   boundary shells for `63`, and `8012836776` of `11122617000` boundary shells
   for `99`; after subtracting the already-closed mixed-`4` row, the remaining
   high-mixed spaces are `19310880` and `3109717224` shells respectively.
   Expanding to the full nearby base-corner position bands does not improve the
   cover, so the remaining shells avoid that whole local overlap mechanism. A
   seed-`20260602`, `50000`-attempt sample conditioned outside the local cover
   found no proper overlaps: `63` split `1747/1496` between residual
   corner-label violations and non-simple residual graphs, and `99` split
   `8512/5594`.
   A stratified low-overhang run with total mixed
   count at most `4` found `189` unique `63` shells and `143` unique `99`
   shells, again with no pass. The full low-overhang census is now exact: all `11040`
   shells for `63` are eliminated over `Q(sqrt(5))` (`6144` non-simple,
   `4896` corner-label violations), and all `63000` shells for `99` are
   eliminated over `Q` (`42480` non-simple, `20520` corner-label violations).
   Higher-mixed boundary orders remain open. A count-only mixed-growth
   diagnostic shows the full boundary-order spaces plateau at `295877600`
   shells for `63` and `11122617000` shells for `99`, so the remaining attack
   needs a structural quotient or obstruction rather than raw exact shell
   enumeration. The aggregate boundary-fan frontier does not supply that
   obstruction: all `88` endpoint/mixed classes remain feasible under local fan
   side-incidence counts for both benchmark rows.

## Current Diophantine Status for `n=19`

After the source reductions now recorded in `PROOF.md`, the main remaining
`19` target is the pair of BLZ non-isosceles `gamma=2pi/3` square-class filters:

```text
(alpha,2alpha,3beta):       19 = ((a+2b)/(3(a+b))) q^2,
(alpha,2beta,2alpha+beta):  19 = ((b+2a)/(a+b)) q^2,
c^2 = a^2 + ab + b^2,       gcd(a,b)=1.
```

Writing `S=a+b` and `A=a+2b` or `A=b+2a`, the side equation becomes

```text
c^2 = A^2 - 3AS + 3S^2.
```

For the second BLZ filter, the prime condition forces square-class pairs
`(A,S)=(u^2,19v^2)` or `(19u^2,v^2)`, giving quartics with Jacobian

```text
E2: y^2 = x(x^2 + 114x - 1083).
```

For the first BLZ filter, the possible square-class pairs are
`(u^2,57v^2)`, `(3u^2,19v^2)`, `(19u^2,3v^2)`, and `(57u^2,v^2)`, with common
Jacobian

```text
E1: y^2 = x(x^2 + 342x - 9747).
```

This square-class obstruction is not enough. Exact witnesses exist:

```text
(alpha,2beta,2alpha+beta):
  (a,b,c) = (1131561,358039,1346761),
  (A,S) = (1619^2, 19*280^2).

(alpha,2alpha,3beta):
  (a,b,c) =
  (64291453825267166692191813022145,
   3194650169777924718531451006912,
   65946838654721589964381492334497),
  (A,S) = (8407184675313313^2, 57*1088102355826499^2).
```

Both satisfy `S < A < 2S` and `c^2 = A^2 - 3AS + 3S^2`. Boundary integrality
then rules them out: the primitive outer side ratios have gcd `1`, so their
scale must be an integer. This forces counts of the form

```text
(alpha,2beta,2alpha+beta):  N = (b+2a)(a+b)m^2 >= 88,
(alpha,2alpha,3beta):       N = 3(a+2b)(a+b)m^2 >= 264.
```

The same boundary-integrality product formulas rule out the two remaining BLZ
non-isosceles `gamma=2pi/3` templates for every prime `N`: their counts must be
`(b+2a)(a+b)m^2` or `3(a+2b)(a+b)m^2`.

## Additional Small Positive Values From Beeson

The elementary families do not explain every known small positive value. Beeson's
`3alpha+2beta=pi` paper lists tilings for `N = 28,44,48,77,84`, all with tile
`(2,3,4)` in that template. Its recorded triquadratic sufficient condition also
gives `112`, `126`, and `153` below `250`; `112` and `126` are new to the
current small-value ledger.

## Current `n=19` Reduction Notes

- Similar/reptile case: impossible by Snover-Waiveris-Williams, since `19` is
  not a square, not `3m^2`, and not a sum of two squares.
- Equilateral outer triangle: impossible by Beeson's theorem that prime `N>3`
  cannot occur for equilateral `ABC`.
- `3alpha+2beta=pi`: ruled out by Beeson's theorem that prime `N` cannot occur
  in this template. The rational necessary-equation filter initially leaves four
  isosceles-`alpha+beta` candidates, but Beeson's stronger Section 11.4 filter
  eliminates them.
- Isosceles outer triangle with `gamma=2pi/3`: ruled out by Beeson's necessary
  arithmetic filter, since `19` has no candidate satisfying
  `c^2=a^2+ab+b^2`, `2b+a | N`, and `N b/(2b+a)` square.
- Other isosceles outer-triangle subcases are also source-ruled for `19`:
  right-tile counts exclude primes `3 mod 4`, `gamma=2alpha` counts are not
  squarefree, and `3alpha+2beta=pi` has no prime counts.
- Non-isosceles `gamma=2pi/3`: BLZ formulas rule out prime counts in the
  `(alpha,alpha+beta,alpha+2beta)` and `(2alpha,2beta,alpha+beta)` templates.
  The remaining two templates have exact `N=19` square-class arithmetic
  witnesses, but boundary-integrality upgrades their counts to composite
  integer product forms for every prime.
- Zhang's proved `2pi/3` and `pi/3` constructions do not produce `19`; this is
  only a positive-family limitation, not an obstruction.
- With those boundary lower bounds, all currently recorded source-reduced cases
  for `N=19` are ruled out.
