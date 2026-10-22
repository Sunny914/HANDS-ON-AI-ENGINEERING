# Risk Policy and Separation of Duties

**ID:** `ex-03`
**Stage:** 11-human-in-the-loop
**Difficulty:** L2
**Category:** Design

## Objective

Decide who may approve which risk.

## Prerequisites

ex-01.

## Problem

Classify the five fake actions and enforce approver rules.

## Requirements

`read_record` is low and does not pause. `send_message` and `update_record` are medium: an approver role may approve, including a different user, and you may allow a same-person approve only if you document why. `publish` and `deploy` are high: the approver principal must differ from the requester, and the approver must have the approver role. A principal with only the requester role cannot approve. The model proposal cannot include an approver id that bypasses the check. The function under test receives the approver id from the application, not from the proposal body.

## Constraints

No UI. A function `can_approve(pending, approver_id, directory) -> decision` is enough.

## Inputs and outputs

Pending snapshot, approver id, and a fake directory of roles.

## Edge cases

Unknown approver. Requester id passed as the approver for deploy. Medium action with a valid approver.

## Errors

Refusal includes a reason code such as `same_principal` or `missing_role`.

## Acceptance criteria

Deploy self-approval fails. Unknown approver fails. A listed approver can approve send. The proposal body is not an argument that can change the directory.

## Testing

Unit tests.

## Common mistakes

Reading the approver id from the proposal dict.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What do you still need from a real identity system that this directory does not prove?

## Extension

Add a second approver requirement for deploy and do not implement a real product around it. A test that one approval is not enough is sufficient.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
