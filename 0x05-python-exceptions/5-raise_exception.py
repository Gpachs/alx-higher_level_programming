#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Wrong typing, try agin please!")
    except TypeError as e:
        print(e)
