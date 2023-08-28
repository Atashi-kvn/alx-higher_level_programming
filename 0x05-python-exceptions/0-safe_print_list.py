#!/usr/bin/python3

def safe_print_list(my_list=[], j=0):
    """Print j elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        j (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for k in range(j):
        try:
            print("{}".format(my_list[k]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
