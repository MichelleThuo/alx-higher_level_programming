#!/usr/bin/python3
import sys

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
    
    result = fct(*args)
  except Exception as e:
    
    print("Exception:", e, file=sys.stderr)
    result = None
  return result

def add(x, y):
  return x + y

result = safe_function(add, 1, 2)
print(result)  # prints 3

result = safe_function(add, "a", "b")
print(result)
