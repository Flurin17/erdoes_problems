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
