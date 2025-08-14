install:
	uv pip install .

test:
	pytest -xvv

test-coverage:
	pytest --cov=gendiff --cov-report xml

lint:
	ruff check .
