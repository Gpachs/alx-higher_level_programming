#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct
        return result
    except Exception:
        print(file=sys.stderr)
        return None
