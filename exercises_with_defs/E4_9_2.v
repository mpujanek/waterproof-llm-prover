Section ex_4_9_2.

Variable A : subset(ℝ).
Hypothesis A_bdd_above : (∃ b ∈ ℝ, b is an _upper bound_ for A).
Hypothesis A_nonempty : (∃ a ∈ ℝ, a ∈ A).

Lemma ex_4_9_2 : ∀ y ∈ ℝ, (y is the _supremum_ of A) ∧ (y ∈ A) ⇒
  y is the _maximum_ of A.
Proof.
We need to show that (∀ y ∈ ℝ,
                        y is the _supremum_ of A ∧ y ∈ A
                        ⇨ y ∈ A ∧ y is an _upper bound_ for A).
We need to show that (∀ y ∈ ℝ,
                        (y is an _upper bound_ for A
                         ∧ (∀ L ∈ ℝ, L is an _upper bound_ for A ⇨ y ≤ L))
                        ∧ y ∈ A ⇨ y ∈ A ∧ y is an _upper bound_ for A).
We need to show that (∀ y ∈ ℝ,
                        ((∀ a ∈ A, a ≤ y)
                         ∧ (∀ L ∈ ℝ, (∀ a ∈ A, a ≤ L) ⇨ y ≤ L)) ∧ 
                        y ∈ A ⇨ y ∈ A ∧ (∀ a ∈ A, a ≤ y)).