Lemma ex_4_9_1 : ∀ a ∈ ℝ, ∀ b ∈ ℝ, a < b ⇒
    a is the infimum of [a,b).
Proof.
We need to show that (∀ a ∈ ℝ,
                        ∀ b ∈ ℝ,
                        a < b
                        ⇨ a is a _lower bound_ for [a, b)
                          ∧ (∀ l ∈ ℝ, l is a _lower bound_ for [a, b) ⇨ l ≤ a)).
Expand the definition of lower bound.
We need to show that (∀ a ∈ ℝ,
                        ∀ b ∈ ℝ,
                        a < b
                        ⇨ (∀ a0 ∈ [a, b), a ≤ a0)
                          ∧ (∀ l ∈ ℝ, (∀ a0 ∈ [a, b), l ≤ a0) ⇨ l ≤ a)).