# Stage 04 Hints

## ex-01

- **H1:** Separate "we fetched the wrong text" from "the model spoke past the text".
- **H2:** Two columns in a markdown table: symptom, which stage of the pipeline you would inspect.
- **H3:** Include empty retrieval, a cut sentence, a filter that removed the only good chunk, and an answer that cites nothing.

## ex-02

- **H1:** Walk the string with a window. Keep the start index increasing.
- **H2:** Parameters are size and overlap. Overlap must be smaller than size.
- **H3:** Next start = previous start + size - overlap. The last slice may be short. Every original character should appear in some slice. Add a test that joins coverage, not a test that forbids overlap duplicates.

## ex-03

- **H1:** Cosine similarity is a dot product of normalized vectors.
- **H2:** A store maps id to vector plus payload. Query embeds, scores, sorts.
- **H3:** Reject a zero vector. Return the top k ids in descending score. Test with basis vectors so one chunk is obviously nearer.

## ex-04

- **H1:** Ingestion is a pipeline of pure steps plus one store write.
- **H2:** parse → chunk → embed → upsert. Metadata includes document id and chunk index.
- **H3:** The embedder is injected. The test uses the fake from ex-03 and reads the chunks back.

## ex-05

- **H1:** A threshold is a minimum score, not a maximum distance, unless you document distance.
- **H2:** Filter the candidate set before you cut to k, or document the opposite and test it.
- **H3:** If the best score is below the threshold, return an empty list. Do not return the best anyway.

## ex-06

- **H1:** The model should see labeled excerpts, and the caller should see ids.
- **H2:** Build a string with `[chunk_id]` headers and return the ids alongside it.
- **H3:** Preserve order. If retrieval is empty, the builder returns a distinguished empty context and the generator must not be required.

## ex-07

- **H1:** Hit@k means the expected id appears in the first k results.
- **H2:** Load cases from JSON. Run the retriever. Average the hits.
- **H3:** A fixture with one relevant and one irrelevant chunk should score 1.0 for a query you designed. A second case should score 0 so the metric can move.

## ex-08

- **H1:** You need two ranked lists, then a way to merge ranks.
- **H2:** Lexical score can be a count of overlapping terms. Vector score is the one you have.
- **H3:** Reciprocal rank fusion: add `1 / (constant + rank)` for each list. Test a query where the lexical winner differs from the vector winner.

## ex-09

- **H1:** Rerank receives a short list, not the whole corpus.
- **H2:** A protocol `rerank(query, chunks) -> chunks`. The default identity reranker returns the same order.
- **H3:** A fake that moves any chunk containing a given word to the front proves the retriever calls it after the first k.

## ex-10

- **H1:** The port is the same as the in-memory store: upsert and search.
- **H2:** SQL filters metadata, orders by distance, limits k. Confirm the operator in the docs.
- **H3:** Skip the test unless `RUN_PGVECTOR=1`. Do not let a closed port fail the default suite.

## arch-01

- **H1:** Draw ingestion and query as two arrows into the same store.
- **H2:** Put the generator to the right of the context builder.
- **H3:** Name the type that crosses from retriever to generator. It should include chunk id and text.

## arch-02

- **H1:** A retriever returns evidence. It does not return an answer.
- **H2:** List the arguments: query, k, threshold, filters.
- **H3:** Write what the retriever is forbidden to import: the chat model, the HTTP request.

## dbg-01

- **H1:** Compare the source length with the set of indexes your chunks cover.
- **H2:** The step size skips characters.
- **H3:** Advance by size minus overlap, and keep the tail.

## dbg-02

- **H1:** Write down whether a larger number means nearer.
- **H2:** The comparison that keeps a chunk is inverted.
- **H3:** Keep scores that are greater than or equal to the minimum similarity.
