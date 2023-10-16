#!/usr/bin/python3
'''Define a file appending function.'''


def append_write(filename="", text=""):
    '''will append a string to the end of a UTF8 file.
    Args:
        filename(str): The name of the file to appenf to.
        text(str): The dtring to append to a file.
    Returns:
    The number of character appended.'''

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
