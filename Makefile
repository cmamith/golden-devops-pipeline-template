.PHONY: fmt lint test dep-audit

fmt:
	python -m black app tests

lint:
	python -m ruff check app tests

test:
	python -m pytest -q

dep-audit:
	python -m pip_audit -r requirements.txt
