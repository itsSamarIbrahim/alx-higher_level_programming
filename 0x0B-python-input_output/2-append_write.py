#!/usr/bin/python3
"""
Module: 2-append_write
a function that appends a string at the end of a text file (UTF8) and returns
the number of characters added
"""


def append_write(filename="", text=""):
    """
    Append the specified text to the given file.

    Args:
    filename (str): The name of the file to which the text will be appended.
    text (str): The text to be appended to the file.

    Returns:
    int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="UTF-8") as File:
        return File.write(text)
