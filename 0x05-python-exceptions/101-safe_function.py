#!/usr/bin/python3
from sys import stderr

"""Executes a function safely.
    Args:
        fct: The function to execute.
        args: Arguments for fct.
    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ex:
        stderr.write("Exception: " + ex.__str__() + "\n")
