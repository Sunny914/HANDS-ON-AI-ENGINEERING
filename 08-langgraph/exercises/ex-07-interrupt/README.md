# Interrupt and Resume

**ID:** `ex-07`
**Stage:** 08-langgraph
**Difficulty:** L4
**Category:** Integration

## Objective

Pause for a decision without repeating a side effect.

## Prerequisites

CONCEPTS.md interrupt section. ex-06.

## Problem

A node proposes an action id, pauses, and records the action only if the resume value approves it.

## Requirements

One resume produces one ledger row. A reject produces zero rows. The payload you interrupt with includes the action id.

## Constraints

Fake ledger list. No email and no network.

## Inputs and outputs

Action id and a resume value.

## Edge cases

Resume value is an unexpected string. Document whether you treat it as reject.

## Errors

Calling the graph without a checkpointer should fail. Assert that if the library raises.

## Acceptance criteria

Approve test, reject test, single-row test.

## Testing

Graph tests with a new thread id each time.

## Common mistakes

Appending before `interrupt`.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Why does the node function run more than once?

## Extension

Include the arguments in the payload and reject a resume that refers to a different action id.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
