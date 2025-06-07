Lemma not_open : ¬ ([0,1) is _open_).
Proof.
We need to show that (¬ (∀ a, [0, 1) a ⇨ a is an _interior point_ of [0, 1))).
Expand the definition of interior point.
We need to show that (¬ (∀ a, [0, 1) a ⇨ ∃ r > 0, ∀ x ∈ B(a, r), x ∈ [0, 1))).