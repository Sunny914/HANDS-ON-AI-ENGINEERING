# Stage 00 — Hints (H1 / H2 / H3)

Do not skip to H3. Do not request implementation code (H4) until you have attempted the exercise.

**H1** = conceptual · **H2** = design/architecture · **H3** = pseudocode (no full solution)

---

## Module 00

### ex-09 — Scope and mutable defaults
- **H2:** Separate “accumulator” state from the function object defaults; factory pattern creates fresh state per caller.
- **H3:** `append_item_right(item, bucket=None): if bucket is None: bucket = []` then append and return bucket.

### ex-13 — Two-module word statistics
- **H2:** `tokenize` returns tokens; `stats` consumes iterable; `__main__` wires path → tokens → counts → print.
- **H3:** `main(): path = sys.argv[1]; tokens = tokenize(read(path)); print(top_k(freq(tokens), 5))`

### ex-15 / ex-16 — Design exercises
- **H2:** Three layers: `cli` → `service` → `storage` (names flexible).
- **H3:** CLI parses command → calls service method → service reads/writes via storage functions.

### ex-17 — Debug mutation
- **H1:** Aggregates may share the same list object in memory.
- **H2:** Look for `.append` on a list that is also stored as a group member.
- **H3:** When starting a new group, allocate a **new** list; do not reuse a module-level or default list.

### ex-18 — Debug None
- **H1:** `or` treats `0` and `""` like missing values.
- **H2:** Merge function should treat “key absent” differently from “key present with falsy value.”
- **H3:** For each field: if key in secondary: take secondary’s value elif key in primary: take primary’s else default.

### ex-19 — Debug paths
- **H2:** Resolve paths relative to package directory, not process cwd.
- **H3:** `base = Path(__file__).resolve().parent; path = base / "data" / "settings.json"`

### ex-20 — Debug imports
- **H2:** Draw import arrows; ensure package on path when using `-m`.
- **H3:** Fix order: define symbols before use; use relative imports inside package consistently.

### ex-23 — Integration pipeline
- **H2:** Config module loads dict; parser yields rows; reporter consumes iterator; main wires them.
- **H3:** `settings = load_config(); for row in parse(path, settings.categories): accumulate; format_report(accum)`

---

## Module 01

### arch-01 / arch-02 / arch-03
- **H1:** Validation is a gate between I/O and domain operations.
- **H2:** Inbound: `loader` → `validator` → `service` → `reporter`/`writer`; errors bubble to CLI.
- **H3:** `main(): data = load(path); records = [validate(r) for r in data]; report = build_report(records); write(out, report)`

### ex-10 — Configuration
- **H2:** Merge dicts in order: defaults < file < env; env keys strip prefix and map to field names.
- **H3:** `def load_settings(): d = defaults(); d.update(file_load()); d.update(env_overrides()); return Settings(**d)`

### ex-12 — Service boundary
- **H2:** Repository raises `UserNotFound`; service never catches generic Exception; CLI catches domain errors only.
- **H3:** `try: user = service.get(id); except UserNotFound: print(...); sys.exit(1)`

### test-04 — Fixtures
- **H1:** Fixture builds path; test writes sample file; loader under test reads it.
- **H2:** Keep JSON sample minimal—one valid object.

### test-05 — Mocking
- **H1:** Patch where dependency is **used**, not where defined.
- **H2:** Inject fetch function into service constructor for easier testing without patch.

### dbg-01 — Mutation
- **H1:** Cached list reused across calls.
- **H2:** Inspect service method that clears or extends shared state.

### dbg-02 — Imports
- **H2:** Running as script vs package changes import root.

### dbg-03 — Resources
- **H1:** File not closed on exception path.
- **H2:** Compare `open` without `with` vs `with`.

### dbg-04 — Types/None
- **H1:** Comparisons between str and int from JSON.
- **H2:** Normalize types at parse boundary.

### dbg-05 — Tests misleading
- **H1:** Test mocks too much; production path untested.
- **H2:** Compare test import path vs runtime entry point.

---

## Module 02

### ex-03 — gather
- **H1:** `gather` schedules coroutines; they interleave while awaiting I/O.
- **H2:** Create coroutines first, then `await gather(*tasks)`.

### ex-04 — Timeouts
- **H2:** `asyncio.wait_for(coro, timeout)` wraps slow tasks.
- **H3:** On timeout, decide: skip task, record error, continue others.

### ex-05 / ex-06 — Comparison
- **H2:** Sequential sums latencies; concurrent approaches max latency (ideal case).
- **H3:** Semaphore: `async with sem: await fetch(u)` limits parallel section.

---

## Mini-project 1 — CLI Task & Job Manager
- **H1:** Commands map to service methods; JSON is infrastructure detail.
- **H2:** `cli` → `TaskService` → `TaskRepository`; `models` hold Task entity; `validation` at service entry.
- **H3:** `create(cmd): dto = parse_args(cmd); task = service.create(validate(dto)); repo.save(all_tasks)`

## Mini-project 2 — Log Analysis CLI
- **H1:** Parser yields `LogRecord` or None for bad lines; analyzer consumes stream.
- **H2:** `parser` (generator) → `aggregator` (state object) → `reporter` (format).
- **H3:** `for rec in parse_lines(path): agg.consume(rec); return agg.summary()`
