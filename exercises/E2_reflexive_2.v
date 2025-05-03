Module Exercise_2_7_3.

Notation "'d(' a , b )" := (d_discrete_R a b) (format "'d(' a ,  b ')'").

Lemma d_reflexive : ∀ a ∈ ℝ, d(a, a) = 0.
Proof.