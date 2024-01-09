#!/usr/bin/python3
"""
Module: 5-save_to_json_file
a function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save the given object as a JSON string to the specified file.

    Args:
    my_obj: The object to be saved as a JSON string.
    filename (str): The name of the file to which the JSON string will be saved
    """
    with open(filename, "w", encoding="UTF-8") as File:
        json.dump(my_obj, File)
