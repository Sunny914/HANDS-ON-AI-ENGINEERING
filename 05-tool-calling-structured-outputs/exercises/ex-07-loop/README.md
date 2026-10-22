# One Tool Round-Trip

**ID:** `ex-07`
**Stage:** 05-tool-calling-structured-outputs
**Difficulty:** L4
**Category:** Integration

## Objective

Turn a fixture proposal into a tool result message.

## Prerequisites

ex-06. `fixtures/tool_call.json`.

## Problem

Implement one loop: read a proposal, execute under a principal, return a result object with status, body, and tool name. Add two more fixtures you write: invalid arguments, and a tool that raises.

## Requirements

The loop does not call a live model. A later optional function may ask a fake model object for a proposal. The default test passes the fixture dict.

## Constraints

One round-trip. No planner.

## Inputs and outputs

Proposal dict and principal in. Result object out.

## Edge cases

Unknown tool. Denied tool. Tool exception.

## Errors

Those become result statuses, not uncaught crashes, unless you document one class of bugs you still let crash. Default: capture tool errors.

## Acceptance criteria

Valid fixture, invalid fixture, and raising tool are tested. The result names the tool.

## Testing

Fixture tests.

## Common mistakes

Catching errors inside the tool and returning a successful refund.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would a second round-trip need that you refused to build?

## Extension

Ask a fake chat model to emit the proposal dict, then run the same loop.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-07` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
