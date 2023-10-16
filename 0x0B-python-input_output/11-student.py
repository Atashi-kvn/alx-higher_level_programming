#!/usr/bin/python3

"""Defines class student"""


class student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        '''Initialize a new student
           Args:
               firsfirst_name (str): The first name of the student.
               last_name (str): The last name of the student.
               age (int): The age of the student.'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a disctionary rep of student
        if attrs is a list of strings, represent only those attributes
        included in the list

        Args:
            attrs (list): (optional) The attributes to represent """

        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replace all attributes of the student

        Args:
           json(dict): The key/value pairs to replace attributes with """

        for k, v, in json.items():
            setattr(self, k, v)
