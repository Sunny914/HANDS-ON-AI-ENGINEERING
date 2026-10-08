# test-05 — Test Requirements

Implement `WeatherService` with method `get_temp(city)` that calls `fetch_json(url)` you define in `http_client.py`.

## Tests

- When `fetch_json` returns `{"temp": 20}`, service returns 20
- When `fetch_json` raises, service propagates or wraps per your docstring—test that behavior
- Use `unittest.mock.patch` or pytest monkeypatch on `fetch_json` at the usage site

Do not call real HTTP in tests.
