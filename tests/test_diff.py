import os

from gendiff import generate_diff


def get_fixture_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', filename)


def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read().strip()


def test_flat_json_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file(get_fixture_path('expected_diff.txt'))
    
    assert generate_diff(file1, file2) == expected