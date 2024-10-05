"""Functions for manipulating data

Raises:
    SyntaxError: File path not found

Returns:
    _type_: list, None
"""

import json
import os

def read_jsonl(url: str) -> list:
    """Reads a JSONL file and returns a list of dictionaries."""
    # Raise error if cannot find file path
    if not os.path.exists(url):
        raise SyntaxError('File path not found')

    data = []
    with open(url, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))

    return data

def show_data(data: list) -> None:
    """Reads a list of dictionaries and prints the data."""

    print("Data type:", type(data))
    print("Length of data:", len(data))
    print("\n")
    print("First 5 values: \n")
    for value in data[:5]:
        print(json.dumps(value, indent=2))
