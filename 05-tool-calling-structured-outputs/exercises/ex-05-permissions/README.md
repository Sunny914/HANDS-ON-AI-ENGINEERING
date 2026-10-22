# Authorize the Caller

**ID:** `ex-05`
**Stage:** 05-tool-calling-structured-outputs
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Deny a tool based on the application's principal.

## Prerequisites

ex-04.

## Problem

Guests may `get_order` for their own id. They may not `refund`. Support may refund. A model argument named `role` must not grant support.

## Requirements

Principal is a dataclass you create in the test, not a field of `RefundArgs`. Denied calls do not run the tool. The denial is visible to the caller of execute.

## Constraints

No OAuth. Two roles are enough.

## Inputs and outputs

Principal, name, raw args.

## Edge cases

Guest refund. Support refund. Guest get. Model JSON containing `role: support` while the principal is a guest.

## Errors

Denial is not a validation error. The arguments can be valid and still denied.

## Acceptance criteria

The four cases above are tested. The refund probe stays at zero for the guest.

## Testing

Unit tests.

## Common mistakes

Reading the role from the tool arguments.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would you log on a denial?

## Extension

Deny a refund above a limit even for support.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-05` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
