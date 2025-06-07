Section Prop_6_2_2_i.

Variable a : ℕ → ℝ.
Definition a_opp (n : ℕ) := - a(n).

Lemma exercise_6_8_2 :
  a _diverges to ∞_
    ⇔
  a_opp _diverges to -∞_.
Proof.
Expand the definition of diverges to -∞.