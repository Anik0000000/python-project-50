.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using uv"
	@uv sync

test:
	pytest -xvv

test-coverage:
	pytest --cov=gendiff --cov-report xml

lint:
	ruff check --fix

check:
	python -m pytest
	ruff check --fix