#!/usr/bin/python3
def print_last_digit(number):
    '''print last digit of a number'''
    lstd = abs(number) % 10
    print(f"{lstd}", end='')
    return (lstd)
