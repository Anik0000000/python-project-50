import json
from collections import OrderedDict


def parse_file(file_path):
    with open(file_path) as f:
        return json.load(f, object_pairs_hook=OrderedDict)


def build_diff(dict1, dict2):
    diff = []
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    
    for key in keys:
        if key not in dict1:
            diff.append((key, 'added', dict2[key]))
        elif key not in dict2:
            diff.append((key, 'removed', dict1[key]))
        elif dict1[key] == dict2[key]:
            diff.append((key, 'unchanged', dict1[key]))
        else:
            diff.append((key, 'changed', (dict1[key], dict2[key])))
    return diff


def format_diff(diff):
    lines = []
    for key, status, value in diff:
        if status == 'unchanged':
            lines.append(f"    {key}: {value}")
        elif status == 'removed':
            lines.append(f"  - {key}: {value}")
        elif status == 'added':
            lines.append(f"  + {key}: {value}")
        elif status == 'changed':
            old_val, new_val = value
            lines.append(f"  - {key}: {old_val}")
            lines.append(f"  + {key}: {new_val}")
    return '{\n' + '\n'.join(lines) + '\n}'


def generate_diff(file1_path, file2_path, format_name='stylish'):
    dict1 = parse_file(file1_path)
    dict2 = parse_file(file2_path)
    diff = build_diff(dict1, dict2)
    return format_diff(diff)


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', 
                      help='set format of output',
                      default='stylish')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))