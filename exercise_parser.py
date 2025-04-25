

def parse(exercise_numbers):
    exercise = proof = """
        Variable f : ℝ → ℝ.
        Variable g : ℝ → ℝ.

        Lemma exercise_3_11_4 :
        (∀ M1 ∈ ℝ, ∃ y > 0, ∀ x > y, f (x) > M1) ⇒
            (∀ M2 < 4, ∃ z > 0, ∀ x > z, g (x) > M2) ⇒
            ∃ c ∈ ℝ, f(c) + g(c) > 10.
        Proof.
    """
    return exercise