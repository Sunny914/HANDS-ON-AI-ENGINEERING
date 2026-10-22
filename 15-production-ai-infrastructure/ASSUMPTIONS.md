# Stage 15 Assumptions

- The HTTP stack from Stage 01 is the expected local server. This stage does not introduce a second web framework.
- Docker is required for the project smoke milestone and not for the earlier exercises. This audit did not build an image. Write the Dockerfile yourself and confirm the syntax with your installed Docker.
- Kubernetes, cloud registries, and paid model APIs are not required. `APP_MODE=live` is optional.
- No Redis or Celery package is required for the core path.
- Retry and timeout behavior is defined by your tests and the concept notes, not by an unstated library default.
