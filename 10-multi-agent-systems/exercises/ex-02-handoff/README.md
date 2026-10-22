# Handoff Schema

**ID:** `ex-02`
**Stage:** 10-multi-agent-systems
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Make delegation a validated message.

## Prerequisites

ex-01.

## Problem

Implement a handoff object and a function that accepts or rejects it before a role runs.

## Requirements

Fields include task id, source role, target role, hop count, payload, and evidence ids already collected. Target role must be one of the known specialists. Hop count must be a non-negative integer. Payload is data, stored as a structured object, not concatenated into an instruction string.

## Constraints

Do not execute tools in this exercise.

## Inputs and outputs

A dict in. A handoff or a named error out.

## Edge cases

Negative hop. Unknown target. Missing evidence list. Payload that contains the text `ignore your role`.

## Errors

The hostile payload is still delivered only as data if the rest of the handoff is valid. It must not change the target role.

## Acceptance criteria

Four tests: valid handoff, unknown role, bad hop, hostile payload preserved as data and not interpreted.

## Testing

Unit tests.

## Common mistakes

Using the payload as the system prompt for the next role.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would you lose by passing the entire chat transcript instead of this schema?

## Extension

Add a size limit and reject oversized payloads with a named error.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
