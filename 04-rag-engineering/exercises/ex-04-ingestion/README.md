# Ingest Documents

**ID:** `ex-04`
**Stage:** 04-rag-engineering
**Difficulty:** L3
**Category:** Integration

## Objective

Run parse, chunk, embed, and store as one function.

## Prerequisites

ex-02 and ex-03.

## Problem

Read `.txt` files from a directory. Each file is a document. Ingest them into the index.

## Requirements

Metadata includes source filename and chunk index. Re-ingesting the same document id replaces its chunks.

## Constraints

UTF-8 text files only.

## Inputs and outputs

Directory in. Count of chunks out.

## Edge cases

Empty directory. A second ingest of the same file does not duplicate chunks.

## Errors

A decode error is reported and that file is skipped or the run fails. Document which.

## Acceptance criteria

Test with two temp files. Search returns a chunk from the intended file.

## Testing

Filesystem plus index. Still no paid API.

## Common mistakes

Embedding inside the chunker so you cannot test splits alone.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What is the document lifecycle when the file changes?

## Extension

Record a content hash and skip unchanged files.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-04` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
