Variable (Y : Metric_Space) (X : Set) (f : X → Y).
Hypothesis f_is_injective : Injective f.

Notation "'dist_Y(' x , z )" := (dist Y x z) (format "'dist_Y(' x ,  z ')'").

Variable d : X -> X -> ℝ.
Hypothesis definition_d :
  ∀ x ∈ X, ∀ z ∈ X, d(x, z) = dist_Y(f(x), f(z)).

Lemma d_positive : ∀ x ∈ X, ∀ y ∈ X, d(x, y) ≥ 0.
Proof.