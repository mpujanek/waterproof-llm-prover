Section Exercise_2_7_1.

Variable (Y : Metric_Space) (X : Set) (f : X → Y).
Hypothesis f_is_injective : Injective f.

Notation "'dist_Y(' x , z )" := (dist Y x z) (format "'dist_Y(' x ,  z ')'").

(* To invoke metric space properties of the distance function on Y, you have to write "By (dist_positive Y), ..." or another property analogously *)
Check (dist_positive Y).
Check (dist_non_degenerate Y).
Check (dist_symmetric Y).
Check (dist_triangle_inequality Y).
Check (dist_reflexive Y).

Variable d : X → X → ℝ.
Hypothesis definition_d :
  ∀ x ∈ X, ∀ z ∈ X, d(x, z) = dist_Y(f(x), f(z)).

Lemma d_reflexive : ∀ x ∈ X, d(x, x) = 0.
Proof.