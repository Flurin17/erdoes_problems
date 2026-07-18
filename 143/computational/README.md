# Exact finite-grid computation

`discrete_skeleton_exact.py` models the rational grid
\(A\subset [2,X]\cap Q^{-1}\mathbb Z\).  A numerator pair \(m<n\) is
compatible exactly when, writing \(r=n\bmod m\),
\[
Q\le r\le m-Q.
\]
The script asserts this modular test against an independent direct enumeration
of all relevant multipliers, solves maximum-weight independent set by exact
`Fraction` arithmetic, rechecks the returned set pairwise, and brute-forces
every graph with at most 16 vertices.

## Reproduction

Run from the repository root:

```sh
python3 143/computational/discrete_skeleton_exact.py \
  --q-max 4 --x-values 4,6,8,10 --compact
```

On 2026-07-17 this completed in under 0.01 seconds per instance.  For every
\(1\le Q\le4\) and \(X\in\{4,6,8,10\}\), both exact objectives were attained
by \(Q\{2,3,5,7\}\cap[2Q,XQ]\).  For example, at \(X=8\) the harmonic
optimum was
\[
\frac12+\frac13+\frac15+\frac17=\frac{247}{210}
\]
for every tested \(Q\), and the dyadic-log surrogate optimum was
\(223/420\).

## Interpretation

These finite results suggest that small-grid optimizers crystallize on the
integer sublattice and recover a primitive set.  They do **not** prove a
uniform-in-\(Q,X\) estimate, and absence of a finite counterexample is not
evidence of convergence for an infinite compatible sequence.  The exact
model is intended to falsify proposed inequalities and to generate candidates
for the uniform \(Q\)-thick estimate isolated in
`../attempts/rational_primitive.md`.

## Larger exact growth diagnostics

`qthick_growth.py` uses the compatibility graph rather than the conflict
graph and solves exact maximum-weight clique by branch and bound. A proper
weighted coloring supplies an integer upper bound at every node. Each row also
solves two constrained problems: all numerators divisible by $Q$, and at least
one numerator not divisible by $Q$. Small rows are independently checked by
the include/exclude dynamic program.

Reproduction commands used on 2026-07-17 and rerun on 2026-07-18:

```sh
python3 143/computational/qthick_growth.py \
  --q-values 1,2,3,4 --x-values 10,14 \
  --objectives both --dp-limit 32 --compact

python3 143/computational/qthick_growth.py \
  --q-values 2,4,6,8 --x-values 18 \
  --objectives both --dp-limit 32 --compact
```

The first command took below $0.04$ seconds per row and the second below
$2.7$ seconds per row on this workspace. For
$Q\in\{1,2,3,4\}$ at $X\in\{10,14\}$ and
$Q\in\{2,4,6,8\}$ at $X=18$, the harmonic and dyadic-log optima were
attained on $Q\mathbb N$; moreover, the separately optimized
forced-off-lattice value was strictly smaller. At $X=18$ the harmonic
optimum was $716167/510510$ and the dyadic-log optimum $119393/204204$,
independently of the tested $Q$.

This is exact finite evidence for the two rational surrogate objectives, not
a proof of crystallization and not a computation of the transcendental
$1/(x\log x)$ objective. A separate exact construction in
`../attempts/qthick_bottleneck.md` shows that crystallization already fails
for some other strictly decreasing weights.
