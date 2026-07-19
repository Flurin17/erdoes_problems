import Mathlib

/-!
# The exact primorial-loss comparison

The analytic argument for Erdős Problem 415 uses the elementary fact that, for a fixed number
of distinct prime divisors, replacing the ordered prime divisors by smaller ones decreases their
product and increases the Euler loss product `prod p / (p - 1)`.  This file isolates that exact
finite comparison.  It deliberately contains no asymptotic input.
-/

namespace Erdos415

open scoped BigOperators

/-- The Euler loss contributed by a prime divisor.  The definition makes sense for every natural
number; all comparison theorems below assume that the arguments are at least two. -/
def lossFactor (n : ℕ) : ℚ := (n : ℚ) / (n - 1 : ℕ)

/-- `p / (p - 1)` is positive for `p ≥ 2`. -/
theorem lossFactor_pos {p : ℕ} (hp : 2 ≤ p) : 0 < lossFactor p := by
  unfold lossFactor
  apply div_pos
  · norm_cast
    omega
  · norm_cast
    omega

/-- Euler loss factors are always nonnegative (the cases zero and one evaluate to zero). -/
theorem lossFactor_nonneg (p : ℕ) : 0 ≤ lossFactor p := by
  unfold lossFactor
  positivity

/-- Every Euler loss factor is at least one. -/
theorem one_le_lossFactor {p : ℕ} (hp : 2 ≤ p) : 1 ≤ lossFactor p := by
  unfold lossFactor
  rw [le_div_iff₀]
  · norm_cast
    omega
  · norm_cast
    omega

/-- The Euler loss factor is antitone on the integers at least two. -/
theorem lossFactor_antitone {p q : ℕ} (hp : 2 ≤ p) (hpq : p ≤ q) :
    lossFactor q ≤ lossFactor p := by
  unfold lossFactor
  have expand (r : ℕ) (hr : 2 ≤ r) :
      (r : ℚ) / (r - 1 : ℕ) = 1 + 1 / (r - 1 : ℕ) := by
    have hrne : (r : ℚ) - 1 ≠ 0 := by
      apply sub_ne_zero.mpr
      norm_cast
      omega
    field_simp [hrne]
  rw [expand q (hp.trans hpq), expand p hp]
  apply add_le_add_left
  apply one_div_le_one_div_of_le
  · norm_cast
    omega
  · norm_cast
    omega

/-- The product of the entries of a componentwise smaller list is smaller. -/
theorem product_le_of_ordered_factors {ps qs : List ℕ}
    (h : List.Forall₂ (· ≤ ·) ps qs) : ps.prod ≤ qs.prod :=
  h.prod_le_prod'

/-- The loss product of a componentwise smaller list (whose entries are at least two) is larger.

This is the finite rearrangement step used for primorial extremality: after ordering the distinct
prime divisors of a number, the `i`-th prime is no smaller than the `i`-th prime in the initial
prime segment. -/
theorem loss_product_le_of_ordered_factors {ps qs : List ℕ}
    (h : List.Forall₂ (· ≤ ·) ps qs) (hps : ∀ p ∈ ps, 2 ≤ p) :
    (qs.map lossFactor).prod ≤ (ps.map lossFactor).prod := by
  induction h with
  | nil => simp
  | @cons p q ps qs hpq htail ih =>
      simp only [List.forall_mem_cons] at hps
      simp only [List.map_cons, List.prod_cons]
      exact mul_le_mul (lossFactor_antitone hps.1 hpq) (ih hps.2)
        (List.prod_nonneg (by simpa using fun q (_ : q ∈ qs) ↦ lossFactor_nonneg q))
        (le_of_lt (lossFactor_pos hps.1))

/-- Simultaneous exact comparison: smaller ordered factors mean a smaller integer product and a
larger Euler loss product. -/
theorem ordered_factors_extremal {ps qs : List ℕ}
    (h : List.Forall₂ (· ≤ ·) ps qs) (hps : ∀ p ∈ ps, 2 ≤ p) :
    ps.prod ≤ qs.prod ∧ (qs.map lossFactor).prod ≤ (ps.map lossFactor).prod :=
  ⟨product_le_of_ordered_factors h, loss_product_le_of_ordered_factors h hps⟩

/-- The logarithmic form of the loss comparison. -/
theorem log_loss_product_le_of_ordered_factors {ps qs : List ℕ}
    (h : List.Forall₂ (· ≤ ·) ps qs) (hps : ∀ p ∈ ps, 2 ≤ p) :
    Real.log (((qs.map lossFactor).prod : ℚ) : ℝ) ≤
      Real.log (((ps.map lossFactor).prod : ℚ) : ℝ) := by
  have hqs : ∀ q ∈ qs, 2 ≤ q := by
    induction h with
    | nil => simp
    | @cons p q ps qs hpq htail ih =>
        simp only [List.forall_mem_cons] at hps ⊢
        exact ⟨hps.1.trans hpq, ih hps.2⟩
  apply Real.log_le_log
  · exact_mod_cast List.prod_pos (by
      intro a ha
      simp only [List.mem_map] at ha
      obtain ⟨q, hq, rfl⟩ := ha
      exact lossFactor_pos (hqs q hq))
  · exact_mod_cast loss_product_le_of_ordered_factors h hps

/-- The first `k` values of an increasing sequence.  In the application, `p i` is the `i`-th
prime, so `prefixProduct p k` is the `k`-prime primorial. -/
def prefixFactors (p : ℕ → ℕ) (k : ℕ) : List ℕ := (List.range k).map p

/-- Product of the first `k` values of a sequence. -/
def prefixProduct (p : ℕ → ℕ) (k : ℕ) : ℕ := (prefixFactors p k).prod

/-- Euler loss product of the first `k` values of a sequence. -/
def prefixLoss (p : ℕ → ℕ) (k : ℕ) : ℚ :=
  ((prefixFactors p k).map lossFactor).prod

/-- Prefix product is monotone in the prefix length when every factor is at least two. -/
theorem prefixProduct_monotone {p : ℕ → ℕ} (hp : ∀ i, 2 ≤ p i) :
    Monotone (prefixProduct p) := by
  refine monotone_nat_of_le_succ fun k ↦ ?_
  rw [show prefixProduct p (k + 1) = prefixProduct p k * p k by
    simp [prefixProduct, prefixFactors, List.range_succ]]
  exact le_mul_of_one_le_right'
    (Nat.one_le_iff_ne_zero.mpr (ne_of_gt (lt_of_lt_of_le Nat.zero_lt_two (hp k))))

/-- Prefix loss is monotone in the prefix length when every factor is at least two. -/
theorem prefixLoss_monotone {p : ℕ → ℕ} (hp : ∀ i, 2 ≤ p i) :
    Monotone (prefixLoss p) := by
  refine monotone_nat_of_le_succ fun k ↦ ?_
  rw [show prefixLoss p (k + 1) = prefixLoss p k * lossFactor (p k) by
    simp [prefixLoss, prefixFactors, List.range_succ]]
  apply le_mul_of_one_le_right
  · exact List.prod_nonneg (by
      intro a ha
      obtain ⟨i, -, rfl⟩ := List.mem_map.mp ha
      exact lossFactor_nonneg i)
  · exact one_le_lossFactor (hp k)

/-- A reusable, exact "largest primorial" theorem.

`p` represents the increasing list of primes, `qs` represents the increasing distinct prime
divisors of a competing integer, and `hordered` is the standard order-statistic comparison saying
that the `i`-th prime is at most the `i`-th member of `qs`.  The hypothesis `hlen` is precisely the
finite consequence of choosing the largest feasible primorial: a competing integer cannot have
more distinct prime divisors.  The conclusion is the required maximal Euler loss product. -/
theorem largest_prefix_maximizes_loss {p : ℕ → ℕ} (hp : ∀ i, 2 ≤ p i) {k : ℕ}
    {qs : List ℕ} (hlen : qs.length ≤ k)
    (hordered : List.Forall₂ (· ≤ ·) (prefixFactors p qs.length) qs) :
    (qs.map lossFactor).prod ≤ prefixLoss p k := by
  calc
    (qs.map lossFactor).prod ≤ prefixLoss p qs.length := by
      apply loss_product_le_of_ordered_factors hordered
      intro q hq
      simp only [prefixFactors, List.mem_map] at hq
      obtain ⟨i, -, rfl⟩ := hq
      exact hp i
    _ ≤ prefixLoss p k := prefixLoss_monotone hp hlen

/-- Exact feasibility form of the largest-prefix argument.

If the `k`-factor prefix fits under `x` but the next prefix does not, then every competing factor
list whose product is at most `x` and whose ordered factors dominate the initial sequence has loss
at most that of the `k`-factor prefix. -/
theorem largest_feasible_prefix_maximizes_loss {p : ℕ → ℕ} (hp : ∀ i, 2 ≤ p i)
    {x k : ℕ} {qs : List ℕ} (hfits : prefixProduct p k ≤ x)
    (hnext : x < prefixProduct p (k + 1)) (hq : qs.prod ≤ x)
    (hordered : List.Forall₂ (· ≤ ·) (prefixFactors p qs.length) qs) :
    prefixProduct p k ≤ x ∧ (qs.map lossFactor).prod ≤ prefixLoss p k := by
  have hpq : prefixProduct p qs.length ≤ qs.prod :=
    product_le_of_ordered_factors hordered
  have hlen : qs.length ≤ k := by
    by_contra hnot
    have hk : k + 1 ≤ qs.length := by omega
    have hmono := prefixProduct_monotone hp hk
    omega
  exact ⟨hfits, largest_prefix_maximizes_loss hp hlen hordered⟩

/-- The zero-indexed sequence of rational primes. -/
noncomputable def nthPrime (i : ℕ) : ℕ := Nat.nth Nat.Prime i

theorem nthPrime_prime (i : ℕ) : Nat.Prime (nthPrime i) := by
  exact Nat.prime_nth_prime i

theorem two_le_nthPrime (i : ℕ) : 2 ≤ nthPrime i := (nthPrime_prime i).two_le

/-- The product of the first `k` primes (the indexed primorial). -/
noncomputable def indexedPrimorial (k : ℕ) : ℕ := prefixProduct nthPrime k

/-- Euler loss product of the first `k` primes. -/
noncomputable def indexedPrimorialLoss (k : ℕ) : ℚ := prefixLoss nthPrime k

/-- Concrete prime specialization of `largest_feasible_prefix_maximizes_loss`.

The only explicit combinatorial input is `hordered`: after the distinct prime divisors of the
competitor are sorted, their `i`-th member dominates the `i`-th prime. -/
theorem largest_primorial_maximizes_loss {x k : ℕ} {qs : List ℕ}
    (hfits : indexedPrimorial k ≤ x) (hnext : x < indexedPrimorial (k + 1))
    (hq : qs.prod ≤ x)
    (hordered : List.Forall₂ (· ≤ ·) (prefixFactors nthPrime qs.length) qs) :
    indexedPrimorial k ≤ x ∧
      (qs.map lossFactor).prod ≤ indexedPrimorialLoss k := by
  exact largest_feasible_prefix_maximizes_loss two_le_nthPrime hfits hnext hq hordered

end Erdos415
