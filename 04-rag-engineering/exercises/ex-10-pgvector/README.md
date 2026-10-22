# pgvector Adapter

**ID:** `ex-10`
**Stage:** 04-rag-engineering
**Difficulty:** L4
**Category:** Integration

## Objective

Implement the store port against Postgres when it is available.

## Prerequisites

ex-04. ASSUMPTIONS.md. Docker compose in `infra/`.

## Problem

Upsert chunks with vectors and metadata. Search with a filter and a limit. Match the in-memory port closely enough that one ingestion test can run on either store.

## Requirements

Default pytest skips this module. `RUN_PGVECTOR=1` enables it.

## Constraints

You may use SQL text. If you use SQLAlchemy, use 2.x style. Verify the distance operator in the pgvector docs you installed.

## Inputs and outputs

Same records the in-memory store accepts.

## Edge cases

Extension missing, connection refused.

## Errors

Skip, do not fail the suite, when the database is absent.

## Acceptance criteria

Enabled test inserts two rows and gets the nearer one first for your fake vectors.

## Testing

Integration test, gated.

## Common mistakes

Copying a blog query that uses a different distance than your Python cosine.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What did you have to change besides the store?

## Extension

Add an index only if you can say which query uses it. Otherwise leave a note that you did not tune it.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-10` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
