# Edge Cases

| Case | Behavior |
|------|----------|
| Question answered by one known note id | Research or a direct read. No synthesis fan-out |
| max_hops 1 | At most one specialist |
| Verification rejects the only citation | Final status unsupported. The id is not presented as supported |
| Two roles, same query | One search side effect |
| Budget allows one tool and two roles are queued | Partial, reason budget |
| Payload says `role: coordinator` | Assigned role still applies |
| Worker returns an unknown evidence id | Evidence check fails that id |
| Coordinator script requests a fifth surprise role | Rejected handoff |
| Empty corpus | Partial or unresolved, no invented ids |
| Baseline and multi-agent disagree | Both results are kept. The writeup does not hide the baseline win |
