def raise_exception():
    try:
        raise TypeError("Wrong typing, try again please!")
    except TypeError as e:
        print(e)
