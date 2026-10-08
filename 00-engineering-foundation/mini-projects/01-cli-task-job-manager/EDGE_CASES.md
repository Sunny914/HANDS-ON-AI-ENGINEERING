# MP1 — Edge Cases

Handle or explicitly document out-of-scope:

| Case | Expected behavior (you decide, document) |
|------|------------------------------------------|
| Empty title | Reject |
| Unknown id on update/delete/show | Clear error |
| Corrupt JSON file | Error message; optional backup strategy |
| Missing data file on first run | Create empty store or error—document |
| Duplicate title allowed? | Your policy in README |
| Filter with no matches | Empty list, exit 0 |
| Very long description | Truncate or reject—document limit |
| System clock changes | Timestamps still ISO from local clock |
| Concurrent CLI runs | Stage 0: document “last write wins” or file lock attempt |

## Security (minimal)

- No code execution from JSON
- Reject absurdly large files if you add size check
