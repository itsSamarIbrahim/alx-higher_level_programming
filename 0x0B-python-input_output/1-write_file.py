#!/usr/bin/python3
"""
Module: 1-write_file
a function that writes a string to a text file (UTF8) and returns the number
of characters written
"""


def write_file(filename="", text=""):
    """
    Write the specified text to the given file.

    Args:
    filename (str): The name of the file to be written.
    text (str): The text to be written to the file.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="UTF-8") as File:
        return File.write(text)
