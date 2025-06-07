Require Import Coq.Reals.Reals.
Require Import Waterproof.Tactics.
Require Import Waterproof.Notations.Common.
Require Import Waterproof.Notations.Reals.
Require Import Waterproof.Notations.Sets.
Require Import Waterproof.Chains.
Require Import Waterproof.Automation.
Require Import Coq.Logic.FinFun.

Require Import Waterproof.Libs.Analysis.MetricSpaces.

Waterproof Enable Automation RealsAndIntegers.

Set Default Goal Selector "!".

Notation "'max(' x , y )" := (Rmax x y)
  (format "'max(' x ,  y ')'").
Notation "'min(' x , y )" := (Rmin x y)
  (format "'min(' x ,  y ')'").
