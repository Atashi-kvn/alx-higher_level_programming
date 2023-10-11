#!/usr/bin/python3

'''Defines a class student'''
class student:
    def __init__(self, first_name, last_name, age):
        '''Initialize a new student

        Args:
            first_name (str): The first name of student.
            last_name (str): The last name ot the student
            age (int): The age of the student.
            '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        '''Getting a dictionary rep of the student

        if attrs is a list of string, represents only attributes included in the list
        Args:
            attrs (list): (optional) The attribute to represent
            '''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return{_: getattr(self, _) for _ in attrs if hasattr(self, _)}
        return self.__dict__
