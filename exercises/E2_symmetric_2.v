Notation "'d(' a , b )" := (d_discrete_R a b) (format "'d(' a ,  b ')'").

Lemma d_symmetric : ∀ a ∈ ℝ, ∀ b ∈ ℝ, d(a, b) = d(b, a).
Proof.