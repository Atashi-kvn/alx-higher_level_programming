#!/usr/bin/python3
"""Defines a class Student."""


class student:
    """Reps the student."""
    def __init__(self, first_name, last_name, age):
        '''Initialize a new student
        args:
            first_name (str): The first name of student
            last_name (str): The last name of stundent
            age (int): The age of the student
            '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Get a dictionary rep of the student.'''
        return self.__dict__
