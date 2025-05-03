Variable A : subset(ℝ).
Hypothesis A_bdd_above : (∃ b ∈ ℝ, b is an _upper bound_ for A).
Hypothesis A_nonempty : (∃ a ∈ ℝ, a ∈ A).

Lemma ex_4_9_2 : ∀ y ∈ ℝ, (y is the _supremum_ of A) ∧ (y ∈ A) ⇒
  y is the _maximum_ of A.
Proof.