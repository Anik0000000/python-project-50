.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using uv"
	@uv sync

test:
	uv run pytest -xvv

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check --fix

check:
	uv run pytest -xvv
	uv run ruff check --fix