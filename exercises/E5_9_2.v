Section Prop_5_8_1.

Context (X : Metric_Space).
Notation "'dist(' x , y )" := (dist X x y)
  (format "'dist(' x ,  y ')'").

Variables (a : ℕ → X) (k : ℕ) (p : X).

Definition a_shift (n : nat) := a (n + k)%nat.

Lemma exercise_5_9_2 :
  (a _converges to_ p) ⇔ (a_shift _converges to_ p).
Proof.
We show both directions.
- We need to show that
    (a _converges to_ p ⇒ a_shift _converges to_ p).
  Assume that (a converges to p) (i).
  By (i) it holds that
    (∀ ε1 > 0, ∃ N2 ∈ ℕ, ∀ n ≥ N2, dist(a(n), p) < ε1) (ii).
  We need to show that (∀ ε > 0, ∃ N1 ∈ ℕ,
    ∀ n ≥ N1, dist(a_shift(n), p) < ε).
  Take ε > 0.
  Use ε1 := ε in (ii).
  { Indeed, (ε > 0). }
  It holds that (∃ N2 ∈ ℕ,
      ∀ n ≥ N2, dist(a(n), p) < ε).
  Obtain such an N2.