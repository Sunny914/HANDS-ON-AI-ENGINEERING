# Local Deploy and Rollback

**ID:** `arch-01`
**Stage:** 15-production-ai-infrastructure
**Difficulty:** L4
**Category:** Architecture

## Objective

Decide how the project runs on one machine.

## Prerequisites

ex-01. ex-02.

## Problem

Write `DEPLOY.md` for the Production-Style AI Agent Service.

## Requirements

Include image contents you refuse, runtime config, a smoke command using fake mode, health routes, and a rollback to a previous local tag. Say Kubernetes is not part of this project. Say how a failed smoke test blocks you from calling the image current.

## Constraints

No cloud account.

## Inputs and outputs

A note.

## Edge cases

Docker is not installed. The note says the exercises still run and the smoke milestone is blocked, not silently skipped.

## Errors

A secret copied into the image.

## Acceptance criteria

Non-root, no baked key, fake-mode smoke, and a rollback step are all present.

## Testing

Not code. The project Dockerfile comes later and should match this note.

## Common mistakes

Starting with a cluster diagram.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would you add for a second environment that you are not adding now?

## Extension

Name a CI command that runs the offline suite before the image build.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
