#!/usr/bin/python3
"""Defines the json file writing function."""
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a file using Json rep"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
