#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divide = a / b
    except Exception:
        return divide
    finally:
        print("Inside result: {}".format(divide))
        return None
