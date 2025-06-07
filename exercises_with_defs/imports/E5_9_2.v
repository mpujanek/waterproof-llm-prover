Set Default Goal Selector "!".

Require Import Coq.Reals.Reals.

Require Import Waterproof.Tactics.
Require Import Waterproof.Notations.Common.
Require Import Waterproof.Notations.Reals.
Require Import Waterproof.Notations.Sets.
Require Import Waterproof.Chains.
Require Import Waterproof.Automation.
Require Import Waterproof.Libs.Analysis.MetricSpaces.
Require Import Waterproof.Libs.Analysis.SequencesMetric.

Waterproof Enable Automation RealsAndIntegers.

Open Scope R_scope.
Open Scope metric_scope.

Notation "'max(' x , y )" := (Rmax x y)
  (format "'max(' x ,  y ')'").
Notation "'min(' x , y )" := (Rmin x y)
  (format "'min(' x ,  y ')'").

Context (X : Metric_Space).
Notation "'dist(' x , y )" := (dist X x y)
  (format "'dist(' x ,  y ')'").
