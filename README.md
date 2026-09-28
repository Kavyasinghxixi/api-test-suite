# API Test Suite

Automated tests for the ReqRes public API using PyTest.

## What this tests
- User retrieval (valid and invalid IDs)
- User creation
- Error handling (404s)
- Edge cases: invalid formats, empty payloads, response time

## How to run
1. `pip install -r requirements.txt`
2. `pytest -v`
3. For an HTML report: `pytest --html=report.html`