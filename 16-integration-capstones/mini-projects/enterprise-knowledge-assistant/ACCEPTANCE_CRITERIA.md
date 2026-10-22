# Acceptance Criteria

- [ ] Baseline answers a fixture question with citations from the same tenant
- [ ] Other tenant's document id is not returned
- [ ] A hostile chunk does not change tenant or call a send tool
- [ ] Retrieval and groundedness are separate, and one fixture splits them
- [ ] Dataset version is on the report
- [ ] A bad citation fails the gate
- [ ] Error or success body carries a request id that is in the trace
- [ ] Completer timeout does not add citations
- [ ] Fake mode needs no API key
- [ ] ADR lists a rejected second agent and a rejected live-model default
- [ ] The checkpoint states the rubric bar you reached
