#!usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError('a Must be an integer')
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError('b Must be an integer')
    return a + b