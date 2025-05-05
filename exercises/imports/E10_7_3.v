Require Import Coq.Reals.Reals.
(* Require Import Arith.Even. *)
Require Import ZArith.ZArith.
Require Import FunctionalExtensionality.

Require Import Waterproof.Tactics.
Require Import Waterproof.Notations.Common.
Require Import Waterproof.Notations.Reals.
Require Import Waterproof.Notations.Sets.
Require Import Waterproof.Chains.
Require Import Waterproof.Automation.
Require Import Waterproof.Libs.Analysis.SequencesMetric.
Require Import Waterproof.Libs.Analysis.SubsequencesMetric.

Waterproof Enable Automation RealsAndIntegers.
Waterproof Enable Automation Intuition.

Set Default Goal Selector "!".

Open Scope R_scope.
Open Scope subset_scope.

Notation "'max(' x , y )" := (Rmax x y)
  (format "'max(' x ,  y ')'").
Notation "'min(' x , y )" := (Rmin x y)
  (format "'min(' x ,  y ')'").

Open Scope metric_scope.

(* Coercion Base : Metric_Space >-> Sortclass. *)

(* For readability. *)
Definition prop_10_3_1 := equivalent_subsequence_convergence.
Notation "n 'is' 'even'" := (Nat.even n) (at level 68).
