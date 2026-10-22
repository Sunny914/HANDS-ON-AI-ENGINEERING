# Stage 04 Architecture

```text
files → parser → chunker → embedder → store
question → embedder → retriever → context builder → generator → cited answer
```

| Piece | Owns |
|-------|------|
| Parser | Bytes or text to a document with an id |
| Chunker | Document to chunks. No I/O. |
| Embedder | Text to vector. Fake or live. |
| Store | Upsert and search. In-memory first. pgvector is a second store. |
| Retriever | k, threshold, filters. Returns chunks, not prose. |
| Context builder | Ordered excerpts and a citation list |
| Generator | Prompt plus model. May be the Stage 03 chain shape. |

The chunker does not call the model. The generator does not open the database. The store does not decide the user's question.

You choose chunk size, overlap, k, and the citation string. Write them down as configuration.
