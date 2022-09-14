#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    value = 0
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
