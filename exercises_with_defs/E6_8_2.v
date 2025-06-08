Section Prop_6_2_2_i.

Variable a : ℕ → ℝ.
Definition a_opp (n : ℕ) := - a(n).

Lemma exercise_6_8_2 :
  a _diverges to ∞_
    ⇔
  a_opp _diverges to -∞_.
Proof.
We need to show that ((∀ M ∈ ℝ, ∃ N1 ∈ ℕ, ∀ n ≥ N1, a(n) > M)
                        ⇔ a_opp _diverges to -∞_).
We need to show that ((∀ M ∈ ℝ, ∃ N1 ∈ ℕ, ∀ n ≥ N1, a(n) > M)
                        ⇔ (∀ M ∈ ℝ, ∃ N1 ∈ ℕ, ∀ n ≥ N1, a_opp(n) < M)).