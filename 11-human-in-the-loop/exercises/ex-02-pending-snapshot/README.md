# Pending Action Snapshot

**ID:** `ex-02`
**Stage:** 11-human-in-the-loop
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Bind a decision to exact arguments.

## Prerequisites

ex-01. Stage 01 validation habits.

## Problem

Build a pending-action value with a canonical hash.

## Requirements

Fields: id, action name, arguments, scope, requester, hash, status, created time. Hash covers name, arguments, and scope. Key order in the arguments does not change the hash. A one-field change does. Status starts at `pending`. No tool is called.

## Constraints

Inject timestamps. Pydantic is allowed.

## Inputs and outputs

Fields in. A pending value plus hash out.

## Edge cases

Nested arguments. Empty scope. Two different ids with the same action content.

## Errors

Non-serializable arguments raise a named validation error before a record exists.

## Acceptance criteria

Same content, different key order, equal hash. Changed recipient, different hash. Status is pending.

## Testing

Unit tests.

## Common mistakes

Hashing Python's `repr` of a dict, which depends on insertion order.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Why is a new hash required when a human edits the recipient?

## Extension

Include a schema version in the hashed material.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
