# Memory Write Policy

**ID:** `ex-03`
**Stage:** 06-memory-state-management
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Reject memories you should not store.

## Prerequisites

CONCEPTS.md write section.

## Problem

A candidate has text, kind, and a source such as `user` or `model`. Decide accept or reject.

## Requirements

Reject empty text. Reject a candidate whose text looks like an instruction override, using a rule you document. Reject a candidate the model proposed unless a flag `user_confirmed` is true. Accept a normal user preference.

## Constraints

The policy does not write files.

## Inputs and outputs

Candidate in. Decision with a reason code out.

## Edge cases

User-confirmed model proposal. Whitespace. Mixed case `Ignore previous`.

## Errors

Decisions are values, not prints.

## Acceptance criteria

Four tests: accept preference, reject model-only, reject override phrase, reject empty.

## Testing

Unit tests.

## Common mistakes

Trusting `source=system` just because the model wrote that word.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would you still refuse to store even if the user confirmed it?

## Extension

Add a retention class: `session` versus `durable`.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
