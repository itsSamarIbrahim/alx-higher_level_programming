#!/usr/bin/python3
"""
Module: 9-rectangle
a class Rectangle that inherits from BaseGeometry
"""


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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The area of the rectangle calculated as the product of its width
        and height.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The area of the rectangle calculated as the product of its width
        and height.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
