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
7. With prime cases classified and `14`, `15`, `21`, `22`, and `30` promoted
   to workspace negative theorems, shift effort back to the remaining composite
   values not covered by the positive families. The exact equilateral
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
   The composite dashboard currently shows no surviving encoded candidates
   through the unresolved values below `100` checked in `RESULTS.md`, with
   `14`, `15`, `21`, `22`, and `30` now upgraded from dashboard evidence to
   proof entries. The newer
   eliminations beyond `30` include a generic `3alpha+2beta` boundary-integrality
   filter for supported triquadratic, isosceles-beta, and isosceles-alpha
   outer shapes; `46` and `56` by triquadratic boundary-star checks; and
   `55`, `88`, `105`, `120`, and `143` by non-isosceles `gamma=2pi/3`
   endpoint boundary-star checks. In the range `100..250`, explicit encoded
   survivors remain only at `132`, `156`, `175`, `189`, `198`, `204`, `224`,
   `228`, and `240`; all are `3alpha+2beta` isosceles-`alpha+beta`
   survivors.

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
