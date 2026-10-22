# Threat Model for a Tool Assistant

**ID:** `ex-01`
**Stage:** 14-security-guardrails
**Difficulty:** L2
**Category:** Architecture

## Objective

Name assets and abuse cases before writing checks.

## Prerequisites

[CONCEPTS.md](../../CONCEPTS.md). Stage 05 and Stage 11 in outline.

## Problem

Write `THREAT_MODEL.md` for a local assistant with `read`, `send`, and `deploy` fake tools.

## Requirements

Include assets, trust boundaries, and at least four abuse cases: direct injection, indirect injection in a retrieved note, cross-user read, and approval bypass. For each, name the application control you will test later. State that prompt wording is not the control.

## Constraints

No exploit steps against a real target. Synthetic system only.

## Inputs and outputs

A markdown note.

## Edge cases

A control you cannot test yet. Mark it as a gap.

## Errors

A model that says it will be careful is not a control.

## Acceptance criteria

Four abuse cases, each with an application control or an explicit gap. The note refuses the claim that injection is solved.

## Testing

Self-review after the draft.

## Common mistakes

A list of threats with no boundary.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which asset is hardest to take back after a bad tool call?

## Extension

Add a tenant-isolation abuse case if you did not already.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
