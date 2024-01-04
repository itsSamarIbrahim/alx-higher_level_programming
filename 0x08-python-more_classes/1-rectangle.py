#!/usr/bin/python3
"""
a Rectangle class that defines a rectangle:
"""


class Rectangle:
    """A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with the given width and height."""
        self.width = width
        self.height = height

    @property
    """int: The width of the rectangle."""
    def width(self):
        return self.__width

    @width.setter
    """Set the width of the rectangle.

       Args:
           value (int): The width value to be set.

       Raises:
           TypeError: If the width is not an integer.
           ValueError: If the width is less than 0.
    """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """int: The height of the rectangle."""
    def height(self):
        return self.__height

    @height.setter
    """Set the height of the rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
    """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
