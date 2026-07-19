import Mathlib

/-!
# Exact finite certificates for Problem 415

The helper lemmas evaluate Euler's totient through the proved
prime-multiplication identities in `Mathlib.Data.Nat.Totient`; they do not
rely on an unverified evaluator. A final finite case split certifies both
first-occurrence claims.
-/

namespace Erdos415.FiniteCert

/-- The totients on `m + 1, ..., m + 4` are strictly decreasing. -/
private def decreasingAt (m : ℕ) : Prop :=
  Nat.totient (m + 1) > Nat.totient (m + 2) ∧
    Nat.totient (m + 2) > Nat.totient (m + 3) ∧
      Nat.totient (m + 3) > Nat.totient (m + 4)

/-- The ranks of the totients on `m + 1, ..., m + 4` are `(3,2,1,4)`. -/
private def threeTwoOneFourAt (m : ℕ) : Prop :=
  Nat.totient (m + 3) < Nat.totient (m + 2) ∧
    Nat.totient (m + 2) < Nat.totient (m + 1) ∧
      Nat.totient (m + 1) < Nat.totient (m + 4)

/-- `s` is the first starting point at which `P` holds. -/
private def FirstStart (P : ℕ → Prop) (s : ℕ) : Prop :=
  P s ∧ ∀ m : Fin s, ¬ P m

@[simp] private theorem phi_1 : Nat.totient 1 = 1 := Nat.totient_one
@[simp] private theorem phi_2 : Nat.totient 2 = 1 := Nat.totient_two

@[simp] private theorem phi_3 : Nat.totient 3 = 2 := by
  calc
    Nat.totient 3 = Nat.totient (3 * 1) := by norm_num
    _ = (3 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 2 := by norm_num

@[simp] private theorem phi_4 : Nat.totient 4 = 2 := by
  calc
    Nat.totient 4 = Nat.totient (2 * 2) := by norm_num
    _ = 2 * Nat.totient 2 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 2 := by norm_num

@[simp] private theorem phi_5 : Nat.totient 5 = 4 := by
  calc
    Nat.totient 5 = Nat.totient (5 * 1) := by norm_num
    _ = (5 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 4 := by norm_num

@[simp] private theorem phi_6 : Nat.totient 6 = 2 := by
  calc
    Nat.totient 6 = Nat.totient (2 * 3) := by norm_num
    _ = (2 - 1) * Nat.totient 3 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 2 := by norm_num

@[simp] private theorem phi_7 : Nat.totient 7 = 6 := by
  calc
    Nat.totient 7 = Nat.totient (7 * 1) := by norm_num
    _ = (7 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 6 := by norm_num

@[simp] private theorem phi_8 : Nat.totient 8 = 4 := by
  calc
    Nat.totient 8 = Nat.totient (2 * 4) := by norm_num
    _ = 2 * Nat.totient 4 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 4 := by norm_num

@[simp] private theorem phi_9 : Nat.totient 9 = 6 := by
  calc
    Nat.totient 9 = Nat.totient (3 * 3) := by norm_num
    _ = 3 * Nat.totient 3 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 6 := by norm_num

@[simp] private theorem phi_10 : Nat.totient 10 = 4 := by
  calc
    Nat.totient 10 = Nat.totient (2 * 5) := by norm_num
    _ = (2 - 1) * Nat.totient 5 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 4 := by norm_num

@[simp] private theorem phi_11 : Nat.totient 11 = 10 := by
  calc
    Nat.totient 11 = Nat.totient (11 * 1) := by norm_num
    _ = (11 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 10 := by norm_num

@[simp] private theorem phi_12 : Nat.totient 12 = 4 := by
  calc
    Nat.totient 12 = Nat.totient (2 * 6) := by norm_num
    _ = 2 * Nat.totient 6 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 4 := by norm_num

@[simp] private theorem phi_13 : Nat.totient 13 = 12 := by
  calc
    Nat.totient 13 = Nat.totient (13 * 1) := by norm_num
    _ = (13 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 12 := by norm_num

@[simp] private theorem phi_14 : Nat.totient 14 = 6 := by
  calc
    Nat.totient 14 = Nat.totient (2 * 7) := by norm_num
    _ = (2 - 1) * Nat.totient 7 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 6 := by norm_num

@[simp] private theorem phi_15 : Nat.totient 15 = 8 := by
  calc
    Nat.totient 15 = Nat.totient (3 * 5) := by norm_num
    _ = (3 - 1) * Nat.totient 5 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 8 := by norm_num

@[simp] private theorem phi_16 : Nat.totient 16 = 8 := by
  calc
    Nat.totient 16 = Nat.totient (2 * 8) := by norm_num
    _ = 2 * Nat.totient 8 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 8 := by norm_num

@[simp] private theorem phi_17 : Nat.totient 17 = 16 := by
  calc
    Nat.totient 17 = Nat.totient (17 * 1) := by norm_num
    _ = (17 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 16 := by norm_num

@[simp] private theorem phi_18 : Nat.totient 18 = 6 := by
  calc
    Nat.totient 18 = Nat.totient (2 * 9) := by norm_num
    _ = (2 - 1) * Nat.totient 9 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 6 := by norm_num

@[simp] private theorem phi_19 : Nat.totient 19 = 18 := by
  calc
    Nat.totient 19 = Nat.totient (19 * 1) := by norm_num
    _ = (19 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 18 := by norm_num

@[simp] private theorem phi_20 : Nat.totient 20 = 8 := by
  calc
    Nat.totient 20 = Nat.totient (2 * 10) := by norm_num
    _ = 2 * Nat.totient 10 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 8 := by norm_num

@[simp] private theorem phi_21 : Nat.totient 21 = 12 := by
  calc
    Nat.totient 21 = Nat.totient (3 * 7) := by norm_num
    _ = (3 - 1) * Nat.totient 7 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 12 := by norm_num

@[simp] private theorem phi_22 : Nat.totient 22 = 10 := by
  calc
    Nat.totient 22 = Nat.totient (2 * 11) := by norm_num
    _ = (2 - 1) * Nat.totient 11 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 10 := by norm_num

@[simp] private theorem phi_23 : Nat.totient 23 = 22 := by
  calc
    Nat.totient 23 = Nat.totient (23 * 1) := by norm_num
    _ = (23 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 22 := by norm_num

@[simp] private theorem phi_24 : Nat.totient 24 = 8 := by
  calc
    Nat.totient 24 = Nat.totient (2 * 12) := by norm_num
    _ = 2 * Nat.totient 12 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 8 := by norm_num

@[simp] private theorem phi_25 : Nat.totient 25 = 20 := by
  calc
    Nat.totient 25 = Nat.totient (5 * 5) := by norm_num
    _ = 5 * Nat.totient 5 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 20 := by norm_num

@[simp] private theorem phi_26 : Nat.totient 26 = 12 := by
  calc
    Nat.totient 26 = Nat.totient (2 * 13) := by norm_num
    _ = (2 - 1) * Nat.totient 13 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 12 := by norm_num

@[simp] private theorem phi_27 : Nat.totient 27 = 18 := by
  calc
    Nat.totient 27 = Nat.totient (3 * 9) := by norm_num
    _ = 3 * Nat.totient 9 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 18 := by norm_num

@[simp] private theorem phi_28 : Nat.totient 28 = 12 := by
  calc
    Nat.totient 28 = Nat.totient (2 * 14) := by norm_num
    _ = 2 * Nat.totient 14 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 12 := by norm_num

@[simp] private theorem phi_29 : Nat.totient 29 = 28 := by
  calc
    Nat.totient 29 = Nat.totient (29 * 1) := by norm_num
    _ = (29 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 28 := by norm_num

@[simp] private theorem phi_30 : Nat.totient 30 = 8 := by
  calc
    Nat.totient 30 = Nat.totient (2 * 15) := by norm_num
    _ = (2 - 1) * Nat.totient 15 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 8 := by norm_num

@[simp] private theorem phi_31 : Nat.totient 31 = 30 := by
  calc
    Nat.totient 31 = Nat.totient (31 * 1) := by norm_num
    _ = (31 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 30 := by norm_num

@[simp] private theorem phi_32 : Nat.totient 32 = 16 := by
  calc
    Nat.totient 32 = Nat.totient (2 * 16) := by norm_num
    _ = 2 * Nat.totient 16 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 16 := by norm_num

@[simp] private theorem phi_33 : Nat.totient 33 = 20 := by
  calc
    Nat.totient 33 = Nat.totient (3 * 11) := by norm_num
    _ = (3 - 1) * Nat.totient 11 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 20 := by norm_num

@[simp] private theorem phi_34 : Nat.totient 34 = 16 := by
  calc
    Nat.totient 34 = Nat.totient (2 * 17) := by norm_num
    _ = (2 - 1) * Nat.totient 17 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 16 := by norm_num

@[simp] private theorem phi_35 : Nat.totient 35 = 24 := by
  calc
    Nat.totient 35 = Nat.totient (5 * 7) := by norm_num
    _ = (5 - 1) * Nat.totient 7 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_36 : Nat.totient 36 = 12 := by
  calc
    Nat.totient 36 = Nat.totient (2 * 18) := by norm_num
    _ = 2 * Nat.totient 18 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 12 := by norm_num

@[simp] private theorem phi_37 : Nat.totient 37 = 36 := by
  calc
    Nat.totient 37 = Nat.totient (37 * 1) := by norm_num
    _ = (37 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 36 := by norm_num

@[simp] private theorem phi_38 : Nat.totient 38 = 18 := by
  calc
    Nat.totient 38 = Nat.totient (2 * 19) := by norm_num
    _ = (2 - 1) * Nat.totient 19 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 18 := by norm_num

@[simp] private theorem phi_39 : Nat.totient 39 = 24 := by
  calc
    Nat.totient 39 = Nat.totient (3 * 13) := by norm_num
    _ = (3 - 1) * Nat.totient 13 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_40 : Nat.totient 40 = 16 := by
  calc
    Nat.totient 40 = Nat.totient (2 * 20) := by norm_num
    _ = 2 * Nat.totient 20 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 16 := by norm_num

@[simp] private theorem phi_41 : Nat.totient 41 = 40 := by
  calc
    Nat.totient 41 = Nat.totient (41 * 1) := by norm_num
    _ = (41 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 40 := by norm_num

@[simp] private theorem phi_42 : Nat.totient 42 = 12 := by
  calc
    Nat.totient 42 = Nat.totient (2 * 21) := by norm_num
    _ = (2 - 1) * Nat.totient 21 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 12 := by norm_num

@[simp] private theorem phi_43 : Nat.totient 43 = 42 := by
  calc
    Nat.totient 43 = Nat.totient (43 * 1) := by norm_num
    _ = (43 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 42 := by norm_num

@[simp] private theorem phi_44 : Nat.totient 44 = 20 := by
  calc
    Nat.totient 44 = Nat.totient (2 * 22) := by norm_num
    _ = 2 * Nat.totient 22 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 20 := by norm_num

@[simp] private theorem phi_45 : Nat.totient 45 = 24 := by
  calc
    Nat.totient 45 = Nat.totient (3 * 15) := by norm_num
    _ = 3 * Nat.totient 15 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_46 : Nat.totient 46 = 22 := by
  calc
    Nat.totient 46 = Nat.totient (2 * 23) := by norm_num
    _ = (2 - 1) * Nat.totient 23 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 22 := by norm_num

@[simp] private theorem phi_47 : Nat.totient 47 = 46 := by
  calc
    Nat.totient 47 = Nat.totient (47 * 1) := by norm_num
    _ = (47 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 46 := by norm_num

@[simp] private theorem phi_48 : Nat.totient 48 = 16 := by
  calc
    Nat.totient 48 = Nat.totient (2 * 24) := by norm_num
    _ = 2 * Nat.totient 24 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 16 := by norm_num

@[simp] private theorem phi_49 : Nat.totient 49 = 42 := by
  calc
    Nat.totient 49 = Nat.totient (7 * 7) := by norm_num
    _ = 7 * Nat.totient 7 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 42 := by norm_num

@[simp] private theorem phi_50 : Nat.totient 50 = 20 := by
  calc
    Nat.totient 50 = Nat.totient (2 * 25) := by norm_num
    _ = (2 - 1) * Nat.totient 25 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 20 := by norm_num

@[simp] private theorem phi_51 : Nat.totient 51 = 32 := by
  calc
    Nat.totient 51 = Nat.totient (3 * 17) := by norm_num
    _ = (3 - 1) * Nat.totient 17 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 32 := by norm_num

@[simp] private theorem phi_52 : Nat.totient 52 = 24 := by
  calc
    Nat.totient 52 = Nat.totient (2 * 26) := by norm_num
    _ = 2 * Nat.totient 26 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_53 : Nat.totient 53 = 52 := by
  calc
    Nat.totient 53 = Nat.totient (53 * 1) := by norm_num
    _ = (53 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 52 := by norm_num

@[simp] private theorem phi_54 : Nat.totient 54 = 18 := by
  calc
    Nat.totient 54 = Nat.totient (2 * 27) := by norm_num
    _ = (2 - 1) * Nat.totient 27 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 18 := by norm_num

@[simp] private theorem phi_55 : Nat.totient 55 = 40 := by
  calc
    Nat.totient 55 = Nat.totient (5 * 11) := by norm_num
    _ = (5 - 1) * Nat.totient 11 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 40 := by norm_num

@[simp] private theorem phi_56 : Nat.totient 56 = 24 := by
  calc
    Nat.totient 56 = Nat.totient (2 * 28) := by norm_num
    _ = 2 * Nat.totient 28 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_57 : Nat.totient 57 = 36 := by
  calc
    Nat.totient 57 = Nat.totient (3 * 19) := by norm_num
    _ = (3 - 1) * Nat.totient 19 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 36 := by norm_num

@[simp] private theorem phi_58 : Nat.totient 58 = 28 := by
  calc
    Nat.totient 58 = Nat.totient (2 * 29) := by norm_num
    _ = (2 - 1) * Nat.totient 29 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 28 := by norm_num

@[simp] private theorem phi_59 : Nat.totient 59 = 58 := by
  calc
    Nat.totient 59 = Nat.totient (59 * 1) := by norm_num
    _ = (59 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 58 := by norm_num

@[simp] private theorem phi_60 : Nat.totient 60 = 16 := by
  calc
    Nat.totient 60 = Nat.totient (2 * 30) := by norm_num
    _ = 2 * Nat.totient 30 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 16 := by norm_num

@[simp] private theorem phi_61 : Nat.totient 61 = 60 := by
  calc
    Nat.totient 61 = Nat.totient (61 * 1) := by norm_num
    _ = (61 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 60 := by norm_num

@[simp] private theorem phi_62 : Nat.totient 62 = 30 := by
  calc
    Nat.totient 62 = Nat.totient (2 * 31) := by norm_num
    _ = (2 - 1) * Nat.totient 31 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 30 := by norm_num

@[simp] private theorem phi_63 : Nat.totient 63 = 36 := by
  calc
    Nat.totient 63 = Nat.totient (3 * 21) := by norm_num
    _ = 3 * Nat.totient 21 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 36 := by norm_num

@[simp] private theorem phi_64 : Nat.totient 64 = 32 := by
  calc
    Nat.totient 64 = Nat.totient (2 * 32) := by norm_num
    _ = 2 * Nat.totient 32 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 32 := by norm_num

@[simp] private theorem phi_65 : Nat.totient 65 = 48 := by
  calc
    Nat.totient 65 = Nat.totient (5 * 13) := by norm_num
    _ = (5 - 1) * Nat.totient 13 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_66 : Nat.totient 66 = 20 := by
  calc
    Nat.totient 66 = Nat.totient (2 * 33) := by norm_num
    _ = (2 - 1) * Nat.totient 33 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 20 := by norm_num

@[simp] private theorem phi_67 : Nat.totient 67 = 66 := by
  calc
    Nat.totient 67 = Nat.totient (67 * 1) := by norm_num
    _ = (67 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 66 := by norm_num

@[simp] private theorem phi_68 : Nat.totient 68 = 32 := by
  calc
    Nat.totient 68 = Nat.totient (2 * 34) := by norm_num
    _ = 2 * Nat.totient 34 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 32 := by norm_num

@[simp] private theorem phi_69 : Nat.totient 69 = 44 := by
  calc
    Nat.totient 69 = Nat.totient (3 * 23) := by norm_num
    _ = (3 - 1) * Nat.totient 23 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 44 := by norm_num

@[simp] private theorem phi_70 : Nat.totient 70 = 24 := by
  calc
    Nat.totient 70 = Nat.totient (2 * 35) := by norm_num
    _ = (2 - 1) * Nat.totient 35 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_71 : Nat.totient 71 = 70 := by
  calc
    Nat.totient 71 = Nat.totient (71 * 1) := by norm_num
    _ = (71 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 70 := by norm_num

@[simp] private theorem phi_72 : Nat.totient 72 = 24 := by
  calc
    Nat.totient 72 = Nat.totient (2 * 36) := by norm_num
    _ = 2 * Nat.totient 36 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_73 : Nat.totient 73 = 72 := by
  calc
    Nat.totient 73 = Nat.totient (73 * 1) := by norm_num
    _ = (73 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_74 : Nat.totient 74 = 36 := by
  calc
    Nat.totient 74 = Nat.totient (2 * 37) := by norm_num
    _ = (2 - 1) * Nat.totient 37 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 36 := by norm_num

@[simp] private theorem phi_75 : Nat.totient 75 = 40 := by
  calc
    Nat.totient 75 = Nat.totient (3 * 25) := by norm_num
    _ = (3 - 1) * Nat.totient 25 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 40 := by norm_num

@[simp] private theorem phi_76 : Nat.totient 76 = 36 := by
  calc
    Nat.totient 76 = Nat.totient (2 * 38) := by norm_num
    _ = 2 * Nat.totient 38 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 36 := by norm_num

@[simp] private theorem phi_77 : Nat.totient 77 = 60 := by
  calc
    Nat.totient 77 = Nat.totient (7 * 11) := by norm_num
    _ = (7 - 1) * Nat.totient 11 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 60 := by norm_num

@[simp] private theorem phi_78 : Nat.totient 78 = 24 := by
  calc
    Nat.totient 78 = Nat.totient (2 * 39) := by norm_num
    _ = (2 - 1) * Nat.totient 39 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_79 : Nat.totient 79 = 78 := by
  calc
    Nat.totient 79 = Nat.totient (79 * 1) := by norm_num
    _ = (79 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 78 := by norm_num

@[simp] private theorem phi_80 : Nat.totient 80 = 32 := by
  calc
    Nat.totient 80 = Nat.totient (2 * 40) := by norm_num
    _ = 2 * Nat.totient 40 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 32 := by norm_num

@[simp] private theorem phi_81 : Nat.totient 81 = 54 := by
  calc
    Nat.totient 81 = Nat.totient (3 * 27) := by norm_num
    _ = 3 * Nat.totient 27 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 54 := by norm_num

@[simp] private theorem phi_82 : Nat.totient 82 = 40 := by
  calc
    Nat.totient 82 = Nat.totient (2 * 41) := by norm_num
    _ = (2 - 1) * Nat.totient 41 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 40 := by norm_num

@[simp] private theorem phi_83 : Nat.totient 83 = 82 := by
  calc
    Nat.totient 83 = Nat.totient (83 * 1) := by norm_num
    _ = (83 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 82 := by norm_num

@[simp] private theorem phi_84 : Nat.totient 84 = 24 := by
  calc
    Nat.totient 84 = Nat.totient (2 * 42) := by norm_num
    _ = 2 * Nat.totient 42 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_85 : Nat.totient 85 = 64 := by
  calc
    Nat.totient 85 = Nat.totient (5 * 17) := by norm_num
    _ = (5 - 1) * Nat.totient 17 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 64 := by norm_num

@[simp] private theorem phi_86 : Nat.totient 86 = 42 := by
  calc
    Nat.totient 86 = Nat.totient (2 * 43) := by norm_num
    _ = (2 - 1) * Nat.totient 43 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 42 := by norm_num

@[simp] private theorem phi_87 : Nat.totient 87 = 56 := by
  calc
    Nat.totient 87 = Nat.totient (3 * 29) := by norm_num
    _ = (3 - 1) * Nat.totient 29 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 56 := by norm_num

@[simp] private theorem phi_88 : Nat.totient 88 = 40 := by
  calc
    Nat.totient 88 = Nat.totient (2 * 44) := by norm_num
    _ = 2 * Nat.totient 44 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 40 := by norm_num

@[simp] private theorem phi_89 : Nat.totient 89 = 88 := by
  calc
    Nat.totient 89 = Nat.totient (89 * 1) := by norm_num
    _ = (89 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 88 := by norm_num

@[simp] private theorem phi_90 : Nat.totient 90 = 24 := by
  calc
    Nat.totient 90 = Nat.totient (2 * 45) := by norm_num
    _ = (2 - 1) * Nat.totient 45 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 24 := by norm_num

@[simp] private theorem phi_91 : Nat.totient 91 = 72 := by
  calc
    Nat.totient 91 = Nat.totient (7 * 13) := by norm_num
    _ = (7 - 1) * Nat.totient 13 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_92 : Nat.totient 92 = 44 := by
  calc
    Nat.totient 92 = Nat.totient (2 * 46) := by norm_num
    _ = 2 * Nat.totient 46 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 44 := by norm_num

@[simp] private theorem phi_93 : Nat.totient 93 = 60 := by
  calc
    Nat.totient 93 = Nat.totient (3 * 31) := by norm_num
    _ = (3 - 1) * Nat.totient 31 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 60 := by norm_num

@[simp] private theorem phi_94 : Nat.totient 94 = 46 := by
  calc
    Nat.totient 94 = Nat.totient (2 * 47) := by norm_num
    _ = (2 - 1) * Nat.totient 47 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 46 := by norm_num

@[simp] private theorem phi_95 : Nat.totient 95 = 72 := by
  calc
    Nat.totient 95 = Nat.totient (5 * 19) := by norm_num
    _ = (5 - 1) * Nat.totient 19 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_96 : Nat.totient 96 = 32 := by
  calc
    Nat.totient 96 = Nat.totient (2 * 48) := by norm_num
    _ = 2 * Nat.totient 48 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 32 := by norm_num

@[simp] private theorem phi_97 : Nat.totient 97 = 96 := by
  calc
    Nat.totient 97 = Nat.totient (97 * 1) := by norm_num
    _ = (97 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_98 : Nat.totient 98 = 42 := by
  calc
    Nat.totient 98 = Nat.totient (2 * 49) := by norm_num
    _ = (2 - 1) * Nat.totient 49 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 42 := by norm_num

@[simp] private theorem phi_99 : Nat.totient 99 = 60 := by
  calc
    Nat.totient 99 = Nat.totient (3 * 33) := by norm_num
    _ = 3 * Nat.totient 33 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 60 := by norm_num

@[simp] private theorem phi_100 : Nat.totient 100 = 40 := by
  calc
    Nat.totient 100 = Nat.totient (2 * 50) := by norm_num
    _ = 2 * Nat.totient 50 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 40 := by norm_num

@[simp] private theorem phi_101 : Nat.totient 101 = 100 := by
  calc
    Nat.totient 101 = Nat.totient (101 * 1) := by norm_num
    _ = (101 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 100 := by norm_num

@[simp] private theorem phi_102 : Nat.totient 102 = 32 := by
  calc
    Nat.totient 102 = Nat.totient (2 * 51) := by norm_num
    _ = (2 - 1) * Nat.totient 51 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 32 := by norm_num

@[simp] private theorem phi_103 : Nat.totient 103 = 102 := by
  calc
    Nat.totient 103 = Nat.totient (103 * 1) := by norm_num
    _ = (103 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 102 := by norm_num

@[simp] private theorem phi_104 : Nat.totient 104 = 48 := by
  calc
    Nat.totient 104 = Nat.totient (2 * 52) := by norm_num
    _ = 2 * Nat.totient 52 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_105 : Nat.totient 105 = 48 := by
  calc
    Nat.totient 105 = Nat.totient (3 * 35) := by norm_num
    _ = (3 - 1) * Nat.totient 35 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_106 : Nat.totient 106 = 52 := by
  calc
    Nat.totient 106 = Nat.totient (2 * 53) := by norm_num
    _ = (2 - 1) * Nat.totient 53 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 52 := by norm_num

@[simp] private theorem phi_107 : Nat.totient 107 = 106 := by
  calc
    Nat.totient 107 = Nat.totient (107 * 1) := by norm_num
    _ = (107 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 106 := by norm_num

@[simp] private theorem phi_108 : Nat.totient 108 = 36 := by
  calc
    Nat.totient 108 = Nat.totient (2 * 54) := by norm_num
    _ = 2 * Nat.totient 54 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 36 := by norm_num

@[simp] private theorem phi_109 : Nat.totient 109 = 108 := by
  calc
    Nat.totient 109 = Nat.totient (109 * 1) := by norm_num
    _ = (109 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 108 := by norm_num

@[simp] private theorem phi_110 : Nat.totient 110 = 40 := by
  calc
    Nat.totient 110 = Nat.totient (2 * 55) := by norm_num
    _ = (2 - 1) * Nat.totient 55 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 40 := by norm_num

@[simp] private theorem phi_111 : Nat.totient 111 = 72 := by
  calc
    Nat.totient 111 = Nat.totient (3 * 37) := by norm_num
    _ = (3 - 1) * Nat.totient 37 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_112 : Nat.totient 112 = 48 := by
  calc
    Nat.totient 112 = Nat.totient (2 * 56) := by norm_num
    _ = 2 * Nat.totient 56 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_113 : Nat.totient 113 = 112 := by
  calc
    Nat.totient 113 = Nat.totient (113 * 1) := by norm_num
    _ = (113 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 112 := by norm_num

@[simp] private theorem phi_114 : Nat.totient 114 = 36 := by
  calc
    Nat.totient 114 = Nat.totient (2 * 57) := by norm_num
    _ = (2 - 1) * Nat.totient 57 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 36 := by norm_num

@[simp] private theorem phi_115 : Nat.totient 115 = 88 := by
  calc
    Nat.totient 115 = Nat.totient (5 * 23) := by norm_num
    _ = (5 - 1) * Nat.totient 23 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 88 := by norm_num

@[simp] private theorem phi_116 : Nat.totient 116 = 56 := by
  calc
    Nat.totient 116 = Nat.totient (2 * 58) := by norm_num
    _ = 2 * Nat.totient 58 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 56 := by norm_num

@[simp] private theorem phi_117 : Nat.totient 117 = 72 := by
  calc
    Nat.totient 117 = Nat.totient (3 * 39) := by norm_num
    _ = 3 * Nat.totient 39 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_118 : Nat.totient 118 = 58 := by
  calc
    Nat.totient 118 = Nat.totient (2 * 59) := by norm_num
    _ = (2 - 1) * Nat.totient 59 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 58 := by norm_num

@[simp] private theorem phi_119 : Nat.totient 119 = 96 := by
  calc
    Nat.totient 119 = Nat.totient (7 * 17) := by norm_num
    _ = (7 - 1) * Nat.totient 17 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_120 : Nat.totient 120 = 32 := by
  calc
    Nat.totient 120 = Nat.totient (2 * 60) := by norm_num
    _ = 2 * Nat.totient 60 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 32 := by norm_num

@[simp] private theorem phi_121 : Nat.totient 121 = 110 := by
  calc
    Nat.totient 121 = Nat.totient (11 * 11) := by norm_num
    _ = 11 * Nat.totient 11 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 110 := by norm_num

@[simp] private theorem phi_122 : Nat.totient 122 = 60 := by
  calc
    Nat.totient 122 = Nat.totient (2 * 61) := by norm_num
    _ = (2 - 1) * Nat.totient 61 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 60 := by norm_num

@[simp] private theorem phi_123 : Nat.totient 123 = 80 := by
  calc
    Nat.totient 123 = Nat.totient (3 * 41) := by norm_num
    _ = (3 - 1) * Nat.totient 41 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_124 : Nat.totient 124 = 60 := by
  calc
    Nat.totient 124 = Nat.totient (2 * 62) := by norm_num
    _ = 2 * Nat.totient 62 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 60 := by norm_num

@[simp] private theorem phi_125 : Nat.totient 125 = 100 := by
  calc
    Nat.totient 125 = Nat.totient (5 * 25) := by norm_num
    _ = 5 * Nat.totient 25 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 100 := by norm_num

@[simp] private theorem phi_126 : Nat.totient 126 = 36 := by
  calc
    Nat.totient 126 = Nat.totient (2 * 63) := by norm_num
    _ = (2 - 1) * Nat.totient 63 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 36 := by norm_num

@[simp] private theorem phi_127 : Nat.totient 127 = 126 := by
  calc
    Nat.totient 127 = Nat.totient (127 * 1) := by norm_num
    _ = (127 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 126 := by norm_num

@[simp] private theorem phi_128 : Nat.totient 128 = 64 := by
  calc
    Nat.totient 128 = Nat.totient (2 * 64) := by norm_num
    _ = 2 * Nat.totient 64 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 64 := by norm_num

@[simp] private theorem phi_129 : Nat.totient 129 = 84 := by
  calc
    Nat.totient 129 = Nat.totient (3 * 43) := by norm_num
    _ = (3 - 1) * Nat.totient 43 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 84 := by norm_num

@[simp] private theorem phi_130 : Nat.totient 130 = 48 := by
  calc
    Nat.totient 130 = Nat.totient (2 * 65) := by norm_num
    _ = (2 - 1) * Nat.totient 65 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_131 : Nat.totient 131 = 130 := by
  calc
    Nat.totient 131 = Nat.totient (131 * 1) := by norm_num
    _ = (131 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 130 := by norm_num

@[simp] private theorem phi_132 : Nat.totient 132 = 40 := by
  calc
    Nat.totient 132 = Nat.totient (2 * 66) := by norm_num
    _ = 2 * Nat.totient 66 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 40 := by norm_num

@[simp] private theorem phi_133 : Nat.totient 133 = 108 := by
  calc
    Nat.totient 133 = Nat.totient (7 * 19) := by norm_num
    _ = (7 - 1) * Nat.totient 19 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 108 := by norm_num

@[simp] private theorem phi_134 : Nat.totient 134 = 66 := by
  calc
    Nat.totient 134 = Nat.totient (2 * 67) := by norm_num
    _ = (2 - 1) * Nat.totient 67 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 66 := by norm_num

@[simp] private theorem phi_135 : Nat.totient 135 = 72 := by
  calc
    Nat.totient 135 = Nat.totient (3 * 45) := by norm_num
    _ = 3 * Nat.totient 45 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_136 : Nat.totient 136 = 64 := by
  calc
    Nat.totient 136 = Nat.totient (2 * 68) := by norm_num
    _ = 2 * Nat.totient 68 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 64 := by norm_num

@[simp] private theorem phi_137 : Nat.totient 137 = 136 := by
  calc
    Nat.totient 137 = Nat.totient (137 * 1) := by norm_num
    _ = (137 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 136 := by norm_num

@[simp] private theorem phi_138 : Nat.totient 138 = 44 := by
  calc
    Nat.totient 138 = Nat.totient (2 * 69) := by norm_num
    _ = (2 - 1) * Nat.totient 69 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 44 := by norm_num

@[simp] private theorem phi_139 : Nat.totient 139 = 138 := by
  calc
    Nat.totient 139 = Nat.totient (139 * 1) := by norm_num
    _ = (139 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 138 := by norm_num

@[simp] private theorem phi_140 : Nat.totient 140 = 48 := by
  calc
    Nat.totient 140 = Nat.totient (2 * 70) := by norm_num
    _ = 2 * Nat.totient 70 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_141 : Nat.totient 141 = 92 := by
  calc
    Nat.totient 141 = Nat.totient (3 * 47) := by norm_num
    _ = (3 - 1) * Nat.totient 47 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 92 := by norm_num

@[simp] private theorem phi_142 : Nat.totient 142 = 70 := by
  calc
    Nat.totient 142 = Nat.totient (2 * 71) := by norm_num
    _ = (2 - 1) * Nat.totient 71 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 70 := by norm_num

@[simp] private theorem phi_143 : Nat.totient 143 = 120 := by
  calc
    Nat.totient 143 = Nat.totient (11 * 13) := by norm_num
    _ = (11 - 1) * Nat.totient 13 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_144 : Nat.totient 144 = 48 := by
  calc
    Nat.totient 144 = Nat.totient (2 * 72) := by norm_num
    _ = 2 * Nat.totient 72 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_145 : Nat.totient 145 = 112 := by
  calc
    Nat.totient 145 = Nat.totient (5 * 29) := by norm_num
    _ = (5 - 1) * Nat.totient 29 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 112 := by norm_num

@[simp] private theorem phi_146 : Nat.totient 146 = 72 := by
  calc
    Nat.totient 146 = Nat.totient (2 * 73) := by norm_num
    _ = (2 - 1) * Nat.totient 73 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_147 : Nat.totient 147 = 84 := by
  calc
    Nat.totient 147 = Nat.totient (3 * 49) := by norm_num
    _ = (3 - 1) * Nat.totient 49 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 84 := by norm_num

@[simp] private theorem phi_148 : Nat.totient 148 = 72 := by
  calc
    Nat.totient 148 = Nat.totient (2 * 74) := by norm_num
    _ = 2 * Nat.totient 74 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_149 : Nat.totient 149 = 148 := by
  calc
    Nat.totient 149 = Nat.totient (149 * 1) := by norm_num
    _ = (149 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 148 := by norm_num

@[simp] private theorem phi_150 : Nat.totient 150 = 40 := by
  calc
    Nat.totient 150 = Nat.totient (2 * 75) := by norm_num
    _ = (2 - 1) * Nat.totient 75 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 40 := by norm_num

@[simp] private theorem phi_151 : Nat.totient 151 = 150 := by
  calc
    Nat.totient 151 = Nat.totient (151 * 1) := by norm_num
    _ = (151 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 150 := by norm_num

@[simp] private theorem phi_152 : Nat.totient 152 = 72 := by
  calc
    Nat.totient 152 = Nat.totient (2 * 76) := by norm_num
    _ = 2 * Nat.totient 76 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_153 : Nat.totient 153 = 96 := by
  calc
    Nat.totient 153 = Nat.totient (3 * 51) := by norm_num
    _ = 3 * Nat.totient 51 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_154 : Nat.totient 154 = 60 := by
  calc
    Nat.totient 154 = Nat.totient (2 * 77) := by norm_num
    _ = (2 - 1) * Nat.totient 77 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 60 := by norm_num

@[simp] private theorem phi_155 : Nat.totient 155 = 120 := by
  calc
    Nat.totient 155 = Nat.totient (5 * 31) := by norm_num
    _ = (5 - 1) * Nat.totient 31 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_156 : Nat.totient 156 = 48 := by
  calc
    Nat.totient 156 = Nat.totient (2 * 78) := by norm_num
    _ = 2 * Nat.totient 78 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_157 : Nat.totient 157 = 156 := by
  calc
    Nat.totient 157 = Nat.totient (157 * 1) := by norm_num
    _ = (157 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 156 := by norm_num

@[simp] private theorem phi_158 : Nat.totient 158 = 78 := by
  calc
    Nat.totient 158 = Nat.totient (2 * 79) := by norm_num
    _ = (2 - 1) * Nat.totient 79 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 78 := by norm_num

@[simp] private theorem phi_159 : Nat.totient 159 = 104 := by
  calc
    Nat.totient 159 = Nat.totient (3 * 53) := by norm_num
    _ = (3 - 1) * Nat.totient 53 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 104 := by norm_num

@[simp] private theorem phi_160 : Nat.totient 160 = 64 := by
  calc
    Nat.totient 160 = Nat.totient (2 * 80) := by norm_num
    _ = 2 * Nat.totient 80 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 64 := by norm_num

@[simp] private theorem phi_161 : Nat.totient 161 = 132 := by
  calc
    Nat.totient 161 = Nat.totient (7 * 23) := by norm_num
    _ = (7 - 1) * Nat.totient 23 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 132 := by norm_num

@[simp] private theorem phi_162 : Nat.totient 162 = 54 := by
  calc
    Nat.totient 162 = Nat.totient (2 * 81) := by norm_num
    _ = (2 - 1) * Nat.totient 81 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 54 := by norm_num

@[simp] private theorem phi_163 : Nat.totient 163 = 162 := by
  calc
    Nat.totient 163 = Nat.totient (163 * 1) := by norm_num
    _ = (163 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 162 := by norm_num

@[simp] private theorem phi_164 : Nat.totient 164 = 80 := by
  calc
    Nat.totient 164 = Nat.totient (2 * 82) := by norm_num
    _ = 2 * Nat.totient 82 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_165 : Nat.totient 165 = 80 := by
  calc
    Nat.totient 165 = Nat.totient (3 * 55) := by norm_num
    _ = (3 - 1) * Nat.totient 55 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_166 : Nat.totient 166 = 82 := by
  calc
    Nat.totient 166 = Nat.totient (2 * 83) := by norm_num
    _ = (2 - 1) * Nat.totient 83 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 82 := by norm_num

@[simp] private theorem phi_167 : Nat.totient 167 = 166 := by
  calc
    Nat.totient 167 = Nat.totient (167 * 1) := by norm_num
    _ = (167 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 166 := by norm_num

@[simp] private theorem phi_168 : Nat.totient 168 = 48 := by
  calc
    Nat.totient 168 = Nat.totient (2 * 84) := by norm_num
    _ = 2 * Nat.totient 84 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_169 : Nat.totient 169 = 156 := by
  calc
    Nat.totient 169 = Nat.totient (13 * 13) := by norm_num
    _ = 13 * Nat.totient 13 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 156 := by norm_num

@[simp] private theorem phi_170 : Nat.totient 170 = 64 := by
  calc
    Nat.totient 170 = Nat.totient (2 * 85) := by norm_num
    _ = (2 - 1) * Nat.totient 85 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 64 := by norm_num

@[simp] private theorem phi_171 : Nat.totient 171 = 108 := by
  calc
    Nat.totient 171 = Nat.totient (3 * 57) := by norm_num
    _ = 3 * Nat.totient 57 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 108 := by norm_num

@[simp] private theorem phi_172 : Nat.totient 172 = 84 := by
  calc
    Nat.totient 172 = Nat.totient (2 * 86) := by norm_num
    _ = 2 * Nat.totient 86 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 84 := by norm_num

@[simp] private theorem phi_173 : Nat.totient 173 = 172 := by
  calc
    Nat.totient 173 = Nat.totient (173 * 1) := by norm_num
    _ = (173 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 172 := by norm_num

@[simp] private theorem phi_174 : Nat.totient 174 = 56 := by
  calc
    Nat.totient 174 = Nat.totient (2 * 87) := by norm_num
    _ = (2 - 1) * Nat.totient 87 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 56 := by norm_num

@[simp] private theorem phi_175 : Nat.totient 175 = 120 := by
  calc
    Nat.totient 175 = Nat.totient (5 * 35) := by norm_num
    _ = 5 * Nat.totient 35 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_176 : Nat.totient 176 = 80 := by
  calc
    Nat.totient 176 = Nat.totient (2 * 88) := by norm_num
    _ = 2 * Nat.totient 88 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_177 : Nat.totient 177 = 116 := by
  calc
    Nat.totient 177 = Nat.totient (3 * 59) := by norm_num
    _ = (3 - 1) * Nat.totient 59 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 116 := by norm_num

@[simp] private theorem phi_178 : Nat.totient 178 = 88 := by
  calc
    Nat.totient 178 = Nat.totient (2 * 89) := by norm_num
    _ = (2 - 1) * Nat.totient 89 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 88 := by norm_num

@[simp] private theorem phi_179 : Nat.totient 179 = 178 := by
  calc
    Nat.totient 179 = Nat.totient (179 * 1) := by norm_num
    _ = (179 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 178 := by norm_num

@[simp] private theorem phi_180 : Nat.totient 180 = 48 := by
  calc
    Nat.totient 180 = Nat.totient (2 * 90) := by norm_num
    _ = 2 * Nat.totient 90 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_181 : Nat.totient 181 = 180 := by
  calc
    Nat.totient 181 = Nat.totient (181 * 1) := by norm_num
    _ = (181 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_182 : Nat.totient 182 = 72 := by
  calc
    Nat.totient 182 = Nat.totient (2 * 91) := by norm_num
    _ = (2 - 1) * Nat.totient 91 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_183 : Nat.totient 183 = 120 := by
  calc
    Nat.totient 183 = Nat.totient (3 * 61) := by norm_num
    _ = (3 - 1) * Nat.totient 61 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_184 : Nat.totient 184 = 88 := by
  calc
    Nat.totient 184 = Nat.totient (2 * 92) := by norm_num
    _ = 2 * Nat.totient 92 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 88 := by norm_num

@[simp] private theorem phi_185 : Nat.totient 185 = 144 := by
  calc
    Nat.totient 185 = Nat.totient (5 * 37) := by norm_num
    _ = (5 - 1) * Nat.totient 37 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_186 : Nat.totient 186 = 60 := by
  calc
    Nat.totient 186 = Nat.totient (2 * 93) := by norm_num
    _ = (2 - 1) * Nat.totient 93 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 60 := by norm_num

@[simp] private theorem phi_187 : Nat.totient 187 = 160 := by
  calc
    Nat.totient 187 = Nat.totient (11 * 17) := by norm_num
    _ = (11 - 1) * Nat.totient 17 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_188 : Nat.totient 188 = 92 := by
  calc
    Nat.totient 188 = Nat.totient (2 * 94) := by norm_num
    _ = 2 * Nat.totient 94 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 92 := by norm_num

@[simp] private theorem phi_189 : Nat.totient 189 = 108 := by
  calc
    Nat.totient 189 = Nat.totient (3 * 63) := by norm_num
    _ = 3 * Nat.totient 63 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 108 := by norm_num

@[simp] private theorem phi_190 : Nat.totient 190 = 72 := by
  calc
    Nat.totient 190 = Nat.totient (2 * 95) := by norm_num
    _ = (2 - 1) * Nat.totient 95 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_191 : Nat.totient 191 = 190 := by
  calc
    Nat.totient 191 = Nat.totient (191 * 1) := by norm_num
    _ = (191 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 190 := by norm_num

@[simp] private theorem phi_192 : Nat.totient 192 = 64 := by
  calc
    Nat.totient 192 = Nat.totient (2 * 96) := by norm_num
    _ = 2 * Nat.totient 96 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 64 := by norm_num

@[simp] private theorem phi_193 : Nat.totient 193 = 192 := by
  calc
    Nat.totient 193 = Nat.totient (193 * 1) := by norm_num
    _ = (193 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_194 : Nat.totient 194 = 96 := by
  calc
    Nat.totient 194 = Nat.totient (2 * 97) := by norm_num
    _ = (2 - 1) * Nat.totient 97 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_195 : Nat.totient 195 = 96 := by
  calc
    Nat.totient 195 = Nat.totient (3 * 65) := by norm_num
    _ = (3 - 1) * Nat.totient 65 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_196 : Nat.totient 196 = 84 := by
  calc
    Nat.totient 196 = Nat.totient (2 * 98) := by norm_num
    _ = 2 * Nat.totient 98 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 84 := by norm_num

@[simp] private theorem phi_197 : Nat.totient 197 = 196 := by
  calc
    Nat.totient 197 = Nat.totient (197 * 1) := by norm_num
    _ = (197 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 196 := by norm_num

@[simp] private theorem phi_198 : Nat.totient 198 = 60 := by
  calc
    Nat.totient 198 = Nat.totient (2 * 99) := by norm_num
    _ = (2 - 1) * Nat.totient 99 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 60 := by norm_num

@[simp] private theorem phi_199 : Nat.totient 199 = 198 := by
  calc
    Nat.totient 199 = Nat.totient (199 * 1) := by norm_num
    _ = (199 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 198 := by norm_num

@[simp] private theorem phi_200 : Nat.totient 200 = 80 := by
  calc
    Nat.totient 200 = Nat.totient (2 * 100) := by norm_num
    _ = 2 * Nat.totient 100 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_201 : Nat.totient 201 = 132 := by
  calc
    Nat.totient 201 = Nat.totient (3 * 67) := by norm_num
    _ = (3 - 1) * Nat.totient 67 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 132 := by norm_num

@[simp] private theorem phi_202 : Nat.totient 202 = 100 := by
  calc
    Nat.totient 202 = Nat.totient (2 * 101) := by norm_num
    _ = (2 - 1) * Nat.totient 101 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 100 := by norm_num

@[simp] private theorem phi_203 : Nat.totient 203 = 168 := by
  calc
    Nat.totient 203 = Nat.totient (7 * 29) := by norm_num
    _ = (7 - 1) * Nat.totient 29 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_204 : Nat.totient 204 = 64 := by
  calc
    Nat.totient 204 = Nat.totient (2 * 102) := by norm_num
    _ = 2 * Nat.totient 102 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 64 := by norm_num

@[simp] private theorem phi_205 : Nat.totient 205 = 160 := by
  calc
    Nat.totient 205 = Nat.totient (5 * 41) := by norm_num
    _ = (5 - 1) * Nat.totient 41 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_206 : Nat.totient 206 = 102 := by
  calc
    Nat.totient 206 = Nat.totient (2 * 103) := by norm_num
    _ = (2 - 1) * Nat.totient 103 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 102 := by norm_num

@[simp] private theorem phi_207 : Nat.totient 207 = 132 := by
  calc
    Nat.totient 207 = Nat.totient (3 * 69) := by norm_num
    _ = 3 * Nat.totient 69 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 132 := by norm_num

@[simp] private theorem phi_208 : Nat.totient 208 = 96 := by
  calc
    Nat.totient 208 = Nat.totient (2 * 104) := by norm_num
    _ = 2 * Nat.totient 104 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_209 : Nat.totient 209 = 180 := by
  calc
    Nat.totient 209 = Nat.totient (11 * 19) := by norm_num
    _ = (11 - 1) * Nat.totient 19 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_210 : Nat.totient 210 = 48 := by
  calc
    Nat.totient 210 = Nat.totient (2 * 105) := by norm_num
    _ = (2 - 1) * Nat.totient 105 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 48 := by norm_num

@[simp] private theorem phi_211 : Nat.totient 211 = 210 := by
  calc
    Nat.totient 211 = Nat.totient (211 * 1) := by norm_num
    _ = (211 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 210 := by norm_num

@[simp] private theorem phi_212 : Nat.totient 212 = 104 := by
  calc
    Nat.totient 212 = Nat.totient (2 * 106) := by norm_num
    _ = 2 * Nat.totient 106 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 104 := by norm_num

@[simp] private theorem phi_213 : Nat.totient 213 = 140 := by
  calc
    Nat.totient 213 = Nat.totient (3 * 71) := by norm_num
    _ = (3 - 1) * Nat.totient 71 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 140 := by norm_num

@[simp] private theorem phi_214 : Nat.totient 214 = 106 := by
  calc
    Nat.totient 214 = Nat.totient (2 * 107) := by norm_num
    _ = (2 - 1) * Nat.totient 107 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 106 := by norm_num

@[simp] private theorem phi_215 : Nat.totient 215 = 168 := by
  calc
    Nat.totient 215 = Nat.totient (5 * 43) := by norm_num
    _ = (5 - 1) * Nat.totient 43 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_216 : Nat.totient 216 = 72 := by
  calc
    Nat.totient 216 = Nat.totient (2 * 108) := by norm_num
    _ = 2 * Nat.totient 108 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_217 : Nat.totient 217 = 180 := by
  calc
    Nat.totient 217 = Nat.totient (7 * 31) := by norm_num
    _ = (7 - 1) * Nat.totient 31 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_218 : Nat.totient 218 = 108 := by
  calc
    Nat.totient 218 = Nat.totient (2 * 109) := by norm_num
    _ = (2 - 1) * Nat.totient 109 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 108 := by norm_num

@[simp] private theorem phi_219 : Nat.totient 219 = 144 := by
  calc
    Nat.totient 219 = Nat.totient (3 * 73) := by norm_num
    _ = (3 - 1) * Nat.totient 73 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_220 : Nat.totient 220 = 80 := by
  calc
    Nat.totient 220 = Nat.totient (2 * 110) := by norm_num
    _ = 2 * Nat.totient 110 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_221 : Nat.totient 221 = 192 := by
  calc
    Nat.totient 221 = Nat.totient (13 * 17) := by norm_num
    _ = (13 - 1) * Nat.totient 17 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_222 : Nat.totient 222 = 72 := by
  calc
    Nat.totient 222 = Nat.totient (2 * 111) := by norm_num
    _ = (2 - 1) * Nat.totient 111 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_223 : Nat.totient 223 = 222 := by
  calc
    Nat.totient 223 = Nat.totient (223 * 1) := by norm_num
    _ = (223 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 222 := by norm_num

@[simp] private theorem phi_224 : Nat.totient 224 = 96 := by
  calc
    Nat.totient 224 = Nat.totient (2 * 112) := by norm_num
    _ = 2 * Nat.totient 112 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_225 : Nat.totient 225 = 120 := by
  calc
    Nat.totient 225 = Nat.totient (3 * 75) := by norm_num
    _ = 3 * Nat.totient 75 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_226 : Nat.totient 226 = 112 := by
  calc
    Nat.totient 226 = Nat.totient (2 * 113) := by norm_num
    _ = (2 - 1) * Nat.totient 113 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 112 := by norm_num

@[simp] private theorem phi_227 : Nat.totient 227 = 226 := by
  calc
    Nat.totient 227 = Nat.totient (227 * 1) := by norm_num
    _ = (227 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 226 := by norm_num

@[simp] private theorem phi_228 : Nat.totient 228 = 72 := by
  calc
    Nat.totient 228 = Nat.totient (2 * 114) := by norm_num
    _ = 2 * Nat.totient 114 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_229 : Nat.totient 229 = 228 := by
  calc
    Nat.totient 229 = Nat.totient (229 * 1) := by norm_num
    _ = (229 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 228 := by norm_num

@[simp] private theorem phi_230 : Nat.totient 230 = 88 := by
  calc
    Nat.totient 230 = Nat.totient (2 * 115) := by norm_num
    _ = (2 - 1) * Nat.totient 115 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 88 := by norm_num

@[simp] private theorem phi_231 : Nat.totient 231 = 120 := by
  calc
    Nat.totient 231 = Nat.totient (3 * 77) := by norm_num
    _ = (3 - 1) * Nat.totient 77 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_232 : Nat.totient 232 = 112 := by
  calc
    Nat.totient 232 = Nat.totient (2 * 116) := by norm_num
    _ = 2 * Nat.totient 116 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 112 := by norm_num

@[simp] private theorem phi_233 : Nat.totient 233 = 232 := by
  calc
    Nat.totient 233 = Nat.totient (233 * 1) := by norm_num
    _ = (233 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 232 := by norm_num

@[simp] private theorem phi_234 : Nat.totient 234 = 72 := by
  calc
    Nat.totient 234 = Nat.totient (2 * 117) := by norm_num
    _ = (2 - 1) * Nat.totient 117 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_235 : Nat.totient 235 = 184 := by
  calc
    Nat.totient 235 = Nat.totient (5 * 47) := by norm_num
    _ = (5 - 1) * Nat.totient 47 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 184 := by norm_num

@[simp] private theorem phi_236 : Nat.totient 236 = 116 := by
  calc
    Nat.totient 236 = Nat.totient (2 * 118) := by norm_num
    _ = 2 * Nat.totient 118 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 116 := by norm_num

@[simp] private theorem phi_237 : Nat.totient 237 = 156 := by
  calc
    Nat.totient 237 = Nat.totient (3 * 79) := by norm_num
    _ = (3 - 1) * Nat.totient 79 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 156 := by norm_num

@[simp] private theorem phi_238 : Nat.totient 238 = 96 := by
  calc
    Nat.totient 238 = Nat.totient (2 * 119) := by norm_num
    _ = (2 - 1) * Nat.totient 119 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_239 : Nat.totient 239 = 238 := by
  calc
    Nat.totient 239 = Nat.totient (239 * 1) := by norm_num
    _ = (239 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 238 := by norm_num

@[simp] private theorem phi_240 : Nat.totient 240 = 64 := by
  calc
    Nat.totient 240 = Nat.totient (2 * 120) := by norm_num
    _ = 2 * Nat.totient 120 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 64 := by norm_num

@[simp] private theorem phi_241 : Nat.totient 241 = 240 := by
  calc
    Nat.totient 241 = Nat.totient (241 * 1) := by norm_num
    _ = (241 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_242 : Nat.totient 242 = 110 := by
  calc
    Nat.totient 242 = Nat.totient (2 * 121) := by norm_num
    _ = (2 - 1) * Nat.totient 121 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 110 := by norm_num

@[simp] private theorem phi_243 : Nat.totient 243 = 162 := by
  calc
    Nat.totient 243 = Nat.totient (3 * 81) := by norm_num
    _ = 3 * Nat.totient 81 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 162 := by norm_num

@[simp] private theorem phi_244 : Nat.totient 244 = 120 := by
  calc
    Nat.totient 244 = Nat.totient (2 * 122) := by norm_num
    _ = 2 * Nat.totient 122 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_245 : Nat.totient 245 = 168 := by
  calc
    Nat.totient 245 = Nat.totient (5 * 49) := by norm_num
    _ = (5 - 1) * Nat.totient 49 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_246 : Nat.totient 246 = 80 := by
  calc
    Nat.totient 246 = Nat.totient (2 * 123) := by norm_num
    _ = (2 - 1) * Nat.totient 123 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_247 : Nat.totient 247 = 216 := by
  calc
    Nat.totient 247 = Nat.totient (13 * 19) := by norm_num
    _ = (13 - 1) * Nat.totient 19 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_248 : Nat.totient 248 = 120 := by
  calc
    Nat.totient 248 = Nat.totient (2 * 124) := by norm_num
    _ = 2 * Nat.totient 124 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_249 : Nat.totient 249 = 164 := by
  calc
    Nat.totient 249 = Nat.totient (3 * 83) := by norm_num
    _ = (3 - 1) * Nat.totient 83 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 164 := by norm_num

@[simp] private theorem phi_250 : Nat.totient 250 = 100 := by
  calc
    Nat.totient 250 = Nat.totient (2 * 125) := by norm_num
    _ = (2 - 1) * Nat.totient 125 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 100 := by norm_num

@[simp] private theorem phi_251 : Nat.totient 251 = 250 := by
  calc
    Nat.totient 251 = Nat.totient (251 * 1) := by norm_num
    _ = (251 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 250 := by norm_num

@[simp] private theorem phi_252 : Nat.totient 252 = 72 := by
  calc
    Nat.totient 252 = Nat.totient (2 * 126) := by norm_num
    _ = 2 * Nat.totient 126 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_253 : Nat.totient 253 = 220 := by
  calc
    Nat.totient 253 = Nat.totient (11 * 23) := by norm_num
    _ = (11 - 1) * Nat.totient 23 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 220 := by norm_num

@[simp] private theorem phi_254 : Nat.totient 254 = 126 := by
  calc
    Nat.totient 254 = Nat.totient (2 * 127) := by norm_num
    _ = (2 - 1) * Nat.totient 127 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 126 := by norm_num

@[simp] private theorem phi_255 : Nat.totient 255 = 128 := by
  calc
    Nat.totient 255 = Nat.totient (3 * 85) := by norm_num
    _ = (3 - 1) * Nat.totient 85 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 128 := by norm_num

@[simp] private theorem phi_256 : Nat.totient 256 = 128 := by
  calc
    Nat.totient 256 = Nat.totient (2 * 128) := by norm_num
    _ = 2 * Nat.totient 128 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 128 := by norm_num

@[simp] private theorem phi_257 : Nat.totient 257 = 256 := by
  calc
    Nat.totient 257 = Nat.totient (257 * 1) := by norm_num
    _ = (257 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 256 := by norm_num

@[simp] private theorem phi_258 : Nat.totient 258 = 84 := by
  calc
    Nat.totient 258 = Nat.totient (2 * 129) := by norm_num
    _ = (2 - 1) * Nat.totient 129 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 84 := by norm_num

@[simp] private theorem phi_259 : Nat.totient 259 = 216 := by
  calc
    Nat.totient 259 = Nat.totient (7 * 37) := by norm_num
    _ = (7 - 1) * Nat.totient 37 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_260 : Nat.totient 260 = 96 := by
  calc
    Nat.totient 260 = Nat.totient (2 * 130) := by norm_num
    _ = 2 * Nat.totient 130 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_261 : Nat.totient 261 = 168 := by
  calc
    Nat.totient 261 = Nat.totient (3 * 87) := by norm_num
    _ = 3 * Nat.totient 87 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_262 : Nat.totient 262 = 130 := by
  calc
    Nat.totient 262 = Nat.totient (2 * 131) := by norm_num
    _ = (2 - 1) * Nat.totient 131 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 130 := by norm_num

@[simp] private theorem phi_263 : Nat.totient 263 = 262 := by
  calc
    Nat.totient 263 = Nat.totient (263 * 1) := by norm_num
    _ = (263 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 262 := by norm_num

@[simp] private theorem phi_264 : Nat.totient 264 = 80 := by
  calc
    Nat.totient 264 = Nat.totient (2 * 132) := by norm_num
    _ = 2 * Nat.totient 132 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_265 : Nat.totient 265 = 208 := by
  calc
    Nat.totient 265 = Nat.totient (5 * 53) := by norm_num
    _ = (5 - 1) * Nat.totient 53 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 208 := by norm_num

@[simp] private theorem phi_266 : Nat.totient 266 = 108 := by
  calc
    Nat.totient 266 = Nat.totient (2 * 133) := by norm_num
    _ = (2 - 1) * Nat.totient 133 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 108 := by norm_num

@[simp] private theorem phi_267 : Nat.totient 267 = 176 := by
  calc
    Nat.totient 267 = Nat.totient (3 * 89) := by norm_num
    _ = (3 - 1) * Nat.totient 89 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 176 := by norm_num

@[simp] private theorem phi_268 : Nat.totient 268 = 132 := by
  calc
    Nat.totient 268 = Nat.totient (2 * 134) := by norm_num
    _ = 2 * Nat.totient 134 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 132 := by norm_num

@[simp] private theorem phi_269 : Nat.totient 269 = 268 := by
  calc
    Nat.totient 269 = Nat.totient (269 * 1) := by norm_num
    _ = (269 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 268 := by norm_num

@[simp] private theorem phi_270 : Nat.totient 270 = 72 := by
  calc
    Nat.totient 270 = Nat.totient (2 * 135) := by norm_num
    _ = (2 - 1) * Nat.totient 135 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 72 := by norm_num

@[simp] private theorem phi_271 : Nat.totient 271 = 270 := by
  calc
    Nat.totient 271 = Nat.totient (271 * 1) := by norm_num
    _ = (271 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 270 := by norm_num

@[simp] private theorem phi_272 : Nat.totient 272 = 128 := by
  calc
    Nat.totient 272 = Nat.totient (2 * 136) := by norm_num
    _ = 2 * Nat.totient 136 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 128 := by norm_num

@[simp] private theorem phi_273 : Nat.totient 273 = 144 := by
  calc
    Nat.totient 273 = Nat.totient (3 * 91) := by norm_num
    _ = (3 - 1) * Nat.totient 91 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_274 : Nat.totient 274 = 136 := by
  calc
    Nat.totient 274 = Nat.totient (2 * 137) := by norm_num
    _ = (2 - 1) * Nat.totient 137 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 136 := by norm_num

@[simp] private theorem phi_275 : Nat.totient 275 = 200 := by
  calc
    Nat.totient 275 = Nat.totient (5 * 55) := by norm_num
    _ = 5 * Nat.totient 55 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 200 := by norm_num

@[simp] private theorem phi_276 : Nat.totient 276 = 88 := by
  calc
    Nat.totient 276 = Nat.totient (2 * 138) := by norm_num
    _ = 2 * Nat.totient 138 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 88 := by norm_num

@[simp] private theorem phi_277 : Nat.totient 277 = 276 := by
  calc
    Nat.totient 277 = Nat.totient (277 * 1) := by norm_num
    _ = (277 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 276 := by norm_num

@[simp] private theorem phi_278 : Nat.totient 278 = 138 := by
  calc
    Nat.totient 278 = Nat.totient (2 * 139) := by norm_num
    _ = (2 - 1) * Nat.totient 139 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 138 := by norm_num

@[simp] private theorem phi_279 : Nat.totient 279 = 180 := by
  calc
    Nat.totient 279 = Nat.totient (3 * 93) := by norm_num
    _ = 3 * Nat.totient 93 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_280 : Nat.totient 280 = 96 := by
  calc
    Nat.totient 280 = Nat.totient (2 * 140) := by norm_num
    _ = 2 * Nat.totient 140 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_281 : Nat.totient 281 = 280 := by
  calc
    Nat.totient 281 = Nat.totient (281 * 1) := by norm_num
    _ = (281 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 280 := by norm_num

@[simp] private theorem phi_282 : Nat.totient 282 = 92 := by
  calc
    Nat.totient 282 = Nat.totient (2 * 141) := by norm_num
    _ = (2 - 1) * Nat.totient 141 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 92 := by norm_num

@[simp] private theorem phi_283 : Nat.totient 283 = 282 := by
  calc
    Nat.totient 283 = Nat.totient (283 * 1) := by norm_num
    _ = (283 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 282 := by norm_num

@[simp] private theorem phi_284 : Nat.totient 284 = 140 := by
  calc
    Nat.totient 284 = Nat.totient (2 * 142) := by norm_num
    _ = 2 * Nat.totient 142 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 140 := by norm_num

@[simp] private theorem phi_285 : Nat.totient 285 = 144 := by
  calc
    Nat.totient 285 = Nat.totient (3 * 95) := by norm_num
    _ = (3 - 1) * Nat.totient 95 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_286 : Nat.totient 286 = 120 := by
  calc
    Nat.totient 286 = Nat.totient (2 * 143) := by norm_num
    _ = (2 - 1) * Nat.totient 143 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_287 : Nat.totient 287 = 240 := by
  calc
    Nat.totient 287 = Nat.totient (7 * 41) := by norm_num
    _ = (7 - 1) * Nat.totient 41 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_288 : Nat.totient 288 = 96 := by
  calc
    Nat.totient 288 = Nat.totient (2 * 144) := by norm_num
    _ = 2 * Nat.totient 144 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_289 : Nat.totient 289 = 272 := by
  calc
    Nat.totient 289 = Nat.totient (17 * 17) := by norm_num
    _ = 17 * Nat.totient 17 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 272 := by norm_num

@[simp] private theorem phi_290 : Nat.totient 290 = 112 := by
  calc
    Nat.totient 290 = Nat.totient (2 * 145) := by norm_num
    _ = (2 - 1) * Nat.totient 145 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 112 := by norm_num

@[simp] private theorem phi_291 : Nat.totient 291 = 192 := by
  calc
    Nat.totient 291 = Nat.totient (3 * 97) := by norm_num
    _ = (3 - 1) * Nat.totient 97 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_292 : Nat.totient 292 = 144 := by
  calc
    Nat.totient 292 = Nat.totient (2 * 146) := by norm_num
    _ = 2 * Nat.totient 146 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_293 : Nat.totient 293 = 292 := by
  calc
    Nat.totient 293 = Nat.totient (293 * 1) := by norm_num
    _ = (293 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 292 := by norm_num

@[simp] private theorem phi_294 : Nat.totient 294 = 84 := by
  calc
    Nat.totient 294 = Nat.totient (2 * 147) := by norm_num
    _ = (2 - 1) * Nat.totient 147 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 84 := by norm_num

@[simp] private theorem phi_295 : Nat.totient 295 = 232 := by
  calc
    Nat.totient 295 = Nat.totient (5 * 59) := by norm_num
    _ = (5 - 1) * Nat.totient 59 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 232 := by norm_num

@[simp] private theorem phi_296 : Nat.totient 296 = 144 := by
  calc
    Nat.totient 296 = Nat.totient (2 * 148) := by norm_num
    _ = 2 * Nat.totient 148 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_297 : Nat.totient 297 = 180 := by
  calc
    Nat.totient 297 = Nat.totient (3 * 99) := by norm_num
    _ = 3 * Nat.totient 99 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_298 : Nat.totient 298 = 148 := by
  calc
    Nat.totient 298 = Nat.totient (2 * 149) := by norm_num
    _ = (2 - 1) * Nat.totient 149 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 148 := by norm_num

@[simp] private theorem phi_299 : Nat.totient 299 = 264 := by
  calc
    Nat.totient 299 = Nat.totient (13 * 23) := by norm_num
    _ = (13 - 1) * Nat.totient 23 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 264 := by norm_num

@[simp] private theorem phi_300 : Nat.totient 300 = 80 := by
  calc
    Nat.totient 300 = Nat.totient (2 * 150) := by norm_num
    _ = 2 * Nat.totient 150 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_301 : Nat.totient 301 = 252 := by
  calc
    Nat.totient 301 = Nat.totient (7 * 43) := by norm_num
    _ = (7 - 1) * Nat.totient 43 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 252 := by norm_num

@[simp] private theorem phi_302 : Nat.totient 302 = 150 := by
  calc
    Nat.totient 302 = Nat.totient (2 * 151) := by norm_num
    _ = (2 - 1) * Nat.totient 151 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 150 := by norm_num

@[simp] private theorem phi_303 : Nat.totient 303 = 200 := by
  calc
    Nat.totient 303 = Nat.totient (3 * 101) := by norm_num
    _ = (3 - 1) * Nat.totient 101 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 200 := by norm_num

@[simp] private theorem phi_304 : Nat.totient 304 = 144 := by
  calc
    Nat.totient 304 = Nat.totient (2 * 152) := by norm_num
    _ = 2 * Nat.totient 152 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_305 : Nat.totient 305 = 240 := by
  calc
    Nat.totient 305 = Nat.totient (5 * 61) := by norm_num
    _ = (5 - 1) * Nat.totient 61 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_306 : Nat.totient 306 = 96 := by
  calc
    Nat.totient 306 = Nat.totient (2 * 153) := by norm_num
    _ = (2 - 1) * Nat.totient 153 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_307 : Nat.totient 307 = 306 := by
  calc
    Nat.totient 307 = Nat.totient (307 * 1) := by norm_num
    _ = (307 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 306 := by norm_num

@[simp] private theorem phi_308 : Nat.totient 308 = 120 := by
  calc
    Nat.totient 308 = Nat.totient (2 * 154) := by norm_num
    _ = 2 * Nat.totient 154 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_309 : Nat.totient 309 = 204 := by
  calc
    Nat.totient 309 = Nat.totient (3 * 103) := by norm_num
    _ = (3 - 1) * Nat.totient 103 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 204 := by norm_num

@[simp] private theorem phi_310 : Nat.totient 310 = 120 := by
  calc
    Nat.totient 310 = Nat.totient (2 * 155) := by norm_num
    _ = (2 - 1) * Nat.totient 155 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_311 : Nat.totient 311 = 310 := by
  calc
    Nat.totient 311 = Nat.totient (311 * 1) := by norm_num
    _ = (311 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 310 := by norm_num

@[simp] private theorem phi_312 : Nat.totient 312 = 96 := by
  calc
    Nat.totient 312 = Nat.totient (2 * 156) := by norm_num
    _ = 2 * Nat.totient 156 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_313 : Nat.totient 313 = 312 := by
  calc
    Nat.totient 313 = Nat.totient (313 * 1) := by norm_num
    _ = (313 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_314 : Nat.totient 314 = 156 := by
  calc
    Nat.totient 314 = Nat.totient (2 * 157) := by norm_num
    _ = (2 - 1) * Nat.totient 157 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 156 := by norm_num

@[simp] private theorem phi_315 : Nat.totient 315 = 144 := by
  calc
    Nat.totient 315 = Nat.totient (3 * 105) := by norm_num
    _ = 3 * Nat.totient 105 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_316 : Nat.totient 316 = 156 := by
  calc
    Nat.totient 316 = Nat.totient (2 * 158) := by norm_num
    _ = 2 * Nat.totient 158 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 156 := by norm_num

@[simp] private theorem phi_317 : Nat.totient 317 = 316 := by
  calc
    Nat.totient 317 = Nat.totient (317 * 1) := by norm_num
    _ = (317 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 316 := by norm_num

@[simp] private theorem phi_318 : Nat.totient 318 = 104 := by
  calc
    Nat.totient 318 = Nat.totient (2 * 159) := by norm_num
    _ = (2 - 1) * Nat.totient 159 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 104 := by norm_num

@[simp] private theorem phi_319 : Nat.totient 319 = 280 := by
  calc
    Nat.totient 319 = Nat.totient (11 * 29) := by norm_num
    _ = (11 - 1) * Nat.totient 29 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 280 := by norm_num

@[simp] private theorem phi_320 : Nat.totient 320 = 128 := by
  calc
    Nat.totient 320 = Nat.totient (2 * 160) := by norm_num
    _ = 2 * Nat.totient 160 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 128 := by norm_num

@[simp] private theorem phi_321 : Nat.totient 321 = 212 := by
  calc
    Nat.totient 321 = Nat.totient (3 * 107) := by norm_num
    _ = (3 - 1) * Nat.totient 107 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 212 := by norm_num

@[simp] private theorem phi_322 : Nat.totient 322 = 132 := by
  calc
    Nat.totient 322 = Nat.totient (2 * 161) := by norm_num
    _ = (2 - 1) * Nat.totient 161 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 132 := by norm_num

@[simp] private theorem phi_323 : Nat.totient 323 = 288 := by
  calc
    Nat.totient 323 = Nat.totient (17 * 19) := by norm_num
    _ = (17 - 1) * Nat.totient 19 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_324 : Nat.totient 324 = 108 := by
  calc
    Nat.totient 324 = Nat.totient (2 * 162) := by norm_num
    _ = 2 * Nat.totient 162 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 108 := by norm_num

@[simp] private theorem phi_325 : Nat.totient 325 = 240 := by
  calc
    Nat.totient 325 = Nat.totient (5 * 65) := by norm_num
    _ = 5 * Nat.totient 65 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_326 : Nat.totient 326 = 162 := by
  calc
    Nat.totient 326 = Nat.totient (2 * 163) := by norm_num
    _ = (2 - 1) * Nat.totient 163 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 162 := by norm_num

@[simp] private theorem phi_327 : Nat.totient 327 = 216 := by
  calc
    Nat.totient 327 = Nat.totient (3 * 109) := by norm_num
    _ = (3 - 1) * Nat.totient 109 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_328 : Nat.totient 328 = 160 := by
  calc
    Nat.totient 328 = Nat.totient (2 * 164) := by norm_num
    _ = 2 * Nat.totient 164 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_329 : Nat.totient 329 = 276 := by
  calc
    Nat.totient 329 = Nat.totient (7 * 47) := by norm_num
    _ = (7 - 1) * Nat.totient 47 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 276 := by norm_num

@[simp] private theorem phi_330 : Nat.totient 330 = 80 := by
  calc
    Nat.totient 330 = Nat.totient (2 * 165) := by norm_num
    _ = (2 - 1) * Nat.totient 165 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 80 := by norm_num

@[simp] private theorem phi_331 : Nat.totient 331 = 330 := by
  calc
    Nat.totient 331 = Nat.totient (331 * 1) := by norm_num
    _ = (331 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 330 := by norm_num

@[simp] private theorem phi_332 : Nat.totient 332 = 164 := by
  calc
    Nat.totient 332 = Nat.totient (2 * 166) := by norm_num
    _ = 2 * Nat.totient 166 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 164 := by norm_num

@[simp] private theorem phi_333 : Nat.totient 333 = 216 := by
  calc
    Nat.totient 333 = Nat.totient (3 * 111) := by norm_num
    _ = 3 * Nat.totient 111 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_334 : Nat.totient 334 = 166 := by
  calc
    Nat.totient 334 = Nat.totient (2 * 167) := by norm_num
    _ = (2 - 1) * Nat.totient 167 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 166 := by norm_num

@[simp] private theorem phi_335 : Nat.totient 335 = 264 := by
  calc
    Nat.totient 335 = Nat.totient (5 * 67) := by norm_num
    _ = (5 - 1) * Nat.totient 67 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 264 := by norm_num

@[simp] private theorem phi_336 : Nat.totient 336 = 96 := by
  calc
    Nat.totient 336 = Nat.totient (2 * 168) := by norm_num
    _ = 2 * Nat.totient 168 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_337 : Nat.totient 337 = 336 := by
  calc
    Nat.totient 337 = Nat.totient (337 * 1) := by norm_num
    _ = (337 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_338 : Nat.totient 338 = 156 := by
  calc
    Nat.totient 338 = Nat.totient (2 * 169) := by norm_num
    _ = (2 - 1) * Nat.totient 169 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 156 := by norm_num

@[simp] private theorem phi_339 : Nat.totient 339 = 224 := by
  calc
    Nat.totient 339 = Nat.totient (3 * 113) := by norm_num
    _ = (3 - 1) * Nat.totient 113 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 224 := by norm_num

@[simp] private theorem phi_340 : Nat.totient 340 = 128 := by
  calc
    Nat.totient 340 = Nat.totient (2 * 170) := by norm_num
    _ = 2 * Nat.totient 170 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 128 := by norm_num

@[simp] private theorem phi_341 : Nat.totient 341 = 300 := by
  calc
    Nat.totient 341 = Nat.totient (11 * 31) := by norm_num
    _ = (11 - 1) * Nat.totient 31 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 300 := by norm_num

@[simp] private theorem phi_342 : Nat.totient 342 = 108 := by
  calc
    Nat.totient 342 = Nat.totient (2 * 171) := by norm_num
    _ = (2 - 1) * Nat.totient 171 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 108 := by norm_num

@[simp] private theorem phi_343 : Nat.totient 343 = 294 := by
  calc
    Nat.totient 343 = Nat.totient (7 * 49) := by norm_num
    _ = 7 * Nat.totient 49 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 294 := by norm_num

@[simp] private theorem phi_344 : Nat.totient 344 = 168 := by
  calc
    Nat.totient 344 = Nat.totient (2 * 172) := by norm_num
    _ = 2 * Nat.totient 172 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_345 : Nat.totient 345 = 176 := by
  calc
    Nat.totient 345 = Nat.totient (3 * 115) := by norm_num
    _ = (3 - 1) * Nat.totient 115 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 176 := by norm_num

@[simp] private theorem phi_346 : Nat.totient 346 = 172 := by
  calc
    Nat.totient 346 = Nat.totient (2 * 173) := by norm_num
    _ = (2 - 1) * Nat.totient 173 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 172 := by norm_num

@[simp] private theorem phi_347 : Nat.totient 347 = 346 := by
  calc
    Nat.totient 347 = Nat.totient (347 * 1) := by norm_num
    _ = (347 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 346 := by norm_num

@[simp] private theorem phi_348 : Nat.totient 348 = 112 := by
  calc
    Nat.totient 348 = Nat.totient (2 * 174) := by norm_num
    _ = 2 * Nat.totient 174 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 112 := by norm_num

@[simp] private theorem phi_349 : Nat.totient 349 = 348 := by
  calc
    Nat.totient 349 = Nat.totient (349 * 1) := by norm_num
    _ = (349 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 348 := by norm_num

@[simp] private theorem phi_350 : Nat.totient 350 = 120 := by
  calc
    Nat.totient 350 = Nat.totient (2 * 175) := by norm_num
    _ = (2 - 1) * Nat.totient 175 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_351 : Nat.totient 351 = 216 := by
  calc
    Nat.totient 351 = Nat.totient (3 * 117) := by norm_num
    _ = 3 * Nat.totient 117 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_352 : Nat.totient 352 = 160 := by
  calc
    Nat.totient 352 = Nat.totient (2 * 176) := by norm_num
    _ = 2 * Nat.totient 176 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_353 : Nat.totient 353 = 352 := by
  calc
    Nat.totient 353 = Nat.totient (353 * 1) := by norm_num
    _ = (353 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 352 := by norm_num

@[simp] private theorem phi_354 : Nat.totient 354 = 116 := by
  calc
    Nat.totient 354 = Nat.totient (2 * 177) := by norm_num
    _ = (2 - 1) * Nat.totient 177 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 116 := by norm_num

@[simp] private theorem phi_355 : Nat.totient 355 = 280 := by
  calc
    Nat.totient 355 = Nat.totient (5 * 71) := by norm_num
    _ = (5 - 1) * Nat.totient 71 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 280 := by norm_num

@[simp] private theorem phi_356 : Nat.totient 356 = 176 := by
  calc
    Nat.totient 356 = Nat.totient (2 * 178) := by norm_num
    _ = 2 * Nat.totient 178 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 176 := by norm_num

@[simp] private theorem phi_357 : Nat.totient 357 = 192 := by
  calc
    Nat.totient 357 = Nat.totient (3 * 119) := by norm_num
    _ = (3 - 1) * Nat.totient 119 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_358 : Nat.totient 358 = 178 := by
  calc
    Nat.totient 358 = Nat.totient (2 * 179) := by norm_num
    _ = (2 - 1) * Nat.totient 179 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 178 := by norm_num

@[simp] private theorem phi_359 : Nat.totient 359 = 358 := by
  calc
    Nat.totient 359 = Nat.totient (359 * 1) := by norm_num
    _ = (359 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 358 := by norm_num

@[simp] private theorem phi_360 : Nat.totient 360 = 96 := by
  calc
    Nat.totient 360 = Nat.totient (2 * 180) := by norm_num
    _ = 2 * Nat.totient 180 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_361 : Nat.totient 361 = 342 := by
  calc
    Nat.totient 361 = Nat.totient (19 * 19) := by norm_num
    _ = 19 * Nat.totient 19 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 342 := by norm_num

@[simp] private theorem phi_362 : Nat.totient 362 = 180 := by
  calc
    Nat.totient 362 = Nat.totient (2 * 181) := by norm_num
    _ = (2 - 1) * Nat.totient 181 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_363 : Nat.totient 363 = 220 := by
  calc
    Nat.totient 363 = Nat.totient (3 * 121) := by norm_num
    _ = (3 - 1) * Nat.totient 121 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 220 := by norm_num

@[simp] private theorem phi_364 : Nat.totient 364 = 144 := by
  calc
    Nat.totient 364 = Nat.totient (2 * 182) := by norm_num
    _ = 2 * Nat.totient 182 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_365 : Nat.totient 365 = 288 := by
  calc
    Nat.totient 365 = Nat.totient (5 * 73) := by norm_num
    _ = (5 - 1) * Nat.totient 73 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_366 : Nat.totient 366 = 120 := by
  calc
    Nat.totient 366 = Nat.totient (2 * 183) := by norm_num
    _ = (2 - 1) * Nat.totient 183 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_367 : Nat.totient 367 = 366 := by
  calc
    Nat.totient 367 = Nat.totient (367 * 1) := by norm_num
    _ = (367 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 366 := by norm_num

@[simp] private theorem phi_368 : Nat.totient 368 = 176 := by
  calc
    Nat.totient 368 = Nat.totient (2 * 184) := by norm_num
    _ = 2 * Nat.totient 184 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 176 := by norm_num

@[simp] private theorem phi_369 : Nat.totient 369 = 240 := by
  calc
    Nat.totient 369 = Nat.totient (3 * 123) := by norm_num
    _ = 3 * Nat.totient 123 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_370 : Nat.totient 370 = 144 := by
  calc
    Nat.totient 370 = Nat.totient (2 * 185) := by norm_num
    _ = (2 - 1) * Nat.totient 185 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_371 : Nat.totient 371 = 312 := by
  calc
    Nat.totient 371 = Nat.totient (7 * 53) := by norm_num
    _ = (7 - 1) * Nat.totient 53 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_372 : Nat.totient 372 = 120 := by
  calc
    Nat.totient 372 = Nat.totient (2 * 186) := by norm_num
    _ = 2 * Nat.totient 186 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_373 : Nat.totient 373 = 372 := by
  calc
    Nat.totient 373 = Nat.totient (373 * 1) := by norm_num
    _ = (373 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 372 := by norm_num

@[simp] private theorem phi_374 : Nat.totient 374 = 160 := by
  calc
    Nat.totient 374 = Nat.totient (2 * 187) := by norm_num
    _ = (2 - 1) * Nat.totient 187 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_375 : Nat.totient 375 = 200 := by
  calc
    Nat.totient 375 = Nat.totient (3 * 125) := by norm_num
    _ = (3 - 1) * Nat.totient 125 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 200 := by norm_num

@[simp] private theorem phi_376 : Nat.totient 376 = 184 := by
  calc
    Nat.totient 376 = Nat.totient (2 * 188) := by norm_num
    _ = 2 * Nat.totient 188 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 184 := by norm_num

@[simp] private theorem phi_377 : Nat.totient 377 = 336 := by
  calc
    Nat.totient 377 = Nat.totient (13 * 29) := by norm_num
    _ = (13 - 1) * Nat.totient 29 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_378 : Nat.totient 378 = 108 := by
  calc
    Nat.totient 378 = Nat.totient (2 * 189) := by norm_num
    _ = (2 - 1) * Nat.totient 189 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 108 := by norm_num

@[simp] private theorem phi_379 : Nat.totient 379 = 378 := by
  calc
    Nat.totient 379 = Nat.totient (379 * 1) := by norm_num
    _ = (379 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 378 := by norm_num

@[simp] private theorem phi_380 : Nat.totient 380 = 144 := by
  calc
    Nat.totient 380 = Nat.totient (2 * 190) := by norm_num
    _ = 2 * Nat.totient 190 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_381 : Nat.totient 381 = 252 := by
  calc
    Nat.totient 381 = Nat.totient (3 * 127) := by norm_num
    _ = (3 - 1) * Nat.totient 127 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 252 := by norm_num

@[simp] private theorem phi_382 : Nat.totient 382 = 190 := by
  calc
    Nat.totient 382 = Nat.totient (2 * 191) := by norm_num
    _ = (2 - 1) * Nat.totient 191 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 190 := by norm_num

@[simp] private theorem phi_383 : Nat.totient 383 = 382 := by
  calc
    Nat.totient 383 = Nat.totient (383 * 1) := by norm_num
    _ = (383 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 382 := by norm_num

@[simp] private theorem phi_384 : Nat.totient 384 = 128 := by
  calc
    Nat.totient 384 = Nat.totient (2 * 192) := by norm_num
    _ = 2 * Nat.totient 192 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 128 := by norm_num

@[simp] private theorem phi_385 : Nat.totient 385 = 240 := by
  calc
    Nat.totient 385 = Nat.totient (5 * 77) := by norm_num
    _ = (5 - 1) * Nat.totient 77 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_386 : Nat.totient 386 = 192 := by
  calc
    Nat.totient 386 = Nat.totient (2 * 193) := by norm_num
    _ = (2 - 1) * Nat.totient 193 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_387 : Nat.totient 387 = 252 := by
  calc
    Nat.totient 387 = Nat.totient (3 * 129) := by norm_num
    _ = 3 * Nat.totient 129 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 252 := by norm_num

@[simp] private theorem phi_388 : Nat.totient 388 = 192 := by
  calc
    Nat.totient 388 = Nat.totient (2 * 194) := by norm_num
    _ = 2 * Nat.totient 194 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_389 : Nat.totient 389 = 388 := by
  calc
    Nat.totient 389 = Nat.totient (389 * 1) := by norm_num
    _ = (389 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 388 := by norm_num

@[simp] private theorem phi_390 : Nat.totient 390 = 96 := by
  calc
    Nat.totient 390 = Nat.totient (2 * 195) := by norm_num
    _ = (2 - 1) * Nat.totient 195 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_391 : Nat.totient 391 = 352 := by
  calc
    Nat.totient 391 = Nat.totient (17 * 23) := by norm_num
    _ = (17 - 1) * Nat.totient 23 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 352 := by norm_num

@[simp] private theorem phi_392 : Nat.totient 392 = 168 := by
  calc
    Nat.totient 392 = Nat.totient (2 * 196) := by norm_num
    _ = 2 * Nat.totient 196 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_393 : Nat.totient 393 = 260 := by
  calc
    Nat.totient 393 = Nat.totient (3 * 131) := by norm_num
    _ = (3 - 1) * Nat.totient 131 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 260 := by norm_num

@[simp] private theorem phi_394 : Nat.totient 394 = 196 := by
  calc
    Nat.totient 394 = Nat.totient (2 * 197) := by norm_num
    _ = (2 - 1) * Nat.totient 197 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 196 := by norm_num

@[simp] private theorem phi_395 : Nat.totient 395 = 312 := by
  calc
    Nat.totient 395 = Nat.totient (5 * 79) := by norm_num
    _ = (5 - 1) * Nat.totient 79 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_396 : Nat.totient 396 = 120 := by
  calc
    Nat.totient 396 = Nat.totient (2 * 198) := by norm_num
    _ = 2 * Nat.totient 198 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_397 : Nat.totient 397 = 396 := by
  calc
    Nat.totient 397 = Nat.totient (397 * 1) := by norm_num
    _ = (397 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 396 := by norm_num

@[simp] private theorem phi_398 : Nat.totient 398 = 198 := by
  calc
    Nat.totient 398 = Nat.totient (2 * 199) := by norm_num
    _ = (2 - 1) * Nat.totient 199 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 198 := by norm_num

@[simp] private theorem phi_399 : Nat.totient 399 = 216 := by
  calc
    Nat.totient 399 = Nat.totient (3 * 133) := by norm_num
    _ = (3 - 1) * Nat.totient 133 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_400 : Nat.totient 400 = 160 := by
  calc
    Nat.totient 400 = Nat.totient (2 * 200) := by norm_num
    _ = 2 * Nat.totient 200 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_401 : Nat.totient 401 = 400 := by
  calc
    Nat.totient 401 = Nat.totient (401 * 1) := by norm_num
    _ = (401 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 400 := by norm_num

@[simp] private theorem phi_402 : Nat.totient 402 = 132 := by
  calc
    Nat.totient 402 = Nat.totient (2 * 201) := by norm_num
    _ = (2 - 1) * Nat.totient 201 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 132 := by norm_num

@[simp] private theorem phi_403 : Nat.totient 403 = 360 := by
  calc
    Nat.totient 403 = Nat.totient (13 * 31) := by norm_num
    _ = (13 - 1) * Nat.totient 31 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_404 : Nat.totient 404 = 200 := by
  calc
    Nat.totient 404 = Nat.totient (2 * 202) := by norm_num
    _ = 2 * Nat.totient 202 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 200 := by norm_num

@[simp] private theorem phi_405 : Nat.totient 405 = 216 := by
  calc
    Nat.totient 405 = Nat.totient (3 * 135) := by norm_num
    _ = 3 * Nat.totient 135 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_406 : Nat.totient 406 = 168 := by
  calc
    Nat.totient 406 = Nat.totient (2 * 203) := by norm_num
    _ = (2 - 1) * Nat.totient 203 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_407 : Nat.totient 407 = 360 := by
  calc
    Nat.totient 407 = Nat.totient (11 * 37) := by norm_num
    _ = (11 - 1) * Nat.totient 37 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_408 : Nat.totient 408 = 128 := by
  calc
    Nat.totient 408 = Nat.totient (2 * 204) := by norm_num
    _ = 2 * Nat.totient 204 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 128 := by norm_num

@[simp] private theorem phi_409 : Nat.totient 409 = 408 := by
  calc
    Nat.totient 409 = Nat.totient (409 * 1) := by norm_num
    _ = (409 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 408 := by norm_num

@[simp] private theorem phi_410 : Nat.totient 410 = 160 := by
  calc
    Nat.totient 410 = Nat.totient (2 * 205) := by norm_num
    _ = (2 - 1) * Nat.totient 205 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_411 : Nat.totient 411 = 272 := by
  calc
    Nat.totient 411 = Nat.totient (3 * 137) := by norm_num
    _ = (3 - 1) * Nat.totient 137 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 272 := by norm_num

@[simp] private theorem phi_412 : Nat.totient 412 = 204 := by
  calc
    Nat.totient 412 = Nat.totient (2 * 206) := by norm_num
    _ = 2 * Nat.totient 206 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 204 := by norm_num

@[simp] private theorem phi_413 : Nat.totient 413 = 348 := by
  calc
    Nat.totient 413 = Nat.totient (7 * 59) := by norm_num
    _ = (7 - 1) * Nat.totient 59 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 348 := by norm_num

@[simp] private theorem phi_414 : Nat.totient 414 = 132 := by
  calc
    Nat.totient 414 = Nat.totient (2 * 207) := by norm_num
    _ = (2 - 1) * Nat.totient 207 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 132 := by norm_num

@[simp] private theorem phi_415 : Nat.totient 415 = 328 := by
  calc
    Nat.totient 415 = Nat.totient (5 * 83) := by norm_num
    _ = (5 - 1) * Nat.totient 83 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 328 := by norm_num

@[simp] private theorem phi_416 : Nat.totient 416 = 192 := by
  calc
    Nat.totient 416 = Nat.totient (2 * 208) := by norm_num
    _ = 2 * Nat.totient 208 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_417 : Nat.totient 417 = 276 := by
  calc
    Nat.totient 417 = Nat.totient (3 * 139) := by norm_num
    _ = (3 - 1) * Nat.totient 139 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 276 := by norm_num

@[simp] private theorem phi_418 : Nat.totient 418 = 180 := by
  calc
    Nat.totient 418 = Nat.totient (2 * 209) := by norm_num
    _ = (2 - 1) * Nat.totient 209 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_419 : Nat.totient 419 = 418 := by
  calc
    Nat.totient 419 = Nat.totient (419 * 1) := by norm_num
    _ = (419 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 418 := by norm_num

@[simp] private theorem phi_420 : Nat.totient 420 = 96 := by
  calc
    Nat.totient 420 = Nat.totient (2 * 210) := by norm_num
    _ = 2 * Nat.totient 210 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 96 := by norm_num

@[simp] private theorem phi_421 : Nat.totient 421 = 420 := by
  calc
    Nat.totient 421 = Nat.totient (421 * 1) := by norm_num
    _ = (421 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 420 := by norm_num

@[simp] private theorem phi_422 : Nat.totient 422 = 210 := by
  calc
    Nat.totient 422 = Nat.totient (2 * 211) := by norm_num
    _ = (2 - 1) * Nat.totient 211 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 210 := by norm_num

@[simp] private theorem phi_423 : Nat.totient 423 = 276 := by
  calc
    Nat.totient 423 = Nat.totient (3 * 141) := by norm_num
    _ = 3 * Nat.totient 141 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 276 := by norm_num

@[simp] private theorem phi_424 : Nat.totient 424 = 208 := by
  calc
    Nat.totient 424 = Nat.totient (2 * 212) := by norm_num
    _ = 2 * Nat.totient 212 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 208 := by norm_num

@[simp] private theorem phi_425 : Nat.totient 425 = 320 := by
  calc
    Nat.totient 425 = Nat.totient (5 * 85) := by norm_num
    _ = 5 * Nat.totient 85 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 320 := by norm_num

@[simp] private theorem phi_426 : Nat.totient 426 = 140 := by
  calc
    Nat.totient 426 = Nat.totient (2 * 213) := by norm_num
    _ = (2 - 1) * Nat.totient 213 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 140 := by norm_num

@[simp] private theorem phi_427 : Nat.totient 427 = 360 := by
  calc
    Nat.totient 427 = Nat.totient (7 * 61) := by norm_num
    _ = (7 - 1) * Nat.totient 61 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_428 : Nat.totient 428 = 212 := by
  calc
    Nat.totient 428 = Nat.totient (2 * 214) := by norm_num
    _ = 2 * Nat.totient 214 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 212 := by norm_num

@[simp] private theorem phi_429 : Nat.totient 429 = 240 := by
  calc
    Nat.totient 429 = Nat.totient (3 * 143) := by norm_num
    _ = (3 - 1) * Nat.totient 143 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_430 : Nat.totient 430 = 168 := by
  calc
    Nat.totient 430 = Nat.totient (2 * 215) := by norm_num
    _ = (2 - 1) * Nat.totient 215 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_431 : Nat.totient 431 = 430 := by
  calc
    Nat.totient 431 = Nat.totient (431 * 1) := by norm_num
    _ = (431 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 430 := by norm_num

@[simp] private theorem phi_432 : Nat.totient 432 = 144 := by
  calc
    Nat.totient 432 = Nat.totient (2 * 216) := by norm_num
    _ = 2 * Nat.totient 216 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_433 : Nat.totient 433 = 432 := by
  calc
    Nat.totient 433 = Nat.totient (433 * 1) := by norm_num
    _ = (433 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 432 := by norm_num

@[simp] private theorem phi_434 : Nat.totient 434 = 180 := by
  calc
    Nat.totient 434 = Nat.totient (2 * 217) := by norm_num
    _ = (2 - 1) * Nat.totient 217 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_435 : Nat.totient 435 = 224 := by
  calc
    Nat.totient 435 = Nat.totient (3 * 145) := by norm_num
    _ = (3 - 1) * Nat.totient 145 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 224 := by norm_num

@[simp] private theorem phi_436 : Nat.totient 436 = 216 := by
  calc
    Nat.totient 436 = Nat.totient (2 * 218) := by norm_num
    _ = 2 * Nat.totient 218 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_437 : Nat.totient 437 = 396 := by
  calc
    Nat.totient 437 = Nat.totient (19 * 23) := by norm_num
    _ = (19 - 1) * Nat.totient 23 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 396 := by norm_num

@[simp] private theorem phi_438 : Nat.totient 438 = 144 := by
  calc
    Nat.totient 438 = Nat.totient (2 * 219) := by norm_num
    _ = (2 - 1) * Nat.totient 219 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_439 : Nat.totient 439 = 438 := by
  calc
    Nat.totient 439 = Nat.totient (439 * 1) := by norm_num
    _ = (439 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 438 := by norm_num

@[simp] private theorem phi_440 : Nat.totient 440 = 160 := by
  calc
    Nat.totient 440 = Nat.totient (2 * 220) := by norm_num
    _ = 2 * Nat.totient 220 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_441 : Nat.totient 441 = 252 := by
  calc
    Nat.totient 441 = Nat.totient (3 * 147) := by norm_num
    _ = 3 * Nat.totient 147 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 252 := by norm_num

@[simp] private theorem phi_442 : Nat.totient 442 = 192 := by
  calc
    Nat.totient 442 = Nat.totient (2 * 221) := by norm_num
    _ = (2 - 1) * Nat.totient 221 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_443 : Nat.totient 443 = 442 := by
  calc
    Nat.totient 443 = Nat.totient (443 * 1) := by norm_num
    _ = (443 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 442 := by norm_num

@[simp] private theorem phi_444 : Nat.totient 444 = 144 := by
  calc
    Nat.totient 444 = Nat.totient (2 * 222) := by norm_num
    _ = 2 * Nat.totient 222 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_445 : Nat.totient 445 = 352 := by
  calc
    Nat.totient 445 = Nat.totient (5 * 89) := by norm_num
    _ = (5 - 1) * Nat.totient 89 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 352 := by norm_num

@[simp] private theorem phi_446 : Nat.totient 446 = 222 := by
  calc
    Nat.totient 446 = Nat.totient (2 * 223) := by norm_num
    _ = (2 - 1) * Nat.totient 223 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 222 := by norm_num

@[simp] private theorem phi_447 : Nat.totient 447 = 296 := by
  calc
    Nat.totient 447 = Nat.totient (3 * 149) := by norm_num
    _ = (3 - 1) * Nat.totient 149 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 296 := by norm_num

@[simp] private theorem phi_448 : Nat.totient 448 = 192 := by
  calc
    Nat.totient 448 = Nat.totient (2 * 224) := by norm_num
    _ = 2 * Nat.totient 224 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_449 : Nat.totient 449 = 448 := by
  calc
    Nat.totient 449 = Nat.totient (449 * 1) := by norm_num
    _ = (449 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 448 := by norm_num

@[simp] private theorem phi_450 : Nat.totient 450 = 120 := by
  calc
    Nat.totient 450 = Nat.totient (2 * 225) := by norm_num
    _ = (2 - 1) * Nat.totient 225 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_451 : Nat.totient 451 = 400 := by
  calc
    Nat.totient 451 = Nat.totient (11 * 41) := by norm_num
    _ = (11 - 1) * Nat.totient 41 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 400 := by norm_num

@[simp] private theorem phi_452 : Nat.totient 452 = 224 := by
  calc
    Nat.totient 452 = Nat.totient (2 * 226) := by norm_num
    _ = 2 * Nat.totient 226 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 224 := by norm_num

@[simp] private theorem phi_453 : Nat.totient 453 = 300 := by
  calc
    Nat.totient 453 = Nat.totient (3 * 151) := by norm_num
    _ = (3 - 1) * Nat.totient 151 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 300 := by norm_num

@[simp] private theorem phi_454 : Nat.totient 454 = 226 := by
  calc
    Nat.totient 454 = Nat.totient (2 * 227) := by norm_num
    _ = (2 - 1) * Nat.totient 227 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 226 := by norm_num

@[simp] private theorem phi_455 : Nat.totient 455 = 288 := by
  calc
    Nat.totient 455 = Nat.totient (5 * 91) := by norm_num
    _ = (5 - 1) * Nat.totient 91 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_456 : Nat.totient 456 = 144 := by
  calc
    Nat.totient 456 = Nat.totient (2 * 228) := by norm_num
    _ = 2 * Nat.totient 228 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_457 : Nat.totient 457 = 456 := by
  calc
    Nat.totient 457 = Nat.totient (457 * 1) := by norm_num
    _ = (457 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 456 := by norm_num

@[simp] private theorem phi_458 : Nat.totient 458 = 228 := by
  calc
    Nat.totient 458 = Nat.totient (2 * 229) := by norm_num
    _ = (2 - 1) * Nat.totient 229 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 228 := by norm_num

@[simp] private theorem phi_459 : Nat.totient 459 = 288 := by
  calc
    Nat.totient 459 = Nat.totient (3 * 153) := by norm_num
    _ = 3 * Nat.totient 153 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_460 : Nat.totient 460 = 176 := by
  calc
    Nat.totient 460 = Nat.totient (2 * 230) := by norm_num
    _ = 2 * Nat.totient 230 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 176 := by norm_num

@[simp] private theorem phi_461 : Nat.totient 461 = 460 := by
  calc
    Nat.totient 461 = Nat.totient (461 * 1) := by norm_num
    _ = (461 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 460 := by norm_num

@[simp] private theorem phi_462 : Nat.totient 462 = 120 := by
  calc
    Nat.totient 462 = Nat.totient (2 * 231) := by norm_num
    _ = (2 - 1) * Nat.totient 231 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 120 := by norm_num

@[simp] private theorem phi_463 : Nat.totient 463 = 462 := by
  calc
    Nat.totient 463 = Nat.totient (463 * 1) := by norm_num
    _ = (463 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 462 := by norm_num

@[simp] private theorem phi_464 : Nat.totient 464 = 224 := by
  calc
    Nat.totient 464 = Nat.totient (2 * 232) := by norm_num
    _ = 2 * Nat.totient 232 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 224 := by norm_num

@[simp] private theorem phi_465 : Nat.totient 465 = 240 := by
  calc
    Nat.totient 465 = Nat.totient (3 * 155) := by norm_num
    _ = (3 - 1) * Nat.totient 155 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_466 : Nat.totient 466 = 232 := by
  calc
    Nat.totient 466 = Nat.totient (2 * 233) := by norm_num
    _ = (2 - 1) * Nat.totient 233 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 232 := by norm_num

@[simp] private theorem phi_467 : Nat.totient 467 = 466 := by
  calc
    Nat.totient 467 = Nat.totient (467 * 1) := by norm_num
    _ = (467 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 466 := by norm_num

@[simp] private theorem phi_468 : Nat.totient 468 = 144 := by
  calc
    Nat.totient 468 = Nat.totient (2 * 234) := by norm_num
    _ = 2 * Nat.totient 234 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_469 : Nat.totient 469 = 396 := by
  calc
    Nat.totient 469 = Nat.totient (7 * 67) := by norm_num
    _ = (7 - 1) * Nat.totient 67 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 396 := by norm_num

@[simp] private theorem phi_470 : Nat.totient 470 = 184 := by
  calc
    Nat.totient 470 = Nat.totient (2 * 235) := by norm_num
    _ = (2 - 1) * Nat.totient 235 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 184 := by norm_num

@[simp] private theorem phi_471 : Nat.totient 471 = 312 := by
  calc
    Nat.totient 471 = Nat.totient (3 * 157) := by norm_num
    _ = (3 - 1) * Nat.totient 157 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_472 : Nat.totient 472 = 232 := by
  calc
    Nat.totient 472 = Nat.totient (2 * 236) := by norm_num
    _ = 2 * Nat.totient 236 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 232 := by norm_num

@[simp] private theorem phi_473 : Nat.totient 473 = 420 := by
  calc
    Nat.totient 473 = Nat.totient (11 * 43) := by norm_num
    _ = (11 - 1) * Nat.totient 43 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 420 := by norm_num

@[simp] private theorem phi_474 : Nat.totient 474 = 156 := by
  calc
    Nat.totient 474 = Nat.totient (2 * 237) := by norm_num
    _ = (2 - 1) * Nat.totient 237 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 156 := by norm_num

@[simp] private theorem phi_475 : Nat.totient 475 = 360 := by
  calc
    Nat.totient 475 = Nat.totient (5 * 95) := by norm_num
    _ = 5 * Nat.totient 95 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_476 : Nat.totient 476 = 192 := by
  calc
    Nat.totient 476 = Nat.totient (2 * 238) := by norm_num
    _ = 2 * Nat.totient 238 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_477 : Nat.totient 477 = 312 := by
  calc
    Nat.totient 477 = Nat.totient (3 * 159) := by norm_num
    _ = 3 * Nat.totient 159 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_478 : Nat.totient 478 = 238 := by
  calc
    Nat.totient 478 = Nat.totient (2 * 239) := by norm_num
    _ = (2 - 1) * Nat.totient 239 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 238 := by norm_num

@[simp] private theorem phi_479 : Nat.totient 479 = 478 := by
  calc
    Nat.totient 479 = Nat.totient (479 * 1) := by norm_num
    _ = (479 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 478 := by norm_num

@[simp] private theorem phi_480 : Nat.totient 480 = 128 := by
  calc
    Nat.totient 480 = Nat.totient (2 * 240) := by norm_num
    _ = 2 * Nat.totient 240 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 128 := by norm_num

@[simp] private theorem phi_481 : Nat.totient 481 = 432 := by
  calc
    Nat.totient 481 = Nat.totient (13 * 37) := by norm_num
    _ = (13 - 1) * Nat.totient 37 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 432 := by norm_num

@[simp] private theorem phi_482 : Nat.totient 482 = 240 := by
  calc
    Nat.totient 482 = Nat.totient (2 * 241) := by norm_num
    _ = (2 - 1) * Nat.totient 241 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_483 : Nat.totient 483 = 264 := by
  calc
    Nat.totient 483 = Nat.totient (3 * 161) := by norm_num
    _ = (3 - 1) * Nat.totient 161 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 264 := by norm_num

@[simp] private theorem phi_484 : Nat.totient 484 = 220 := by
  calc
    Nat.totient 484 = Nat.totient (2 * 242) := by norm_num
    _ = 2 * Nat.totient 242 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 220 := by norm_num

@[simp] private theorem phi_485 : Nat.totient 485 = 384 := by
  calc
    Nat.totient 485 = Nat.totient (5 * 97) := by norm_num
    _ = (5 - 1) * Nat.totient 97 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 384 := by norm_num

@[simp] private theorem phi_486 : Nat.totient 486 = 162 := by
  calc
    Nat.totient 486 = Nat.totient (2 * 243) := by norm_num
    _ = (2 - 1) * Nat.totient 243 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 162 := by norm_num

@[simp] private theorem phi_487 : Nat.totient 487 = 486 := by
  calc
    Nat.totient 487 = Nat.totient (487 * 1) := by norm_num
    _ = (487 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 486 := by norm_num

@[simp] private theorem phi_488 : Nat.totient 488 = 240 := by
  calc
    Nat.totient 488 = Nat.totient (2 * 244) := by norm_num
    _ = 2 * Nat.totient 244 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_489 : Nat.totient 489 = 324 := by
  calc
    Nat.totient 489 = Nat.totient (3 * 163) := by norm_num
    _ = (3 - 1) * Nat.totient 163 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 324 := by norm_num

@[simp] private theorem phi_490 : Nat.totient 490 = 168 := by
  calc
    Nat.totient 490 = Nat.totient (2 * 245) := by norm_num
    _ = (2 - 1) * Nat.totient 245 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_491 : Nat.totient 491 = 490 := by
  calc
    Nat.totient 491 = Nat.totient (491 * 1) := by norm_num
    _ = (491 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 490 := by norm_num

@[simp] private theorem phi_492 : Nat.totient 492 = 160 := by
  calc
    Nat.totient 492 = Nat.totient (2 * 246) := by norm_num
    _ = 2 * Nat.totient 246 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_493 : Nat.totient 493 = 448 := by
  calc
    Nat.totient 493 = Nat.totient (17 * 29) := by norm_num
    _ = (17 - 1) * Nat.totient 29 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 448 := by norm_num

@[simp] private theorem phi_494 : Nat.totient 494 = 216 := by
  calc
    Nat.totient 494 = Nat.totient (2 * 247) := by norm_num
    _ = (2 - 1) * Nat.totient 247 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_495 : Nat.totient 495 = 240 := by
  calc
    Nat.totient 495 = Nat.totient (3 * 165) := by norm_num
    _ = 3 * Nat.totient 165 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_496 : Nat.totient 496 = 240 := by
  calc
    Nat.totient 496 = Nat.totient (2 * 248) := by norm_num
    _ = 2 * Nat.totient 248 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_497 : Nat.totient 497 = 420 := by
  calc
    Nat.totient 497 = Nat.totient (7 * 71) := by norm_num
    _ = (7 - 1) * Nat.totient 71 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 420 := by norm_num

@[simp] private theorem phi_498 : Nat.totient 498 = 164 := by
  calc
    Nat.totient 498 = Nat.totient (2 * 249) := by norm_num
    _ = (2 - 1) * Nat.totient 249 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 164 := by norm_num

@[simp] private theorem phi_499 : Nat.totient 499 = 498 := by
  calc
    Nat.totient 499 = Nat.totient (499 * 1) := by norm_num
    _ = (499 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 498 := by norm_num

@[simp] private theorem phi_500 : Nat.totient 500 = 200 := by
  calc
    Nat.totient 500 = Nat.totient (2 * 250) := by norm_num
    _ = 2 * Nat.totient 250 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 200 := by norm_num

@[simp] private theorem phi_501 : Nat.totient 501 = 332 := by
  calc
    Nat.totient 501 = Nat.totient (3 * 167) := by norm_num
    _ = (3 - 1) * Nat.totient 167 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 332 := by norm_num

@[simp] private theorem phi_502 : Nat.totient 502 = 250 := by
  calc
    Nat.totient 502 = Nat.totient (2 * 251) := by norm_num
    _ = (2 - 1) * Nat.totient 251 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 250 := by norm_num

@[simp] private theorem phi_503 : Nat.totient 503 = 502 := by
  calc
    Nat.totient 503 = Nat.totient (503 * 1) := by norm_num
    _ = (503 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 502 := by norm_num

@[simp] private theorem phi_504 : Nat.totient 504 = 144 := by
  calc
    Nat.totient 504 = Nat.totient (2 * 252) := by norm_num
    _ = 2 * Nat.totient 252 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_505 : Nat.totient 505 = 400 := by
  calc
    Nat.totient 505 = Nat.totient (5 * 101) := by norm_num
    _ = (5 - 1) * Nat.totient 101 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 400 := by norm_num

@[simp] private theorem phi_506 : Nat.totient 506 = 220 := by
  calc
    Nat.totient 506 = Nat.totient (2 * 253) := by norm_num
    _ = (2 - 1) * Nat.totient 253 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 220 := by norm_num

@[simp] private theorem phi_507 : Nat.totient 507 = 312 := by
  calc
    Nat.totient 507 = Nat.totient (3 * 169) := by norm_num
    _ = (3 - 1) * Nat.totient 169 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_508 : Nat.totient 508 = 252 := by
  calc
    Nat.totient 508 = Nat.totient (2 * 254) := by norm_num
    _ = 2 * Nat.totient 254 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 252 := by norm_num

@[simp] private theorem phi_509 : Nat.totient 509 = 508 := by
  calc
    Nat.totient 509 = Nat.totient (509 * 1) := by norm_num
    _ = (509 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 508 := by norm_num

@[simp] private theorem phi_510 : Nat.totient 510 = 128 := by
  calc
    Nat.totient 510 = Nat.totient (2 * 255) := by norm_num
    _ = (2 - 1) * Nat.totient 255 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 128 := by norm_num

@[simp] private theorem phi_511 : Nat.totient 511 = 432 := by
  calc
    Nat.totient 511 = Nat.totient (7 * 73) := by norm_num
    _ = (7 - 1) * Nat.totient 73 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 432 := by norm_num

@[simp] private theorem phi_512 : Nat.totient 512 = 256 := by
  calc
    Nat.totient 512 = Nat.totient (2 * 256) := by norm_num
    _ = 2 * Nat.totient 256 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 256 := by norm_num

@[simp] private theorem phi_513 : Nat.totient 513 = 324 := by
  calc
    Nat.totient 513 = Nat.totient (3 * 171) := by norm_num
    _ = 3 * Nat.totient 171 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 324 := by norm_num

@[simp] private theorem phi_514 : Nat.totient 514 = 256 := by
  calc
    Nat.totient 514 = Nat.totient (2 * 257) := by norm_num
    _ = (2 - 1) * Nat.totient 257 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 256 := by norm_num

@[simp] private theorem phi_515 : Nat.totient 515 = 408 := by
  calc
    Nat.totient 515 = Nat.totient (5 * 103) := by norm_num
    _ = (5 - 1) * Nat.totient 103 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 408 := by norm_num

@[simp] private theorem phi_516 : Nat.totient 516 = 168 := by
  calc
    Nat.totient 516 = Nat.totient (2 * 258) := by norm_num
    _ = 2 * Nat.totient 258 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_517 : Nat.totient 517 = 460 := by
  calc
    Nat.totient 517 = Nat.totient (11 * 47) := by norm_num
    _ = (11 - 1) * Nat.totient 47 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 460 := by norm_num

@[simp] private theorem phi_518 : Nat.totient 518 = 216 := by
  calc
    Nat.totient 518 = Nat.totient (2 * 259) := by norm_num
    _ = (2 - 1) * Nat.totient 259 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_519 : Nat.totient 519 = 344 := by
  calc
    Nat.totient 519 = Nat.totient (3 * 173) := by norm_num
    _ = (3 - 1) * Nat.totient 173 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 344 := by norm_num

@[simp] private theorem phi_520 : Nat.totient 520 = 192 := by
  calc
    Nat.totient 520 = Nat.totient (2 * 260) := by norm_num
    _ = 2 * Nat.totient 260 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_521 : Nat.totient 521 = 520 := by
  calc
    Nat.totient 521 = Nat.totient (521 * 1) := by norm_num
    _ = (521 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 520 := by norm_num

@[simp] private theorem phi_522 : Nat.totient 522 = 168 := by
  calc
    Nat.totient 522 = Nat.totient (2 * 261) := by norm_num
    _ = (2 - 1) * Nat.totient 261 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_523 : Nat.totient 523 = 522 := by
  calc
    Nat.totient 523 = Nat.totient (523 * 1) := by norm_num
    _ = (523 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 522 := by norm_num

@[simp] private theorem phi_524 : Nat.totient 524 = 260 := by
  calc
    Nat.totient 524 = Nat.totient (2 * 262) := by norm_num
    _ = 2 * Nat.totient 262 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 260 := by norm_num

@[simp] private theorem phi_525 : Nat.totient 525 = 240 := by
  calc
    Nat.totient 525 = Nat.totient (3 * 175) := by norm_num
    _ = (3 - 1) * Nat.totient 175 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_526 : Nat.totient 526 = 262 := by
  calc
    Nat.totient 526 = Nat.totient (2 * 263) := by norm_num
    _ = (2 - 1) * Nat.totient 263 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 262 := by norm_num

@[simp] private theorem phi_527 : Nat.totient 527 = 480 := by
  calc
    Nat.totient 527 = Nat.totient (17 * 31) := by norm_num
    _ = (17 - 1) * Nat.totient 31 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 480 := by norm_num

@[simp] private theorem phi_528 : Nat.totient 528 = 160 := by
  calc
    Nat.totient 528 = Nat.totient (2 * 264) := by norm_num
    _ = 2 * Nat.totient 264 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_529 : Nat.totient 529 = 506 := by
  calc
    Nat.totient 529 = Nat.totient (23 * 23) := by norm_num
    _ = 23 * Nat.totient 23 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 506 := by norm_num

@[simp] private theorem phi_530 : Nat.totient 530 = 208 := by
  calc
    Nat.totient 530 = Nat.totient (2 * 265) := by norm_num
    _ = (2 - 1) * Nat.totient 265 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 208 := by norm_num

@[simp] private theorem phi_531 : Nat.totient 531 = 348 := by
  calc
    Nat.totient 531 = Nat.totient (3 * 177) := by norm_num
    _ = 3 * Nat.totient 177 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 348 := by norm_num

@[simp] private theorem phi_532 : Nat.totient 532 = 216 := by
  calc
    Nat.totient 532 = Nat.totient (2 * 266) := by norm_num
    _ = 2 * Nat.totient 266 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_533 : Nat.totient 533 = 480 := by
  calc
    Nat.totient 533 = Nat.totient (13 * 41) := by norm_num
    _ = (13 - 1) * Nat.totient 41 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 480 := by norm_num

@[simp] private theorem phi_534 : Nat.totient 534 = 176 := by
  calc
    Nat.totient 534 = Nat.totient (2 * 267) := by norm_num
    _ = (2 - 1) * Nat.totient 267 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 176 := by norm_num

@[simp] private theorem phi_535 : Nat.totient 535 = 424 := by
  calc
    Nat.totient 535 = Nat.totient (5 * 107) := by norm_num
    _ = (5 - 1) * Nat.totient 107 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 424 := by norm_num

@[simp] private theorem phi_536 : Nat.totient 536 = 264 := by
  calc
    Nat.totient 536 = Nat.totient (2 * 268) := by norm_num
    _ = 2 * Nat.totient 268 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 264 := by norm_num

@[simp] private theorem phi_537 : Nat.totient 537 = 356 := by
  calc
    Nat.totient 537 = Nat.totient (3 * 179) := by norm_num
    _ = (3 - 1) * Nat.totient 179 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 356 := by norm_num

@[simp] private theorem phi_538 : Nat.totient 538 = 268 := by
  calc
    Nat.totient 538 = Nat.totient (2 * 269) := by norm_num
    _ = (2 - 1) * Nat.totient 269 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 268 := by norm_num

@[simp] private theorem phi_539 : Nat.totient 539 = 420 := by
  calc
    Nat.totient 539 = Nat.totient (7 * 77) := by norm_num
    _ = 7 * Nat.totient 77 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 420 := by norm_num

@[simp] private theorem phi_540 : Nat.totient 540 = 144 := by
  calc
    Nat.totient 540 = Nat.totient (2 * 270) := by norm_num
    _ = 2 * Nat.totient 270 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_541 : Nat.totient 541 = 540 := by
  calc
    Nat.totient 541 = Nat.totient (541 * 1) := by norm_num
    _ = (541 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 540 := by norm_num

@[simp] private theorem phi_542 : Nat.totient 542 = 270 := by
  calc
    Nat.totient 542 = Nat.totient (2 * 271) := by norm_num
    _ = (2 - 1) * Nat.totient 271 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 270 := by norm_num

@[simp] private theorem phi_543 : Nat.totient 543 = 360 := by
  calc
    Nat.totient 543 = Nat.totient (3 * 181) := by norm_num
    _ = (3 - 1) * Nat.totient 181 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_544 : Nat.totient 544 = 256 := by
  calc
    Nat.totient 544 = Nat.totient (2 * 272) := by norm_num
    _ = 2 * Nat.totient 272 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 256 := by norm_num

@[simp] private theorem phi_545 : Nat.totient 545 = 432 := by
  calc
    Nat.totient 545 = Nat.totient (5 * 109) := by norm_num
    _ = (5 - 1) * Nat.totient 109 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 432 := by norm_num

@[simp] private theorem phi_546 : Nat.totient 546 = 144 := by
  calc
    Nat.totient 546 = Nat.totient (2 * 273) := by norm_num
    _ = (2 - 1) * Nat.totient 273 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_547 : Nat.totient 547 = 546 := by
  calc
    Nat.totient 547 = Nat.totient (547 * 1) := by norm_num
    _ = (547 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 546 := by norm_num

@[simp] private theorem phi_548 : Nat.totient 548 = 272 := by
  calc
    Nat.totient 548 = Nat.totient (2 * 274) := by norm_num
    _ = 2 * Nat.totient 274 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 272 := by norm_num

@[simp] private theorem phi_549 : Nat.totient 549 = 360 := by
  calc
    Nat.totient 549 = Nat.totient (3 * 183) := by norm_num
    _ = 3 * Nat.totient 183 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_550 : Nat.totient 550 = 200 := by
  calc
    Nat.totient 550 = Nat.totient (2 * 275) := by norm_num
    _ = (2 - 1) * Nat.totient 275 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 200 := by norm_num

@[simp] private theorem phi_551 : Nat.totient 551 = 504 := by
  calc
    Nat.totient 551 = Nat.totient (19 * 29) := by norm_num
    _ = (19 - 1) * Nat.totient 29 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 504 := by norm_num

@[simp] private theorem phi_552 : Nat.totient 552 = 176 := by
  calc
    Nat.totient 552 = Nat.totient (2 * 276) := by norm_num
    _ = 2 * Nat.totient 276 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 176 := by norm_num

@[simp] private theorem phi_553 : Nat.totient 553 = 468 := by
  calc
    Nat.totient 553 = Nat.totient (7 * 79) := by norm_num
    _ = (7 - 1) * Nat.totient 79 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 468 := by norm_num

@[simp] private theorem phi_554 : Nat.totient 554 = 276 := by
  calc
    Nat.totient 554 = Nat.totient (2 * 277) := by norm_num
    _ = (2 - 1) * Nat.totient 277 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 276 := by norm_num

@[simp] private theorem phi_555 : Nat.totient 555 = 288 := by
  calc
    Nat.totient 555 = Nat.totient (3 * 185) := by norm_num
    _ = (3 - 1) * Nat.totient 185 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_556 : Nat.totient 556 = 276 := by
  calc
    Nat.totient 556 = Nat.totient (2 * 278) := by norm_num
    _ = 2 * Nat.totient 278 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 276 := by norm_num

@[simp] private theorem phi_557 : Nat.totient 557 = 556 := by
  calc
    Nat.totient 557 = Nat.totient (557 * 1) := by norm_num
    _ = (557 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 556 := by norm_num

@[simp] private theorem phi_558 : Nat.totient 558 = 180 := by
  calc
    Nat.totient 558 = Nat.totient (2 * 279) := by norm_num
    _ = (2 - 1) * Nat.totient 279 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_559 : Nat.totient 559 = 504 := by
  calc
    Nat.totient 559 = Nat.totient (13 * 43) := by norm_num
    _ = (13 - 1) * Nat.totient 43 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 504 := by norm_num

@[simp] private theorem phi_560 : Nat.totient 560 = 192 := by
  calc
    Nat.totient 560 = Nat.totient (2 * 280) := by norm_num
    _ = 2 * Nat.totient 280 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_561 : Nat.totient 561 = 320 := by
  calc
    Nat.totient 561 = Nat.totient (3 * 187) := by norm_num
    _ = (3 - 1) * Nat.totient 187 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 320 := by norm_num

@[simp] private theorem phi_562 : Nat.totient 562 = 280 := by
  calc
    Nat.totient 562 = Nat.totient (2 * 281) := by norm_num
    _ = (2 - 1) * Nat.totient 281 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 280 := by norm_num

@[simp] private theorem phi_563 : Nat.totient 563 = 562 := by
  calc
    Nat.totient 563 = Nat.totient (563 * 1) := by norm_num
    _ = (563 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 562 := by norm_num

@[simp] private theorem phi_564 : Nat.totient 564 = 184 := by
  calc
    Nat.totient 564 = Nat.totient (2 * 282) := by norm_num
    _ = 2 * Nat.totient 282 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 184 := by norm_num

@[simp] private theorem phi_565 : Nat.totient 565 = 448 := by
  calc
    Nat.totient 565 = Nat.totient (5 * 113) := by norm_num
    _ = (5 - 1) * Nat.totient 113 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 448 := by norm_num

@[simp] private theorem phi_566 : Nat.totient 566 = 282 := by
  calc
    Nat.totient 566 = Nat.totient (2 * 283) := by norm_num
    _ = (2 - 1) * Nat.totient 283 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 282 := by norm_num

@[simp] private theorem phi_567 : Nat.totient 567 = 324 := by
  calc
    Nat.totient 567 = Nat.totient (3 * 189) := by norm_num
    _ = 3 * Nat.totient 189 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 324 := by norm_num

@[simp] private theorem phi_568 : Nat.totient 568 = 280 := by
  calc
    Nat.totient 568 = Nat.totient (2 * 284) := by norm_num
    _ = 2 * Nat.totient 284 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 280 := by norm_num

@[simp] private theorem phi_569 : Nat.totient 569 = 568 := by
  calc
    Nat.totient 569 = Nat.totient (569 * 1) := by norm_num
    _ = (569 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 568 := by norm_num

@[simp] private theorem phi_570 : Nat.totient 570 = 144 := by
  calc
    Nat.totient 570 = Nat.totient (2 * 285) := by norm_num
    _ = (2 - 1) * Nat.totient 285 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_571 : Nat.totient 571 = 570 := by
  calc
    Nat.totient 571 = Nat.totient (571 * 1) := by norm_num
    _ = (571 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 570 := by norm_num

@[simp] private theorem phi_572 : Nat.totient 572 = 240 := by
  calc
    Nat.totient 572 = Nat.totient (2 * 286) := by norm_num
    _ = 2 * Nat.totient 286 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_573 : Nat.totient 573 = 380 := by
  calc
    Nat.totient 573 = Nat.totient (3 * 191) := by norm_num
    _ = (3 - 1) * Nat.totient 191 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 380 := by norm_num

@[simp] private theorem phi_574 : Nat.totient 574 = 240 := by
  calc
    Nat.totient 574 = Nat.totient (2 * 287) := by norm_num
    _ = (2 - 1) * Nat.totient 287 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_575 : Nat.totient 575 = 440 := by
  calc
    Nat.totient 575 = Nat.totient (5 * 115) := by norm_num
    _ = 5 * Nat.totient 115 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 440 := by norm_num

@[simp] private theorem phi_576 : Nat.totient 576 = 192 := by
  calc
    Nat.totient 576 = Nat.totient (2 * 288) := by norm_num
    _ = 2 * Nat.totient 288 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_577 : Nat.totient 577 = 576 := by
  calc
    Nat.totient 577 = Nat.totient (577 * 1) := by norm_num
    _ = (577 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 576 := by norm_num

@[simp] private theorem phi_578 : Nat.totient 578 = 272 := by
  calc
    Nat.totient 578 = Nat.totient (2 * 289) := by norm_num
    _ = (2 - 1) * Nat.totient 289 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 272 := by norm_num

@[simp] private theorem phi_579 : Nat.totient 579 = 384 := by
  calc
    Nat.totient 579 = Nat.totient (3 * 193) := by norm_num
    _ = (3 - 1) * Nat.totient 193 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 384 := by norm_num

@[simp] private theorem phi_580 : Nat.totient 580 = 224 := by
  calc
    Nat.totient 580 = Nat.totient (2 * 290) := by norm_num
    _ = 2 * Nat.totient 290 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 224 := by norm_num

@[simp] private theorem phi_581 : Nat.totient 581 = 492 := by
  calc
    Nat.totient 581 = Nat.totient (7 * 83) := by norm_num
    _ = (7 - 1) * Nat.totient 83 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 492 := by norm_num

@[simp] private theorem phi_582 : Nat.totient 582 = 192 := by
  calc
    Nat.totient 582 = Nat.totient (2 * 291) := by norm_num
    _ = (2 - 1) * Nat.totient 291 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_583 : Nat.totient 583 = 520 := by
  calc
    Nat.totient 583 = Nat.totient (11 * 53) := by norm_num
    _ = (11 - 1) * Nat.totient 53 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 520 := by norm_num

@[simp] private theorem phi_584 : Nat.totient 584 = 288 := by
  calc
    Nat.totient 584 = Nat.totient (2 * 292) := by norm_num
    _ = 2 * Nat.totient 292 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_585 : Nat.totient 585 = 288 := by
  calc
    Nat.totient 585 = Nat.totient (3 * 195) := by norm_num
    _ = 3 * Nat.totient 195 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_586 : Nat.totient 586 = 292 := by
  calc
    Nat.totient 586 = Nat.totient (2 * 293) := by norm_num
    _ = (2 - 1) * Nat.totient 293 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 292 := by norm_num

@[simp] private theorem phi_587 : Nat.totient 587 = 586 := by
  calc
    Nat.totient 587 = Nat.totient (587 * 1) := by norm_num
    _ = (587 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 586 := by norm_num

@[simp] private theorem phi_588 : Nat.totient 588 = 168 := by
  calc
    Nat.totient 588 = Nat.totient (2 * 294) := by norm_num
    _ = 2 * Nat.totient 294 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 168 := by norm_num

@[simp] private theorem phi_589 : Nat.totient 589 = 540 := by
  calc
    Nat.totient 589 = Nat.totient (19 * 31) := by norm_num
    _ = (19 - 1) * Nat.totient 31 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 540 := by norm_num

@[simp] private theorem phi_590 : Nat.totient 590 = 232 := by
  calc
    Nat.totient 590 = Nat.totient (2 * 295) := by norm_num
    _ = (2 - 1) * Nat.totient 295 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 232 := by norm_num

@[simp] private theorem phi_591 : Nat.totient 591 = 392 := by
  calc
    Nat.totient 591 = Nat.totient (3 * 197) := by norm_num
    _ = (3 - 1) * Nat.totient 197 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 392 := by norm_num

@[simp] private theorem phi_592 : Nat.totient 592 = 288 := by
  calc
    Nat.totient 592 = Nat.totient (2 * 296) := by norm_num
    _ = 2 * Nat.totient 296 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_593 : Nat.totient 593 = 592 := by
  calc
    Nat.totient 593 = Nat.totient (593 * 1) := by norm_num
    _ = (593 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 592 := by norm_num

@[simp] private theorem phi_594 : Nat.totient 594 = 180 := by
  calc
    Nat.totient 594 = Nat.totient (2 * 297) := by norm_num
    _ = (2 - 1) * Nat.totient 297 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 180 := by norm_num

@[simp] private theorem phi_595 : Nat.totient 595 = 384 := by
  calc
    Nat.totient 595 = Nat.totient (5 * 119) := by norm_num
    _ = (5 - 1) * Nat.totient 119 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 384 := by norm_num

@[simp] private theorem phi_596 : Nat.totient 596 = 296 := by
  calc
    Nat.totient 596 = Nat.totient (2 * 298) := by norm_num
    _ = 2 * Nat.totient 298 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 296 := by norm_num

@[simp] private theorem phi_597 : Nat.totient 597 = 396 := by
  calc
    Nat.totient 597 = Nat.totient (3 * 199) := by norm_num
    _ = (3 - 1) * Nat.totient 199 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 396 := by norm_num

@[simp] private theorem phi_598 : Nat.totient 598 = 264 := by
  calc
    Nat.totient 598 = Nat.totient (2 * 299) := by norm_num
    _ = (2 - 1) * Nat.totient 299 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 264 := by norm_num

@[simp] private theorem phi_599 : Nat.totient 599 = 598 := by
  calc
    Nat.totient 599 = Nat.totient (599 * 1) := by norm_num
    _ = (599 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 598 := by norm_num

@[simp] private theorem phi_600 : Nat.totient 600 = 160 := by
  calc
    Nat.totient 600 = Nat.totient (2 * 300) := by norm_num
    _ = 2 * Nat.totient 300 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_601 : Nat.totient 601 = 600 := by
  calc
    Nat.totient 601 = Nat.totient (601 * 1) := by norm_num
    _ = (601 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 600 := by norm_num

@[simp] private theorem phi_602 : Nat.totient 602 = 252 := by
  calc
    Nat.totient 602 = Nat.totient (2 * 301) := by norm_num
    _ = (2 - 1) * Nat.totient 301 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 252 := by norm_num

@[simp] private theorem phi_603 : Nat.totient 603 = 396 := by
  calc
    Nat.totient 603 = Nat.totient (3 * 201) := by norm_num
    _ = 3 * Nat.totient 201 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 396 := by norm_num

@[simp] private theorem phi_604 : Nat.totient 604 = 300 := by
  calc
    Nat.totient 604 = Nat.totient (2 * 302) := by norm_num
    _ = 2 * Nat.totient 302 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 300 := by norm_num

@[simp] private theorem phi_605 : Nat.totient 605 = 440 := by
  calc
    Nat.totient 605 = Nat.totient (5 * 121) := by norm_num
    _ = (5 - 1) * Nat.totient 121 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 440 := by norm_num

@[simp] private theorem phi_606 : Nat.totient 606 = 200 := by
  calc
    Nat.totient 606 = Nat.totient (2 * 303) := by norm_num
    _ = (2 - 1) * Nat.totient 303 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 200 := by norm_num

@[simp] private theorem phi_607 : Nat.totient 607 = 606 := by
  calc
    Nat.totient 607 = Nat.totient (607 * 1) := by norm_num
    _ = (607 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 606 := by norm_num

@[simp] private theorem phi_608 : Nat.totient 608 = 288 := by
  calc
    Nat.totient 608 = Nat.totient (2 * 304) := by norm_num
    _ = 2 * Nat.totient 304 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_609 : Nat.totient 609 = 336 := by
  calc
    Nat.totient 609 = Nat.totient (3 * 203) := by norm_num
    _ = (3 - 1) * Nat.totient 203 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_610 : Nat.totient 610 = 240 := by
  calc
    Nat.totient 610 = Nat.totient (2 * 305) := by norm_num
    _ = (2 - 1) * Nat.totient 305 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_611 : Nat.totient 611 = 552 := by
  calc
    Nat.totient 611 = Nat.totient (13 * 47) := by norm_num
    _ = (13 - 1) * Nat.totient 47 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 552 := by norm_num

@[simp] private theorem phi_612 : Nat.totient 612 = 192 := by
  calc
    Nat.totient 612 = Nat.totient (2 * 306) := by norm_num
    _ = 2 * Nat.totient 306 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_613 : Nat.totient 613 = 612 := by
  calc
    Nat.totient 613 = Nat.totient (613 * 1) := by norm_num
    _ = (613 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 612 := by norm_num

@[simp] private theorem phi_614 : Nat.totient 614 = 306 := by
  calc
    Nat.totient 614 = Nat.totient (2 * 307) := by norm_num
    _ = (2 - 1) * Nat.totient 307 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 306 := by norm_num

@[simp] private theorem phi_615 : Nat.totient 615 = 320 := by
  calc
    Nat.totient 615 = Nat.totient (3 * 205) := by norm_num
    _ = (3 - 1) * Nat.totient 205 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 320 := by norm_num

@[simp] private theorem phi_616 : Nat.totient 616 = 240 := by
  calc
    Nat.totient 616 = Nat.totient (2 * 308) := by norm_num
    _ = 2 * Nat.totient 308 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_617 : Nat.totient 617 = 616 := by
  calc
    Nat.totient 617 = Nat.totient (617 * 1) := by norm_num
    _ = (617 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 616 := by norm_num

@[simp] private theorem phi_618 : Nat.totient 618 = 204 := by
  calc
    Nat.totient 618 = Nat.totient (2 * 309) := by norm_num
    _ = (2 - 1) * Nat.totient 309 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 204 := by norm_num

@[simp] private theorem phi_619 : Nat.totient 619 = 618 := by
  calc
    Nat.totient 619 = Nat.totient (619 * 1) := by norm_num
    _ = (619 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 618 := by norm_num

@[simp] private theorem phi_620 : Nat.totient 620 = 240 := by
  calc
    Nat.totient 620 = Nat.totient (2 * 310) := by norm_num
    _ = 2 * Nat.totient 310 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_621 : Nat.totient 621 = 396 := by
  calc
    Nat.totient 621 = Nat.totient (3 * 207) := by norm_num
    _ = 3 * Nat.totient 207 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 396 := by norm_num

@[simp] private theorem phi_622 : Nat.totient 622 = 310 := by
  calc
    Nat.totient 622 = Nat.totient (2 * 311) := by norm_num
    _ = (2 - 1) * Nat.totient 311 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 310 := by norm_num

@[simp] private theorem phi_623 : Nat.totient 623 = 528 := by
  calc
    Nat.totient 623 = Nat.totient (7 * 89) := by norm_num
    _ = (7 - 1) * Nat.totient 89 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 528 := by norm_num

@[simp] private theorem phi_624 : Nat.totient 624 = 192 := by
  calc
    Nat.totient 624 = Nat.totient (2 * 312) := by norm_num
    _ = 2 * Nat.totient 312 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_625 : Nat.totient 625 = 500 := by
  calc
    Nat.totient 625 = Nat.totient (5 * 125) := by norm_num
    _ = 5 * Nat.totient 125 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 500 := by norm_num

@[simp] private theorem phi_626 : Nat.totient 626 = 312 := by
  calc
    Nat.totient 626 = Nat.totient (2 * 313) := by norm_num
    _ = (2 - 1) * Nat.totient 313 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_627 : Nat.totient 627 = 360 := by
  calc
    Nat.totient 627 = Nat.totient (3 * 209) := by norm_num
    _ = (3 - 1) * Nat.totient 209 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_628 : Nat.totient 628 = 312 := by
  calc
    Nat.totient 628 = Nat.totient (2 * 314) := by norm_num
    _ = 2 * Nat.totient 314 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_629 : Nat.totient 629 = 576 := by
  calc
    Nat.totient 629 = Nat.totient (17 * 37) := by norm_num
    _ = (17 - 1) * Nat.totient 37 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 576 := by norm_num

@[simp] private theorem phi_630 : Nat.totient 630 = 144 := by
  calc
    Nat.totient 630 = Nat.totient (2 * 315) := by norm_num
    _ = (2 - 1) * Nat.totient 315 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 144 := by norm_num

@[simp] private theorem phi_631 : Nat.totient 631 = 630 := by
  calc
    Nat.totient 631 = Nat.totient (631 * 1) := by norm_num
    _ = (631 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 630 := by norm_num

@[simp] private theorem phi_632 : Nat.totient 632 = 312 := by
  calc
    Nat.totient 632 = Nat.totient (2 * 316) := by norm_num
    _ = 2 * Nat.totient 316 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_633 : Nat.totient 633 = 420 := by
  calc
    Nat.totient 633 = Nat.totient (3 * 211) := by norm_num
    _ = (3 - 1) * Nat.totient 211 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 420 := by norm_num

@[simp] private theorem phi_634 : Nat.totient 634 = 316 := by
  calc
    Nat.totient 634 = Nat.totient (2 * 317) := by norm_num
    _ = (2 - 1) * Nat.totient 317 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 316 := by norm_num

@[simp] private theorem phi_635 : Nat.totient 635 = 504 := by
  calc
    Nat.totient 635 = Nat.totient (5 * 127) := by norm_num
    _ = (5 - 1) * Nat.totient 127 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 504 := by norm_num

@[simp] private theorem phi_636 : Nat.totient 636 = 208 := by
  calc
    Nat.totient 636 = Nat.totient (2 * 318) := by norm_num
    _ = 2 * Nat.totient 318 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 208 := by norm_num

@[simp] private theorem phi_637 : Nat.totient 637 = 504 := by
  calc
    Nat.totient 637 = Nat.totient (7 * 91) := by norm_num
    _ = 7 * Nat.totient 91 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 504 := by norm_num

@[simp] private theorem phi_638 : Nat.totient 638 = 280 := by
  calc
    Nat.totient 638 = Nat.totient (2 * 319) := by norm_num
    _ = (2 - 1) * Nat.totient 319 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 280 := by norm_num

@[simp] private theorem phi_639 : Nat.totient 639 = 420 := by
  calc
    Nat.totient 639 = Nat.totient (3 * 213) := by norm_num
    _ = 3 * Nat.totient 213 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 420 := by norm_num

@[simp] private theorem phi_640 : Nat.totient 640 = 256 := by
  calc
    Nat.totient 640 = Nat.totient (2 * 320) := by norm_num
    _ = 2 * Nat.totient 320 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 256 := by norm_num

@[simp] private theorem phi_641 : Nat.totient 641 = 640 := by
  calc
    Nat.totient 641 = Nat.totient (641 * 1) := by norm_num
    _ = (641 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 640 := by norm_num

@[simp] private theorem phi_642 : Nat.totient 642 = 212 := by
  calc
    Nat.totient 642 = Nat.totient (2 * 321) := by norm_num
    _ = (2 - 1) * Nat.totient 321 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 212 := by norm_num

@[simp] private theorem phi_643 : Nat.totient 643 = 642 := by
  calc
    Nat.totient 643 = Nat.totient (643 * 1) := by norm_num
    _ = (643 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 642 := by norm_num

@[simp] private theorem phi_644 : Nat.totient 644 = 264 := by
  calc
    Nat.totient 644 = Nat.totient (2 * 322) := by norm_num
    _ = 2 * Nat.totient 322 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 264 := by norm_num

@[simp] private theorem phi_645 : Nat.totient 645 = 336 := by
  calc
    Nat.totient 645 = Nat.totient (3 * 215) := by norm_num
    _ = (3 - 1) * Nat.totient 215 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_646 : Nat.totient 646 = 288 := by
  calc
    Nat.totient 646 = Nat.totient (2 * 323) := by norm_num
    _ = (2 - 1) * Nat.totient 323 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_647 : Nat.totient 647 = 646 := by
  calc
    Nat.totient 647 = Nat.totient (647 * 1) := by norm_num
    _ = (647 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 646 := by norm_num

@[simp] private theorem phi_648 : Nat.totient 648 = 216 := by
  calc
    Nat.totient 648 = Nat.totient (2 * 324) := by norm_num
    _ = 2 * Nat.totient 324 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_649 : Nat.totient 649 = 580 := by
  calc
    Nat.totient 649 = Nat.totient (11 * 59) := by norm_num
    _ = (11 - 1) * Nat.totient 59 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 580 := by norm_num

@[simp] private theorem phi_650 : Nat.totient 650 = 240 := by
  calc
    Nat.totient 650 = Nat.totient (2 * 325) := by norm_num
    _ = (2 - 1) * Nat.totient 325 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_651 : Nat.totient 651 = 360 := by
  calc
    Nat.totient 651 = Nat.totient (3 * 217) := by norm_num
    _ = (3 - 1) * Nat.totient 217 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_652 : Nat.totient 652 = 324 := by
  calc
    Nat.totient 652 = Nat.totient (2 * 326) := by norm_num
    _ = 2 * Nat.totient 326 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 324 := by norm_num

@[simp] private theorem phi_653 : Nat.totient 653 = 652 := by
  calc
    Nat.totient 653 = Nat.totient (653 * 1) := by norm_num
    _ = (653 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 652 := by norm_num

@[simp] private theorem phi_654 : Nat.totient 654 = 216 := by
  calc
    Nat.totient 654 = Nat.totient (2 * 327) := by norm_num
    _ = (2 - 1) * Nat.totient 327 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_655 : Nat.totient 655 = 520 := by
  calc
    Nat.totient 655 = Nat.totient (5 * 131) := by norm_num
    _ = (5 - 1) * Nat.totient 131 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 520 := by norm_num

@[simp] private theorem phi_656 : Nat.totient 656 = 320 := by
  calc
    Nat.totient 656 = Nat.totient (2 * 328) := by norm_num
    _ = 2 * Nat.totient 328 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 320 := by norm_num

@[simp] private theorem phi_657 : Nat.totient 657 = 432 := by
  calc
    Nat.totient 657 = Nat.totient (3 * 219) := by norm_num
    _ = 3 * Nat.totient 219 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 432 := by norm_num

@[simp] private theorem phi_658 : Nat.totient 658 = 276 := by
  calc
    Nat.totient 658 = Nat.totient (2 * 329) := by norm_num
    _ = (2 - 1) * Nat.totient 329 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 276 := by norm_num

@[simp] private theorem phi_659 : Nat.totient 659 = 658 := by
  calc
    Nat.totient 659 = Nat.totient (659 * 1) := by norm_num
    _ = (659 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 658 := by norm_num

@[simp] private theorem phi_660 : Nat.totient 660 = 160 := by
  calc
    Nat.totient 660 = Nat.totient (2 * 330) := by norm_num
    _ = 2 * Nat.totient 330 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 160 := by norm_num

@[simp] private theorem phi_661 : Nat.totient 661 = 660 := by
  calc
    Nat.totient 661 = Nat.totient (661 * 1) := by norm_num
    _ = (661 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 660 := by norm_num

@[simp] private theorem phi_662 : Nat.totient 662 = 330 := by
  calc
    Nat.totient 662 = Nat.totient (2 * 331) := by norm_num
    _ = (2 - 1) * Nat.totient 331 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 330 := by norm_num

@[simp] private theorem phi_663 : Nat.totient 663 = 384 := by
  calc
    Nat.totient 663 = Nat.totient (3 * 221) := by norm_num
    _ = (3 - 1) * Nat.totient 221 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 384 := by norm_num

@[simp] private theorem phi_664 : Nat.totient 664 = 328 := by
  calc
    Nat.totient 664 = Nat.totient (2 * 332) := by norm_num
    _ = 2 * Nat.totient 332 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 328 := by norm_num

@[simp] private theorem phi_665 : Nat.totient 665 = 432 := by
  calc
    Nat.totient 665 = Nat.totient (5 * 133) := by norm_num
    _ = (5 - 1) * Nat.totient 133 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 432 := by norm_num

@[simp] private theorem phi_666 : Nat.totient 666 = 216 := by
  calc
    Nat.totient 666 = Nat.totient (2 * 333) := by norm_num
    _ = (2 - 1) * Nat.totient 333 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_667 : Nat.totient 667 = 616 := by
  calc
    Nat.totient 667 = Nat.totient (23 * 29) := by norm_num
    _ = (23 - 1) * Nat.totient 29 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 616 := by norm_num

@[simp] private theorem phi_668 : Nat.totient 668 = 332 := by
  calc
    Nat.totient 668 = Nat.totient (2 * 334) := by norm_num
    _ = 2 * Nat.totient 334 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 332 := by norm_num

@[simp] private theorem phi_669 : Nat.totient 669 = 444 := by
  calc
    Nat.totient 669 = Nat.totient (3 * 223) := by norm_num
    _ = (3 - 1) * Nat.totient 223 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 444 := by norm_num

@[simp] private theorem phi_670 : Nat.totient 670 = 264 := by
  calc
    Nat.totient 670 = Nat.totient (2 * 335) := by norm_num
    _ = (2 - 1) * Nat.totient 335 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 264 := by norm_num

@[simp] private theorem phi_671 : Nat.totient 671 = 600 := by
  calc
    Nat.totient 671 = Nat.totient (11 * 61) := by norm_num
    _ = (11 - 1) * Nat.totient 61 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 600 := by norm_num

@[simp] private theorem phi_672 : Nat.totient 672 = 192 := by
  calc
    Nat.totient 672 = Nat.totient (2 * 336) := by norm_num
    _ = 2 * Nat.totient 336 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_673 : Nat.totient 673 = 672 := by
  calc
    Nat.totient 673 = Nat.totient (673 * 1) := by norm_num
    _ = (673 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 672 := by norm_num

@[simp] private theorem phi_674 : Nat.totient 674 = 336 := by
  calc
    Nat.totient 674 = Nat.totient (2 * 337) := by norm_num
    _ = (2 - 1) * Nat.totient 337 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_675 : Nat.totient 675 = 360 := by
  calc
    Nat.totient 675 = Nat.totient (3 * 225) := by norm_num
    _ = 3 * Nat.totient 225 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_676 : Nat.totient 676 = 312 := by
  calc
    Nat.totient 676 = Nat.totient (2 * 338) := by norm_num
    _ = 2 * Nat.totient 338 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_677 : Nat.totient 677 = 676 := by
  calc
    Nat.totient 677 = Nat.totient (677 * 1) := by norm_num
    _ = (677 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 676 := by norm_num

@[simp] private theorem phi_678 : Nat.totient 678 = 224 := by
  calc
    Nat.totient 678 = Nat.totient (2 * 339) := by norm_num
    _ = (2 - 1) * Nat.totient 339 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 224 := by norm_num

@[simp] private theorem phi_679 : Nat.totient 679 = 576 := by
  calc
    Nat.totient 679 = Nat.totient (7 * 97) := by norm_num
    _ = (7 - 1) * Nat.totient 97 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 576 := by norm_num

@[simp] private theorem phi_680 : Nat.totient 680 = 256 := by
  calc
    Nat.totient 680 = Nat.totient (2 * 340) := by norm_num
    _ = 2 * Nat.totient 340 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 256 := by norm_num

@[simp] private theorem phi_681 : Nat.totient 681 = 452 := by
  calc
    Nat.totient 681 = Nat.totient (3 * 227) := by norm_num
    _ = (3 - 1) * Nat.totient 227 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 452 := by norm_num

@[simp] private theorem phi_682 : Nat.totient 682 = 300 := by
  calc
    Nat.totient 682 = Nat.totient (2 * 341) := by norm_num
    _ = (2 - 1) * Nat.totient 341 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 300 := by norm_num

@[simp] private theorem phi_683 : Nat.totient 683 = 682 := by
  calc
    Nat.totient 683 = Nat.totient (683 * 1) := by norm_num
    _ = (683 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 682 := by norm_num

@[simp] private theorem phi_684 : Nat.totient 684 = 216 := by
  calc
    Nat.totient 684 = Nat.totient (2 * 342) := by norm_num
    _ = 2 * Nat.totient 342 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_685 : Nat.totient 685 = 544 := by
  calc
    Nat.totient 685 = Nat.totient (5 * 137) := by norm_num
    _ = (5 - 1) * Nat.totient 137 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 544 := by norm_num

@[simp] private theorem phi_686 : Nat.totient 686 = 294 := by
  calc
    Nat.totient 686 = Nat.totient (2 * 343) := by norm_num
    _ = (2 - 1) * Nat.totient 343 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 294 := by norm_num

@[simp] private theorem phi_687 : Nat.totient 687 = 456 := by
  calc
    Nat.totient 687 = Nat.totient (3 * 229) := by norm_num
    _ = (3 - 1) * Nat.totient 229 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 456 := by norm_num

@[simp] private theorem phi_688 : Nat.totient 688 = 336 := by
  calc
    Nat.totient 688 = Nat.totient (2 * 344) := by norm_num
    _ = 2 * Nat.totient 344 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_689 : Nat.totient 689 = 624 := by
  calc
    Nat.totient 689 = Nat.totient (13 * 53) := by norm_num
    _ = (13 - 1) * Nat.totient 53 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 624 := by norm_num

@[simp] private theorem phi_690 : Nat.totient 690 = 176 := by
  calc
    Nat.totient 690 = Nat.totient (2 * 345) := by norm_num
    _ = (2 - 1) * Nat.totient 345 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 176 := by norm_num

@[simp] private theorem phi_691 : Nat.totient 691 = 690 := by
  calc
    Nat.totient 691 = Nat.totient (691 * 1) := by norm_num
    _ = (691 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 690 := by norm_num

@[simp] private theorem phi_692 : Nat.totient 692 = 344 := by
  calc
    Nat.totient 692 = Nat.totient (2 * 346) := by norm_num
    _ = 2 * Nat.totient 346 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 344 := by norm_num

@[simp] private theorem phi_693 : Nat.totient 693 = 360 := by
  calc
    Nat.totient 693 = Nat.totient (3 * 231) := by norm_num
    _ = 3 * Nat.totient 231 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_694 : Nat.totient 694 = 346 := by
  calc
    Nat.totient 694 = Nat.totient (2 * 347) := by norm_num
    _ = (2 - 1) * Nat.totient 347 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 346 := by norm_num

@[simp] private theorem phi_695 : Nat.totient 695 = 552 := by
  calc
    Nat.totient 695 = Nat.totient (5 * 139) := by norm_num
    _ = (5 - 1) * Nat.totient 139 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 552 := by norm_num

@[simp] private theorem phi_696 : Nat.totient 696 = 224 := by
  calc
    Nat.totient 696 = Nat.totient (2 * 348) := by norm_num
    _ = 2 * Nat.totient 348 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 224 := by norm_num

@[simp] private theorem phi_697 : Nat.totient 697 = 640 := by
  calc
    Nat.totient 697 = Nat.totient (17 * 41) := by norm_num
    _ = (17 - 1) * Nat.totient 41 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 640 := by norm_num

@[simp] private theorem phi_698 : Nat.totient 698 = 348 := by
  calc
    Nat.totient 698 = Nat.totient (2 * 349) := by norm_num
    _ = (2 - 1) * Nat.totient 349 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 348 := by norm_num

@[simp] private theorem phi_699 : Nat.totient 699 = 464 := by
  calc
    Nat.totient 699 = Nat.totient (3 * 233) := by norm_num
    _ = (3 - 1) * Nat.totient 233 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 464 := by norm_num

@[simp] private theorem phi_700 : Nat.totient 700 = 240 := by
  calc
    Nat.totient 700 = Nat.totient (2 * 350) := by norm_num
    _ = 2 * Nat.totient 350 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_701 : Nat.totient 701 = 700 := by
  calc
    Nat.totient 701 = Nat.totient (701 * 1) := by norm_num
    _ = (701 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 700 := by norm_num

@[simp] private theorem phi_702 : Nat.totient 702 = 216 := by
  calc
    Nat.totient 702 = Nat.totient (2 * 351) := by norm_num
    _ = (2 - 1) * Nat.totient 351 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_703 : Nat.totient 703 = 648 := by
  calc
    Nat.totient 703 = Nat.totient (19 * 37) := by norm_num
    _ = (19 - 1) * Nat.totient 37 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 648 := by norm_num

@[simp] private theorem phi_704 : Nat.totient 704 = 320 := by
  calc
    Nat.totient 704 = Nat.totient (2 * 352) := by norm_num
    _ = 2 * Nat.totient 352 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 320 := by norm_num

@[simp] private theorem phi_705 : Nat.totient 705 = 368 := by
  calc
    Nat.totient 705 = Nat.totient (3 * 235) := by norm_num
    _ = (3 - 1) * Nat.totient 235 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 368 := by norm_num

@[simp] private theorem phi_706 : Nat.totient 706 = 352 := by
  calc
    Nat.totient 706 = Nat.totient (2 * 353) := by norm_num
    _ = (2 - 1) * Nat.totient 353 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 352 := by norm_num

@[simp] private theorem phi_707 : Nat.totient 707 = 600 := by
  calc
    Nat.totient 707 = Nat.totient (7 * 101) := by norm_num
    _ = (7 - 1) * Nat.totient 101 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 600 := by norm_num

@[simp] private theorem phi_708 : Nat.totient 708 = 232 := by
  calc
    Nat.totient 708 = Nat.totient (2 * 354) := by norm_num
    _ = 2 * Nat.totient 354 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 232 := by norm_num

@[simp] private theorem phi_709 : Nat.totient 709 = 708 := by
  calc
    Nat.totient 709 = Nat.totient (709 * 1) := by norm_num
    _ = (709 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 708 := by norm_num

@[simp] private theorem phi_710 : Nat.totient 710 = 280 := by
  calc
    Nat.totient 710 = Nat.totient (2 * 355) := by norm_num
    _ = (2 - 1) * Nat.totient 355 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 280 := by norm_num

@[simp] private theorem phi_711 : Nat.totient 711 = 468 := by
  calc
    Nat.totient 711 = Nat.totient (3 * 237) := by norm_num
    _ = 3 * Nat.totient 237 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 468 := by norm_num

@[simp] private theorem phi_712 : Nat.totient 712 = 352 := by
  calc
    Nat.totient 712 = Nat.totient (2 * 356) := by norm_num
    _ = 2 * Nat.totient 356 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 352 := by norm_num

@[simp] private theorem phi_713 : Nat.totient 713 = 660 := by
  calc
    Nat.totient 713 = Nat.totient (23 * 31) := by norm_num
    _ = (23 - 1) * Nat.totient 31 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 660 := by norm_num

@[simp] private theorem phi_714 : Nat.totient 714 = 192 := by
  calc
    Nat.totient 714 = Nat.totient (2 * 357) := by norm_num
    _ = (2 - 1) * Nat.totient 357 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_715 : Nat.totient 715 = 480 := by
  calc
    Nat.totient 715 = Nat.totient (5 * 143) := by norm_num
    _ = (5 - 1) * Nat.totient 143 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 480 := by norm_num

@[simp] private theorem phi_716 : Nat.totient 716 = 356 := by
  calc
    Nat.totient 716 = Nat.totient (2 * 358) := by norm_num
    _ = 2 * Nat.totient 358 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 356 := by norm_num

@[simp] private theorem phi_717 : Nat.totient 717 = 476 := by
  calc
    Nat.totient 717 = Nat.totient (3 * 239) := by norm_num
    _ = (3 - 1) * Nat.totient 239 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 476 := by norm_num

@[simp] private theorem phi_718 : Nat.totient 718 = 358 := by
  calc
    Nat.totient 718 = Nat.totient (2 * 359) := by norm_num
    _ = (2 - 1) * Nat.totient 359 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 358 := by norm_num

@[simp] private theorem phi_719 : Nat.totient 719 = 718 := by
  calc
    Nat.totient 719 = Nat.totient (719 * 1) := by norm_num
    _ = (719 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 718 := by norm_num

@[simp] private theorem phi_720 : Nat.totient 720 = 192 := by
  calc
    Nat.totient 720 = Nat.totient (2 * 360) := by norm_num
    _ = 2 * Nat.totient 360 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_721 : Nat.totient 721 = 612 := by
  calc
    Nat.totient 721 = Nat.totient (7 * 103) := by norm_num
    _ = (7 - 1) * Nat.totient 103 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 612 := by norm_num

@[simp] private theorem phi_722 : Nat.totient 722 = 342 := by
  calc
    Nat.totient 722 = Nat.totient (2 * 361) := by norm_num
    _ = (2 - 1) * Nat.totient 361 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 342 := by norm_num

@[simp] private theorem phi_723 : Nat.totient 723 = 480 := by
  calc
    Nat.totient 723 = Nat.totient (3 * 241) := by norm_num
    _ = (3 - 1) * Nat.totient 241 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 480 := by norm_num

@[simp] private theorem phi_724 : Nat.totient 724 = 360 := by
  calc
    Nat.totient 724 = Nat.totient (2 * 362) := by norm_num
    _ = 2 * Nat.totient 362 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_725 : Nat.totient 725 = 560 := by
  calc
    Nat.totient 725 = Nat.totient (5 * 145) := by norm_num
    _ = 5 * Nat.totient 145 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 560 := by norm_num

@[simp] private theorem phi_726 : Nat.totient 726 = 220 := by
  calc
    Nat.totient 726 = Nat.totient (2 * 363) := by norm_num
    _ = (2 - 1) * Nat.totient 363 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 220 := by norm_num

@[simp] private theorem phi_727 : Nat.totient 727 = 726 := by
  calc
    Nat.totient 727 = Nat.totient (727 * 1) := by norm_num
    _ = (727 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 726 := by norm_num

@[simp] private theorem phi_728 : Nat.totient 728 = 288 := by
  calc
    Nat.totient 728 = Nat.totient (2 * 364) := by norm_num
    _ = 2 * Nat.totient 364 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_729 : Nat.totient 729 = 486 := by
  calc
    Nat.totient 729 = Nat.totient (3 * 243) := by norm_num
    _ = 3 * Nat.totient 243 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 486 := by norm_num

@[simp] private theorem phi_730 : Nat.totient 730 = 288 := by
  calc
    Nat.totient 730 = Nat.totient (2 * 365) := by norm_num
    _ = (2 - 1) * Nat.totient 365 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_731 : Nat.totient 731 = 672 := by
  calc
    Nat.totient 731 = Nat.totient (17 * 43) := by norm_num
    _ = (17 - 1) * Nat.totient 43 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 672 := by norm_num

@[simp] private theorem phi_732 : Nat.totient 732 = 240 := by
  calc
    Nat.totient 732 = Nat.totient (2 * 366) := by norm_num
    _ = 2 * Nat.totient 366 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_733 : Nat.totient 733 = 732 := by
  calc
    Nat.totient 733 = Nat.totient (733 * 1) := by norm_num
    _ = (733 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 732 := by norm_num

@[simp] private theorem phi_734 : Nat.totient 734 = 366 := by
  calc
    Nat.totient 734 = Nat.totient (2 * 367) := by norm_num
    _ = (2 - 1) * Nat.totient 367 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 366 := by norm_num

@[simp] private theorem phi_735 : Nat.totient 735 = 336 := by
  calc
    Nat.totient 735 = Nat.totient (3 * 245) := by norm_num
    _ = (3 - 1) * Nat.totient 245 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_736 : Nat.totient 736 = 352 := by
  calc
    Nat.totient 736 = Nat.totient (2 * 368) := by norm_num
    _ = 2 * Nat.totient 368 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 352 := by norm_num

@[simp] private theorem phi_737 : Nat.totient 737 = 660 := by
  calc
    Nat.totient 737 = Nat.totient (11 * 67) := by norm_num
    _ = (11 - 1) * Nat.totient 67 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 660 := by norm_num

@[simp] private theorem phi_738 : Nat.totient 738 = 240 := by
  calc
    Nat.totient 738 = Nat.totient (2 * 369) := by norm_num
    _ = (2 - 1) * Nat.totient 369 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_739 : Nat.totient 739 = 738 := by
  calc
    Nat.totient 739 = Nat.totient (739 * 1) := by norm_num
    _ = (739 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 738 := by norm_num

@[simp] private theorem phi_740 : Nat.totient 740 = 288 := by
  calc
    Nat.totient 740 = Nat.totient (2 * 370) := by norm_num
    _ = 2 * Nat.totient 370 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_741 : Nat.totient 741 = 432 := by
  calc
    Nat.totient 741 = Nat.totient (3 * 247) := by norm_num
    _ = (3 - 1) * Nat.totient 247 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 432 := by norm_num

@[simp] private theorem phi_742 : Nat.totient 742 = 312 := by
  calc
    Nat.totient 742 = Nat.totient (2 * 371) := by norm_num
    _ = (2 - 1) * Nat.totient 371 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_743 : Nat.totient 743 = 742 := by
  calc
    Nat.totient 743 = Nat.totient (743 * 1) := by norm_num
    _ = (743 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 742 := by norm_num

@[simp] private theorem phi_744 : Nat.totient 744 = 240 := by
  calc
    Nat.totient 744 = Nat.totient (2 * 372) := by norm_num
    _ = 2 * Nat.totient 372 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_745 : Nat.totient 745 = 592 := by
  calc
    Nat.totient 745 = Nat.totient (5 * 149) := by norm_num
    _ = (5 - 1) * Nat.totient 149 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 592 := by norm_num

@[simp] private theorem phi_746 : Nat.totient 746 = 372 := by
  calc
    Nat.totient 746 = Nat.totient (2 * 373) := by norm_num
    _ = (2 - 1) * Nat.totient 373 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 372 := by norm_num

@[simp] private theorem phi_747 : Nat.totient 747 = 492 := by
  calc
    Nat.totient 747 = Nat.totient (3 * 249) := by norm_num
    _ = 3 * Nat.totient 249 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 492 := by norm_num

@[simp] private theorem phi_748 : Nat.totient 748 = 320 := by
  calc
    Nat.totient 748 = Nat.totient (2 * 374) := by norm_num
    _ = 2 * Nat.totient 374 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 320 := by norm_num

@[simp] private theorem phi_749 : Nat.totient 749 = 636 := by
  calc
    Nat.totient 749 = Nat.totient (7 * 107) := by norm_num
    _ = (7 - 1) * Nat.totient 107 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 636 := by norm_num

@[simp] private theorem phi_750 : Nat.totient 750 = 200 := by
  calc
    Nat.totient 750 = Nat.totient (2 * 375) := by norm_num
    _ = (2 - 1) * Nat.totient 375 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 200 := by norm_num

@[simp] private theorem phi_751 : Nat.totient 751 = 750 := by
  calc
    Nat.totient 751 = Nat.totient (751 * 1) := by norm_num
    _ = (751 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 750 := by norm_num

@[simp] private theorem phi_752 : Nat.totient 752 = 368 := by
  calc
    Nat.totient 752 = Nat.totient (2 * 376) := by norm_num
    _ = 2 * Nat.totient 376 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 368 := by norm_num

@[simp] private theorem phi_753 : Nat.totient 753 = 500 := by
  calc
    Nat.totient 753 = Nat.totient (3 * 251) := by norm_num
    _ = (3 - 1) * Nat.totient 251 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 500 := by norm_num

@[simp] private theorem phi_754 : Nat.totient 754 = 336 := by
  calc
    Nat.totient 754 = Nat.totient (2 * 377) := by norm_num
    _ = (2 - 1) * Nat.totient 377 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_755 : Nat.totient 755 = 600 := by
  calc
    Nat.totient 755 = Nat.totient (5 * 151) := by norm_num
    _ = (5 - 1) * Nat.totient 151 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 600 := by norm_num

@[simp] private theorem phi_756 : Nat.totient 756 = 216 := by
  calc
    Nat.totient 756 = Nat.totient (2 * 378) := by norm_num
    _ = 2 * Nat.totient 378 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_757 : Nat.totient 757 = 756 := by
  calc
    Nat.totient 757 = Nat.totient (757 * 1) := by norm_num
    _ = (757 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 756 := by norm_num

@[simp] private theorem phi_758 : Nat.totient 758 = 378 := by
  calc
    Nat.totient 758 = Nat.totient (2 * 379) := by norm_num
    _ = (2 - 1) * Nat.totient 379 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 378 := by norm_num

@[simp] private theorem phi_759 : Nat.totient 759 = 440 := by
  calc
    Nat.totient 759 = Nat.totient (3 * 253) := by norm_num
    _ = (3 - 1) * Nat.totient 253 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 440 := by norm_num

@[simp] private theorem phi_760 : Nat.totient 760 = 288 := by
  calc
    Nat.totient 760 = Nat.totient (2 * 380) := by norm_num
    _ = 2 * Nat.totient 380 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 288 := by norm_num

@[simp] private theorem phi_761 : Nat.totient 761 = 760 := by
  calc
    Nat.totient 761 = Nat.totient (761 * 1) := by norm_num
    _ = (761 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 760 := by norm_num

@[simp] private theorem phi_762 : Nat.totient 762 = 252 := by
  calc
    Nat.totient 762 = Nat.totient (2 * 381) := by norm_num
    _ = (2 - 1) * Nat.totient 381 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 252 := by norm_num

@[simp] private theorem phi_763 : Nat.totient 763 = 648 := by
  calc
    Nat.totient 763 = Nat.totient (7 * 109) := by norm_num
    _ = (7 - 1) * Nat.totient 109 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 648 := by norm_num

@[simp] private theorem phi_764 : Nat.totient 764 = 380 := by
  calc
    Nat.totient 764 = Nat.totient (2 * 382) := by norm_num
    _ = 2 * Nat.totient 382 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 380 := by norm_num

@[simp] private theorem phi_765 : Nat.totient 765 = 384 := by
  calc
    Nat.totient 765 = Nat.totient (3 * 255) := by norm_num
    _ = 3 * Nat.totient 255 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 384 := by norm_num

@[simp] private theorem phi_766 : Nat.totient 766 = 382 := by
  calc
    Nat.totient 766 = Nat.totient (2 * 383) := by norm_num
    _ = (2 - 1) * Nat.totient 383 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 382 := by norm_num

@[simp] private theorem phi_767 : Nat.totient 767 = 696 := by
  calc
    Nat.totient 767 = Nat.totient (13 * 59) := by norm_num
    _ = (13 - 1) * Nat.totient 59 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 696 := by norm_num

@[simp] private theorem phi_768 : Nat.totient 768 = 256 := by
  calc
    Nat.totient 768 = Nat.totient (2 * 384) := by norm_num
    _ = 2 * Nat.totient 384 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 256 := by norm_num

@[simp] private theorem phi_769 : Nat.totient 769 = 768 := by
  calc
    Nat.totient 769 = Nat.totient (769 * 1) := by norm_num
    _ = (769 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 768 := by norm_num

@[simp] private theorem phi_770 : Nat.totient 770 = 240 := by
  calc
    Nat.totient 770 = Nat.totient (2 * 385) := by norm_num
    _ = (2 - 1) * Nat.totient 385 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_771 : Nat.totient 771 = 512 := by
  calc
    Nat.totient 771 = Nat.totient (3 * 257) := by norm_num
    _ = (3 - 1) * Nat.totient 257 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 512 := by norm_num

@[simp] private theorem phi_772 : Nat.totient 772 = 384 := by
  calc
    Nat.totient 772 = Nat.totient (2 * 386) := by norm_num
    _ = 2 * Nat.totient 386 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 384 := by norm_num

@[simp] private theorem phi_773 : Nat.totient 773 = 772 := by
  calc
    Nat.totient 773 = Nat.totient (773 * 1) := by norm_num
    _ = (773 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 772 := by norm_num

@[simp] private theorem phi_774 : Nat.totient 774 = 252 := by
  calc
    Nat.totient 774 = Nat.totient (2 * 387) := by norm_num
    _ = (2 - 1) * Nat.totient 387 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 252 := by norm_num

@[simp] private theorem phi_775 : Nat.totient 775 = 600 := by
  calc
    Nat.totient 775 = Nat.totient (5 * 155) := by norm_num
    _ = 5 * Nat.totient 155 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 600 := by norm_num

@[simp] private theorem phi_776 : Nat.totient 776 = 384 := by
  calc
    Nat.totient 776 = Nat.totient (2 * 388) := by norm_num
    _ = 2 * Nat.totient 388 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 384 := by norm_num

@[simp] private theorem phi_777 : Nat.totient 777 = 432 := by
  calc
    Nat.totient 777 = Nat.totient (3 * 259) := by norm_num
    _ = (3 - 1) * Nat.totient 259 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 432 := by norm_num

@[simp] private theorem phi_778 : Nat.totient 778 = 388 := by
  calc
    Nat.totient 778 = Nat.totient (2 * 389) := by norm_num
    _ = (2 - 1) * Nat.totient 389 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 388 := by norm_num

@[simp] private theorem phi_779 : Nat.totient 779 = 720 := by
  calc
    Nat.totient 779 = Nat.totient (19 * 41) := by norm_num
    _ = (19 - 1) * Nat.totient 41 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 720 := by norm_num

@[simp] private theorem phi_780 : Nat.totient 780 = 192 := by
  calc
    Nat.totient 780 = Nat.totient (2 * 390) := by norm_num
    _ = 2 * Nat.totient 390 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 192 := by norm_num

@[simp] private theorem phi_781 : Nat.totient 781 = 700 := by
  calc
    Nat.totient 781 = Nat.totient (11 * 71) := by norm_num
    _ = (11 - 1) * Nat.totient 71 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 700 := by norm_num

@[simp] private theorem phi_782 : Nat.totient 782 = 352 := by
  calc
    Nat.totient 782 = Nat.totient (2 * 391) := by norm_num
    _ = (2 - 1) * Nat.totient 391 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 352 := by norm_num

@[simp] private theorem phi_783 : Nat.totient 783 = 504 := by
  calc
    Nat.totient 783 = Nat.totient (3 * 261) := by norm_num
    _ = 3 * Nat.totient 261 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 504 := by norm_num

@[simp] private theorem phi_784 : Nat.totient 784 = 336 := by
  calc
    Nat.totient 784 = Nat.totient (2 * 392) := by norm_num
    _ = 2 * Nat.totient 392 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_785 : Nat.totient 785 = 624 := by
  calc
    Nat.totient 785 = Nat.totient (5 * 157) := by norm_num
    _ = (5 - 1) * Nat.totient 157 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 624 := by norm_num

@[simp] private theorem phi_786 : Nat.totient 786 = 260 := by
  calc
    Nat.totient 786 = Nat.totient (2 * 393) := by norm_num
    _ = (2 - 1) * Nat.totient 393 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 260 := by norm_num

@[simp] private theorem phi_787 : Nat.totient 787 = 786 := by
  calc
    Nat.totient 787 = Nat.totient (787 * 1) := by norm_num
    _ = (787 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 786 := by norm_num

@[simp] private theorem phi_788 : Nat.totient 788 = 392 := by
  calc
    Nat.totient 788 = Nat.totient (2 * 394) := by norm_num
    _ = 2 * Nat.totient 394 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 392 := by norm_num

@[simp] private theorem phi_789 : Nat.totient 789 = 524 := by
  calc
    Nat.totient 789 = Nat.totient (3 * 263) := by norm_num
    _ = (3 - 1) * Nat.totient 263 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 524 := by norm_num

@[simp] private theorem phi_790 : Nat.totient 790 = 312 := by
  calc
    Nat.totient 790 = Nat.totient (2 * 395) := by norm_num
    _ = (2 - 1) * Nat.totient 395 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 312 := by norm_num

@[simp] private theorem phi_791 : Nat.totient 791 = 672 := by
  calc
    Nat.totient 791 = Nat.totient (7 * 113) := by norm_num
    _ = (7 - 1) * Nat.totient 113 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 672 := by norm_num

@[simp] private theorem phi_792 : Nat.totient 792 = 240 := by
  calc
    Nat.totient 792 = Nat.totient (2 * 396) := by norm_num
    _ = 2 * Nat.totient 396 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 240 := by norm_num

@[simp] private theorem phi_793 : Nat.totient 793 = 720 := by
  calc
    Nat.totient 793 = Nat.totient (13 * 61) := by norm_num
    _ = (13 - 1) * Nat.totient 61 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 720 := by norm_num

@[simp] private theorem phi_794 : Nat.totient 794 = 396 := by
  calc
    Nat.totient 794 = Nat.totient (2 * 397) := by norm_num
    _ = (2 - 1) * Nat.totient 397 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 396 := by norm_num

@[simp] private theorem phi_795 : Nat.totient 795 = 416 := by
  calc
    Nat.totient 795 = Nat.totient (3 * 265) := by norm_num
    _ = (3 - 1) * Nat.totient 265 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 416 := by norm_num

@[simp] private theorem phi_796 : Nat.totient 796 = 396 := by
  calc
    Nat.totient 796 = Nat.totient (2 * 398) := by norm_num
    _ = 2 * Nat.totient 398 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 396 := by norm_num

@[simp] private theorem phi_797 : Nat.totient 797 = 796 := by
  calc
    Nat.totient 797 = Nat.totient (797 * 1) := by norm_num
    _ = (797 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 796 := by norm_num

@[simp] private theorem phi_798 : Nat.totient 798 = 216 := by
  calc
    Nat.totient 798 = Nat.totient (2 * 399) := by norm_num
    _ = (2 - 1) * Nat.totient 399 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_799 : Nat.totient 799 = 736 := by
  calc
    Nat.totient 799 = Nat.totient (17 * 47) := by norm_num
    _ = (17 - 1) * Nat.totient 47 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 736 := by norm_num

@[simp] private theorem phi_800 : Nat.totient 800 = 320 := by
  calc
    Nat.totient 800 = Nat.totient (2 * 400) := by norm_num
    _ = 2 * Nat.totient 400 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 320 := by norm_num

@[simp] private theorem phi_801 : Nat.totient 801 = 528 := by
  calc
    Nat.totient 801 = Nat.totient (3 * 267) := by norm_num
    _ = 3 * Nat.totient 267 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 528 := by norm_num

@[simp] private theorem phi_802 : Nat.totient 802 = 400 := by
  calc
    Nat.totient 802 = Nat.totient (2 * 401) := by norm_num
    _ = (2 - 1) * Nat.totient 401 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 400 := by norm_num

@[simp] private theorem phi_803 : Nat.totient 803 = 720 := by
  calc
    Nat.totient 803 = Nat.totient (11 * 73) := by norm_num
    _ = (11 - 1) * Nat.totient 73 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 720 := by norm_num

@[simp] private theorem phi_804 : Nat.totient 804 = 264 := by
  calc
    Nat.totient 804 = Nat.totient (2 * 402) := by norm_num
    _ = 2 * Nat.totient 402 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 264 := by norm_num

@[simp] private theorem phi_805 : Nat.totient 805 = 528 := by
  calc
    Nat.totient 805 = Nat.totient (5 * 161) := by norm_num
    _ = (5 - 1) * Nat.totient 161 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 528 := by norm_num

@[simp] private theorem phi_806 : Nat.totient 806 = 360 := by
  calc
    Nat.totient 806 = Nat.totient (2 * 403) := by norm_num
    _ = (2 - 1) * Nat.totient 403 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_807 : Nat.totient 807 = 536 := by
  calc
    Nat.totient 807 = Nat.totient (3 * 269) := by norm_num
    _ = (3 - 1) * Nat.totient 269 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 536 := by norm_num

@[simp] private theorem phi_808 : Nat.totient 808 = 400 := by
  calc
    Nat.totient 808 = Nat.totient (2 * 404) := by norm_num
    _ = 2 * Nat.totient 404 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 400 := by norm_num

@[simp] private theorem phi_809 : Nat.totient 809 = 808 := by
  calc
    Nat.totient 809 = Nat.totient (809 * 1) := by norm_num
    _ = (809 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 808 := by norm_num

@[simp] private theorem phi_810 : Nat.totient 810 = 216 := by
  calc
    Nat.totient 810 = Nat.totient (2 * 405) := by norm_num
    _ = (2 - 1) * Nat.totient 405 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 216 := by norm_num

@[simp] private theorem phi_811 : Nat.totient 811 = 810 := by
  calc
    Nat.totient 811 = Nat.totient (811 * 1) := by norm_num
    _ = (811 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 810 := by norm_num

@[simp] private theorem phi_812 : Nat.totient 812 = 336 := by
  calc
    Nat.totient 812 = Nat.totient (2 * 406) := by norm_num
    _ = 2 * Nat.totient 406 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 336 := by norm_num

@[simp] private theorem phi_813 : Nat.totient 813 = 540 := by
  calc
    Nat.totient 813 = Nat.totient (3 * 271) := by norm_num
    _ = (3 - 1) * Nat.totient 271 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 540 := by norm_num

@[simp] private theorem phi_814 : Nat.totient 814 = 360 := by
  calc
    Nat.totient 814 = Nat.totient (2 * 407) := by norm_num
    _ = (2 - 1) * Nat.totient 407 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 360 := by norm_num

@[simp] private theorem phi_815 : Nat.totient 815 = 648 := by
  calc
    Nat.totient 815 = Nat.totient (5 * 163) := by norm_num
    _ = (5 - 1) * Nat.totient 163 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 648 := by norm_num

@[simp] private theorem phi_816 : Nat.totient 816 = 256 := by
  calc
    Nat.totient 816 = Nat.totient (2 * 408) := by norm_num
    _ = 2 * Nat.totient 408 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 256 := by norm_num

@[simp] private theorem phi_817 : Nat.totient 817 = 756 := by
  calc
    Nat.totient 817 = Nat.totient (19 * 43) := by norm_num
    _ = (19 - 1) * Nat.totient 43 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 756 := by norm_num

@[simp] private theorem phi_818 : Nat.totient 818 = 408 := by
  calc
    Nat.totient 818 = Nat.totient (2 * 409) := by norm_num
    _ = (2 - 1) * Nat.totient 409 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 408 := by norm_num

@[simp] private theorem phi_819 : Nat.totient 819 = 432 := by
  calc
    Nat.totient 819 = Nat.totient (3 * 273) := by norm_num
    _ = 3 * Nat.totient 273 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 432 := by norm_num

@[simp] private theorem phi_820 : Nat.totient 820 = 320 := by
  calc
    Nat.totient 820 = Nat.totient (2 * 410) := by norm_num
    _ = 2 * Nat.totient 410 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 320 := by norm_num

@[simp] private theorem phi_821 : Nat.totient 821 = 820 := by
  calc
    Nat.totient 821 = Nat.totient (821 * 1) := by norm_num
    _ = (821 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 820 := by norm_num

@[simp] private theorem phi_822 : Nat.totient 822 = 272 := by
  calc
    Nat.totient 822 = Nat.totient (2 * 411) := by norm_num
    _ = (2 - 1) * Nat.totient 411 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 272 := by norm_num

@[simp] private theorem phi_823 : Nat.totient 823 = 822 := by
  calc
    Nat.totient 823 = Nat.totient (823 * 1) := by norm_num
    _ = (823 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 822 := by norm_num

@[simp] private theorem phi_824 : Nat.totient 824 = 408 := by
  calc
    Nat.totient 824 = Nat.totient (2 * 412) := by norm_num
    _ = 2 * Nat.totient 412 :=
      Nat.totient_mul_of_prime_of_dvd (by norm_num) (by norm_num)
    _ = 408 := by norm_num

@[simp] private theorem phi_825 : Nat.totient 825 = 400 := by
  calc
    Nat.totient 825 = Nat.totient (3 * 275) := by norm_num
    _ = (3 - 1) * Nat.totient 275 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 400 := by norm_num

@[simp] private theorem phi_826 : Nat.totient 826 = 348 := by
  calc
    Nat.totient 826 = Nat.totient (2 * 413) := by norm_num
    _ = (2 - 1) * Nat.totient 413 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 348 := by norm_num

@[simp] private theorem phi_827 : Nat.totient 827 = 826 := by
  calc
    Nat.totient 827 = Nat.totient (827 * 1) := by norm_num
    _ = (827 - 1) * Nat.totient 1 :=
      Nat.totient_mul_of_prime_of_not_dvd (by norm_num) (by norm_num)
    _ = 826 := by norm_num

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- The decreasing four-pattern first appears on `823, ..., 826`. -/
theorem decreasing_first_endpoint_826 : FirstStart decreasingAt 822 := by
  constructor
  · norm_num [decreasingAt]
  · intro m
    fin_cases m <;> norm_num [decreasingAt]

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- The four-pattern `(3,2,1,4)` first appears on `824, ..., 827`. -/
theorem threeTwoOneFour_first_endpoint_827 :
    FirstStart threeTwoOneFourAt 823 := by
  constructor
  · norm_num [threeTwoOneFourAt]
  · intro m
    fin_cases m <;> norm_num [threeTwoOneFourAt]

/-- Therefore the decreasing four-pattern is not the last pattern to make its
first appearance. -/
theorem decreasing_not_last :
    822 + 4 < 823 + 4 ∧
      FirstStart decreasingAt 822 ∧ FirstStart threeTwoOneFourAt 823 := by
  exact ⟨by norm_num, decreasing_first_endpoint_826,
    threeTwoOneFour_first_endpoint_827⟩

/-- The first two positive integers have equal Euler totients. -/
theorem totient_one_eq_totient_two : Nat.totient 1 = Nat.totient 2 := by
  rw [Nat.totient_one, Nat.totient_two]

#print axioms decreasing_first_endpoint_826
#print axioms threeTwoOneFour_first_endpoint_827
#print axioms decreasing_not_last
#print axioms totient_one_eq_totient_two

end Erdos415.FiniteCert
