Section Prop_5_4_1.

Context (X : Metric_Space).
Notation "'dist(' x , y )" := (dist X x y)
  (format "'dist(' x ,  y ')'").

Variable (p : X).
Definition a (n : ℕ) := p.

Lemma exercise_5_9_1 : a _converges to_ p.
Proof.
We need to show that (∀ ε > 0, ∃ N1 ∈ ℕ, ∀ n ≥ N1, dist(a(n), p) < ε).