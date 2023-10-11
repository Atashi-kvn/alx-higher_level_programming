#!/usr/bin/python3
"""Defines a text file reading function."""

def read_file(filename=""):
    """Will print the content of a UTF8 file."""
    with open(filename, encoding="utf-8') as file:
        print(file.read(), end="")
