Section Prop_5_4_1.

Context (X : Metric_Space).
Notation "'dist(' x , y )" := (dist X x y)
  (format "'dist(' x ,  y ')'").

Variable (p : X).

(* To invoke metric space properties of the distance function on X, you have to write "By (dist_positive X), ..." or another property analogously *)
Check (dist_positive X).
Check (dist_non_degenerate X).
Check (dist_symmetric X).
Check (dist_triangle_inequality X).
Check (dist_reflexive X).

Definition a (n : ℕ) := p.

Lemma exercise_5_9_1 : a _converges to_ p.
Proof.
We need to show that (∀ ε > 0, ∃ N1 ∈ ℕ, ∀ n ≥ N1, dist(a(n), p) < ε).