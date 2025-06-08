Lemma not_closed : ¬ ([0,1) is _closed_).
Proof.
We need to show that (¬ ℝ\[0, 1) is _open_).
We need to show that (¬ (∀ a,
                           (ℝ\[0, 1)) a
                           ⇨ a is an _interior point_ of ℝ\[0, 1))).
We need to show that (¬ (∀ a,
                           (ℝ\[0, 1)) a
                           ⇨ ∃ r > 0, ∀ x ∈ B(a, r), x ∈ ℝ\[0, 1))).