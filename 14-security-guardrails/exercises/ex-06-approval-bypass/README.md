# Approval Bypass

**ID:** `ex-06`
**Stage:** 14-security-guardrails
**Difficulty:** L4
**Category:** Integration

## Objective

Show that a proposal cannot approve itself.

## Prerequisites

Stage 11 policy. ex-03.

## Problem

`deploy` is high risk. Execute it only with a different approver principal supplied by the application.

## Requirements

Ignore `approved` and `skip_approval` on the proposal. The requester cannot approve their own deploy. A valid approver runs the fake tool once. A second execute does not double-apply.

## Constraints

No UI. Fake ledger.

## Inputs and outputs

Proposal, requester id, approver id.

## Edge cases

Flag set to true. Same principal. Different principal. Double execute.

## Errors

Unauthorized deploy leaves the ledger unchanged.

## Acceptance criteria

The three cases in the hint, after you have written them as tests from the requirements.

## Testing

Unit tests.

## Common mistakes

Reading the approver id from the proposal body.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which Stage 11 test is this repeating, and what did the untrusted document add?

## Extension

Require the approved hash to match the arguments, as in Stage 11.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
