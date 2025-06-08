Section exercise_13_11_3.

Variable Y : Metric_Space.
Notation "'dist_Y(' x , z )" := (dist Y x z) (format "'dist_Y(' x ,  z ')'").
Variable a : ℕ → Y.

Lemma exercise_13_11_3 :
  ∀ n ∈ ℕ, a is _continuous_ in n.
Proof.
We need to show that (∀ n ∈ ℕ,
                        n is an _accumulation point_
                        ∧ _limit_ of a in n is a(n)
                        ∨ n is an _isolated point_).
We need to show that (∀ n ∈ ℕ,
                        n is an _accumulation point_
                        ∧ _limit_ of a in n is a(n)
                        ∨ (∃ ε > 0, ∀ n0 ∈ ℕ, |n0 - n| = 0 ∨ ε ≤ |n0 - n|)).
We need to show that (∀ n ∈ ℕ,
                        n is an _accumulation point_
                        ∧ (∀ ε > 0,
                           ∃ δ > 0,
                           ∀ n0 ∈ ℕ,
                           0 < |n0 - n| < δ ⇨ dist_Y(a(n0), a(n)) < ε)
                        ∨ (∃ ε > 0, ∀ n0 ∈ ℕ, |n0 - n| = 0 ∨ ε ≤ |n0 - n|)).