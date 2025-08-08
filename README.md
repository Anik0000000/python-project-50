# Gendiff - JSON Difference Generator
[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=Anik0000000_python-project-50)](https://sonarcloud.io/summary/new_code?id=Anik0000000_python-project-50)
![Python CI](https://github.com/Anik0000000/python-project-50/actions/workflows/python.yml/badge.svg)
![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=Anik0000000_python-project-50&metric=coverage)

## Installation
```bash
pip install git+https://github.com/Anik0000000/python-project-50.git
```

## Usage
### As CLI tool
```bash
gendiff file1.json file2.json
```

### As library
```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json')
print(diff)
```

## Development
```bash
make lint  # Run linter
make test  # Run tests
make coverage  # Generate coverage report
```