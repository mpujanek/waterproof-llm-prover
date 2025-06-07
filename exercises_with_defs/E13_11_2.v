Definition f (x : ℝ) := x.

Lemma exercise_13_11_2 : ∀ a ∈ ℝ, f is _continuous_ in a.
Proof.
We need to show that (∀ a ∈ ℝ,
                        a is an _accumulation point_
                        ∧ _limit_ of f in a is f(a)
                        ∨ a is an _isolated point_).
Expand the definition of isolated point.