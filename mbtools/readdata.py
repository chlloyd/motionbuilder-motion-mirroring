"""
readdata.py
Utility to read json.
"""
import json


def _read_json_file(filepath):
    with open(filepath, "r") as fp:
        return json.loads(fp.read())


def _write_json_file(filepath, serialised_data):
    with open(filepath, 'w+') as fp:
        fp.write(json.dumps(serialised_data, indent=4))

