#!/usr/bin/python3
"""Define a Json to object function"""
import json

def from_json_string(my_str):
    """"Return the python object representative of a Json string"""
    return json.loads(my_str)
