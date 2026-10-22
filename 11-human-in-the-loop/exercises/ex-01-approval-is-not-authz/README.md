# Approval Is Not Authorization

**ID:** `ex-01`
**Stage:** 11-human-in-the-loop
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Show that a model cannot approve itself or skip policy.

## Prerequisites

Stage 05 permissions. Stage 07 untrusted model output.

## Problem

Implement a policy function that decides whether an action needs a human pause.

## Requirements

Inputs are the action name and the raw proposal. `read_record` does not need approval. `send_message`, `update_record`, `publish`, and `deploy` do. If the proposal contains `skip_approval` or `approved` set to true, the result is unchanged. The function does not execute anything.

## Constraints

Pure function. No file I/O.

## Inputs and outputs

Action name and proposal dict in. A decision object out: needs_approval and reason.

## Edge cases

Unknown action name. Empty proposal. Skip flag as the string `true`.

## Errors

Unknown actions need approval or are rejected. Pick one, document it, and test it. Do not default them to allowed.

## Acceptance criteria

Tests: read does not pause, send pauses, send with `skip_approval: true` still pauses, unknown action does not run as allowed.

## Testing

Unit tests.

## Common mistakes

Returning the proposal's own `approved` field.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which earlier stage treated a model field as a permission?

## Extension

Return the policy version on the decision so later audits can show which rules were in force.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
