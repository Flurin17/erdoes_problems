# Evolving Classification for Erdős Problem #634

## Target Theorem

Determine exactly which positive integers `n` occur as the number of congruent triangular tiles in a dissection of some triangle.

## Current Candidate Classification

No complete classification is currently established in this workspace or in the
source corpus read so far. The page for Problem #634 and Beeson slides explicitly
identify `n = 19` as unknown. The workspace now has a derived obstruction for
`n=19` and, more generally, classifies prime tile counts, but the requested
all-`n` theorem is still not available.

Validated source-level facts:

- Many infinite positive families are known.
- `7` and `11` are impossible.
- If the tile is similar to the outer triangle, the possible `N` are exactly
  `m^2`, `m^2+k^2`, and `3m^2`.
- Every equilateral outer triangle tiling with `N > 3` has composite `N`.
- The hoped-for obstruction for all primes `4r+3` is not proved by the source
  corpus. This workspace now derives it from the source reductions plus the
  boundary-integrality and boundary-transition lemmas below.

## Positive Constructions

### Subdivision Lemma

Let `PQR` be any triangle and let `m >= 1`. In barycentric coordinates define

```text
v(i,j,k) = (iP + jQ + kR)/m,        i+j+k=m.
```

The small triangles

```text
conv(v(i+1,j,k), v(i,j+1,k), v(i,j,k+1))        for i+j+k=m-1
conv(v(i+1,j+1,k), v(i+1,j,k+1), v(i,j+1,k+1))  for i+j+k=m-2
```

partition `PQR` into `m^2` congruent triangles similar to `PQR`, with reflected
orientation allowed. This lemma upgrades any primitive `N`-tiling to an
`Nm^2`-tiling.

### Squares: `n = m^2`

For any triangle `ABC`, divide each side into `m` equal segments and draw all parallels to the sides through division points. This partitions `ABC` into `m^2` triangles similar to `ABC`, hence congruent after accounting for orientation.

Coordinate certificate for tile triangle with vertices `(0,0)`, `(1,0)`, `(0,1)`: large triangle `(0,0)`, `(m,0)`, `(0,m)` tiled by the standard unit right-triangle grid.

### `n = 2m^2`

Take the large isosceles right triangle

```text
A = (-m,0),  B = (m,0),  C = (0,m).
```

The altitude from `C` to `D=(0,0)` splits it into the two congruent right
triangles `ACD` and `BCD`, each with legs `m,m`. Apply the subdivision lemma
inside each half to get `2m^2` congruent right-isosceles tiles.

### `n = 3m^2`

Let

```text
A = (m,0),
B = (-m/2,  sqrt(3)m/2),
C = (-m/2, -sqrt(3)m/2),
O = (0,0).
```

The equilateral triangle `ABC` is split into `OAB`, `OBC`, and `OCA`. Each has
side lengths `m,m,sqrt(3)m`, so the three triangles are congruent. Subdivide each
one into `m^2` similar copies. This gives `3m^2` congruent tiles.

### `n = 6m^2`

Take an equilateral triangle of side `m`. Join its center to its three vertices and
three side midpoints. This partitions it into six congruent `30-60-90` triangles
with side-length ratio `1:sqrt(3):2`. Subdivide each of the six triangles into
`m^2` similar copies. This gives `6m^2` congruent tiles.

### Sums of Two Squares: `n = a^2 + b^2`

Let `a,b` be positive integers and let the tile be the right triangle with legs
`a,b`.

Set `N = a^2+b^2` and define the outer triangle

```text
A = (0,0),  B = (a^2,ab),  C = (-b^2,ab),  D = (0,ab).
```

Then

```text
|AB|^2 = a^2N,    |AC|^2 = b^2N,    |BC|^2 = N^2,
AB dot AC = 0.
```

Thus `ABC` is a right triangle similar to the tile, with scale `sqrt(N)`. The
altitude segment `AD` splits `ABC` into two right triangles:

- `ADB` has legs `a^2` and `ab`, hence is `a` times the tile.
- `ADC` has legs `ab` and `b^2`, hence is `b` times a reflected/swapped copy of
  the tile.

Subdivide `ADB` into `a^2` copies and `ADC` into `b^2` copies by the subdivision
lemma. Total tile count is `a^2+b^2`.

### Zhang Equilateral `2pi/3` Family

Source theorem, not yet fully reconstructed with all coordinates:

Let `(a,b,c)` be pairwise-coprime positive integers satisfying

```text
c^2 = a^2 + ab + b^2.
```

This is the side relation for a triangle whose angle opposite `c` is `2pi/3`.
Define

```text
M = 3 ceil((c^2-a-b)/(ab)).
```

For every integer `m >= M`, an equilateral triangle of side `mab` can be tiled by
`m^2 ab` congruent copies of the triangle `(a,b,c)`.

Construction mechanism from Zhang:

1. Tile ideal trapezoids with angles `pi/3, pi/3` on the legs by copies of
   `(a,b,c)`.
2. Use a Frobenius-coin argument to make all sufficiently long multiples of `ab`
   available as trapezoid side data.
3. Glue three tileable ideal trapezoids cyclically to form an equilateral triangle.
4. Compare areas: equilateral area divided by tile area is `m^2ab`.

Example: `(a,b,c) = (3,5,7)` gives `ab=15` and

```text
M = 3 ceil((49-3-5)/15) = 9.
```

Therefore `15m^2` occurs for every `m >= 9`; the first value from this family is
`1215`.

### Other Zhang Families

Zhang gives additional constructive families for the `gamma=2pi/3` and `pi/3`
incommensurable-angle templates:

- The `pi/3` analogue has `c^2=a^2+b^2-ab` and gives equilateral counts
  `m^2ab` for every `m >= 3 ceil((a^2+b^2-a-b)/(ab))`.
- For `(2alpha,2beta,alpha+beta)` outer triangles, counts of the form
  `(a+2b)(b+2a)q^2` occur whenever `q` lies in the semigroup
  `b*N0+c*N0`; in particular, every `q > bc-b-c` works.
- The equilateral auxiliary construction gives the six additional quadratic
  count forms
  `b(a+2b)m^2`, `a(b+2a)m^2`, `b(a+b)m^2`, `a(a+b)m^2`,
  `(b+2a)(a+b)m^2`, and `(a+2b)(a+b)m^2`, all for `m` beyond Zhang's
  equilateral threshold.
- The `(2alpha,2beta,alpha+beta)` auxiliary construction gives
  `3(a+2b)(a+b)q^2` and `3(b+2a)(a+b)q^2` for
  `q in b*N0+c*N0`.

These enlarge the positive set but are not a complete classification.
In particular, the proved Zhang families do not construct `N=19`: a prime count
would require the square parameter to be `1` and the coefficient to be `19`;
the coefficient equations for `19` have no compatible primitive
`c^2=a^2+ab+b^2` or `c^2=a^2+b^2-ab` tile in these families. This is only a
non-construction statement, not an impossibility theorem for arbitrary tilings.

### Beeson `3alpha+2beta=pi` Table Constructions

Beeson's `3alpha+2beta=pi` paper lists the following explicit tilings with
`N <= 100`, all using tile `(a,b,c)=(2,3,4)` in the normalization
`a/c=s`, `b/c=1-s^2`:

| N | M | outer-triangle case |
|---:|---:|---|
| 28 | 2 | triquadratic `(2alpha,beta,alpha+beta)` |
| 44 | 6 | isosceles-beta |
| 48 | 4 | isosceles-`alpha+beta` |
| 77 | 5 | `(alpha,2alpha,2beta)` |
| 84 | 10 | isosceles-alpha |

These add isolated positive values not captured by the elementary families above.

The same source records two sufficient subfamilies that can be enumerated
directly:

- In the triquadratic case `(2alpha,beta,alpha+beta)`, if
  `0 < M < K` and `K | M^2`, then

  ```text
  N = 2K^2 - M^2
  ```

  occurs with `s=a/c=M/K`.
- In the `(2alpha,alpha,2beta)` case, a rational-root candidate is sufficient
  when the primitive reconstructed sides satisfy `c | a^2`.

The experiment `EXPERIMENTS/beeson_3alpha2beta_sufficient.py` enumerates these
recorded sufficient conditions. Below `250` this adds the triquadratic
constructions `112`, `126`, and `153`; `153` is also a sum of two squares, while
`112` and `126` are new to the small-value ledger.

## Negative Results

### Global Source Case Split

The proof ledger uses the following published reductions as theorem-level
inputs.

First, Snover-Waiveris-Williams classify the similar/reptile case; the count
forms are recorded in the next subsection.

Second, Beeson's NoSevenTiling records Laczkovich's commensurable-angle list
and adds the possible congruent-tile counts. If all tile angles are rational
multiples of `pi`, every tiling has one of the following count forms:

```text
m^2,        a^2+b^2,        2m^2,        3m^2,        6m^2.
```

Third, when not all tile angles are rational multiples of `pi`, Beeson's Table
4 gives the finite complementary list:

```text
similar to the outer triangle,
equilateral with alpha = pi/3,
isosceles/right-tile gamma = pi/2,
isosceles gamma = 2alpha,
(2alpha,beta,alpha+beta) with 3alpha+2beta = pi,
(2alpha,alpha,2beta) with 3alpha+2beta = pi,
isosceles with 3alpha+2beta = pi,
isosceles gamma = 2pi/3,
(alpha,2alpha,3beta) with gamma = 2pi/3,
(alpha,2beta,2alpha+beta) with gamma = 2pi/3,
(alpha,alpha+beta,alpha+2beta) with gamma = 2pi/3,
(2alpha,2beta,alpha+beta) with gamma = 2pi/3,
equilateral with gamma = 2pi/3.
```

This is now the global table against which the rest of the obstructions are
organized. The remaining gaps are not in the existence of a finite source case
split; they are in the exact count restrictions for several composite
incommensurable rows.

### Similar/Reptile Case

By Snover-Waiveris-Williams, if the tile is similar to the outer triangle, then
the only possible values are:

```text
m^2,        m^2+k^2,        3m^2.
```

More precisely, if `N` is not a square then both triangles are right; either
`N=3m^2` with a `30-60-90` triangle, or `N=e^2+f^2` with the acute right-triangle
tangents `e/f` and `f/e`.

This rules out prime `p = 3 mod 4` in the similar-tile case, except for `p=3`.

### `n = 7`

Beeson proves there is no `7`-tiling of any triangle by any tile.

The proof is not a single elementary obstruction; it is a case analysis using:

- Snover-Waiveris-Williams for reptilings;
- Laczkovich's finite reductions for commensurable and incommensurable angle
  templates;
- angle, area, and coloring equations;
- boundary `c`-edge lemmas;
- finite Sage computations in the small exceptional templates.

Exact obstruction category: finite Laczkovich case reduction plus algebraic
area/coloring constraints and finite computation.

### `n = 11`

Beeson proves there is no `11`-tiling of any triangle by any tile, by the same
framework as for `7`.

Exact obstruction category: finite Laczkovich case reduction plus algebraic
area/coloring constraints and finite computation.

### Equilateral Outer Triangle

Beeson proves that if an equilateral triangle has an `N`-tiling and `N > 3`, then
`N` is not prime. This is stronger than the `7`/`11` obstruction for equilateral
outer triangles only.

The following normalization is the local proof behind the exact equilateral
filters. Laczkovich's equilateral classification, as quoted in Beeson's
equilateral paper, leaves only five tile shapes: equilateral, `(pi/6,pi/6,2pi/3)`,
`(pi/6,pi/2,pi/3)`, or an incommensurable tile with a distinguished angle
`pi/3` or `2pi/3`. The first three have count forms `m^2`, `3m^2`, and `6m^2`.
In the last two cases Laczkovich's 2012 theorem gives rational tile side ratios.

Therefore, in either incommensurable equilateral case, scale the tile so its sides
adjacent to the distinguished angle are coprime positive integers `a,b`, and let
`c` be the opposite side. The law of cosines gives

```text
c^2 = a^2-ab+b^2        when gamma=pi/3,
c^2 = a^2+ab+b^2        when gamma=2pi/3.
```

Let `L` be the equilateral outer side. The tile area is
`ab sin(gamma)/2 = ab sqrt(3)/4`, and the outer area is `L^2 sqrt(3)/4`, so

```text
L^2 = Nab.
```

Finally, each outer side is covered by full sides of boundary tiles. Therefore
for some nonnegative integers `x,y,z`, not all zero, and with at most `N`
boundary tile sides on a fixed outer side,

```text
L = xa + yb + zc,        0 < x+y+z <= N.
```

Thus every candidate in the incommensurable equilateral `pi/3` and `2pi/3`
cases lies in the finite integer-side model used below.

For composite diagnostics, an equilateral outer triangle with a tile angle
`gamma=2pi/3` and primitive integer sides `(a,b,c)` must satisfy

```text
c^2 = a^2+ab+b^2,        L^2 = Nab,
```

where `L` is the equilateral outer side. Each outer side must also be an integer
sum of tile side lengths. The experiment
`EXPERIMENTS/equilateral_area_candidates.py` records a side-bounded version of
this necessary area/boundary-length filter.

For a proof-level finite filter, note that one outer side uses at most `N` full
tile sides. Thus for some nonnegative integers `x,y,z` with
`0 < x+y+z <= N`,

```text
L = xa + yb + zc.
```

After substituting `r=a/b` and eliminating `L` and `c`, this gives a polynomial
equation in the rational number `r`. If `z=0`, the equation is the quadratic

```text
(xr+y)^2 = Nr.
```

If `z>0`, write

```text
A = xr+y,        C = r^2 +/- r + 1,
B = Nr - A^2 - z^2 C,
```

with the plus sign for `gamma=2pi/3` and the minus sign for `gamma=pi/3`.
Then every candidate satisfies the quartic equation

```text
B^2 = 4z^2 A^2 C.
```

The experiment `EXPERIMENTS/equilateral_boundary_exact.py` iterates all
`x+y+z <= N`, solves these rational equations exactly, and checks the original
integer side, area, and boundary equations.

For the first composite targets, the exact boundary-length candidates are:

```text
N=14: tile (7,8,13), L=28;
N=15: tile (3,5,7), L=15.
```

Both are eliminated by the same local side-label transition method used for the
isosceles `gamma=2pi/3` prime obstruction. Since the side lengths are rational,
the tile angles have rational cosines; for these two candidates Niven's theorem
gives `alpha/pi` and `beta/pi` irrational. Thus the only straight boundary
types are

```text
alpha + beta + gamma = pi,        3alpha + 3beta = pi.
```

At an equilateral corner the angle is `pi/3=alpha+beta`. The two incident
boundary tiles must therefore contribute one `alpha` and one `beta` angle, and
their interior sides emanating from the corner must have the same side label.
Writing an oriented boundary side as `side:start->end`, the only corner
transitions are

```text
b:gamma->alpha  followed by  a:beta->gamma,
a:gamma->beta   followed by  b:alpha->gamma.
```

Using the straight transition table already displayed in the isosceles
`gamma=2pi/3` section, the possible full boundary-side words are:

```text
N=14, L=28, sides=(7,8,13):
  (a:beta->gamma)^4,
  (a:gamma->beta)^4.

N=15, L=15, sides=(3,5,7):
  (a:beta->gamma)^5,
  (a:gamma->beta)^5,
  (b:alpha->gamma)^3,
  (b:gamma->alpha)^3.
```

No ordered triple of these side words satisfies the three equilateral corner
transition constraints. Therefore these two exact equilateral `gamma=2pi/3`
candidates cannot be tilings. Together with the Laczkovich/Beeson rationality
bridge for equilateral outer-triangle tilings, this eliminates the equilateral
source branch for `N=14` and `N=15`.

The analogous exact `gamma=pi/3` equilateral candidates for the next composite
cases are

```text
N=21: tile (16,21,19), L=84;
N=30: tile (8,15,13), L=60,
```

together with their `a,b` swaps. Here

```text
c^2 = a^2-ab+b^2,        L^2 = Nab.
```

For these rational tiles, Niven's theorem again makes `alpha/pi` and `beta/pi`
irrational. Since `gamma=pi/3`, the only straight boundary types are

```text
alpha + beta + gamma = pi,        3gamma = pi.
```

At an equilateral corner the outer angle is exactly one `gamma` tile angle, so
the two incident boundary side labels must be `a` and `b`. The generic straight
transition table is

```text
a:beta->gamma   may be followed by a:beta->gamma or b:gamma->alpha
a:gamma->beta   may be followed only by a:gamma->beta
b:alpha->gamma  may be followed by a:gamma->beta or b:alpha->gamma
b:gamma->alpha  may be followed only by b:gamma->alpha
c:alpha->beta   may be followed only by c:alpha->beta
c:beta->alpha   may be followed only by c:beta->alpha
```

For the displayed orientation of both side triples, the only full boundary-side
words are

```text
(b:alpha->gamma)^4,        (b:gamma->alpha)^4.
```

The `a,b` swaps give the corresponding two `a`-only words. In either
normalization no ordered triple of side words has the required `a/b` label pair
at each equilateral corner. Thus the exact `N=21` and `N=30` equilateral
`gamma=pi/3` candidates are also eliminated by a boundary-star obstruction.
The exact scan gives no equilateral boundary-length candidates for `N=22`.

### `3alpha+2beta=pi` Necessary Equation Filter

Beeson's `3alpha+2beta=pi` paper proves that in this non-similar template,
`N` is not prime. This rules out `N=19` for all five shape templates in this
case. The proof is by five separate shape arguments, referenced in the paper's
conclusion as Theorems 8, 12, 18, 15, and 20.

As a sanity check and candidate generator, the experiment
`EXPERIMENTS/beeson_3alpha2beta_filter.py` solves Beeson's final necessary
equations in `N`, coloring number `M`, and `s=a/c` over rational `s`.

For `N=19`, the first-pass equation filter finds four rational necessary
candidates, all in the isosceles-`alpha+beta` case:

| M | s=a/c | primitive tile sides |
|---:|---:|---|
| 1 | `9/10` | `(90,19,100)` |
| 2 | `15/23` | `(345,304,529)` |
| 3 | `5/14` | `(70,171,196)` |
| 4 | `3/35` | `(105,1216,1225)` |

The stronger filter printed in Beeson Section 11.4 eliminates all four. In any
case, the prime-nonexistence theorem already rules out this template completely
for `N=19`.

For the isosceles-`alpha+beta` branch, Section 11.4 is used only as a necessary
filter. The source first derives the equation

```text
s = (N-M^2)/(N+M^2)
```

and then checks the following necessary conditions: primitive integral tile
sides, `c=g^2` with `g=gcd(a,c)`, integrality of `g*mu` for
`mu=M(1+s)`, the square condition `Nbc`, Lemma 46's extra `mu`-integrality
condition when `b` is squarefree and coprime to `c-a`, and boundary side
decompositions after the two forced `c` edges are removed. This is exactly the
filter implemented in `EXPERIMENTS/beeson_isosceles_alpha_plus_beta_filter.py`.
Failing the filter is a source-backed obstruction; passing it is not a tiling
certificate.

For small composite diagnostics, the same necessary-equation filter leaves raw
`N=14` and `N=15` candidates. The `N=15` candidates, and three of the four
`N=14` candidates, are in the isosceles-`alpha+beta` case and fail Beeson's
stronger Section 11.4 filter. The remaining `N=14` candidate is triquadratic:

```text
N=14, M=2, tile sides (a,b,c)=(6,5,9),
outer angles (2alpha,beta,alpha+beta),
outer side lengths (28,15,27).
```

The experiment `EXPERIMENTS/beeson_3alpha2beta_boundary.py` rules out this
candidate by a boundary-star check. It enumerates all decompositions of the
outer side lengths into full tile sides and all orientations passing the
straight-boundary vertex star constraints. There are `2`, `6`, and `2` oriented
side paths for the three sides after those local straight checks, but no full
cycle compatible with the three corner angle stars `2alpha`, `beta`, and
`alpha+beta`. Thus `N=14` and `N=15` have no surviving candidates in the
currently encoded `3alpha+2beta=pi` filters.

The same boundary-star script also rules out the remaining encoded
`N=21` candidate in this template:

```text
N=21, M=5, tile sides (a,b,c)=(2,3,4),
outer angles (alpha,alpha,alpha+2beta),
outer side lengths (12,12,21).
```

The side paths passing straight-boundary stars number `10` for the base length
`21` and `6` for each equal side length `12`, but none close around the three
corner angle stars.

### Isosceles `gamma=2pi/3` Filter

Beeson's isosceles-triangle paper treats the case where the outer triangle is
isosceles with base angles `alpha` and the tile has angles
`(alpha,beta,2pi/3)`. In that setting the tile is rational; after scaling to
primitive integer sides `(a,b,c)`, the following necessary conditions hold:

```text
c^2 = a^2 + ab + b^2,
2b+a divides N,
N b/(2b+a) is a square m^2,
outer equal side X = mc,
outer base Y = m(2b+a).
```

The experiment `EXPERIMENTS/gamma_2pi3_isosceles_filter.py` reproduces this
finite arithmetic filter. It gives no candidates for `N=19`, so this isosceles
`gamma=2pi/3` subcase is ruled out for the benchmark prime. It also reproduces
the first candidates from Beeson's table: `N=33` with tile `(5,3,7)`, `N=37`
with tile `(5,16,19)`, `N=46` with tile `(7,8,13)`, and so on.

### Other Isosceles Outer-Triangle Subcases

Beeson’s isosceles-triangle paper reduces non-equilateral isosceles outer
triangles, aside from the reptile case, to right-tile, `gamma=2alpha`,
`gamma=2pi/3`, and `3alpha+2beta=pi` templates.

The right-tile branch is complete for counts. Beeson's Theorem 7.8 gives the
possibilities

```text
N is a square,
N is twice a square,
N = 6k^2,
N is an even sum of two squares.
```

Equivalently for the small-value obstructions used here, the right-tile
isosceles branch is contained in `square`, `sum of two squares`, and `6k^2`.
Thus `N=22` is excluded in this branch because `22` is not a square, not a sum
of two squares, and not `6k^2`.

For the `gamma=2alpha` branch, Beeson proves rationality and then Theorem 11.7:
`N` is not squarefree. This excludes `N=22` and every prime count in this
branch.

For prime `N=19`:

- right-tile isosceles counts are squares, even sums of squares, or `6m^2`,
  so `19` is excluded;
- `gamma=2alpha` counts are not squarefree, so every prime is excluded;
- `gamma=2pi/3` is excluded by the arithmetic filter above;
- `3alpha+2beta=pi` is excluded by Beeson's prime theorem for that template.

Thus all isosceles outer-triangle cases are source-ruled for `N=19`.

### Non-Isosceles `gamma=2pi/3` BLZ Filters

BLZ gives number-of-tiles formulas for the four non-isosceles
`gamma=2pi/3` templates. Let the primitive integer tile satisfy

```text
c^2 = a^2 + ab + b^2.
```

For outer angles `(alpha,alpha+beta,alpha+2beta)`, BLZ Proposition 24 gives

```text
N = ((a+b)/b) m^2.
```

This rules out prime `N=p` in this template. Since `gcd(a+b,b)=1`, the equation
`p=((a+b)/b)m^2` forces `a+b=p` and `b` to be a square. Then
`c^2=a^2+ab+b^2` gives `c^2 == b^2 (mod p)`, while the triangle inequality gives
`0<c<p`; hence `c=b` or `c=a`, both impossible with positive `a,b`.

For outer angles `(2alpha,2beta,alpha+beta)`, BLZ Proposition 31 gives

```text
N = (a+2b)(b+2a)m^2.
```

Both factors are integers greater than `1`, so this template also has no prime
tile count.

The corresponding primitive sine-law outer side ratio is

```text
(a(a+2b), b(b+2a), c^2).
```

For primitive `c^2=a^2+ab+b^2`, this triple has gcd `1`. A common prime divisor
would divide `c`; since `c` is coprime to `a` and `b`, it must divide both
`a+2b` and `b+2a`, hence either divides `3` or contradicts primitivity. The
lemma below rules out `3 | c`. Thus the integral BLZ coefficient is already the
area coefficient forced by boundary integrality. In particular, `N=143` has the
two arithmetic candidates `(a,b,c)=(3,5,7)` and `(5,3,7)` with primitive outer
side triples `(39,55,49)` and `(55,39,49)`; they require a separate
boundary-star obstruction, not a length-integrality obstruction.

For the two remaining templates BLZ gives exact square-class constraints, not
prime impossibility:

```text
(alpha,2alpha,3beta):       N = ((a+2b)/(3(a+b))) * q^2,
(alpha,2beta,2alpha+beta):  N = ((b+2a)/(a+b)) * q^2,
```

for a rational square factor `q^2`. The experiment
`EXPERIMENTS/blz_gamma_2pi3_nonisosceles_filter.py` checks these square classes.
For `N=19`, the square-class obstruction alone fails: there are exact arithmetic
witnesses satisfying the BLZ area square-class conditions.

For `(alpha,2beta,2alpha+beta)`:

```text
(a,b,c) = (1131561, 358039, 1346761),
A = b+2a = 2621161 = 1619^2,
S = a+b = 1489600 = 19*280^2,
19 = (A/S) * (5320/1619)^2.
```

For `(alpha,2alpha,3beta)`:

```text
(a,b,c) =
(64291453825267166692191813022145,
 3194650169777924718531451006912,
 65946838654721589964381492334497),
A = a+2b = 70680754164823016129254715035969,
S = a+b = 67486103995045091410723264029057,
19 = (A/(3S)) * (62021834282110443/8407184675313313)^2.
```

These are not tiling certificates. They require a fractional scaling of the
outer triangle relative to the primitive integer side ratios, which is impossible
for a genuine tiling.

We use the following elementary lemma repeatedly. If `gcd(a,b)=1` and
`c^2=a^2+ab+b^2`, then

```text
gcd(c,a) = gcd(c,b) = gcd(c,a+b) = 1, and 3 does not divide c.
```

The first three coprimality statements follow by reducing the side equation
modulo a prime divisor of the indicated pair. For the last statement, if
`3 | c`, then `a^2+ab+b^2 == 0 (mod 3)`, so primitivity gives
`a == b != 0 (mod 3)`. Writing `b=a+3k` gives
`c^2 == 3a^2 (mod 9)`, impossible because the square residues modulo `9` are
`0,1,4,7`.

We also use the following boundary lemma, which is safe for non-strict tilings.
Each outer side of the tiled triangle is a disjoint union of full sides of the
tiles adjacent to that outer side, so in primitive tile units every outer side
length is an integer sum of tile side lengths. A tile vertex may lie in the
relative interior of one of those boundary tile sides, but that does not split
the boundary side of the tile itself or create a second tile side overlapping it
on the same side of the polygon.

For `(alpha,2beta,2alpha+beta)`, the sine-law outer side ratio is

```text
(ac, b(b+2a), c(a+b)).
```

For primitive `c^2=a^2+ab+b^2`, this triple has gcd `1`: if a prime divides
`c` and `b+2a`, then substituting `b=-2a` into the side equation gives
`3a^2 == 0`; for `p != 3` this contradicts `gcd(a,b)=1`, and for `p=3` it
contradicts the lemma. If a common prime does not divide `c`, it would divide
both `a` and `a+b`, again contradicting `gcd(a,b)=1`. Thus the outer side scale
is an integer `m`, and the area ratio is

```text
N = (b+2a)(a+b)m^2.
```

For prime counts this is already impossible, since both integer factors
`b+2a` and `a+b` are greater than `1`. For coefficient tracking, write
`S=a+b`. Since
`(b+2a)(a+b)=S(S+a) >= S(S+1)`, any value below `88` would have `S <= 8`.
A finite check of positive coprime pairs with `S <= 8` gives only
`(a,b,c)=(3,5,7)` and `(5,3,7)`, and the smaller coefficient is
`(5+2*3)*8 = 88`. Therefore this template has no `N=19` tiling, and in fact no
prime-count tiling at all.

For `(alpha,2alpha,3beta)`, the sine-law outer side ratio is

```text
(c^2, c(a+2b), 3b(a+b)).
```

Again the gcd is `1`: any common prime must divide `c` and `3b(a+b)`, while
`c` is coprime to `b` and `a+b`, and the lemma prevents `3 | c`. Hence the
outer side scale is an integer `m`, and the area ratio is

```text
N = 3(a+2b)(a+b)m^2.
```

This is also impossible for prime counts. Here
`3(a+2b)(a+b)=3S(S+b) >= 3S(S+1)`. A value below `264` again forces
`S <= 8`, and the same finite check gives the minimum at `(a,b,c)=(5,3,7)`:
`3*(5+2*3)*8 = 264`. This rules out `N=19` in the final non-isosceles
`gamma=2pi/3` template, and in fact rules out every prime count in this
template.

Combining these two boundary-integrality product formulas with the two BLZ
prime-impossible templates rules out all non-isosceles `gamma=2pi/3` cases for
prime `N`.

For composite diagnostics, the experiment
`EXPERIMENTS/gamma_2pi3_nonisosceles_exact.py` enumerates the exact arithmetic
filters for all four non-isosceles `gamma=2pi/3` templates. It uses

```text
N = ((a+b)/b)m^2,
N = (a+2b)(b+2a)m^2,
N = (b+2a)(a+b)m^2,
N = 3(a+2b)(a+b)m^2,
```

respectively. This proves, for example, that `N=14`, `15`, and `22` do not even
survive the non-isosceles `gamma=2pi/3` arithmetic filters, while `21` and `30`
survive in the first BLZ template. The follow-up experiment
`EXPERIMENTS/gamma_2pi3_nonisosceles_boundary.py` applies the local endpoint
boundary-star check to these and later low-scale survivors:

The endpoint check is deliberately corner-aware: at a straight boundary vertex
it requires the ordinary side-label star, while at an outer corner it also
allows the two incident boundary sides to be the two sides of a single tile
when the whole outer corner is exactly one tile angle. This avoids the
overcounting error that would count one tile corner twice.

```text
N=21: tile (5,16,19), scale 4, opposite outer sides (20,76,84);
N=30: tile (7,8,13), scale 4, opposite outer sides (28,52,60);
N=55: tile (39,16,49), scale 4, opposite outer sides (156,196,220);
N=88: tile (3,5,7), scale 1, opposite outer sides (21,55,56);
N=105: tiles (8,7,13) and (16,5,19), opposite outer sides
       (56,91,105) and (80,95,105);
N=120: tile (7,8,13), scale 8, opposite outer sides (56,104,120);
N=143: tiles (3,5,7) and (5,3,7), opposite outer sides
       (39,55,49) and (55,39,49).
```

All these candidates have zero feasible full boundary endpoint cycles, so none
can be a tiling. The same generic endpoint-pair check removes the later BLZ
survivors `154`, `168`, `210`, and `220` in the `100..250` diagnostic scan.

The remaining prime-specific issue is Beeson's isosceles
`gamma=2pi/3` filter. Running the exact divisibility and square test from
Section 12 for primes `p == 3 (mod 4)` below `100` gives no candidates for

```text
p = 7, 11, 19, 23, 31, 43, 47, 59, 67, 79, 83,
```

and one candidate for `p=71`:

```text
(a,b,c) = (39,16,49), m=4, outer sides (196,196,284).
```

The `71` candidate is ruled out by the boundary-orientation argument below.
Consequently the current reductions rule out all `p == 3 (mod 4)` primes below
`100`, except for the positive prime `3`.
For prime `p` in this isosceles filter, the divisor condition simplifies:
`2b+a | p` forces `2b+a=p`, and then `p b/(2b+a)=b` must be a square. Thus the
remaining prime candidates are exactly the primitive integer solutions

```text
p = a + 2t^2,
c^2 = a^2 + a t^2 + t^4.
```

Using the standard primitive parametrization of `c^2=a^2+ab+b^2` and the fact
that `b=t^2`, these candidates can be written as

```text
t = 2rs,
a = 3s^4 - 2r^2s^2 - r^4,
b = 4r^2s^2,
c = 3s^4 + r^4,
p = 3s^4 + 6r^2s^2 - r^4,
```

where `gcd(r,s)=1`, `0<r<s`, and `r,s` have opposite parity. Equivalently,
if `u=s^2+r^2` and `v=s^2-r^2`, then the useful side-length relation

```text
u a = v(b+c)
```

holds for every remaining isosceles prime candidate.

The exact scan `EXPERIMENTS/gamma_2pi3_isosceles_filter.py --prime-scan 20000`
finds the following `p == 3 (mod 4)` candidates up to `20000`:

```text
71, 443, 863, 2459, 4019, 8363, 8663, 12671.
```

The diagnostic script `EXPERIMENTS/isosceles_prime_family.py` shows that the
equal sides have the unique decomposition into `t` copies of the tile side `c`
for these arithmetic candidates. Its boundary-parity check rules out strict
edge-to-edge tilings for `71,443,863,2459,8363,12671`; the candidates `4019`
and `8663` survive that strict-parity check.

In fact this entire isosceles `gamma=2pi/3` subcase is impossible by a local
boundary-transition lemma. Because the tile has rational side lengths, each
angle has rational cosine. Since `0 < alpha,beta < pi/3`, Niven's theorem shows
that `alpha/pi` and `beta/pi` are irrational; hence the only straight boundary
angle types are

```text
alpha + beta + gamma = pi,        3alpha + 3beta = pi.
```

At a straight boundary transition, the visible boundary endpoint angles must fit
one of these two angle types, and the inward side labels must be connectable by
the remaining tile angles. Writing an oriented boundary side as
`side:start->end`, the complete local transition table is:

```text
a:beta->gamma   may be followed only by a:beta->gamma
a:gamma->beta   may be followed by a:gamma->beta or b:alpha->gamma
b:alpha->gamma  may be followed only by b:alpha->gamma
b:gamma->alpha  may be followed by a:beta->gamma or b:gamma->alpha
c:alpha->beta   may be followed only by c:alpha->beta
c:beta->alpha   may be followed only by c:beta->alpha
```

The base of the outer isosceles triangle has angle `alpha` at both ends. At the
left base corner the first full boundary side on the base is therefore either
`b:alpha->gamma` or `c:alpha->beta`; the adjacent side of an `alpha` tile is
one of `b,c`. The transition table makes each of these two states absorbing
along the base. Thus the final base side would end at `gamma` or `beta`, not at
the required `alpha` endpoint of the right base corner. This contradiction uses
only full tile sides on the outer boundary and the local side-label star at
straight boundary vertices, so shifted T-junctions in interiors of boundary
sides do not affect it.

The script `EXPERIMENTS/isosceles_prime_boundary_words.py --limit 100000`
checks the table against all arithmetic prime candidates in that range and
finds no survivors. The argument above is the proof; the scan is a sanity check.

For the `71` candidate, the boundary arithmetic is even more rigid. The equal
sides have length `196=4c`, and the only decomposition by tile side lengths is
four `c`-edges. Each base corner has angle `alpha`. Since
`cos(alpha)=71/98`, Niven's theorem excludes `alpha/pi` rational; in particular
`alpha` is not an integer multiple of `beta`. Thus a base corner consists of one
tile angle `alpha`, not a fan of several smaller tile angles. The two sides
adjacent to a tile's `alpha` angle are `b` and `c`; because the equal side is
forced to use `c`, the base must start and end with a `b`-edge at its `alpha`
endpoint.

The base length `284` has only two decompositions:

```text
284 = a + 5c = 8b + 4a.
```

The first has no `b`-edge and is incompatible with the base corners. Hence the
base is a sequence of eight `b`-edges and four `a`-edges, with `b` at both
corners. Both `a` and `b` have exactly one `gamma` endpoint:

```text
a = (beta,gamma),       b = (alpha,gamma).
```

Traverse the base from left to right. The first `b`-edge starts at its `alpha`
endpoint, so it ends at `gamma`. At a straight boundary transition, the next
edge cannot also present its `gamma` endpoint, because two `gamma` tile angles
already sum to `4pi/3 > pi`; any additional incident tile angles would only
increase the sum. Therefore the next `a`- or `b`-edge must start at its
non-`gamma` endpoint, and so it also ends at `gamma`. Induction forces every
edge in the base sequence to end at `gamma`, including the final edge, but the
right base corner requires a `b`-edge at its `alpha` endpoint. This
contradiction uses only the full tile sides lying on the outer boundary, so it
is unaffected by shifted T-junctions in the relative interiors of those boundary
sides. Thus `N=71` is impossible.

The side-to-side boundary count gives a weaker check: the boundary would have
`4+4+12=20` tile edges, and `3*71-20` is odd, so no strict edge-to-edge tiling
exists. The older angle-parity bookkeeping also says that, in a simple
T-junction model, the number of interior T-junctions would have to be odd, but
the boundary-orientation contradiction is already decisive.

There is also a length-only side-matching constraint that is independent of
edge-to-edge assumptions. After removing the forced boundary sides, the interior
side incidences are

```text
a: 67, b: 63, c: 63.
```

The script `EXPERIMENTS/isosceles_71_matching.py` partitions these incidences
into two-sided equal-length interior components, ignoring geometry and angle
order. The reason for the threshold is simple: there are `63` interior `c`-side
incidences, and every two-sided component of length at most `194` has an even
number of `c` incidences. For side lengths `(a,b,c)=(39,16,49)`, all integer
relations among lengths are generated by

```text
2a + 2c = 11b,        5a = 3b + 3c.
```

The first generator has even `c`-parity; the second is the smallest relation
with odd `c`-parity. Thus the first odd-`c` equality is

```text
5a = 3b + 3c = 195.
```

Therefore any hypothetical non-strict `71` tiling, before applying the boundary
orientation contradiction, would have to contain an interior collinear matched
segment of length at least `195`. This diagnostic is no longer needed to rule
out `71`, but it remains useful for testing length-matching invariants.

The minimal odd-`c` component is locally compatible with angle sums. The
component has one side consisting of five `a`-edges and the other consisting of
three `b`-edges and three `c`-edges. The `5a` side has breakpoints
`39,78,117,156`; every ordering of the three `b` and three `c` edges has five
breakpoints disjoint from those four. Hence the component creates nine
T-junction breakpoints. The script `EXPERIMENTS/isosceles_71_interface_angles.py`
checks that the endpoint angles along both sides can be completed at every
breakpoint to one of the straight angle types

```text
alpha + beta + gamma = pi,        3alpha + 3beta = pi.
```

Thus the length-`195` component is not eliminated by local straight-angle
conditions. This explains why the boundary-orientation obstruction is needed:
purely local interior interface checks do not by themselves eliminate the
candidate.

A separate coloring obstruction is available for the lattice-vertex subcase of
the `71` candidate. It is weaker than the boundary-orientation contradiction,
but it is a useful sanity check. In axial coordinates for the triangular
lattice, the outer triangle is

```text
(0,0), (284,0), (64,156),
```

and one tile orientation is

```text
(0,0), (39,0), (-16,16).
```

Color unit lattice triangles by orientation. The outer triangle contains
`22198` upward and `22106` downward unit triangles, so its up-minus-down
difference is `92`. Every lattice-oriented copy of the tile has difference
`+8` or `-8`. Since `92` is not divisible by `8`, no tiling whose vertices all
lie in this triangular lattice exists. This covers strict edge-to-edge tilings,
but still does not exclude arbitrary non-strict tilings with shifted T-junction
cosets.

## Classified Integers and Families

This table records only values/families classified by the current proof file.

| n or family | status | proof source |
|---|---|---|
| `m^2` | positive | subdivision lemma |
| `2m^2` | positive | isosceles altitude + subdivision |
| `3m^2` | positive | equilateral center split + subdivision |
| `6m^2` | positive | equilateral center/midpoint split + subdivision |
| `a^2+b^2` | positive | right-triangle coordinate construction |
| `28,44,48,77,84` | positive | Beeson `3alpha+2beta=pi` table |
| `112,126,153` | positive | Beeson `3alpha+2beta=pi` sufficient subfamilies |
| sufficiently large `m^2ab` for `c^2=a^2+ab+b^2` | positive | Zhang construction |
| `7` | negative | Beeson |
| `11` | negative | Beeson |
| `14` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `15` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `19` | negative in this workspace | Beeson/Laczkovich/SWW source reductions; equilateral and `3alpha+2beta` prime theorems; isosceles reductions; boundary-transition and BLZ `gamma=2pi/3` boundary-integrality arguments |
| `21` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `22` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `30` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `33` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `35` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `38` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `39` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `42` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `46` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `51` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `55` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `56` | negative in this workspace | published source case split plus exact arithmetic and `gamma=2alpha` boundary-enumeration elimination in the composite benchmark below |
| `57` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `60` | negative in this workspace | published source case split plus exact arithmetic and local `gamma=2alpha` c-edge/base endpoint/Lemma 11.17 obstruction |
| `62` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `66` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `69` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `70` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `76` | negative in this workspace | published source case split plus exact arithmetic and local `gamma=2alpha` c-edge/base endpoint/Lemma 11.17 obstruction |
| `78` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `86` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `87` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `88` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| `91` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `92` | negative in this workspace | published source case split plus exact arithmetic and local `gamma=2alpha` c-edge/base endpoint/Lemma 11.17 obstruction |
| `93` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `94` | negative in this workspace | published source case split plus exact arithmetic elimination in the composite benchmark below |
| `95` | negative in this workspace | published source case split plus exact arithmetic and boundary-star elimination in the composite benchmark below |
| primes `p == 3 (mod 4)`, `p > 3` | negative | source reductions + non-isosceles product formulas + isosceles boundary-transition lemma |
| similar-tile subcase | classified | Snover-Waiveris-Williams |
| equilateral outer triangle with prime `N>3` | negative | Beeson |
| non-isosceles `gamma=2pi/3` templates `(alpha,alpha+beta,alpha+2beta)` and `(2alpha,2beta,alpha+beta)` with prime `N` | negative | BLZ formulas |
| non-isosceles `gamma=2pi/3` templates `(alpha,2beta,2alpha+beta)` and `(alpha,2alpha,3beta)` with prime `N` | negative | boundary-integrality product formulas |
| isosceles `gamma=2pi/3` template | negative in the rational nondegenerate case | boundary-transition lemma |

## Source-Reduction Coverage Matrix

This matrix records which reductions are theorem-level in this workspace and
which are only implemented as diagnostics. It is meant to prevent a dashboard
empty set from being mistaken for a proof. The detailed proof-obligation ledger
is maintained in `SOURCE_REDUCTION_AUDIT.md`, including a row-by-row map from
BLZ Problem #633 outer-triangle classes to the #634 case filters below.

| case/template | current status | remaining gap |
|---|---|---|
| similar/reptile | classified by Snover-Waiveris-Williams | none for this subcase |
| commensurable-angle source table | closed by Beeson's NoSevenTiling Table 3 and Theorem 3, with forms `m^2`, `a^2+b^2`, `2m^2`, `3m^2`, `6m^2` | none for this branch |
| right-tile isosceles | source-backed count forms from Beeson Theorem 7.8 | none for small-value obstructions using these forms |
| isosceles `gamma=2alpha` | source-backed non-squarefree obstruction from Beeson Theorem 11.7; Beeson Lemma 11.14/Theorem 11.18 give a finite boundary enumeration and state that after `45` the next left-open values are `63,64,72`; local base endpoint, `c`-parity, and Lemma 11.17 filters are encoded | non-edge-to-edge overhangs at outer-boundary fans remain the gap for `63` and `99` |
| isosceles `gamma=2pi/3` | ruled out in the rational nondegenerate case by boundary-transition lemma | audit interaction with every source-reduced equilateral/degenerate exception |
| `3alpha+2beta=pi` | necessary rational equations encoded; several sufficient cases encoded; selected boundary-star eliminations and a generic boundary-integrality filter for supported outer shapes | isosceles-`alpha+beta` composite survivors remain after Beeson's stronger source filter; not a complete composite classification |
| non-isosceles `gamma=2pi/3` | exact arithmetic formulas encoded; prime obstruction proved; endpoint boundary-star eliminations for `21`, `30`, `55`, `88`, `105`, `120`, `143`, and the later `100..250` BLZ survivors | no explicit encoded survivor remains below `250`; a general composite obstruction is not yet proved |
| equilateral outer triangle with tile angle `pi/3` or `2pi/3` | source bridge from Laczkovich/Beeson gives the rational side model; exact boundary-length arithmetic filter, `gamma=2pi/3` and `gamma=pi/3` boundary-star checks, and lattice exact-cover checks added | exact `14`, `15`, `21`, and `30` equilateral candidates eliminated; composite cases still require exact scans and boundary checks |
| Zhang positive families | sufficient constructions recorded | conjectural converses are not used as obstructions |

The BLZ #633 theorem is used here only as a cover of possible outer-triangle
similarity classes for non-square tilings. It does not by itself determine
which `N` occur for a given row. In particular, an outer triangle in the
right-triangle or `pi/3` rows may have the obvious similar-tile construction
while still requiring a separate source reduction to rule out other congruent
tile shapes and other counts.

## Composite Benchmark: `N=14` and `N=15`

The same published source case split used for `N=22` also classifies `14` and
`15`. The elementary and commensurable-count forms do not contain either value:

```text
14 and 15 are not squares,
14 and 15 are not sums of two positive squares,
14 and 15 are not 2m^2, 3m^2, or 6m^2.
```

Thus the similar/reptile and commensurable-angle table branches are removed.
The right-tile isosceles branch is also removed by Beeson's Theorem 7.8: neither
count is a square, `6m^2`, or twice a sum of two squares. The
`gamma=2alpha` isosceles branch is removed by Beeson's squarefree obstruction.

The exact equilateral boundary-length equations leave only the following
`gamma=2pi/3` candidates, together with the displayed `a,b` swaps:

| N | primitive tile | equilateral side L | boundary decompositions found by exact scan |
|---:|---|---:|---|
| 14 | `(7,8,13)` and `(8,7,13)` | 28 | `a+b+c`, `4a` or swapped `4b` |
| 15 | `(3,5,7)` and `(5,3,7)` | 15 | `3b`, `a+b+c`, `5a` or swapped |

For `gamma=2pi/3`, an equilateral corner must be one tile `gamma` angle. The
straight-boundary side-label transitions are the ones recorded in the
equilateral section above. The script
`EXPERIMENTS/equilateral_gamma_boundary.py` enumerates every oriented boundary
side word passing those straight-vertex stars and then tests the three
equilateral corner stars. It finds two oriented side paths and zero full cycles
for `N=14`, and four oriented side paths and zero full cycles for `N=15`.
Therefore neither equilateral candidate can be a tiling.

The `gamma=2pi/3` isosceles arithmetic filter gives no candidates for `14` or
`15`. The exact non-isosceles `gamma=2pi/3` formulas likewise give no candidates
in any of the four BLZ templates.

It remains to check the `3alpha+2beta=pi` template. Beeson's five final
necessary equations leave four raw roots for `N=14`:

| M | source row | s=a/c | primitive tile sides |
|---:|---|---:|---|
| 2 | triquadratic `(2a,b,a+b)` | `2/3` | `(6,5,9)` |
| 1 | isosceles `(a+b,a+b,a)` | `13/15` | `(195,56,225)` |
| 2 | isosceles `(a+b,a+b,a)` | `5/9` | `(45,56,81)` |
| 3 | isosceles `(a+b,a+b,a)` | `5/23` | `(115,504,529)` |

The three isosceles-`alpha+beta` roots fail Beeson's stronger Section 11.4
filter. The remaining triquadratic root has outer side lengths `(28,15,27)`;
`EXPERIMENTS/beeson_3alpha2beta_boundary.py` enumerates the full boundary side
words and finds `6`, `2`, and `2` oriented side paths on the three sides, but
zero full cycles compatible with the corner stars `(2alpha,beta,alpha+beta)`.

For `N=15`, Beeson's necessary equations leave only three
isosceles-`alpha+beta` roots:

| M | s=a/c | primitive tile sides |
|---:|---:|---|
| 1 | `7/8` | `(56,15,64)` |
| 2 | `11/19` | `(209,240,361)` |
| 3 | `1/4` | `(4,15,16)` |

All three fail Beeson's stronger Section 11.4 filter. Therefore `N=14` and
`N=15` have no survivor in any source case, and both are classified negative in
this workspace.

## Composite Benchmark: `N=21` and `N=30`

The values `21` and `30` are removed by the same source-row method. Neither is
a square, a sum of two positive squares, `2m^2`, `3m^2`, or `6m^2`; hence the
similar/reptile, commensurable-angle, and right-tile isosceles branches are
removed. Both counts are squarefree, so Beeson's `gamma=2alpha` isosceles
branch is removed as well.

The exact equilateral boundary-length equations leave only `gamma=pi/3`
candidates:

| N | primitive tile | equilateral side L | exact boundary decompositions |
|---:|---|---:|---|
| 21 | `(16,21,19)` and `(21,16,19)` | 84 | `4b` or swapped `4a` |
| 30 | `(8,15,13)` and `(15,8,13)` | 60 | `4b`, `a+4c`, `4a+b+c` or swapped |

For `gamma=pi/3`, each equilateral corner is one tile `gamma` angle, so its
incident boundary side labels must be `a` and `b`. The script
`EXPERIMENTS/equilateral_pi_boundary.py` enumerates the legal straight-boundary
side words and corner stars. It finds two oriented side paths and zero
compatible full boundary cycles for both `N=21` and `N=30`, and the `a,b` swaps
are symmetric. Thus the equilateral source branch is eliminated.

The `gamma=2pi/3` isosceles arithmetic filter gives no candidates for `21` or
`30`. The exact non-isosceles `gamma=2pi/3` formulas leave one candidate for
each value:

| N | template | primitive tile | scale | outer sides |
|---:|---|---|---:|---|
| 21 | `(alpha,alpha+beta,alpha+2beta)` | `(5,16,19)` | 4 | `(20,76,84)` |
| 30 | `(alpha,alpha+beta,alpha+2beta)` | `(7,8,13)` | 4 | `(28,52,60)` |

`EXPERIMENTS/gamma_2pi3_nonisosceles_boundary.py` applies the endpoint
boundary-star obstruction: the possible endpoint-pair states are `{84: 2,
20: 2, 76: 4}` for `N=21` and `{60: 2, 28: 2, 52: 4}` for `N=30`, with zero
compatible full boundary endpoint cycles in both cases.

It remains to check `3alpha+2beta=pi`. For `N=21`, the five raw roots are:

| M | source row | s=a/c | primitive tile sides |
|---:|---|---:|---|
| 1 | isosceles `(a+b,a+b,a)` | `10/11` | `(110,21,121)` |
| 2 | isosceles `(a+b,a+b,a)` | `17/25` | `(425,336,625)` |
| 3 | isosceles `(a+b,a+b,a)` | `2/5` | `(10,21,25)` |
| 4 | isosceles `(a+b,a+b,a)` | `5/37` | `(185,1344,1369)` |
| 5 | isosceles-alpha `(a,a,a+2b)` | `1/2` | `(2,3,4)` |

The four isosceles-`alpha+beta` roots fail Beeson's stronger Section 11.4
filter. The remaining isosceles-alpha root has outer sides `(12,12,21)`;
`EXPERIMENTS/beeson_3alpha2beta_boundary.py` finds `10` legal oriented paths on
the base, `6` on each equal side, and zero full boundary cycles compatible with
the corner stars `(alpha,alpha,alpha+2beta)`.

For `N=30`, all five raw roots are isosceles-`alpha+beta` and fail Beeson's
stronger Section 11.4 filter:

| M | s=a/c | primitive tile sides |
|---:|---:|---|
| 1 | `29/31` | `(899,120,961)` |
| 2 | `13/17` | `(221,120,289)` |
| 3 | `7/13` | `(91,120,169)` |
| 4 | `7/23` | `(161,480,529)` |
| 5 | `1/11` | `(11,120,121)` |

Therefore `N=21` and `N=30` have no survivor in any source case, and both are
classified negative in this workspace.

## Composite Benchmark: `N=22`

The published Laczkovich/Beeson reduction bridge recorded in
`SOURCE_REDUCTION_AUDIT.md` reduces every non-square `22`-tiling to the source
cases below. Each case is eliminated by an exact arithmetic obstruction, so
`N=22` is a negative workspace theorem.

The elementary and commensurable-count forms do not contain `22`:

```text
22 is not a square,
22 is not a sum of two positive squares,
22 is not 2m^2, 3m^2, or 6m^2.
```

Thus the similar/reptile, right-tile, and commensurable-angle table subcases are
removed by their recorded arithmetic forms. The isosceles `gamma=2alpha`
subcase is also removed by the recorded squarefree obstruction, since `22` is
squarefree.

The exact equilateral boundary-length equations give no candidates for `N=22`.
In the rational `pi/3` or `2pi/3` equilateral models, an outer side must satisfy

```text
L^2 = 22ab,        L = xa + yb + zc,        0 < x+y+z <= 22,
```

with `c^2=a^2-ab+b^2` or `c^2=a^2+ab+b^2`. The exact rational-root enumeration
over all side-edge triples finds none.

The `gamma=2pi/3` isosceles arithmetic filter has no `N=22` candidates:

```text
c^2=a^2+ab+b^2,
2b+a | 22,
22b/(2b+a) is a square.
```

The exact non-isosceles `gamma=2pi/3` formulas likewise give no candidates in
any of the four BLZ templates:

```text
22 = ((a+b)/b)m^2,
22 = (a+2b)(b+2a)m^2,
22 = (b+2a)(a+b)m^2,
22 = 3(a+2b)(a+b)m^2.
```

This step uses the stronger boundary-integrality product forms, not just the
older BLZ square-class necessary conditions. The diagnostic
`blz_gamma_2pi3_nonisosceles_filter.py 22 --limit-side 5000` finds a
square-class witness with tile `(3,5,7)` in the
`(alpha,2beta,2alpha+beta)` template and coefficient `11/8`; it is eliminated
only after upgrading that template to the product form
`N=(b+2a)(a+b)m^2`.

It remains only to check the `3alpha+2beta=pi` template. Beeson's five final
necessary equations leave four raw rational roots for `N=22`, all in the
isosceles-`alpha+beta` branch:

| M | s=a/c | primitive tile sides |
|---:|---:|---|
| 1 | `21/23` | `(483,88,529)` |
| 2 | `9/13` | `(117,88,169)` |
| 3 | `13/31` | `(403,792,961)` |
| 4 | `3/19` | `(57,352,361)` |

Beeson's stronger Section 11.4 filter for this branch rejects all four. In the
notation of that section, no candidate survives the requirements involving
`c=g^2`, `g*mu` integrality, square class `Nbc`, Lemma 46's squarefree-`b`
condition, and the necessary boundary decompositions after reserving the two
forced `c` edges.

Therefore `N=22` has no survivor in any source case. This promotes `22` from
"open/no encoded survivor" to a classified negative value in the table above.

## Composite Benchmark: `N=33` and `N=35`

The same source-row checks also classify `33` and `35`. Neither count is a
square, a sum of two positive squares, `2m^2`, `3m^2`, or `6m^2`, so the
similar/reptile, commensurable-angle, and right-tile isosceles branches are
removed. Both counts are squarefree, so the `gamma=2alpha` isosceles branch is
removed.

The exact equilateral boundary-length equations give no candidates for either
count. The exact non-isosceles `gamma=2pi/3` product formulas also give no
candidates for either count.

In the isosceles `gamma=2pi/3` branch, `N=35` has no arithmetic candidate.
`N=33` has exactly one arithmetic candidate:

```text
c^2=a^2+ab+b^2,        (a,b,c)=(5,3,7),
m=3,        outer equal side X=21,        outer base Y=33.
```

This branch is already ruled out by the boundary-transition lemma for every
rational nondegenerate isosceles `gamma=2pi/3` source-row candidate, so the
`N=33` arithmetic candidate cannot be a tiling.

It remains to check `3alpha+2beta=pi`. For `N=33`, Beeson's necessary equations
leave five isosceles-`alpha+beta` roots:

| M | s=a/c | primitive tile sides |
|---:|---:|---|
| 1 | `16/17` | `(272,33,289)` |
| 2 | `29/37` | `(1073,528,1369)` |
| 3 | `4/7` | `(28,33,49)` |
| 4 | `17/49` | `(833,2112,2401)` |
| 5 | `4/29` | `(116,825,841)` |

For `N=35`, the five roots are also all isosceles-`alpha+beta`:

| M | s=a/c | primitive tile sides |
|---:|---:|---|
| 1 | `17/18` | `(306,35,324)` |
| 2 | `31/39` | `(1209,560,1521)` |
| 3 | `13/22` | `(286,315,484)` |
| 4 | `19/51` | `(969,2240,2601)` |
| 5 | `1/6` | `(6,35,36)` |

All ten fail Beeson's stronger Section 11.4 isosceles-`alpha+beta` filter.
Therefore `N=33` and `N=35` have no survivor in any source case, and both are
classified negative in this workspace.

## Composite Benchmark: `N=38`, `N=39`, and `N=42`

The next three below-`100` no-survivor values are `38`, `39`, and `42`. None is
a square, a sum of two positive squares, `2m^2`, `3m^2`, or `6m^2`, so the
similar/reptile, commensurable-angle, and right-tile isosceles branches are
removed. Each is squarefree, which removes the `gamma=2alpha` isosceles branch.

The exact non-isosceles `gamma=2pi/3` formulas and the isosceles
`gamma=2pi/3` arithmetic filter give no candidates for all three values.

The exact equilateral boundary-length equations give no candidates for `38` or
`42`. For `39`, they leave four candidates:

| angle | primitive tile | equilateral side L |
|---|---|---:|
| `2pi/3` | `(16,39,49)` and `(39,16,49)` | 156 |
| `pi/3` | `(13,48,43)` and `(48,13,43)` | 156 |

The `2pi/3` boundary-star check for `(16,39,49)` and the `pi/3` boundary-star
check for `(13,48,43)` each find two oriented side paths and zero compatible
full boundary cycles; the `a,b` swaps are symmetric. Thus the equilateral
source branch is eliminated for `39` as well.

In the `3alpha+2beta=pi` template, the raw roots are:

| N | raw roots | surviving roots after Section 11.4/boundary filters |
|---:|---:|---:|
| 38 | 6 isosceles-`alpha+beta` roots | 0 |
| 39 | 6 isosceles-`alpha+beta` roots plus one isosceles-beta root `(12,7,16)` | 0 |
| 42 | 6 isosceles-`alpha+beta` roots | 0 |

For `38` and `42`, all raw roots fail Beeson's stronger Section 11.4
isosceles-`alpha+beta` filter. For `39`, the six isosceles-`alpha+beta` roots
fail the same filter, and the remaining isosceles-beta root is removed by the
boundary-integrality obstruction: the area normalization requires an irrational
side scale and hence cannot make all outer sides integer sums of primitive tile
side lengths.

Therefore `N=38`, `N=39`, and `N=42` have no survivor in any source case, and
all three are classified negative in this workspace.

## Composite Benchmark: `N=46` and `N=51`

The values `46` and `51` are removed by the same source case split. Neither
count is a square, a sum of two positive squares, `2m^2`, `3m^2`, or `6m^2`,
so the similar/reptile, commensurable-angle, and right-tile isosceles branches
are removed. Both are squarefree, so the `gamma=2alpha` isosceles branch is
removed.

The exact equilateral boundary-length equations give no candidates for either
count, and the exact non-isosceles `gamma=2pi/3` product formulas give no
candidates for either count.

In the isosceles `gamma=2pi/3` branch, `N=51` has no arithmetic candidate.
`N=46` has exactly one arithmetic candidate:

```text
c^2=a^2+ab+b^2,        (a,b,c)=(7,8,13),
m=4,        outer equal side X=52,        outer base Y=92.
```

This candidate is ruled out by the same boundary-transition lemma for rational
nondegenerate isosceles `gamma=2pi/3` tilings.

In the `3alpha+2beta=pi` template, `N=46` has six
isosceles-`alpha+beta` roots rejected by Beeson's stronger Section 11.4 filter,
plus one triquadratic root:

```text
M=2,        (a,b,c)=(10,21,25),
outer sides=(92,105,125),        outer angles=(2alpha,beta,alpha+beta).
```

`EXPERIMENTS/beeson_3alpha2beta_boundary.py` finds `6`, `2`, and `2` oriented
side paths on the three sides and zero full boundary cycles compatible with the
corner stars. For `N=51`, all seven raw `3alpha+2beta=pi` roots are
isosceles-`alpha+beta` roots and all seven fail Beeson's stronger Section 11.4
filter.

Therefore `N=46` and `N=51` have no survivor in any source case, and both are
classified negative in this workspace.

## Composite Benchmark: `N=55`

The value `55` is also classified by the source-row checks. It is not a square,
a sum of two positive squares, `2m^2`, `3m^2`, or `6m^2`, so the
similar/reptile, commensurable-angle, and right-tile isosceles branches are
removed. It is squarefree, so Beeson's `gamma=2alpha` isosceles branch is
removed.

The exact equilateral boundary-length equations leave exactly two `gamma=pi/3`
candidates:

```text
N=55: tile (16,55,49), L=220, and its a,b swap.
```

The `pi/3` equilateral boundary-star check for `(16,55,49)` finds two oriented
side paths and zero compatible full boundary cycles; the swap is symmetric.
Thus the equilateral source branch is eliminated.

The isosceles `gamma=2pi/3` arithmetic filter gives no candidates. The exact
non-isosceles `gamma=2pi/3` product formulas leave one candidate:

```text
template=(alpha,alpha+beta,alpha+2beta),
tile (39,16,49), scale 4, outer sides (156,196,220).
```

The endpoint boundary-star check finds endpoint-pair states `{220: 2, 156: 2,
196: 2}` and zero compatible full boundary endpoint cycles.

In the `3alpha+2beta=pi` branch, Beeson's necessary equations leave seven raw
isosceles-`alpha+beta` roots; all seven fail Beeson's stronger Section 11.4
filter. Therefore `N=55` has no survivor in any source case and is classified
negative in this workspace.

## Composite Benchmark: `N=56`

The value `56` is the first non-squarefree no-survivor row after `55`, so it
requires a separate `gamma=2alpha` check. It is not in the square,
sum-of-two-squares, `2m^2`, `3m^2`, or `6m^2` families, so the
commensurable-angle, similar/reptile, and right-tile isosceles branches are
removed.

The exact equilateral boundary-length scan gives six `2pi/3` candidates:

```text
(7,8,13), (8,7,13), (9,56,61), (56,9,61),
(32,175,193), and (175,32,193).
```

Each is eliminated by the equilateral `2pi/3` boundary-star check. The
isosceles and non-isosceles `gamma=2pi/3` filters give no arithmetic
candidates.

In the `3alpha+2beta=pi` branch, Beeson's necessary equations leave eight raw
roots. Seven are isosceles-`alpha+beta` roots and fail Beeson's stronger
Section 11.4 filter; the remaining triquadratic root has tile `(6,5,9)` and is
removed by the triquadratic boundary-star check.

For the remaining `gamma=2alpha` isosceles branch, the local implementation of
Beeson Lemma 11.14 enumerates coprime `(k,m)`, sides
`(a,b,c)=(k^2,m^2-k^2,mk)`, squarefree-part matches, integral area-derived
boundary lengths `X,Y`, and the allowed `X=pa+qb+rc` representations. It
returns no boundary-arithmetic candidate for `N=56`:

```text
N=56: 0 gamma=2alpha boundary candidate(s), 0 after boundary-count obstruction
```

Therefore `N=56` has no survivor in any source case and is classified negative
in this workspace.

### Local `gamma=2alpha` Base Endpoint Lemma And Fan Gap

In the isosceles `gamma=2alpha` branch, the tile angles satisfy

```text
gamma = 2alpha,        3alpha + beta = pi.
```

At a straight boundary point the visible endpoint angles of the two adjacent
boundary tile sides must be extendable to either `alpha+beta+gamma` or
`3alpha+beta`. In particular, two `beta` endpoints cannot meet, and two
`gamma` endpoints cannot meet. At each base corner of the outer isosceles
triangle the angle is exactly `alpha`, so the boundary edge on the base must be
a `b`-edge or a `c`-edge using its `alpha` endpoint.

Therefore the base representation

```text
Y = ua + vb + wc
```

must have both `v > 0` and `w > 0`. If `w=0`, the base uses only `a`- and
`b`-edges. The first base edge at the left corner must be a `b`-edge oriented
from its `alpha` endpoint to its `gamma` endpoint. Since a following `a`- or
`b`-edge cannot start with `gamma` without creating a forbidden `gamma+gamma`
straight boundary point, every subsequent edge must also end at `gamma`. The
last base edge then cannot present the required `alpha` endpoint at the right
base corner. The case `v=0` is identical with `c` in place of `b` and uses the
forbidden `beta+beta` straight boundary point.

For `v>0` and `w>0`, the base necessarily has a transition between a `c` edge
and an `a`- or `b`-edge. At a transition point in the relative interior of a
straight outer side, no tile side can pass through the point along the outer
line: a non-tangent side would leave the tiled triangle, and a tangent
pass-through would overlap the adjacent boundary intervals. Thus the visible
angles at the point form a half-plane angle fan.

The stricter side-label fan table used by
`gamma_2alpha_endpoint_automaton.py --mode fan` is only diagnostic at present.
In a non-edge-to-edge tiling, an interior ray from that boundary point may be
covered by unequal tile sides on its two sides, with the overhang resolved
farther inside. The following side-label transitions would be valid if such
overhangs were ruled out at the boundary fan:

```text
a:beta->gamma   -> a:beta->gamma
a:gamma->beta   -> a:gamma->beta or b:alpha->gamma
b:alpha->gamma  -> b:alpha->gamma
b:gamma->alpha  -> a:beta->gamma or b:gamma->alpha
c:alpha->beta   -> c:alpha->beta
c:beta->alpha   -> c:beta->alpha
```

This table would forbid a `c` edge from transitioning to an `a`- or `b`-edge,
but it is not yet a proof-level obstruction. Primitive equal-length overhangs
such as `a+c=kb` occur in the relevant arithmetic rows, so the missing lemma is
to prove that such overhangs cannot emanate from an outer-boundary transition
in the `gamma=2alpha` branch. The diagnostic
`gamma_2alpha_overhang_fan.py` currently shows the opposite local picture:
using `ca | bbb` for `N=63` and `ca | bbbbb` for `N=99`, the primitive
overhang components can support the `c`/non-`c` boundary fan transitions
locally. For example, a boundary transition `b:gamma->alpha` to
`c:beta->alpha` supplies the visible `alpha+beta`; the overhang ray
`ca | b^k` and one remaining `gamma` sector complete
`alpha+beta+gamma=pi`. Any obstruction must therefore use more global
constraints.

Two further safe refinements are used only when their hypotheses are checked.
Beeson's older boundary `c`-edge lemma says that if `gamma > pi/2`,
`alpha/pi` is irrational, and all three outer angles are less than `gamma`, then
each outer side contains at least two `c` edges. In the `gamma=2alpha`
isosceles branch this removes any side representation with fewer than two
`c` edges whenever `c^2 > a^2+b^2` and Niven's theorem rules out
`alpha/pi in Q`. Finally, the total number of boundary `c` edges has the same
parity as `N`, since every interior `c` edge is counted by two tiles.

## Composite Benchmark: `N=60`

The value `60` is not in the elementary positive forms, so the
commensurable-angle, similar/reptile, and right-tile isosceles branches are
removed. The exact equilateral scan leaves two `2pi/3` candidates,
`(3,5,7)` and its swap in an equilateral triangle of side `30`; both have zero
compatible full boundary cycles. The isosceles and non-isosceles
`gamma=2pi/3` filters give no candidates.

In the `3alpha+2beta=pi` branch, Beeson's necessary equations leave seven raw
isosceles-`alpha+beta` roots, and all seven fail Beeson's stronger Section 11.4
filter.

The remaining branch is `gamma=2alpha`. The local Lemma 11.14 boundary
enumeration leaves one arithmetic candidate:

```text
tile=(49,15,56), X=210=a+7b+c, Y=240
Y representations: 16b, a+9b+c, 2a+2b+2c.
```

The two `Y` representations with one or two `c` edges are removed by Beeson
Lemma 11.17. The zero-`c` representation `Y=16b` is removed by the base-endpoint
lemma above.

Therefore `N=60` has no survivor in any source case and is classified negative
in this workspace.

## Composite Benchmark: `N=57` and `N=62`

The next squarefree composite rows with no encoded survivor are `57` and `62`.
Neither value is a square, a sum of two positive squares, `2m^2`, `3m^2`, or
`6m^2`, so the commensurable-angle, similar/reptile, and right-tile isosceles
count forms do not apply. Since both are squarefree, Beeson's
`gamma=2alpha` isosceles branch is also removed.

The exact equilateral boundary-length scan returns no candidates:

```text
N=57: 0 exact equilateral boundary-length candidate(s), side-edge cap 57
N=62: 0 exact equilateral boundary-length candidate(s), side-edge cap 62
```

The isosceles `gamma=2pi/3` arithmetic filter gives no candidates for either
value, and the exact non-isosceles `gamma=2pi/3` product formulas also give no
candidates.

In the `3alpha+2beta=pi` branch, Beeson's necessary equations leave seven raw
roots for `N=57`, all in the isosceles-`alpha+beta` case; all seven fail
Beeson's stronger Section 11.4 filter. For `N=62`, the necessary equations
leave eight raw roots. Seven are isosceles-`alpha+beta` roots and fail the same
stronger filter; the remaining triquadratic root has tile sides `(42,13,49)`
and outer-angle case `(2a,b,a+b)`, but the sine-law outer side ratio cannot be
scaled to integral boundary side lengths at area ratio `62`, giving a boundary
integrality obstruction.

Therefore `N=57` and `N=62` have no survivor in any source case and are
classified negative in this workspace.

## Composite Benchmark: `N=66`, `N=69`, and `N=70`

The next promoted squarefree composite rows are `66`, `69`, and `70`. None is a
square, a sum of two positive squares, `2m^2`, `3m^2`, or `6m^2`, so the
commensurable-angle, similar/reptile, and right-tile isosceles branches are
removed. Since all three are squarefree, Beeson's `gamma=2alpha` isosceles
branch is also removed.

The exact equilateral boundary-length scan gives six candidates for `N=66`,
none for `N=69`, and four for `N=70`:

```text
N=66:
  2pi/3: (11,24,31), (24,11,31), (33,800,817), (800,33,817)
  pi/3:  (11,96,91), (96,11,91)
N=69:
  no exact equilateral candidates
N=70:
  2pi/3: (35,288,307), (288,35,307)
  pi/3:  (7,40,37), (40,7,37)
```

Every listed equilateral candidate has zero compatible full boundary cycles in
the corresponding `pi/3` or `2pi/3` boundary-star check.

The isosceles `gamma=2pi/3` and exact non-isosceles `gamma=2pi/3` filters give
no candidates for any of the three values. In the `3alpha+2beta=pi` branch,
the stronger isosceles-`alpha+beta` filter returns no survivors. The remaining
raw roots for `66` and `70` outside that isosceles-`alpha+beta` row fail the
encoded boundary-integrality filters for their outer-angle shapes.

Therefore `N=66`, `N=69`, and `N=70` have no survivor in any source case and
are classified negative in this workspace.

## Composite Benchmark: `N=76` and `N=92`

The next two locally closed non-squarefree rows below `100` are `76` and `92`.
Neither value is in the elementary positive forms, so the commensurable-angle,
similar/reptile, and right-tile isosceles branches are removed. The exact
equilateral boundary-length scan, the isosceles `gamma=2pi/3` filter, and the
exact non-isosceles `gamma=2pi/3` filters give no candidates for either value.
In the `3alpha+2beta=pi` branch, the stronger isosceles-`alpha+beta` filter
removes all raw roots.

The remaining branch is `gamma=2alpha`. Lemma 11.14 leaves one boundary
arithmetic candidate for each value:

```text
N=76: tile=(81,19,90),  X=342=a+9b+c,
      Y=380 with representations 20b, a+11b+c, 2a+2b+2c.

N=92: tile=(121,23,132), X=506=a+11b+c,
      Y=552 with representations 24b, a+13b+c, 2a+2b+2c.
```

In both rows the equal side has exactly one `c` edge. Beeson Lemma 11.17
therefore eliminates the base representations with one or two `c` edges, while
the local `gamma=2alpha` base endpoint lemma eliminates the all-`b`
representations.

Therefore `N=76` and `N=92` have no survivor in any source case and are
classified negative in this workspace.

## Composite Benchmark: `N=63` and `N=99`

The remaining below-`100` rows after the preceding refinements are `63` and
`99`. Neither is in the elementary positive forms, so the commensurable-angle,
similar/reptile, and right-tile isosceles branches are removed. The exact
equilateral boundary-length scan, the isosceles `gamma=2pi/3` filter, and the
exact non-isosceles `gamma=2pi/3` filters give no candidates. In the
`3alpha+2beta=pi` branch, the stronger isosceles-`alpha+beta` filter and
boundary-integrality checks remove all raw roots.

The only remaining branch is `gamma=2alpha`. The two-`c` boundary-edge lemma,
the base-endpoint lemma, boundary `c`-parity, and Beeson Lemma 11.17 reduce the
boundary arithmetic to exactly one pattern for each value:

```text
N=63: tile=(9,7,12),   X=2a+3b+2c on both equal sides, Y=3a+3b+3c.
N=99: tile=(25,11,30), X=2a+5b+2c on both equal sides, Y=3a+3b+3c.
```

The side-label fan automaton has zero witnesses for both patterns, but that is
not a proof-level obstruction until the boundary-overhang gap in the preceding
section is closed. Therefore `N=63` and `N=99` remain open in this workspace,
with exactly the displayed `gamma=2alpha` boundary patterns as the current
benchmark survivors.

Both rows are instances of a broader boundary-survivor family in the Lemma 11.14
parameterization. If `k=t` and `m=t+1`, then

```text
(a,b,c) = (t^2, 2t+1, t(t+1)),      a+c = t b,
N = 9(2t+1),                         X = 3t b,
Y = 3(t+1)b = 3a+3b+3c.
```

For `t=3` and `t=5` this gives `N=63` and `N=99`; the same family also explains
later `gamma=2alpha` survivor rows such as `135`, `171`, `189`, and `207`.
Values such as `117`, `153`, and `225` from the same formula are already
positive by elementary families, so this is a boundary-survivor family rather
than an obstruction or construction by itself.

The boundary transition-demand program currently finds a common boundary shape
for all active `gamma=2alpha` survivors below `250`: four `c`/non-`c`
transitions suffice. In particular the benchmark rows have angle-compatible
boundary side-label words

```text
N=63: L=baabccb,     R=aabbbcc,        B=baaabbccc.
N=99: L=baabbbccb,   R=aabbbbbcc,      B=baaabbccc.
```

Each of the four mixed transitions must be supplied by an interior overhang ray.
This again points away from a purely local boundary obstruction and toward a
global side-matching or graph-embedding obstruction.

The stronger local fan-inventory diagnostic gives no contradiction either.  It
enumerates overhang-aware fans at every straight boundary vertex in the displayed
boundary words and sums the side incidences consumed by their interior rays:

```text
N=63: boundary=(7,9,7), interior=(56,54,56),
      fan-inventory min=(39,35,31), slack=(17,19,25).
N=99: boundary=(7,13,7), interior=(92,86,92),
      fan-inventory min=(48,34,40), slack=(44,52,52).
```

Thus the remaining obstruction, if these rows are impossible, must use more than
the local boundary-fan side-count lower bound.

In the consecutive-parameter family, this failure of parity-only obstructions
has a closed form. The boundary words are

```text
L = baa b^(t-2) ccb,      R = aa b^t cc,      B = baaabbccc,
```

with boundary side counts `(7,2t+3,7)` and interior side incidences
`(18t+2,16t+6,18t+2)`. The four mixed transitions admit a balanced local fan
frontier `(16,8,8)`, leaving the even slack `(18t-14,16t-2,18t-6)`.

A floating boundary-shell placement check gives the first constructive-search
seed. After merging the two duplicate base-corner tiles, the forced boundary
shell has `21` unique tiles for `N=63` and `25` for `N=99`, with no remaining
positive-area overlaps. The residual areas are respectively `42` and `74` tile
areas. This is not an existence certificate, but it shows that the obstruction
cannot be just immediate boundary-shell overlap.

Splitting the shell edges at T-junctions leaves a clean simple residual
boundary cycle for `N=99` in the floating model: `46` residual segments and all
`46` residual vertices of degree `2`. For `N=63`, the same extraction has
degree-1 and degree-4 junctions, so a residual search there must model a
network domain rather than only a simple polygon.

## Composite Benchmark: `N=78`, `N=86`, `N=87`, `N=88`, `N=91`, `N=93`, `N=94`, and `N=95`

The next no-survivor rows below `100` are `78`, `86`, `87`, `88`, `91`, `93`,
`94`, and `95`. None is in the elementary positive forms, so the
commensurable-angle, similar/reptile, and right-tile isosceles branches are
removed. For the seven squarefree values, Beeson's `gamma=2alpha` branch is
removed by the squarefree obstruction; for `N=88`, the local Lemma 11.14
enumeration returns no `gamma=2alpha` boundary-arithmetic candidate.

The exact equilateral boundary-length scan returns no candidates for `78`,
`86`, `87`, `88`, `91`, `93`, and `94`. For `N=95`, it returns exactly two
`2pi/3` candidates:

```text
N=95: (19,80,91), L=380, and its a,b swap.
```

Both `95` candidates have zero compatible full boundary cycles in the
equilateral `2pi/3` boundary-star check.

For all eight values, the isosceles `gamma=2pi/3` filter gives no candidates.
The exact non-isosceles `gamma=2pi/3` filter gives no candidates except at
`N=88`, where the sole `(3,5,7)` candidate has zero feasible full boundary
endpoint cycles. In the `3alpha+2beta=pi` branch,
the stronger isosceles-`alpha+beta` filter returns no survivors; the only raw
root outside that row occurs for `N=94` in the triquadratic case and fails the
encoded boundary-integrality filter.

Therefore `N=78`, `N=86`, `N=87`, `N=88`, `N=91`, `N=93`, `N=94`, and `N=95`
have no survivor in any source case and are classified negative in this
workspace.

## Open/Unresolved Ledger

- `19` is listed as open in the source corpus, but the workspace now records a
  derived obstruction ruling it out.
- The general claim "all primes `4r+3` are impossible" was unproved in the
  source corpus. This workspace now records a derived proof, assuming the
  source case reductions summarized above.
- The prime cases are now classified: `2`, `3`, and primes `1 mod 4` are
  positive, while primes `3 mod 4` greater than `3` are negative.
- The first composite negative values beyond Beeson's `7` and `11`
  obstructions now recorded in this workspace are `14`, `15`, `21`, `22`, and
  `30`, followed by `33`, `35`, `38`, `39`, `42`, `46`, `51`, `55`, `56`,
  `57`, `60`, `62`, `66`, `69`, `70`, `76`, `78`, `86`, `87`, `88`,
  `91`, `92`, `93`, `94`, and `95`.
- An April 2026 external draft by David Turturean independently claims the same
  prime dichotomy. Its proof uses a different final obstruction for primes
  `p == 11 (mod 12)`: after reducing to the remaining `120` degree tile family,
  it parametrizes the isosceles survivor and applies a witness-level form of
  Beeson's Triangle Tiling IV suspicious-edge lemma plus a width bound. This
  draft is useful corroborating context for the prime subproblem, but it is not
  a complete classification of all composite `n`. A first Beeson IV audit
  supports local reuse of Lemma 12's sweep technique at a non-apex corner, but
  the draft still needs its corner-unsplitting, Type I side-label, and width
  contradiction checked before it can replace the current proof ledger.
- The exact equilateral boundary-length scan gives a `2pi/3` candidate for
  `14` with tile `(7,8,13)` and outer side `28`, and the analogous `(3,5,7)`
  candidate for `15` with outer side `15`; the composite benchmark above now
  combines the source reduction, boundary-star obstruction, and other source
  filters to classify both values negative.
- The same exact equilateral boundary-length scan finds `gamma=pi/3` candidates
  for `21` and `30`, and no equilateral candidates for `22`;
  the composite benchmark above now combines the equilateral boundary-star
  obstruction with the other source filters to classify `21` and `30`
  negative.
- The current below-`100` gap scan with primitive equilateral side bound `250`
  has two remaining open composite rows, `63` and `99`. All source rows except
  `gamma=2alpha` are eliminated, and the surviving boundary patterns are:

  ```text
  N=63: X=2a+3b+2c, Y=3a+3b+3c for tile (9,7,12).
  N=99: X=2a+5b+2c, Y=3a+3b+3c for tile (25,11,30).
  ```

  The same scan formerly listed `14`, `15`, `21`, `22`, `30`, `33`,
  `35`, `38`, `39`, `42`, `46`, `51`, `55`, `56`, `57`, `60`, `62`, `66`,
  `69`, `70`, `76`, `78`, `86`, `87`, `88`, `91`, `92`, `93`, `94`, and
  `95`; these are now classified negative, while `63` and `99` are the next
  benchmark open rows.
- For the `gamma=2alpha` branch, Beeson records a finite boundary-enumeration
  algorithm and says that after the `N=45` threshold row the next values left
  open are `63,64,72`. The local base endpoint lemma removes the no-`b` and
  no-`c` base representations, but the side-label fan obstruction still needs a
  no-overhang lemma before it can remove the surviving `63` and `99` patterns.
- In the range `100..250`, the former `3alpha+2beta` isosceles-`alpha+beta`
  survivor records at `132`, `156`, `175`, `189`, `198`, `204`, `224`, `228`,
  and `240` are removed by the branch lemma below. The resonant `240` record
  needs the special overhang-endpoint argument because `c-a=12=3a`. This is
  only a branch refinement; some of these counts still have separate
  `gamma=2alpha` boundary-arithmetic survivors until the no-overhang fan gap is
  closed.
- Zhang's conjectural exactness statements are not proved here.
- For `19`, all source-reduced cases are now ruled out in this workspace:
  similar/reptile, commensurable-angle, equilateral-outer, all isosceles
  outer-triangle, `3alpha+2beta=pi`, and all four non-isosceles
  `gamma=2pi/3` subcases.

## Branch Lemma: `3alpha+2beta` Isosceles-`alpha+beta` Boundary Order

In the isosceles-`alpha+beta` branch, the outer angles are
`(alpha+beta, alpha+beta, alpha)`. With the usual side labels
`a=(beta,gamma)`, `b=(alpha,gamma)`, `c=(alpha,beta)`, and
`gamma=2alpha+beta`, the straight-boundary transition table is:

```text
a:beta->gamma   -> a:beta->gamma
a:gamma->beta   -> a:gamma->beta
b:alpha->gamma  -> b:alpha->gamma
b:gamma->alpha  -> b:gamma->alpha or c:alpha->beta or c:beta->alpha
c:alpha->beta   -> c:alpha->beta or b:alpha->gamma
c:beta->alpha   -> c:beta->alpha or b:alpha->gamma
```

Therefore, in a strict boundary fan, any outer side containing an `a` edge is
made entirely of same-oriented `a` edges. If a non-strict tiling tries to avoid
this conclusion by shifting two different side labels along the same boundary
ray, the remaining collinear segment has length one of `|a-b|`, `|a-c|`, or
`|b-c|`. When none of these differences is a nonnegative integer sum of `a`,
`b`, and `c`, the shifted rescue is impossible and the strict transition
conclusion applies to arbitrary boundary tilings.

For Beeson's Section 11.4 survivor records in this branch, the boundary counts
after the forced corner `c` edges have the following obstruction status:

| N | tile `(a,b,c)` | equal-side triples | base triples | status |
|---:|---|---|---|---|
| `132` | `(28,33,49)` | `(3,7,3)` | `(3,1,3)` | obstructed |
| `156` | `(40,39,64)` | `(3,8,3)` | `(3,2,3)` | obstructed |
| `175` | `(33,112,121)` | `(2,11,2)` | `(2,1,2)` | obstructed |
| `189` | `(10,21,25)` | five triples, all mixing `a` with non-`a` | `(3,1,3)` | obstructed |
| `198` | `(117,88,169)` | `(2,13,2)` | `(2,7,2)` | obstructed |
| `204` | `(70,51,100)` | `(3,10,3)` | `(3,4,3)` | obstructed |
| `224` | `(195,56,225)` | `(2,15,2)` | `(2,11,2)` | obstructed |
| `224` | `(45,56,81)` | `(4,9,4)` | `(4,1,4)` | obstructed |
| `228` | `(88,57,121)` | `(3,11,3)` | `(3,5,3)` | obstructed |
| `240` | `(4,15,16)` | eighteen triples | `(3,0,3)`, `(7,0,2)` | obstructed by resonant overhang-endpoint lemma |

In each obstructed row through `N=228`, every allowed count triple on every
outer side contains
at least one `a` edge and at least one non-`a` edge, while no pairwise side
difference is in the semigroup generated by the three side lengths. This
contradicts the boundary-order lemma.

For `N=240`, the tile is `(a,b,c)=(4,15,16)` and the only representable
difference is `c-a=12=3a`. Even granting every `a/c` straight transition as an
overhang rescue, the two outer `alpha+beta` base corners have endpoint pairs
`(b:gamma->alpha, a:beta->gamma)` and
`(a:gamma->beta, b:alpha->gamma)`. The base triples `(3,0,3)` and `(7,0,2)`
contain no `b` edge, so one base corner forces the adjacent equal side to end
with a `b:gamma->alpha` edge. Under the optimistic transition graph this
endpoint can only be preceded by another `b:gamma->alpha` edge, forcing that
whole equal side to be all `b` edges. None of the eighteen equal-side triples is
all `b`, so the resonant `240` survivor is also impossible in this branch.

Consequently, the requested complete classification of all positive integers `n`
is not presently available.
