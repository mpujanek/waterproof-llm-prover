Definition f (x : ℝ) := x.

Lemma exercise_13_11_2 : ∀ a ∈ ℝ, f is _continuous_ in a.
Proof.
We need to show that (∀ a ∈ ℝ,
                        a is an _accumulation point_
                        ∧ _limit_ of f in a is f(a)
                        ∨ a is an _isolated point_).
We need to show that (∀ a ∈ ℝ,
                        (∀ ε > 0, ∃ x ∈ ℝ, 0 < |x - a| < ε)
                        ∧ _limit_ of f in a is f(a)
                        ∨ a is an _isolated point_).
We need to show that (∀ a ∈ ℝ,
                        (∀ ε > 0, ∃ x ∈ ℝ, 0 < |x - a| < ε)
                        ∧ (∀ ε > 0,
                           ∃ δ > 0,
                           ∀ x ∈ ℝ, 0 < |x - a| < δ ⇨ |f(x) - f(a)| < ε)
                        ∨ a is an _isolated point_).
We need to show that (∀ a ∈ ℝ,
                        (∀ ε > 0, ∃ x ∈ ℝ, 0 < |x - a| < ε)
                        ∧ (∀ ε > 0,
                           ∃ δ > 0,
                           ∀ x ∈ ℝ, 0 < |x - a| < δ ⇨ |f(x) - f(a)| < ε)
                        ∨ (∃ ε > 0, ∀ x ∈ ℝ, |x - a| = 0 ∨ ε ≤ |x - a|)).