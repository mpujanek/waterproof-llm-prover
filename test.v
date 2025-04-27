Require Import Coq.Reals.Reals.
Require Import Waterproof.Tactics.
Require Import Waterproof.Notations.Common.
Require Import Waterproof.Notations.Reals.
Require Import Waterproof.Notations.Sets.
Require Import Waterproof.Chains.

Require Import Waterproof.Libs.Analysis.SupAndInf.
Require Import Waterproof.Libs.Analysis.SupAndInf.

Require Import Waterproof.Automation.

Waterproof Enable Automation RealsAndIntegers.
Waterproof Enable Automation Intuition.

Open Scope R_scope.
Open Scope subset_scope.

Set Default Goal Selector "!".

Notation "'max(' x , y )" := (Rmax x y)
  (format "'max(' x ,  y ')'").
Notation "'min(' x , y )" := (Rmin x y)
  (format "'min(' x ,  y ')'").

Inductive answer : Type :=
| Yes : answer.

Set Default Timeout 10.

Lemma ex_4_9_1 : ∀ a ∈ ℝ, ∀ b ∈ ℝ, a < b ⇒
    a is the infimum of [a,b).
Proof.
We need to show that (∀ a ∈ ℝ,
                      ∀ b ∈ ℝ,
                      a < b
                      ⇨ a is a _lower bound_ for [a, b)
                        ∧ (∀ l ∈ ℝ, l is a _lower bound_ for [a, b) ⇨ l ≤ a)).
We need to show that (∀ a ∈ ℝ,
                      ∀ b ∈ ℝ,
                      a < b
                      ⇨ (∀ a0 ∈ [a, b), a ≤ a0)
                        ∧ (∀ l ∈ ℝ, (∀ a0 ∈ [a, b), l ≤ a0) ⇨ l ≤ a)).
Qed.
