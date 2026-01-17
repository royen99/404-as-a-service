# GitHub Actions CI/CD

This repository uses GitHub Actions for automated testing and quality checks.

## Workflows

### CI Tests (`.github/workflows/ci.yml`)
Runs on every push and pull request to main branches.

**Jobs:**
- **test**: Runs tests on Python 3.12 and 3.13
  - Installs dependencies
  - Lints code with Ruff
  - Checks formatting
  - Runs pytest with coverage
  - Uploads coverage to Codecov (optional)

- **docker-build**: Validates Docker setup
  - Builds Docker image
  - Tests health endpoint

### Lint and Format (`.github/workflows/lint.yml`)
Runs on pull requests for code quality checks.

**Jobs:**
- Runs Ruff linter
- Checks code formatting

## Status Badges

Add to your README.md:

```markdown
![CI Tests](https://github.com/YOUR_USERNAME/404-as-a-service/workflows/CI%20Tests/badge.svg)
![Lint and Format](https://github.com/YOUR_USERNAME/404-as-a-service/workflows/Lint%20and%20Format/badge.svg)
```

## Local Testing

Before pushing, run locally:

```bash
# Run tests
pytest -v --cov=app

# Check linting
ruff check .

# Check formatting
ruff format --check .

# Auto-fix formatting
ruff format .
```

## Codecov Integration (Optional)

To enable coverage reports:
1. Sign up at https://codecov.io
2. Add `CODECOV_TOKEN` to your repository secrets
3. Coverage reports will appear on PRs

## Notes

- Tests must pass before merging PRs
- Ruff checks enforce code quality
- Docker build validates container setup
- Matrix testing ensures Python 3.12 and 3.13 compatibility
