#!/usr/bin/python3
"""
Module: 8-rectangle
a class BaseGeometry
Public instance method: def area(self): that raises an Exception
  with the message area() is not implemented
Public instance method: def integer_validator(self, name, value):
  that validates value:
    you can assume name is always a string
    if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
    if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
This is a rectangle class that inherit the BaseGeometry
from the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry:
    """
    A base class for geometric shapes.

    Methods:
    area(self): Raises an exception indicating that
                the area calculation is not implemented.
    """
    def area(self):
        """
        This method raises an exception to indicate that
        the area calculation is not implemented for this geometric shape.

        Raises:
        Exception: Always raises an exception
        with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if the given value is an integer and greater than 0.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

class Rectangle(BaseGeometry):
    """
    Rectangle (class): create a rectangle from base geometry
    Args:
    BaseGeometry (class): The base class for geometric shapes.

    Methods:
    __init__(self, width, height): Initializes a rectangle
    with the given width and height.

    Attributes:
    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: If the width or height is not an integer.
        ValueError: If the width or height is not greater than 0.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
