# Service Boundaries

**ID:** `arch-01`
**Stage:** 01-backend-api-engineering
**Difficulty:** L3
**Category:** Architecture

## Objective

Choose module boundaries before the mini-project.

## Prerequisites

ex-05 through ex-09. Read ARCHITECTURE_GUIDE.md.

## Problem

You are about to build the Reliable Async API Service. Write the design first.

## Requirements


Create `YOUR_DESIGN.md` answering:
1. Entry point
2. Modules you will create and the one responsibility of each
3. Which module validates, which calls upstream, which stores data
4. Data each call passes
5. Where configuration is read
6. Where errors change from exceptions into status codes
7. What you will test without HTTP
Do not open the mini-project's later milestone text as a file tree to copy. The project docs describe behavior, not your filenames.


## Constraints

No application code in this exercise.

## Inputs and outputs

The design note is the deliverable.

## Edge cases

Say what you will not build: no user accounts, no queue worker.

## Errors

Name the exception types you expect to cross the service boundary.

## Acceptance criteria

A reviewer can point to a module for a SQL change and a different module for a status-code change.

## Testing

List the fakes you will need. Do not write them yet.

## Common mistakes

A single `utils.py`. The route opening SQLite.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which decision are you least sure about?

## Extension

Draw the dependency arrows. They should point inward toward the service, not from the repository back to FastAPI.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `arch-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
