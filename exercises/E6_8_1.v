Variable a : ℕ → ℝ.

Lemma exercise_6_8_1 :
  (a is _bounded_)
    ⇔
  (a is _bounded above_ ∧ a is _bounded below_).
Proof.
By application_of_prop_5_2_2 it suffices to show that
  ((∃ M > 0, ∀ n ∈ ℕ, | a(n) | ≤ M)
    ⇔
  (a is _bounded above_ ∧ a is _bounded below_)).