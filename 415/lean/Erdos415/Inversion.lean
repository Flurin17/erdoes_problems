import Mathlib

/-!
# Inverting a sharply growing threshold sequence

This module isolates the analytic inversion used in Part IV of the proof of
Erdős Problem 415.  The inverse is represented by its defining threshold
bracket; all small-index pathologies are handled with eventual hypotheses.
-/

open Filter Function Topology

namespace Erdos415

noncomputable section

set_option maxHeartbeats 800000

/-- The `r`-fold iterate of the natural logarithm. -/
def logIter : ℕ → ℝ → ℝ
  | 0, x => x
  | r + 1, x => Real.log (logIter r x)

@[simp] theorem logIter_zero (x : ℝ) : logIter 0 x = x := rfl

@[simp] theorem logIter_succ (r : ℕ) (x : ℝ) :
    logIter (r + 1) x = Real.log (logIter r x) := rfl

/-- Every fixed iterate of `log` tends to infinity. -/
theorem tendsto_logIter_atTop (r : ℕ) : Tendsto (logIter r) atTop atTop := by
  induction r with
  | zero => simpa [logIter] using (tendsto_id : Tendsto (id : ℝ → ℝ) atTop atTop)
  | succ r ih =>
      simpa [logIter_succ] using Real.tendsto_log_atTop.comp ih

/-- The logarithmic difference of two nonzero functions tends to zero when
their ratio tends to one. -/
theorem tendsto_log_sub_log_of_ratio {α : Type*} {l : Filter α}
    {x y : α → ℝ} (hxy : Tendsto (fun i => x i / y i) l (𝓝 1))
    (hx : ∀ᶠ i in l, x i ≠ 0) (hy : ∀ᶠ i in l, y i ≠ 0) :
    Tendsto (fun i => Real.log (x i) - Real.log (y i)) l (𝓝 0) := by
  have hlog : Tendsto (fun i => Real.log (x i / y i)) l (𝓝 0) := by
    simpa using hxy.log one_ne_zero
  apply hlog.congr'
  filter_upwards [hx, hy] with i hxi hyi
  rw [Real.log_div hxi hyi]

/-- Successive values of every positive iterate of `log` differ by `o(1)` on
the natural numbers. -/
theorem tendsto_logIter_nat_succ_sub (r : ℕ) :
    Tendsto (fun k : ℕ =>
      logIter (r + 1) (k + 1 : ℕ) - logIter (r + 1) (k : ℕ))
      atTop (𝓝 0) := by
  induction r with
  | zero =>
      simpa using Real.tendsto_log_nat_add_one_sub_log
  | succ r ih =>
      have hf : Tendsto (fun k : ℕ => logIter (r + 1) (k : ℝ)) atTop atTop :=
        (tendsto_logIter_atTop (r + 1)).comp tendsto_natCast_atTop_atTop
      have hquot : Tendsto (fun k : ℕ =>
          (logIter (r + 1) (k + 1 : ℕ) - logIter (r + 1) (k : ℕ)) /
            logIter (r + 1) (k : ℕ)) atTop (𝓝 0) :=
        ih.div_atTop hf
      have hratio : Tendsto (fun k : ℕ =>
          logIter (r + 1) (k + 1 : ℕ) / logIter (r + 1) (k : ℕ))
          atTop (𝓝 1) := by
        have h := (tendsto_const_nhds (x := (1 : ℝ))).add hquot
        have heq : (fun k : ℕ =>
            1 + (logIter (r + 1) (k + 1 : ℕ) - logIter (r + 1) (k : ℕ)) /
              logIter (r + 1) (k : ℕ)) =ᶠ[atTop]
            (fun k : ℕ =>
              logIter (r + 1) (k + 1 : ℕ) / logIter (r + 1) (k : ℕ)) := by
          filter_upwards [hf.eventually_ne_atTop 0] with k hk
          have hk' : Real.log (logIter r (k : ℝ)) ≠ 0 := by
            simpa [logIter_succ] using hk
          field_simp [hk']
        have h' : Tendsto (fun k : ℕ =>
            1 + (logIter (r + 1) (k + 1 : ℕ) - logIter (r + 1) (k : ℕ)) /
              logIter (r + 1) (k : ℕ)) atTop (𝓝 1) := by
          simpa using h
        exact h'.congr' heq
      have hne : ∀ᶠ k : ℕ in atTop, logIter (r + 1) (k : ℕ) ≠ 0 :=
        hf.eventually_ne_atTop 0
      have hne' : ∀ᶠ k : ℕ in atTop, logIter (r + 1) (k + 1 : ℕ) ≠ 0 := by
        have hshift : Tendsto (fun k : ℕ => k + 1) atTop atTop :=
          tendsto_atTop_mono (fun k => Nat.le_succ k) tendsto_id
        have hf' : Tendsto (fun k : ℕ => logIter (r + 1) (k + 1 : ℕ)) atTop atTop :=
          (tendsto_logIter_atTop (r + 1)).comp
            (tendsto_natCast_atTop_atTop.comp hshift)
        exact hf'.eventually_ne_atTop 0
      simpa [logIter_succ, Nat.cast_add, Nat.cast_one] using
        tendsto_log_sub_log_of_ratio hratio hne' hne

/-- One more logarithm is little-oh of the preceding iterate. -/
theorem logIter_succ_isLittleO (r : ℕ) :
    logIter (r + 1) =o[atTop] logIter r := by
  simpa only [Function.comp_apply, logIter_succ] using
    Real.isLittleO_log_id_atTop.comp_tendsto (tendsto_logIter_atTop r)

/-- Three iterated logarithms are little-oh of the identity. -/
theorem logIter_three_isLittleO_id : logIter 3 =o[atTop] id := by
  exact ((logIter_succ_isLittleO 2).trans (logIter_succ_isLittleO 1)).trans
    (logIter_succ_isLittleO 0)

/-- The elementary successor ratio on the natural numbers. -/
theorem tendsto_nat_succ_div_nat :
    Tendsto (fun k : ℕ => ((k + 1 : ℕ) : ℝ) / (k : ℝ)) atTop (𝓝 1) := by
  have hinv : Tendsto (fun k : ℕ => (1 : ℝ) / (k : ℝ)) atTop (𝓝 0) :=
    tendsto_const_nhds.div_atTop tendsto_natCast_atTop_atTop
  have h := (tendsto_const_nhds (x := (1 : ℝ))).add hinv
  have heq : (fun k : ℕ => 1 + (1 : ℝ) / (k : ℝ)) =ᶠ[atTop]
      (fun k : ℕ => ((k + 1 : ℕ) : ℝ) / (k : ℝ)) := by
    filter_upwards [eventually_ne_atTop (0 : ℕ)] with k hk
    push_cast
    field_simp
  exact (by simpa using h).congr' heq

/-- The third iterated logarithm at `k+1`, divided by `k`, tends to zero. -/
theorem tendsto_logIter_three_succ_div_nat :
    Tendsto (fun k : ℕ => logIter 3 (k + 1 : ℕ) / (k : ℝ)) atTop (𝓝 0) := by
  have hshift : Tendsto (fun k : ℕ => k + 1) atTop atTop :=
    tendsto_atTop_mono (fun k => Nat.le_succ k) tendsto_id
  have hbase : Tendsto (fun x : ℝ => logIter 3 x / x) atTop (𝓝 0) :=
    logIter_three_isLittleO_id.tendsto_div_nhds_zero
  have hs : Tendsto (fun k : ℕ =>
      logIter 3 (k + 1 : ℕ) / ((k + 1 : ℕ) : ℝ)) atTop (𝓝 0) :=
    hbase.comp (tendsto_natCast_atTop_atTop.comp hshift)
  have hmul := hs.mul tendsto_nat_succ_div_nat
  apply hmul.congr'
  filter_upwards [eventually_ne_atTop (0 : ℕ)] with k hk
  norm_cast at hk
  field_simp

/-- An asymptotic formula at `k` also supplies the upper endpoint expression
with threshold `M (k+1)` and denominator `k`. -/
theorem threshold_upper_transfer (M : ℕ → ℕ) (a : ℝ)
    (hM : Tendsto (fun k : ℕ =>
      logIter 3 (M k : ℝ) / (k : ℝ) - logIter 3 (k : ℝ)) atTop (𝓝 a)) :
    Tendsto (fun k : ℕ =>
      logIter 3 (M (k + 1) : ℝ) / (k : ℝ) - logIter 3 (k : ℝ))
      atTop (𝓝 a) := by
  have hshift : Tendsto (fun k : ℕ => k + 1) atTop atTop :=
    tendsto_atTop_mono (fun k => Nat.le_succ k) tendsto_id
  have he : Tendsto (fun k : ℕ =>
      logIter 3 (M (k + 1) : ℝ) / ((k + 1 : ℕ) : ℝ) -
        logIter 3 (k + 1 : ℝ)) atTop (𝓝 a) := hM.comp hshift
  have hprod := he.mul tendsto_nat_succ_div_nat
  have hsucc := tendsto_logIter_nat_succ_sub 2
  have hsum := (hprod.add hsucc).add tendsto_logIter_three_succ_div_nat
  apply hsum.congr'
  filter_upwards [eventually_ne_atTop (0 : ℕ)] with k hk
  norm_cast at hk
  field_simp
  ring

end

end Erdos415
