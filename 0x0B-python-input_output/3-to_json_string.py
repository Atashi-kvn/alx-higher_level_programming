#!/usr/bin/python3

'''Defines a string-to Json function.'''
import json

def to_json_string(my_obj):
    '''Returns the json representation of a string object'''
    return json.dumps(my_obj)
