# Stage 04 Testing

- Use a fake embedder with stable vectors. A useful fake: map each known word to a basis vector so tests can predict the nearest chunk.
- Do not call a paid embedding or chat API in the default suite.
- Chunk tests check ids, text coverage, and metadata.
- Index tests insert three chunks and assert the order of a query.
- Threshold tests include a query whose nearest neighbor is still below the cutoff.
- Evaluation tests load a golden JSON file and compute hit rate. Keep the file under five questions.
- pgvector tests skip when `RUN_PGVECTOR=1` is unset or the port is closed.

If a test only mocks the retriever and then checks the generator wording, it is not a retrieval test.
