import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Nat.ChineseRemainder
import Mathlib.Data.Nat.Totient

/-!
# Exact CRT and ordering core for Erdős Problem 415

This module isolates the finite, exact part of the block construction.  It
contains no asymptotic input.  The first group of lemmas constructs a Chinese
remainder representative in the half-open interval `[Q, 2Q)`.  The second
group records exactly which shifts can be divisible by a prescribed modulus.
The final group turns a quantitative decomposition of Euler-totient loss into
a strict ordering of totients.
-/

open scoped BigOperators Function

namespace Erdos415.CRTCore

/-- Distinct primes in a finite set are pairwise coprime. -/
theorem prime_moduli_pairwise_coprime (S : Finset ℕ)
    (hprime : ∀ p ∈ S, Nat.Prime p) :
    Set.Pairwise (S : Set ℕ) Nat.Coprime := by
  intro p hp q hq hpq
  exact (Nat.coprime_primes (hprime p hp) (hprime q hq)).2 hpq

/--
For arbitrary residues at finitely many distinct primes, let `Q` be the
product of the primes.  There is a simultaneous CRT representative `m` in
`[Q, 2Q)`.  Choosing this shifted representative (rather than the least
nonnegative one) is what later makes the block size comparable with `Q`.
-/
theorem exists_crt_representative_in_product_interval
    (S : Finset ℕ) (residue : ℕ → ℕ)
    (hprime : ∀ p ∈ S, Nat.Prime p) :
    let Q := ∏ p ∈ S, p
    ∃ m : ℕ, Q ≤ m ∧ m < 2 * Q ∧
      ∀ p ∈ S, m ≡ residue p [MOD p] := by
  dsimp only
  let Q := ∏ p ∈ S, p
  have hpair : Set.Pairwise (S : Set ℕ) Nat.Coprime :=
    prime_moduli_pairwise_coprime S hprime
  have hnonzero : ∀ p ∈ S, (fun q : ℕ => q) p ≠ 0 := by
    intro p hp
    exact (hprime p hp).ne_zero
  let z := Nat.chineseRemainderOfFinset residue (fun p : ℕ => p) S hnonzero hpair
  have hz_lt : (z : ℕ) < Q := by
    simpa [Q] using
      Nat.chineseRemainderOfFinset_lt_prod (t := S) residue (fun p : ℕ => p)
        hnonzero hpair
  have hQ_pos : 0 < Q := by
    dsimp [Q]
    exact Finset.prod_pos fun p hp => (hprime p hp).pos
  refine ⟨Q + z, Nat.le_add_right Q z, ?_, ?_⟩
  · omega
  · intro p hp
    have hpQ : p ∣ Q := by
      dsimp [Q]
      exact Finset.dvd_prod_of_mem (fun q : ℕ => q) hp
    have hQz : Q + (z : ℕ) ≡ z [MOD p] := by
      have hzrefl : (z : ℕ) ≡ z [MOD p] := Nat.ModEq.refl _
      simpa using hpQ.modEq_zero_nat.add hzrefl
    exact hQz.trans (z.property p hp)

/-- A prescribed residue whose shifted value is zero makes the corresponding
modulus divide that shift. -/
theorem prescribed_residue_divides_shift {p m a i : ℕ}
    (hm : m ≡ a [MOD p]) (ha : a + i ≡ 0 [MOD p]) : p ∣ m + i := by
  exact Nat.modEq_zero_iff_dvd.mp ((hm.add Nat.ModEq.rfl).trans ha)

/-- If `m` is zero modulo `p`, divisibility inside the translated block is
exactly the baseline divisibility of the shift index. -/
theorem zero_residue_baseline {p m i : ℕ} (hm : m ≡ 0 [MOD p]) :
    p ∣ m + i ↔ p ∣ i := by
  have hmi : m + i ≡ i [MOD p] := by
    simpa using hm.add (Nat.ModEq.rfl : i ≡ i [MOD p])
  exact hmi.dvd_iff (dvd_refl p)

/-- A modulus larger than the block length can divide at most one positive
shift in that block.  Primality is not needed for this fact. -/
theorem large_modulus_dvd_at_most_one_shift {p k m i j : ℕ}
    (hik : i ≤ k) (hjk : j ≤ k) (hkp : k < p)
    (hi : p ∣ m + i) (hj : p ∣ m + j) : i = j := by
  have hsum : m + i ≡ m + j [MOD p] :=
    hi.modEq_zero_nat.trans hj.modEq_zero_nat.symm
  have hij : i ≡ j [MOD p] := Nat.ModEq.add_left_cancel' m hsum
  exact hij.eq_of_lt_of_lt (lt_of_le_of_lt hik hkp) (lt_of_le_of_lt hjk hkp)

/-- Once a large modulus is designated to divide one shift, it divides no
other shift in the block. -/
theorem designated_large_modulus_divides_exactly_one_shift
    {p k m i : ℕ} (hi : i ≤ k) (hkp : k < p) (hdesignated : p ∣ m + i) :
    ∀ {j : ℕ}, j ≤ k → (p ∣ m + j ↔ j = i) := by
  intro j hj
  constructor
  · intro hjdvd
    exact large_modulus_dvd_at_most_one_shift hj hi hkp hjdvd hdesignated
  · rintro rfl
    exact hdesignated

/-- An unassigned modulus, represented by the zero residue, misses every
positive shift when it is larger than the block length. -/
theorem zero_residue_large_modulus_misses_block {p k m i : ℕ}
    (hm : m ≡ 0 [MOD p]) (hi : 0 < i) (hik : i ≤ k) (hkp : k < p) :
    ¬p ∣ m + i := by
  rw [zero_residue_baseline hm]
  intro hpi
  exact (not_le_of_gt (lt_of_le_of_lt hik hkp)) (Nat.le_of_dvd hi hpi)

/--
Combined behavior of an unassigned prime through a cutoff `y`: at the small
primes it contributes precisely the baseline divisibility pattern, while an
unassigned prime larger than `k` misses every positive shift of the block.
-/
theorem unassigned_prime_through_cutoff {p y k m : ℕ}
    (_hp_le_y : p ≤ y) (hm : m ≡ 0 [MOD p]) :
    (∀ i, p ∣ m + i ↔ p ∣ i) ∧
      (k < p → ∀ i, 0 < i → i ≤ k → ¬p ∣ m + i) := by
  constructor
  · intro i
    exact zero_residue_baseline hm
  · intro hkp i hi hik
    exact zero_residue_large_modulus_misses_block hm hi hik hkp

/-- The exact logarithmic loss attached to Euler's totient. -/
noncomputable def totientLoss (n : ℕ) : ℝ :=
  Real.log (n : ℝ) - Real.log (Nat.totient n : ℝ)

/-- A loss gap larger than the logarithmic shift ratio forces the desired
strict totient comparison. -/
theorem totient_lt_of_loss_gap {a b : ℕ} (ha : 0 < a) (hb : 0 < b)
    (hgap : Real.log (a : ℝ) - Real.log (b : ℝ) <
      totientLoss a - totientLoss b) :
    Nat.totient a < Nat.totient b := by
  have hφa : 0 < Nat.totient a := Nat.totient_pos.mpr ha
  have hφb : 0 < Nat.totient b := Nat.totient_pos.mpr hb
  have hφaR : (0 : ℝ) < Nat.totient a := by exact_mod_cast hφa
  have hφbR : (0 : ℝ) < Nat.totient b := by exact_mod_cast hφb
  have hlog : Real.log (Nat.totient a : ℝ) <
      Real.log (Nat.totient b : ℝ) := by
    dsimp [totientLoss] at hgap
    linarith
  have hcast : (Nat.totient a : ℝ) < Nat.totient b :=
    (Real.log_lt_log_iff hφaR hφbR).mp hlog
  exact_mod_cast hcast

/--
Quantitative error-budget lemma used by the CRT construction.  Write the
actual loss at each endpoint as `controlled + extra`.  The earlier endpoint
may have any nonnegative extra loss; the later endpoint has extra loss at
most `tail`.  If the controlled gap pays for both `tail` and a bound `shift`
on the logarithmic change of the arguments, then the totients are strictly
ordered.
-/
theorem controlled_errors_force_totient_order
    {a b : ℕ} {controlledA controlledB extraA extraB tail shift : ℝ}
    (ha : 0 < a) (hb : 0 < b)
    (hlossA : totientLoss a = controlledA + extraA)
    (hlossB : totientLoss b = controlledB + extraB)
    (hextraA : 0 ≤ extraA) (hextraB : extraB ≤ tail)
    (hbudget : tail + shift ≤ controlledA - controlledB)
    (hshift : |Real.log (a : ℝ) - Real.log (b : ℝ)| < shift) :
    Nat.totient a < Nat.totient b := by
  apply totient_lt_of_loss_gap ha hb
  have hlog : Real.log (a : ℝ) - Real.log (b : ℝ) < shift :=
    lt_of_le_of_lt (le_abs_self _) hshift
  rw [hlossA, hlossB]
  linarith

/-- Pointwise controlled-gap estimates imply a strict ordering for an entire
ranked family of block entries. -/
theorem strictMono_totient_of_controlled_gaps
    {ι : Type*} [Preorder ι]
    (entry : ι → ℕ) (controlled extra : ι → ℝ) (tail shift : ℝ)
    (hentry : ∀ i, 0 < entry i)
    (hloss : ∀ i, totientLoss (entry i) = controlled i + extra i)
    (hextra_nonneg : ∀ i, 0 ≤ extra i)
    (hextra_le : ∀ i, extra i ≤ tail)
    (hgap : ∀ ⦃i j⦄, i < j → tail + shift ≤ controlled i - controlled j)
    (hshift : ∀ ⦃i j⦄, i < j →
      |Real.log (entry i : ℝ) - Real.log (entry j : ℝ)| < shift) :
    StrictMono (fun i => Nat.totient (entry i)) := by
  intro i j hij
  exact controlled_errors_force_totient_order
    (hentry i) (hentry j) (hloss i) (hloss j)
    (hextra_nonneg i) (hextra_le j) (hgap hij) (hshift hij)

end Erdos415.CRTCore
