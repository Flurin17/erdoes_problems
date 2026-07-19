import Mathlib

/-!
# The prime-power error in the logarithmic Mertens sum

This module identifies the absolutely convergent higher-prime-power part of
the logarithmic Euler factors with the non-prime part of the normalized von
Mangoldt sum.  The final theorem says that the two corresponding finite sums
differ by a quantity tending to zero.
-/

open Filter Topology
open scoped ArithmeticFunction BigOperators

namespace Erdos415.Analytic

/-- The normalized von Mangoldt summand. -/
noncomputable def normalizedMangoldt (n : ℕ) : ℝ :=
  ArithmeticFunction.vonMangoldt n / ((n : ℝ) * Real.log n)

/-- The normalized von Mangoldt summand with the primes removed. -/
noncomputable def nonprimeNormalizedMangoldt (n : ℕ) : ℝ :=
  if n.Prime then 0 else normalizedMangoldt n

/-- The contribution of the prime power `p ^ (k + 2)`. -/
noncomputable def higherPrimePowerTerm (p : Nat.Primes) (k : ℕ) : ℝ :=
  ((p : ℝ)⁻¹) ^ (k + 2) / (k + 2)

/-- The part of a logarithmic Euler factor beyond its reciprocal-prime term. -/
noncomputable def logarithmicPrimeCorrection (p : Nat.Primes) : ℝ :=
  Real.log ((p : ℝ) / ((p : ℕ) - 1 : ℕ)) - (p : ℝ)⁻¹

/-- Taylor expansion of one logarithmic Euler factor. -/
lemma hasSum_logarithmicEulerFactor (p : Nat.Primes) :
    HasSum (fun k : ℕ ↦ ((p : ℝ)⁻¹) ^ (k + 1) / (k + 1))
      (Real.log ((p : ℝ) / ((p : ℕ) - 1 : ℕ))) := by
  have hp1 : (1 : ℝ) < p := by exact_mod_cast p.prop.one_lt
  have habs : |((p : ℝ)⁻¹)| < (1 : ℝ) := by
    rw [abs_inv, abs_of_pos (by positivity)]
    exact inv_lt_one_of_one_lt₀ hp1
  have hs := Real.hasSum_pow_div_log_of_abs_lt_one habs
  convert hs using 1
  have hpne : (p : ℝ) ≠ 0 := by positivity
  have hpm1 : (((p : ℕ) - 1 : ℕ) : ℝ) = (p : ℝ) - 1 := by
    rw [Nat.cast_sub p.prop.one_lt.le]
    norm_num
  have hpm1pos : (0 : ℝ) < ((p : ℕ) - 1 : ℕ) := by
    exact_mod_cast Nat.sub_pos_of_lt p.prop.one_lt
  have hone : 1 - (p : ℝ)⁻¹ = (((p : ℕ) - 1 : ℕ) : ℝ) / p := by
    rw [hpm1]
    field_simp
  rw [hone, Real.log_div (ne_of_gt hpm1pos) hpne,
    Real.log_div hpne (ne_of_gt hpm1pos)]
  ring

/-- The tail of the Taylor series is exactly the correction after `1 / p`. -/
lemma logarithmicPrimeCorrection_eq_tsum (p : Nat.Primes) :
    logarithmicPrimeCorrection p = ∑' k : ℕ, higherPrimePowerTerm p k := by
  have hs := hasSum_logarithmicEulerFactor p
  rw [logarithmicPrimeCorrection, ← hs.tsum_eq, hs.summable.tsum_eq_zero_add]
  have htail :
      (∑' k : ℕ, ((p : ℝ)⁻¹) ^ (k + 1 + 1) / ((k + 1 : ℕ) + 1)) =
        ∑' k : ℕ, higherPrimePowerTerm p k := by
    apply tsum_congr
    intro k
    simp only [higherPrimePowerTerm]
    rw [show k + 1 + 1 = k + 2 by omega]
    norm_num [Nat.cast_add]
    ring
  simpa only [Nat.cast_zero, zero_add, pow_one, Nat.cast_one, div_one,
    add_sub_cancel_left] using htail

/-- The double series of contributions from powers of exponent at least two
is absolutely convergent. -/
lemma summable_higherPrimePowerTerm :
    Summable (fun pk : Nat.Primes × ℕ ↦ higherPrimePowerTerm pk.1 pk.2) := by
  have hp : Summable (fun p : Nat.Primes ↦ ((p : ℝ) ^ (-2 : ℝ))) :=
    Nat.Primes.summable_rpow.mpr (by norm_num)
  have hp' : Summable (fun p : Nat.Primes ↦ ((p : ℝ)⁻¹) ^ 2) := by
    convert hp using 1
    ext p
    rw [← Real.rpow_natCast]
    norm_num [Real.rpow_neg (by positivity : (0 : ℝ) ≤ p)]
  have hk : Summable (fun k : ℕ ↦ ((2 : ℝ)⁻¹) ^ k) :=
    summable_geometric_of_lt_one (by positivity) (by norm_num)
  have hprod : Summable (fun pk : Nat.Primes × ℕ ↦
      ((pk.1 : ℝ)⁻¹) ^ 2 * ((2 : ℝ)⁻¹) ^ pk.2) :=
    hp'.mul_of_nonneg hk
      (fun p ↦ pow_nonneg (inv_nonneg.mpr (Nat.cast_nonneg p)) _)
      (fun k ↦ pow_nonneg (by norm_num : (0 : ℝ) ≤ (2 : ℝ)⁻¹) k)
  refine hprod.of_nonneg_of_le
    (fun pk ↦ div_nonneg (pow_nonneg (inv_nonneg.mpr (Nat.cast_nonneg pk.1)) _)
      (add_nonneg (Nat.cast_nonneg _) (by norm_num))) ?_
  rintro ⟨p, k⟩
  have hp0 : 0 ≤ (p : ℝ)⁻¹ := by positivity
  have hp2 : (p : ℝ)⁻¹ ≤ (2 : ℝ)⁻¹ := by
    exact (inv_le_inv₀ (by exact_mod_cast p.prop.pos) (by norm_num : (0 : ℝ) < 2)).2
      (by exact_mod_cast p.prop.two_le)
  have hpow : ((p : ℝ)⁻¹) ^ (k + 2) ≤
      ((p : ℝ)⁻¹) ^ 2 * ((2 : ℝ)⁻¹) ^ k := by
    rw [show k + 2 = 2 + k by omega, pow_add]
    exact mul_le_mul_of_nonneg_left (pow_le_pow_left₀ hp0 hp2 k) (by positivity)
  have hkden : (1 : ℝ) ≤ (k : ℝ) + 2 := by
    have hk0 : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
    linarith
  exact (div_le_self (by positivity) hkden).trans hpow

end Erdos415.Analytic
