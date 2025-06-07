Require Import Coq.Reals.Reals.
Require Import Qreals.
(* Require Import Arith.Even. *)
Require Import ZArith.ZArith.
Require Import FunctionalExtensionality.
Require Import Rbase.
Require Import Rbasic_fun.

Require Import Waterproof.Tactics.
Require Import Waterproof.Notations.Common.
Require Import Waterproof.Notations.Reals.
Require Import Waterproof.Notations.Sets.
Require Import Waterproof.Chains.
Require Import Waterproof.Automation.
Require Import Coq.Logic.FinFun.

Require Import Waterproof.Libs.Analysis.MetricSpaces.
Require Import Waterproof.Libs.Analysis.SupAndInf.
Require Import Waterproof.Libs.Analysis.SequencesMetric.
Require Import Waterproof.Libs.Analysis.Sequences.
Require Import Waterproof.Libs.Reals.
Require Import Waterproof.Libs.Analysis.SubsequencesMetric.
Require Import Waterproof.Libs.Analysis.StrongInductionIndexSequence.
Require Import Waterproof.Libs.Analysis.OpenAndClosed.
Require Import Waterproof.Libs.Analysis.ContinuityDomainR.
Require Import Waterproof.Libs.Analysis.ContinuityDomainNat.

Waterproof Enable Automation RealsAndIntegers.
Waterproof Enable Automation Sets.
Waterproof Enable Automation Intuition.

Notation "'max(' x , y )" := (Rmax x y)
  (format "'max(' x ,  y ')'").
Notation "'min(' x , y )" := (Rmin x y)
  (format "'min(' x ,  y ')'").

Inductive Color : Set :=
| blue : Color
| orange : Color.

Definition prop_5_2_2 := is_bounded_equivalence.
Definition application_of_prop_5_2_2 (a : ℕ → ℝ) :=
  iff_trans(_, _, (is_bounded_above a ∧ is_bounded_below a), prop_5_2_2 a).

Definition prop_10_3_1 := equivalent_subsequence_convergence.
Notation "n 'is' 'even'" := (Nat.even n) (at level 68).

Open Scope R_scope.
Open Scope subset_scope.
Open Scope metric_scope.
Open Scope nat_scope.
