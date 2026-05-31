# Source-Reduction Audit for Problem #634

This file records the remaining theorem-level obligations needed before the
current computational/proof filters can be promoted to a complete classification.
It is deliberately conservative: an empty dashboard is not a negative theorem
unless every possible tiling has first been reduced to the encoded cases.

## Current Reduction Backbone

The workspace uses these source-level reductions as inputs:

1. Snover-Waiveris-Williams classifies the similar/reptile subcase.
2. Beeson proves `N=7` and `N=11` impossible.
3. Beeson proves an equilateral outer triangle with `N>3` cannot have prime
   `N`.
4. Beeson proves prime `N` is impossible in the `3alpha+2beta=pi` template.
5. Beeson's isosceles-triangle reductions list right-tile, `gamma=2alpha`,
   `gamma=2pi/3`, and `3alpha+2beta=pi` subcases.
6. BLZ gives non-isosceles `gamma=2pi/3` templates and count formulas.
7. BLZ Problem #633 classifies outer triangles that admit a non-square tiling.

The workspace has independently strengthened several filters, especially:

- prime `p == 3 mod 4`, `p>3`, now ruled out using source reductions plus
  boundary-integrality and boundary-transition lemmas;
- exact equilateral boundary-length arithmetic for the first composite targets;
- local boundary-star eliminations for many small composite candidates.

## Published Laczkovich/Beeson Global Tables

The commensurable-angle branch is source-closed. In Beeson's NoSevenTiling,
Table 3 lists the possible `N` forms for congruent tilings whose tile angles
are rational multiples of `pi`, and Theorem 3 states that every such tiling
corresponds to one of the table lines. The resulting count forms are exactly:

```text
m^2,
a^2+b^2,
2m^2,
3m^2,
6m^2.
```

Beeson's Table 4 records the complementary Laczkovich finite list when not all
tile angles are rational multiples of `pi`. The rows are:

```text
similar to the outer triangle,
equilateral with alpha = pi/3,
isosceles/right-tile gamma = pi/2,
isosceles gamma = 2alpha,
three rows with 3alpha+2beta = pi,
five non-equilateral rows with gamma = 2pi/3,
equilateral with gamma = 2pi/3.
```

This closes the previously vague commensurable-table item. It does not close
the incommensurable rows: for those rows the workspace still has to match each
source hypothesis exactly to the encoded arithmetic filters.

## BLZ #633 Row Map Into #634

BLZ Theorem 1 is a useful global cover for #634 non-square cases: if an
`N`-tiling with non-square `N` exists, then its outer triangle is itself an
outer triangle admitting a non-square tiling, so its similarity class appears in
one of the eight BLZ rows. The caveat is essential: BLZ #633 classifies outer
triangles, not the possible tile counts for each outer triangle. Therefore the
rows below are a source-reduction map, not a classification of `N`.

| BLZ row | outer-triangle condition | #634 workspace route | current count status |
|---:|---|---|---|
| 1 | `A=B` | Split into equilateral and non-equilateral isosceles. Equilateral uses Beeson's equilateral theorem plus the `pi/3` and `2pi/3` integer-side models. Non-equilateral uses Beeson's isosceles reductions: right-tile, `gamma=2alpha`, `gamma=2pi/3`, and `3alpha+2beta=pi`. | Prime obstruction and several local composite eliminations; composite count classification incomplete. |
| 2 | `C=pi/2`, legs have integer ratio `M/K`, `M^2+K^2` nonsquare | Similar/reptile sum-of-two-squares construction and right-triangle arithmetic; overlaps the commensurable/right-tile branches. | Positive family `M^2+K^2` times squares is explicit. Arbitrary non-similar tilings of the same outer shape still need the relevant source branch. |
| 3 | `(pi/6,pi/2,pi/3)` | Similar/reptile `3m^2` branch and commensurable-angle table; also related to the elementary `6m^2` construction after changing the outer triangle. | Positive `3m^2` and `6m^2` families are explicit; exact non-similar count completeness is tied to the commensurable table. |
| 4 | `C=pi/3`, `sqrt(3)tan(A/2)` rational | Non-isosceles `gamma=2pi/3` rows with a `pi/3` outer angle, especially BLZ Propositions 24 and 31; equilateral is the row-1 overlap. | Exact formulas are encoded for Propositions 24 and 31; primes are obstructed. Composite coverage is only partial. |
| 5 | `B=2A`, `sqrt(3)tan(A/2)` rational | Non-isosceles `gamma=2pi/3` template `(alpha,2alpha,3beta)` from BLZ Proposition 26. | Square-class filter plus boundary-integrality product formula; prime obstruction proved, composite classification incomplete. |
| 6 | `B=2A`, `sin(A/2)` rational | Beeson `3alpha+2beta=pi` template, notably the `(2alpha,alpha,2beta)` branch after reordering. | Necessary equations and selected sufficient constructions encoded; Beeson prime theorem quoted; composites incomplete. |
| 7 | `C=A/2+B`, `2sin(A/4)=M/K`, `2K^2-M^2` nonsquare | Beeson triquadratic `3alpha+2beta=pi` branch `(2alpha,beta,alpha+beta)`. | Sufficient subfamily `N=2K^2-M^2` when the source divisibility condition holds; otherwise only necessary diagnostics. |
| 8 | `C=2A+B/2`, `sqrt(3)tan(A/2)` rational | Non-isosceles `gamma=2pi/3` template `(alpha,2beta,2alpha+beta)` from BLZ Proposition 28. | Square-class filter plus boundary-integrality product formula; prime obstruction proved, composite classification incomplete. |

Rows 2 and 3 explain two of the elementary positive mechanisms, while rows 4,
5, and 8 align with the four BLZ non-isosceles `gamma=2pi/3` formulas after
choosing the appropriate angle ordering. Rows 6 and 7 align with named
`3alpha+2beta=pi` branches. Row 1 remains the largest gap because it contains
all isosceles outer triangles, including the equilateral special case.

## Encoded Count Forms

This table records the arithmetic forms actually tested by the workspace. A
row marked "diagnostic" is a necessary-filter implementation or local
elimination, not a complete classification of that source case.

| source case | encoded count forms or constraints | status |
|---|---|---|
| Commensurable-angle table | `m^2`, `a^2+b^2`, `2m^2`, `3m^2`, `6m^2` | Complete for this branch by Beeson's NoSevenTiling Table 3 and Theorem 3. |
| Similar/reptile | `m^2`, `a^2+b^2`, `3m^2` | Complete for this subcase by Snover-Waiveris-Williams. |
| Equilateral `pi/3` tile model | Primitive integer sides `c^2=a^2-ab+b^2`, outer side `L^2=Nab`, boundary length `L=xa+yb+zc`. | Source rationality bridge closed by Laczkovich/Beeson; exact arithmetic scan plus boundary-star eliminations for selected small candidates. |
| Equilateral `2pi/3` tile model | Primitive integer sides `c^2=a^2+ab+b^2`, outer side `L^2=Nab`, boundary length `L=xa+yb+zc`. | Source rationality bridge closed by Laczkovich/Beeson; exact arithmetic scan plus boundary-star eliminations for selected small candidates. |
| Beeson `3alpha+2beta=pi`: triquadratic | `N/M^2=2/s^2-1`, with sufficient subfamily `N=2K^2-M^2` when `s=M/K` and `K|M^2`. | Necessary filter plus one sufficient family; generic boundary-integrality filter for candidates with irrational or nonintegral area-normalized outer sides; composites not complete. |
| Beeson `3alpha+2beta=pi`: `(2alpha,alpha,2beta)` | `N/M^2=(2-s^2)(3-s^2)/((1-s)^2(2+s)^2)`, sufficient when reconstructed sides satisfy `c|a^2`. | Necessary filter plus one sufficient criterion; composites not complete. |
| Beeson `3alpha+2beta=pi`: isosceles-beta | `N/M^2=(3-s^2)/(1+s)^2`. | Necessary diagnostic plus generic boundary-integrality filter, except listed source examples. |
| Beeson `3alpha+2beta=pi`: isosceles-`alpha+beta` | `N/M^2=(1+s)/(1-s)`, with a stronger source filter encoded separately. | Necessary diagnostic plus selected local eliminations. |
| Beeson `3alpha+2beta=pi`: isosceles-alpha | `N/M^2=(1+s)(2-s^2)/((1-s)(2+s)^2)`. | Necessary diagnostic plus generic boundary-integrality filter, except listed source examples. |
| Isosceles `gamma=2pi/3` | Primitive sides `c^2=a^2+ab+b^2`, divisibility `2b+a | N`, and `Nb/(2b+a)` square. | Arithmetic candidates are removed by the local boundary-transition lemma in the rational nondegenerate case; source exceptional cases still need auditing. |
| Non-isosceles `gamma=2pi/3`: `(alpha,alpha+beta,alpha+2beta)` | `N=((a+b)/b)m^2`, with `c^2=a^2+ab+b^2`. | Exact formula; primes obstructed; endpoint boundary-star filter applied to composites. |
| Non-isosceles `gamma=2pi/3`: `(2alpha,2beta,alpha+beta)` | `N=(a+2b)(b+2a)m^2`, with `c^2=a^2+ab+b^2`. | Exact formula; primes obstructed; endpoint boundary-star filter applied to composites. |
| Non-isosceles `gamma=2pi/3`: `(alpha,2beta,2alpha+beta)` | Boundary-integrality upgrades BLZ's square class to `N=(b+2a)(a+b)m^2`. | Prime obstruction proved; endpoint boundary-star filter applied to composites. |
| Non-isosceles `gamma=2pi/3`: `(alpha,2alpha,3beta)` | Boundary-integrality upgrades BLZ's square class to `N=3(a+2b)(a+b)m^2`. | Prime obstruction proved; endpoint boundary-star filter applied to composites. |

## What Is Theorem-Level Locally

These items are internally reconstructed enough to be used as proof components
once the relevant source-reduction hypotheses are accepted:

| component | local status |
|---|---|
| Elementary positive families | coordinate/geometric constructions in `PROOF.md` |
| Similar/reptile counts | source theorem quoted with exact arithmetic alternatives |
| Commensurable-angle counts | closed by Beeson's NoSevenTiling Table 3 and Theorem 3 |
| Prime obstruction for non-isosceles `gamma=2pi/3` | BLZ formulas plus local boundary-integrality product formulas |
| Isosceles `gamma=2pi/3` obstruction | local boundary-transition lemma |
| Exact equilateral boundary-length arithmetic | source rationality plus `equilateral_boundary_exact.py` finite rational-root enumeration |
| Equilateral `pi/3` and `2pi/3` local boundary checks | `equilateral_pi_boundary.py`, `equilateral_gamma_boundary.py` |
| `3alpha+2beta=pi` boundary/integrality eliminations | `beeson_3alpha2beta_boundary.py` |
| Selected non-isosceles `gamma=2pi/3` boundary eliminations | `gamma_2pi3_nonisosceles_boundary.py` |

## Missing Bridges And Closed Checks

### 1. Incommensurable Source-Row Count Restrictions

Needed statement:

> Each incommensurable row in Beeson's Table 4 has exactly the count
> restrictions encoded by the corresponding workspace filter.

Current evidence:

- `PROOF.md` now records the source-level global split: Snover-Waiveris-
  Williams for the similar case, Beeson's Table 3/Theorem 3 for the
  commensurable branch, and Beeson's Table 4 for the incommensurable finite
  list.
- The BLZ #633 outer-triangle row map is recorded above as a second organizing
  map, but it classifies outer-triangle similarity classes rather than #634
  tile counts.

Impact:

- Without row-by-row count restrictions for the incommensurable cases, small
  values with no encoded survivors are not yet negative.

### 2. Isosceles Composite Reductions

Needed statement:

> Non-equilateral isosceles outer triangles reduce exactly to the right-tile,
> `gamma=2alpha`, `gamma=2pi/3`, and `3alpha+2beta=pi` subcases with the
> arithmetic restrictions recorded in `PROOF.md`.

Current evidence:

- This is summarized from Beeson's isosceles paper.
- `PROOF.md` now records the right-tile count forms from Theorem 7.8 and the
  `gamma=2alpha` non-squarefree obstruction from Theorem 11.7.
- `gamma=2pi/3` has a local boundary-transition obstruction.
- The `gamma=2pi/3` arithmetic filter is encoded from Lemma 12.9 and Theorem
  12.10.

Impact:

- The right-tile and `gamma=2alpha` rows are now source-backed enough for
  small-value obstructions such as `N=22`; the remaining isosceles gap is exact
  composite completeness in the `gamma=2pi/3` and `3alpha+2beta=pi` rows.

### Closed Check: Equilateral Rational/Integer Side Model

Closed statement:

> Every equilateral outer-triangle tiling in the relevant source cases either
> is handled by Beeson's prime theorem/commensurable table or has rational tile
> side ratios with a distinguished tile angle `pi/3` or `2pi/3`.

Current evidence:

- Beeson's equilateral paper quotes Laczkovich's equilateral classification and
  rationality theorem for the incommensurable `pi/3` and `2pi/3` cases.
- With rationality and the distinguished `pi/3` or `2pi/3` angle accepted,
  `PROOF.md` now derives the integer-side model
  `c^2=a^2±ab+b^2`, `L^2=Nab`, and `L=xa+yb+zc` with
  `0 < x+y+z <= N`.
- The exact boundary-length script proves finiteness inside this model.

Impact:

- For `14`, `15`, `21`, `22`, and `30`, the exact equilateral model is fully
  eliminated locally.

### 3. Composite `3alpha+2beta=pi` Completeness

Needed statement:

> Beeson's necessary equations for the five `3alpha+2beta=pi` outer shapes are
> exactly the complete set of composite candidates, and the workspace's stronger
> filters are valid for each shape.

Current evidence:

- `beeson_3alpha2beta_filter.py` encodes the five final equations.
- `PROOF.md` now records the Section 11.4 necessary conditions for the
  isosceles-`alpha+beta` branch; `beeson_isosceles_alpha_plus_beta_filter.py`
  encodes that source filter.
- `beeson_3alpha2beta_boundary.py` removes selected boundary-star survivors
  and now applies the generic boundary-integrality obstruction to every
  supported `3alpha+2beta=pi` outer shape.

Impact:

- The generic boundary-integrality obstruction now removes all supported
  `3alpha+2beta=pi` branches below `250` except the isosceles-`alpha+beta`
  source-filter branch. The remaining `3alpha+2beta` survivors in the
  `100..250` scan are all in that branch. This is still conditional on the full
  `3alpha+2beta=pi` source setup.

### 4. Composite Non-Isosceles `gamma=2pi/3` Completeness

Needed statement:

> The four BLZ non-isosceles `gamma=2pi/3` formulas, together with the
> boundary-integrality product formulas for the last two, cover all composite
> candidates in this non-isosceles source case.

Current evidence:

- `gamma_2pi3_nonisosceles_exact.py` encodes the exact arithmetic formulas.
- `gamma_2pi3_nonisosceles_boundary.py` now applies the endpoint-pair
  boundary-star obstruction to all four encoded BLZ templates.
- For `N=22`, the older BLZ square-class-only diagnostic still sees a
  `(3,5,7)` witness in the `(alpha,2beta,2alpha+beta)` template with
  coefficient `11/8`; this witness disappears only after applying the local
  boundary-integrality product upgrade to `N=(b+2a)(a+b)m^2`.

Impact:

- `21`, `30`, `55`, `88`, `105`, `120`, and `143` are eliminated locally.
- In the `100..250` diagnostic range the endpoint-pair check also removes the
  later BLZ survivors `154`, `168`, `210`, and `220`; no explicit
  non-isosceles `gamma=2pi/3` survivor remains in that range.

## Current Small-Value Status

The following unresolved values below `100` have no survivor in the currently
encoded filters:

```text
14, 15, 21, 22, 30, 33, 35, 38, 39, 42, 46, 51, 55, 56, 57,
60, 62, 63, 66, 69, 70, 76, 78, 86, 87, 88, 91, 92, 93, 94,
95, 99
```

They should remain recorded as "open/no encoded survivor" until the missing
bridges above are proved or accepted as source theorems with exact hypotheses.

In the range `100..250`, after the generic `3alpha+2beta`
boundary-integrality filter and the non-isosceles `gamma=2pi/3`
endpoint-pair boundary-star filter, the remaining values with explicit encoded
survivors are:

```text
132, 156, 175, 189, 198, 204, 224, 228, 240
```

The `3alpha+2beta` survivors among these are only the
isosceles-`alpha+beta` branch that passes Beeson's Section 11.4 filter.
The `--counts` diagnostic in `beeson_isosceles_alpha_plus_beta_filter.py`
records the remaining side-count structure. Most of these survivors are rigid
at the count level, but this is not yet an ordering or matching obstruction.

## Beeson IV Base-Corner Audit

The external Turturean prime-count draft uses a witness-level version of
Beeson's Triangle Tiling IV Lemma 12 at base corners of a residual isosceles
triangle. A direct check of the cached Triangle Tiling IV text gives the
following status:

- Lemma 12 itself is a local unsplit-vertex statement: after choosing a vertex
  `B` with exactly one `beta` tile, Beeson draws `B` at the top only as a
  coordinate convention and permits relabeling the two incident sides so that
  the corner tile is Type I.
- The proof explicitly says that the initial sweep argument in Direction `C`
  does not use the opposite side `AC`; only the final contradictions depend on
  the sweep hitting the two sides adjacent to `B`.
- Lemma 13 reuses the Lemma 12 technique inside a subtriangle with a new
  vertical and modified Type I/II definitions, which supports reapplication of
  the method when the same local hypotheses are restored.

This reduces the audit burden but does not eliminate it. To promote the draft's
argument to a theorem-level replacement for the workspace prime obstruction,
one must still verify the draft's setup lemmas: each base corner where the
lemma is used must be unsplit, have the required `beta` corner tile, and satisfy
the Type I side-label configuration and non-similar `gamma=2pi/3`,
`alpha != beta` hypotheses. Those facts are not consequences of Lemma 12 alone.

## Next Best Work

1. Formalize the count restrictions row-by-row for Beeson's incommensurable
   Table 4. The global finite case split and the commensurable branch are now
   recorded in `PROOF.md`.
2. Continue auditing Turturean's April 2026 prime-count draft against the local
   prime proof. The Beeson IV locality check is provisionally favorable; the
   remaining task is to verify the draft's base-corner setup lemmas and width
   contradiction. If accepted, use the draft to replace the current
   source-reduction-dependent prime obstruction with a cleaner theorem-level
   prime classification. This does not close the composite classification gap.
3. For a first theorem-level composite test case, target `N=22`. Among the
   currently unresolved values below `100`, it has the cleanest local profile:
   no exact equilateral candidates, no isosceles or non-isosceles
   `gamma=2pi/3` candidates, and only four `3alpha+2beta=pi`
   isosceles-`alpha+beta` raw candidates, all rejected by Beeson's stronger
   Section 11.4 filter. This now needs the remaining row-by-row composite
   count restrictions before it can be promoted from "no encoded survivor" to a
   negative theorem.
4. Build a corner-capped ordering/matching obstruction for the remaining
   `3alpha+2beta` isosceles-`alpha+beta` survivors, using `N=48` as the
   positive regression case.
5. Continue extending local boundary/integrality eliminations to larger
   composite survivors as they appear.
