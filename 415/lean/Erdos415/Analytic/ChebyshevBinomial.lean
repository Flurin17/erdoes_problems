import Mathlib.NumberTheory.Bertrand
import Mathlib.Analysis.Asymptotics.Theta
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# Chebyshev bounds from central binomial coefficients

This file gives a self-contained elementary proof that Chebyshev's theta function is of
linear order.  The only substantial input is the central-binomial-coefficient estimate already
used in mathlib's proof of Bertrand's postulate.
-/

open scoped BigOperators

namespace Erdos415.ChebyshevBinomial

/-- Chebyshev's theta function, with primes at the endpoint included. -/
noncomputable def theta (n : ℕ) : ℝ :=
  ∑ p ∈ (Finset.range (n + 1)).filter Nat.Prime, Real.log p

/-- Chebyshev theta is the logarithm of the primorial. -/
theorem theta_eq_log_primorial (n : ℕ) : theta n = Real.log (primorial n) := by
  rw [theta, primorial, ← Real.log_prod]
  · simp only [Nat.cast_prod]
  · intro p hp
    exact_mod_cast (Finset.mem_filter.mp hp).2.ne_zero

/-- The primorial is monotone. -/
theorem monotone_primorial : Monotone primorial := by
  intro m n hmn
  rw [primorial, primorial]
  refine Finset.prod_le_prod_of_subset_of_one_le' ?_ ?_
  · intro p hp
    simp only [Finset.mem_filter, Finset.mem_range] at hp ⊢
    exact ⟨hp.1.trans_le (Nat.succ_le_succ hmn), hp.2⟩
  · intro p hp _
    exact (Finset.mem_filter.mp hp).2.one_lt.le

/-- The contribution from primes above `sqrt (2*n)` occurs with exponent at most one; the
remaining prime powers are bounded individually by `2*n`. -/
theorem centralBinom_le_pow_sqrt_mul_primorial (n : ℕ) (hn : 0 < n) :
    Nat.centralBinom n ≤ (2 * n) ^ Nat.sqrt (2 * n) * primorial (2 * n) := by
  let S := {p ∈ Finset.range (2 * n + 1) | Nat.Prime p}
  let f : ℕ → ℕ := fun p ↦ p ^ (Nat.centralBinom n).factorization p
  have hfac : ∏ p ∈ S, f p = Nat.centralBinom n := by
    rw [← Nat.prod_pow_factorization_centralBinom]
    dsimp only [S]
    exact Finset.prod_filter_of_ne fun p _ hp ↦ by
      contrapose! hp
      dsimp only [f]
      rw [Nat.factorization_eq_zero_of_non_prime _ hp, pow_zero]
  rw [← hfac, ← Finset.prod_filter_mul_prod_filter_not S (· ≤ Nat.sqrt (2 * n))]
  apply Nat.mul_le_mul
  · refine (Finset.prod_le_prod' fun p _ ↦ (?_ : f p ≤ 2 * n)).trans ?_
    · exact Nat.pow_factorization_choose_le (Nat.mul_pos Nat.two_pos hn)
    · have hcard : ({p ∈ S | p ≤ Nat.sqrt (2 * n)} : Finset ℕ).card ≤
          Nat.sqrt (2 * n) := by
        have hsubset : ({p ∈ S | p ≤ Nat.sqrt (2 * n)} : Finset ℕ) ⊆
            Finset.Icc 1 (Nat.sqrt (2 * n)) := by
          intro p hp
          simp only [Finset.mem_filter] at hp
          exact Finset.mem_Icc.mpr
            ⟨(Finset.mem_filter.mp hp.1).2.one_lt.le, hp.2⟩
        calc
          _ ≤ (Finset.Icc 1 (Nat.sqrt (2 * n))).card := Finset.card_le_card hsubset
          _ = Nat.sqrt (2 * n) := by rw [Nat.card_Icc, Nat.add_sub_cancel]
      simpa only [Finset.prod_const] using
        Nat.pow_le_pow_right (Nat.mul_pos Nat.two_pos hn) hcard
  · refine (Finset.prod_le_prod' fun p hp ↦ (?_ : f p ≤ p)).trans ?_
    · obtain ⟨hpS, hpbig⟩ := Finset.mem_filter.mp hp
      refine (Nat.pow_le_pow_right (Finset.mem_filter.mp hpS).2.pos ?_).trans (pow_one p).le
      exact Nat.factorization_choose_le_one (Nat.sqrt_lt'.mp (not_le.mp hpbig))
    · refine Finset.prod_le_prod_of_subset_of_one_le' ?_ ?_
      · intro p hp
        obtain ⟨hpS, _⟩ := Finset.mem_filter.mp hp
        dsimp only [S] at hpS
        simpa only [primorial, Finset.mem_filter, Finset.mem_range] using hpS
      · intro p hp _
        exact (Finset.mem_filter.mp hp).2.one_lt.le

/-- The key exponential lower bound for primorials at even arguments. -/
theorem four_pow_two_mul_div_three_lt_primorial_two_mul (n : ℕ) (hn : 512 ≤ n) :
    4 ^ (2 * n / 3) < primorial (2 * n) := by
  by_contra h
  have hprim : primorial (2 * n) ≤ 4 ^ (2 * n / 3) := Nat.le_of_not_lt h
  have hpos : 0 < n := by omega
  have hchoose := centralBinom_le_pow_sqrt_mul_primorial n hpos
  have hfour : 4 ^ n < n * Nat.centralBinom n :=
    Nat.four_pow_lt_mul_centralBinom n (by omega)
  have hmain := bertrand_main_inequality hn
  have hcontra : 4 ^ n < n * ((2 * n) ^ Nat.sqrt (2 * n) * 4 ^ (2 * n / 3)) :=
    hfour.trans_le (Nat.mul_le_mul_left n
      (hchoose.trans (Nat.mul_le_mul_left _ hprim)))
  rw [← Nat.mul_assoc] at hcontra
  exact (Nat.not_lt_of_ge hmain) hcontra

/-- A lower primorial bound at all sufficiently large arguments. -/
theorem four_pow_div_four_le_primorial (n : ℕ) (hn : 1024 ≤ n) :
    4 ^ (n / 4) ≤ primorial n := by
  have hhalf : 512 ≤ n / 2 := by omega
  have hexp : n / 4 ≤ 2 * (n / 2) / 3 := by omega
  calc
    4 ^ (n / 4) ≤ 4 ^ (2 * (n / 2) / 3) := Nat.pow_le_pow_right (by omega) hexp
    _ ≤ primorial (2 * (n / 2)) :=
      (four_pow_two_mul_div_three_lt_primorial_two_mul (n / 2) hhalf).le
    _ ≤ primorial n := monotone_primorial (by omega)

/-- Theta is nonnegative. -/
theorem theta_nonneg (n : ℕ) : 0 ≤ theta n := by
  rw [theta_eq_log_primorial]
  exact Real.log_nonneg (by exact_mod_cast primorial_pos n)

/-- Explicit upper Chebyshev bound. -/
theorem theta_le (n : ℕ) : theta n ≤ (n : ℝ) * Real.log 4 := by
  rw [theta_eq_log_primorial, ← Real.log_pow]
  exact Real.strictMonoOn_log.monotoneOn
    (Set.mem_Ioi.mpr (by exact_mod_cast primorial_pos n))
    (Set.mem_Ioi.mpr (by positivity)) (by exact_mod_cast primorial_le_4_pow n)

/-- Explicit lower Chebyshev bound, before removing the floor. -/
theorem theta_lower (n : ℕ) (hn : 1024 ≤ n) :
    ((n / 4 : ℕ) : ℝ) * Real.log 4 ≤ theta n := by
  rw [theta_eq_log_primorial, ← Real.log_pow]
  exact Real.strictMonoOn_log.monotoneOn
    (Set.mem_Ioi.mpr (by positivity))
    (Set.mem_Ioi.mpr (by exact_mod_cast primorial_pos n))
    (by exact_mod_cast four_pow_div_four_le_primorial n hn)

/-- A genuinely linear lower bound, with a slightly weakened constant to absorb the floor. -/
theorem theta_lower_linear (n : ℕ) (hn : 1024 ≤ n) :
    (Real.log 4 / 5) * n ≤ theta n := by
  refine le_trans ?_ (theta_lower n hn)
  have hlog : 0 ≤ Real.log 4 := Real.log_nonneg (by norm_num)
  have hdiv : (n : ℝ) / 5 ≤ (n / 4 : ℕ) := by
    rw [div_le_iff₀ (by norm_num)]
    exact_mod_cast (show n ≤ (n / 4) * 5 by omega)
  nlinarith

/-- Explicit eventual two-sided Chebyshev estimates. -/
theorem theta_two_sided :
    ∀ᶠ n : ℕ in Filter.atTop,
      (Real.log 4 / 5) * n ≤ theta n ∧ theta n ≤ Real.log 4 * n := by
  filter_upwards [Filter.eventually_ge_atTop 1024] with n hn
  exact ⟨theta_lower_linear n hn, by simpa [mul_comm] using theta_le n⟩

/-- Chebyshev's theta function has exactly linear order. -/
theorem theta_isTheta :
    theta =Θ[Filter.atTop] (fun n : ℕ ↦ (n : ℝ)) := by
  apply Asymptotics.IsBigO.antisymm
  · refine Asymptotics.isBigO_iff.mpr ⟨Real.log 4, ?_⟩
    filter_upwards with n
    rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_nonneg (theta_nonneg n),
      abs_of_nonneg (Nat.cast_nonneg n)]
    simpa [mul_comm] using theta_le n
  · refine Asymptotics.isBigO_iff.mpr ⟨5 / Real.log 4, ?_⟩
    filter_upwards [Filter.eventually_ge_atTop 1024] with n hn
    rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_nonneg (Nat.cast_nonneg n),
      abs_of_nonneg (theta_nonneg n)]
    have hlo : 0 < Real.log 4 := Real.log_pos (by norm_num)
    have h := theta_lower_linear n hn
    calc
      (n : ℝ) = (5 / Real.log 4) * ((Real.log 4 / 5) * n) := by
        field_simp
        ring
      _ ≤ (5 / Real.log 4) * theta n := mul_le_mul_of_nonneg_left h (by positivity)

end Erdos415.ChebyshevBinomial
