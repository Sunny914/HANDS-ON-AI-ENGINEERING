# Project Debugging

| Symptom | Check |
|---------|--------|
| Expected note never appears | Chunker gaps, filter, or embedder collapse |
| Always the same chunk | Fake embedder returns a constant vector |
| Citation does not match the prompt | Builder reordered text and not ids |
| Hit rate is 1.0 and you do not trust it | The golden questions are copies of the chunks |
| Docker error on default pytest | Missing skip |
| Answer when retrieval was empty | Completer called anyway |

Inspect chunk ids before you change the prompt.
