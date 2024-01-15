#!/usr/bin/python3
"""
model-1
"""


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
