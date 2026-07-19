import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.NumberTheory.SmoothNumbers
import Mathlib.Analysis.PSeries
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# The absolutely convergent prime-power correction

This file separates the elementary, absolutely convergent part of the
Mertens logarithmic product from the genuinely analytic prime-reciprocal
asymptotic.  Every result here is unconditional.
-/

open Filter Topology
open scoped BigOperators

namespace Erdos415.Analytic

/-- The logarithmic prime product, with closed cutoff `p ≤ n`. -/
noncomputable def mobiusMertensPrimeLog (n : ℕ) : ℝ :=
  ∑ p ∈ (n + 1).primesBelow, Real.log ((p : ℝ) / (p - 1 : ℕ))

/-- The Mertens product assertion, stated locally so this route has no project
dependencies. -/
def MobiusMertensProductLog : Prop :=
  Tendsto
    (fun n : ℕ ↦ mobiusMertensPrimeLog n - Real.log (Real.log n))
    atTop (nhds Real.eulerMascheroniConstant)

/-- At a prime `p`, this is `log (p / (p - 1)) - 1 / p`; it is zero away
from the primes. -/
noncomputable def primeLogCorrection (n : ℕ) : ℝ :=
  if n.Prime then Real.log ((n : ℝ) / (n - 1 : ℕ)) - 1 / (n : ℝ) else 0

lemma primeLogCorrection_apply_of_prime {p : ℕ} (hp : p.Prime) :
    primeLogCorrection p =
      Real.log ((p : ℝ) / (p - 1 : ℕ)) - 1 / (p : ℝ) := by
  simp [primeLogCorrection, hp]

lemma primeLogCorrection_apply_of_not_prime {n : ℕ} (hn : ¬ n.Prime) :
    primeLogCorrection n = 0 := by
  simp [primeLogCorrection, hn]

/-- The correction is nonnegative. -/
lemma primeLogCorrection_nonneg (n : ℕ) : 0 ≤ primeLogCorrection n := by
  by_cases hp : n.Prime
  · rw [primeLogCorrection_apply_of_prime hp]
    have hn : (0 : ℝ) < n := by exact_mod_cast hp.pos
    have hnm1 : (0 : ℝ) < (n - 1 : ℕ) := by
      exact_mod_cast Nat.sub_pos_of_lt hp.one_lt
    have hratio : (0 : ℝ) < (n : ℝ) / (n - 1 : ℕ) := div_pos hn hnm1
    have hlog := Real.one_sub_inv_le_log_of_pos hratio
    have hcastsub : ((n - 1 : ℕ) : ℝ) = (n : ℝ) - 1 := by
      rw [Nat.cast_sub hp.one_lt.le]
      norm_num
    have hid : 1 - (((n : ℝ) / (n - 1 : ℕ))⁻¹) = 1 / (n : ℝ) := by
      rw [hcastsub, inv_div]
      field_simp
    rw [hid] at hlog
    linarith
  · simp [primeLogCorrection_apply_of_not_prime hp]

/-- A summable `O(p⁻²)` majorant for the correction. -/
lemma primeLogCorrection_le_two_div_sq (n : ℕ) :
    primeLogCorrection n ≤ 2 / (n : ℝ) ^ 2 := by
  by_cases hp : n.Prime
  · rw [primeLogCorrection_apply_of_prime hp]
    have hn : (0 : ℝ) < n := by exact_mod_cast hp.pos
    have hnm1 : (0 : ℝ) < (n - 1 : ℕ) := by
      exact_mod_cast Nat.sub_pos_of_lt hp.one_lt
    have hratio : (0 : ℝ) < (n : ℝ) / (n - 1 : ℕ) := div_pos hn hnm1
    have hlog := Real.log_le_sub_one_of_pos hratio
    have htwo : (2 : ℝ) ≤ n := by exact_mod_cast hp.two_le
    have hcastsub : ((n - 1 : ℕ) : ℝ) = (n : ℝ) - 1 := by
      rw [Nat.cast_sub hp.one_lt.le]
      norm_num
    rw [hcastsub] at hratio hlog hnm1 ⊢
    have hbound :
        (n : ℝ) / ((n : ℝ) - 1) - 1 - 1 / (n : ℝ) ≤
          2 / (n : ℝ) ^ 2 := by
      have hid :
          (n : ℝ) / ((n : ℝ) - 1) - 1 - 1 / (n : ℝ) =
            1 / ((n : ℝ) * ((n : ℝ) - 1)) := by
        field_simp
        ring
      rw [hid]
      apply (div_le_div_iff₀ (mul_pos hn hnm1) (sq_pos_of_pos hn)).2
      nlinarith
    exact (sub_le_sub_right hlog _).trans hbound
  · rw [primeLogCorrection_apply_of_not_prime hp]
    positivity

/-- The prime-power correction has an absolutely convergent sum. -/
theorem summable_primeLogCorrection : Summable primeLogCorrection := by
  refine Summable.of_nonneg_of_le primeLogCorrection_nonneg
    primeLogCorrection_le_two_div_sq ?_
  simpa [div_eq_mul_inv] using
    (Real.summable_one_div_nat_pow.mpr one_lt_two).mul_left 2

/-- The finite reciprocal-prime sum with the same closed endpoint as
`mobiusMertensPrimeLog`. -/
noncomputable def primeReciprocalSum (n : ℕ) : ℝ :=
  ∑ p ∈ (n + 1).primesBelow, 1 / (p : ℝ)

/-- Exact finite decomposition into reciprocal-prime and correction terms. -/
theorem mertensPrimeLog_eq_reciprocal_add_correction (n : ℕ) :
    mobiusMertensPrimeLog n = primeReciprocalSum n +
      ∑ p ∈ (n + 1).primesBelow, primeLogCorrection p := by
  rw [mobiusMertensPrimeLog, primeReciprocalSum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro p hp
  have hprime := (Nat.mem_primesBelow.mp hp).2
  rw [primeLogCorrection_apply_of_prime hprime]
  ring

/-- Partial prime sums of the correction converge to its full sum. -/
theorem tendsto_sum_primeLogCorrection :
    Tendsto
      (fun n : ℕ ↦ ∑ p ∈ (n + 1).primesBelow, primeLogCorrection p)
      atTop (nhds (∑' p : ℕ, primeLogCorrection p)) := by
  have h := summable_primeLogCorrection.hasSum.tendsto_sum_nat
  have h' := h.comp (tendsto_add_atTop_nat 1)
  apply h'.congr'
  filter_upwards with n
  rw [Nat.primesBelow, Finset.sum_filter]
  apply Finset.sum_congr rfl
  intro p hp
  by_cases hprime : p.Prime
  · simp [hprime]
  · simp [hprime, primeLogCorrection_apply_of_not_prime hprime]

/-- The correction constant used by the human proof. -/
noncomputable def primeLogCorrectionConstant : ℝ :=
  ∑' p : ℕ, primeLogCorrection p

/-- The Mertens logarithmic product is equivalent to the corresponding
prime-reciprocal asymptotic, with the correction constant made explicit. -/
theorem mertensProductLog_iff_primeReciprocal :
    MobiusMertensProductLog ↔
      Tendsto
        (fun n : ℕ ↦ primeReciprocalSum n - Real.log (Real.log n))
        atTop
        (nhds (Real.eulerMascheroniConstant - primeLogCorrectionConstant)) := by
  rw [MobiusMertensProductLog]
  constructor
  · intro h
    have hc := tendsto_sum_primeLogCorrection
    have ht := h.sub hc
    convert ht using 1
    · funext n
      simp only [mertensPrimeLog_eq_reciprocal_add_correction,
        primeLogCorrectionConstant]
      ring
    · simp only [primeLogCorrectionConstant]
  · intro h
    have hc := tendsto_sum_primeLogCorrection
    have ht := h.add hc
    convert ht using 1
    · funext n
      simp only [mertensPrimeLog_eq_reciprocal_add_correction,
        primeLogCorrectionConstant]
      ring
    · simp only [primeLogCorrectionConstant]
      ring

end Erdos415.Analytic
