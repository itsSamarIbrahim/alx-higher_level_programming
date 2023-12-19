#!/usr/bin/python3
"""Square module"""


class Square:
    """define a class Square"""
    def __init__(self, size=0):
        """initializing a new square"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            size: square's size
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print("")
