# Redact Secrets before Storage

**ID:** `ex-04`
**Stage:** 13-observability
**Difficulty:** L3
**Category:** Integration

## Objective

Keep credentials out of the event file.

## Prerequisites

ex-01. Stage 14 will go further. This exercise is the logging slice.

## Problem

A redactor runs on attributes before append.

## Requirements

Keys `api_key`, `authorization`, and `secret` are replaced with `[redacted]`. String values containing `sk-test-` are replaced even if the key is innocent. Other fields remain. The stored record is what tests read.

## Constraints

Synthetic secrets only. No real credentials.

## Inputs and outputs

Attributes in. Stored event out.

## Edge cases

Nested dict. Secret inside a list of strings. Already-redacted value.

## Errors

If redaction throws, do not store the raw event.

## Acceptance criteria

The marker `sk-test-` is absent after read-back. A tool name beside it remains.

## Testing

Unit tests.

## Common mistakes

Redacting only at print time and writing the raw dict to disk.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What sensitive data does this redactor still miss?

## Extension

Add a test-only debug flag that keeps a 20-character excerpt, and show that the default test leaves it off.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
