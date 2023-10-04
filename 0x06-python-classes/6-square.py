#!/usr/bin/python3


class Square:
    """
    The class square has the following attribute:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialization of the function for our square class
        """
        if self.__validate_size(size):
            self.__size = size
        if self.__validate_pos(position):
            self.__position = position

    @property
    def size(self):
        """
        gets the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    @property
    def position(self):
        """
        gets the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position attribute
        """
        if self.__validate_pos(value):
            self.__position = value

    def area(self):
        """
        For calculating the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Will print the square using '#' character
        also takes into account position (x, y) offsets
        """
        a = 0
        if self.__size == 0:
            print()
            return
        for a in range(0, self.__position[1]):
            print()
        a = 0
        for a in range(0, self.__size):
            b = 0
            x_pad = 0
            for x_pad in range(0, self.__position[0]):
                print(" ", end='')
            for b in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        will validate the size and checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater 0")
        else:
            return True
        return False

    def __validate_pos(self, position):
        """
        will validate the position and checking for type errors
        """
        if not isinstance(position, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        return True
