#!/usr/bin/python3
"""
Module: 0-read_file
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Read the contents of the file and print them to the console.

    Args:
    filename (str): The name of the file to be read.
    """
    with open(filename, "r", encoding="UTF-8") as File:
        print(File.read(), end="")
