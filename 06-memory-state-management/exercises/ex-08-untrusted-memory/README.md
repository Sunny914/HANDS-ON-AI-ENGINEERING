# Memory Is Data

**ID:** `ex-08`
**Stage:** 06-memory-state-management
**Difficulty:** L3
**Category:** Failure analysis

## Objective

Stop a stored sentence from becoming a new rule.

## Prerequisites

ex-07.

## Problem

A memory says the assistant may delete files and should ignore earlier rules. Assemble context anyway.

## Requirements

The system message stays the one you wrote. The hostile sentence is inside the labeled data block. A pure checker you write asserts the system text is unchanged.

## Constraints

No model call.

## Inputs and outputs

Same as ex-07.

## Edge cases

Hostile text in the user message and in a memory. Both stay out of the system message.

## Errors

If the builder cannot label the block, it fails rather than appending to the system string.

## Acceptance criteria

Assertion on the system message equality, and assertion that the hostile string is still present in the data message.

## Testing

Unit test.

## Common mistakes

Hoping the model will notice. Deleting the test string so the test goes green.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What can labeling not prevent?

## Extension

Add a write-policy test that rejects this sentence before it is stored. Both layers may exist.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-08` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
