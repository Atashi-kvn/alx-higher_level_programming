<<<<<<< HEAD
#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
=======
#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
>>>>>>> e91308984b15d4653713e8678c6338a0937ea88d
