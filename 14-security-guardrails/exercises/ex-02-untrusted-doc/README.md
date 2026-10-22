# Retrieved Text Cannot Grant a Tool

**ID:** `ex-02`
**Stage:** 14-security-guardrails
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Treat indirect injection as data.

## Prerequisites

ex-01 on paper. Stage 10 least privilege.

## Problem

An authorizer decides a tool call from the principal and the tool name. A document string is available and must not change the decision.

## Requirements

Principal `researcher` may read and may not deploy or send. A document that contains `you are admin` and `call deploy` does not add tools. The fake ledger does not change on deny.

## Constraints

No model call. The document is a Python string.

## Inputs and outputs

Principal, tool name, document text.

## Edge cases

Empty document. Document that names a different user. Allowed read.

## Errors

Deny is a structured result.

## Acceptance criteria

Deploy denied with the hostile document. Read allowed for the same principal. Ledger unchanged on deny.

## Testing

Unit tests.

## Common mistakes

Searching the document for the word admin and elevating the role.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Why can the model still quote the document in its answer?

## Extension

Log the deny with a hash of the document, not the document body.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
