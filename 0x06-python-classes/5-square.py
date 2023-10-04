#!/usr/bin/python3


class Square:
    """
    The class square has the following attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        The initialization of the function our square class
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        gets the size of property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size property
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        For calculating the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        will print the square using '#' characters
        """
        i = 0
        for a in range(0, self.__size):
            b = 0
            for b in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        validates the size, checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than 0")
        else:
            return True
        return False
