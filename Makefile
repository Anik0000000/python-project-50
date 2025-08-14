install:
	uv pip install .

test:
	pytest -xvv

test-coverage:
	pytest --cov=gendiff --cov-report xml

lint:
	ruff check .
	ruff format --check .

format:
	ruff format .

build:
	uv pip install build
	python -m build

publish:
	uv pip install twine
	twine upload dist/*