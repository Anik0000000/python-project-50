lint:
	python -m ruff check src/

test:
	python -m pytest tests/

coverage:
	python -m pytest --cov=gendiff --cov-report=xml tests/