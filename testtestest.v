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
Set Default Goal Selector "!".

Require Import Coq.Reals.Reals.
Require Import Waterproof.Tactics.
Require Import Waterproof.Notations.Common.
Require Import Waterproof.Notations.Reals.
Require Import Waterproof.Notations.Sets.
Require Import Waterproof.Chains.
Require Import Waterproof.Libs.Analysis.OpenAndClosed.
Require Import Waterproof.Automation.

Waterproof Enable Automation RealsAndIntegers.
Waterproof Enable Automation Intuition.

Open Scope R_scope.
Open Scope subset_scope.

Notation "'max(' x , y )" := (Rmax x y)
  (format "'max(' x ,  y ')'").
Notation "'min(' x , y )" := (Rmin x y)
  (format "'min(' x ,  y ')'").
Lemma not_closed : ¬ ([0,1) is _closed_).
Proof.
We argue by contradiction.
Assume that ([0,1) is _closed_).
It suffices to show that (1 ∈ [0,1)).
We need to show that (1 is a limit point of [0,1)).
Take ε > 0.
- It holds that (∃ x ∈ [0,1), (& 1 - ε < x < 1)).
We conclude that (1 is a limit point of [0,1)).
By the definition of closed sets, we conclude that (1 ∈ [0,1)).
However, by the definition of [0,1), it holds that (1 ∉ [0,1)).
Contradiction.
Qed.