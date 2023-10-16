#!/usr/bin/python3

'''Defines a python function that converts a py class to json.'''


def class_to_json(obj):
    '''Retruns a dictionary representative of a simple data structure.'''
    return obj.__dict__
