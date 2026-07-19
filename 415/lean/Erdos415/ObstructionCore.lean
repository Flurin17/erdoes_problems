import Mathlib

/-!
# Finite obstruction lemmas for Erdős Problem 415

This file formalizes the elementary, non-asymptotic core of Part III of the
paper proof.  A block of length `k` is indexed by `i < k`, and its `i`th term
is `m + i + 1`.
-/

namespace Erdos415.ObstructionCore

open scoped BigOperators
open Finset

/-- The logarithmic loss `log (n / φ(n))`, written in a form convenient for
order arguments. -/
noncomputable def totientLoss (n : ℕ) : ℝ :=
  Real.log n - Real.log n.totient

/-- If two positive arguments increase while their raw totients decrease,
then their logarithmic losses strictly increase. -/
theorem totientLoss_lt_of_lt_of_totient_gt {a b : ℕ} (ha : 0 < a)
    (hab : a < b) (hφ : b.totient < a.totient) :
    totientLoss a < totientLoss b := by
  have hφa : 0 < a.totient := Nat.totient_pos.mpr ha
  have hb : 0 < b := ha.trans hab
  have hφb : 0 < b.totient := Nat.totient_pos.mpr hb
  have hlog_ab : Real.log (a : ℝ) < Real.log (b : ℝ) := by
    exact Real.strictMonoOn_log (Set.mem_Ioi.mpr (by exact_mod_cast ha))
      (Set.mem_Ioi.mpr (by exact_mod_cast ha.trans hab)) (by exact_mod_cast hab)
  have hlog_φ : Real.log (b.totient : ℝ) < Real.log (a.totient : ℝ) := by
    exact Real.strictMonoOn_log
      (Set.mem_Ioi.mpr (by exact_mod_cast hφb))
      (Set.mem_Ioi.mpr (by exact_mod_cast hφa)) (by exact_mod_cast hφ)
  unfold totientLoss
  linarith

/-- A strictly decreasing block of raw totients has a strictly increasing
loss sequence. -/
theorem totientLoss_strictMono_of_totient_strictAnti {m k : ℕ}
    (hφ : StrictAnti fun i : Fin k => Nat.totient (m + i.1 + 1)) :
    StrictMono fun i : Fin k => totientLoss (m + i.1 + 1) := by
  intro i j hij
  apply totientLoss_lt_of_lt_of_totient_gt (by omega)
  · omega
  · exact hφ hij

/-- Every `R` consecutive positive shifts `m+1, ..., m+R` contain a
multiple of `R`. -/
theorem exists_dvd_in_consecutive_block (m R : ℕ) (hR : 0 < R) :
    ∃ j, 1 ≤ j ∧ j ≤ R ∧ R ∣ m + j := by
  let j := R - m % R
  have hmod : m % R < R := Nat.mod_lt _ hR
  have hjpos : 1 ≤ j := by
    dsimp [j]
    omega
  have hjR : j ≤ R := Nat.sub_le _ _
  refine ⟨j, hjpos, hjR, ?_⟩
  refine ⟨m / R + 1, ?_⟩
  have hremle : m % R ≤ m := Nat.mod_le _ _
  have hquot : m - m % R = R * (m / R) := by
    rw [Nat.sub_eq_iff_eq_add hremle]
    simpa [Nat.add_comm] using (Nat.mod_add_div m R).symm
  calc
    m + j = (m - m % R) + R := by dsimp [j]; omega
    _ = R * (m / R) + R := by rw [hquot]
    _ = R * (m / R + 1) := by simp [Nat.mul_add, Nat.mul_comm]

/-- A modulus larger than the block length cannot divide two different
members of that block.  Primality is not needed for this spacing fact. -/
theorem divisor_gt_length_private {m k p i j : ℕ} (hkp : k < p)
    (hi : i < k) (hj : j < k) (hpi : p ∣ m + i + 1)
    (hpj : p ∣ m + j + 1) : i = j := by
  have hc : m + i + 1 ≡ m + j + 1 [MOD p] :=
    hpi.modEq_zero_nat.trans hpj.modEq_zero_nat.symm
  have hij : i ≡ j [MOD p] := by
    have hc' : m + (i + 1) ≡ m + (j + 1) [MOD p] := by simpa [add_assoc] using hc
    have hsucc : i + 1 ≡ j + 1 [MOD p] := hc'.add_left_cancel' m
    exact hsucc.add_right_cancel' 1
  exact hij.eq_of_lt_of_lt (hi.trans hkp) (hj.trans hkp)

/-- In particular, a prime `p > k` divides at most one of the `k` shifts. -/
theorem large_prime_divides_at_most_one {m k p : ℕ} (_hp : p.Prime)
    (hkp : k < p) :
    Set.Subsingleton {i : Fin k | p ∣ m + i.1 + 1} := by
  intro i hi j hj
  exact Fin.ext (divisor_gt_length_private hkp i.2 j.2 hi hj)

/-- Product of the members of the consecutive block. -/
def blockProduct (m k : ℕ) : ℕ :=
  ∏ i ∈ range k, (m + i + 1)

/-- The finite set of all prime divisors larger than the block length that
occur in at least one member of the block. -/
def largePrimeDivisors (m k : ℕ) : Finset ℕ :=
  (range k).biUnion fun i => (m + i + 1).primeFactors.filter (k < ·)

theorem mem_largePrimeDivisors_iff {m k p : ℕ} :
    p ∈ largePrimeDivisors m k ↔
      k < p ∧ p.Prime ∧ ∃ i < k, p ∣ m + i + 1 := by
  simp only [largePrimeDivisors, mem_biUnion, mem_range, mem_filter,
    Nat.mem_primeFactors]
  constructor
  · rintro ⟨i, hi, hpTerm, hkp⟩
    exact ⟨hkp, hpTerm.1, i, hi, hpTerm.2.1⟩
  · rintro ⟨hkp, hp, i, hi, hdiv⟩
    refine ⟨i, hi, ?_, hkp⟩
    exact ⟨hp, hdiv, by omega⟩

/-- The squarefree product of all large prime divisors divides the product of
the block. -/
theorem prod_largePrimeDivisors_dvd_blockProduct (m k : ℕ) :
    (∏ p ∈ largePrimeDivisors m k, p) ∣ blockProduct m k := by
  have hprod0 : blockProduct m k ≠ 0 := by
    unfold blockProduct
    exact Finset.prod_ne_zero_iff.mpr fun i hi => by omega
  have hsubset : largePrimeDivisors m k ⊆ (blockProduct m k).primeFactors := by
    intro p hp
    rw [Nat.mem_primeFactors_of_ne_zero hprod0]
    obtain ⟨_, hpprime, i, hi, hpdiv⟩ := mem_largePrimeDivisors_iff.mp hp
    refine ⟨hpprime, hpdiv.trans ?_⟩
    unfold blockProduct
    exact Finset.dvd_prod_of_mem (fun i => m + i + 1) (mem_range.mpr hi)
  exact (Finset.prod_dvd_prod_of_subset _ _ id hsubset).trans
    (Nat.prod_primeFactors_dvd (blockProduct m k))

/-- The loss weight attached to a prime divisor. -/
noncomputable def primeLossWeight (p : ℕ) : ℝ :=
  Real.log ((p : ℝ) / (p - 1 : ℕ))

theorem primeLossWeight_nonneg {p : ℕ} (hp : p.Prime) :
    0 ≤ primeLossWeight p := by
  apply Real.log_nonneg
  apply (one_le_div (by exact_mod_cast Nat.sub_pos_of_lt hp.one_lt)).mpr
  exact_mod_cast Nat.pred_le p

/-- Number of members of a length-`k` block divisible by `p`. -/
def occurrenceCount (m k p : ℕ) : ℕ :=
  #{i ∈ range k | p ∣ m + i + 1}

/-- Any residue class occurs at most `k / p + 1` times among `k`
consecutive integers. -/
theorem occurrenceCount_le (m k p : ℕ) (hp : 0 < p) :
    occurrenceCount m k p ≤ k / p + 1 := by
  let v := p - ((m + 1) % p)
  have heq :
      {i ∈ range k | p ∣ m + i + 1} =
        {i ∈ range k | i ≡ v [MOD p]} := by
    ext i
    simp only [mem_filter, mem_range, and_congr_right_iff]
    intro _
    rw [← Nat.modEq_zero_iff_dvd]
    constructor
    · intro h
      have hbase : m + 1 + v ≡ 0 [MOD p] := by
        rw [Nat.modEq_zero_iff_dvd]
        refine ⟨(m + 1) / p + 1, ?_⟩
        have hmod : (m + 1) % p < p := Nat.mod_lt _ hp
        have hremle : (m + 1) % p ≤ m + 1 := Nat.mod_le _ _
        have hquot : m + 1 - (m + 1) % p = p * ((m + 1) / p) := by
          rw [Nat.sub_eq_iff_eq_add hremle]
          simpa [Nat.add_comm] using (Nat.mod_add_div (m + 1) p).symm
        calc
          m + 1 + v = (m + 1 - (m + 1) % p) + p := by dsimp [v]; omega
          _ = p * ((m + 1) / p) + p := by rw [hquot]
          _ = p * ((m + 1) / p + 1) := by simp [Nat.mul_add, Nat.mul_comm]
      have hi : i ≡ v [MOD p] := by
        have h' : m + 1 + i ≡ m + 1 + v [MOD p] := by
          simpa [add_assoc, add_left_comm, add_comm] using h.trans hbase.symm
        exact h'.add_left_cancel' (m + 1)
      exact hi
    · intro hi
      have hbase : m + 1 + v ≡ 0 [MOD p] := by
        rw [Nat.modEq_zero_iff_dvd]
        refine ⟨(m + 1) / p + 1, ?_⟩
        have hmod : (m + 1) % p < p := Nat.mod_lt _ hp
        have hremle : (m + 1) % p ≤ m + 1 := Nat.mod_le _ _
        have hquot : m + 1 - (m + 1) % p = p * ((m + 1) / p) := by
          rw [Nat.sub_eq_iff_eq_add hremle]
          simpa [Nat.add_comm] using (Nat.mod_add_div (m + 1) p).symm
        calc
          m + 1 + v = (m + 1 - (m + 1) % p) + p := by dsimp [v]; omega
          _ = p * ((m + 1) / p) + p := by rw [hquot]
          _ = p * ((m + 1) / p + 1) := by simp [Nat.mul_add, Nat.mul_comm]
      have := (hi.add_left (m + 1)).trans hbase
      simpa [add_assoc, add_left_comm, add_comm] using this
  unfold occurrenceCount
  rw [heq, ← Nat.count_eq_card_filter_range, Nat.count_modEq_card k hp]
  split_ifs <;> omega

/-- The primes at most `k`. -/
def smallPrimes (k : ℕ) : Finset ℕ :=
  (range (k + 1)).filter Nat.Prime

theorem mem_smallPrimes_iff {k p : ℕ} :
    p ∈ smallPrimes k ↔ p.Prime ∧ p ≤ k := by
  simp [smallPrimes, Nat.lt_succ_iff, and_comm]

/-- Finite weighted form of the small-prime occurrence estimate used in the
obstruction argument:

`Σ count_p w_p ≤ k Σ (w_p / p) + Σ w_p`.
-/
theorem aggregate_smallPrime_occurrence_bound (m k : ℕ) :
    (∑ p ∈ smallPrimes k,
        (occurrenceCount m k p : ℝ) * primeLossWeight p) ≤
      (k : ℝ) * ∑ p ∈ smallPrimes k, primeLossWeight p / p +
        ∑ p ∈ smallPrimes k, primeLossWeight p := by
  calc
    (∑ p ∈ smallPrimes k,
        (occurrenceCount m k p : ℝ) * primeLossWeight p) ≤
        ∑ p ∈ smallPrimes k,
          ((k : ℝ) / p + 1) * primeLossWeight p := by
      apply sum_le_sum
      intro p hp
      have hpprime := (mem_smallPrimes_iff.mp hp).1
      apply mul_le_mul_of_nonneg_right _ (primeLossWeight_nonneg hpprime)
      have hcount := occurrenceCount_le m k p hpprime.pos
      calc
        (occurrenceCount m k p : ℝ) ≤ (k / p + 1 : ℕ) := by exact_mod_cast hcount
        _ ≤ (k : ℝ) / p + 1 := by
          simpa only [Nat.cast_add, Nat.cast_one] using
            (add_le_add_right (Nat.cast_div_le (α := ℝ)) 1)
    _ = (k : ℝ) * ∑ p ∈ smallPrimes k, primeLossWeight p / p +
          ∑ p ∈ smallPrimes k, primeLossWeight p := by
      simp_rw [add_mul, one_mul, sum_add_distrib, mul_sum]
      congr 1
      apply sum_congr rfl
      intro p hp
      ring

#print axioms totientLoss_lt_of_lt_of_totient_gt
#print axioms totientLoss_strictMono_of_totient_strictAnti
#print axioms exists_dvd_in_consecutive_block
#print axioms large_prime_divides_at_most_one
#print axioms prod_largePrimeDivisors_dvd_blockProduct
#print axioms aggregate_smallPrime_occurrence_bound

end Erdos415.ObstructionCore
