# Stage 06 Architecture

```text
policy → memory repository → retrieval
transcript selector → context builder → model input
```

| Piece | Owns |
|-------|------|
| Schema | Fields and legal transitions |
| Write policy | Accept, reject, or expire a candidate memory |
| Repository | Load and save. No prompt wording |
| Retrieval | Which rows, in which order |
| Context builder | Fits a budget and labels provenance |
| Transcript selector | What remains of the message list |

The repository must not call a model. The context builder must not decide that a secret is fine to store. That decision belongs in the write policy.
