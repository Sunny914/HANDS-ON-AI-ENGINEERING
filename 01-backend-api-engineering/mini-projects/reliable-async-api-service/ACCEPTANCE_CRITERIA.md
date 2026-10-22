# Acceptance Criteria

- [ ] Authorized create with a fake upstream stores a succeeded job
- [ ] The same idempotency key does not perform a second upstream call
- [ ] A different body with the same key is a documented conflict, not a silent overwrite
- [ ] Upstream timeout becomes a failed job or a documented HTTP error, and the test finishes
- [ ] 404 from upstream is not retried
- [ ] 503 from upstream is retried up to the limit and then recorded
- [ ] Pagination tests cover an interior page
- [ ] Missing token returns 401 and the body does not contain the secret
- [ ] Repository tests use a temporary database
- [ ] README says how to install, run, and test
- [ ] You can explain the path of one request without opening every file
