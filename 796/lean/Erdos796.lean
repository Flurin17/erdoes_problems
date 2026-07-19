import Std

namespace Erdos796

/-- A representation counted by Problem #796: the factors are distinct and
stored in increasing order. -/
structure Representation (m : Nat) where
  lo : Nat
  hi : Nat
  positive : 0 < lo
  ordered : lo < hi
  product_eq : lo * hi = m

namespace Representation

theorem lo_pos {m : Nat} (r : Representation m) : 0 < r.lo :=
  r.positive

theorem hi_pos {m : Nat} (r : Representation m) : 0 < r.hi :=
  Nat.lt_trans r.positive r.ordered

theorem eq_of_values {m : Nat} {r s : Representation m}
    (hlo : r.lo = s.lo) (hhi : r.hi = s.hi) : r = s := by
  cases r
  cases s
  simp_all

theorem eq_of_lo_eq {m : Nat} (r s : Representation m)
    (hlo : r.lo = s.lo) : r = s := by
  apply eq_of_values hlo
  apply Nat.mul_left_cancel r.positive
  calc
    r.lo * r.hi = m := r.product_eq
    _ = s.lo * s.hi := s.product_eq.symm
    _ = r.lo * s.hi := by rw [← hlo]

theorem eq_of_hi_eq {m : Nat} (r s : Representation m)
    (hhi : r.hi = s.hi) : r = s := by
  apply eq_of_values
  · apply Nat.mul_right_cancel (hi_pos r)
    calc
      r.lo * r.hi = m := r.product_eq
      _ = s.lo * s.hi := s.product_eq.symm
      _ = s.lo * r.hi := by rw [hhi]
  · exact hhi

theorem lo_ne_hi {m : Nat} (r s : Representation m) : r.lo ≠ s.hi := by
  intro hcross
  have hprod : r.lo * r.hi = r.lo * s.lo := by
    calc
      r.lo * r.hi = m := r.product_eq
      _ = s.lo * s.hi := s.product_eq.symm
      _ = r.lo * s.lo := by rw [← hcross, Nat.mul_comm]
  have hswap : r.hi = s.lo := Nat.mul_left_cancel r.positive hprod
  have hback : s.hi < s.lo := by
    calc
      s.hi = r.lo := hcross.symm
      _ < r.hi := r.ordered
      _ = s.lo := hswap
  exact (Nat.not_lt_of_ge (Nat.le_of_lt s.ordered)) hback

theorem hi_ne_lo {m : Nat} (r s : Representation m) : r.hi ≠ s.lo := by
  intro hcross
  exact lo_ne_hi s r hcross.symm

/-- Distinct representations of one positive integer have disjoint endpoints.
This is the cancellation lemma behind the six-vertex forbidden pattern. -/
theorem distinct_endpoints {m : Nat} {r s : Representation m} (hne : r ≠ s) :
    r.lo ≠ s.lo ∧ r.lo ≠ s.hi ∧ r.hi ≠ s.lo ∧ r.hi ≠ s.hi := by
  refine ⟨?_, lo_ne_hi r s, hi_ne_lo r s, ?_⟩
  · intro hlo
    exact hne (eq_of_lo_eq r s hlo)
  · intro hhi
    exact hne (eq_of_hi_eq r s hhi)

/-- Three distinct representations have six distinct endpoints. -/
theorem three_endpoints_nodup {m : Nat} (r₁ r₂ r₃ : Representation m)
    (h₁₂ : r₁ ≠ r₂) (h₁₃ : r₁ ≠ r₃) (h₂₃ : r₂ ≠ r₃) :
    [r₁.lo, r₁.hi, r₂.lo, r₂.hi, r₃.lo, r₃.hi].Nodup := by
  have h₁ : r₁.lo ≠ r₁.hi := Nat.ne_of_lt r₁.ordered
  have h₂ : r₂.lo ≠ r₂.hi := Nat.ne_of_lt r₂.ordered
  have h₃ : r₃.lo ≠ r₃.hi := Nat.ne_of_lt r₃.ordered
  rcases distinct_endpoints h₁₂ with ⟨h₁₂ll, h₁₂lh, h₁₂hl, h₁₂hh⟩
  rcases distinct_endpoints h₁₃ with ⟨h₁₃ll, h₁₃lh, h₁₃hl, h₁₃hh⟩
  rcases distinct_endpoints h₂₃ with ⟨h₂₃ll, h₂₃lh, h₂₃hl, h₂₃hh⟩
  simp_all [List.nodup_cons]

end Representation

/-- Cartesian product of two finite profiles, represented as duplicate-free
lists below. -/
def cartesian (U V : List Nat) : List (Nat × Nat) :=
  U.flatMap fun u => V.map fun v => (u, v)

theorem mem_cartesian_iff {U V : List Nat} {a b : Nat} :
    (a, b) ∈ cartesian U V ↔ a ∈ U ∧ b ∈ V := by
  simp [cartesian]

/-- The list of ordered pairs that implements the convention `a < b` in the
definition of the representation function from Problem #796. -/
def representationPairs (A : List Nat) (m : Nat) : List (Nat × Nat) :=
  (cartesian A A).filter fun p => decide (p.1 < p.2 ∧ p.1 * p.2 = m)

/-- The representation function `r_A(m)` from the problem statement. -/
def representationCount (A : List Nat) (m : Nat) : Nat :=
  (representationPairs A m).length

/-- Membership in `representationPairs` is exactly membership of both
endpoints, strict order, and the required product equality. -/
theorem mem_representationPairs_iff {A : List Nat} {m a b : Nat} :
    (a, b) ∈ representationPairs A m ↔
      a ∈ A ∧ b ∈ A ∧ a < b ∧ a * b = m := by
  unfold representationPairs
  rw [List.mem_filter, mem_cartesian_iff]
  simp [and_assoc]

/-- Finite version of the admissibility condition in Problem #796. -/
def Admissible (A : List Nat) : Prop :=
  ∀ m : Nat, representationCount A m ≤ 2

/-- Number of ordered cross-profile representations of `t`.  Unlike
`representationCount`, the two coordinates belong to named profiles, so no
order condition is imposed. -/
def crossCount (U V : List Nat) (t : Nat) : Nat :=
  ((cartesian U V).filter fun p => decide (p.1 * p.2 = t)).length

/-- The compatibility relation used by the variational problem. -/
def Compatible (U V : List Nat) : Prop :=
  ∀ t : Nat, crossCount U V t ≤ 2

/-- Every element of `U` is at most `B`. -/
def BoundedBy (B : Nat) (U : List Nat) : Prop :=
  ∀ x ∈ U, x ≤ B

/-- A finite compatibility certificate through product value `B`. -/
def CompatibleThrough (B : Nat) (U V : List Nat) : Prop :=
  ∀ t : Fin (B + 1), crossCount U V t.val ≤ 2

/-- Executable form of a bounded compatibility check. -/
def compatibilityCertificate (B : Nat) (U V : List Nat) : Bool :=
  (List.range (B + 1)).all fun t => decide (crossCount U V t ≤ 2)

theorem compatibleThrough_of_certificate {B : Nat} {U V : List Nat}
    (h : compatibilityCertificate B U V = true) : CompatibleThrough B U V := by
  intro t
  have hall := List.all_eq_true.mp h
  have ht := hall t.val (List.mem_range.mpr t.isLt)
  simpa [compatibilityCertificate] using ht

/-- A finite collision certificate suffices once both profiles have bounded
support. -/
theorem compatible_of_bounded_certificate {B : Nat} {U V : List Nat}
    (hU : BoundedBy B U) (hV : BoundedBy B V)
    (hcert : CompatibleThrough (B * B) U V) : Compatible U V := by
  intro t
  by_cases ht : t ≤ B * B
  · exact hcert ⟨t, Nat.lt_succ_iff.mpr ht⟩
  · have hempty :
        (cartesian U V).filter (fun p => decide (p.1 * p.2 = t)) = [] := by
      apply List.filter_eq_nil_iff.mpr
      intro p hp
      simp only [decide_eq_true_eq]
      intro hprod
      rcases p with ⟨u, v⟩
      have hpUV : u ∈ U ∧ v ∈ V := mem_cartesian_iff.mp hp
      have hle : u * v ≤ B * B :=
        Nat.mul_le_mul (hU u hpUV.1) (hV v hpUV.2)
      exact ht (hprod ▸ hle)
    simp [crossCount, hempty]

/-- The three finite cores below 17 used in the explicit `79/60` profile
construction.  Primes at least 17 are deliberately not part of this finite
certificate. -/
def core0 : List Nat := [1, 2, 3, 5, 7, 11, 13]

def core1 : List Nat := [1, 3, 4, 5, 6, 7, 11, 13]

def core2 : List Nat := [1, 2, 5, 7, 8, 9, 11, 12, 13, 15]

theorem core0_nodup : core0.Nodup := by native_decide

theorem core1_nodup : core1.Nodup := by native_decide

theorem core2_nodup : core2.Nodup := by native_decide

theorem core0_bounded : BoundedBy 15 core0 := by
  simp [BoundedBy, core0]

theorem core1_bounded : BoundedBy 15 core1 := by
  simp [BoundedBy, core1]

theorem core2_bounded : BoundedBy 15 core2 := by
  simp [BoundedBy, core2]

theorem core0_core0_certificate : CompatibleThrough 225 core0 core0 := by
  apply compatibleThrough_of_certificate
  native_decide

theorem core0_core1_certificate : CompatibleThrough 225 core0 core1 := by
  apply compatibleThrough_of_certificate
  native_decide

theorem core0_core2_certificate : CompatibleThrough 225 core0 core2 := by
  apply compatibleThrough_of_certificate
  native_decide

theorem core1_core0_certificate : CompatibleThrough 225 core1 core0 := by
  apply compatibleThrough_of_certificate
  native_decide

theorem core1_core1_certificate : CompatibleThrough 225 core1 core1 := by
  apply compatibleThrough_of_certificate
  native_decide

theorem core1_core2_certificate : CompatibleThrough 225 core1 core2 := by
  apply compatibleThrough_of_certificate
  native_decide

theorem core2_core0_certificate : CompatibleThrough 225 core2 core0 := by
  apply compatibleThrough_of_certificate
  native_decide

theorem core2_core1_certificate : CompatibleThrough 225 core2 core1 := by
  apply compatibleThrough_of_certificate
  native_decide

theorem core2_core2_certificate : CompatibleThrough 225 core2 core2 := by
  apply compatibleThrough_of_certificate
  native_decide

/-- Machine-checked all-value compatibility of every ordered pair of finite
cores. -/
theorem finite_cores_pairwise_compatible :
    Compatible core0 core0 ∧ Compatible core0 core1 ∧
    Compatible core0 core2 ∧ Compatible core1 core0 ∧
    Compatible core1 core1 ∧ Compatible core1 core2 ∧
    Compatible core2 core0 ∧ Compatible core2 core1 ∧
    Compatible core2 core2 := by
  exact ⟨
    compatible_of_bounded_certificate core0_bounded core0_bounded
      core0_core0_certificate,
    compatible_of_bounded_certificate core0_bounded core1_bounded
      core0_core1_certificate,
    compatible_of_bounded_certificate core0_bounded core2_bounded
      core0_core2_certificate,
    compatible_of_bounded_certificate core1_bounded core0_bounded
      core1_core0_certificate,
    compatible_of_bounded_certificate core1_bounded core1_bounded
      core1_core1_certificate,
    compatible_of_bounded_certificate core1_bounded core2_bounded
      core1_core2_certificate,
    compatible_of_bounded_certificate core2_bounded core0_bounded
      core2_core0_certificate,
    compatible_of_bounded_certificate core2_bounded core1_bounded
      core2_core1_certificate,
    compatible_of_bounded_certificate core2_bounded core2_bounded
      core2_core2_certificate
  ⟩

/-- Algebraic identity behind the four antipodal pairings of a
`K_{2,2,2}^{(3)}` cube.  Distinctness of the eight corners is a separate
hypothesis in the paper proof. -/
theorem cube_antipodal_products
    (x₀ x₁ y₀ y₁ z₀ z₁ : Nat) :
    (x₀ * y₀ * z₀) * (x₁ * y₁ * z₁) =
        (x₀ * y₀ * z₁) * (x₁ * y₁ * z₀) ∧
    (x₀ * y₀ * z₀) * (x₁ * y₁ * z₁) =
        (x₀ * y₁ * z₀) * (x₁ * y₀ * z₁) ∧
    (x₀ * y₀ * z₀) * (x₁ * y₁ * z₁) =
        (x₀ * y₁ * z₁) * (x₁ * y₀ * z₀) := by
  simp [Nat.mul_comm, Nat.mul_left_comm]

end Erdos796
