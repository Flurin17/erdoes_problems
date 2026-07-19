import Mathlib

/-!
# Prime-power expansion of the Mertens logarithm

This file develops the exact prime-power expansion needed in an elementary
von Mangoldt proof of Mertens' product formula.  In particular, it separates
the reciprocal-prime term from an absolutely convergent higher-prime-power
correction.
-/

open Filter Topology
open scoped ArithmeticFunction BigOperators

namespace Erdos415.Analytic

/-- The logarithm of the finite Mertens product, with closed prime cutoff.
This local name keeps the module independent of the other analytic files. -/
noncomputable def mertensPrimeLogMM (n : ℕ) : ℝ :=
  ∑ p ∈ (n + 1).primesBelow, Real.log ((p : ℝ) / (p - 1 : ℕ))

/-- The Taylor series for the logarithmic Euler factor at `p`. -/
noncomputable def primeLogSeries (p : ℕ) : ℝ :=
  ∑' j : ℕ, ((p : ℝ)⁻¹) ^ (j + 1) / (j + 1)

/-- The Taylor series at a prime is exactly the logarithm of its Euler factor. -/
theorem hasSum_primeLogSeries {p : ℕ} (hp : p.Prime) :
    HasSum (fun j : ℕ ↦ ((p : ℝ)⁻¹) ^ (j + 1) / (j + 1))
      (Real.log ((p : ℝ) / (p - 1 : ℕ))) := by
  have hp1 : (1 : ℝ) < p := by exact_mod_cast hp.one_lt
  have habs : |((p : ℝ)⁻¹)| < (1 : ℝ) := by
    rw [abs_inv, abs_of_pos (by positivity)]
    exact inv_lt_one_of_one_lt₀ hp1
  have hs := Real.hasSum_pow_div_log_of_abs_lt_one habs
  convert hs using 1
  have hp_cast_ne : (p : ℝ) ≠ 0 := by positivity
  have hpm1_cast : ((p - 1 : ℕ) : ℝ) = (p : ℝ) - 1 := by
    rw [Nat.cast_sub hp.one_lt.le]
    norm_num
  have hpm1_pos : (0 : ℝ) < (p - 1 : ℕ) := by
    exact_mod_cast Nat.sub_pos_of_lt hp.one_lt
  have hone_sub : 1 - (p : ℝ)⁻¹ = ((p - 1 : ℕ) : ℝ) / p := by
    rw [hpm1_cast]
    field_simp
  rw [hone_sub, Real.log_div (ne_of_gt hpm1_pos) hp_cast_ne,
    Real.log_div hp_cast_ne (ne_of_gt hpm1_pos)]
  ring

theorem primeLogSeries_eq {p : ℕ} (hp : p.Prime) :
    primeLogSeries p = Real.log ((p : ℝ) / (p - 1 : ℕ)) :=
  (hasSum_primeLogSeries hp).tsum_eq

/-- The contribution from powers `p^r` with `r ≥ 2`. -/
noncomputable def higherPrimePowerCorrection (p : ℕ) : ℝ :=
  ∑' j : ℕ, ((p : ℝ)⁻¹) ^ (j + 2) / (j + 2)

theorem primeLogSeries_eq_inv_add_correction {p : ℕ} (hp : p.Prime) :
    primeLogSeries p = (p : ℝ)⁻¹ + higherPrimePowerCorrection p := by
  have hs := (hasSum_primeLogSeries hp).summable
  rw [primeLogSeries, hs.tsum_eq_zero_add, higherPrimePowerCorrection]
  congr 1
  · norm_num
  · apply tsum_congr
    intro j
    rw [show j + 1 + 1 = j + 2 by omega]
    norm_num [Nat.cast_add]
    ring

/-- Reciprocal-prime sum with the same closed cutoff as `mertensPrimeLog`. -/
noncomputable def primeReciprocalSum (n : ℕ) : ℝ :=
  ∑ p ∈ (n + 1).primesBelow, (p : ℝ)⁻¹

/-- Finite higher-prime-power correction with closed prime cutoff. -/
noncomputable def finiteHigherPrimePowerCorrection (n : ℕ) : ℝ :=
  ∑ p ∈ (n + 1).primesBelow, higherPrimePowerCorrection p

/-- Exact decomposition into reciprocal primes and higher prime powers. -/
theorem mertensPrimeLog_eq_reciprocal_add_correction (n : ℕ) :
    mertensPrimeLogMM n =
      primeReciprocalSum n + finiteHigherPrimePowerCorrection n := by
  rw [mertensPrimeLogMM, primeReciprocalSum, finiteHigherPrimePowerCorrection,
    ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro p hp
  rw [← primeLogSeries_eq_inv_add_correction (Nat.prime_of_mem_primesBelow hp),
    primeLogSeries_eq (Nat.prime_of_mem_primesBelow hp)]

theorem higherPrimePowerCorrection_nonneg (p : ℕ) :
    0 ≤ higherPrimePowerCorrection p := by
  exact tsum_nonneg fun j ↦ by positivity

/-- A uniform square-summable majorant for all higher powers at a prime. -/
theorem higherPrimePowerCorrection_le {p : ℕ} (hp : p.Prime) :
    higherPrimePowerCorrection p ≤ 2 * ((p : ℝ)⁻¹) ^ 2 := by
  let r : ℝ := (p : ℝ)⁻¹
  have hr0 : 0 ≤ r := by dsimp [r]; positivity
  have hrhalf : r ≤ (1 / 2 : ℝ) := by
    dsimp [r]
    exact inv_le_inv₀ (by norm_num) (by exact_mod_cast hp.two_le)
  have hmajor : Summable (fun j : ℕ ↦ r ^ 2 * (1 / 2 : ℝ) ^ j) :=
    summable_geometric_two.mul_left (r ^ 2)
  have hterm (j : ℕ) :
      r ^ (j + 2) / (j + 2) ≤ r ^ 2 * (1 / 2 : ℝ) ^ j := by
    calc
      r ^ (j + 2) / (j + 2) ≤ r ^ (j + 2) :=
        div_le_self (pow_nonneg hr0 _) (by exact_mod_cast Nat.succ_le_succ (Nat.succ_le_succ j.zero_le))
      _ = r ^ 2 * r ^ j := by rw [show j + 2 = 2 + j by omega, pow_add]
      _ ≤ r ^ 2 * (1 / 2 : ℝ) ^ j := by
        gcongr
  calc
    higherPrimePowerCorrection p
        ≤ ∑' j : ℕ, r ^ 2 * (1 / 2 : ℝ) ^ j := by
          apply hmajor.tsum_le_tsum
          intro j
          simpa [higherPrimePowerCorrection, r] using hterm j
    _ = 2 * r ^ 2 := by rw [tsum_mul_left, tsum_geometric_two]; ring
    _ = 2 * ((p : ℝ)⁻¹) ^ 2 := rfl

/-- The higher-prime-power term, extended by zero away from primes. -/
noncomputable def higherPrimePowerTerm (p : ℕ) : ℝ :=
  if p.Prime then higherPrimePowerCorrection p else 0

theorem higherPrimePowerTerm_nonneg (p : ℕ) : 0 ≤ higherPrimePowerTerm p := by
  rw [higherPrimePowerTerm]
  split_ifs
  · exact higherPrimePowerCorrection_nonneg p
  · exact le_rfl

theorem summable_higherPrimePowerTerm : Summable higherPrimePowerTerm := by
  have hsq : Summable (fun p : ℕ ↦ 2 * ((p : ℝ)⁻¹) ^ 2) :=
    (Real.summable_nat_pow_inv.mpr (by omega : 1 < 2)).mul_left 2
  refine Summable.of_nonneg_of_le higherPrimePowerTerm_nonneg ?_ hsq
  intro p
  rw [higherPrimePowerTerm]
  split_ifs with hp
  · exact higherPrimePowerCorrection_le hp
  · positivity

/-- The absolutely convergent constant contributed by powers `p^r`, `r ≥ 2`. -/
noncomputable def totalHigherPrimePowerCorrection : ℝ :=
  ∑' p : ℕ, higherPrimePowerTerm p

theorem finiteHigherPrimePowerCorrection_eq_sum_range (n : ℕ) :
    finiteHigherPrimePowerCorrection n =
      ∑ p ∈ Finset.range (n + 1), higherPrimePowerTerm p := by
  rw [finiteHigherPrimePowerCorrection, Nat.primesBelow, Finset.sum_filter]
  apply Finset.sum_congr rfl
  intro p hp
  simp only [higherPrimePowerTerm]
  split_ifs <;> simp_all

/-- Finite higher-power corrections converge to the global correction. -/
theorem tendsto_finiteHigherPrimePowerCorrection :
    Tendsto finiteHigherPrimePowerCorrection atTop
      (𝓝 totalHigherPrimePowerCorrection) := by
  have ht : Tendsto (fun n : ℕ ↦ n + 1) atTop atTop :=
    (tendsto_add_atTop_iff_nat 1).mpr tendsto_id
  have h := summable_higherPrimePowerTerm.hasSum.tendsto_sum_nat.comp ht
  apply h.congr'
  filter_upwards with n
  rw [finiteHigherPrimePowerCorrection_eq_sum_range, Finset.sum_filter]

/-- Mertens' logarithmic product is reduced, with no loss in the constant,
to the reciprocal-prime asymptotic and one explicit absolutely convergent
prime-power correction. -/
theorem mertensPrimeLog_tendsto_iff_primeReciprocalSum :
    Tendsto (fun n : ℕ ↦ mertensPrimeLogMM n - Real.log (Real.log n)) atTop
        (𝓝 Real.eulerMascheroniConstant) ↔
      Tendsto (fun n : ℕ ↦ primeReciprocalSum n - Real.log (Real.log n)) atTop
        (𝓝 (Real.eulerMascheroniConstant - totalHigherPrimePowerCorrection)) := by
  constructor
  · intro h
    convert h.sub tendsto_finiteHigherPrimePowerCorrection using 1
    · funext n
      rw [mertensPrimeLog_eq_reciprocal_add_correction]
      ring
    · ring
  · intro h
    convert h.add tendsto_finiteHigherPrimePowerCorrection using 1
    · funext n
      rw [mertensPrimeLog_eq_reciprocal_add_correction]
      ring
    · ring

end Erdos415.Analytic
