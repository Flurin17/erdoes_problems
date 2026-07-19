import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.NumberTheory.SmoothNumbers
import Mathlib.NumberTheory.SumPrimeReciprocals

/-!
# The Mertens product input for Erdős 415

This file fixes the precise sequence meant by the Mertens-product input in
`PROOF.md`.  The cutoff `mertensPrimeLog n` includes exactly the primes `p ≤ n`.

Mathlib 4.19 contains the convergence of the harmonic-number sequence to the
Euler--Mascheroni constant, but it does not contain Mertens' product theorem.
The final theorem below isolates the remaining analytic statement as the
convergence to zero of one explicit remainder; both directions of the
reduction are proved.
-/

open Filter Topology

namespace Erdos415.Analytic

/-- The logarithm of the finite Mertens product, with the prime cutoff `p ≤ n`. -/
noncomputable def mertensPrimeLog (n : ℕ) : ℝ :=
  ∑ p ∈ (n + 1).primesBelow, Real.log ((p : ℝ) / (p - 1 : ℕ))

/-- The finite Mertens product whose logarithm is `mertensPrimeLog`. -/
noncomputable def mertensProduct (n : ℕ) : ℝ :=
  ∏ p ∈ (n + 1).primesBelow, (p : ℝ) / (p - 1 : ℕ)

/-- Membership in the finite set used by `mertensPrimeLog` has the advertised
closed-cutoff interpretation. -/
lemma mem_primesBelow_succ_iff {p n : ℕ} :
    p ∈ (n + 1).primesBelow ↔ p.Prime ∧ p ≤ n := by
  rw [Nat.mem_primesBelow]
  constructor
  · rintro ⟨hp, hprime⟩
    exact ⟨hprime, by omega⟩
  · rintro ⟨hprime, hp⟩
    exact ⟨by omega, hprime⟩

lemma log_mertensProduct (n : ℕ) :
    Real.log (mertensProduct n) = mertensPrimeLog n := by
  rw [mertensProduct, mertensPrimeLog, Real.log_prod]
  intro p hp
  have hprime := Nat.prime_of_mem_primesBelow hp
  exact div_ne_zero (by exact_mod_cast hprime.ne_zero)
    (by exact_mod_cast (Nat.sub_ne_zero_of_lt hprime.one_lt))

/-- Each logarithmic Euler factor dominates the corresponding prime
reciprocal. -/
lemma one_div_le_primeLog {p : ℕ} (hp : p.Prime) :
    (1 : ℝ) / p ≤ Real.log ((p : ℝ) / (p - 1 : ℕ)) := by
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp.pos
  have hp1n : 0 < p - 1 := Nat.sub_pos_of_lt hp.one_lt
  have hp1 : (0 : ℝ) < (p - 1 : ℕ) := by exact_mod_cast hp1n
  have hx : 0 < (p : ℝ) / (p - 1 : ℕ) := div_pos hp0 hp1
  convert Real.one_sub_inv_le_log_of_pos hx using 1
  rw [inv_div]
  rw [Nat.cast_sub hp.one_lt.le]
  field_simp

/-- The reciprocal-of-a-prime sequence, extended by zero to all naturals. -/
noncomputable def primeReciprocalIndicator (p : ℕ) : ℝ :=
  Set.indicator {q : ℕ | q.Prime} (fun q ↦ (1 : ℝ) / q) p

lemma primeReciprocalIndicator_nonneg (p : ℕ) : 0 ≤ primeReciprocalIndicator p := by
  simp only [primeReciprocalIndicator, Set.indicator_apply]
  split_ifs <;> positivity

lemma primeReciprocalIndicator_not_summable :
    ¬Summable primeReciprocalIndicator := by
  simpa only [primeReciprocalIndicator] using not_summable_one_div_on_primes

lemma sum_range_primeReciprocalIndicator (n : ℕ) :
    ∑ p ∈ Finset.range (n + 1), primeReciprocalIndicator p =
      ∑ p ∈ (n + 1).primesBelow, (1 : ℝ) / p := by
  rw [Nat.primesBelow]
  simp only [primeReciprocalIndicator, Set.indicator_apply, Set.mem_setOf_eq,
    Finset.sum_filter]

lemma sum_primeReciprocal_le_mertensPrimeLog (n : ℕ) :
    (∑ p ∈ Finset.range (n + 1), primeReciprocalIndicator p) ≤
      mertensPrimeLog n := by
  rw [sum_range_primeReciprocalIndicator]
  exact Finset.sum_le_sum fun p hp ↦
    one_div_le_primeLog (Nat.prime_of_mem_primesBelow hp)

/-- The finite Mertens log sums diverge.  This is the qualitative part needed
to make the prime-packing construction in `PROOF.md` terminate. -/
theorem tendsto_mertensPrimeLog_atTop :
    Tendsto mertensPrimeLog atTop atTop := by
  have hrec :
      Tendsto (fun n : ℕ ↦ ∑ p ∈ Finset.range n, primeReciprocalIndicator p)
        atTop atTop :=
    (not_summable_iff_tendsto_nat_atTop_of_nonneg
      primeReciprocalIndicator_nonneg).mp primeReciprocalIndicator_not_summable
  have hrec' := hrec.comp (tendsto_add_atTop_nat 1)
  exact tendsto_atTop_mono sum_primeReciprocal_le_mertensPrimeLog hrec'

/-- The exact Mertens product/log-weight assertion used in `PROOF.md`. -/
def MertensProductLog : Prop :=
  Tendsto (fun n : ℕ ↦ mertensPrimeLog n - Real.log (Real.log n)) atTop
    (𝓝 Real.eulerMascheroniConstant)

/-- Difference between the Mertens sequence and the harmonic-number sequence.
The convergence of this remainder to zero is the only missing analytic lemma
once `Real.tendsto_harmonic_sub_log` is available. -/
noncomputable def mertensHarmonicRemainder (n : ℕ) : ℝ :=
  (mertensPrimeLog n - Real.log (Real.log n)) -
    ((harmonic n : ℝ) - Real.log n)

/-- Exact reduction of the required Mertens theorem to the explicit remainder
above.  No asymptotic information is discarded in this equivalence. -/
theorem mertensProductLog_iff_remainder :
    MertensProductLog ↔
      Tendsto mertensHarmonicRemainder atTop (𝓝 0) := by
  unfold MertensProductLog mertensHarmonicRemainder
  constructor
  · intro h
    simpa using h.sub Real.tendsto_harmonic_sub_log
  · intro h
    simpa using h.add Real.tendsto_harmonic_sub_log

end Erdos415.Analytic
