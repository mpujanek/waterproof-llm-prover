Require Import Coq.Reals.Reals.
Require Import Qreals.

Require Import Waterproof.Tactics.
Require Import Waterproof.Notations.Common.
Require Import Waterproof.Notations.Reals.
Require Import Waterproof.Notations.Sets.
Require Import Waterproof.Chains.
Require Import Waterproof.Automation.

Waterproof Enable Automation RealsAndIntegers.
Waterproof Enable Automation Sets.

Open Scope R_scope.
Open Scope subset_scope.

Set Default Goal Selector "!".

Notation "'max(' x , y )" := (Rmax x y)
  (format "'max(' x ,  y ')'").
Notation "'min(' x , y )" := (Rmin x y)
  (format "'min(' x ,  y ')'").
