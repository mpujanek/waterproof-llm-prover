Module Exercise_2_7_3.

Notation "'d(' a , b )" := (d_discrete_R a b) (format "'d(' a ,  b ')'").

Lemma d_non_degenerate :
  ∀ a ∈ ℝ, ∀ b ∈ ℝ, (d(a, b) = 0) ⇒ (a = b).
Proof.