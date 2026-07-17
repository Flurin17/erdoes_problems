# Lean formalization for Erdős Problem #796

This directory contains a Lean 4 formalization of the finite combinatorial
core used in `../PROOF.md`.  It has no Mathlib or third-party dependency.

`Erdos796.lean` verifies:

- the strict, unordered representation-count convention from the problem;
- cancellation: distinct representations of one positive integer have
  disjoint endpoints, so three representations use six distinct endpoints;
- the four equal antipodal products in a `K_{2,2,2}^{(3)}` cube;
- the exact finite cores
  `C0 = [1,2,3,5,7,11,13]`,
  `C1 = [1,3,4,5,6,7,11,13]`, and
  `C2 = [1,2,5,7,8,9,11,12,13,15]`;
- all nine ordered self/cross compatibility claims for these cores.  Lean
  evaluates the collision tables through 225 with `native_decide`; a proved
  bounded-support lemma extends each certificate to every product value.

The analytic number theory, large-prime tail lifting, infinite-profile
argument, and variational-limit asymptotic remain in the readable proof and
are not claimed to be formalized here.

## Reproduce

With Lean 4.32.0 installed:

```sh
lake build
```

The project is pinned by `lean-toolchain` to `leanprover/lean4:v4.32.0`.
