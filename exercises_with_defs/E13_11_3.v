Section exercise_13_11_3.

Variable Y : Metric_Space.
Notation "'dist_Y(' x , z )" := (dist Y x z) (format "'dist_Y(' x ,  z ')'").
Variable a : ℕ → Y.

Lemma exercise_13_11_3 :
  ∀ n ∈ ℕ, a is _continuous_ in n.
Proof.