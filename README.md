# Golden DevOps Pipeline Template (GitHub Actions + Docker + AWS ECR via OIDC)

This is a clone-and-go template repo you can start from a feature branch.

## What you get
- **PR checks**: format, lint, tests, dependency scan (OSV), optional IaC scan hooks
- **Security**: CodeQL (SAST) on PR/push, Dependabot
- **Build & ship**: Docker build + **Trivy image scan** (fail on HIGH/CRITICAL) + push to **ECR**
- **No static AWS keys**: uses **GitHub OIDC** to assume an IAM role

## Repo layout
- `app/` : tiny Flask app
- `tests/` : pytest smoke test
- `.github/workflows/` : PR checks, CodeQL, build-scan-push to ECR
- `.github/dependabot.yml` : dependency updates

## Quick start (local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
make fmt lint test
docker build -t demo:local .
```

## GitHub setup (minimal)
1) Create a new GitHub repo and push this code.
2) Create an **ECR repo** (e.g., `golden-demo`).
3) Create an **IAM role for GitHub OIDC** with permission to push to that ECR repo.
4) In GitHub repo settings, add **Repository Variables**:
   - `AWS_REGION` (example: `ap-southeast-1`)
   - `AWS_ACCOUNT_ID` (example: `123456789012`)
   - `ECR_REPOSITORY` (example: `golden-demo`)
   - `AWS_OIDC_ROLE_ARN` (example: `arn:aws:iam::123456789012:role/github-oidc-ecr`)

> Why variables? Because they’re not secrets; they’re config.

## How the pipelines work
- **PR ->** `.github/workflows/pr-checks.yml`
  - black/ruff/pytest
  - OSV scan
  - (optional hook for IaC scanning)
- **SAST ->** `.github/workflows/codeql.yml`
- **main push ->** `.github/workflows/build-scan-push.yml`
  - build image
  - Trivy scan (fails on HIGH/CRITICAL)
  - push to ECR (OIDC role)

## Branch protection (recommended)
Protect `main`:
- Require PR
- Require status checks: `pr-checks` + `CodeQL`
- Require at least 1 review

## Next step (GitOps handoff)
If you want, add a 2nd repo `gitops-apps` and update a Helm values file with the new image tag (commit/PR).
That keeps deployment separated and clean.
