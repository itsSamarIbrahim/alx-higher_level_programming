#!/usr/bin/python3
"""Square module"""


class Square:
    """define a class Square"""
    def __init__(self, size=0):
        """initializing a new square
        Args:
            size: square's size
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the square area"""
        return (self.__size ** 2)
