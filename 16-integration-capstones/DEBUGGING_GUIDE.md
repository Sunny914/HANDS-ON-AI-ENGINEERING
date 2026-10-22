# Stage 16 Debugging

Use the guides from the stage that owns the symptom. Integration failures are often a boundary leak:

| Symptom | Look at |
|---------|---------|
| The HTTP layer contains ranking or approval math | Policy moved into the route |
| Tests pass only when the live flag is on | Fakes not used on the default path |
| Eval score uses a different corpus than the app | Two data sources |
| A trace cannot be joined to the error body | Request id dropped at the edge |
| The second milestone rewrote the baseline | No regression test for milestone 1 |
