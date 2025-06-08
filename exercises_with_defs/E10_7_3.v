Section exercise_10_7_3.

Variable (X : Metric_Space) (a b : ℕ → X) (p : X).
Notation "'dist(' x , y )" := (dist X x y) (format "'dist(' x ,  y ')'").

Hypothesis (a_converges_to_p : a converges to p).

Definition c (k : ℕ) := if k is even then a(k) else b(k).

Open Scope nat_scope.

Definition n (k : nat) := (2 * k).

Lemma n_is_index_sequence : n is an _index sequence_.
Proof.
We need to show that (∀ k ∈ ℕ, n(k) < n(k + 1)).
Take k ∈ ℕ.
We need to show that (n(k) < n(k + 1))%nat.
We need to show that (2 * k < 2 * (k + 1))%nat.
It holds that (2 * k < 2 * k + 2)%nat.
It holds that (2 * k + 2 = 2 * (k + 1))%nat.
We conclude that (& 2 * k < 2 * k + 2 = 2 * (k + 1))%nat.
Qed.

Lemma c_n_k_equals_a_n_k : ∀ k ∈ ℕ, c(n(k)) = a(n(k)).
Proof.
Take k ∈ ℕ.
It holds that
  (c(n(k)) = if n(k) is even then a(n(k)) else b(n(k))).
It holds that (n(k) is even = true).
We conclude that (c(n(k)) = a(n(k))).
Qed.

Lemma exercise_10_7_3 :
  p is an _accumulation point_ of c.
Proof.
We need to show that
  (∃ k : ℕ → ℕ, k is an index sequence ∧
     c ◦ k converges to p).
Choose k := (n).
We need to show that (k is an _index sequence_ ∧ c ◦ k _converges to_ p).
We show both statements.
- By (n_is_index_sequence) we conclude that
    (k is an index sequence).
- We need to show that (c ◦ n converges to p).
  It holds that (a converges to p).
  By prop_10_3_1 it suffices to show that
    (c ◦ n is a subsequence of a).
  We need to show that (∃ m,
                        m is an _index sequence_
                        ∧ (∀ k ∈ ℕ, c(n(k)) = a(m(k)))).
  We need to show that (∃ m,
                        (∀ k ∈ ℕ, m(k) < m(k + 1))
                        ∧ (∀ k ∈ ℕ, c(n(k)) = a(m(k)))).