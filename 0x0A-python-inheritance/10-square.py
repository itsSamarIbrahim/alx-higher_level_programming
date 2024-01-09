#!/usr/bin/python3
"""
Module: 10-square
This is a class Square that inherits from Rectangle class as the base class
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle where all sides are of equal length.

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
