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
