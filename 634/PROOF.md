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
filters. Suppose the source reductions have put an equilateral outer-triangle
tiling into one of the rational tile-side cases with a distinguished tile angle
`gamma` equal to `pi/3` or `2pi/3`. Scale the tile so its sides adjacent to
`gamma` are coprime positive integers `a,b`, and let `c` be the opposite side.
The law of cosines gives

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

This proves that, once the source rationality hypothesis is accepted, every
candidate in these equilateral `pi/3` and `2pi/3` cases lies in the finite
integer-side model used below.

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
candidates cannot be tilings. This is not yet a complete equilateral
obstruction for `N=14` or `N=15`, because the source-level proof that every
relevant equilateral case has a rational/integer side model of this kind has
not been fully reconstructed.

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

Beeson's isosceles-triangle paper reduces non-equilateral isosceles outer
triangles, aside from the reptile case, to right-tile, `gamma=2alpha`,
`gamma=2pi/3`, and `3alpha+2beta=pi` templates.

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
| `19` | negative | source reductions + boundary integrality in remaining BLZ `gamma=2pi/3` cases |
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
| commensurable-angle source table | recorded as arithmetic forms `m^2`, `a^2+b^2`, `2m^2`, `3m^2`, `6m^2` | exact independent reconstruction of the full Laczkovich table is not in this workspace |
| right-tile isosceles | recorded arithmetic restrictions | source dependence remains |
| isosceles `gamma=2alpha` | squarefree obstruction recorded | complete composite formula not reconstructed |
| isosceles `gamma=2pi/3` | ruled out in the rational nondegenerate case by boundary-transition lemma | audit interaction with every source-reduced equilateral/degenerate exception |
| `3alpha+2beta=pi` | necessary rational equations encoded; several sufficient cases encoded; selected boundary-star eliminations and a generic boundary-integrality filter for supported outer shapes | isosceles-`alpha+beta` composite survivors remain after Beeson's stronger source filter; not a complete composite classification |
| non-isosceles `gamma=2pi/3` | exact arithmetic formulas encoded; prime obstruction proved; endpoint boundary-star eliminations for `21`, `30`, `55`, `88`, `105`, `120`, `143`, and the later `100..250` BLZ survivors | no explicit encoded survivor remains below `250`; a general composite obstruction is not yet proved |
| equilateral outer triangle with tile angle `pi/3` or `2pi/3` | exact boundary-length arithmetic filter, `gamma=2pi/3` and `gamma=pi/3` boundary-star checks, and lattice exact-cover checks added | exact `14`, `15`, `21`, and `30` equilateral candidates eliminated; source-level reduction to this rational/integer model still needs auditing |
| Zhang positive families | sufficient constructions recorded | conjectural converses are not used as obstructions |

The BLZ #633 theorem is used here only as a cover of possible outer-triangle
similarity classes for non-square tilings. It does not by itself determine
which `N` occur for a given row. In particular, an outer triangle in the
right-triangle or `pi/3` rows may have the obvious similar-tile construction
while still requiring a separate source reduction to rule out other congruent
tile shapes and other counts.

## Open/Unresolved Ledger

- `19` is listed as open in the source corpus, but the workspace now records a
  derived obstruction ruling it out.
- The general claim "all primes `4r+3` are impossible" was unproved in the
  source corpus. This workspace now records a derived proof, assuming the
  source case reductions summarized above.
- The prime cases are now classified: `2`, `3`, and primes `1 mod 4` are
  positive, while primes `3 mod 4` greater than `3` are negative.
- Small non-prime values not covered by the positive families above are not
  classified here. The exact equilateral boundary-length scan gives a
  `2pi/3` candidate for `14` with tile `(7,8,13)` and outer side `28`, and the
  analogous `(3,5,7)` candidate for `15` with outer side `15`; the
  `equilateral_gamma_boundary.py` boundary-star check eliminates both. They
  also fail the induced triangular-lattice exact-cover check; for `14`, the
  lattice model is already blocked by an up-minus-down coloring count. A full
  negative proof still needs a source-level reduction showing that all relevant
  equilateral cases are covered by this rational/integer model.
- The same exact equilateral boundary-length scan finds `gamma=pi/3` candidates
  for `21` and `30`, and no equilateral candidates for `22`;
  `equilateral_pi_boundary.py` eliminates the `21` and `30` candidates and
  their `a,b` swaps by the full-boundary side-label star check.
- The current gap scan with primitive equilateral side bound `250` reports
  `14`, `15`, `21`, `22`, `30`, `33`, `35`, `38`, `39`, `42`, `46`, `51`,
  `55`, `56`, `57`, `60`, `62`, `63`, `66`, `69`, `70`, `76`, `78`, `86`,
  `87`, `88`, `91`, `92`, `93`, `94`, `95`, and `99` as open with no survivor
  in the currently encoded filters. This is not a proof of negativity until
  the source-reduction coverage gaps in the matrix above are closed.
- In the range `100..250`, the current encoded survivor list has shrunk to
  `132`, `156`, `175`, `189`, `198`, `204`, `224`, `228`, and `240`. All are
  `3alpha+2beta` isosceles-`alpha+beta` survivors of Beeson's Section 11.4
  filter; no non-isosceles `gamma=2pi/3` BLZ survivor remains in this range
  after the endpoint boundary-star check.
- A safe count-level diagnostic for these remaining isosceles-`alpha+beta`
  candidates is now recorded in
  `EXPERIMENTS/beeson_isosceles_alpha_plus_beta_filter.py --counts`. It accepts
  Beeson's positive `N=48` example. The survivors `132`, `156`, `175`, `198`,
  `204`, `224`, and `228` have unique Beeson side-count triples on both the
  equal side and base, while `189` and `240` still have multiple equal-side
  count decompositions. This is structural data, not a nonexistence proof.
- Zhang's conjectural exactness statements are not proved here.
- For `19`, all source-reduced cases are now ruled out in this workspace:
  similar/reptile, commensurable-angle, equilateral-outer, all isosceles
  outer-triangle, `3alpha+2beta=pi`, and all four non-isosceles
  `gamma=2pi/3` subcases.

Consequently, the requested complete classification of all positive integers `n`
is not presently available.
