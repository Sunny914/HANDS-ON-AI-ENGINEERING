# Project Debugging


| Symptom | Check |
|---------|--------|
| Other tenant's chunk appears | Filter after ranking, or the cache key omitted tenant |
| Gate always passes | It scores retrieval only |
| Trace has no retrieval span | Completer called the index privately |
| Timeouts return citations | Except block fills placeholder ids |
