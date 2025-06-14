Module Exercise_2_7_3.

Notation "'d(' a , b )" := (d_discrete_R a b) (format "'d(' a ,  b ')'").

(* Natural-languge definition of distance function d (d_discrete_R): *)
(* d(x, y) = *)
(* = 0, if (x = y) *)
(* = 3, if (x ≠ y) *)

Lemma d_reflexive : ∀ a ∈ ℝ, d(a, a) = 0.
Proof.