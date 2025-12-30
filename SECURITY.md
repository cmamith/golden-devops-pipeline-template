# Security notes

- Do not hardcode secrets.
- Use GitHub OIDC to assume AWS roles (no static keys).
- PR checks should be required before merge to main.
- Image scanning blocks HIGH/CRITICAL vulnerabilities by default.
