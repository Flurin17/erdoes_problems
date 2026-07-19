import Mathlib.Analysis.Normed.Group.Tannery
import Mathlib.Analysis.PSeries
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Nat.Totient
import Mathlib.NumberTheory.SumPrimeReciprocals

/-!
# The totient loss and its mean

This file isolates the elementary analytic identity used in the solution of
Erdős problem 415.  All sums over primes use the subtype `Nat.Primes`.
-/

noncomputable section

open Filter Finset Nat Real Set Topology
open scoped BigOperators

namespace Erdos415

/-- The contribution of a prime `p` to `log (n / φ(n))`. -/
def primeWeight (p : ℕ) : ℝ :=
  Real.log ((p : ℝ) / (p - 1 : ℕ))

/-- The logarithmic loss of Euler's totient function. -/
def loss (n : ℕ) : ℝ :=
  Real.log ((n : ℝ) / n.totient)

/-- The summand defining the mean totient-loss constant. -/
def meanTerm (p : Nat.Primes) : ℝ :=
  primeWeight p / (p : ℝ)

/-- The mean totient-loss constant. -/
def meanLoss : ℝ :=
  ∑' p : Nat.Primes, meanTerm p

lemma primeWeight_nonneg {p : ℕ} (hp : p.Prime) : 0 ≤ primeWeight p := by
  have hpR : 0 < (p : ℝ) := by exact_mod_cast hp.pos
  have hden : 0 < (((p - 1 : ℕ) : ℝ)) := by
    exact_mod_cast Nat.sub_pos_of_lt hp.one_lt
  rw [primeWeight, Real.log_nonneg_iff (div_pos hpR hden), one_le_div hden]
  exact_mod_cast Nat.sub_le p 1

lemma primeWeight_pos {p : ℕ} (hp : p.Prime) : 0 < primeWeight p := by
  have hpR : 0 < (p : ℝ) := by exact_mod_cast hp.pos
  have hden : 0 < (((p - 1 : ℕ) : ℝ)) := by
    exact_mod_cast Nat.sub_pos_of_lt hp.one_lt
  rw [primeWeight, Real.log_pos_iff (div_pos hpR hden).le, one_lt_div hden]
  exact_mod_cast Nat.sub_lt hp.pos Nat.zero_lt_one

/-- A convenient quadratic majorant for the summand defining `meanLoss`. -/
lemma meanTerm_le_two_div_sq (p : Nat.Primes) :
    meanTerm p ≤ 2 / (p : ℝ) ^ 2 := by
  have hp2 : 2 ≤ (p : ℕ) := p.prop.two_le
  have hpR : 0 < (p : ℝ) := by exact_mod_cast p.prop.pos
  have hp1R : 0 < ((p : ℕ) - 1 : ℕ) := Nat.sub_pos_of_lt p.prop.one_lt
  have hp1cast : (((p : ℕ) - 1 : ℕ) : ℝ) = (p : ℝ) - 1 := by
    rw [Nat.cast_sub (by omega)]
    norm_num
  have hp1R' : 0 < (p : ℝ) - 1 := by
    rw [← hp1cast]
    exact_mod_cast hp1R
  have hlog : primeWeight p ≤ 1 / ((p : ℝ) - 1) := by
    rw [primeWeight, hp1cast]
    calc
      Real.log ((p : ℝ) / ((p : ℝ) - 1))
          ≤ (p : ℝ) / ((p : ℝ) - 1) - 1 :=
            Real.log_le_sub_one_of_pos (div_pos hpR hp1R')
      _ = 1 / ((p : ℝ) - 1) := by field_simp
  rw [meanTerm]
  apply (div_le_div_of_nonneg_right hlog hpR.le).trans
  rw [div_div]
  have hp2R : (2 : ℝ) ≤ (p : ℝ) := by exact_mod_cast hp2
  have hpHalf : (p : ℝ) / 2 ≤ (p : ℝ) - 1 := by linarith
  have hden : 0 < ((p : ℝ) - 1) * (p : ℝ) := mul_pos hp1R' hpR
  have hsq : 0 < (p : ℝ) ^ 2 := sq_pos_of_pos hpR
  rw [div_le_div_iff₀ hden hsq]
  nlinarith

lemma meanTerm_nonneg (p : Nat.Primes) : 0 ≤ meanTerm p := by
  exact div_nonneg (primeWeight_nonneg p.prop) (by positivity)

/-- Absolute convergence of the prime sum defining `meanLoss`. -/
theorem summable_meanTerm : Summable meanTerm := by
  have hsNat : Summable (fun n : ℕ ↦ 2 / (n : ℝ) ^ 2) := by
    simpa [div_eq_mul_inv] using
      (Real.summable_one_div_nat_pow.mpr (by norm_num : 1 < (2 : ℕ))).mul_left 2
  have hsPrime : Summable (fun p : Nat.Primes ↦ 2 / (p : ℝ) ^ 2) :=
    hsNat.subtype _
  exact hsPrime.of_nonneg_of_le meanTerm_nonneg meanTerm_le_two_div_sq

/-- Euler's product formula, expressed additively after taking logarithms. -/
theorem loss_eq_sum_primeFactors {n : ℕ} (hn : n ≠ 0) :
    loss n = ∑ p ∈ n.primeFactors, primeWeight p := by
  have hphi : 0 < n.totient := Nat.totient_pos.mpr (Nat.pos_of_ne_zero hn)
  have hprodP : 0 < ∏ p ∈ n.primeFactors, (p : ℝ) := by
    apply Finset.prod_pos
    intro p hp
    exact_mod_cast (Nat.prime_of_mem_primeFactors hp).pos
  have hprodPred : 0 < ∏ p ∈ n.primeFactors, (((p - 1 : ℕ) : ℝ)) := by
    apply Finset.prod_pos
    intro p hp
    exact_mod_cast Nat.sub_pos_of_lt (Nat.prime_of_mem_primeFactors hp).one_lt
  have heq :
      (n.totient : ℝ) * ∏ p ∈ n.primeFactors, (p : ℝ) =
        (n : ℝ) * ∏ p ∈ n.primeFactors, (((p - 1 : ℕ) : ℝ)) := by
    simpa only [Nat.cast_mul, Nat.cast_prod] using
      congrArg (fun m : ℕ ↦ (m : ℝ)) (Nat.totient_mul_prod_primeFactors n)
  have hratio :
      (n : ℝ) / n.totient =
        ∏ p ∈ n.primeFactors, ((p : ℝ) / ((p - 1 : ℕ) : ℝ)) := by
    rw [Finset.prod_div_distrib]
    apply (div_eq_div_iff (Nat.cast_ne_zero.mpr hphi.ne') hprodPred.ne').2
    simpa [mul_comm] using heq.symm
  rw [loss, hratio, Real.log_prod]
  · rfl
  · intro p hp
    have hprime := Nat.prime_of_mem_primeFactors hp
    exact div_ne_zero (Nat.cast_ne_zero.mpr hprime.ne_zero)
      (Nat.cast_ne_zero.mpr (Nat.sub_pos_of_lt hprime.one_lt).ne')

private lemma primeFactors_eq_filter_primesBelow_succ {i k : ℕ}
    (hi : 0 < i) (hik : i ≤ k) :
    i.primeFactors = k.succ.primesBelow.filter fun p ↦ p ∣ i := by
  ext p
  simp only [Nat.mem_primeFactors_of_ne_zero hi.ne', Finset.mem_filter,
    Nat.mem_primesBelow]
  constructor
  · rintro ⟨hp, hdvd⟩
    exact ⟨⟨Nat.lt_succ_of_le ((Nat.le_of_dvd hi hdvd).trans hik), hp⟩, hdvd⟩
  · rintro ⟨⟨_, hp⟩, hdvd⟩
    exact ⟨hp, hdvd⟩

/-- Exact double counting of prime divisors in the first `k` positive integers. -/
theorem sum_loss_eq_sum_div_primeWeight (k : ℕ) :
    ∑ i ∈ Finset.Ioc 0 k, loss i =
      ∑ p ∈ k.succ.primesBelow, ((k / p : ℕ) : ℝ) * primeWeight p := by
  calc
    ∑ i ∈ Finset.Ioc 0 k, loss i =
        ∑ i ∈ Finset.Ioc 0 k, ∑ p ∈ i.primeFactors, primeWeight p := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [loss_eq_sum_primeFactors]
      exact (Finset.mem_Ioc.mp hi).1.ne'
    _ = ∑ i ∈ Finset.Ioc 0 k, ∑ p ∈ k.succ.primesBelow,
          if p ∣ i then primeWeight p else 0 := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [← Finset.sum_filter]
      congr 1
      exact primeFactors_eq_filter_primesBelow_succ
        (Finset.mem_Ioc.mp hi).1 (Finset.mem_Ioc.mp hi).2
    _ = ∑ p ∈ k.succ.primesBelow, ∑ i ∈ Finset.Ioc 0 k,
          if p ∣ i then primeWeight p else 0 := by
      rw [Finset.sum_comm]
    _ = ∑ p ∈ k.succ.primesBelow, ((k / p : ℕ) : ℝ) * primeWeight p := by
      apply Finset.sum_congr rfl
      intro p hp
      rw [← Finset.sum_filter]
      simp [Nat.Ioc_filter_dvd_card_eq_div]

/-- For fixed positive `p`, the normalized count of multiples of `p` tends to `1 / p`. -/
lemma tendsto_cast_natDiv_div (p : ℕ) (hp : 0 < p) :
    Tendsto (fun k : ℕ ↦ ((k / p : ℕ) : ℝ) / (k : ℝ)) atTop
      (𝓝 (1 / (p : ℝ))) := by
  have hpR : 0 < (p : ℝ) := by exact_mod_cast hp
  have hconst : Tendsto (fun _ : ℕ ↦ 1 / (p : ℝ)) atTop (𝓝 (1 / (p : ℝ))) :=
    tendsto_const_nhds
  have hmodp :
      Tendsto (fun k : ℕ ↦ (((k % p : ℕ) : ℝ) / (k : ℝ)) / (p : ℝ)) atTop (𝓝 0) := by
    simpa using (tendsto_mod_div_atTop_nhds_zero_nat hp).div_const (p : ℝ)
  have hlim := hconst.sub hmodp
  have heq :
      (fun k : ℕ ↦ ((k / p : ℕ) : ℝ) / (k : ℝ)) =ᶠ[atTop]
        fun k : ℕ ↦ 1 / (p : ℝ) - (((k % p : ℕ) : ℝ) / (k : ℝ)) / (p : ℝ) := by
    filter_upwards [eventually_gt_atTop (0 : ℕ)] with k hk
    have hkR : 0 < (k : ℝ) := by exact_mod_cast hk
    have hdecomp :
        (((k / p : ℕ) : ℝ) * (p : ℝ) + ((k % p : ℕ) : ℝ)) = (k : ℝ) := by
      exact_mod_cast Nat.div_add_mod' k p
    have hquot :
        ((k / p : ℕ) : ℝ) * (p : ℝ) = (k : ℝ) - ((k % p : ℕ) : ℝ) := by
      linarith
    field_simp [hkR.ne', hpR.ne']
    calc
      ((k / p : ℕ) : ℝ) * ((k : ℝ) * (p : ℝ)) =
          (((k / p : ℕ) : ℝ) * (p : ℝ)) * (k : ℝ) := by ring
      _ = ((k : ℝ) - ((k % p : ℕ) : ℝ)) * (k : ℝ) := by rw [hquot]
  have hlim' :
      Tendsto
        (fun k : ℕ ↦ 1 / (p : ℝ) - (((k % p : ℕ) : ℝ) / (k : ℝ)) / (p : ℝ))
        atTop (𝓝 (1 / (p : ℝ))) := by
    simpa using hlim
  exact hlim'.congr' heq.symm

end Erdos415
