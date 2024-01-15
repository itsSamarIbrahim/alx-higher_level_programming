#!/usr/bin/python3
"""
model-1
"""
import json


class Base:
    """
    Base class for creating objects with unique IDs.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object with a unique ID.

        Args:
        id (int, optional): The ID to assign to the object.
        If not provided, a unique ID will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list):
            A list of dictionaries to be converted to JSON.

        Returns:
            str:
            A JSON string representation of the input list of dictionaries.
            If the input list is None or empty, returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
