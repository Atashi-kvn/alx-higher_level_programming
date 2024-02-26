<<<<<<< HEAD
#!/usr/bin/python3
"""function that checks if object is is an instance of an inherited class"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class,
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
=======
#!/usr/bin/python3
"""function that checks if object is is an instance of an inherited class"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class,
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
>>>>>>> e91308984b15d4653713e8678c6338a0937ea88d
