#!/usr/bin/python3
"""
Module: 6-load_from_json_file.py
a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Load a JSON string from the specified file and convert it
    to a Python object.

    Args:
    filename (str): The name of the file from which the JSON string
    will be loaded.

    Returns:
    object: The Python object represented by the JSON string in the file.
    """
    with open(filename, "r", encoding="UTF-8") as File:
        return json.load(File)
