# Project Debugging

| Symptom | Check |
|---------|--------|
| Infinite recursion | Cycle without a counter, or library step limit unset |
| Evidence list length 1 after two collects | Update replaced the list |
| Resume sees an empty question | New thread id |
| Validate never runs | START edge missing |
| Synthesis runs with no evidence | Router ignores empty evidence |
