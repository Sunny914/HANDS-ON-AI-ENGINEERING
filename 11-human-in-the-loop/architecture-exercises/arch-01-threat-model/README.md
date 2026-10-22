# Threat Model

**ID:** `arch-01`
**Stage:** 11-human-in-the-loop
**Difficulty:** L4
**Category:** Architecture

## Objective

State how approval fails if the surrounding controls are fake.

## Prerequisites

ex-01 through ex-06 at least on paper. Stage 05 authorization.

## Problem

Write `THREAT_MODEL.md` for the project actions: send, update, publish, and deploy.

## Requirements

Cover these cases:

- The model sets `approved: true`.
- The requester presents themselves as the approver.
- The payload changes after a human approved a preview.
- The same approval id is executed twice.
- The record version changes before execute.
- A worker or tool result says to skip the policy.

For each case, name the control and the test that shows the control. End with a list of decisions the model must never own: authentication, role membership, skip-approval, and whether an old approval covers a new payload.

## Constraints

No exploit code. No real external systems. This is a design note plus test names.

## Inputs and outputs

A threat model.

## Edge cases

An edit by the human, which is legitimate and must become a new snapshot.

## Errors

A control you cannot test is a gap. List it as a gap.

## Acceptance criteria

All six cases have a control and a test name. The never-delegate list is present. At least one residual gap is honest, such as a crash between tool success and the audit write.

## Testing

Not code. The test names must match tests you later add in the project, or you update the note.

## Common mistakes

Writing that approval makes the system safe.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which control is application authorization rather than human approval?

## Extension

Add a rejected-action path and say what the proposer is allowed to see from the rejection reason.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
