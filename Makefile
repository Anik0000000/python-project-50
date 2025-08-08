lint:
	ruff check .

test:
	pytest tests/

coverage:
	pytest --cov=gendiff --cov-report=xml tests/