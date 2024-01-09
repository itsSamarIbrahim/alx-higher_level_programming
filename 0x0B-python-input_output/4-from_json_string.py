#!/usr/bin/python3
"""
Module: 4-from_json_string
a function that returns an object (Python data structure) represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Convert the given JSON string to a Python object.

    Args:
    my_str (str): The JSON string to be converted to a Python object.

    Returns:
    object: The Python object represented by the input JSON string.
    """
    return json.loads(my_str)
