# Literature Notes

This file records source-derived claims and distinguishes them from reconstructed
arguments. The working rule is: source claims can be used as known inputs only
after their exact hypotheses are recorded.

## Source Map

- Problem #634 page and LaTeX: `https://www.erdosproblems.com/634`,
  `https://www.erdosproblems.com/latex/634`.
- Related Problem #633 page and LaTeX: `https://www.erdosproblems.com/633`,
  `https://www.erdosproblems.com/latex/633`.
- Beeson talk slides: `https://www.michaelbeeson.com/research/talks/TriangleTilingSlides.pdf`.
- Beeson, "No triangle can be cut into seven congruent triangles":
  `https://www.michaelbeeson.com/research/papers/NoSevenTiling.pdf`.
- Zhang, "Tiling Triangles With 2pi/3 Angles", arXiv:2512.22696.
- Beeson-Laczkovich-Zhang, "Solution of Erdos Problem 633", arXiv:2604.03609.
- Beeson related papers cited by Zhang and BLZ:
  `TriangleTilingEquilateral.pdf`, `IsoscelesTilings.pdf`, `TriangleTiling3.pdf`.
- David Turturean, "Triangle Dissections into a Prime Number of Congruent
  Triangles", GitHub draft `davidturturean/erdos-634`, April 2026. This is a
  useful outside draft for the prime-count subproblem, not a published source
  in the corpus above.

## Erdős Problems Page #634

The page states the problem:

> Find all `n` such that there is at least one triangle which can be cut into
> `n` congruent triangles.

Its additional text records the following state of knowledge.

- Squares occur; indeed every triangle has an `m^2` congruent-triangle tiling.
- Soifer showed that numbers of the forms `2m^2`, `3m^2`, `6m^2`, and
  `m^2+k^2` occur.
- Beeson showed that `7` and `11` do not occur.
- The page says it is possible that every prime `4r+3` does not occur.
- The page explicitly says it is not known whether `19` occurs.
- If congruence is relaxed to similarity, Soifer proved every triangle can be
  cut into `N` similar triangles for `N != 2,3,5`.
- If the small triangles are required to be similar to the large triangle, the
  page attributes to Snover-Waiveris-Williams the possible values
  `N = m^2`, `m^2+k^2`, or `3m^2`.
- The page summarizes Zhang's construction: for integers `a >= b`, sufficiently
  large `n` makes `n^2 ab` occur.
- As accessed on 2026-05-31, the page status is still `OPEN`, and it explicitly
  says the case `19` is not known on the site. The page also warns that status
  may lag the literature or comments.

Important correction/note: the #634 page text says Zhang tiles with side lengths
`a,b,sqrt(a^2+b^2+2+ab)`. Zhang's paper uses the law-of-cosines condition
`c^2 = a^2+b^2+ab` for a `2pi/3` angle. The `+2` on the problem page appears
to be a transcription error.

## Related Problem #633

Problem #633 asks for a classification of triangles that can only be cut into a
square number of congruent triangles.

The #633 page records:

- Every triangle has `m^2` congruent-triangle tilings.
- Soifer proved there exists a triangle, for example with sides
  `sqrt(2), sqrt(3), sqrt(4)`, that can only be cut into a square number of
  congruent triangles.
- Soifer's stronger condition: if a triangle's sides and angles are both
  integrally independent, then it has only square-number congruent tilings.
- Isosceles triangles always have a `2`-tiling by the symmetry altitude.
- Beeson-Laczkovich-Zhang solve #633. Consequence stated on the page: the
  triangles admitting a non-square tiling are the isosceles triangles together
  with countably many similarity classes.

BLZ Theorem 1 states that a triangle `T` admits a non-square tiling iff, up to
ordering of angles `(A,B,C)`, one of the following holds:

1. `A = B` (isosceles, including equilateral).
2. `C = pi/2` and the legs have integer ratio `M/K`, with `M^2+K^2` not a
   square.
3. `(A,B,C) = (pi/6, pi/2, pi/3)`.
4. `C = pi/3` and `sqrt(3) tan(A/2)` is rational.
5. `B = 2A` and `sqrt(3) tan(A/2)` is rational.
6. `B = 2A` and `sin(A/2)` is rational.
7. `C = A/2+B`, `2 sin(A/4) = M/K`, and `2K^2-M^2` is not a square.
8. `C = 2A+B/2` and `sqrt(3) tan(A/2)` is rational.

This solves the "which outer triangles have a non-square tiling?" problem, not
the #634 "which numbers occur?" problem.

Workspace interpretation for #634:

- Row 1 is the isosceles/equilateral branch and must still be split by the
  stronger Beeson isosceles and equilateral reductions.
- Rows 2 and 3 explain the right-triangle reptile mechanisms that give
  `m^2+k^2` and `3m^2`, but do not by themselves rule out other tile shapes for
  those same outer triangles.
- Rows 4, 5, and 8 are the non-isosceles `gamma=2pi/3` branches after choosing
  angle orderings; row 4 contains the two branches with a `pi/3` outer angle.
- Rows 6 and 7 are represented in Beeson's `3alpha+2beta=pi` analysis, with
  row 7 matching the triquadratic branch.

The detailed row-to-filter ledger is maintained in `SOURCE_REDUCTION_AUDIT.md`.

BLZ also gives useful number-of-tiles formulas for non-isosceles
`gamma=2pi/3` cases. For a primitive integer tile `(a,b,c)` with
`c^2=a^2+ab+b^2`:

- Proposition 24: for outer angles `(alpha, alpha+beta, alpha+2beta)`,
  `N=((a+b)/b)m^2`. Therefore prime `N` is impossible in this template: if
  `N=p`, coprimality forces `a+b=p` and `b` square; then
  `c^2=a^2+ab+b^2` has no solution with `0<c<a+b`.
- Proposition 31: for outer angles `(2alpha,2beta,alpha+beta)`,
  `N=(a+2b)(b+2a)m^2`, so prime `N` is impossible.
- Proposition 26: for outer angles `(alpha,2alpha,3beta)`, writing
  `t=tan(alpha/2)/sqrt(3)`, `N` is
  `((2/3)(3t^2-1)/((3t+1)(t-1)))` times a rational square. This proves the
  count is not a square, but it does not by itself rule out primes.
- Proposition 28: for outer angles `(alpha,2beta,2alpha+beta)`, `N` is
  `((3t^2-6t-1)/((t-1)(3t+1)))` times a rational square. Again this is a
  non-square result, not a general prime obstruction.

For `N=19`, the two square-class formulas above have exact arithmetic
witnesses, so BLZ's non-square result alone cannot rule out the benchmark
prime. These witnesses are necessary arithmetic data only, not tilings; the
workspace proof rules them out using boundary integrality of the outer side
ratios.

## Soifer

Soifer is the source cited by the Erdős Problems pages for the original problem
statements and early constructive families.

Recorded claims from the problem pages and Beeson:

- All squares occur for any triangle.
- `2m^2`, `3m^2`, `6m^2`, and `m^2+k^2` occur for at least one triangle.
- For similar, not congruent, dissections: every triangle can be cut into `N`
  similar triangles when `N != 2,3,5`, and there are triangles that cannot be cut
  into `2`, `3`, or `5` similar triangles.
- Soifer's #633 result: integrally independent sides and angles force only
  square congruent tilings.

## Snover-Waiveris-Williams

Snover, Waiveris, and Williams, "Rep-tiling for triangles", Discrete Math. 91
(1991), 193-200.

Beeson states their theorem as follows. Suppose the tiled triangle `ABC` is
`N`-tiled by a tile `T` similar to `ABC`. If `N` is not a square, then `T` and
`ABC` are right triangles. Then exactly one of these alternatives holds:

- `N = 3m^2`, and the triangle is a `30-60-90` triangle.
- `N = e^2+f^2`, the right angle of `ABC` is split by the tiling, and the acute
  angles have rational tangents `e/f` and `f/e`.

This theorem is a complete classification of the reptile/similar-tile subcase.
It immediately rules out prime `p = 3 mod 4` in the reptile subcase, except the
special prime `3`.

## Laczkovich

Laczkovich's work provides the finite angle-shape reductions used by Beeson and
BLZ.

Commensurable-angle case:

- If the tile angles are rational multiples of `pi`, Laczkovich's 1995 table
  gives finite possibilities for `(ABC, tile)`.
- His 2012 congruent-tile refinements eliminate several equilateral rows that
  are possible for similar tiles but impossible for congruent tiles.

Incommensurable-angle case:

- If not all tile angles are rational multiples of `pi`, Laczkovich again reduces
  to finitely many shape templates.
- Beeson slides list templates including reptile cases, equilateral cases with
  a tile angle `pi/3` or `2pi/3`, isosceles cases, the `3alpha+2beta=pi`
  cases, and `gamma=2pi/3` cases.

Laczkovich's reductions do not by themselves classify the possible `N`; they
reduce #634 to finitely many analytic/combinatorial families.

## Beeson

### Slides

The slides emphasize three targets:

- Given `N`, find a tile and outer triangle, or prove none exist.
- Given an outer triangle, determine possible tiles and `N`.
- Describe all `N` for which some triangle has an `N`-tiling.

Key statements from the slides:

- `N = 7` and `N = 11` are impossible for any outer triangle and tile.
- `N = 19` is explicitly unknown in the slides.
- Beeson says one might hope every prime `4r+3` is impossible, but he does not
  even label it a conjecture.
- If an equilateral triangle has an `N`-tiling and `N > 3`, then `N` is not
  prime.
- For `3alpha+2beta=pi`, the coloring equation and area equation give finite
  computations. For small `N`, Beeson reports no `7` or `11`; for `19` the
  computation finds algebraic candidates that are not known to correspond to
  tilings.

### NoSevenTiling

Beeson, "No triangle can be cut into seven congruent triangles", proves no
`7`-tiling and no `11`-tiling.

Proof structure:

1. Use Snover-Waiveris-Williams for the reptile/similar case.
2. Use Laczkovich's finite reductions for commensurable and incommensurable
   angle cases.
3. For commensurable angles, possible `N` forms include squares, sums of two
   squares, `3m^2`, `2m^2`, `6m^2`; these exclude `7` and `11`.
4. For some incommensurable isosceles/right cases, Beeson proves `N` is even or
   otherwise non-prime.
5. For `3alpha+2beta=pi`, Beeson combines coloring equations, area equations,
   boundary `c`-edge lemmas, and Sage computations to prove `N >= 12` for the
   small cases needed, ruling out `7` and `11`.
6. For `gamma=2pi/3`, geometric area lower bounds show `N >= 12` in the
   relevant non-similar cases.
7. Remaining equilateral cases are handled by rationality and finite Sage
   checks.

The paper notes that longer unpublished machinery would imply more prime
non-existence statements, including all primes `3 mod 4`, but the short paper
only establishes `7` and `11`.

### TriangleTilingEquilateral

Beeson's "Tiling an equilateral triangle" records Laczkovich's equilateral
classification. A tile for an equilateral outer triangle is, up to angle order,
one of:

```text
(pi/3,pi/3,pi/3),
(pi/6,pi/6,2pi/3),
(pi/6,pi/2,pi/3),
(alpha,beta,pi/3) with alpha/pi irrational,
(alpha,beta,2pi/3) with alpha/pi irrational.
```

The first three count forms are known: `m^2`, `3m^2`, and `6m^2`. For the last
two incommensurable cases, Beeson quotes Laczkovich's 2012 theorem that the
tile is rational. This is the source bridge for the workspace's exact
equilateral integer-side model

```text
c^2=a^2-ab+b^2        or        c^2=a^2+ab+b^2,
L^2=Nab,
L=xa+yb+zc.
```

Beeson proves that in either incommensurable equilateral case `N` is not prime
for `N > 3`, but the paper does not classify composite values.

### IsoscelesTilings

Beeson's "Tilings of an isosceles triangle" treats non-equilateral isosceles
outer triangles in several cases. For the subcase where the outer triangle has
base angles `alpha` and the tile has angles `(alpha,beta,2pi/3)`, Beeson proves
the tile is rational and derives the arithmetic filter

```text
c^2 = a^2+ab+b^2,
2b+a | N,
N b/(2b+a) is a square.
```

Theorem 12.10 states that this subcase has no candidates for `N < 33`. For
`N <= 200`, the candidates begin with `33:(5,3,7)`, `37:(5,16,19)`,
`46:(7,8,13)`, `65:(3,5,7)`, and `71:(39,16,49)`. Beeson further rules out the
`37` candidate by a geometric argument, but leaves `71` as the next prime case
to consider.

The same paper records other isosceles subcase obstructions useful for small
values. Theorem 7.8 gives a complete count classification for isosceles tilings
by a right triangle: `N` is a square, twice a square, `6k^2`, or an even sum of
two squares. Theorem 11.7 proves that in the `gamma=2alpha` isosceles template,
`N` is not squarefree; in particular no prime count occurs there.

For composite counts in the same `gamma=2alpha` branch, Lemma 11.14 gives a
finite boundary-enumeration algorithm: for a fixed `N`, enumerate coprime
parameters `(k,m)`, form integer sides `(a,b,c)=(k^2,m^2-k^2,mk)`, reject
wrong squarefree parts and nonintegral area-derived boundary lengths `X,Y`,
then enumerate boundary decompositions of `X` and `Y`. Theorem 11.18 uses this
enumeration plus Lemma 11.17 to prove `N >= 45`, and then notes that after
`45` the next possibilities left open are `63,64,72`. This is a strong source
lead for `N=60`; the workspace now has a local Lemma 11.14 certificate showing
no boundary-arithmetic candidate for `N=56`.

### TriangleTiling4

Beeson's Triangle Tiling IV supplies the local "suspicious edge" machinery used
in several `gamma=2pi/3` reductions. Lemma 12 is stated for a vertex `B` at
which exactly one tile occurs and that tile has angle `beta`; under the
non-similarity and non-isosceles hypotheses it forces an actual tiling edge
relation

```text
jb = ua + vc,        j > 0, u >= 0, v >= 0.
```

Two points matter for later reuse. First, the lemma is not an apex-only
statement: `B` is the chosen unsplit vertex, and the proof draws it "north" only
for description. Second, Beeson explicitly says the sweep argument in Direction
`C` does not use the opposite side `AC`; the only boundary-specific endgame is
where the lowest sweep line hits `W=C` or the reflected line hits `S=A`. Lemma
13 then reuses the same technique inside a subtriangle with a new angle
bisector, which is textual evidence that the method is local once the same
hypotheses are restored.

This does not by itself justify every later application at an arbitrary base
corner. A base-corner reuse still needs separate proof that the corner is
unsplit, that the unique corner tile has the required `beta` angle, that after
possibly relabeling the incident sides the corner tile is Type I, and that the
residual triangle satisfies the same non-similar, `alpha != beta`,
`gamma=2pi/3` hypotheses. Those setup lemmas are external to Beeson IV.

### TriangleTiling3

Beeson's "Triangle tiling: the case `3alpha+2beta=pi`" studies all five possible
outer-triangle shapes in that template. The paper derives necessary tiling
equations for each shape and sufficient conditions for three of them. Its
conclusion states that in the non-similar `3alpha+2beta=pi` template, prime
tile counts do not occur; the proof cites Theorems 8, 12, 18, 15, and 20 for the
five shapes. The theorem line in the extracted PDF reads `3alpha+beta=pi`, but
the paper title, section conclusion, table, and preceding sentence all identify the
case as `3alpha+2beta=pi`.

The source also records sufficient conditions used in the workspace enumerator:

- triquadratic `(2alpha,beta,alpha+beta)`: `N=2K^2-M^2` occurs when
  `s=a/c=M/K` and `K | M^2`;
- `(2alpha,alpha,2beta)`: the rational-root candidate is sufficient when the
  primitive sides satisfy `c | a^2`;
- Table 7 gives explicit examples `28,44,48,77,84`.

## Zhang

Zhang, "Tiling Triangles With 2pi/3 Angles", arXiv:2512.22696.

Setup:

- Tile side lengths `(a,b,c)` are integers.
- The angle opposite `c` is `gamma = 2pi/3`.
- Therefore `c^2 = a^2+b^2+ab`.

Main equilateral construction:

Let

```text
M = 3 ceil((c^2-a-b)/(ab)).
```

For every integer `m >= M`, an equilateral triangle with side `mab` can be tiled
by `m^2 ab` copies of `(a,b,c)`.

Construction idea:

- Build tileable "ideal trapezoids" with parallel sides in prescribed multiples
  of `ab`.
- Glue three such ideal trapezoids cyclically to form an equilateral triangle.
- Area gives the tile count `m^2 ab`.

Zhang also gives:

- A `pi/3` analogue with `c^2 = a^2+b^2-ab`.
- A family for the `(2alpha,2beta,alpha+beta)` outer triangle. If the auxiliary
  semigroup parameter is `q in b*N0+c*N0` (and in particular for every
  `q > bc-b-c`), the count is `(a+2b)(b+2a)q^2`.
- Further constructions for four other `gamma=2pi/3` incommensurable-angle
  templates by attaching equilateral or `(2alpha,2beta,alpha+beta)` auxiliary
  tilings. With `m >= M`, the equilateral-auxiliary cases give counts
  `b(a+2b)m^2`, `a(b+2a)m^2`, `b(a+b)m^2`, `a(a+b)m^2`,
  `(b+2a)(a+b)m^2`, and `(a+2b)(a+b)m^2`. With
  `q in b*N0+c*N0`, the final two cases give
  `3(a+2b)(a+b)q^2` and `3(b+2a)(a+b)q^2`.

Zhang's conjectures:

- In the equilateral `2pi/3` setting, all sufficiently large possible `N` should
  be exactly `m^2 ab` with `m >= M`.
- Divisibility of equilateral side lengths by `ab` is conjectured in general.
- Analogous exactness conjectures are made for the `pi/3` and related families.

These are new infinite positive families, not a complete solution of #634.

## Turturean Prime-Count Draft

David Turturean's April 2026 draft, "Triangle Dissections into a Prime Number of
Congruent Triangles", claims the complete prime-count dichotomy:

```text
prime p occurs iff p = 2, p = 3, or p == 1 (mod 4).
```

The draft's `N=19` proof imports published reductions from Snover-Waiveris-
Williams, Laczkovich, and Beeson's Triangle Tiling I-IV series to reduce to the
remaining non-isosceles `120` degree tile with primitive integer sides
`c^2=a^2+ab+b^2`. It then proves supporting-line integrality for outer sides,
derives five possible `120` degree outer-triangle side families, and eliminates
four of them for prime `N` by denominator/copimality arguments. The final
family forces an isosceles outer triangle with `a+2b=p` or `2a+b=p`.

For `p=19`, that last family is eliminated because it would require `3` to be a
quadratic residue modulo `19`, which it is not. For all primes `p == 7 (mod
12)`, the same quadratic-residue obstruction applies. For primes `p == 11 (mod
12)`, the draft parametrizes the surviving integer side triples and uses a
witness-level form of Beeson's Triangle Tiling IV suspicious-edge lemma plus a
width bound in the isosceles triangle to force an internal segment longer than
can fit. The critical interpretive point is that the draft applies Beeson's
Lemma 12 technique at base corners of the residual isosceles triangle. The
source audit above supports the locality of the sweep argument, but the draft
still has to supply the corner setup hypotheses before the application can be
imported as a theorem.

Workspace status: this draft should be treated as an external, unrefereed
prime-only solution until independently checked. It does not attempt the
all-integer classification requested by Problem #634.
