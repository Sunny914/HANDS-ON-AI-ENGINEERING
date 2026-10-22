# Project Debugging

| Symptom | Check |
|---------|--------|
| Tree is empty | Query uses a different request id than the one you started |
| Durations fluctuate | Wall clock instead of the injected clock |
| Secret still on disk | Redactor after the write, or a second writer |
| Retry count stays 0 | Summary keeps the last attempt only |
| Diagnosis always says model | It skips zero durations incorrectly or ignores retrieval |
