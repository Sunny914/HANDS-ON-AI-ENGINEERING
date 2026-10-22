# Stage 04 — RAG Engineering

Build a retrieval pipeline you can measure. Generation comes after you can say which chunk was retrieved and why.

## Objectives

- Explain chunking, embeddings, and similarity before writing an index
- Ingest text into chunks with metadata
- Retrieve with a fake embedder and an in-memory index
- Add filters, a similarity threshold, a simple hybrid score, and citations
- Evaluate a tiny golden set
- Put the same port behind PostgreSQL and pgvector when Docker is available

## Prerequisites

- Stage 02 for generation and structured output
- Stage 03 for composing a prompt around a selected excerpt
- The selector in Stage 03 is not this stage. You will replace that idea with retrieval.

## How the stage is layered

Essential path: concepts, chunking, in-memory vectors, ingestion, filters, citations, evaluation.

Advanced path, after the essential index works: hybrid scoring, a rerank interface, and pgvector.

The mini-project's first milestone is the essential path. Later milestones add the advanced path. Do not start with hybrid search.

## Sequence

[ROADMAP.md](./ROADMAP.md). Concept notes that must be read first are marked in [CONCEPTS.md](./CONCEPTS.md).

## Next

[Stage 05](../05-tool-calling-structured-outputs/README.md) after the checkpoint.
