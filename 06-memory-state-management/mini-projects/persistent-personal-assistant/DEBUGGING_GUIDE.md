# Project Debugging

| Symptom | Check |
|---------|--------|
| Fact gone after a second remember | Full-record replace |
| Fact gone after restart | Path differs, or write buffered |
| Other user's fact appears | Query missing user id |
| System prompt changed | Builder concatenated memory into it |
| Expired fact still used | Clock not injected |
| Tests pass but a manual rerun does not | Test used the same object and never reopened |
