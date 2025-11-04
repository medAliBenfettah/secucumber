secucumber — Selenium + Behave BDD tests

A small BDD test suite for OrangeHRM using Behave and Selenium. This repository includes page objects, step definitions, a driver factory, and a GitHub Actions workflow that runs smoke tests on push / PR.

## Quick overview
- Tests: Behave (Gherkin) scenarios in `features/`
- Page objects: `pages/`
- Step implementations: `features/steps/`
- Utilities (driver, config, waits): `utils/`
- Reports: generated into `allure-results/` (ignored in Git)

## Requirements
- Python 3.11+ (this project uses 3.11 in CI)
- Chrome (or change `utils.Config.BROWSER` to a browser you have)
- Git

Optional tools (recommended for prettier reports):
- Allure commandline (to serve HTML reports) — https://docs.qameta.io/allure/

## Setup (Windows PowerShell)
Run these commands from the project root:

```powershell
# create a virtual environment (one-time)
python -m venv venv

# activate the venv (PowerShell)
.\venv\Scripts\Activate.ps1

# upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install the minimal packages:

```powershell
pip install behave selenium allure-behave
```

## Running tests locally

Run all smoke tests (headless recommended):

```powershell
venv\Scripts\python.exe -m behave --tags=@smoke -f pretty
```

Run all tests:

```powershell
venv\Scripts\python.exe -m behave -f pretty
```

If you want Allure results to be produced, run Behave with the Allure formatter (requires `allure-behave`):

```powershell
venv\Scripts\python.exe -m behave --tags=@smoke -f allure_behave.formatter:AllureFormatter -o allure-results

# then view report (requires Allure CLI installed):
allure serve allure-results
```

## GitHub Actions (CI)

A workflow is provided at `.github/workflows/behave.yml`. It runs on `push` and `pull_request` to `main`, installs dependencies, runs the smoke tests, and uploads `allure-results` as an artifact. To supply secrets (for example `USERNAME`, `PASSWORD`, `BASE_URL`) add them in the repository Settings → Secrets and variables → Actions.

## Project structure

- `features/` — Gherkin feature files
- `features/steps/` — step implementations
- `pages/` — Page Object classes
- `utils/` — driver factory, wait helpers, config
- `.github/workflows/behave.yml` — CI workflow
- `requirements.txt` — Python dependencies

## Tips & best practices
- Keep feature steps stable: change step text only when necessary to avoid breaking step matches.
- Use Page Objects for UI interactions and keep steps thin.
- Do not commit `allure-results/`, `venv/`, or `__pycache__/` (they are in `.gitignore`).

## Contributing
- Create a feature branch: `git checkout -b feat/your-change`
- Make changes and run tests locally
- Push branch and open a PR targeting `main`

If you want, I can add a short CONTRIBUTING.md with test/PR checklist.

## Troubleshooting
- If step definitions aren't found, check that the step text in the `.feature` matches the decorator string exactly.
- If the editor doesn't resolve imports (yellow highlights), make sure VS Code is using the project venv (`.\venv\Scripts\python.exe`) as the interpreter and restart the language server.

