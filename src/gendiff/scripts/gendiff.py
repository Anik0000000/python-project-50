import argparse
import json
from pathlib import Path


def parse_file(file_path):
    with open(file_path) as f:
        return json.load(f)


def generate_diff(file1_path, file2_path, format_name='stylish'):
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    return f"Comparing:\n{data1}\nand\n{data2}"


def main():
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