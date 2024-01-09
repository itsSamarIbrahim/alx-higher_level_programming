#!/usr/bin/python3
"""
Module: 3-to_json_string
a function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Convert the given object to a JSON string.

    Args:
    my_obj: The object to be converted to a JSON string.

    Returns:
    str: The JSON representation of the input object.
    """
    return json.dumps(my_obj)
