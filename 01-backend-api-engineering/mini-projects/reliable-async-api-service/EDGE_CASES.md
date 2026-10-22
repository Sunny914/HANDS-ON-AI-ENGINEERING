# Edge Cases

| Case | Required behavior |
|------|-------------------|
| Missing idempotency key | Accept the job. Do not pretend it is safe to retry from the client. |
| Reused key, same body | Return the stored job. No second upstream call. |
| Reused key, different body | 409 or another documented conflict. |
| Upstream 404 | Do not retry. Job failed or request failed, as you documented. |
| Upstream 503 then 200 | Succeed if the success happens within the attempt limit. |
| Timeout | Bounded wait. Controlled error. |
| Invalid URL | 422. No outbound call. |
| page_size above 100 | 422. |
| Empty database list | 200 and an empty page. |
| Process restart | Job still fetchable from SQLite. |
| Two keys in flight | Single-process tests only. Document the race you are not solving. |
