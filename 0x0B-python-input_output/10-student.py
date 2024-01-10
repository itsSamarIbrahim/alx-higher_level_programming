#!/usr/bin/python3
"""
Module: 9-student
a class Student that defines a student
"""


class Student:
    """
    A class representing a student.

    Attributes:
    first_name (str): The first name of the student.
    last_name (str): The last name of the student.
    age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student
        for JSON serialization.

        Args:
        attrs (list): A list of strings containing attribute names.

        Returns:
        dict: A dictionary containing the student's data.
        """
        if attrs is None:
            return self.__dict__
        else:
            student_data = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_data[attr] = getattr(self, attr)
            return student_data
