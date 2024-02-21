#!/usr/bin/python3
"""function to read and print a file info"""


def read_file(filename=""):
    """
    Read the contents of a file and print them to the console.

    Args:
        filename (str, optional): The name of the file to read.

    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
