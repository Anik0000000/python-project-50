# Gendiff - JSON Difference Generator

Compares two JSON configuration files and shows a difference.

## Installation
```bash
pip install git+https://github.com/Anik0000000/python-project-50.git
```

## Usage
### As CLI tool
```bash
gendiff file1.json file2.json
```

Example output:
```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### As library
```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json')
print(diff)
```