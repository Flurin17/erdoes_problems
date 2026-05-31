# Experiment Results

## Elementary Certificate Checks

Command:

```sh
python3 634/EXPERIMENTS/positive_constructions.py
```

Result:

- subdivision count verified for `m <= 11`;
- sum-of-two-squares coordinate certificates verified for `a,b <= 11`;
- primitive Zhang `c^2=a^2+ab+b^2` triples enumerated up to side bound `80`.

## Small Family Coverage

Command:

```sh
python3 634/EXPERIMENTS/small_family_coverage.py
```

The script includes:

- elementary positive families;
- Beeson negatives `7` and `11`;
- workspace prime obstructions for primes `3 mod 4`;
- recorded sufficient Beeson `3alpha+2beta=pi` constructions, including table
  entries `28,44,48,77,84` and the triquadratic sufficient values
  `112,126,153` below `250`;
- Zhang sufficiently-large `2pi/3` families within the search bound.

It deliberately reports everything else as unresolved by current certificates.

## Beeson `3alpha+2beta=pi` Sufficient Families

Command:

```sh
python3 634/EXPERIMENTS/beeson_3alpha2beta_sufficient.py --limit-n 250
```

Result:

```text
recorded sufficient 3alpha+2beta constructions <= 250: 8 counts
28: Beeson Table 7; triquadratic, M=2, tile=(2,3,4)
44: Beeson Table 7; isosceles-beta, M=6, tile=(2,3,4)
48: Beeson Table 7; isosceles-alpha+beta, M=4, tile=(2,3,4)
77: Beeson Table 7; (2alpha,alpha,2beta), M=5, tile=(2,3,4)
84: Beeson Table 7; isosceles-alpha, M=10, tile=(2,3,4)
112: TriangleTiling3 triquadratic sufficient condition; M=4, K=8, tile=(2, 3, 4)
126: TriangleTiling3 triquadratic sufficient condition; M=6, K=9, tile=(6, 5, 9)
153: TriangleTiling3 triquadratic sufficient condition; M=3, K=9, tile=(3, 8, 9)
```

Interpretation: these are positive certificates from recorded source sufficient
conditions. They do not settle `14` or `15`; both remain outside the current
constructive ledger.

## Composite Case Dashboard

Command:

```sh
python3 634/EXPERIMENTS/composite_case_dashboard.py 14 15 21 22 30 --equilateral-side-bound 250
```

Result summary:

```text
N=14:
  no elementary hit; similar/reptile subcase ruled out;
  no recorded 3alpha+2beta sufficient construction;
  no Zhang hit with side bound 80;
  equilateral outer arithmetic filter has candidates
    (7,8,13), L=28 and its a/b swap, both eliminated by the
    gamma=2pi/3 boundary-star check;
  3alpha+2beta necessary filter has 4 raw rational candidates, 0 remain after
    encoded local eliminations;
  the raw candidates are eliminated by one boundary-star obstruction and three
    strong isosceles-alpha+beta filter failures;
  isosceles gamma=2pi/3 has no arithmetic candidates;
  non-isosceles gamma=2pi/3 exact arithmetic filter has 0 candidates.

N=15:
  no elementary hit; similar/reptile subcase ruled out;
  no recorded 3alpha+2beta sufficient construction;
  no Zhang hit with side bound 80;
  equilateral outer arithmetic filter has candidates
    (3,5,7), L=15 and its a/b swap, both eliminated by the
    gamma=2pi/3 boundary-star check;
  3alpha+2beta necessary filter has 3 raw rational candidates, 0 remain after
    encoded local eliminations;
  the raw candidates are all eliminated by the strong isosceles-alpha+beta
    filter;
  isosceles gamma=2pi/3 has no arithmetic candidates;
  non-isosceles gamma=2pi/3 exact arithmetic filter has 0 candidates.
N=21:
  equilateral pi/3 candidates (16,21,19), L=84 and its a/b swap, both
    eliminated by the pi/3 boundary-star check;
  the encoded 3alpha+2beta and non-isosceles gamma candidates are locally
    eliminated.

N=22:
  no equilateral area candidate within primitive side bound 250;
  no surviving encoded 3alpha+2beta or gamma=2pi/3 candidates.

N=30:
  equilateral pi/3 candidates (8,15,13), L=60 and its a/b swap, both
    eliminated by the pi/3 boundary-star check;
  the encoded 3alpha+2beta and non-isosceles gamma candidates are locally
    eliminated.
```

Interpretation: the first composite obstruction gap has shifted to exact
coverage of the equilateral outer-triangle reductions. The encoded
`3alpha+2beta=pi`, isosceles `gamma=2pi/3`, non-isosceles `gamma=2pi/3`, and
side-bounded equilateral boundary-star filters leave no survivors for
`14`, `15`, `21`, `22`, or `30`.

## Composite Gap Scan

Command:

```sh
python3 634/EXPERIMENTS/composite_gap_scan.py 14 15 21 22 30 33 35 38 39 42 46 51 55 56 60 --equilateral-side-bound 250
```

Result summary:

```text
39,46,55,56: open with an encoded survivor
14,15,21,22,30,33,35,38,42,51,60: open with no survivor in the currently encoded filters
```

Interpretation: this scanner is a triage tool, not a proof engine. The
`open-no-encoded-survivor` values are exactly where the local implementation of
the source reductions is still incomplete.

## Equilateral Boundary-Length Checks

Side-bounded arithmetic command:

```sh
python3 634/EXPERIMENTS/equilateral_area_candidates.py 14 15 21 22 30 --side-bound 250
```

Result summary:

```text
N=14: 2pi/3 candidates (7,8,13), L=28 and swap
N=15: 2pi/3 candidates (3,5,7), L=15 and swap
N=21: pi/3 candidates (16,21,19), L=84 and swap
N=22: no candidates with primitive side entries <= 250
N=30: pi/3 candidates (8,15,13), L=60 and swap
```

Exact arithmetic command:

```sh
python3 634/EXPERIMENTS/equilateral_boundary_exact.py 14 15 21 22 30
```

Result summary:

```text
N=14: exactly the 2pi/3 candidates (7,8,13), L=28 and swap
N=15: exactly the 2pi/3 candidates (3,5,7), L=15 and swap
N=21: exactly the pi/3 candidates (16,21,19), L=84 and swap
N=22: 0 exact equilateral boundary-length candidates
N=30: exactly the pi/3 candidates (8,15,13), L=60 and swap
```

Interpretation: the exact command is stronger than the side-bounded scan. It
uses the fact that one outer side contains at most `N` full tile sides, writes
`L=xa+yb+zc` with `x+y+z<=N`, and solves the resulting rational quadratic or
quartic equations for `a/b`.

Boundary-star commands:

```sh
python3 634/EXPERIMENTS/equilateral_gamma_boundary.py 14 7 8
python3 634/EXPERIMENTS/equilateral_gamma_boundary.py 15 3 5
python3 634/EXPERIMENTS/equilateral_pi_boundary.py 21 16 21
python3 634/EXPERIMENTS/equilateral_pi_boundary.py 30 8 15
```

Results:

```text
N=14: 2 oriented side paths passing straight-vertex stars; 0 full boundary cycles
N=15: 4 oriented side paths passing straight-vertex stars; 0 full boundary cycles
N=21: 2 oriented side paths passing straight-vertex stars; 0 full boundary cycles
N=30: 2 oriented side paths passing straight-vertex stars; 0 full boundary cycles
```

Interpretation: the smallest `2pi/3` equilateral candidates for `14` and `15`
and the smallest `pi/3` equilateral candidates for `21` and `30` cannot even
form a compatible equilateral boundary from full tile sides. The `2pi/3` check
uses the corner condition `pi/3 = alpha + beta`; the `pi/3` check uses the
condition that each equilateral corner is a single `gamma` tile angle, with
boundary side labels `a` and `b`.

Lattice exact-cover commands:

```sh
python3 634/EXPERIMENTS/equilateral_lattice_exact_cover.py 15 2pi/3 3 5 --max-nodes 2000000
python3 634/EXPERIMENTS/equilateral_lattice_exact_cover.py 14 2pi/3 7 8 --max-nodes 2000000
```

Results:

```text
N=15 equilateral 2pi/3 tile (3, 5, 7)
outer side=15, outer unit cells=225, tile unit cells=15
outer up-minus-down=15, tile orientation differences=[-1, 1]
candidate placements=540, search nodes=29
no lattice-aligned exact cover found

N=14 equilateral 2pi/3 tile (7, 8, 13)
outer side=28, outer unit cells=784, tile unit cells=56
outer up-minus-down=28, tile orientation differences=[0]
candidate placements=720, search nodes=11
lattice orientation-coloring obstruction applies
no lattice-aligned exact cover found
```

Interpretation: these two smallest equilateral arithmetic candidates fail in
the induced triangular-lattice model. For `N=14`, the coloring count already
rules out the lattice model because every lattice-oriented tile has zero
up-minus-down difference while the outer triangle has difference `28`. This is
useful sanity evidence but not an obstruction to arbitrary tilings with shifted,
non-lattice vertices.

## `N=14` Triquadratic Boundary-Star Check

Command:

```sh
python3 634/EXPERIMENTS/beeson_3alpha2beta_boundary.py
```

Result:

```text
N=14 triquadratic 3alpha+2beta boundary-star check
tile sides (a,b,c)=(6,5,9); outer sides (28,15,27)
outer angles: (2alpha, beta, alpha+beta)
side-label decompositions by length:
  length 27: 15
  length 28: 16
  length 15: 3
oriented side paths passing straight-vertex stars:
  length 27: 2
  length 28: 6
  length 15: 2
feasible full boundary cycles: 0
boundary-star obstruction: candidate cannot be a tiling
```

Interpretation: the `N=14` triquadratic raw candidate survives Beeson's first
necessary equation but cannot satisfy even the local full-boundary side-label
star constraints.

The same script also checks the remaining `N=21` `3alpha+2beta=pi` candidate:

```text
N=21 isosceles-alpha 3alpha+2beta boundary-star check
tile sides (a,b,c)=(2,3,4); outer sides (12,12,21)
outer angles: (alpha, alpha, alpha+2beta)
oriented side paths passing straight-vertex stars:
  length 21: 10
  length 12: 6
feasible full boundary cycles: 0
boundary-star obstruction: candidate cannot be a tiling
```

## Zhang Constructive Families

Command:

```sh
python3 634/EXPERIMENTS/zhang_constructive_families.py --limit-n 5000 --limit-side 80 --prime 19
```

Result summary:

- the first nontrivial counts found by Zhang's proved families are
  `1215,1287,1440,1500,1815,1944,1960,...`;
- `1215` is Zhang Theorem 4 for tile `(3,5,7)`, equilateral outer triangle,
  `m=9`;
- `1440` is the `pi/3` analogue, Theorem 5, for tile `(5,8,7)`, `m=6`;
- no searched Zhang quadratic family hits the benchmark prime `19`.

Interpretation: Zhang's constructions are positive certificates only. The
failure to hit `19` is not an obstruction to some other tiling.

## `N=15` Zhang Lattice Exact-Cover Check

Command:

```sh
python3 634/EXPERIMENTS/zhang_15_lattice_exact_cover.py
```

Result:

```text
N=15 equilateral (3,5,7) lattice exact-cover check
outer unit cells=225
candidate placements=540
no lattice-aligned exact cover found
limitation: arbitrary non-lattice tilings are not excluded
```

Interpretation: tile `(3,5,7)` has exactly the right area for an equilateral
`15`-tiling, but the smallest triangular-lattice version does not exist. This
does not rule out a non-lattice construction for `15`.

## `3alpha+2beta=pi` Filter for `N=19`

Command:

```sh
python3 634/EXPERIMENTS/beeson_3alpha2beta_filter.py --json 19
```

Exact rational candidates that survive Beeson's necessary equations:

```json
{
  "19": [
    {
      "n": 19,
      "M": 1,
      "template": "3alpha+2beta=pi",
      "outer_triangle_case": "(a+b,a+b,a)",
      "s=a_over_c": "9/10",
      "primitive_tile_sides": [90, 19, 100],
      "necessary_polynomial_coefficients_in_increasing_degree": [18, -20],
      "sufficient_by_recorded_source_condition": false
    },
    {
      "n": 19,
      "M": 2,
      "template": "3alpha+2beta=pi",
      "outer_triangle_case": "(a+b,a+b,a)",
      "s=a_over_c": "15/23",
      "primitive_tile_sides": [345, 304, 529],
      "necessary_polynomial_coefficients_in_increasing_degree": [15, -23],
      "sufficient_by_recorded_source_condition": false
    },
    {
      "n": 19,
      "M": 3,
      "template": "3alpha+2beta=pi",
      "outer_triangle_case": "(a+b,a+b,a)",
      "s=a_over_c": "5/14",
      "primitive_tile_sides": [70, 171, 196],
      "necessary_polynomial_coefficients_in_increasing_degree": [10, -28],
      "sufficient_by_recorded_source_condition": false
    },
    {
      "n": 19,
      "M": 4,
      "template": "3alpha+2beta=pi",
      "outer_triangle_case": "(a+b,a+b,a)",
      "s=a_over_c": "3/35",
      "primitive_tile_sides": [105, 1216, 1225],
      "necessary_polynomial_coefficients_in_increasing_degree": [3, -35],
      "sufficient_by_recorded_source_condition": false
    }
  ]
}
```

Interpretation: these are first-pass necessary-equation survivors, not tilings.
Beeson's stronger Section 11.4 filter eliminates them, and his Theorem 21 rules
out prime `N` in the full `3alpha+2beta=pi` template.

Command:

```sh
python3 634/EXPERIMENTS/beeson_isosceles_alpha_plus_beta_filter.py 19 45 48 64 72 81 90 96 100 108
```

Result:

```text
N=19: 0 candidate(s)
N=45: 1 candidate(s)
  M=3 mu=5 sides=(6, 5, 9) X=45 Y=30
N=48: 1 candidate(s)
  M=4 mu=6 sides=(2, 3, 4) X=24 Y=12
N=64: 1 candidate(s)
  M=4 mu=32/5 sides=(15, 16, 25) X=160 Y=96
N=72: 1 candidate(s)
  M=6 mu=8 sides=(3, 8, 9) X=72 Y=24
N=81: 1 candidate(s)
  M=3 mu=27/5 sides=(20, 9, 25) X=135 Y=108
N=90: 1 candidate(s)
  M=6 mu=60/7 sides=(21, 40, 49) X=420 Y=180
N=96: 1 candidate(s)
  M=4 mu=48/7 sides=(35, 24, 49) X=336 Y=240
N=100: 1 candidate(s)
  M=5 mu=8 sides=(15, 16, 25) X=200 Y=120
N=108: 1 candidate(s)
  M=6 mu=9 sides=(2, 3, 4) X=36 Y=18
```

## Prime Dashboard for `p=19`

Command:

```sh
python3 634/EXPERIMENTS/prime_case_dashboard.py 19
```

Result:

```text
Prime case dashboard for p=19
- similar/reptile: ruled out. Snover-Waiveris-Williams: prime reptile counts are 3 or sums of two squares.
- commensurable-angle source table: ruled out. Beeson/Laczkovich table forms reduce prime counts to 2, 3, or sums of two squares.
- equilateral outer triangle: ruled out. Beeson: equilateral N-tiling with N>3 is not prime.
- 3alpha+2beta=pi template: ruled out. Beeson Theorem 21 proves prime N impossible in this template; sanity filters: 4 raw rational candidate(s), 4 isosceles-alpha+beta, 0 survive the stronger filter.
- gamma=2pi/3 isosceles outer triangle: ruled out by necessary arithmetic. Beeson Section 12 filter leaves 0 candidate(s).
- gamma=2pi/3 non-isosceles templates: ruled out for prime counts. BLZ Propositions 24 and 31 rule out primes in two templates; boundary integrality upgrades the Proposition 26 and 28 square-class templates to integer product formulas, hence no prime counts; minimum coefficients for those two templates are 88, 264; 2 exact N=19 square-class witness(es) illustrate why the extra boundary step is needed.
- other isosceles outer-triangle templates: ruled out for this prime. Beeson: right-tile isosceles counts are squares, even sums of squares, or 6m^2; gamma=2alpha counts are not squarefree; 3alpha+2beta is prime-ruled by TriangleTiling3.
```

Interpretation: `19` is ruled out across the source-reduced case list. The last
two BLZ square-class subfamilies
`(alpha,2alpha,3beta)` and `(alpha,2beta,2alpha+beta)` have exact arithmetic
witnesses, but boundary-integrality product formulas rule them out for `N=19`.
In fact the boundary step gives integer product formulas, so these two
non-isosceles templates have no prime-count tilings at all.

## Prime Scan Below `100`

Command:

```sh
python3 - <<'PY'
import sys
sys.path.insert(0, '634/EXPERIMENTS')
import prime_case_dashboard as mod
primes = [3,7,11,19,23,31,43,47,59,67,71,79,83]
for p in primes:
    rows = mod.status_for_prime(p)
    unresolved = [(n,s,d) for n,s,d in rows if 'remain' in s or 'partly' in s]
    print(p, unresolved)
PY
```

Result summary:

```text
p=3: positive by the 3m^2 family
p=7,11: ruled out by Beeson
p=19,23,31,43,47,59,67,71,79,83: all dashboard cases ruled out
```

Interpretation: the boundary-integrality product formulas rule out the hard
non-isosceles `gamma=2pi/3` templates for every prime `N`; the lone
source-filter survivor below `100`, namely `71`, is now removed by the boundary
orientation obstruction below.

## Prime `71` Boundary Analysis

Command:

```sh
python3 634/EXPERIMENTS/isosceles_71_boundary.py
```

Result:

```text
p=71 isosceles gamma=2pi/3 candidate
tile sides (a,b,c)=(39,16,49)
outer sides=(196,196,284)
equal-side decompositions as (b,a,c): [(0, 0, 4)]
base decompositions as (b,a,c): [(0, 1, 5), (8, 4, 0)]
base corners force a b-edge on the base, so the feasible base decomposition is (8,4,0)
side-to-side boundary tile-edge count B=20
3N-B=193
strict edge-to-edge tilings are impossible by parity
forced non-corner boundary vertices=17
alpha-angle parity: corners and boundary non-corners contribute even total; simple interior T-junctions would have to occur in odd number
angle vertex types:
  base corner angle alpha: [(1, 0, 0)]
  apex angle alpha+3beta: [(1, 3, 0)]
  straight boundary angle pi: [(1, 1, 1), (3, 3, 0)]
  simple interior T-junction tile-angle sum pi: [(1, 1, 1), (3, 3, 0)]
  interior angle 2pi: [(0, 0, 3), (2, 2, 2), (4, 4, 1), (6, 6, 0)]
stronger follow-up: isosceles_71_boundary_sequences.py rules out the non-strict case
```

Interpretation: this first boundary check rules out strict edge-to-edge tilings
for the `71` candidate. The stronger boundary sequence check below closes the
non-strict case as well.

## Prime `71` Boundary Sequence Orientation

Command:

```sh
python3 634/EXPERIMENTS/isosceles_71_boundary_sequences.py
```

Result:

```text
prime-71 boundary sequence orientation check
base decomposition: 8 b-edges and 4 a-edges, with b at both corners
base orders checked: 210
base orientations with alpha endpoints at both corners: 215040
valid base orientations: 0
feasible base (b0,b1) counts: []
feasible equal-side (b0,b1) counts: [(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)]
feasible full-boundary (b0,b1) counts: []
obstruction: a and b each have exactly one gamma endpoint; starting with alpha at the left base corner and forbidding gamma-gamma at a straight boundary vertex forces every base edge to end at gamma, contradicting the required alpha endpoint at the right base corner
```

Interpretation: the `71` candidate is impossible even with arbitrary shifted
T-junctions. The obstruction uses only full tile sides on the outer boundary:
the equal sides are forced to be `4c`, the base corners force `b`-edges with
alpha endpoints on the base, and every `a` or `b` edge has exactly one gamma
endpoint. Two gamma endpoints cannot meet at a straight boundary point because
`2gamma > pi`, so the forced base orientation propagates to a gamma endpoint at
the right base corner, contradicting the required alpha endpoint.

## Prime `71` Interior Matching Constraint

Command:

```sh
python3 634/EXPERIMENTS/isosceles_71_matching.py
```

Result:

```text
prime-71 interior length-only side-matching model
tile sides (a,b,c)=(39, 16, 49)
interior side incidences (a,b,c)=(67, 63, 63)
relation basis: 2a+2c=11b and 5a=3b+3c
components of length <= 194 have even c-incidence
first odd-c component: length 195, (0, 3, 3) | (5, 0, 0)
minimum possible max segment length from c-parity: 195
one length-only partition uses 18 matched segment(s):
  8 x length 195: (0, 3, 3) | (0, 3, 3) -> counts (0, 6, 6)
  6 x length 195: (5, 0, 0) | (5, 0, 0) -> counts (10, 0, 0)
  1 x length 194: (0, 6, 2) | (0, 6, 2) -> counts (0, 12, 4)
  1 x length 195: (0, 3, 3) | (5, 0, 0) -> counts (5, 3, 3)
  1 x length 186: (1, 0, 3) | (1, 0, 3) -> counts (2, 0, 6)
  1 x length 49: (0, 0, 1) | (0, 0, 1) -> counts (0, 0, 2)
```

Interpretation: this diagnostic ignores the boundary-orientation contradiction.
Within that relaxed length-only model, any hypothetical non-strict tiling would
need an interior matched segment of length at least `195`; the first way to get
odd `c`-incidence is the equality `5a = 3b + 3c`.

## Prime `71` Interface Angle Check

Command:

```sh
python3 634/EXPERIMENTS/isosceles_71_interface_angles.py
```

Result summary:

```text
prime-71 forced odd-c interface local angle check
interface length: 5a = 3b + 3c = 195
5a breakpoints: [39, 78, 117, 156]
5a feasible endpoint orientations: 6
3b+3c feasible edge orders: 20 of 20
all 20 orders are locally straight-angle feasible
no breakpoints coincide, so the minimal component has 4+5=9 T-junctions
```

Interpretation: the forced minimal odd-`c` component is not ruled out by local
straight-angle feasibility. This is now secondary evidence: the candidate is
already eliminated by the boundary-orientation obstruction.

## Prime `71` Lattice Coloring

Command:

```sh
python3 634/EXPERIMENTS/isosceles_71_lattice_coloring.py
```

Result:

```text
prime-71 triangular-lattice orientation coloring
outer up=22198, down=22106, difference=92
tile orientation differences=[-8, 8]
outer difference mod 8 = 4
lattice-vertex tilings are impossible by orientation-coloring
limitation: arbitrary non-strict T-junction tilings may use shifted lattice cosets
```

Interpretation: this gives a short independent obstruction to every strict
edge-to-edge tiling and every non-strict tiling whose vertices remain in the
induced triangular lattice. The full arbitrary shifted T-junction case is closed
instead by the boundary-orientation obstruction above.

## Isosceles `gamma=2pi/3` Filter

Command:

```sh
python3 634/EXPERIMENTS/gamma_2pi3_isosceles_filter.py 19 33 37 71 193
```

Result:

```text
N=19: 0 candidate(s)
N=33: 1 candidate(s)
  sides=(5, 3, 7) m=3 X=21 Y=33
N=37: 1 candidate(s)
  sides=(5, 16, 19) m=4 X=76 Y=148
N=71: 1 candidate(s)
  sides=(39, 16, 49) m=4 X=196 Y=284
N=193: 1 candidate(s)
  sides=(143, 25, 157) m=5 X=785 Y=965
```

Interpretation: in Beeson's isosceles `gamma=2pi/3` subcase, `19` is ruled out
by necessary arithmetic before any geometric backtracking is needed.

Prime scan command:

```sh
python3 634/EXPERIMENTS/gamma_2pi3_isosceles_filter.py --prime-scan 20000
```

Result:

```text
prime N == 3 mod 4 candidates up to 20000: 8
  N=71: sides=(39, 16, 49) m=4 X=196 Y=284
  N=443: sides=(155, 144, 259) m=12 X=3108 Y=5316
  N=863: sides=(735, 64, 769) m=8 X=6152 Y=6904
  N=2459: sides=(1659, 400, 1891) m=20 X=37820 Y=49180
  N=4019: sides=(819, 1600, 2131) m=40 X=85240 Y=160760
  N=8363: sides=(6795, 784, 7219) m=28 X=202132 Y=234164
  N=8663: sides=(1463, 3600, 4513) m=60 X=270780 Y=519780
  N=12671: sides=(12159, 256, 12289) m=16 X=196624 Y=202736
```

Interpretation: after the all-prime non-isosceles `gamma=2pi/3` obstruction,
the prime `3 mod 4` problem reduces to these isosceles arithmetic candidates in
the searched range. The first candidate, `71`, is eliminated by the boundary
sequence obstruction above; the next arithmetic benchmark is `443`.

Family diagnostic command:

```sh
python3 634/EXPERIMENTS/isosceles_prime_family.py --limit 20000
```

Result summary:

```text
prime isosceles gamma=2pi/3 candidates up to 20000: 8
N=71,443,863,2459,8363,12671: strict edge-to-edge boundary parity impossible
N=4019,8663: strict edge-to-edge boundary parity possible
```

The script recovers the parametrization
`p=3s^4+6r^2s^2-r^4`, checks that the equal sides decompose uniquely as `t`
copies of `c` for these candidates, and lists all compatible base decompositions.

Boundary-transition command:

```sh
python3 634/EXPERIMENTS/isosceles_prime_boundary_words.py --limit 100000
```

Result summary:

```text
prime isosceles boundary-word check up to 100000: 14
all viable base decompositions for all 14 arithmetic candidates are boundary-word obstructed
boundary-word obstructed candidates:
  [71, 443, 863, 2459, 4019, 8363, 8663, 12671, 21611, 28703, 46691, 46811, 56999, 86291]
boundary-word survivors: []
```

Interpretation: the upgraded automaton checks not just angle sums, but also the
side labels of the inward rays in each straight boundary vertex star. The
result supports the general transition-table proof in `PROOF.md`: an isosceles
outer base with `alpha` at both corners cannot be tiled in this template.

Length-matching command:

```sh
python3 634/EXPERIMENTS/isosceles_prime_matching.py --limit 20000
```

Result summary:

```text
length-only matching diagnostics up to 20000
```

Interpretation: after the stronger boundary-transition check there are no
boundary-word survivors left for the length-only diagnostic to inspect.

## BLZ Non-Isosceles `gamma=2pi/3` Filter

Exact arithmetic command:

```sh
python3 634/EXPERIMENTS/gamma_2pi3_nonisosceles_exact.py 14 15 21 22 30 88 143 264
```

Result summary:

```text
N=14,15,22: 0 exact non-isosceles gamma=2pi/3 arithmetic candidates
N=21: candidate in alpha,alpha+beta,alpha+2beta with sides=(5,16,19)
N=30: candidate in alpha,alpha+beta,alpha+2beta with sides=(7,8,13)
N=88: candidate in alpha,2beta,2alpha+beta with sides=(3,5,7)
N=143: candidates in 2alpha,2beta,alpha+beta with sides=(3,5,7),(5,3,7)
N=264: candidate in alpha,2alpha,3beta with sides=(5,3,7)
```

Interpretation: this exact filter supersedes the older side-bounded
square-class scan when checking whether a particular `N` can survive the
non-isosceles `gamma=2pi/3` arithmetic formulas.

Boundary-star command:

```sh
python3 634/EXPERIMENTS/gamma_2pi3_nonisosceles_boundary.py
```

Result summary:

```text
N=21 with tile (5,16,19), scale 4, outer sides (84,20,76):
  feasible full boundary cycles: 0
N=30 with tile (7,8,13), scale 4, outer sides (60,28,52):
  feasible full boundary cycles: 0
```

Interpretation: the exact arithmetic candidates for `N=21` and `N=30` in the
`(alpha,alpha+beta,alpha+2beta)` template fail the local boundary-star check.

Command:

```sh
python3 634/EXPERIMENTS/blz_gamma_2pi3_nonisosceles_filter.py 19 --limit-side 5000
```

Result:

```text
N=19: 0 BLZ square-class candidate(s) with side bound 5000
prime-impossible template: alpha,alpha+beta,alpha+2beta; BLZ Proposition 24: N=((a+b)/b)m^2; for prime N this forces a+b=N and b square, contradicting c^2=a^2+ab+b^2 with 0<c<a+b
prime-impossible template: 2alpha,2beta,alpha+beta; BLZ Proposition 31: N=(a+2b)(b+2a)m^2; the coefficient is a product of two integers >1
N=19 square-class cases for the two unresolved templates:
  alpha,2alpha,3beta: (A,S)=(1u^2,57v^2), (A,S)=(3u^2,19v^2), (A,S)=(19u^2,3v^2), (A,S)=(57u^2,1v^2)
  alpha,2beta,2alpha+beta: (A,S)=(1u^2,19v^2), (A,S)=(19u^2,1v^2)
N=19 exact square-class witnesses satisfying the BLZ necessary arithmetic:
  alpha,2beta,2alpha+beta: sides=(1131561,358039,1346761), (A,S)=(u^2,19v^2), u=1619, v=280, q=5320/1619
  alpha,2alpha,3beta: sides=(64291453825267166692191813022145,3194650169777924718531451006912,65946838654721589964381492334497), (A,S)=(u^2,57v^2), u=8407184675313313, v=1088102355826499, q=62021834282110443/8407184675313313
N=19 boundary-integrality obstruction for those witnesses/templates:
  alpha,2beta,2alpha+beta: ruled out for prime N; outer side ratio (ac, b(b+2a), c(a+b)); primitive, so N=(b+2a)(a+b)m^2; minimum attained at sides=(3,5,7) with primitive ratio=(21, 55, 56)
  alpha,2alpha,3beta: ruled out for prime N; outer side ratio (c^2, c(a+2b), 3b(a+b)); primitive, so N=3(a+2b)(a+b)m^2; minimum attained at sides=(5,3,7) with primitive ratio=(49, 77, 72)
```

Interpretation: two non-isosceles `gamma=2pi/3` templates are source-ruled for
all prime `N`. The remaining two templates have exact BLZ square-class
necessary conditions, and `N=19` survives those necessary conditions. The
boundary side-integrality condition then rules out the corresponding templates.
