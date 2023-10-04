#!/usr/bin/python3


class Square:
    """
    The class square has the following attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        initialization of the function for our square class
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        geting the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        will calculate the area of the square
        """
        return self.__size ** 2

    def __validate_size(self, size):
        """
        For validating the size, checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than 0")
        else:
            return True
        return False
