Module Exercise_2_7_3.

Notation "'d(' a , b )" := (d_discrete_R a b) (format "'d(' a ,  b ')'").

Lemma d_triangle_inequality :
  ∀ a ∈ ℝ, ∀ b ∈ ℝ, ∀ c ∈ ℝ, d(a, c) ≤ d(a, b) + d(b, c).
Proof.