import Mathlib.NumberTheory.EulerProduct.Basic
import Mathlib.NumberTheory.Harmonic.Bounds
import Mathlib.NumberTheory.Harmonic.EulerMascheroni

/-!
# The harmonic-number side of Mertens' product

The finite Euler product below is written with the endpoint convention `p < N`, matching
`Nat.primesBelow`.  The main identity proved here says that it is exactly the sum of `1 / m`
over the positive `N`-smooth integers.  This is the algebraic bridge used in the elementary
harmonic-number proof of Mertens' product theorem.

The remaining analytic estimate needed for the full theorem is a uniform comparison of this
smooth harmonic sum with `exp Real.eulerMascheroniConstant * log N`.  That estimate is not part
of mathlib 4.19's Euler-product API, so this file records the dependency-free identities on
which such an estimate must be built.
-/

open scoped BigOperators Topology

namespace Erdos415

/-- The Mertens product over primes strictly below `N`. -/
noncomputable def mertensProduct (N : ℕ) : ℝ :=
  ∏ p ∈ N.primesBelow, (1 - (p : ℝ)⁻¹)⁻¹

/-- The completely multiplicative reciprocal map on natural numbers. -/
noncomputable def reciprocalHom : ℕ →* ℝ where
  toFun n := (n : ℝ)⁻¹
  map_one' := by norm_num
  map_mul' m n := by
    push_cast
    exact mul_inv _ _

@[simp]
theorem reciprocalHom_apply (n : ℕ) : reciprocalHom n = (n : ℝ)⁻¹ := rfl

private theorem norm_reciprocalHom_prime_lt_one {p : ℕ} (hp : p.Prime) :
    ‖reciprocalHom p‖ < 1 := by
  rw [reciprocalHom_apply, Real.norm_eq_abs, abs_inv, abs_of_pos]
  · exact inv_lt_one_of_one_lt₀ (by exact_mod_cast hp.one_lt)
  · exact_mod_cast hp.pos

/-- The finite product is the convergent harmonic sum over all positive `N`-smooth numbers. -/
theorem mertensProduct_hasSum_smooth (N : ℕ) :
    HasSum (fun m : N.smoothNumbers ↦ ((m : ℕ) : ℝ)⁻¹) (mertensProduct N) := by
  simpa only [mertensProduct, reciprocalHom_apply] using
    (EulerProduct.summable_and_hasSum_smoothNumbers_prod_primesBelow_geometric
      (f := reciprocalHom) (fun {_} hp ↦ norm_reciprocalHom_prime_lt_one hp) N).2

/-- The value form of `mertensProduct_hasSum_smooth`. -/
theorem mertensProduct_eq_tsum_smooth (N : ℕ) :
    mertensProduct N = ∑' m : N.smoothNumbers, ((m : ℕ) : ℝ)⁻¹ :=
  (mertensProduct_hasSum_smooth N).tsum_eq.symm

/-- Every factor in the finite Mertens product is positive. -/
theorem mertensProduct_pos (N : ℕ) : 0 < mertensProduct N := by
  rw [mertensProduct]
  exact Finset.prod_pos fun p hp ↦ by
    have hp' := Nat.prime_of_mem_primesBelow hp
    exact inv_pos.mpr (sub_pos.mpr (inv_lt_one_of_one_lt₀ (by exact_mod_cast hp'.one_lt)))

/-- The ordinary harmonic sum embeds in the smooth harmonic sum.  The shift in the product's
argument is solely due to the strict endpoint convention in `Nat.primesBelow`. -/
theorem harmonic_le_mertensProduct (N : ℕ) :
    (harmonic N : ℝ) ≤ mertensProduct (N + 1) := by
  let e : {i // i ∈ Finset.range N} ↪ (N + 1).smoothNumbers :=
    { toFun := fun i ↦
        ⟨i.1 + 1, Nat.mem_smoothNumbers_of_lt (Nat.succ_pos _) (by
          have hi := Finset.mem_range.mp i.2
          omega)⟩
      inj' := by
        intro i j hij
        apply Subtype.ext
        have hval : i.1 + 1 = j.1 + 1 := congrArg Subtype.val hij
        omega }
  let s : Finset ((N + 1).smoothNumbers) := (Finset.range N).attach.map e
  calc
    (harmonic N : ℝ) = ∑ i ∈ (Finset.range N).attach, (((i.1 + 1 : ℕ) : ℝ)⁻¹) := by
      rw [harmonic, Rat.cast_sum]
      simp only [Rat.cast_inv, Rat.cast_natCast]
      symm
      exact Finset.sum_attach (Finset.range N) (fun i ↦ (((i + 1 : ℕ) : ℝ)⁻¹))
    _ = ∑ m ∈ s, (((m : ℕ) : ℝ)⁻¹) := by
      change _ = ∑ m ∈ (Finset.range N).attach.map e, (((m : ℕ) : ℝ)⁻¹)
      rw [Finset.sum_map]
      rfl
    _ ≤ mertensProduct (N + 1) :=
      sum_le_hasSum s (fun m _ ↦ inv_nonneg.mpr (by positivity))
        (mertensProduct_hasSum_smooth (N + 1))

end Erdos415
