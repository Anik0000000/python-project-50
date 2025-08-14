import pytest

from gendiff.generate_diff import generate_diff

json_old = "tests/test_data/file3.json"
json_new = "tests/test_data/file4.json"
yaml_old = "tests/test_data/file3.yaml"
yaml_new = "tests/test_data/file4.yaml"

stylish = "tests/test_data/nested_stylish"
plain = "tests/test_data/nested_plain"
jsonn = "tests/test_data/json.json"


@pytest.mark.parametrize(
    "path1, path2, format_name, expected",
    [
        (json_old, json_new, "stylish", stylish),
        (json_old, json_new, "plain", plain),
        (json_old, json_new, "json", jsonn),
        (yaml_old, yaml_new, "stylish", stylish),
        (yaml_old, yaml_new, "plain", plain),
        (yaml_old, yaml_new, "json", jsonn),
    ],
)
def test_generate_diff(path1, path2, format_name, expected):
    with open(expected) as expectation:
        assert generate_diff(path1, path2, format_name) == expectation.read()
