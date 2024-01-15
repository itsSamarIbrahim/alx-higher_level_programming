#!/usr/bin/python3
"""
model Base
"""
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class with attributes set from a dictionary.

        Args:
            **dictionary:

            Arbitrary keyword arguments representing
            the attributes of the instance.

        Returns:
            Base: An instance of the class with
                  attributes set from the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file in JSON format.

        Returns:
            list:
            List of instances loaded from the file.
            If the file doesn't exist, returns an empty list.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding="UTF-8") as File:
                json_string = File.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to be serialized.

        Returns:
            None
        """
        filename = __name__ + ".csv"
        with open(filename, 'w', newline='', encoding="UTF-8") as File:
            writer = csv.writer(File)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width,
                                     obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a CSV file to a list of instances.

        Returns:
            list: A list of instances deserialized from the CSV file.
        """
        filename = __name__ + ".csv"
        try:
            with open(filename, 'r', newline='', encoding="UTF-8") as File:
                reader = csv.reader(File)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[0]), int(row[1]),
                                       int(row[2]), int(row[3]), int(row[4]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[0]), int(row[1]),
                                       int(row[2]), int(row[3]))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
