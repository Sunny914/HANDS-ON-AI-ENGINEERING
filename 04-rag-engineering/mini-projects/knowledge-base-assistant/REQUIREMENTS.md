# Requirements

## Milestone 1 — required

- Ingest UTF-8 text files with document ids, chunk indexes, and source names.
- Fake embedder in tests. The embedder is replaceable.
- In-memory store with top-k, a similarity threshold, and one metadata filter.
- Context builder and citations.
- Generator behind an injected completer. Empty retrieval does not call it.
- A golden file with at least three questions, including one expected miss or a deliberately irrelevant note.
- Configuration for chunk size, overlap, k, and threshold.
- Logs: document id, chunk count, latency. Not full note text at info.
- CLI or a single function entry point. HTTP is optional and not required.

## Milestone 2 — required before you call the project done

- Hybrid fusion from ex-08, or a written reason in the checkpoint why your corpus does not benefit, plus the fusion code still tested on a toy list.
- A rerank interface with an identity default and one fake.

## Milestone 3 — optional

- pgvector store behind the same port, skipped unless `RUN_PGVECTOR=1`.
- Live embeddings or a live chat model behind env flags.

## Non-goals

Web crawling, authentication, multi-tenant isolation, and a model-as-judge. Those belong to later stages.
