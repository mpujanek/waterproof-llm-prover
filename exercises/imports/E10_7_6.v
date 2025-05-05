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
Require Import Waterproof.Libs.Analysis.StrongInductionIndexSequence.

Open Scope metric_scope.

Waterproof Enable Automation RealsAndIntegers.
Waterproof Enable Automation Intuition.

Open Scope nat_scope.

Inductive Color : Set :=
| blue : Color
| orange : Color.
