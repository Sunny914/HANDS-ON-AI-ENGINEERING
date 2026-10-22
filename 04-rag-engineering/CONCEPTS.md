# Stage 04 Concepts

Read the first three sections before ex-02. They are the concept-first gate.

## Chunking

A document is too large for a context window and too mixed for one vector. A **chunk** is a contiguous piece you are willing to retrieve. Size and overlap are trade-offs. Small chunks miss context. Large chunks dilute the idea you wanted. Overlap exists so a sentence cut at a boundary still appears in one of the neighbors. Overlap that drops or duplicates carelessly is a bug, not a strategy.

Store **metadata** beside the text: document id, source name, position, and any filter fields such as product or date. If it is not stored, you cannot filter on it later.

## Embeddings

An embedding model maps text to a list of numbers. Similar texts should land nearer each other. The list is not a summary you can read. This stage uses a **fake embedder** you control: for example, a function that hashes tokens into a small vector. Tests then stay deterministic. A live embedding API is optional and must read its key from the environment.

Distance is not relevance to a human question. A high similarity can still be the wrong fact.

## Retrieval

The index returns the nearest k chunks. A **threshold** drops weak neighbors. An empty result is a valid outcome. Do not call the generator as if you had evidence.

**Filters** remove chunks before or after the similarity sort. Apply the filter you can explain. Document which.

## Advanced, after the basic path

**BM25 or a simple lexical score** counts term overlap. It finds rare exact words that vectors smear. **Hybrid** search mixes lexical and vector ranks. A simple reciprocal-rank fusion is enough here. Do not import a search engine unless you can explain the score you would have computed by hand.

**Reranking** is a second score on a short candidate list. Put it behind an interface. A fake reranker that boosts a keyword is enough to test the seam.

**pgvector** stores vectors in PostgreSQL. The SQL concept is: filter rows, order by a distance operator, limit k. The Python driver and the exact operator must be checked against the pgvector version you run. See [ASSUMPTIONS.md](./ASSUMPTIONS.md).

## Generation and citations

The generator may only see the selected chunks. The answer should carry citations back to chunk ids. A citation is not proof. It is a pointer a human can open. If the chunks do not support the question, the answer should say so. You already have a structured-output parser from Stage 02 and a chain from Stage 03. Reuse that pattern. Do not rebuild LangChain theory here.

## Evaluation

A **golden set** is a list of questions with the chunk ids that should have been retrieved, and sometimes a fact the answer must include. Retrieval metrics on a tiny set can be: hit at k, and whether the expected id is missing. Answer checks can be exact inclusion of a fact. Do not treat a model judge as the first metric. Stage 12 goes deeper. Here you only need a set you can fail on purpose.

## Cost and latency

Embedding every chunk costs money and time on a live model. Retrieval is usually cheaper than stuffing the whole file into the prompt. Log chunk counts, k, and latency. Do not log full document bodies at info.
