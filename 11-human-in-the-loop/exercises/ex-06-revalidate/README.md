# Revalidate Before Execution

**ID:** `ex-06`
**Stage:** 11-human-in-the-loop
**Difficulty:** L4
**Category:** Integration

## Objective

Refuse when the approved action and the current world diverge.

## Prerequisites

ex-02. ex-05.

## Problem

Execution checks the snapshot hash and a record version.

## Requirements

The snapshot stores `record_version` for update and publish actions. Execute loads the current version from the fake store. A mismatch refuses execution, leaves the tool counter unchanged, and records reason `stale_version`. If the caller supplies a fresh argument dict, ignore it and use the snapshot. If you also offer an explicit compare helper, it must fail closed when the hashes differ.

## Constraints

Fake record store. No model.

## Inputs and outputs

Approved pending action and a mutable record.

## Edge cases

Version unchanged. Version incremented. Arguments differ, hash differs, same pending id reused by a buggy caller.

## Errors

Refusal does not mark the item executed.

## Acceptance criteria

Three tests: unchanged version runs once, stale version runs zero times, substituted arguments run zero times and do not overwrite the snapshot.

## Testing

Unit tests.

## Common mistakes

Updating the snapshot in place so the new arguments look approved.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Why is a second approval the right follow-up to a stale version?

## Extension

Return the current version in the refusal so a UI could show a new preview. Do not build the UI.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
