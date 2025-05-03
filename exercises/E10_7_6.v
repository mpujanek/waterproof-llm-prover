Inductive Color : Set :=
| blue : Color
| orange : Color.

Variable P : ℕ → Color.

Parameter infinitely_many_blues :
  ∀ K ∈ ℕ, ∃ m ≥ K, P(m) = blue.

Lemma exercise_10_7_6 : ∃ n : (ℕ → ℕ),
  (is_index_sequence n) ∧ (∀ k ∈ ℕ, P(n(k)) = blue).
Proof.
Define the index sequence n inductively.