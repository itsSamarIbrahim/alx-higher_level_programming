#!/usr/bin/python3
"""
Module: 8-class_to_json
a function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns a dictionary description suitable for JSON serialization of
    an object

    Args:
    obj: The object to be serialized.

    Returns:
    dict: A dictionary containing the serialized object data.
    """
    return obj.__dict__
