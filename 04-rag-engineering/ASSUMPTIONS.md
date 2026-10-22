# Stage 04 Assumptions

- Default path needs no Docker and no API key.
- Fake embeddings are required for tests. Live embeddings are optional.
- PostgreSQL with pgvector is the advanced store. A compose file is in `infra/docker-compose.yml`. The image tag `pgvector/pgvector:pg16` was a common official image at generation time. Confirm the tag before you rely on it.
- pgvector Python package 0.5.x, checked on 2026-10-21, expects Python 3.10+ and SQLAlchemy 2 if you use SQLAlchemy. You may use `psycopg` with SQL text instead. Do not copy a blog's operator blindly. Check the distance operator for cosine versus L2 in the pgvector docs for the version you installed.
- Stage 12 will expand evaluation. This stage's golden set is intentionally tiny.
