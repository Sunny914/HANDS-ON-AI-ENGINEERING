# arch-03 — Reference Architecture (after your design)

## Components

- `settings.py` — load/merge config
- `logging_config.py` — configure root logger from settings
- `csv_loader.py` — generator of row dicts
- `dedupe.py` — pure dedupe function
- `report.py` — build summary dict
- `pipeline.py` or `service.py` — orchestration
- `main.py` — entry

## Dependency injection

`main(settings)` wires `pipeline(csv_path, output_path)`; tests call `dedupe` and `build_report` directly.

## Generator use

`csv_loader` yields rows; pipeline consumes without storing all rows if possible (still may need dict for dedupe—document tradeoff).
