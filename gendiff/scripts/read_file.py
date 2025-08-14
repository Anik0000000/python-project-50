import requests
import yaml

from .parser import parse


def read_file(file_path):
    with open(file_path) as f:
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(f)
        elif file_path.endswith('.json'):
            return json.load(f)
        raise ValueError("Unsupported file format")


def network_data(url):
    data = requests.get(url).text

    if url.endswith("json"):
        return parse(data, "json")

    elif url.endswith("yaml") or url.endswith("yml"):
        return parse(data, "yaml")
