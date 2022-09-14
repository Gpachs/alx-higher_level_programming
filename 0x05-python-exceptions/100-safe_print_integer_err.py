#!/usr/bin/python3
def safe_print_integer_err(value):
    value = 0
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
