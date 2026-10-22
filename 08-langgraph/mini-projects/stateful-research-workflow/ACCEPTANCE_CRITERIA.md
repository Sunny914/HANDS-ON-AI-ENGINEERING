# Acceptance Criteria

- [ ] Invalid question does not collect
- [ ] A designed question gathers an expected evidence id
- [ ] Loop counter never exceeds the configured max
- [ ] Weak evidence at the max still finalizes with a partial status
- [ ] Same thread id sees prior evidence. A new id does not
- [ ] Failed collect is recorded and does not spin
- [ ] At least one node is unit-tested without `compile`
- [ ] Side effects are not placed before a pause. This project should not need a pause
- [ ] Design note lists one function that stayed outside the graph
