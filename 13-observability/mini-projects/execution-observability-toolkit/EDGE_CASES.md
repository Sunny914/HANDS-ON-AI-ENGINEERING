# Edge Cases

| Case | Behavior |
|------|----------|
| Orphan parent id | Reported, not dropped |
| Missing duration | Gap in the diagnosis, not treated as the fastest |
| Secret in a nested field | Redacted |
| Tool event | No token fields required |
| Two attempts | Both stored |
| Empty trace | Named empty diagnosis |
| Debug flag unset | No prompt body stored |
