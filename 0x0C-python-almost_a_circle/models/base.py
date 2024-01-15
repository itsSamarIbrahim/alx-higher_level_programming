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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list of objects to a file.

        Args:
            list_objs (list):
            A list of objects to be serialized to JSON and written to a file.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="UTF-8") as File:
            json.data = [obj.to_dictionary() for obj in list_objs]
            json.string = cls.to_json_string(json.data)
            File.write(json.string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by the JSON string.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: The list represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
