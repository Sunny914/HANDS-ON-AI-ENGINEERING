# Edge Cases

| Case | Behavior |
|------|----------|
| Empty folder | Zero chunks, no crash |
| Overlap greater than or equal to size | Reject at configuration |
| Duplicate filenames | Document how ids are assigned |
| Query with no term overlap and a weak vector | Empty or a low score you then threshold |
| Completer cites an unknown id | Drop or fail, as designed in ex-06 |
| Golden case with the wrong expected id | The score drops. Do not edit the metric to hide it. |
| pgvector port closed | Skip milestone 3 |
| File replaced on disk | Re-ingest updates chunks |
