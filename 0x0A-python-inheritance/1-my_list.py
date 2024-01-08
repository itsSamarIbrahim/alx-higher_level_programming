#!/usr/bin/python3
"""
Module: 1-my_list
a class MyList that inherits from list
"""


class MyList(list):
    """
    A custom list class that extends the built-in list class.

    This class provides additional functionality for working with lists.

    Attributes:
    Inherits all attributes and methods from the built-in list class.

    Methods:
    print_sorted(): Prints the elements of the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
