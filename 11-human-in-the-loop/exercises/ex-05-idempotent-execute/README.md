# Idempotent Execution

**ID:** `ex-05`
**Stage:** 11-human-in-the-loop
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Run an approved fake tool once.

## Prerequisites

ex-03. Stage 05 idempotency.

## Problem

After approval, execute the snapshot. A repeated execute does not repeat the side effect.

## Requirements

The idempotency key is the pending id. The stored result includes the tool output. The second call returns that result. Pending status becomes `executed` and stays there. A call on a still-pending id does not execute.

## Constraints

Fake send tool with a counter. No network.

## Inputs and outputs

Pending id and an approver decision.

## Edge cases

Execute called twice. Execute called before approval. Two different pending ids.

## Errors

Missing id is a named error.

## Acceptance criteria

Counter is 1 after two executes of the same approval. A different id can send once more. Pending without approval does not increment the counter.

## Testing

Unit tests with the fake tool.

## Common mistakes

Keying only on the action name, so two different recipients share one result.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What should a retry do if the first execute failed after the tool succeeded but before you stored the result? Describe the gap even if you do not close it.

## Extension

Store the result before you mark the status, or the reverse, and write down which crash window you still have.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
