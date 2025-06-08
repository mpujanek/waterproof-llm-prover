Section exercise_10_7_3.

Variable (X : Metric_Space) (a b : ℕ → X) (p : X).
Notation "'dist(' x , y )" := (dist X x y) (format "'dist(' x ,  y ')'").

Hypothesis (a_converges_to_p : a converges to p).

Definition c (k : ℕ) := if k is even then a(k) else b(k).

Open Scope nat_scope.

Definition n (k : nat) := (2 * k).

Lemma n_is_index_sequence : n is an _index sequence_.
Proof.