from collections import OrderedDict

from gendiff.formatters.json_formated import format_json
from gendiff.formatters.plain_formated import format_plain
from gendiff.formatters.stylish_formated import format_stylish

from .read_file import read_file


def gen_diff(data1, data2) -> dict:
    diff = {}
    keys = set(data1.keys() | set(data2.keys()))

    for i in keys:
        if isinstance(data1.get(i), dict) and isinstance(data2.get(i), dict):
            diff[i] = {"type": "nested", "value": gen_diff(data1[i], data2[i])}
        elif i not in data1.keys():
            diff[i] = {"type": "added", "value": data2[i]}
        elif i not in data2.keys():
            diff[i] = {"type": "removed", "value": data1[i]}
        elif data1[i] == data2[i]:
            diff[i] = {"type": "unchanged", "value": data1[i]}
        else:
            diff[i] = {"type": "changed", "old": data1[i], "new": data2[i]}

    return OrderedDict(sorted(diff.items(), key=lambda k: k))


def generate_diff(
    file_path1: str,
    file_path2: str,
    format_name: str = "stylish"
    ) -> str:
   
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = gen_diff(data1, data2)

    formatters = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json
    }

    if format_name not in formatters:
        raise ValueError(f"Unknown format: {format_name}")

    return formatters[format_name](diff) 