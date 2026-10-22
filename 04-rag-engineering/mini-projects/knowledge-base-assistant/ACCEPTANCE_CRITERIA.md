# Acceptance Criteria

- [ ] Two notes ingest, and a designed query returns the expected chunk id first
- [ ] Re-ingest replaces chunks instead of duplicating them
- [ ] A boundary character from a long note appears in at least one chunk
- [ ] Threshold can force an empty retrieval, and the completer is not called
- [ ] Metadata filter can exclude the nearest chunk
- [ ] The answer object includes only citation ids that were retrieved
- [ ] Golden-set hit rate matches a hand-computed value
- [ ] Hybrid or the documented waiver exists, and the rerank fake changes order in a test
- [ ] Default tests need no Docker and no API key
- [ ] Design note updated if the module split changed
