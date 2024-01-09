#!/usr/bin/python3
"""
Module: 11-square
This is a class Square that inherits from Rectangle class as the base class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle
    where all sides are of equal length.

    Args:
    Rectangle (class): The base class for rectangles.

    Methods:
    __init__(self, size): Initializes a square with the given size.

    Attributes:
    __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes a square with the given size.

        Args:
        size (int): The size of the square.

        Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is not greater than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: A string in the format "[Square] size/size" representing
        the square's size.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
