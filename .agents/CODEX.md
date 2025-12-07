# CODEx – Contributor Onboarding for daplug-s3

This guide keeps agents aligned with the project’s expectations. Read it before modifying the repo.

## Mission Overview
- Library: `daplug_s3`, a schema-aware S3 adapter built atop `daplug_core.BaseAdapter`.
- Python version: **3.10.14** (enforced via Pipenv).
- Key feature set: S3 CRUD operations, streaming uploads, multipart uploads, presigned URLs, SNS publish hooks.

## Environment & Tooling
1. **Dependency management:** Pipenv only. Never install with raw `pip`.
   - Install: `pipenv install --dev`
   - Shell: `pipenv shell` (optional) or prefix commands with `pipenv run`.
2. **Quality gates:**
   - Lint: `pipenv run lint` (expects 10/10).
   - Type check: `pipenv run type-check` (MyPy, Python 3.9 target).
   - Unit tests: `pipenv run test` (runs `tests/unit`).
   - Coverage sweep: `pipenv run coverage` (unit + integration for coverage reports).
   - Integration tests: `pipenv run integrations` (uses docker-compose + LocalStack S3). Ensure Docker is running.
3. **Mock assets:** JSON/PDF/CSV/TXT fixtures live under both `tests/unit/mocks` and `tests/integrations/mocks`.
4. **CI:** CircleCI with two workflows.
   - `install-build-test-workflow`: lint → mypy → unit tests on `localstack` S3 → package-smoke-test job that builds a wheel, installs it into a clean venv, and reruns tests (unit + LocalStack integration).
   - `install-build-publish-workflow`: runs `install-build-publish` when tags are pushed (PyPI release).

## Testing Expectations
- Unit suite (`tests/unit`) must stay at **100%** coverage.
- Each adapter method has both positive and negative coverage. Limit assertions per test (≤3) and avoid log assertions.
- Integration suite exercises real S3 interactions against LocalStack. Do not bypass publish calls—tests patch `BaseAdapter.publish` as necessary.
- When adding tests, run them immediately (`pipenv run pytest path/to/test_file`) before touching other files.

## Coding Constraints
- **Do not modify** `daplug_s3` implementation unless explicitly assigned; default task scope is tests/docs/infra.
- Avoid `Any`; use `TypedDict` definitions found in `daplug_s3/types/s3.py` when annotating new utilities.
- Keep imports sorted/grouped (standard, third-party, local).
- Respect existing publishing contract: `BaseAdapter.publish(db_data=..., **kwargs)`; tests should mock via monkeypatch on `BaseAdapter.publish`.

## Local Development Workflow
1. `pipenv install --dev`
2. Make targeted edits.
3. Run the relevant quick checks (unit tests, lint, mypy) before broad changes.
4. Before yielding, run:
   - `pipenv run lint`
   - `pipenv run type-check`
   - `pipenv run test`
   - `pipenv run integrations` (only if integration paths touched)
5. Summaries should list commands executed.

## Integration Harness
- `tests/integrations/docker-compose.yml` spins up `localstack/localstack:3.2` with S3.
- The `pipenv run integrations` script wraps compose up/down and exports:
  - `AWS_ACCESS_KEY_ID=test`
  - `AWS_SECRET_ACCESS_KEY=test`
  - `AWS_DEFAULT_REGION=us-east-1`
  - `S3_ENDPOINT=http://localhost:4566`
- Integration fixtures (`tests/integrations/conftest.py`) wait for LocalStack, create the bucket, and auto-clean objects after each test.

## CI Artifacts & Smoke Tests
- Coverage, lint, typing outputs stored in `./coverage/...` and uploaded by CircleCI.
- Package smoke test job:
  1. Attach workspace.
  2. `pipenv run python -m build` to create wheel.
  3. Install wheel into `/tmp/package-smoke` virtualenv along with dev requirements (generated via `pipenv requirements --dev`).
  4. Run unit and integration suites from the installed package while LocalStack is running.

## Communication Conventions
- Plans live in `.agents/plans/*`; update or add one when requested.
- Respond concisely; mention only relevant commands.
- Never undo or overwrite user changes outside your scope.

## Common Pitfalls
- Forgetting to run tests after each new file addition. Always run targeted pytest command before proceeding.
- Installing deps with `pip` instead of Pipenv (strictly forbidden).
- Leaving docker-compose stacks running; rely on provided integration script to auto-clean.
- Publishing kwargs removed from adapter; tests must no longer toggle `publish=False`.

Keep this file current as processes evolve. EOF
