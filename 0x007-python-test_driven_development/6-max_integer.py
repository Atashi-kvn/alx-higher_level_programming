#!/usr/bin/python3

def max_integer(list=[]):
    if len(list) == 0:
        return None
    result = list[0]
    a = 1

    while a < len(list):
        if list[a] > result:
            result = list[a]
        a += 1
    return result