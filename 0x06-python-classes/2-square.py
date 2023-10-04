#!/usr/bin/python3


class Square:
    """
    class square that has an attribute:
        size
    And its protected from input.
    """
    def __init__(self, size=0):
        """
        the initialization of the function of square class
        and checks for input errors for size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size cannot be less than 0")
        else:
            self.__size = size
