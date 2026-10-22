# Test Plan

- Chunk coverage and tail
- Fake embedder order
- Re-ingest
- Threshold and filter
- Citation ids
- Golden hit rate, including a miss
- Rerank order
- Hybrid toy lists
- Optional pgvector, skipped by default

The generator test uses a fake completer and asserts it saw a chunk id. It is not a retrieval test by itself.
