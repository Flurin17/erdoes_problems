import Mathlib

/-!
# Exact finite normalization for Erdős Problem 415

A pattern of length `k` is represented by a permutation `π : Equiv.Perm (Fin k)`.
The value `π r` is the zero-based position occupied by rank `r`.  Thus the
pattern occurs at shift `m` precisely when

`totient (m + π 0 + 1) < ⋯ < totient (m + π (k - 1) + 1)`.

The strict inequality is intentional: a block containing a tie realizes no
pattern.  `OccursBy n π` restricts the entire block to the positive integers
at most `n`, and `F n` is the bounded greatest length for which every pattern
has occurred.
-/

namespace Erdos415

/-- A rank-to-position permutation for a block of length `k`. -/
abbrev Pattern (k : ℕ) := Equiv.Perm (Fin k)

/-- The totient value at zero-based position `i` in the block beginning at `m + 1`. -/
def blockValue {k : ℕ} (m : ℕ) (i : Fin k) : ℕ :=
  Nat.totient (m + i.1 + 1)

/-- The strict pattern `π` occurs in the block `m + 1, …, m + k`. -/
def OccursAt {k : ℕ} (π : Pattern k) (m : ℕ) : Prop :=
  StrictMono fun r : Fin k ↦ blockValue m (π r)

instance occursAtDecidable {k : ℕ} (π : Pattern k) (m : ℕ) :
    Decidable (OccursAt π m) := by
  unfold OccursAt
  infer_instance

/-- The pattern occurs in a block wholly contained in `{1, …, n}`. -/
def OccursBy (n : ℕ) {k : ℕ} (π : Pattern k) : Prop :=
  ∃ m ∈ Finset.range (n + 1), m + k ≤ n ∧ OccursAt π m

instance occursByDecidable (n : ℕ) {k : ℕ} (π : Pattern k) :
    Decidable (OccursBy n π) := by
  unfold OccursBy
  infer_instance

/-- Every strict pattern of length `k` occurs by endpoint `n`. -/
def AllPatterns (n k : ℕ) : Prop :=
  ∀ π : Pattern k, OccursBy n π

instance allPatternsDecidable (n k : ℕ) : Decidable (AllPatterns n k) := by
  unfold AllPatterns
  infer_instance

/-- The greatest `k ≤ n` for which every strict length-`k` pattern occurs by `n`. -/
def F (n : ℕ) : ℕ :=
  Nat.findGreatest (AllPatterns n) n

/-- The first endpoint realizing `π`, or `⊤` when `π` never occurs. -/
noncomputable def firstEndpoint {k : ℕ} (π : Pattern k) : WithTop ℕ :=
  by
    classical
    exact if h : ∃ m : ℕ, OccursAt π m then
      ((Nat.find h + k : ℕ) : WithTop ℕ)
    else
      ⊤

/-- The latest first endpoint among all length-`k` patterns.

This is `⊤` exactly when at least one pattern never occurs.
-/
noncomputable def maxFirstEndpoint (k : ℕ) : WithTop ℕ :=
  Finset.univ.sup fun π : Pattern k ↦ firstEndpoint π

@[simp] theorem blockValue_apply {k : ℕ} (m : ℕ) (i : Fin k) :
    blockValue m i = Nat.totient (m + i.1 + 1) :=
  rfl

theorem occursAt_iff {k : ℕ} (π : Pattern k) (m : ℕ) :
    OccursAt π m ↔
      ∀ r s : Fin k, r < s →
        Nat.totient (m + (π r).1 + 1) < Nat.totient (m + (π s).1 + 1) := by
  rfl

/-- A tie between two positions ordered by the pattern prevents occurrence. -/
theorem not_occursAt_of_tie {k : ℕ} {π : Pattern k} {m : ℕ} {r s : Fin k}
    (hrs : r < s) (htie : blockValue m (π r) = blockValue m (π s)) :
    ¬ OccursAt π m := by
  intro h
  exact (ne_of_lt (h hrs)) htie

theorem occursBy_iff {n k : ℕ} {π : Pattern k} :
    OccursBy n π ↔ ∃ m : ℕ, m + k ≤ n ∧ OccursAt π m := by
  constructor
  · rintro ⟨m, -, hmk, hm⟩
    exact ⟨m, hmk, hm⟩
  · rintro ⟨m, hmk, hm⟩
    refine ⟨m, Finset.mem_range.2 ?_, hmk, hm⟩
    omega

theorem occursBy_mono {m n k : ℕ} (hmn : m ≤ n) {π : Pattern k}
    (h : OccursBy m π) : OccursBy n π := by
  rw [occursBy_iff] at h ⊢
  obtain ⟨a, hak, ha⟩ := h
  exact ⟨a, hak.trans hmn, ha⟩

theorem not_occursBy_of_endpoint_lt_length {n k : ℕ} (hnk : n < k)
    (π : Pattern k) : ¬ OccursBy n π := by
  rw [occursBy_iff]
  rintro ⟨m, hmk, -⟩
  omega

theorem allPatterns_mono {m n k : ℕ} (hmn : m ≤ n)
    (h : AllPatterns m k) : AllPatterns n k := by
  intro π
  exact occursBy_mono hmn (h π)

@[simp] theorem allPatterns_zero (n : ℕ) : AllPatterns n 0 := by
  intro π
  rw [occursBy_iff]
  refine ⟨0, by simp, ?_⟩
  intro r
  exact Fin.elim0 r

theorem allPatterns_length_le {n k : ℕ} (h : AllPatterns n k) : k ≤ n := by
  have hi := h (Equiv.refl (Fin k))
  rw [occursBy_iff] at hi
  obtain ⟨m, hmk, -⟩ := hi
  omega

theorem not_allPatterns_of_endpoint_lt_length {n k : ℕ} (hnk : n < k) :
    ¬ AllPatterns n k := by
  intro h
  exact (Nat.not_le_of_lt hnk) (allPatterns_length_le h)

@[simp] theorem F_zero : F 0 = 0 :=
  rfl

theorem F_le (n : ℕ) : F n ≤ n := by
  exact Nat.findGreatest_le n

theorem allPatterns_F (n : ℕ) : AllPatterns n (F n) := by
  exact Nat.findGreatest_spec (m := 0) (Nat.zero_le n) (allPatterns_zero n)

theorem le_F_of_allPatterns {n k : ℕ} (h : AllPatterns n k) : k ≤ F n := by
  exact Nat.le_findGreatest (allPatterns_length_le h) h

theorem F_eq_of_allPatterns_at_bound {n : ℕ} (h : AllPatterns n n) : F n = n := by
  exact Nat.findGreatest_eq h

theorem F_mono {m n : ℕ} (hmn : m ≤ n) : F m ≤ F n := by
  exact Nat.findGreatest_mono (fun _ h ↦ allPatterns_mono hmn h) hmn

theorem F_eq_iff {n k : ℕ} :
    F n = k ↔
      k ≤ n ∧ (k ≠ 0 → AllPatterns n k) ∧
        ∀ j, k < j → j ≤ n → ¬ AllPatterns n j := by
  exact Nat.findGreatest_eq_iff

theorem firstEndpoint_eq_of_exists {k : ℕ} (π : Pattern k)
    (h : ∃ m : ℕ, OccursAt π m) :
    firstEndpoint π = ((Nat.find h + k : ℕ) : WithTop ℕ) := by
  simp [firstEndpoint, h]

@[simp] theorem firstEndpoint_eq_top_iff {k : ℕ} (π : Pattern k) :
    firstEndpoint π = ⊤ ↔ ¬ ∃ m : ℕ, OccursAt π m := by
  classical
  simp [firstEndpoint]

theorem firstEndpoint_lt_top_iff {k : ℕ} (π : Pattern k) :
    firstEndpoint π < ⊤ ↔ ∃ m : ℕ, OccursAt π m := by
  classical
  by_cases h : ∃ m : ℕ, OccursAt π m
  · rw [firstEndpoint_eq_of_exists π h]
    simp [h]
  · simp [firstEndpoint, h]

theorem firstEndpoint_le_coe_iff {n k : ℕ} (π : Pattern k) :
    firstEndpoint π ≤ (n : WithTop ℕ) ↔ OccursBy n π := by
  classical
  by_cases h : ∃ m : ℕ, OccursAt π m
  · rw [firstEndpoint_eq_of_exists π h, occursBy_iff]
    constructor
    · intro hend
      have hend' : Nat.find h + k ≤ n := by
        exact_mod_cast hend
      exact ⟨Nat.find h, hend', Nat.find_spec h⟩
    · rintro ⟨m, hm, hom⟩
      have hend : Nat.find h + k ≤ n :=
        (Nat.add_le_add_right (Nat.find_min' h hom) k).trans hm
      exact_mod_cast hend
  · constructor
    · intro hle
      rw [show firstEndpoint π = ⊤ by simp [firstEndpoint, h]] at hle
      simp at hle
    · intro hocc
      obtain ⟨m, -, hom⟩ := occursBy_iff.1 hocc
      exact (h ⟨m, hom⟩).elim

theorem maxFirstEndpoint_le_coe_iff {n k : ℕ} :
    maxFirstEndpoint k ≤ (n : WithTop ℕ) ↔ AllPatterns n k := by
  classical
  rw [maxFirstEndpoint, Finset.sup_le_iff]
  constructor
  · intro h π
    exact (firstEndpoint_le_coe_iff π).1 (h π (Finset.mem_univ π))
  · intro h π _
    exact (firstEndpoint_le_coe_iff π).2 (h π)

@[simp] theorem maxFirstEndpoint_eq_top_iff (k : ℕ) :
    maxFirstEndpoint k = ⊤ ↔ ∃ π : Pattern k, ¬ ∃ m : ℕ, OccursAt π m := by
  classical
  rw [maxFirstEndpoint, Finset.sup_eq_top_iff]
  simp

end Erdos415
