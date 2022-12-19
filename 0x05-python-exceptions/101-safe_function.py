#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    
    """Executes a function safely.
    Args:
        fct: The function to execute.
        args: Arguments for fct.
    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    
    try:
        return fct(*args)
    except Exception as e:
        error = "Exception: " + str(e) + "\n"
        sys.stderr.write(error)
        return None
    
