#!/usr/bin/python3
"""Square module"""


class Square:
    """define a class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializing a new square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        """sets the position to a value"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(element, int) for element in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
