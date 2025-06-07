Set Default Goal Selector "!".

Require Import Coq.Reals.Reals.
Require Import Waterproof.Tactics.
Require Import Waterproof.Notations.Common.
Require Import Waterproof.Notations.Reals.
Require Import Waterproof.Notations.Sets.
Require Import Waterproof.Chains.
Require Import Waterproof.Automation.
Require Import Waterproof.Libs.Analysis.Sequences.

Require Import Waterproof.Libs.Reals.

Waterproof Enable Automation RealsAndIntegers.
Waterproof Enable Automation Intuition.

Open Scope R_scope.
Open Scope subset_scope.

Definition prop_5_2_2 := is_bounded_equivalence.
Definition application_of_prop_5_2_2 (a : ℕ → ℝ) :=
  iff_trans(_, _, (is_bounded_above a ∧ is_bounded_below a), prop_5_2_2 a).

Notation "'max(' x , y )" := (Rmax x y)
  (format "'max(' x ,  y ')'").
Notation "'min(' x , y )" := (Rmin x y)
  (format "'min(' x ,  y ')'").
